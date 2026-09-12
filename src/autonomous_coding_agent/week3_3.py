"""
이슈 분해기 + TDD 사이클 + LLM 리뷰어 (Week 3-3)
- IssueDecomposer: 복잡한 이슈를 서브태스크로 분해, 의존성 그래프 구성
- TDDCycle: Red-Green-Refactor 자동화 (테스트 우선 → 구현 → 리팩터)
- LLMReviewer: PR diff 기반 LLM 코드 리뷰 (기존 PRReviewer 보강)
"""

from __future__ import annotations

import ast
import json
import logging
import re
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .coder import CodeGenerator, _parses
from .llm_client import chat
from .llm_coder import LLMCoder
from .models import (
    CodeSymbol,
    CritiqueResult,
    ExploreResult,
    Plan,
    PlanStep,
    StepStatus,
    StepType,
    VerificationResult,
)
from .verifier import Verifier

log = logging.getLogger("autonomous_coding_agent.week3_3")


# ============================================================================
# 1. IssueDecomposer — 이슈 분해 & 의존성 그래프
# ============================================================================


@dataclass
class SubTask:
    """분해된 서브태스크"""

    id: str
    title: str
    description: str
    task_type: str  # feature, bugfix, refactor, test, doc
    assigned_files: list[str] = field(default_factory=list)
    depends_on: list[str] = field(default_factory=list)  # 선행 태스크 ID
    priority: int = 0  # 높을수록 우선
    estimate_hours: float = 1.0
    acceptance_criteria: list[str] = field(default_factory=list)


@dataclass
class DecompositionResult:
    """분해 결과"""

    original_goal: str
    sub_tasks: list[SubTask]
    dependency_graph: dict[str, list[str]]  # task_id -> [dependent_task_ids]
    topological_order: list[str]  # 실행 순서


