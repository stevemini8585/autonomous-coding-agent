"""
벡터 임베딩 기반 지능형 패턴 메모리
- sentence-transformers로 컨텍스트/솔루션 임베딩
- FAISS/ChromaDB로 벡터 검색
- 성공/실패 패턴 가중치 학습
"""

from __future__ import annotations

import json
import logging
import pickle
import uuid
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np

try:
    from sentence_transformers import SentenceTransformer

    SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SENTENCE_TRANSFORMERS_AVAILABLE = False

try:
    import faiss

    FAISS_AVAILABLE = True
except ImportError:
    FAISS_AVAILABLE = False

try:
    import chromadb

    CHROMADB_AVAILABLE = True
except ImportError:
    CHROMADB_AVAILABLE = False

from .memory import (
    LearningAgent,
    PatternMemory,
    SessionRecord,
    SuccessPattern,
)

log = logging.getLogger("autonomous_coding_agent.vector_memory")


@dataclass
class VectorPattern(SuccessPattern):
    """벡터 임베딩이 포함된 패턴"""

    context_embedding: list[float] | None = field(default=None, repr=False)
    solution_embedding: list[float] | None = field(default=None, repr=False)
    combined_embedding: list[float] | None = field(default=None, repr=False)
    weight: float = 1.0  # 학습된 가중치 (성공/실패 기반)
    failure_count: int = 0  # 실패 횟수
    last_failure: datetime | None = None


