"""
자율 코딩 에이전트 - 메인 컨트롤러 (Agent)
"""

from __future__ import annotations

import logging
import time
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .coder import CodeGenerator
from .critic import Critic
from .dashboard import DashboardServer, get_dashboard
from .explorer import CodeExplorer
from .llm_coder import LLMCoder
from .memory import LearningAgent, PatternMemory
from .models import (
    AgentResult,
    AgentState,
    CritiqueResult,
    PlanStep,
    StepStatus,
    StepType,
    VerificationResult,
)
from .planner import WorkPlanner
from .state import get_state_manager
from .verifier import Verifier

log = logging.getLogger("autonomous_coding_agent.agent")


class DashboardClient:
    """대시보드 클라이언트 - 에이전트에서 대시보드 서버로 진행 상황 전송"""

    def __init__(self, session_id: str, dashboard_url: str = "http://localhost:8899"):
        self.session_id = session_id
        self.dashboard_url = dashboard_url.rstrip("/")
        self.enabled = True
        self._session_started = False

    def _post(self, endpoint: str, data: dict) -> bool:
        """HTTP POST 요청 전송"""
        if not self.enabled:
            return False
        try:
            import json
            import urllib.request

            url = f"{self.dashboard_url}{endpoint}"
            req = urllib.request.Request(
                url,
                data=json.dumps(data).encode("utf-8"),
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            urllib.request.urlopen(req, timeout=2).read()
            return True
        except Exception as e:
            log.debug(f"Dashboard update failed: {e}")
            return False

    def start_session(self, goal: str, total_steps: int = 0) -> None:
        """세션 시작 알림"""
        if self._session_started:
            return
        self._post(
            f"/api/sessions/{self.session_id}/start",
            {"goal": goal, "total_steps": total_steps},
        )
        self._session_started = True

    def start_step(self, step_id: str, title: str) -> None:
        """단계 시작 알림"""
        self._post(
            f"/api/sessions/{self.session_id}/step/{step_id}/start",
            {"title": title},
        )

    def update_step_progress(
        self, step_id: str, progress: float, log: str | None = None, metrics: dict | None = None
    ) -> None:
        """단계 진행률 업데이트"""
        data = {"progress": progress}
        if log:
            data["log"] = log
        if metrics:
            data["metrics"] = metrics
        self._post(f"/api/sessions/{self.session_id}/step/{step_id}/progress", data)

    def complete_step(
        self, step_id: str, status: str = "completed", metrics: dict | None = None
    ) -> None:
        """단계 완료 알림"""
        data = {"status": status}
        if metrics:
            data["metrics"] = metrics
        self._post(f"/api/sessions/{self.session_id}/step/{step_id}/complete", data)

    def complete_session(self, status: str = "completed", metrics: dict | None = None) -> None:
        """세션 완료 알림"""
        data = {"status": status}
        if metrics:
            data["metrics"] = metrics
        self._post(f"/api/sessions/{self.session_id}/complete", data)


class AutonomousCodingAgent:
    """자율 코딩 에이전트 메인 컨트롤러"""

    def __init__(
        self,
        workspace: str | Path,
        max_iterations: int = 5,
        timeout_per_step: int = 300,
        parallel_steps: bool = True,
        verify_tests: bool = True,
        verify_lint: bool = True,
        verify_types: bool = True,
        coverage_threshold: float = 80.0,
        auto_commit: bool = False,
        hitl_on_failure: bool = True,
        resume_session: str | None = None,
    ):
        self.workspace = Path(workspace).resolve()
        self.max_iterations = max_iterations
        self.timeout_per_step = timeout_per_step
        self.parallel_steps = parallel_steps
        self.verify_tests = verify_tests
        self.verify_lint = verify_lint
        self.verify_types = verify_types
        self.coverage_threshold = coverage_threshold
        self.auto_commit = auto_commit
        self.hitl_on_failure = hitl_on_failure

        # 상태 관리
        self.state_manager = get_state_manager(self.workspace)

        # 세션 복원 또는 새로 생성
        if resume_session:
            self.state = self.state_manager.load_state(resume_session)
            if not self.state:
                raise ValueError(f"세션을 찾을 수 없음: {resume_session}")
            log.info(f"세션 복원: {resume_session}")
        else:
            self.state = AgentState(
                session_id=f"session_{uuid.uuid4().hex[:8]}",
                workspace=self.workspace,
                goal="",
                max_iterations=max_iterations,
            )

        # 모듈 초기화
        self.explorer = CodeExplorer(self.workspace)
        self.planner = WorkPlanner(self.workspace)
        self.coder = LLMCoder(self.workspace, max_refinement_rounds=3)
        self.verifier = Verifier(self.workspace)
        self.critic = Critic(self.workspace)

        # 학습/메모리 초기화
        self.pattern_memory = PatternMemory()
        self.learning_agent = LearningAgent(self.pattern_memory)

        # 대시보드 클라이언트 초기화
        self.dashboard_client = DashboardClient(self.state.session_id)

        # 결과
        self._result = None

    def run(self, goal: str, task_type: str | None = None) -> AgentResult:
        """자율 실행 메인 루프"""
        log.info(f"자율 에이전트 시작: {goal[:100]}...")
        log.info(f"세션: {self.state.session_id}")
        log.info(f"워크스페이스: {self.workspace}")

        start_time = time.time()
        self.state.goal = goal

        # 대시보드 세션 시작
        self.dashboard_client.start_session(goal, total_steps=0)  # plan이 생성된 후 업데이트

        # 학습 에이전트 세션 시작
        self.learning_agent.start_session(goal, str(self.workspace))

        try:
            # 1. 탐색 (최초 1회 또는 세션 복원 시 건너뛰기)
            if self.state.explore_result is None:
                self._run_explore()

            # 2. 계획 수립
            if self.state.plan is None:
                self._create_plan(task_type)

            # 대시보드 총 단계 수 업데이트
            if self.state.plan:
                self.dashboard_client.start_session(goal, total_steps=len(self.state.plan.steps))

            # 3. 실행 루프
            self._run_execution_loop()

            # 4. 최종 검증
            final_result = self._final_verification()

            duration = time.time() - start_time
            self._result = AgentResult(
                success=final_result.get("success", False),
                summary=final_result.get("summary", ""),
                files_changed=final_result.get("files_changed", []),
                files_created=final_result.get("files_created", []),
                files_modified=final_result.get("files_modified", []),
                test_results=final_result.get("test_results", {}),
                verification_results=final_result.get("verification_results", []),
                critique_results=final_result.get("critique_results", []),
                duration_seconds=duration,
                iterations_used=self.state.iteration,
            )

            log.info(
                f"자율 에이전트 완료: {'성공' if self._result.success else '실패'} ({duration:.1f}초)"
            )

            # 대시보드 세션 완료
            self.dashboard_client.complete_session(
                status="completed" if self._result.success else "failed",
                metrics={"duration": duration, "iterations": self.state.iteration},
            )

            # 학습 에이전트 세션 종료 (패턴 추출)
            self.learning_agent.end_session(
                success=self._result.success,
                metrics={
                    "language": (
                        self.state.explore_result.files[0].language
                        if self.state.explore_result and self.state.explore_result.files
                        else "python"
                    ),
                    "framework": (
                        "fastapi"
                        if self.state.explore_result
                        and any("fastapi" in f.path for f in self.state.explore_result.files)
                        else None
                    ),
                    "tests_generated": len(self._result.files_created),
                    "files_modified": len(self._result.files_modified),
                    "files_created": len(self._result.files_created),
                    "coverage": 0.0,  # TODO: extract from test results
                },
            )

        except (OSError, RuntimeError, ValueError) as e:
            log.error(f"자율 에이전트 오류: {e}")
            self._result = AgentResult(
                success=False,
                summary=f"실행 중 오류: {e}",
                error=str(e),
                duration_seconds=time.time() - start_time,
                iterations_used=self.state.iteration,
            )
            # 대시보드 세션 완료 (실패)
            self.dashboard_client.complete_session(status="failed", metrics={"error": str(e)})

        # 최종 상태 저장
        self.state_manager.save_state(self.state)

        return self._result

    def _run_explore(self) -> None:
        """코드베이스 탐색"""
        log.info("1️⃣ 코드베이스 탐색 중...")

        explore_result = self.explorer.explore()
        self.state.explore_result = explore_result

        log.info(
            f"  탐색 완료: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼"
        )

        # 상태 저장
        self.state_manager.save_state(self.state)

    def _create_plan(self, task_type: str | None = None) -> None:
        """실행 계획 수립"""
        log.info("2️⃣ 실행 계획 수립 중...")

        plan = self.planner.create_plan(
            goal=self.state.goal,
            explore_result=self.state.explore_result,
            task_type=task_type,
        )
        self.state.plan = plan

        log.info(f"  계획 완료: {len(plan.steps)}개 단계")

        # 상태 저장
        self.state_manager.save_state(self.state)

    def _run_execution_loop(self) -> None:
        """실행 루프"""
        log.info("3️⃣ 실행 루프 시작...")

        while not self.state.plan.is_complete() and self.state.iteration < self.max_iterations:
            self.state.iteration += 1
            log.info(f"--- 반복 {self.state.iteration}/{self.max_iterations} ---")

            # 실행 가능한 단계들 가져오기
            ready_steps = self.state.plan.get_ready_steps()

            if not ready_steps:
                if self.state.plan.has_failures():
                    log.warning("실행 가능한 단계 없음, 실패한 단계 존재")
                    break
                else:
                    log.info("모든 단계 완료")
                    break

            # 단계 실행 (병렬 또는 순차)
            if self.parallel_steps and len(ready_steps) > 1:
                self._run_steps_parallel(ready_steps)
            else:
                for step in ready_steps:
                    self._run_single_step(step)

            # 상태 저장
            self.state_manager.save_state(self.state)

            # 중간 체크포인트
            if self.state.iteration % 2 == 0:
                self.state_manager.create_checkpoint(self.state, f"iter_{self.state.iteration}")

        log.info(f"실행 루프 완료: {self.state.iteration}회 반복")

    def _run_steps_parallel(self, steps: list[PlanStep]) -> None:
        """병렬 단계 실행 - 독립적인 단계들을 동시에 실행"""
        import concurrent.futures

        log.info(f"병렬 실행: {len(steps)}개 단계")

        def run_step_in_thread(step: PlanStep) -> tuple[PlanStep, Exception | None]:
            """스레드에서 단계 실행"""
            try:
                # 각 스레드마다 별도 컨텍스트 생성 (공유 상태 방지)
                context = {
                    "goal": self.state.goal,
                    "explore_result": self.state.explore_result,
                    "plan": self.state.plan,
                    "workspace": self.workspace,
                    "config": {
                        "verify_tests": self.verify_tests,
                        "verify_lint": self.verify_lint,
                        "verify_types": self.verify_types,
                        "coverage_threshold": self.coverage_threshold,
                    },
                }

                log.info(f"  ▶ [병렬] {step.id}: {step.title}")
                step.status = StepStatus.IN_PROGRESS
                step.started_at = datetime.now(UTC)

                # 대시보드: 단계 시작 (병렬)
                self.dashboard_client.start_step(step.id, step.title)

                # 1. 코드 실행
                if step.type == StepType.CODE:
                    code_result = self.coder.execute_step(step, context)
                    step.artifacts.update(code_result)

                    # 대시보드: 진행률 업데이트 (병렬)
                    self.dashboard_client.update_step_progress(step.id, 0.5, log="코드 생성 중...")

                # 2. 검증
                if step.type in (StepType.CODE, StepType.VERIFY):
                    project_files = step.assigned_files or step.artifacts.get("files_modified", [])
                    if not project_files and self.state.explore_result is not None:
                        project_files = [f.path for f in self.state.explore_result.files]
                    verification = self.verifier.verify_step(step, project_files)
                    step.artifacts["verification"] = verification.__dict__

                    # 대시보드: 검증 진행 (병렬)
                    self.dashboard_client.update_step_progress(step.id, 0.8, log="검증 중...")

                    if not verification.passed:
                        step.status = StepStatus.FAILED
                        step.error = f"검증 실패: {verification.errors}"
                        log.warning(f"  ❌ [병렬] 검증 실패: {step.id}")

                        # 대시보드: 단계 실패 (병렬 - 검증)
                        self.dashboard_client.complete_step(
                            step.id, "failed", metrics={"errors": verification.errors}
                        )

                        # 비평 수행
                        critique = self.critic.critique(step, verification, context)
                        step.artifacts["critique"] = critique.__dict__

                        # 재시도 로직
                        if critique.should_retry and step.retry_count < step.max_retries:
                            step.retry_count += 1
                            step.status = StepStatus.PENDING
                            log.info(
                                f"  🔄 [병렬] 재시도 예정 ({step.retry_count}/{step.max_retries})"
                            )
                        return step, None

                # 3. 비평 (검증 통과한 경우에도)
                if step.type == StepType.CODE and verification.passed:
                    verification_obj = VerificationResult(**step.artifacts.get("verification", {}))
                    critique = self.critic.critique(step, verification_obj, context)
                    step.artifacts["critique"] = critique.__dict__

                    if critique.should_retry and step.retry_count < step.max_retries:
                        step.retry_count += 1
                        step.status = StepStatus.PENDING
                        log.info(f"  🔄 [병렬] 재시도 예정 ({step.retry_count}/{step.max_retries})")
                        return step, None

                step.status = StepStatus.COMPLETED
                step.completed_at = datetime.now(UTC)

                # 대시보드: 단계 완료 (병렬)
                self.dashboard_client.complete_step(
                    step.id,
                    "completed",
                    metrics={
                        "files_created": step.artifacts.get("files_created", []),
                        "files_modified": step.artifacts.get("files_modified", []),
                    },
                )
                return step, None

            except (OSError, RuntimeError, ValueError) as e:
                step.status = StepStatus.FAILED
                step.error = str(e)
                log.error(f"  ❌ [병렬] 단계 실행 오류: {step.id} - {e}")

                # 대시보드: 단계 실패 (병렬)
                self.dashboard_client.complete_step(step.id, "failed", metrics={"error": str(e)})
                return step, e

        # ThreadPoolExecutor로 병렬 실행 (최대 4개 동시)
        max_workers = min(4, len(steps))
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 모든 단계 제출
            future_to_step = {executor.submit(run_step_in_thread, step): step for step in steps}

            # 완료 순서대로 결과 수집
            for future in concurrent.futures.as_completed(future_to_step):
                step, error = future.result()
                if error:
                    log.error(f"병렬 실행 중 예외 발생: {step.id} - {error}")
                # 상태 저장 (메인 스레드에서)
                self.state_manager.save_state(self.state)

    def _run_single_step(self, step: PlanStep) -> None:
        """단일 단계 실행"""
        assert self.state is not None, "상태 없이 단계 실행 불가"
        log.info(f"  ▶ {step.id}: {step.title}")

        self.state.current_step_id = step.id
        step.status = StepStatus.IN_PROGRESS
        step.started_at = datetime.now(UTC)

        # 대시보드: 단계 시작
        self.dashboard_client.start_step(step.id, step.title)

        try:
            # 컨텍스트 구성
            context = {
                "goal": self.state.goal,
                "explore_result": self.state.explore_result,
                "plan": self.state.plan,
                "workspace": self.workspace,
                "config": {
                    "verify_tests": self.verify_tests,
                    "verify_lint": self.verify_lint,
                    "verify_types": self.verify_types,
                    "coverage_threshold": self.coverage_threshold,
                },
            }

            # 1. 코드 실행 (LLM-first Coder + Self-Correction 루프)
            if step.type == StepType.CODE:
                # LLMCoder의 refine 루프 사용 (버전 호환성 위해 속성 확인)
                if hasattr(self.coder, "execute_step_with_refinement"):
                    code_result = self.coder.execute_step_with_refinement(
                        step, context, self.verifier, self.critic
                    )
                else:
                    # 폴백: 기존 CodeGenerator
                    code_result = self.coder.execute_step(step, context)
                # Merge code result into artifacts (preserve any existing)
                step.artifacts.update(code_result)

                # 대시보드: 진행률 업데이트
                self.dashboard_client.update_step_progress(step.id, 0.5, log="코드 생성 중...")

                # 코드 실행 자체가 실패하면 검증 실패와 동일하게 취급
                # (가드레일 거부 등 — 깨진 코드가 파일에 남지 않은 경우)
                if step.status == StepStatus.FAILED or code_result.get("error"):
                    step.status = StepStatus.FAILED
                    step.error = step.error or str(code_result.get("error", "코드 실행 실패"))
                    log.warning(f"  ❌ 코드 실행 실패: {step.id} - {step.error}")
                    self.dashboard_client.complete_step(
                        step.id, "failed", metrics={"errors": [step.error]}
                    )
                    failed_verification = VerificationResult(
                        step_id=step.id, passed=False, errors=[step.error or "코드 실행 실패"]
                    )
                    step.artifacts["verification"] = failed_verification.__dict__
                    critique = self.critic.critique(step, failed_verification, context)
                    step.artifacts["critique"] = critique.__dict__
                    if critique.should_retry and step.retry_count < step.max_retries:
                        step.retry_count += 1
                        step.status = StepStatus.PENDING
                        log.info(f"  🔄 재시도 예정 ({step.retry_count}/{step.max_retries})")
                    return

            # 2. 검증
            if step.type in (StepType.CODE, StepType.VERIFY):
                # Only verify the assigned/modified files, not all project files.
                # VERIFY 단계는 형제 CODE 단계들의 산출물을 검증한다.
                project_files = step.assigned_files or step.artifacts.get("files_modified", [])
                if not project_files and self.state.plan is not None:
                    for other in self.state.plan.steps:
                        if other.type == StepType.CODE:
                            project_files.extend(other.artifacts.get("files_created", []))
                            project_files.extend(other.artifacts.get("files_modified", []))
                    project_files = sorted(set(project_files))
                if not project_files and self.state.explore_result:
                    project_files = [
                        f.path for f in self.state.explore_result.files if f.path.endswith(".py")
                    ][:20]
                verification = self.verifier.verify_step(step, project_files)
                # Merge verification with existing artifacts (preserve files_created/files_modified)
                step.artifacts["verification"] = verification.__dict__

                # 대시보드: 검증 진행
                self.dashboard_client.update_step_progress(step.id, 0.8, log="검증 중...")

                if not verification.passed:
                    step.status = StepStatus.FAILED
                    step.error = f"검증 실패: {verification.errors}"
                    log.warning(f"  ❌ 검증 실패: {step.id}")

                    # 대시보드: 단계 실패
                    self.dashboard_client.complete_step(
                        step.id, "failed", metrics={"errors": verification.errors}
                    )

                    # 비평 수행
                    critique = self.critic.critique(step, verification, context)
                    step.artifacts["critique"] = critique.__dict__

                    # 재시도 로직
                    if critique.should_retry and step.retry_count < step.max_retries:
                        step.retry_count += 1
                        step.status = StepStatus.PENDING
                        log.info(f"  🔄 재시도 예정 ({step.retry_count}/{step.max_retries})")
                    return

            # 3. 비평 (검증 통과한 경우에도)
            if step.type == StepType.CODE and verification.passed:
                verification_obj = VerificationResult(**step.artifacts.get("verification", {}))
                critique = self.critic.critique(step, verification_obj, context)
                step.artifacts["critique"] = critique.__dict__

                if critique.should_retry and step.retry_count < step.max_retries:
                    step.retry_count += 1
                    step.status = StepStatus.PENDING
                    log.info(f"  🔄 품질 개선 위해 재시도 ({step.retry_count}/{step.max_retries})")
                    return

            step.status = StepStatus.COMPLETED
            step.completed_at = datetime.now(UTC)
            log.info(f"  ✅ 완료: {step.id}")

            # 대시보드: 단계 완료
            self.dashboard_client.complete_step(
                step.id,
                "completed",
                metrics={
                    "files_created": step.artifacts.get("files_created", []),
                    "files_modified": step.artifacts.get("files_modified", []),
                },
            )

        except (OSError, RuntimeError, ValueError) as e:
            step.status = StepStatus.FAILED
            step.error = str(e)
            step.completed_at = datetime.now(UTC)
            log.error(f"  ❌ 단계 실패 {step.id}: {e}")

            # 대시보드: 단계 실패
            self.dashboard_client.complete_step(step.id, "failed", metrics={"error": str(e)})

    def _final_verification(self) -> dict[str, Any]:
        """최종 검증 (변경 파일 범위로만 — 전체 프로젝트 검사 금지)"""
        log.info("4️⃣ 최종 검증...")

        assert self.state is not None, "상태 없이 최종 검증 불가"
        assert self.state.plan is not None, "계획 없이 최종 검증 불가"
        plan = self.state.plan
        changed: set[str] = set()
        for step in plan.steps:
            if step.status == StepStatus.COMPLETED:
                artifacts = step.artifacts
                changed.update(artifacts.get("files_created", []))
                changed.update(artifacts.get("files_modified", []))

        changed_list = sorted(changed)
        if not changed_list:
            all_passed = plan.is_complete()
            final_verification: dict[str, VerificationResult] = {}
        else:
            scope_step = PlanStep(
                id="final_verification",
                type=StepType.VERIFY,
                title="최종 검증",
                description="변경 파일 범위 최종 확인",
                assigned_files=changed_list,
            )
            v = self.verifier.verify_step(scope_step, changed_list)
            final_verification = {"final": v}
            all_passed = v.passed and plan.is_complete()

        files_changed = []
        files_created = []
        files_modified = []

        all_verification_results = []
        all_critique_results = []

        for step in self.state.plan.steps:
            if step.status == StepStatus.COMPLETED:
                artifacts = step.artifacts
                files_created.extend(artifacts.get("files_created", []))
                files_modified.extend(artifacts.get("files_modified", []))

                # Collect verification results
                if "verification" in artifacts:
                    all_verification_results.append(VerificationResult(**artifacts["verification"]))
                # Collect critique results
                if "critique" in artifacts:
                    all_critique_results.append(CritiqueResult(**artifacts["critique"]))

        files_changed = list(set(files_created + files_modified))

        # 요약 생성
        summary_parts = [
            f"목표: {self.state.goal[:100]}",
            f"단계: {len([s for s in self.state.plan.steps if s.status == StepStatus.COMPLETED])}/{len(self.state.plan.steps)} 완료",
            f"파일 생성: {len(files_created)}개, 수정: {len(files_modified)}개",
        ]

        for check_name, v in final_verification.items():
            status = "✅" if v.passed else "❌"
            summary_parts.append(f"{status} {check_name}: {'통과' if v.passed else '실패'}")

        return {
            "success": all_passed,
            "summary": "\n".join(summary_parts),
            "files_changed": files_changed,
            "files_created": files_created,
            "files_modified": files_modified,
            "test_results": {k: v.__dict__ for k, v in final_verification.items()},
            "verification_results": all_verification_results,
            "critique_results": all_critique_results,
        }

    def get_status(self) -> dict[str, Any]:
        """현재 상태 조회"""
        return {
            "session_id": self.state.session_id,
            "goal": self.state.goal,
            "iteration": self.state.iteration,
            "max_iterations": self.max_iterations,
            "current_step": self.state.current_step_id,
            "plan_complete": (self.state.plan.is_complete() if self.state.plan else False),
            "plan_has_failures": (self.state.plan.has_failures() if self.state.plan else False),
            "steps": [
                {
                    "id": s.id,
                    "title": s.title,
                    "type": s.type.value,
                    "status": s.status.value,
                    "retry_count": s.retry_count,
                    "error": s.error,
                }
                for s in (self.state.plan.steps if self.state.plan else [])
            ],
        }

    def pause(self) -> None:
        """일시 정지 (상태 저장)"""
        self.state_manager.save_state(self.state)
        log.info(f"일시 정지: {self.state.session_id}")

    def resume(self) -> None:
        """재개"""
        log.info(f"재개: {self.state.session_id}")

    def cancel(self) -> None:
        """취소"""
        self.state_manager.save_state(self.state)
        log.info(f"취소: {self.state.session_id}")

    def resume_from_checkpoint(self, checkpoint_name: str) -> AgentResult:
        """체크포인트에서 실행 재개"""
        log.info(f"체크포인트에서 재개: {checkpoint_name}")

        # 체크포인트에서 상태 복원
        restored_state = self.state_manager.restore_checkpoint(
            self.state.session_id, checkpoint_name
        )

        # 현재 상태에 복원된 내용 적용
        self.state.plan = restored_state.plan
        self.state.explore_result = restored_state.explore_result
        self.state.current_step_id = restored_state.current_step_id
        self.state.iteration = restored_state.iteration

        log.info(f"복원 완료: 반복 {self.state.iteration}, 단계 {self.state.current_step_id}")

        # 실행 루프 재개
        self._run_execution_loop()

        # 최종 검증
        final_result = self._final_verification()

        self._result = AgentResult(
            success=final_result.get("success", False),
            summary=final_result.get("summary", ""),
            files_changed=final_result.get("files_changed", []),
            files_created=final_result.get("files_created", []),
            files_modified=final_result.get("files_modified", []),
            test_results=final_result.get("test_results", {}),
            verification_results=final_result.get("verification_results", []),
            critique_results=final_result.get("critique_results", []),
            duration_seconds=0.0,
            iterations_used=self.state.iteration,
        )

        self.state_manager.save_state(self.state)
        return self._result

    def _run_with_auto_recovery(self, goal: str, max_retries: int = 3) -> AgentResult:
        """자동 재시도/복구 로직 포함 메인 루프"""
        last_error = None

        for attempt in range(max_retries):
            try:
                log.info(f"자율 에이전트 실행 시도 {attempt + 1}/{max_retries}")
                result = self.run(goal)

                if result.success:
                    log.info("자율 에이전트 성공적으로 완료")
                    return result
                else:
                    last_error = result.error or "알 수 없는 실패"
                    log.warning(f"실행 실패 (시도 {attempt + 1}): {last_error}")

                    if attempt < max_retries - 1:
                        # 마지막 체크포인트에서 재시도
                        checkpoints = self.state_manager.list_checkpoints(self.state.session_id)
                        if checkpoints:
                            latest_cp = checkpoints[0]["checkpoint_id"]
                            log.info(f"체크포인트에서 재시도: {latest_cp}")
                            self.state = self.state_manager.restore_checkpoint(
                                self.state.session_id, latest_cp
                            )
                            continue

            except (OSError, RuntimeError, ValueError) as e:
                last_error = str(e)
                log.error(f"실행 중 예외 발생 (시도 {attempt + 1}): {e}")

                if attempt < max_retries - 1:
                    checkpoints = self.state_manager.list_checkpoints(self.state.session_id)
                    if checkpoints:
                        latest_cp = checkpoints[0]["checkpoint_id"]
                        log.info(f"체크포인트에서 복구 재시도: {latest_cp}")
                        self.state = self.state_manager.restore_checkpoint(
                            self.state.session_id, latest_cp
                        )
                        continue

        # 모든 재시도 실패
        return AgentResult(
            success=False,
            summary=f"최대 재시도 횟수({max_retries}) 초과 후 실패",
            error=f"마지막 오류: {last_error}",
            duration_seconds=0.0,
            iterations_used=self.state.iteration,
        )


def run_autonomous(
    goal: str,
    workspace: str | Path,
    task_type: str | None = None,
    max_iterations: int = 5,
    **kwargs,
) -> AgentResult:
    """자율 에이전트 실행 헬퍼"""
    agent = AutonomousCodingAgent(
        workspace=workspace,
        max_iterations=max_iterations,
        **kwargs,
    )
    return agent.run(goal, task_type)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python -m autonomous_coding_agent <workspace> <goal>")
        sys.exit(1)

    workspace = sys.argv[1]
    goal = " ".join(sys.argv[2:])

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
    )

    result = run_autonomous(goal, workspace)

    print("\n" + "=" * 50)
    print("자율 에이전트 실행 결과")
    print("=" * 50)
    print(f"성공: {result.success}")
    print(f"요약:\n{result.summary}")
    print(f"파일 변경: {len(result.files_changed)}개")
    print(f"반복 횟수: {result.iterations_used}")
    print(f"소요 시간: {result.duration_seconds:.1f}초")

    if result.error:
        print(f"오류: {result.error}")

    sys.exit(0 if result.success else 1)