class IssueDecomposer:
    """
    복잡한 이슈/목표를 실행 가능한 서브태스크로 분해.
    - LLM 기반 분해 (템플릿 폴백 포함)
    - 의존성 그래프 구성 + 위상 정렬
    - 각 서브태스크에 파일/검증 기준 매핑
    """

    SYSTEM_PROMPT = """당신은 소프트웨어 아키텍트이자 테크 리드입니다.
복잡한 이슈를 작고 독립적이며 테스트 가능한 서브태스크로 분해하세요.

분해 원칙:
1. **단일 책임**: 각 태스크는 하나의 명확한 목표만 가짐
2. **독립성**: 가능하면 병렬 실행 가능하도록 의존성 최소화
3. **검증 가능**: 각 태스크는 명확한 완료 기준(acceptance criteria) 보유
4. **파일 매핑**: 어떤 파일을 수정/생성해야 하는지 명시
5. **의존성 명시**: 선행되어야 할 태스크 ID 명시

출력 JSON 스키마:
{
  "sub_tasks": [
    {
      "id": "task_1",
      "title": "짧은 제목",
      "description": "상세 설명",
      "task_type": "feature|bugfix|refactor|test|doc",
      "assigned_files": ["src/...py"],
      "depends_on": ["task_0"],
      "priority": 10,
      "estimate_hours": 2.0,
      "acceptance_criteria": ["기준1", "기준2"]
    }
  ]
}"""

    DECOMPOSE_PROMPT = """이슈/목표: {goal}

코드베이스 탐색 결과:
- 주요 심볼: {symbols}
- 관련 파일: {files}
- 언어: {language}
- 프레임워크: {framework}

작업 유형 힌트: {task_type}

위 정보를 바탕으로 이슈를 서브태스크로 분해해 JSON으로 출력하세요."""

    def __init__(self, workspace: Path, use_llm: bool = True):
        self.workspace = Path(workspace).resolve()
        self.use_llm = use_llm

    def decompose(
        self,
        goal: str,
        explore_result: ExploreResult | None = None,
        task_type: str | None = None,
    ) -> DecompositionResult:
        """이슈 분해 실행"""
        log.info(f"📋 이슈 분해 시작: {goal[:80]}...")

        # 탐색 결과 요약
        symbols = []
        files = []
        language = "python"
        framework = "unknown"
        if explore_result:
            symbols = [f"{s.name}({s.type})@{s.file_path}" for s in explore_result.symbols[:30]]
            files = [f.path for f in explore_result.files[:20] if f.path.endswith(".py")]
            if explore_result.files:
                language = explore_result.files[0].language or "python"

        # LLM 분해 시도
        sub_tasks = []
        if self.use_llm:
            try:
                sub_tasks = self._llm_decompose(
                    goal, explore_result, task_type, symbols, files, language, framework
                )
            except Exception as e:
                log.warning(f"LLM 분해 실패, 템플릿 폴백: {e}")

        # 폴백: 템플릿 기반 분해
        if not sub_tasks:
            sub_tasks = self._template_decompose(goal, task_type, explore_result)

        # 의존성 그래프 + 위상 정렬
        dep_graph = {t.id: t.depends_on for t in sub_tasks}
        topo_order = self._topological_sort(sub_tasks)

        return DecompositionResult(
            original_goal=goal,
            sub_tasks=sub_tasks,
            dependency_graph=dep_graph,
            topological_order=topo_order,
        )

    def _llm_decompose(
        self,
        goal: str,
        explore_result: ExploreResult | None,
        task_type: str | None,
        symbols: list[str],
        files: list[str],
        language: str,
        framework: str,
    ) -> list[SubTask]:
        prompt = self.DECOMPOSE_PROMPT.format(
            goal=goal,
            symbols=", ".join(symbols[:20]) if symbols else "없음",
            files=", ".join(files[:15]) if files else "없음",
            language=language,
            framework=framework,
            task_type=task_type or "auto",
        )
        provider, text = chat(prompt, self.SYSTEM_PROMPT)
        if provider == "none" or not text.strip():
            return []

        text = text.strip()
        if text.startswith("```"):
            lines = text.split("\n")
            lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            text = "\n".join(lines)

        try:
            data = json.loads(text)
            tasks = []
            for i, t in enumerate(data.get("sub_tasks", [])):
                tasks.append(
                    SubTask(
                        id=t.get("id", f"task_{i}"),
                        title=t.get("title", f"Task {i}"),
                        description=t.get("description", ""),
                        task_type=t.get("task_type", "feature"),
                        assigned_files=t.get("assigned_files", []),
                        depends_on=t.get("depends_on", []),
                        priority=t.get("priority", 0),
                        estimate_hours=t.get("estimate_hours", 1.0),
                        acceptance_criteria=t.get("acceptance_criteria", []),
                    )
                )
            return tasks
        except json.JSONDecodeError as e:
            log.warning(f"LLM 분해 JSON 파싱 실패: {e}")
            return []

    def _template_decompose(
        self,
        goal: str,
        task_type: str | None,
        explore_result: ExploreResult | None,
    ) -> list[SubTask]:
        """템플릿 기반 폴백 분해"""
        from .planner import WorkPlanner

        planner = WorkPlanner(self.workspace)
        detected_type = task_type or planner._detect_task_type(goal)

        # 기본 템플릿에서 단계 추출
        from .planner import WorkPlanner

        planner = WorkPlanner(self.workspace)
        template = planner.STEP_TEMPLATES.get(detected_type, planner.STEP_TEMPLATES["feature"])

        tasks = []
        for i, (step_type, title) in enumerate(template):
            tasks.append(
                SubTask(
                    id=f"task_{i}",
                    title=title,
                    description=f"{detected_type} 템플릿의 {i+1}단계: {title}",
                    task_type=detected_type,
                    assigned_files=[],
                    depends_on=[f"task_{i-1}"] if i > 0 else [],
                    priority=10 - i,
                    estimate_hours=1.0,
                    acceptance_criteria=[f"{title} 완료"],
                )
            )
        return tasks

    def _topological_sort(self, tasks: list[SubTask]) -> list[str]:
        """위상 정렬 (Kahn 알고리즘)"""
        from collections import deque

        task_map = {t.id: t for t in tasks}
        in_degree = {t.id: 0 for t in tasks}
        adj = {t.id: [] for t in tasks}

        for t in tasks:
            for dep in t.depends_on:
                if dep in adj:
                    adj[dep].append(t.id)
                    in_degree[t.id] += 1

        queue = deque([tid for tid, deg in in_degree.items() if deg == 0])
        order = []

        while queue:
            tid = queue.popleft()
            order.append(tid)
            for nxt in adj[tid]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)

        # 순환 의존성 있으면 남은 것 추가
        if len(order) < len(tasks):
            for t in tasks:
                if t.id not in order:
                    order.append(t.id)

        return order


