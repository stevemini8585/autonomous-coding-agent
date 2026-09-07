"""학습/메모리 모듈
세션 간 성공 패턴 저장/재사용
"""

from __future__ import annotations

import json
import logging
import pickle
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Optional
from collections import defaultdict

log = logging.getLogger("autonomous_coding_agent.memory")


@dataclass
class SuccessPattern:
    """성공 패턴"""
    pattern_id: str
    pattern_type: str  # code, test, fix, refactor, review
    context: dict[str, Any]  # 언어, 프레임워크, 문제 유형 등
    solution: dict[str, Any]  # 해결 방법 (코드, 테스트 케이스, 모킹 등)
    success_metrics: dict[str, float]  # 테스트 통과율, 커버리지, 실행 시간 등
    created_at: datetime = field(default_factory=datetime.now)
    use_count: int = 0
    last_used: Optional[datetime] = None
    tags: list[str] = field(default_factory=list)


@dataclass
class SessionRecord:
    """세션 기록"""
    session_id: str
    goal: str
    workspace: str
    start_time: datetime
    end_time: Optional[datetime] = None
    success: bool = False
    steps_completed: int = 0
    total_steps: int = 0
    patterns_used: list[str] = field(default_factory=list)
    patterns_created: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    metrics: dict[str, Any] = field(default_factory=dict)