class VectorPatternMemory(PatternMemory):
    """벡터 임베딩 기반 패턴 메모리"""

    def __init__(
        self,
        memory_dir: str | Path | None = None,
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
        use_chroma: bool = True,
        collection_name: str = "patterns",
    ):
        super().__init__(memory_dir)

        self.model_name = model_name
        self.use_chroma = use_chroma and CHROMADB_AVAILABLE
        self.collection_name = collection_name

        # 임베딩 모델 초기화
        self.encoder = None
        if SENTENCE_TRANSFORMERS_AVAILABLE:
            try:
                self.encoder = SentenceTransformer(model_name)
                log.info(f"임베딩 모델 로드: {model_name}")
            except Exception as e:
                log.warning(f"임베딩 모델 로드 실패: {e}")

        # 벡터 DB 초기화
        self.vector_store = None
        if self.use_chroma:
            self._init_chroma()
        elif FAISS_AVAILABLE:
            self._init_faiss()

        # 벡터 패턴 저장소 (기존 dict 확장)
        self.vector_patterns: dict[str, VectorPattern] = {}
        self._load_vectors()

    def _init_chroma(self) -> None:
        """ChromaDB 초기화"""
        try:
            chroma_dir = self.memory_dir / "chroma"
            chroma_dir.mkdir(exist_ok=True)

            self.chroma_client = chromadb.PersistentClient(path=str(chroma_dir))
            self.vector_store = self.chroma_client.get_or_create_collection(
                name=self.collection_name, metadata={"hnsw:space": "cosine"}
            )
            log.info("ChromaDB 초기화 완료")
        except Exception as e:
            log.warning(f"ChromaDB 초기화 실패, FAISS로 폴백: {e}")
            self.use_chroma = False

    def _init_faiss(self) -> None:
        """FAISS 인덱스 초기화"""
        try:
            self.faiss_index = faiss.IndexFlatIP(384)  # MiniLM-L6-v2 = 384 dim
            self.faiss_id_map = {}  # idx -> pattern_id
            log.info("FAISS 인덱스 초기화 완료")
        except Exception as e:
            log.warning(f"FAISS 초기화 실패: {e}")
            self.faiss_index = None

    def _load_vectors(self) -> None:
        """벡터 패턴 로드"""
        vector_file = self.memory_dir / "vector_patterns.json"
        if vector_file.exists():
            try:
                data = json.loads(vector_file.read_text(encoding="utf-8"))
                for p in data:
                    pattern = VectorPattern(
                        pattern_id=p["pattern_id"],
                        pattern_type=p["pattern_type"],
                        context=p["context"],
                        solution=p["solution"],
                        success_metrics=p["success_metrics"],
                        created_at=datetime.fromisoformat(p["created_at"]),
                        use_count=p.get("use_count", 0),
                        last_used=(
                            datetime.fromisoformat(p["last_used"]) if p.get("last_used") else None
                        ),
                        tags=p.get("tags", []),
                        weight=p.get("weight", 1.0),
                        failure_count=p.get("failure_count", 0),
                        last_failure=(
                            datetime.fromisoformat(p["last_failure"])
                            if p.get("last_failure")
                            else None
                        ),
                    )
                    # 임베딩 복원
                    if "context_embedding" in p:
                        pattern.context_embedding = p["context_embedding"]
                    if "solution_embedding" in p:
                        pattern.solution_embedding = p["solution_embedding"]
                    if "combined_embedding" in p:
                        pattern.combined_embedding = p["combined_embedding"]

                    self.vector_patterns[pattern.pattern_id] = pattern

                # 벡터 인덱스 재구성
                self._rebuild_vector_index()
                log.info(f"벡터 패턴 로드: {len(self.vector_patterns)}개")
            except Exception as e:
                log.warning(f"벡터 패턴 로드 실패: {e}")

    def _rebuild_vector_index(self) -> None:
        """벡터 인덱스 재구성"""
        if not self.vector_patterns:
            return

        embeddings = []
        pattern_ids = []

        for pid, pattern in self.vector_patterns.items():
            if pattern.combined_embedding is not None:
                embeddings.append(pattern.combined_embedding)
                pattern_ids.append(pid)

        if not embeddings:
            return

        embeddings_array = np.array(embeddings, dtype=np.float32)

        if self.use_chroma and self.vector_store:
            # ChromaDB는 자동 관리
            pass
        elif self.faiss_index is not None:
            self.faiss_index.reset()
            # 정규화 후 내적 = 코사인 유사도
            faiss.normalize_L2(embeddings_array)
            self.faiss_index.add(embeddings_array)
            self.faiss_id_map = dict(enumerate(pattern_ids))

    def _encode_text(self, text: str) -> list[float]:
        """텍스트를 임베딩으로 변환"""
        if self.encoder is None:
            return []
        try:
            embedding = self.encoder.encode(text, normalize_embeddings=True)
            return embedding.tolist()
        except Exception as e:
            log.warning(f"임베딩 생성 실패: {e}")
            return []

    def _create_combined_text(self, context: dict[str, Any], solution: dict[str, Any]) -> str:
        """컨텍스트 + 솔루션을 결합한 텍스트 생성"""
        parts = []

        # 컨텍스트
        for k, v in context.items():
            if isinstance(v, (str, int, float)):
                parts.append(f"{k}: {v}")

        # 솔루션
        for k, v in solution.items():
            if isinstance(v, (str, int, float)):
                parts.append(f"{k}: {v}")
            elif isinstance(v, list):
                parts.append(f"{k}: {', '.join(str(x) for x in v)}")

        return " | ".join(parts)

    def _compute_embeddings(
        self, context: dict[str, Any], solution: dict[str, Any]
    ) -> tuple[list[float], list[float], list[float]]:
        """컨텍스트, 솔루션, 결합 임베딩 계산"""
        context_text = " | ".join(
            f"{k}: {v}" for k, v in context.items() if isinstance(v, (str, int, float))
        )
        solution_text = " | ".join(
            f"{k}: {v}" for k, v in solution.items() if isinstance(v, (str, int, float))
        )
        combined_text = f"Context: {context_text} | Solution: {solution_text}"

        context_emb = self._encode_text(context_text)
        solution_emb = self._encode_text(solution_text)
        combined_emb = self._encode_text(combined_text)

        return context_emb, solution_emb, combined_emb

    def store_pattern(
        self,
        pattern_type: str,
        context: dict[str, Any],
        solution: dict[str, Any],
        success_metrics: dict[str, float],
        tags: list[str] | None = None,
    ) -> str:
        """벡터 임베딩과 함께 패턴 저장"""
        # 기본 저장 (부모 클래스)
        pattern_id = super().store_pattern(pattern_type, context, solution, success_metrics, tags)

        # 벡터 패턴 생성
        if self.encoder is not None:
            context_emb, solution_emb, combined_emb = self._compute_embeddings(context, solution)

            # 기존 패턴을 VectorPattern으로 업그레이드
            base_pattern = self.patterns[pattern_id]
            vector_pattern = VectorPattern(
                pattern_id=base_pattern.pattern_id,
                pattern_type=base_pattern.pattern_type,
                context=base_pattern.context,
                solution=base_pattern.solution,
                success_metrics=base_pattern.success_metrics,
                created_at=base_pattern.created_at,
                use_count=base_pattern.use_count,
                last_used=base_pattern.last_used,
                tags=base_pattern.tags,
                context_embedding=context_emb,
                solution_embedding=solution_emb,
                combined_embedding=combined_emb,
                weight=1.0,
            )

            self.vector_patterns[pattern_id] = vector_pattern

            # 벡터 인덱스에 추가
            if self.use_chroma and self.vector_store:
                self.vector_store.add(
                    ids=[pattern_id],
                    embeddings=[combined_emb],
                    metadatas=[
                        {
                            "pattern_type": pattern_type,
                            "tags": ",".join(tags or []),
                            "success_rate": success_metrics.get("success_rate", 0),
                            "use_count": 0,
                        }
                    ],
                    documents=[self._create_combined_text(context, solution)],
                )
            elif self.faiss_index is not None and combined_emb:
                emb_array = np.array([combined_emb], dtype=np.float32)
                faiss.normalize_L2(emb_array)
                self.faiss_index.add(emb_array)
                self.faiss_id_map[self.faiss_index.ntotal - 1] = pattern_id

            self._save_vectors()

        return pattern_id

    def _save_vectors(self) -> None:
        """벡터 패턴 저장"""
        vector_file = self.memory_dir / "vector_patterns.json"
        try:
            data = []
            for p in self.vector_patterns.values():
                data.append(
                    {
                        "pattern_id": p.pattern_id,
                        "pattern_type": p.pattern_type,
                        "context": p.context,
                        "solution": p.solution,
                        "success_metrics": p.success_metrics,
                        "created_at": p.created_at.isoformat(),
                        "use_count": p.use_count,
                        "last_used": p.last_used.isoformat() if p.last_used else None,
                        "tags": p.tags,
                        "weight": p.weight,
                        "failure_count": p.failure_count,
                        "last_failure": p.last_failure.isoformat() if p.last_failure else None,
                        "context_embedding": p.context_embedding,
                        "solution_embedding": p.solution_embedding,
                        "combined_embedding": p.combined_embedding,
                    }
                )
            vector_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            log.error(f"벡터 패턴 저장 실패: {e}")

    def find_patterns_vector(
        self,
        query_context: dict[str, Any],
        query_solution: dict[str, Any] | None = None,
        pattern_type: str | None = None,
        min_weight: float = 0.3,
        limit: int = 5,
    ) -> list[VectorPattern]:
        """벡터 유사도 기반 패턴 검색"""
        if self.encoder is None or not self.vector_patterns:
            # 폴백: 기존 키워드 기반 검색
            return self.find_patterns(
                pattern_type=pattern_type,
                context=query_context,
                limit=limit,
            )

        # 쿼리 임베딩 생성
        query_text = self._create_combined_text(query_context, query_solution or {})
        query_emb = self._encode_text(query_text)

        if not query_emb:
            return self.find_patterns(pattern_type=pattern_type, context=query_context, limit=limit)

        results = []

        if self.use_chroma and self.vector_store:
            # ChromaDB 검색
            where_filter = {}
            if pattern_type:
                where_filter["pattern_type"] = pattern_type

            try:
                result = self.vector_store.query(
                    query_embeddings=[query_emb],
                    n_results=limit * 2,  # 필터링 위해 여유분
                    where=where_filter if where_filter else None,
                )

                for pid, score in zip(result["ids"][0], result["distances"][0]):
                    if pid in self.vector_patterns:
                        pattern = self.vector_patterns[pid]
                        if pattern.weight >= min_weight:
                            pattern._similarity = 1.0 - score  # cosine distance -> similarity
                            results.append(pattern)
            except Exception as e:
                log.warning(f"ChromaDB 검색 실패: {e}")

        elif self.faiss_index is not None and self.faiss_index.ntotal > 0:
            # FAISS 검색
            query_array = np.array([query_emb], dtype=np.float32)
            faiss.normalize_L2(query_array)

            k = min(limit * 2, self.faiss_index.ntotal)
            scores, indices = self.faiss_index.search(query_array, k)

            for score, idx in zip(scores[0], indices[0]):
                if idx in self.faiss_id_map:
                    pid = self.faiss_id_map[idx]
                    if pid in self.vector_patterns:
                        pattern = self.vector_patterns[pid]
                        if pattern.weight >= min_weight:
                            pattern._similarity = float(score)
                            results.append(pattern)

        # 타입 필터
        if pattern_type:
            results = [p for p in results if p.pattern_type == pattern_type]

        # 유사도 + 가중치 + 사용 횟수로 정렬
        results.sort(
            key=lambda p: (getattr(p, "_similarity", 0) * p.weight + p.use_count * 0.01),
            reverse=True,
        )

        return results[:limit]

    def update_pattern_weight(
        self, pattern_id: str, success: bool, metrics: dict[str, float] | None = None
    ) -> None:
        """패턴 가중치 업데이트 (강화학습 스타일)"""
        if pattern_id not in self.vector_patterns:
            return

        pattern = self.vector_patterns[pattern_id]

        if success:
            # 성공: 가중치 증가 (상한 2.0)
            pattern.weight = min(2.0, pattern.weight * 1.1)
            pattern.use_count += 1
            pattern.last_used = datetime.now()

            # 성공 메트릭 업데이트
            if metrics:
                for k, v in metrics.items():
                    if k in pattern.success_metrics:
                        # 지수 이동 평균
                        pattern.success_metrics[k] = 0.9 * pattern.success_metrics[k] + 0.1 * v
                    else:
                        pattern.success_metrics[k] = v
        else:
            # 실패: 가중치 감소 (하한 0.1), 실패 횟수 증가
            pattern.weight = max(0.1, pattern.weight * 0.8)
            pattern.failure_count += 1
            pattern.last_failure = datetime.now()

        self._save_vectors()
        log.info(f"패턴 가중치 업데이트: {pattern_id} -> {pattern.weight:.2f}")

    def get_pattern_recommendations(
        self,
        context: dict[str, Any],
        top_k: int = 3,
    ) -> list[dict[str, Any]]:
        """현재 컨텍스트에 맞는 패턴 추천 (상세 정보 포함)"""
        patterns = self.find_patterns_vector(context, limit=top_k)

        recommendations = []
        for p in patterns:
            recommendations.append(
                {
                    "pattern_id": p.pattern_id,
                    "pattern_type": p.pattern_type,
                    "similarity": getattr(p, "_similarity", 0),
                    "weight": p.weight,
                    "use_count": p.use_count,
                    "success_rate": p.success_metrics.get("success_rate", 0),
                    "solution_summary": self._summarize_solution(p.solution),
                    "tags": p.tags,
                    "confidence": min(1.0, getattr(p, "_similarity", 0) * p.weight),
                }
            )

        return recommendations

    def _summarize_solution(self, solution: dict[str, Any]) -> str:
        """솔루션 요약"""
        parts = []
        for k, v in solution.items():
            if isinstance(v, bool) and v:
                parts.append(k)
            elif isinstance(v, (str, int, float)):
                parts.append(f"{k}={v}")
        return ", ".join(parts)[:100]


class VectorLearningAgent(LearningAgent):
    """벡터 메모리 기반 학습 에이전트"""

    def __init__(self, memory: VectorPatternMemory):
        self.memory = memory
        self.current_session: SessionRecord | None = None

    def end_session(self, success: bool, metrics: dict[str, Any] | None = None) -> None:
        """세션 종료 및 패턴 가중치 업데이트"""
        super().end_session(success, metrics)

        # 최근 생성된 패턴들의 가중치 업데이트
        if self.current_session and self.current_session.patterns_created:
            for pattern_id in self.current_session.patterns_created:
                self.memory.update_pattern_weight(pattern_id, success, metrics)

    def get_smart_recommendations(self, context: dict[str, Any]) -> list[dict[str, Any]]:
        """스마트 추천 (벡터 검색 + 가중치)"""
        return self.memory.get_pattern_recommendations(context, top_k=5)


def create_vector_memory(memory_dir: str | Path | None = None) -> VectorPatternMemory:
    """벡터 메모리 팩토리"""
    return VectorPatternMemory(memory_dir)


def create_vector_learning_agent(memory: VectorPatternMemory) -> VectorLearningAgent:
    """벡터 학습 에이전트 팩토리"""
    return VectorLearningAgent(memory)
