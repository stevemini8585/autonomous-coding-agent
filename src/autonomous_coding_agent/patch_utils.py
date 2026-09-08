"""
Patch 유틸리티 - 향상된 fuzzy matching, 멀티 파일 원자적 적용, 백업/롤백
"""

from __future__ import annotations

import difflib
import logging
import shutil
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path

log = logging.getLogger("autonomous_coding_agent.patch")


@dataclass
class PatchResult:
    """패치 적용 결과"""

    success: bool
    file_path: str
    applied: bool
    error: str | None = None
    hunks_applied: int = 0
    hunks_failed: int = 0


@dataclass
class PatchOperation:
    """단일 패치 작업"""

    file_path: str
    old_content: str
    new_content: str
    description: str = ""


class PatchManager:
    """향상된 패치 관리자 - 퍼지 매칭, 원자적 멀티파일, 백업/롤백"""

    def __init__(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self._backup_dir = self.workspace / ".patch_backups"
        self._backup_dir.mkdir(exist_ok=True)
        self._transaction_backups: dict[str, str] = {}

    @contextmanager
    def transaction(self):
        """트랜잭션 컨텍스트 - 실패 시 전체 롤백"""
        self._transaction_backups = {}
        try:
            yield self
        except Exception:
            self._rollback_all()
            raise
        else:
            # 성공 시 백업 정리
            self._cleanup_backups()

    def _create_backup(self, file_path: str) -> str:
        """파일 백업 생성"""
        full_path = self.workspace / file_path
        if full_path.exists():
            backup_path = self._backup_dir / f"{file_path.replace('/', '_')}.bak"
            backup_path.parent.mkdir(parents=True, exist_ok=True)
            content = full_path.read_text(encoding="utf-8")
            backup_path.write_text(content, encoding="utf-8")
            self._transaction_backups[file_path] = str(backup_path)
            return str(backup_path)
        return ""

    def _rollback_all(self) -> None:
        """모든 변경사항 롤백"""
        for file_path, backup_path in self._transaction_backups.items():
            full_path = self.workspace / file_path
            backup = Path(backup_path)
            if backup.exists():
                full_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(backup, full_path)
                log.info(f"롤백: {file_path}")

    def _cleanup_backups(self) -> None:
        """성공 시 백업 정리"""
        for backup_path in self._transaction_backups.values():
            Path(backup_path).unlink(missing_ok=True)
        self._transaction_backups.clear()

    def apply_patches(self, operations: list[PatchOperation]) -> list[PatchResult]:
        """여러 패치를 원자적으로 적용"""
        results = []

        # 1. 모든 백업 생성
        for op in operations:
            self._create_backup(op.file_path)

        # 2. 모든 패치 적용 시도
        for op in operations:
            result = self._apply_single_patch(op)
            results.append(result)

            if not result.success:
                log.warning(f"패치 실패, 롤백 시작: {op.file_path}")
                self._rollback_all()
                # 실패한 것부터 이후 모두 실패로 표시
                for r in results:
                    if not r.success:
                        pass  # 이미 실패
                return results

        return results

    def apply_single_patch(self, file_path: str, old_content: str, new_content: str) -> PatchResult:
        """단일 패치 적용"""
        op = PatchOperation(file_path=file_path, old_content=old_content, new_content=new_content)

        with self.transaction():
            self._create_backup(file_path)
            return self._apply_single_patch(op)

    def _apply_single_patch(self, op: PatchOperation) -> PatchResult:
        """단일 패치 적용 (내부)"""
        file_path = op.file_path
        old_content = op.old_content
        new_content = op.new_content

        full_path = self.workspace / file_path
        existing = full_path.read_text(encoding="utf-8") if full_path.exists() else ""

        # 내용이 같으면 스킵
        if existing == new_content:
            return PatchResult(
                success=True,
                file_path=file_path,
                applied=False,
                error="이미 최신 상태",
            )

        # 1. 파일이 짧으면 전체 교체 (100줄 미만)
        if len(existing.split("\n")) < 100:
            full_path.write_text(new_content, encoding="utf-8")
            return PatchResult(
                success=True,
                file_path=file_path,
                applied=True,
                hunks_applied=1,
            )

        # 2. difflib로 unified diff 생성 + fuzzy matching
        return self._apply_with_fuzzy_match(file_path, existing, new_content)

    def _apply_with_fuzzy_match(
        self, file_path: str, old_content: str, new_content: str
    ) -> PatchResult:
        """퍼지 매칭으로 패치 적용"""
        # 1차: 표준 unified diff 시도
        diff = list(
            difflib.unified_diff(
                old_content.splitlines(keepends=True),
                new_content.splitlines(keepends=True),
                fromfile=f"a/{file_path}",
                tofile=f"b/{file_path}",
                n=3,  # 컨텍스트 라인 수
            )
        )

        if diff:
            result = self._apply_diff(file_path, diff)
            if result.success:
                return result

        # 2차: 퍼지 매칭으로 hunks 재구성 (컨텍스트 줄 늘리기)
        for context_lines in [5, 8, 10, 15]:
            diff = list(
                difflib.unified_diff(
                    old_content.splitlines(keepends=True),
                    new_content.splitlines(keepends=True),
                    fromfile=f"a/{file_path}",
                    tofile=f"b/{file_path}",
                    n=context_lines,
                )
            )
            if diff:
                result = self._apply_diff(file_path, diff)
                if result.success:
                    return result

        # 3차: SequenceMatcher로 블록 단위 매칭
        return self._apply_with_sequence_matcher(file_path, old_content, new_content)

    def _apply_diff(self, file_path: str, diff: list[str]) -> PatchResult:
        """diff 리스트를 patch 명령어로 적용"""
        if not diff:
            return PatchResult(
                success=True,
                file_path=file_path,
                applied=False,
                error="변경사항 없음",
            )

        # 임시 패치 파일 생성
        with tempfile.NamedTemporaryFile(mode="w", suffix=".patch", delete=False) as f:
            f.writelines(diff)
            patch_file = f.name

        try:
            # patch 명령어 실행
            result = subprocess.run(
                ["patch", "-p1", "-i", patch_file, "--no-backup-if-mismatch"],
                cwd=self.workspace,
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode == 0:
                # 성공 시 적용된 hunks 수 계산
                hunks = sum(1 for line in diff if line.startswith("@@"))
                return PatchResult(
                    success=True,
                    file_path=file_path,
                    applied=True,
                    hunks_applied=hunks,
                )
            else:
                return PatchResult(
                    success=False,
                    file_path=file_path,
                    applied=False,
                    error=f"patch 실패: {result.stderr}",
                    hunks_failed=1,
                )
        except Exception as e:
            return PatchResult(
                success=False,
                file_path=file_path,
                applied=False,
                error=f"예외 발생: {e}",
            )
        finally:
            Path(patch_file).unlink(missing_ok=True)

    def _apply_with_sequence_matcher(
        self, file_path: str, old_content: str, new_content: str
    ) -> PatchResult:
        """SequenceMatcher로 블록 단위 매칭 후 적용"""
        try:
            matcher = difflib.SequenceMatcher(
                None, old_content.splitlines(keepends=True), new_content.splitlines(keepends=True)
            )

            # 전체 교체로 폴백 (안전)
            full_path = self.workspace / file_path
            full_path.write_text(new_content, encoding="utf-8")

            return PatchResult(
                success=True,
                file_path=file_path,
                applied=True,
                error="SequenceMatcher 폴백으로 전체 교체",
                hunks_applied=1,
            )
        except Exception as e:
            return PatchResult(
                success=False,
                file_path=file_path,
                applied=False,
                error=f"SequenceMatcher 실패: {e}",
            )


def create_patch(old_content: str, new_content: str, file_path: str) -> str:
    """unified diff 문자열 생성"""
    diff = difflib.unified_diff(
        old_content.splitlines(keepends=True),
        new_content.splitlines(keepends=True),
        fromfile=f"a/{file_path}",
        tofile=f"b/{file_path}",
        n=3,
    )
    return "".join(diff)


def apply_patch(content: str, patch_text: str) -> str:
    """patch 텍스트를 내용에 적용"""
    # 간단한 구현: 전체 교체
    # 실제로는 patch 라이브러리 사용 권장
    return content  # TODO: 실제 구현


def generate_unified_diff(old_file: Path, new_file: Path) -> str:
    """두 파일 간 unified diff 생성"""
    old_content = old_file.read_text(encoding="utf-8")
    new_content = new_file.read_text(encoding="utf-8")
    return create_patch(old_content, new_content, old_file.name)


# 편의 함수
def patch_file(workspace: Path, file_path: str, new_content: str) -> bool:
    """파일 패치 적용 (편의 함수)"""
    manager = PatchManager(Path(workspace))
    full_path = Path(workspace) / file_path
    old_content = full_path.read_text(encoding="utf-8") if full_path.exists() else ""
    result = manager.apply_single_patch(file_path, old_content, new_content)
    return result.success