class PatternMemory:
    """패턴 메모리 - 성공 패턴 저장 및 검색"""

    def __init__(self, memory_dir: str | Path = ".autonomous_memory"):
        self.memory_dir = Path(memory_dir).resolve()
        self.memory_dir.mkdir(parents=True, exist_ok=True)

        self.patterns_file = self.memory_dir / "patterns.json"
        self.sessions_file = self.memory_dir / "sessions.json"
        self.index_file = self.memory_dir / "index.pkl"

        self.patterns: dict[str, SuccessPattern] = {}
        self.sessions: list[SessionRecord] = []
        self._load()

    def _load(self) -> None:
        """메모리 로드"""
        try:
            if self.patterns_file.exists():
                data = json.loads(self.patterns_file.read_text(encoding="utf-8"))
                for p in data:
                    pattern = SuccessPattern(
                        pattern_id=p["pattern_id"],
                        pattern_type=p["pattern_type"],
                        context=p["context"],
                        solution=p["solution"],
                        success_metrics=p["success_metrics"],
                        created_at=datetime.fromisoformat(p["created_at"]),
                        use_count=p.get("use_count", 0),
                        last_used=datetime.fromisoformat(p["last_used"]) if p.get("last_used") else None,
                        tags=p.get("tags", []),
                    )
                    self.patterns[pattern.pattern_id] = pattern

            if self.sessions_file.exists():
                data = json.loads(self.sessions_file.read_text(encoding="utf-8"))
                for s in data:
                    session = SessionRecord(
                        session_id=s["session_id"],
                        goal=s["goal"],
                        workspace=s["workspace"],
                        start_time=datetime.fromisoformat(s["start_time"]),
                        end_time=datetime.fromisoformat(s["end_time"]) if s.get("end_time") else None,
                        success=s.get("success", False),
                        steps_completed=s.get("steps_completed", 0),
                        total_steps=s.get("total_steps", 0),
                        patterns_used=s.get("patterns_used", []),
                        patterns_created=s.get("patterns_created", []),
                        errors=s.get("errors", []),
                        metrics=s.get("metrics", {}),
                    )
                    self.sessions.append(session)

            log.info(f"메모리 로드 완료: 패턴 {len(self.patterns)}개, 세션 {len(self.sessions)}개")

        except Exception as e:
            log.warning(f"메모리 로드 실패: {e}")

    def _save(self) -> None:
        """메모리 저장"""
        try:
            # 패턴 저장
            patterns_data = []
            for p in self.patterns.values():
                patterns_data.append({
                    "pattern_id": p.pattern_id,
                    "pattern_type": p.pattern_type,
                    "context": p.context,
                    "solution": p.solution,
                    "success_metrics": p.success_metrics,
                    "created_at": p.created_at.isoformat(),
                    "use_count": p.use_count,
                    "last_used": p.last_used.isoformat() if p.last_used else None,
                    "tags": p.tags,
                })
            self.patterns_file.write_text(
                json.dumps(patterns_data, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )

            # 세션 저장
            sessions_data = []
            for s in self.sessions:
                sessions_data.append({
                    "session_id": s.session_id,
                    "goal": s.goal,
                    "workspace": s.workspace,
                    "start_time": s.start_time.isoformat(),
                    "end_time": s.end_time.isoformat() if s.end_time else None,
                    "success": s.success,
                    "steps_completed": s.steps_completed,
                    "total_steps": s.total_steps,
                    "patterns_used": s.patterns_used,
                    "patterns_created": s.patterns_created,
                    "errors": s.errors,
                    "metrics": s.metrics,
                })
            self.sessions_file.write_text(
                json.dumps(sessions_data, ensure_ascii=False, indent=2),
                encoding="utf-8"
            )

        except Exception as e:
            log.error(f"메모리 저장 실패: {e}")

    def store_pattern(
        self,
        pattern_type: str,
        context: dict[str, Any],
        solution: dict[str, Any],
        success_metrics: dict[str, float],
        tags: list[str] | None = None,
    ) -> str:
        """성공 패턴 저장"""
        import uuid
        pattern_id = f"{pattern_type}_{uuid.uuid4().hex[:8]}"

        pattern = SuccessPattern(
            pattern_id=pattern_id,
            pattern_type=pattern_type,
            context=context,
            solution=solution,
            success_metrics=success_metrics,
            tags=tags or [],
        )

        self.patterns[pattern_id] = pattern
        self._save()
        log.info(f"패턴 저장: {pattern_id} ({pattern_type})")
        return pattern_id

    def find_patterns(
        self,
        pattern_type: str | None = None,
        context: dict[str, Any] | None = None,
        tags: list[str] | None = None,
        min_success_rate: float = 0.8,
        limit: int = 5,
    ) -> list[SuccessPattern]:
        """패턴 검색"""
        results = []

        for pattern in self.patterns.values():
            # 타입 필터
            if pattern_type and pattern.pattern_type != pattern_type:
                continue

            # 태그 필터
            if tags and not any(t in pattern.tags for t in tags):
                continue

            # 성공률 필터
            success_rate = pattern.success_metrics.get("success_rate", 0)
            if success_rate < min_success_rate:
                continue

            # 컨텍스트 유사도 계산
            if context:
                similarity = self._calculate_similarity(pattern.context, context)
                if similarity < 0.5:  # 50% 이상 유사
                    continue
                pattern._similarity = similarity  # type: ignore
            else:
                pattern._similarity = 1.0  # type: ignore

            results.append(pattern)

        # 유사도 내림차순, 사용 횟수 내림차순 정렬
        results.sort(key=lambda p: (getattr(p, '_similarity', 0), p.use_count), reverse=True)

        return results[:limit]

    def _calculate_similarity(self, ctx1: dict[str, Any], ctx2: dict[str, Any]) -> float:
        """컨텍스트 유사도 계산 (0~1)"""
        if not ctx1 or not ctx2:
            return 0.0

        keys = set(ctx1.keys()) | set(ctx2.keys())
        if not keys:
            return 1.0

        matches = 0
        for k in keys:
            v1 = ctx1.get(k)
            v2 = ctx2.get(k)
            if v1 == v2:
                matches += 1
            elif isinstance(v1, str) and isinstance(v2, str):
                # 문자열 유사도 (간단한 포함 관계)
                if v1 in v2 or v2 in v1:
                    matches += 0.5

        return matches / len(keys)

    def use_pattern(self, pattern_id: str) -> Optional[SuccessPattern]:
        """패턴 사용 기록"""
        if pattern_id in self.patterns:
            pattern = self.patterns[pattern_id]
            pattern.use_count += 1
            pattern.last_used = datetime.now()
            self._save()
            return pattern
        return None

    def record_session(self, session: SessionRecord) -> None:
        """세션 기록"""
        self.sessions.append(session)
        self._save()

    def get_statistics(self) -> dict[str, Any]:
        """통계 조회"""
        total_patterns = len(self.patterns)
        total_sessions = len(self.sessions)
        successful_sessions = sum(1 for s in self.sessions if s.success)

        pattern_types = defaultdict(int)
        for p in self.patterns.values():
            pattern_types[p.pattern_type] += 1

        return {
            "total_patterns": total_patterns,
            "total_sessions": total_sessions,
            "successful_sessions": successful_sessions,
            "success_rate": successful_sessions / max(total_sessions, 1),
            "pattern_types": dict(pattern_types),
            "most_used_patterns": sorted(
                self.patterns.values(),
                key=lambda p: p.use_count,
                reverse=True
            )[:5],
        }


class LearningAgent:
    """학습 에이전트 - 자율 에이전트와 연동하여 패턴 학습"""

    def __init__(self, memory: PatternMemory):
        self.memory = memory
        self.current_session: Optional[SessionRecord] = None

    def start_session(self, goal: str, workspace: str) -> SessionRecord:
        """세션 시작"""
        import uuid
        session = SessionRecord(
            session_id=f"session_{uuid.uuid4().hex[:8]}",
            goal=goal,
            workspace=workspace,
            start_time=datetime.now(),
        )
        self.current_session = session
        return session

    def end_session(self, success: bool, metrics: dict[str, Any] | None = None) -> None:
        """세션 종료 및 패턴 추출"""
        if not self.current_session:
            return

        self.current_session.end_time = datetime.now()
        self.current_session.success = success
        if metrics:
            self.current_session.metrics = metrics

        # 성공한 경우 패턴 추출
        if success:
            self._extract_patterns()

        self.memory.record_session(self.current_session)
        self.current_session = None

    def _extract_patterns(self) -> None:
        """세션에서 성공 패턴 추출"""
        if not self.current_session:
            return

        # 테스트 생성 패턴
        if self.current_session.metrics.get("tests_generated", 0) > 0:
            self.memory.store_pattern(
                pattern_type="test",
                context={
                    "language": self.current_session.metrics.get("language", "python"),
                    "framework": self.current_session.metrics.get("framework"),
                    "test_framework": self.current_session.metrics.get("test_framework", "pytest"),
                },
                solution={
                    "method": "ast_based_generation",
                    "edge_cases": True,
                    "parameter_combinations": True,
                    "mocking": True,
                },
                success_metrics={
                    "success_rate": 1.0,
                    "tests_generated": self.current_session.metrics.get("tests_generated", 0),
                    "coverage": self.current_session.metrics.get("coverage", 0),
                },
                tags=["test_generation", "ast", "edge_cases"],
            )

        # PR 리뷰 패턴
        if self.current_session.metrics.get("pr_reviewed", False):
            self.memory.store_pattern(
                pattern_type="review",
                context={
                    "language": self.current_session.metrics.get("language", "python"),
                },
                solution={
                    "categories": ["security", "performance", "correctness", "maintainability", "style"],
                    "auto_fix_suggestions": True,
                },
                success_metrics={
                    "success_rate": 1.0,
                    "issues_found": self.current_session.metrics.get("issues_found", 0),
                },
                tags=["pr_review", "auto_fix"],
            )

        # 코드 수정 패턴
        if self.current_session.metrics.get("files_modified", 0) > 0:
            self.memory.store_pattern(
                pattern_type="fix",
                context={
                    "language": self.current_session.metrics.get("language", "python"),
                    "error_types": self.current_session.metrics.get("error_types", []),
                },
                solution={
                    "method": "patch_based_fix",
                    "validation": "ruff + black + mypy + pytest",
                },
                success_metrics={
                    "success_rate": 1.0,
                    "files_fixed": self.current_session.metrics.get("files_modified", 0),
                },
                tags=["auto_fix", "patch", "validation"],
            )

    def get_relevant_patterns(self, context: dict[str, Any]) -> list[SuccessPattern]:
        """현재 컨텍스트에 맞는 패턴 조회"""
        return self.memory.find_patterns(context=context, limit=3)

    def apply_pattern(self, pattern_id: str, target_context: dict[str, Any]) -> dict[str, Any] | None:
        """패턴 적용"""
        pattern = self.memory.use_pattern(pattern_id)
        if not pattern:
            return None

        # 컨텍스트에 맞게 솔루션 변환
        adapted_solution = self._adapt_solution(pattern.solution, pattern.context, target_context)

        return {
            "pattern_id": pattern_id,
            "original_solution": pattern.solution,
            "adapted_solution": adapted_solution,
            "confidence": pattern.success_metrics.get("success_rate", 0.8),
        }

    def _adapt_solution(
        self,
        solution: dict[str, Any],
        source_context: dict[str, Any],
        target_context: dict[str, Any],
    ) -> dict[str, Any]:
        """솔루션을 타겟 컨텍스트에 맞게 변환"""
        adapted = solution.copy()

        # 언어별 변환
        if source_context.get("language") != target_context.get("language"):
            adapted["language_adapted"] = True
            adapted["target_language"] = target_context.get("language")

        # 프레임워크별 변환
        if source_context.get("framework") != target_context.get("framework"):
            adapted["framework_adapted"] = True
            adapted["target_framework"] = target_context.get("framework")

        return adapted