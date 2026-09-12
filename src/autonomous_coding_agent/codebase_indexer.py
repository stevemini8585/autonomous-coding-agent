"""
코드베이스 RAG 인덱서 + 컨텍스트 빌더 (Week 3-2)
- 실제 소스 파일(*.py)을 임베딩하여 ChromaDB/FAISS에 인덱싱
- 목표(이슈 설명) 기반으로 관련 파일 Top-K 검색
- LLMCoder에 주입할 컨텍스트(파일 내용+심볼+요약) 자동 구성
- 증분 업데이트 지원 (mtime 기반 변경 감지)
"""

from __future__ import annotations

import contextlib
import hashlib
import json
import logging
import os
import pickle
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import numpy as np

try:
    from sentence_transformers import SentenceTransformer

    SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SENTENCE_TRANSFORMERS_AVAILABLE = False

try:
    import chromadb

    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False

try:
    import faiss

    FAISS_AVAILABLE = True
except ImportError:
    FAISS_AVAILABLE = False

from .llm_client import chat
from .models import CodeSymbol, ExploreResult, FileInfo

log = logging.getLogger("autonomous_coding_agent.codebase_indexer")


@dataclass
class IndexedFile:
    """인덱싱된 파일 메타데이터"""

    path: str  # 상대 경로
    mtime: float  # 수정 시간 (변경 감지용)
    content_hash: str  # 내용 해시 (중복 방지)
    symbols: list[CodeSymbol]  # 추출된 심볼
    summary: str  # LLM 생성 요약 (선택)
    embedding: list[float] | None = None  # 파일 전체 임베딩


@dataclass
class SearchResult:
    """검색 결과"""

    file: IndexedFile
    score: float  # 유사도 (cosine similarity, 0~1)
    matched_symbols: list[CodeSymbol] = field(default_factory=list)