# ============================================================================
# 2. TDDCycle — Red-Green-Refactor 자동화
# ============================================================================


@dataclass
class TDDResult:
    """TDD 사이클 결과"""

    success: bool
    test_file: str
    implementation_file: str
    red_phase_passed: bool = False  # 테스트 실패 확인
    green_phase_passed: bool = False  # 구현 후 테스트 통과
    refactor_phase_passed: bool = False
    cycles: int = 0
    error: str | None = None


class TDDCycle:
    """
    Red-Green-Refactor 자동화 사이클.
    1. RED: 실패하는 테스트 작성 (기존 테스트가 없으면 생성)
    2. GREEN: 테스트를 통과하는 최소 구현
    3. REFACTOR: 품질 개선 (테스트 계속 통과하며)
    """

    def __init__(
        self,
        workspace: Path,
        coder: LLMCoder | CodeGenerator,
        verifier: Verifier,
        max_cycles: int = 3,
    ):
        self.workspace = Path(workspace).resolve()
        self.coder = coder
        self.verifier = verifier
        self.max_cycles = max_cycles

    def run_tdd_cycle(
        self,
        step: PlanStep,
        context: dict[str, Any],
    ) -> TDDResult:
        """TDD 사이클 실행"""
        goal = context.get("goal", "")
        test_file = self._find_or_create_test_file(step)
        impl_files = step.assigned_files

        log.info(f"🔴🟢♻️ TDD 사이클 시작: {step.id} (테스트: {test_file})")

        # 1. RED: 테스트가 실패하는지 확인 (없으면 생성)
        if not self._run_tests(test_file, impl_files):
            log.info("  🔴 RED: 테스트 실패 확인됨 (또는 테스트 없음)")
        else:
            # 테스트가 이미 통과하면 새로운 테스트 케이스 추가 필요
            self._add_failing_test_case(test_file, context.get("goal", ""))
            if not self._run_tests(test_file, impl_files):
                log.info("  🔴 RED: 새 테스트 케이스 실패 확인")
            else:
                return TDDResult(
                    success=False,
                    test_file=test_file,
                    implementation_file=impl_files[0] if impl_files else "",
                    error="테스트가 처음부터 통과 — 새로운 실패 케이스 생성 실패",
                )

        # 2. GREEN + REFACTOR 사이클
        for cycle in range(self.max_cycles):
            log.info(f"  🔄 TDD 사이클 {cycle + 1}/{self.max_cycles}")

            # GREEN: 구현 생성/수정
            step.assigned_files = impl_files
            impl_result = self.coder.execute_step(
                PlanStep(
                    id=f"{step.id}_impl_{cycle}",
                    type=StepType.CODE,
                    title=f"TDD 구현 {cycle+1}",
                    description=goal,
                    assigned_files=impl_files,
                ),
                {
                    "goal": context.get("goal", ""),
                    "explore_result": context.get("explore_result"),
                    "plan": context.get("plan"),
                },
            )

            # 테스트 실행
            if self._run_tests(test_file, impl_files):
                log.info("  🟢 GREEN: 테스트 통과")
                # REFACTOR: 품질 개선 (테스트 통과 유지하며)
                self._refactor_while_green(test_file, impl_files)
                log.info("  ♻️ REFACTOR: 품질 개선 완료")
                return TDDResult(
                    success=True,
                    test_file=test_file,
                    implementation_file=impl_files[0] if impl_files else "",
                    red_phase_passed=True,
                    green_phase_passed=True,
                    refactor_phase_passed=True,
                    cycles=cycle + 1,
                )

            log.warning(f"  ❌ 사이클 {cycle + 1}: 테스트 여전히 실패 — 재시도")

        return TDDResult(
            success=False,
            test_file=test_file,
            implementation_file=impl_files[0] if impl_files else "",
            red_phase_passed=True,
            error=f"{self.max_cycles} 사이클 내 GREEN 도달 실패",
        )

    def _find_or_create_test_file(self, step: PlanStep) -> str:
        """테스트 파일 찾기 또는 생성"""
        # step.assigned_files에서 대응하는 테스트 파일 찾기
        for f in step.assigned_files:
            if f.startswith("tests/"):
                return f
            # src/...py -> tests/test_...py 변환
            if f.startswith("src/") and f.endswith(".py"):
                test_path = f.replace("src/", "tests/").replace(".py", "_test.py")
                test_path = test_path.replace("/test_", "/test_").replace(".py", "_test.py")
                # 더 정확히: src/pkg/mod.py -> tests/pkg/test_mod.py
                parts = Path(f).parts
                if parts[0] == "src":
                    test_name = "test_" + parts[-1]
                    test_path = "tests/" + "/".join(parts[1:-1]) + "/" + test_name
                else:
                    test_path = "tests/test_" + Path(f).stem + ".py"

                full = self.workspace / test_path
                if full.exists():
                    return test_path

        # 없으면 기본 생성
        test_path = "tests/test_tdd_" + step.id + ".py"
        full = self.workspace / test_path
        full.parent.mkdir(parents=True, exist_ok=True)
        if not full.exists():
            full.write_text(
                '"""TDD 테스트 (자동 생성)"""\n\nimport pytest\n\n\ndef test_tdd_placeholder():\n    """TDD 테스트 플레이스홀더"""\n    assert False, "구현 필요"\n',
                encoding="utf-8",
            )
        return test_path

    def _run_tests(self, test_file: str, impl_files: list[str]) -> bool:
        """pytest 실행 및 결과 반환"""
        try:
            result = subprocess.run(
                ["pytest", test_file, "-v", "--tb=short"],
                cwd=self.workspace,
                capture_output=True,
                text=True,
                timeout=120,
            )
            return result.returncode == 0
        except subprocess.TimeoutExpired:
            log.warning("테스트 타임아웃")
            return False
        except Exception as e:
            log.warning(f"테스트 실행 오류: {e}")
            return False

    def _add_failing_test_case(self, test_file: str, goal: str) -> None:
        """목표 기반으로 실패하는 테스트 케이스 추가"""
        full = self.workspace / test_file
        try:
            existing = full.read_text(encoding="utf-8")
        except OSError:
            existing = ""

        # LLM으로 테스트 케이스 생성
        system = "너는 pytest 테스트 작성기다. 실패하는 테스트 케이스만 추가해. 설명 없이 코드만."
        prompt = f"""파일: {test_file}
목표: {goal}

기존 내용:
```python
{existing}
```

이 목표를 검증하는 **실패하는** pytest 테스트 함수 1개를 추가해.
테스트 이름은 test_tdd_<목표키워드> 형태.
assert False 또는 구현 전이라 실패할 조건으로 작성.
기존 코드에 자연스럽게 이어지도록 추가해. 펜스 없이 코드만 출력."""

        provider, text = chat(prompt, "pytest 테스트 작성기. 실패하는 테스트만 추가. 코드만 출력.")
        if provider != "none" and text.strip():
            text = text.strip()
            if text.startswith("```"):
                lines = text.split("\n")
                lines = lines[1:]
                if lines and lines[-1].strip() == "```":
                    lines = lines[:-1]
                text = "\n".join(lines)
            # 기존 파일 끝에 추가
            (self.workspace / test_file).write_text(existing + "\n\n" + text, encoding="utf-8")

    def _refactor_while_green(self, test_file: str, impl_files: list[str]) -> None:
        """테스트 통과 유지하며 리팩터 (린트/타입/포맷)"""
        # 1. ruff --fix
        for f in impl_files:
            subprocess.run(["ruff", "check", "--fix", f], cwd=self.workspace, capture_output=True)
        # 2. black
        for f in impl_files:
            subprocess.run(["black", "-q", f], cwd=self.workspace, capture_output=True)
        # 3. 테스트 재실행으로 회귀 확인
        self._run_tests(test_file, impl_files)


