"""
자율 코딩 에이전트 - 작업 계획자 (Planner)
"""

from __future__ import annotations

import logging
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import Plan, PlanStep, StepType, StepStatus, ExploreResult

log = logging.getLogger("autonomous_coding_agent.planner")


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
    
    def __init__(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
    
    def create_plan(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: Optional[str] = None,
        context: Optional[Dict[str, Any]] = None,
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
                step.dependencies = [step_objects[i-1].id]
        
        # 탐색 결과 기반 파일 할당
        self._assign_files_to_steps(step_objects, explore_result, goal)
        
        plan.steps = step_objects
        log.info(f"  생성된 단계: {len(plan.steps)}개")
        
        return plan
    
    def _detect_task_type(self, goal: str) -> str:
        """목표에서 작업 유형 감지"""
        goal_lower = goal.lower()
        
        if any(kw in goal_lower for kw in ['버그', 'bug', 'fix', '오류', '에러', '안됨', '깨짐']):
            return "bugfix"
        elif any(kw in goal_lower for kw in ['리팩토링', 'refactor', '정리', '개선', '최적화']):
            return "refactor"
        elif any(kw in goal_lower for kw in ['테스트', 'test', '커버리지', 'coverage']):
            return "test"
        elif any(kw in goal_lower for kw in ['문서', 'doc', 'readme', '주석', 'comment']):
            return "documentation"
        else:
            return "feature"
    
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
    
    def _get_verification_criteria(self, step_type: StepType) -> List[str]:
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
    
    def _assign_files_to_steps(
        self,
        steps: List[PlanStep],
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
            if file_info.language in ('python', 'javascript', 'typescript', 'go', 'rust'):
                score += 1
            
            if score > 0:
                relevant_files.append((file_info.path, score))
        
        # 점수순 정렬
        relevant_files.sort(key=lambda x: x[1], reverse=True)
        top_files = [f[0] for f in relevant_files[:10]]
        
        # CODE 단계에 파일 할당
        for step in steps:
            if step.type == StepType.CODE:
                step.assigned_files = top_files[:5] if top_files else [f.path for f in explore_result.files[:5]]
    
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
        if critique_result and hasattr(critique_result, 'improvements'):
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
        
        plan.updated_at = __import__('datetime').datetime.now()
        return plan
    
    def get_next_steps(self, plan: Plan) -> List[PlanStep]:
        """다음 실행 가능한 단계들 반환"""
        return plan.get_ready_steps()


def create_plan(
    goal: str,
    explore_result: ExploreResult,
    workspace: Path,
    task_type: Optional[str] = None,
) -> Plan:
    """계획 생성 헬퍼"""
    planner = WorkPlanner(workspace)
    return planner.create_plan(goal, explore_result, task_type)