class CodebaseIndexer:
    """
    프로젝트 소스 코드 임베딩 인덱서.
    - ChromaDB 우선, FAISS 폴백
    - 증분 업데이트: mtime + content_hash로 변경된 파일만 재임베딩
    - 컬렉션 분리: "codebase_files" (파일 단위), "codebase_symbols" (심볼 단위)
    """

    DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    EMBED_DIM = 384  # MiniLM-L6-v2
    CHUNK_SIZE = 1500  # 문자 단위 청크 크기
    CHUNK_OVERLAP = 200

    def __init__(
        self,
        workspace: Path,
        index_dir: Path | None = None,
        model_name: str = DEFAULT_MODEL,
        use_chroma: bool = True,
    ):
        self.workspace = Path(workspace).resolve()
        self.index_dir = (index_dir or self.workspace / ".codebase_index").resolve()
        self.index_dir.mkdir(parents=True, exist_ok=True)

        self.model_name = model_name
        self.use_chroma = use_chroma and CHROMADB_AVAILABLE

        # 임베딩 모델
        self.encoder = None
        if SENTENCE_TRANSFORMERS_AVAILABLE:
            try:
                self.encoder = SentenceTransformer(model_name)
                log.info(f"코드베이스 인덱서 임베딩 모델 로드: {model_name}")
            except Exception as e:
                log.warning(f"임베딩 모델 로드 실패: {e}")

        # 벡터 스토어
        self.chroma_client = None
        self.files_collection = None
        self.symbols_collection = None
        self.faiss_files_index = None
        self.faiss_symbols_index = None
        self.faiss_files_id_map = {}
        self.faiss_symbols_id_map = {}

        # 메타데이터 캐시
        self.file_meta: dict[str, IndexedFile] = {}  # path -> IndexedFile
        self.symbol_meta: dict[str, tuple[str, CodeSymbol]] = {}  # symbol_id -> (file_path, symbol)

        if self.use_chroma:
            self._init_chroma()
        elif FAISS_AVAILABLE:
            self._init_faiss()

        self._load_meta()

    def _init_chroma(self) -> None:
        try:
            chroma_dir = self.index_dir / "chroma"
            chroma_dir.mkdir(exist_ok=True)
            self.chroma_client = chromadb.PersistentClient(path=str(chroma_dir))

            self.files_collection = self.chroma_client.get_or_create_collection(
                name="codebase_files",
                metadata={"hnsw:space": "cosine"},
            )
            self.symbols_collection = self.chroma_client.get_or_create_collection(
                name="codebase_symbols",
                metadata={"hnsw:space": "cosine"},
            )
            log.info("ChromaDB 코드베이스 인덱스 초기화 완료")
        except Exception as e:
            log.warning(f"ChromaDB 초기화 실패, FAISS로 폴백: {e}")
            self.use_chroma = False

    def _init_faiss(self) -> None:
        try:
            self.faiss_files_index = faiss.IndexFlatIP(self.EMBED_DIM)
            self.faiss_symbols_index = faiss.IndexFlatIP(self.EMBED_DIM)
            log.info("FAISS 코드베이스 인덱스 초기화 완료")
        except Exception as e:
            log.warning(f"FAISS 초기화 실패: {e}")
            self.faiss_files_index = None
            self.faiss_symbols_index = None

    def _load_meta(self) -> None:
        """메타데이터 로드 (피클 + JSON)"""
        meta_file = self.index_dir / "file_meta.json"
        if meta_file.exists():
            try:
                data = json.loads(meta_file.read_text(encoding="utf-8"))
                for item in data:
                    symbols = [CodeSymbol(**s) for s in item.get("symbols", [])]
                    self.file_meta[item["path"]] = IndexedFile(
                        path=item["path"],
                        mtime=item["mtime"],
                        content_hash=item["content_hash"],
                        symbols=symbols,
                        summary=item.get("summary", ""),
                        embedding=item.get("embedding"),
                    )
                log.info(f"파일 메타 로드: {len(self.file_meta)}개")
            except Exception as e:
                log.warning(f"메타 로드 실패: {e}")

        # 심볼 메타도 로드
        sym_file = self.index_dir / "symbol_meta.json"
        if sym_file.exists():
            try:
                data = json.loads(sym_file.read_text(encoding="utf-8"))
                for item in data:
                    sym = CodeSymbol(**item["symbol"])
                    self.symbol_meta[item["symbol_id"]] = (item["file_path"], sym)
            except Exception as e:
                log.warning(f"심볼 메타 로드 실패: {e}")

    def _save_meta(self) -> None:
        """메타데이터 저장"""
        # 파일 메타
        meta_file = self.index_dir / "file_meta.json"
        data = []
        for f in self.file_meta.values():
            data.append(
                {
                    "path": f.path,
                    "mtime": f.mtime,
                    "content_hash": f.content_hash,
                    "symbols": [s.__dict__ for s in f.symbols],
                    "summary": f.summary,
                    "embedding": f.embedding,
                }
            )
        meta_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

        # 심볼 메타
        sym_file = self.index_dir / "symbol_meta.json"
        data = []
        for sym_id, (fpath, sym) in self.symbol_meta.items():
            data.append(
                {
                    "symbol_id": sym_id,
                    "file_path": fpath,
                    "symbol": sym.__dict__,
                }
            )
        sym_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    # ------------------------------------------------------------
    # 공개 API
    # ------------------------------------------------------------
    def build_index(self, force: bool = False) -> dict[str, int]:
        """전체 인덱스 빌드/증분 업데이트.
        Returns: {"indexed": n, "updated": n, "removed": n, "skipped": n}"""
        if self.encoder is None:
            log.warning("임베딩 모델 없음 — 인덱스 빌드 생략")
            return {"indexed": 0, "updated": 0, "removed": 0, "skipped": 0}

        py_files = list(self.workspace.rglob("*.py"))
        # __pycache__, .autonomous_*, 테스트 부산물 제외
        exclude_dirs = {
            ".autonomous_backups",
            ".autonomous_memory",
            ".autonomous_state",
            ".patch_backups",
            "__pycache__",
            ".git",
            "mutants",
            ".pytest_cache",
        }
        py_files = [f for f in py_files if not any(p in exclude_dirs for p in f.parts)]

        stats = {"indexed": 0, "updated": 0, "removed": 0, "skipped": 0}
        current_paths = set()

        for fpath in py_files:
            rel = fpath.relative_to(self.workspace).as_posix()
            current_paths.add(rel)

            try:
                stat = fpath.stat()
                content = fpath.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue

            content_hash = hashlib.md5(content.encode()).hexdigest()
            existing = self.file_meta.get(rel)

            # 변경 감지: force 또는 mtime/hash 변경 시 재인덱싱
            if (
                not force
                and existing
                and existing.mtime >= stat.st_mtime
                and existing.content_hash == content_hash
            ):
                stats["skipped"] += 1
                continue

            # 심볼 추출 (탐색기 재사용)
            from .explorer import CodeExplorer

            explorer = CodeExplorer(self.workspace)
            # 단일 파일만 탐색 (target_paths 지원으로 몽키패치 불필요)
            explore_result = explorer.explore([rel])

            symbols = explore_result.symbols if explore_result else []

            # 파일 임베딩 생성
            embedding = self._embed_file(content)

            # 메타 업데이트
            indexed = IndexedFile(
                path=rel,
                mtime=stat.st_mtime,
                content_hash=content_hash,
                symbols=symbols,
                summary="",  # 필요 시 LLM 요약 추가
                embedding=embedding,
            )
            is_new = rel not in self.file_meta
            self.file_meta[rel] = indexed

            # 벡터 스토어 업데이트
            self._upsert_file_vector(rel, content, embedding, symbols, is_new)

            # 심볼별 인덱싱
            for sym in symbols:
                sym_id = f"{rel}::{sym.name}"
                sym_embedding = self._embed_text(f"{sym.name} {sym.type} {sym.file_path}")
                self._upsert_symbol_vector(sym_id, rel, sym, sym_embedding, is_new)

            stats["indexed" if is_new else "updated"] += 1

        # 삭제된 파일 정리
        removed = set(self.file_meta.keys()) - current_paths
        for rel in removed:
            self._remove_file(rel)
            stats["removed"] += 1

        self._save_meta()
        log.info(f"인덱스 빌드 완료: {stats}")
        return stats

    def _embed_file(self, content: str) -> list[float] | None:
        """파일 내용을 청크로 나눠 임베딩 후 평균 풀링"""
        if self.encoder is None:
            return None
        chunks = self._chunk_text(content)
        if not chunks:
            return None
        embeddings = self.encoder.encode(chunks, normalize_embeddings=True)
        mean_emb = np.mean(embeddings, axis=0)
        return mean_emb.tolist()

    def _embed_text(self, text: str) -> list[float] | None:
        if self.encoder is None:
            return None
        emb = self.encoder.encode([text], normalize_embeddings=True)
        return emb[0].tolist()

    def _chunk_text(self, text: str) -> list[str]:
        """오버랩 있는 청크 분할"""
        chunks = []
        start = 0
        while start < len(text):
            end = min(start + self.CHUNK_SIZE, len(text))
            chunks.append(text[start:end])
            if end == len(text):
                break
            start = end - self.CHUNK_OVERLAP
        return chunks

    def _upsert_file_vector(
        self, rel: str, content: str, embedding: list[float] | None, symbols: list, is_new: bool
    ) -> None:
        if embedding is None:
            return
        meta = {
            "path": rel,
            "symbols": ",".join(s.name for s in symbols[:20]),
            "symbol_count": len(symbols),
        }
        if self.use_chroma and self.files_collection:
            self.files_collection.upsert(
                ids=[rel],
                embeddings=[embedding],
                documents=[content[:8000]],  # 문서 저장 (검색 시 표시용)
                metadatas=[meta],
            )
        elif self.faiss_files_index is not None:
            emb_arr = np.array([embedding], dtype=np.float32)
            faiss.normalize_L2(emb_arr)
            if is_new:
                idx = self.faiss_files_index.ntotal
                self.faiss_files_id_map[idx] = rel
                self.faiss_files_index.add(emb_arr)
            else:
                # FAISS는 삭제 불가 → 재빌드 플래그 관리 필요 (간단히 무시)
                pass

    def _upsert_symbol_vector(
        self, sym_id: str, file_path: str, symbol, embedding: list[float] | None, is_new: bool
    ) -> None:
        if embedding is None:
            return
        meta = {
            "file_path": file_path,
            "symbol_name": symbol.name,
            "symbol_type": symbol.type,
            "line_start": symbol.line_start,
            "line_end": symbol.line_end,
        }
        self.symbol_meta[sym_id] = (file_path, symbol)
        if self.use_chroma and self.symbols_collection:
            self.symbols_collection.upsert(
                ids=[sym_id],
                embeddings=[embedding],
                documents=[f"{symbol.name} ({symbol.type}) in {file_path}"],
                metadatas=[meta],
            )
        elif self.faiss_symbols_index is not None:
            emb_arr = np.array([embedding], dtype=np.float32)
            faiss.normalize_L2(emb_arr)
            if is_new:
                idx = self.faiss_symbols_index.ntotal
                self.faiss_symbols_id_map[idx] = sym_id
                self.faiss_symbols_index.add(emb_arr)

    def _remove_file(self, rel: str) -> None:
        if rel in self.file_meta:
            del self.file_meta[rel]
        # ChromaDB에서 삭제
        if self.use_chroma and self.files_collection:
            with contextlib.suppress(Exception):
                self.files_collection.delete(ids=[rel])
        # 심볼도 정리
        to_del = [sid for sid, (fp, _) in self.symbol_meta.items() if fp == rel]
        for sid in to_del:
            del self.symbol_meta[sid]
            if self.use_chroma and self.symbols_collection:
                with contextlib.suppress(Exception):
                    self.symbols_collection.delete(ids=[sid])

    def search_files(self, query: str, k: int = 10, min_score: float = 0.2) -> list[SearchResult]:
        """목표 쿼리로 관련 파일 검색"""
        if self.encoder is None or not self.file_meta:
            return []

        query_emb = self._embed_text(query)
        if query_emb is None:
            return []

        results = []

        if self.use_chroma and self.files_collection:
            try:
                res = self.files_collection.query(
                    query_embeddings=[query_emb],
                    n_results=min(k * 2, len(self.file_meta)),
                )
                for fid, score, doc in zip(res["ids"][0], res["distances"][0], res["documents"][0]):
                    sim = 1.0 - score  # cosine distance -> similarity
                    if sim >= min_score and fid in self.file_meta:
                        f = self.file_meta[fid]
                        results.append(SearchResult(file=f, score=sim))
            except Exception as e:
                log.warning(f"ChromaDB 파일 검색 실패: {e}")

        elif self.faiss_files_index is not None and self.faiss_files_index.ntotal > 0:
            query_arr = np.array([query_emb], dtype=np.float32)
            faiss.normalize_L2(query_arr)
            k_search = min(k * 2, self.faiss_files_index.ntotal)
            scores, indices = self.faiss_files_index.search(query_arr, k_search)
            for score, idx in zip(scores[0], indices[0]):
                if idx in self.faiss_files_id_map:
                    fid = self.faiss_files_id_map[idx]
                    if fid in self.file_meta:
                        sim = float(score)
                        if sim >= min_score:
                            results.append(SearchResult(file=self.file_meta[fid], score=sim))

        # 점수순 정렬
        results.sort(key=lambda r: r.score, reverse=True)
        return results[:k]

    def search_symbols(
        self, query: str, k: int = 10, min_score: float = 0.25
    ) -> list[tuple[CodeSymbol, float, str]]:
        """심볼 단위 검색 (더 정밀)"""
        if self.encoder is None or not self.symbol_meta:
            return []

        query_emb = self._embed_text(query)
        if query_emb is None:
            return []

        results = []

        if self.use_chroma and self.symbols_collection:
            try:
                res = self.symbols_collection.query(
                    query_embeddings=[query_emb],
                    n_results=min(k * 2, len(self.symbol_meta)),
                )
                for sid, score, doc in zip(res["ids"][0], res["distances"][0], res["documents"][0]):
                    sim = 1.0 - score
                    if sim >= min_score and sid in self.symbol_meta:
                        fpath, sym = self.symbol_meta[sid]
                        results.append((sym, sim, fpath))
            except Exception as e:
                log.warning(f"ChromaDB 심볼 검색 실패: {e}")

        elif self.faiss_symbols_index is not None and self.faiss_symbols_index.ntotal > 0:
            query_arr = np.array([query_emb], dtype=np.float32)
            faiss.normalize_L2(query_arr)
            k_search = min(k * 2, self.faiss_symbols_index.ntotal)
            scores, indices = self.faiss_symbols_index.search(query_arr, k_search)
            for score, idx in zip(scores[0], indices[0]):
                if idx in self.faiss_symbols_id_map:
                    sid = self.faiss_symbols_id_map[idx]
                    if sid in self.symbol_meta:
                        fpath, sym = self.symbol_meta[sid]
                        sim = float(score)
                        if sim >= min_score:
                            results.append((sym, sim, fpath))

        results.sort(key=lambda x: x[1], reverse=True)
        return results[:k]

    def get_file_content(self, rel_path: str) -> str | None:
        """원본 파일 내용 읽기"""
        fpath = self.workspace / rel_path
        try:
            return fpath.read_text(encoding="utf-8")
        except OSError:
            return None

    def get_stats(self) -> dict[str, int]:
        return {
            "files": len(self.file_meta),
            "symbols": len(self.symbol_meta),
            "chroma_files": (
                self.files_collection.count() if self.use_chroma and self.files_collection else 0
            ),
            "faiss_files": self.faiss_files_index.ntotal if self.faiss_files_index else 0,
        }


