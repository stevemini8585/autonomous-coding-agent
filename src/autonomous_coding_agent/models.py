"""
자율 코딩 에이전트 - 데이터 모델
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any


class StepStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


class StepType(Enum):
    EXPLORE = "explore"
    PLAN = "plan"
    CODE = "code"
    VERIFY = "verify"
    CRITIQUE = "critique"


@dataclass
class CodeSymbol:
    """코드 심볼 (함수, 클래스, 변수 등)"""

    name: str
    type: str  # function, class, method, variable, import
    file_path: str
    line_start: int
    line_end: int
    signature: str = ""
    docstring: str = ""
    references: list[str] = field(default_factory=list)  # 이 심볼을 참조하는 파일들


@dataclass
class FileInfo:
    """파일 메타데이터"""

    path: str
    language: str
    size: int
    lines: int
    imports: list[str] = field(default_factory=list)
    exports: list[str] = field(default_factory=list)  # export되는 심볼들
    last_modified: datetime = field(default_factory=datetime.now)


@dataclass
class ExploreResult:
    """탐색 결과"""

    symbols: list[CodeSymbol] = field(default_factory=list)
    files: list[FileInfo] = field(default_factory=list)
    import_graph: dict[str, list[str]] = field(default_factory=dict)  # file -> imported files
    call_graph: dict[str, list[str]] = field(default_factory=dict)  # function -> called functions
    entry_points: list[str] = field(default_factory=list)  # main, cli, test entry points
    config_files: list[str] = field(default_factory=list)
    test_files: list[str] = field(default_factory=list)


@dataclass
class PlanStep:
    """계획 단계"""

    id: str
    type: StepType
    title: str
    description: str
    dependencies: list[str] = field(default_factory=list)  # 선행 단계 ID들
    status: StepStatus = StepStatus.PENDING
    assigned_files: list[str] = field(default_factory=list)
    expected_outputs: list[str] = field(default_factory=list)
    verification_criteria: list[str] = field(default_factory=list)
    max_retries: int = 3
    retry_count: int = 0
    started_at: datetime | None = None
    completed_at: datetime | None = None
    error: str | None = None
    artifacts: dict[str, Any] = field(default_factory=dict)  # 생성된 파일, 테스트 결과 등


@dataclass
class Plan:
    """실행 계획"""

    goal: str
    steps: list[PlanStep] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def get_step(self, step_id: str) -> PlanStep | None:
        for step in self.steps:
            if step.id == step_id:
                return step
        return None

    def get_ready_steps(self) -> list[PlanStep]:
        """실행 가능한 단계들 반환 (의존성 완료된 것들)"""
        ready = []
        completed_ids = {s.id for s in self.steps if s.status == StepStatus.COMPLETED}
        for step in self.steps:
            if step.status == StepStatus.PENDING:
                if all(dep in completed_ids for dep in step.dependencies):
                    ready.append(step)
        return ready

    def is_complete(self) -> bool:
        return all(s.status in (StepStatus.COMPLETED, StepStatus.SKIPPED) for s in self.steps)

    def has_failures(self) -> bool:
        return any(s.status == StepStatus.FAILED for s in self.steps)


@dataclass
class VerificationResult:
    """검증 결과"""

    step_id: str
    passed: bool = False
    test_results: dict[str, Any] = field(default_factory=dict)
    lint_results: dict[str, Any] = field(default_factory=dict)
    type_results: dict[str, Any] = field(default_factory=dict)
    format_results: dict[str, Any] = field(default_factory=dict)
    build_results: dict[str, Any] = field(default_factory=dict)
    coverage: float = 0.0
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    duration_seconds: float = 0.0


@dataclass
class CritiqueResult:
    """비평 결과"""

    step_id: str
    score: float = 0.0  # 0.0 ~ 1.0
    issues: list[dict[str, Any]] = field(
        default_factory=list
    )  # {type, severity, file, line, message, suggestion}
    improvements: list[str] = field(default_factory=list)
    should_retry: bool = False
    retry_feedback: str = ""
    artifacts: dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentState:
    """에이전트 전체 상태"""

    session_id: str
    workspace: Path
    goal: str
    plan: Plan | None = None
    explore_result: ExploreResult | None = None
    current_step_id: str | None = None
    iteration: int = 0
    max_iterations: int = 5
    started_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    checkpoints: list[dict[str, Any]] = field(default_factory=list)  # 롤백용

    def to_json(self) -> str:
        return json.dumps(
            {
                "session_id": self.session_id,
                "workspace": str(self.workspace),
                "goal": self.goal,
                "iteration": self.iteration,
                "max_iterations": self.max_iterations,
                "current_step_id": self.current_step_id,
                "plan": self.plan.__dict__ if self.plan else None,
            },
            default=str,
            ensure_ascii=False,
            indent=2,
        )


@dataclass
class AgentResult:
    """에이전트 실행 최종 결과"""

    success: bool
    summary: str
    files_changed: list[str] = field(default_factory=list)
    files_created: list[str] = field(default_factory=list)
    files_modified: list[str] = field(default_factory=list)
    test_results: dict[str, Any] = field(default_factory=dict)
    verification_results: list[VerificationResult] = field(default_factory=list)
    critique_results: list[CritiqueResult] = field(default_factory=list)
    duration_seconds: float = 0.0
    iterations_used: int = 0
    error: str | None = None
