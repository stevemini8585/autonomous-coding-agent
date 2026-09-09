"""
자율 코딩 에이전트 - 작업 계획자 (Planner)
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

from .models import ExploreResult, Plan, PlanStep, StepStatus, StepType

log = logging.getLogger("autonomous_coding_agent.planner")


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁWorkPlannerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁWorkPlannerǁcreate_plan__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWorkPlannerǁ_expand_description__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut: MutantDict = {}  # type: ignore
mutants_xǁWorkPlannerǁrefine_plan__mutmut: MutantDict = {}  # type: ignore


class WorkPlanner:
    """자연어 요청을 구조화된 실행 계획으로 변환"""

    # 단계 템플릿
    STEP_TEMPLATES = {
        "feature": [
            (StepType.EXPLORE, "코드베이스 탐색 및 관련 파일 식별"),
            (StepType.PLAN, "상세 구현 계획 수립"),
            (StepType.CODE, "핵심 로직 구현"),
            (StepType.CODE, "테스트 코드 작성"),
            (StepType.VERIFY, "테스트 실행 및 검증"),
            (StepType.CRITIQUE, "코드 리뷰 및 개선"),
        ],
        "bugfix": [
            (StepType.EXPLORE, "버그 재현 및 원인 분석"),
            (StepType.PLAN, "수정 계획 수립"),
            (StepType.CODE, "버그 수정"),
            (StepType.CODE, "회귀 테스트 추가"),
            (StepType.VERIFY, "테스트 실행 및 검증"),
            (StepType.CRITIQUE, "수정 사항 검토"),
        ],
        "refactor": [
            (StepType.EXPLORE, "리팩토링 대상 분석 및 영향도 파악"),
            (StepType.PLAN, "리팩토링 단계별 계획"),
            (StepType.CODE, "단계별 리팩토링 수행"),
            (StepType.VERIFY, "각 단계 테스트 검증"),
            (StepType.CRITIQUE, "품질 메트릭 비교"),
        ],
        "test": [
            (StepType.EXPLORE, "테스트 대상 코드 분석"),
            (StepType.PLAN, "테스트 시나리오 설계"),
            (StepType.CODE, "테스트 코드 작성"),
            (StepType.VERIFY, "테스트 실행 및 커버리지 확인"),
        ],
        "documentation": [
            (StepType.EXPLORE, "문서화 대상 코드 분석"),
            (StepType.PLAN, "문서 구조 설계"),
            (StepType.CODE, "문서 작성 (README, API docs, 주석)"),
            (StepType.VERIFY, "문서 빌드 및 링크 검증"),
        ],
    }

    @_mutmut_mutated(mutants_xǁWorkPlannerǁ__init____mutmut)
    def __init__(self, workspace: Path):
        self.workspace = Path(workspace).resolve()

    def xǁWorkPlannerǁ__init____mutmut_orig(self, workspace: Path):
        self.workspace = Path(workspace).resolve()

    def xǁWorkPlannerǁ__init____mutmut_1(self, workspace: Path):
        self.workspace = None

    def xǁWorkPlannerǁ__init____mutmut_2(self, workspace: Path):
        self.workspace = Path(None).resolve()

    @_mutmut_mutated(mutants_xǁWorkPlannerǁcreate_plan__mutmut)
    def create_plan(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_orig(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_1(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(None)

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_2(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:101]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_3(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is not None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_4(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = None

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_5(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(None)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_6(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = None

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_7(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=None)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_8(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = None

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_9(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(None, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_10(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, None)

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_11(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_12(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, )

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_13(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["XXfeatureXX"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_14(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["FEATURE"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_15(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = None
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_16(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(None):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_17(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = None
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_18(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i - 1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_19(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+2}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_20(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = None
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_21(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=None,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_22(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=None,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_23(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=None,
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_24(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=None,
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_25(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=None,
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_26(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=None,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_27(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_28(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_29(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_30(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_31(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_32(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_33(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.lower()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_34(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(None, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_35(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, None, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_36(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, None, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_37(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, None),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_38(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_39(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_40(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_41(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, ),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_42(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(None),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_43(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=4,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_44(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(None)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_45(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(None):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_46(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i >= 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_47(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 1:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_48(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = None

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_49(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i + 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_50(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 2].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_51(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(None, explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_52(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, None, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_53(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, None)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_54(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(explore_result, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_55(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, goal)

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_56(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, )

        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_57(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = None
        log.info(f"  생성된 단계: {len(plan.steps)}개")

        return plan

    def xǁWorkPlannerǁcreate_plan__mutmut_58(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """목표와 탐색 결과를 바탕으로 실행 계획 생성"""
        log.info(f"계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        plan = Plan(goal=goal)

        # 템플릿 기반 기본 단계 생성
        template = self.STEP_TEMPLATES.get(task_type, self.STEP_TEMPLATES["feature"])

        step_objects = []
        for i, (step_type, description) in enumerate(template):
            step_id = f"step_{i+1}_{step_type.value}"
            step = PlanStep(
                id=step_id,
                type=step_type,
                title=f"{step_type.value.upper()}: {description}",
                description=self._expand_description(step_type, description, goal, explore_result),
                verification_criteria=self._get_verification_criteria(step_type),
                max_retries=3,
            )
            step_objects.append(step)

        # 의존성 설정 (순차 실행)
        for i, step in enumerate(step_objects):
            if i > 0:
                step.dependencies = [step_objects[i - 1].id]

        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)

        plan.steps = step_objects
        log.info(None)

        return plan

    @_mutmut_mutated(mutants_xǁWorkPlannerǁ_detect_task_type__mutmut)
    def _detect_task_type(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_orig(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_1(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = None

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_2(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.upper()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_3(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(None):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_4(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw not in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_5(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["XX버그XX", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_6(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "XXbugXX", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_7(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "BUG", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_8(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "XXfixXX", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_9(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "FIX", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_10(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "XX오류XX", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_11(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "XX에러XX", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_12(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "XX안됨XX", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_13(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "XX깨짐XX"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_14(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "XXbugfixXX"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_15(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "BUGFIX"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_16(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(None):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_17(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw not in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_18(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["XX리팩토링XX", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_19(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "XXrefactorXX", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_20(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "REFACTOR", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_21(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "XX정리XX", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_22(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "XX개선XX", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_23(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "XX최적화XX"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_24(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "XXrefactorXX"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_25(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "REFACTOR"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_26(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(None):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_27(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw not in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_28(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["XX테스트XX", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_29(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "XXtestXX", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_30(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "TEST", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_31(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "XX커버리지XX", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_32(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "XXcoverageXX"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_33(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "COVERAGE"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_34(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "XXtestXX"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_35(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "TEST"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_36(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(None):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_37(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw not in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_38(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["XX문서XX", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_39(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "XXdocXX", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_40(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "DOC", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_41(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "XXreadmeXX", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_42(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "README", "주석", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_43(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "XX주석XX", "comment"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_44(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "XXcommentXX"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_45(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "COMMENT"]):
            return "documentation"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_46(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "XXdocumentationXX"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_47(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "DOCUMENTATION"
        else:
            return "feature"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_48(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "XXfeatureXX"

    def xǁWorkPlannerǁ_detect_task_type__mutmut_49(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()

        if any(kw in goal_lower for kw in ["버그", "bug", "fix", "오류", "에러", "안됨", "깨짐"]):
            return "bugfix"
        elif any(kw in goal_lower for kw in ["리팩토링", "refactor", "정리", "개선", "최적화"]):
            return "refactor"
        elif any(kw in goal_lower for kw in ["테스트", "test", "커버리지", "coverage"]):
            return "test"
        elif any(kw in goal_lower for kw in ["문서", "doc", "readme", "주석", "comment"]):
            return "documentation"
        else:
            return "FEATURE"

    @_mutmut_mutated(mutants_xǁWorkPlannerǁ_expand_description__mutmut)
    def _expand_description(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_orig(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_1(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = None

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_2(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type != StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_3(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base = f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_4(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base -= f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_5(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base = f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_6(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base -= f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_7(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(None)}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_8(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {'XX, XX'.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_9(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:6])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_10(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base = f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_11(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base -= f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_12(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type != StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_13(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base = "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_14(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base -= "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_15(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "XX\n\n기존 코드 스타일과 컨벤션을 따를 것XX"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_16(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base = "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_17(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base -= "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_18(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "XX\n타입 힌트/문서화 포함XX"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_19(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base = "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_20(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base -= "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_21(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "XX\n에러 처리 및 로깅 추가XX"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_22(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type != StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_23(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base = "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_24(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base -= "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_25(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "XX\n\n- 단위 테스트 통과XX"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_26(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base = "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_27(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base -= "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_28(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "XX\n- 린트/포맷 검사 통과XX"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_29(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base = "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_30(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base -= "\n- 타입 체크 통과 (해당 언어)"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_31(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "XX\n- 타입 체크 통과 (해당 언어)XX"
            base += "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_32(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base = "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_33(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base -= "\n- 커버리지 임계치 달성"

        return base

    def xǁWorkPlannerǁ_expand_description__mutmut_34(
        self,
        step_type: StepType,
        base_description: str,
        goal: str,
        explore_result: ExploreResult,
    ) -> str:
        """단계 설명 확장"""
        base = f"목표: {goal}\n\n{base_description}"

        if step_type == StepType.EXPLORE:
            base += f"\n\n탐색 결과: {len(explore_result.files)}개 파일, {len(explore_result.symbols)}개 심볼 발견"
            if explore_result.entry_points:
                base += f"\n진입점: {', '.join(explore_result.entry_points[:5])}"
            if explore_result.test_files:
                base += f"\n테스트 파일: {len(explore_result.test_files)}개"

        elif step_type == StepType.CODE:
            base += "\n\n기존 코드 스타일과 컨벤션을 따를 것"
            base += "\n타입 힌트/문서화 포함"
            base += "\n에러 처리 및 로깅 추가"

        elif step_type == StepType.VERIFY:
            base += "\n\n- 단위 테스트 통과"
            base += "\n- 린트/포맷 검사 통과"
            base += "\n- 타입 체크 통과 (해당 언어)"
            base += "XX\n- 커버리지 임계치 달성XX"

        return base

    @_mutmut_mutated(mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut)
    def _get_verification_criteria(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_orig(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_1(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = None
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_2(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "XX관련 파일/심볼 식별 완료XX",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_3(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "XX의존성 그래프 구성 완료XX",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_4(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "XX진입점 및 테스트 파일 식별XX",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_5(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "XX구체적 구현 단계 정의됨XX",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_6(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "XX파일별 담당 범위 명확함XX",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_7(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "XX의존성 순서 토폴로지 정렬됨XX",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_8(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "XX구현 완료 (모든 TODO 해결)XX",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_9(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 todo 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_10(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "XX기존 테스트 통과XX",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_11(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "XX새 테스트 추가됨XX",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_12(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "XX타입 힌트/문서화 포함XX",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_13(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "XX전체 테스트 스위트 통과XX",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_14(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "XX린트/포맷 오류 없음XX",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_15(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "XX타입 체크 통과XX",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_16(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "XX커버리지 80% 이상XX",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_17(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "XX빌드 성공XX",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_18(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "XX코드 품질 메트릭 기준 충족XX",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_19(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "XX보안/성능 이슈 없음XX",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_20(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "XX리팩토링 기회 식별XX",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_21(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "XX문서화 완료XX",
            ],
        }
        return criteria_map.get(step_type, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_22(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(None, ["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_23(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, None)

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_24(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(["완료 기준 충족"])

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_25(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, )

    def xǁWorkPlannerǁ_get_verification_criteria__mutmut_26(self, step_type: StepType) -> list[str]:
        """단계 유형별 검증 기준"""
        criteria_map = {
            StepType.EXPLORE: [
                "관련 파일/심볼 식별 완료",
                "의존성 그래프 구성 완료",
                "진입점 및 테스트 파일 식별",
            ],
            StepType.PLAN: [
                "구체적 구현 단계 정의됨",
                "파일별 담당 범위 명확함",
                "의존성 순서 토폴로지 정렬됨",
            ],
            StepType.CODE: [
                "구현 완료 (모든 TODO 해결)",
                "기존 테스트 통과",
                "새 테스트 추가됨",
                "타입 힌트/문서화 포함",
            ],
            StepType.VERIFY: [
                "전체 테스트 스위트 통과",
                "린트/포맷 오류 없음",
                "타입 체크 통과",
                "커버리지 80% 이상",
                "빌드 성공",
            ],
            StepType.CRITIQUE: [
                "코드 품질 메트릭 기준 충족",
                "보안/성능 이슈 없음",
                "리팩토링 기회 식별",
                "문서화 완료",
            ],
        }
        return criteria_map.get(step_type, ["XX완료 기준 충족XX"])

    @_mutmut_mutated(mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut)
    def _assign_files_to_steps(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_orig(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_1(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = None

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_2(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(None)

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_3(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.upper().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_4(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = None
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_5(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = None
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_6(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".upper()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_7(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(None)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_8(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {'XX XX'.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_9(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = None

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_10(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(None)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_11(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(2 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_12(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw not in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_13(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = None
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_14(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.upper()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_15(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(None).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_16(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem not in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_17(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.upper():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_18(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score = 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_19(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score -= 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_20(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 11  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_21(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language not in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_22(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("XXpythonXX", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_23(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("PYTHON", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_24(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "XXjavascriptXX", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_25(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "JAVASCRIPT", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_26(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "XXtypescriptXX", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_27(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "TYPESCRIPT", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_28(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "XXgoXX", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_29(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "GO", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_30(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "XXrustXX"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_31(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "RUST"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_32(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score = 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_33(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score -= 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_34(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 2

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_35(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score >= 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_36(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 1:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_37(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append(None)

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_38(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=None, reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_39(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=None)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_40(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_41(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], )
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_42(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: None, reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_43(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[2], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_44(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=False)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_45(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = None

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_46(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[1] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_47(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:11]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_48(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type != StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_49(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = None

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_50(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:6] if top_files else [f.path for f in explore_result.files[:5]]
                )

    def xǁWorkPlannerǁ_assign_files_to_steps__mutmut_51(
        self,
        steps: list[PlanStep],
        explore_result: ExploreResult,
        goal: str,
    ) -> None:
        """탐색 결과 기반으로 단계별 담당 파일 할당"""
        # 관련 파일 추출 (파일명 + 키워드 매칭)
        goal_keywords = set(goal.lower().split())

        relevant_files = []
        for file_info in explore_result.files:
            # 1. 파일명/경로에서 키워드 매칭
            file_text = f"{file_info.path} {' '.join(file_info.imports)}".lower()
            score = sum(1 for kw in goal_keywords if kw in file_text)

            # 2. 파일명 직접 매칭 (확장자 제거한 이름)
            file_stem = Path(file_info.path).stem.lower()
            if file_stem in goal.lower():
                score += 10  # 높은 가중치

            # 3. 일반적인 소스 파일은 기본 점수 부여
            if file_info.language in ("python", "javascript", "typescript", "go", "rust"):
                score += 1

            if score > 0:
                relevant_files.append((file_info.path, score))

        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]

        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = (
                    top_files[:5] if top_files else [f.path for f in explore_result.files[:6]]
                )

    @_mutmut_mutated(mutants_xǁWorkPlannerǁrefine_plan__mutmut)
    def refine_plan(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_orig(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_1(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(None)

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_2(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = None
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_3(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(None)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_4(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_5(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count = 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_6(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count -= 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_7(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 2
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_8(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = None
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_9(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = None  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_10(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result or hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_11(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(None, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_12(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, None):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_13(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr("improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_14(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, ):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_15(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "XXimprovementsXX"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_16(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "IMPROVEMENTS"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_17(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(None):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_18(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:3]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_19(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = None
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_20(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=None,
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_21(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=None,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_22(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=None,
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_23(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=None,
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_24(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=None,
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_25(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=None,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_26(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_27(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_28(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_29(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_30(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_31(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_32(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i - 1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_33(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+2}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_34(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:51]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_35(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=3,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_36(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(None)

        plan.updated_at = __import__("datetime").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_37(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = None
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_38(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__(None).datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_39(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("XXdatetimeXX").datetime.now()
        return plan

    def xǁWorkPlannerǁrefine_plan__mutmut_40(
        self,
        plan: Plan,
        failed_step_id: str,
        error: str,
        critique_result: Any,
    ) -> Plan:
        """실패한 단계 기반 계획 보완"""
        log.info(f"계획 보완: {failed_step_id} 실패 반영")

        failed_step = plan.get_step(failed_step_id)
        if not failed_step:
            return plan

        # 재시도 카운트 증가
        failed_step.retry_count += 1
        failed_step.error = error
        failed_step.status = StepStatus.PENDING  # 재시도 위해 초기화

        # 피드백 기반 추가 단계 생성
        if critique_result and hasattr(critique_result, "improvements"):
            for i, improvement in enumerate(critique_result.improvements[:2]):  # 최대 2개 추가
                new_step = PlanStep(
                    id=f"{failed_step_id}_retry_{i+1}",
                    type=StepType.CODE,
                    title=f"재시도: {improvement[:50]}",
                    description=f"이전 실패 원인: {error}\n개선 사항: {improvement}",
                    dependencies=[failed_step_id],
                    max_retries=2,
                )
                plan.steps.append(new_step)

        plan.updated_at = __import__("DATETIME").datetime.now()
        return plan

    def get_next_steps(self, plan: Plan) -> list[PlanStep]:
        """다음 실행 가능한 단계들 반환"""
        return plan.get_ready_steps()

mutants_xǁWorkPlannerǁ__init____mutmut['_mutmut_orig'] = WorkPlanner.xǁWorkPlannerǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ__init____mutmut['xǁWorkPlannerǁ__init____mutmut_1'] = WorkPlanner.xǁWorkPlannerǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ__init____mutmut['xǁWorkPlannerǁ__init____mutmut_2'] = WorkPlanner.xǁWorkPlannerǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁWorkPlannerǁcreate_plan__mutmut['_mutmut_orig'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_1'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_2'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_3'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_4'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_5'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_6'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_7'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_8'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_9'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_10'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_10 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_11'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_11 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_12'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_12 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_13'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_13 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_14'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_14 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_15'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_15 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_16'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_16 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_17'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_17 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_18'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_18 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_19'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_19 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_20'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_20 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_21'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_21 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_22'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_22 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_23'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_23 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_24'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_24 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_25'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_25 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_26'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_26 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_27'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_27 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_28'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_28 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_29'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_29 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_30'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_30 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_31'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_31 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_32'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_32 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_33'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_33 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_34'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_34 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_35'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_35 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_36'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_36 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_37'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_37 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_38'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_38 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_39'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_39 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_40'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_40 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_41'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_41 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_42'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_42 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_43'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_43 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_44'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_44 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_45'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_45 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_46'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_46 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_47'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_47 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_48'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_48 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_49'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_49 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_50'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_50 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_51'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_51 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_52'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_52 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_53'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_53 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_54'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_54 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_55'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_55 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_56'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_56 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_57'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_57 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁcreate_plan__mutmut['xǁWorkPlannerǁcreate_plan__mutmut_58'] = WorkPlanner.xǁWorkPlannerǁcreate_plan__mutmut_58 # type: ignore # mutmut generated

mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['_mutmut_orig'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_1'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_2'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_3'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_4'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_5'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_6'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_7'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_8'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_9'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_10'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_10 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_11'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_11 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_12'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_12 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_13'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_13 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_14'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_14 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_15'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_15 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_16'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_16 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_17'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_17 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_18'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_18 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_19'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_19 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_20'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_20 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_21'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_21 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_22'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_22 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_23'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_23 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_24'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_24 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_25'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_25 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_26'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_26 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_27'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_27 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_28'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_28 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_29'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_29 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_30'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_30 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_31'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_31 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_32'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_32 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_33'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_33 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_34'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_34 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_35'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_35 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_36'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_36 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_37'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_37 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_38'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_38 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_39'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_39 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_40'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_40 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_41'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_41 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_42'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_42 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_43'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_43 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_44'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_44 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_45'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_45 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_46'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_46 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_47'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_47 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_48'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_48 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_detect_task_type__mutmut['xǁWorkPlannerǁ_detect_task_type__mutmut_49'] = WorkPlanner.xǁWorkPlannerǁ_detect_task_type__mutmut_49 # type: ignore # mutmut generated

mutants_xǁWorkPlannerǁ_expand_description__mutmut['_mutmut_orig'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_1'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_2'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_3'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_4'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_5'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_6'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_7'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_8'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_9'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_10'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_10 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_11'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_11 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_12'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_12 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_13'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_13 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_14'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_14 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_15'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_15 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_16'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_16 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_17'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_17 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_18'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_18 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_19'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_19 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_20'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_20 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_21'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_21 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_22'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_22 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_23'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_23 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_24'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_24 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_25'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_25 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_26'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_26 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_27'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_27 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_28'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_28 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_29'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_29 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_30'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_30 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_31'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_31 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_32'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_32 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_33'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_33 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_expand_description__mutmut['xǁWorkPlannerǁ_expand_description__mutmut_34'] = WorkPlanner.xǁWorkPlannerǁ_expand_description__mutmut_34 # type: ignore # mutmut generated

mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['_mutmut_orig'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_1'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_2'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_3'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_4'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_5'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_6'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_7'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_8'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_9'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_10'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_10 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_11'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_11 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_12'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_12 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_13'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_13 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_14'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_14 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_15'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_15 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_16'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_16 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_17'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_17 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_18'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_18 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_19'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_19 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_20'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_20 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_21'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_21 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_22'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_22 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_23'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_23 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_24'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_24 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_25'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_25 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_get_verification_criteria__mutmut['xǁWorkPlannerǁ_get_verification_criteria__mutmut_26'] = WorkPlanner.xǁWorkPlannerǁ_get_verification_criteria__mutmut_26 # type: ignore # mutmut generated

mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['_mutmut_orig'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_1'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_2'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_3'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_4'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_5'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_6'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_7'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_8'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_9'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_10'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_10 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_11'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_11 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_12'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_12 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_13'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_13 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_14'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_14 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_15'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_15 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_16'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_16 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_17'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_17 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_18'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_18 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_19'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_19 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_20'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_20 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_21'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_21 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_22'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_22 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_23'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_23 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_24'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_24 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_25'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_25 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_26'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_26 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_27'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_27 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_28'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_28 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_29'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_29 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_30'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_30 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_31'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_31 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_32'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_32 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_33'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_33 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_34'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_34 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_35'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_35 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_36'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_36 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_37'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_37 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_38'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_38 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_39'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_39 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_40'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_40 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_41'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_41 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_42'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_42 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_43'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_43 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_44'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_44 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_45'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_45 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_46'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_46 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_47'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_47 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_48'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_48 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_49'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_49 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_50'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_50 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁ_assign_files_to_steps__mutmut['xǁWorkPlannerǁ_assign_files_to_steps__mutmut_51'] = WorkPlanner.xǁWorkPlannerǁ_assign_files_to_steps__mutmut_51 # type: ignore # mutmut generated

mutants_xǁWorkPlannerǁrefine_plan__mutmut['_mutmut_orig'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_orig # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_1'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_1 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_2'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_2 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_3'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_3 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_4'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_4 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_5'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_5 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_6'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_6 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_7'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_7 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_8'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_8 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_9'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_9 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_10'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_10 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_11'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_11 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_12'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_12 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_13'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_13 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_14'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_14 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_15'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_15 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_16'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_16 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_17'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_17 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_18'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_18 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_19'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_19 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_20'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_20 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_21'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_21 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_22'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_22 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_23'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_23 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_24'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_24 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_25'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_25 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_26'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_26 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_27'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_27 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_28'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_28 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_29'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_29 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_30'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_30 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_31'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_31 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_32'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_32 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_33'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_33 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_34'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_34 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_35'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_35 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_36'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_36 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_37'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_37 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_38'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_38 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_39'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_39 # type: ignore # mutmut generated
mutants_xǁWorkPlannerǁrefine_plan__mutmut['xǁWorkPlannerǁrefine_plan__mutmut_40'] = WorkPlanner.xǁWorkPlannerǁrefine_plan__mutmut_40 # type: ignore # mutmut generated
mutants_x_create_plan__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_plan__mutmut)
def create_plan(
    goal: str,
    explore_result: ExploreResult,
    workspace: Path,
    task_type: str | None = None,
) -> Plan:
    """계획 생성 헬퍼"""
    planner = WorkPlanner(workspace)
    return planner.create_plan(goal, explore_result, task_type)


def x_create_plan__mutmut_orig(
    goal: str,
    explore_result: ExploreResult,
    workspace: Path,
    task_type: str | None = None,
) -> Plan:
    """계획 생성 헬퍼"""
    planner = WorkPlanner(workspace)
    return planner.create_plan(goal, explore_result, task_type)


def x_create_plan__mutmut_1(
    goal: str,
    explore_result: ExploreResult,
    workspace: Path,
    task_type: str | None = None,
) -> Plan:
    """계획 생성 헬퍼"""
    planner = None
    return planner.create_plan(goal, explore_result, task_type)


def x_create_plan__mutmut_2(
    goal: str,
    explore_result: ExploreResult,
    workspace: Path,
    task_type: str | None = None,
) -> Plan:
    """계획 생성 헬퍼"""
    planner = WorkPlanner(None)
    return planner.create_plan(goal, explore_result, task_type)


def x_create_plan__mutmut_3(
    goal: str,
    explore_result: ExploreResult,
    workspace: Path,
    task_type: str | None = None,
) -> Plan:
    """계획 생성 헬퍼"""
    planner = WorkPlanner(workspace)
    return planner.create_plan(None, explore_result, task_type)


def x_create_plan__mutmut_4(
    goal: str,
    explore_result: ExploreResult,
    workspace: Path,
    task_type: str | None = None,
) -> Plan:
    """계획 생성 헬퍼"""
    planner = WorkPlanner(workspace)
    return planner.create_plan(goal, None, task_type)


def x_create_plan__mutmut_5(
    goal: str,
    explore_result: ExploreResult,
    workspace: Path,
    task_type: str | None = None,
) -> Plan:
    """계획 생성 헬퍼"""
    planner = WorkPlanner(workspace)
    return planner.create_plan(goal, explore_result, None)


def x_create_plan__mutmut_6(
    goal: str,
    explore_result: ExploreResult,
    workspace: Path,
    task_type: str | None = None,
) -> Plan:
    """계획 생성 헬퍼"""
    planner = WorkPlanner(workspace)
    return planner.create_plan(explore_result, task_type)


def x_create_plan__mutmut_7(
    goal: str,
    explore_result: ExploreResult,
    workspace: Path,
    task_type: str | None = None,
) -> Plan:
    """계획 생성 헬퍼"""
    planner = WorkPlanner(workspace)
    return planner.create_plan(goal, task_type)


def x_create_plan__mutmut_8(
    goal: str,
    explore_result: ExploreResult,
    workspace: Path,
    task_type: str | None = None,
) -> Plan:
    """계획 생성 헬퍼"""
    planner = WorkPlanner(workspace)
    return planner.create_plan(goal, explore_result, )

mutants_x_create_plan__mutmut['_mutmut_orig'] = x_create_plan__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_plan__mutmut['x_create_plan__mutmut_1'] = x_create_plan__mutmut_1 # type: ignore # mutmut generated
mutants_x_create_plan__mutmut['x_create_plan__mutmut_2'] = x_create_plan__mutmut_2 # type: ignore # mutmut generated
mutants_x_create_plan__mutmut['x_create_plan__mutmut_3'] = x_create_plan__mutmut_3 # type: ignore # mutmut generated
mutants_x_create_plan__mutmut['x_create_plan__mutmut_4'] = x_create_plan__mutmut_4 # type: ignore # mutmut generated
mutants_x_create_plan__mutmut['x_create_plan__mutmut_5'] = x_create_plan__mutmut_5 # type: ignore # mutmut generated
mutants_x_create_plan__mutmut['x_create_plan__mutmut_6'] = x_create_plan__mutmut_6 # type: ignore # mutmut generated
mutants_x_create_plan__mutmut['x_create_plan__mutmut_7'] = x_create_plan__mutmut_7 # type: ignore # mutmut generated
mutants_x_create_plan__mutmut['x_create_plan__mutmut_8'] = x_create_plan__mutmut_8 # type: ignore # mutmut generated
