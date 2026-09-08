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
from .explorer import CodeExplorer
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
        self.coder = CodeGenerator(self.workspace)
        self.verifier = Verifier(self.workspace)
        self.critic = Critic(self.workspace)

        # 결과
        self._result = None

    def run(self, goal: str, task_type: str | None = None) -> AgentResult:
        """자율 실행 메인 루프"""
        log.info(f"자율 에이전트 시작: {goal[:100]}...")
        log.info(f"세션: {self.state.session_id}")
        log.info(f"워크스페이스: {self.workspace}")

        start_time = time.time()
        self.state.goal = goal

        try:
            # 1. 탐색 (최초 1회 또는 세션 복원 시 건너뛰기)
            if self.state.explore_result is None:
                self._run_explore()

            # 2. 계획 수립
            if self.state.plan is None:
                self._create_plan(task_type)

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

        except (OSError, RuntimeError, ValueError) as e:
            log.error(f"자율 에이전트 오류: {e}")
            self._result = AgentResult(
                success=False,
                summary=f"실행 중 오류: {e}",
                error=str(e),
                duration_seconds=time.time() - start_time,
                iterations_used=self.state.iteration,
            )

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

                # 1. 코드 실행
                if step.type == StepType.CODE:
                    code_result = self.coder.execute_step(step, context)
                    step.artifacts.update(code_result)

                # 2. 검증
                if step.type in (StepType.CODE, StepType.VERIFY):
                    project_files = step.assigned_files or [
                        f.path for f in self.state.explore_result.files
                    ]
                    verification = self.verifier.verify_step(step, project_files)
                    step.artifacts["verification"] = verification.__dict__

                    if not verification.passed:
                        step.status = StepStatus.FAILED
                        step.error = f"검증 실패: {verification.errors}"
                        log.warning(f"  ❌ [병렬] 검증 실패: {step.id}")

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
                return step, None

            except (OSError, RuntimeError, ValueError) as e:
                step.status = StepStatus.FAILED
                step.error = str(e)
                log.error(f"  ❌ [병렬] 단계 실행 오류: {step.id} - {e}")
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
        log.info(f"  ▶ {step.id}: {step.title}")

        self.state.current_step_id = step.id
        step.status = StepStatus.IN_PROGRESS
        step.started_at = datetime.now(UTC)

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

            # 1. 코드 실행
            if step.type == StepType.CODE:
                code_result = self.coder.execute_step(step, context)
                # Merge code result into artifacts (preserve any existing)
                step.artifacts.update(code_result)

            # 2. 검증
            if step.type in (StepType.CODE, StepType.VERIFY):
                project_files = step.assigned_files or [
                    f.path for f in self.state.explore_result.files
                ]
                verification = self.verifier.verify_step(step, project_files)
                # Merge verification with existing artifacts (preserve files_created/files_modified)
                step.artifacts["verification"] = verification.__dict__

                if not verification.passed:
                    step.status = StepStatus.FAILED
                    step.error = f"검증 실패: {verification.errors}"
                    log.warning(f"  ❌ 검증 실패: {step.id}")

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

        except (OSError, RuntimeError, ValueError) as e:
            step.status = StepStatus.FAILED
            step.error = str(e)
            step.completed_at = datetime.now(UTC)
            log.error(f"  ❌ 단계 실패 {step.id}: {e}")

    def _final_verification(self) -> dict[str, Any]:
        """최종 전체 검증"""
        log.info("4️⃣ 최종 검증...")

        # 원본 파일 + 생성/수정된 파일 모두 검증
        all_files = {f.path for f in self.state.explore_result.files}

        for step in self.state.plan.steps:
            if step.status == StepStatus.COMPLETED:
                artifacts = step.artifacts
                all_files.update(artifacts.get("files_created", []))
                all_files.update(artifacts.get("files_modified", []))

        all_files_list = list(all_files)
        final_verification = self.verifier.verify_project(all_files_list)

        # 결과 종합
        all_passed = all(v.passed for v in final_verification.values())

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