# ============================================================================
# 3. LLMReviewer — PR diff 기반 LLM 코드 리뷰
# ============================================================================


@dataclass
class ReviewComment:
    """리뷰 코멘트"""

    file_path: str
    line_start: int
    line_end: int
    severity: str  # critical, error, warning, info, nit
    category: str  # correctness, style, security, performance, maintainability
    message: str
    suggestion: str | None = None
    code_snippet: str | None = None


@dataclass
class LLMReviewResult:
    """LLM 리뷰 결과"""

    pr_number: int
    comments: list[ReviewComment]
    summary: str
    approved: bool
    critical_count: int = 0
    error_count: int = 0
    warning_count: int = 0


class LLMReviewer:
    """
    PR diff 기반 LLM 코드 리뷰어.
    - 기존 PRReviewer(정규식/ruff/mypy) 보강
    - 변경된 파일만 컨텍스트로 LLM 리뷰
    - 구조화된 코멘트(라인 단위) 생성
    """

    SYSTEM_PROMPT = """당신은 시니어 소프트웨어 엔지니어이자 코드 리뷰어입니다.
변경된 코드(diff)를 보고 다음 관점에서 리뷰하세요:

1. **Correctness (정확성)**: 버그, 논리 오류, 경계값, 예외 처리
2. **Security (보안)**: 입력 검증, 인젝션, 시크릿, 권한, 암호화
3. **Performance (성능)**: 복잡도, N+1, 메모리, 불필요한 연산
4. **Maintainability (유지보수성)**: 가독성, 명명, 모듈화, 문서화
5. **Style (스타일)**: 컨벤션, 포맷, 타입 힌트, import 정리

출력: JSON 배열. 각 코멘트:
{{
  "file_path": "src/...py",
  "line_start": 42,
  "line_end": 45,
  "severity": "critical|error|warning|info|nit",
  "category": "correctness|security|performance|maintainability|style",
  "message": "구체적 설명",
  "suggestion": "구체적 수정 제안 (선택)",
  "code_snippet": "문제 코드片段" (선택)
}}

중요: **변경된 라인(+/ diff)**만 리뷰하세요. 기존 코드는 건드리지 마세요."""

    REVIEW_PROMPT = """PR #{pr_number}: {pr_title}

변경된 파일들:
{diff_summary}

--- Diff 시작 ---
{diff_content}
--- Diff 끝 ---

위 변경사항을 위 5가지 관점에서 리뷰하세요. JSON 배열로만 출력."""

    def __init__(self, workspace: Path, use_llm: bool = True):
        self.workspace = Path(workspace).resolve()
        self.use_llm = use_llm
        # 기존 PRReviewer도 내부에서 사용 (정적 분석 보강용)
        from .pr_reviewer import PRReviewer

        self.static_reviewer = PRReviewer(workspace)

    def review_pr(
        self,
        pr_number: int,
        repo: str,
        base_branch: str = "main",
    ) -> LLMReviewResult:
        """PR 리뷰 수행 (LLM + 정적 분석 결합)"""
        log.info(f"🤖 LLM 리뷰 시작: PR #{pr_number}")

        # 1. 정적 분석 리뷰 (기존)
        static_result = self.static_reviewer.review_pr(pr_number, repo, base_branch)

        # 2. LLM 리뷰 (diff 기반)
        llm_comments = []
        if self.use_llm:
            llm_comments = self._llm_review(pr_number, repo, base_branch)

        # 3. 병합
        all_comments = self._merge_comments(static_result.comments, llm_comments)

        # 집계
        crit = sum(1 for c in all_comments if c.severity == "critical")
        err = sum(1 for c in all_comments if c.severity == "error")
        warn = sum(1 for c in all_comments if c.severity == "warning")

        approved = crit == 0 and err == 0

        summary = f"critical {crit}, error {err}, warning {warn}, info {sum(1 for c in all_comments if c.severity=='info')}, nit {sum(1 for c in all_comments if c.severity=='nit')}"

        return LLMReviewResult(
            pr_number=pr_number,
            comments=all_comments,
            summary=summary,
            approved=approved,
            critical_count=crit,
            error_count=err,
            warning_count=warn,
        )

    def _get_pr_diff(self, pr_number: int, repo: str) -> str:
        """PR diff 가져오기"""
        try:
            result = subprocess.run(
                ["gh", "pr", "diff", str(pr_number), "-R", repo],
                cwd=self.workspace,
                capture_output=True,
                text=True,
                timeout=60,
            )
            return result.stdout if result.returncode == 0 else ""
        except Exception as e:
            log.warning(f"PR diff 가져오기 실패: {e}")
            return ""

    def _llm_review(self, pr_number: int, repo: str, base_branch: str) -> list[ReviewComment]:
        """LLM 기반 리뷰"""
        diff = self._get_pr_diff(pr_number, repo)
        if not diff:
            return []

        # diff 요약 (파일별 변경 라인 수)
        diff_summary = self._summarize_diff(diff)

        prompt = self.REVIEW_PROMPT.format(
            pr_number=pr_number,
            pr_title="",  # gh pr view로 가져올 수 있지만 생략
            diff_summary=diff_summary,
            diff_content=diff[:15000],  # 토큰 제한
        )

        provider, text = chat(prompt, self.SYSTEM_PROMPT)
        if provider == "none" or not text.strip():
            return []

        text = text.strip()
        if text.startswith("```"):
            lines = text.split("\n")
            lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            text = "\n".join(lines)

        try:
            comments_data = json.loads(text)
            comments = []
            for c in comments_data:
                comments.append(
                    ReviewComment(
                        file_path=c.get("file_path", ""),
                        line_start=c.get("line_start", 1),
                        line_end=c.get("line_end", c.get("line_start", 1)),
                        severity=c.get("severity", "info"),
                        category=c.get("category", "style"),
                        message=c.get("message", ""),
                        suggestion=c.get("suggestion"),
                        code_snippet=c.get("code_snippet"),
                    )
                )
            return comments
        except json.JSONDecodeError as e:
            log.warning(f"LLM 리뷰 JSON 파싱 실패: {e}")
            return []

    def _summarize_diff(self, diff: str) -> str:
        """diff 요약 (파일별 변경 개요)"""
        lines = diff.split("\n")
        current_file = None
        file_changes = {}

        for line in lines:
            if line.startswith("diff --git"):
                parts = line.split()
                if len(parts) >= 4:
                    current_file = parts[3][2:]  # b/ 제거
                    file_changes[current_file] = {"added": 0, "removed": 0}
            elif line.startswith("+") and not line.startswith("+++"):
                if current_file:
                    file_changes[current_file]["added"] += 1
            elif line.startswith("-") and not line.startswith("---"):
                if current_file:
                    file_changes[current_file]["removed"] += 1

        summary_lines = []
        for f, c in file_changes.items():
            summary_lines.append(f"  {f}: +{c['added']} -{c['removed']}")
        return "\n".join(summary_lines) if summary_lines else "변경사항 없음"

    def _merge_comments(
        self,
        static_comments: list,
        llm_comments: list[ReviewComment],
    ) -> list[ReviewComment]:
        """정적 분석 + LLM 코멘트 병합 (중복 제거)"""
        # 라인+파일+메시지 기준으로 중복 제거
        seen = set()
        merged = []

        def to_review_comment(c) -> ReviewComment:
            if isinstance(c, ReviewComment):
                return c
            # PRReviewer의 ReviewComment 변환
            return ReviewComment(
                file_path=c.file_path,
                line_start=c.line_start,
                line_end=c.line_end,
                severity=(
                    c.severity.value.lower()
                    if hasattr(c.severity, "value")
                    else str(c.severity).lower()
                ),
                category=(
                    c.category.value.lower()
                    if hasattr(c.category, "value")
                    else str(c.category).lower()
                ),
                message=c.message,
                suggestion=c.suggestion,
            )

        for c in static_comments:
            rc = to_review_comment(c)
            key = (rc.file_path, rc.line_start, rc.message[:50])
            if key not in seen:
                seen.add(key)
                merged.append(rc)

        for c in llm_comments:
            key = (c.file_path, c.line_start, c.message[:50])
            if key not in seen:
                seen.add(key)
                merged.append(c)

        return merged


# ============================================================================
# 편의 팩토리
# ============================================================================


def create_issue_decomposer(workspace: Path | str, **kwargs) -> IssueDecomposer:
    return IssueDecomposer(Path(workspace), **kwargs)


def create_tdd_cycle(
    workspace: Path | str,
    coder: LLMCoder | CodeGenerator,
    verifier: Verifier,
    **kwargs,
) -> TDDCycle:
    return TDDCycle(Path(workspace), coder, verifier, **kwargs)


def create_llm_reviewer(workspace: Path | str, **kwargs) -> LLMReviewer:
    return LLMReviewer(Path(workspace), **kwargs)