class ContextBuilder:
    """
    LLMCoder에 주입할 컨텍스트 자동 구성.
    - 인덱서 검색 결과 + 탐색 결과 + 메모리 힌트 조합
    - 토큰 예산 내로 프루닝 (파일당/전체 상한)
    """

    def __init__(
        self,
        indexer: CodebaseIndexer,
        max_files: int = 8,
        max_symbols: int = 30,
        max_file_chars: int = 3000,
        max_total_chars: int = 15000,
    ):
        self.indexer = indexer
        self.max_files = max_files
        self.max_symbols = max_symbols
        self.max_file_chars = max_file_chars
        self.max_total_chars = max_total_chars

    def build_context(
        self,
        goal: str,
        explore_result: ExploreResult | None = None,
        memory_hint: str = "",
    ) -> dict[str, Any]:
        """LLMCoder 프롬프트에 들어갈 컨텍스트 구성"""
        # 1) 파일 검색
        file_results = self.indexer.search_files(goal, k=self.max_files)

        # 2) 심볼 검색 (보조)
        symbol_results = self.indexer.search_symbols(goal, k=self.max_symbols)

        # 3) 탐색 결과에서 심볼 보강
        explore_symbols = []
        if explore_result and explore_result.symbols:
            explore_symbols = explore_result.symbols[: self.max_symbols]

        # 4) 파일 내용 수집 (토큰 예산 내)
        files_context = []
        total_chars = 0
        for res in file_results:
            content = self.indexer.get_file_content(res.file.path)
            if not content:
                continue
            # 파일당 상한
            if len(content) > self.max_file_chars:
                content = content[: self.max_file_chars] + "\n# ... (truncated)"
            if total_chars + len(content) > self.max_total_chars:
                break
            files_context.append(
                {
                    "path": res.file.path,
                    "score": round(res.score, 3),
                    "symbols": [s.name for s in res.file.symbols[:10]],
                    "content": content,
                }
            )
            total_chars += len(content)

        # 5) 심볼 리스트 구성 (중복 제거)
        all_symbols = {}
        for sym, score, fpath in symbol_results:
            key = f"{fpath}::{sym.name}"
            if key not in all_symbols:
                all_symbols[key] = {"symbol": sym, "score": score, "file": fpath}
        for sym in explore_symbols:
            key = f"{sym.file_path}::{sym.name}"
            if key not in all_symbols:
                all_symbols[key] = {"symbol": sym, "score": 1.0, "file": sym.file_path}

        symbols_list = [
            {
                "name": v["symbol"].name,
                "type": v["symbol"].type,
                "file": v["file"],
                "line": v["symbol"].line_start,
                "score": round(v["score"], 3),
            }
            for v in sorted(all_symbols.values(), key=lambda x: x["score"], reverse=True)[
                : self.max_symbols
            ]
        ]

        return {
            "goal": goal,
            "memory_hint": memory_hint,
            "files": files_context,
            "symbols": symbols_list,
            "stats": {
                "files_found": len(file_results),
                "files_included": len(files_context),
                "symbols_included": len(symbols_list),
                "total_chars": total_chars,
            },
        }

    def format_for_prompt(self, ctx: dict[str, Any]) -> str:
        """컨텍스트를 프롬프트 문자열로 포맷"""
        lines = []
        if ctx.get("memory_hint"):
            lines.append(ctx["memory_hint"])
            lines.append("")

        if ctx["files"]:
            lines.append("=== 관련 파일 (유사도순) ===")
            for f in ctx["files"]:
                lines.append(f"\n--- {f['path']} (score: {f['score']}) ---")
                lines.append(f"심볼: {', '.join(f['symbols']) if f['symbols'] else '없음'}")
                lines.append(f["content"])

        if ctx["symbols"]:
            lines.append("\n=== 핵심 심볼 ===")
            for s in ctx["symbols"]:
                lines.append(
                    f"- {s['name']} ({s['type']}) @ {s['file']}:{s['line']} (score: {s['score']})"
                )

        return "\n".join(lines)


def create_codebase_indexer(workspace: Path | str, **kwargs) -> CodebaseIndexer:
    return CodebaseIndexer(Path(workspace), **kwargs)


def create_context_builder(indexer: CodebaseIndexer, **kwargs) -> ContextBuilder:
    return ContextBuilder(indexer, **kwargs)
