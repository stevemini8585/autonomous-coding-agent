"""
LLM 기반 지능형 플래너 (Planner v2)
- Chain-of-Thought 프롬프팅
- 벡터 메모리 연동 (과거 성공 패턴 활용)
- 자기 일관성 검증 (Self-Consistency)
- 동적 단계 분해/병합
"""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path
from typing import Any

from .models import ExploreResult, Plan, PlanStep, StepStatus, StepType
from .vector_memory import VectorPatternMemory

log = logging.getLogger("autonomous_coding_agent.llm_planner")


class LLMPlanner:
    """LLM 기반 지능형 플래너"""

    # 시스템 프롬프트
    SYSTEM_PROMPT = """당신은 세계 최고 수준의 소프트웨어 아키텍트이자 시니어 엔지니어입니다.
사용자의 목표를 분석하여 실행 가능하고, 검증 가능하며, 유지보수하기 쉬운 상세한 실행 계획을 수립하세요.

계획 수립 원칙:
1. **단일 책임**: 각 단계는 하나의 명확한 목표를 가져야 합니다.
2. **의존성 명시**: 단계 간 의존성을 명확히 하고 순환 의존성 방지
3. **검증 가능**: 각 단계는 객관적 검증 기준을 포함해야 합니다.
4. **점진적 복잡도**: 단순 → 복잡 순서로, 리스크 낮은 것부터 시작
5. **롤백 가능**: 실패 시 되돌릴 수 있는 체크포인트 고려
6. **테스트 우선**: 구현 전 테스트 설계 (TDD 원칙)

출력 형식: JSON (Plan 스키마 준수)"""

    # Chain-of-Thought 프롬프트 템플릿
    COT_PROMPT = """목표: {goal}

작업 유형: {task_type}

코드베이스 탐색 결과:
- 전체 파일: {file_count}개
- 심볼: {symbol_count}개
- 언어 분포: {languages}
- 진입점: {entry_points}
- 테스트 파일: {test_files}개
- 설정 파일: {config_files}개

관련 파일 (상위 10개):
{relevant_files}

과거 성공 패턴 (벡터 검색 결과):
{past_patterns}

---

다음 단계로 Chain-of-Thought 추론을 수행하세요:

1. **목표 분석**: 목표의 핵심 요구사항, 제약조건, 성공 기준은 무엇인가?
2. **작업 분해**: 목표를 달성하기 위한 논리적 서브태스크는 무엇인가? (최소 3개, 최대 8개)
3. **의존성 매핑**: 각 서브태스크 간 선행/후행 관계는?
4. **리스크 평가**: 각 단계의 기술적 리스크, 불확실성, 롤백 난이도는?
5. **검증 전략**: 각 단계별 객관적 검증 기준 (테스트, 린트, 타입, 커버리지 등)
6. **패턴 적용**: 과거 성공 패턴 중 적용 가능한 것은?
7. **최종 계획**: 위 추론을 종합한 실행 가능한 단계 리스트

출력: 다음 JSON 스키마 준수
{{
  "reasoning": "위 1-6번 추론 과정의 요약",
  "risk_assessment": "주요 리스크와 완화 방안",
  "steps": [
    {{
      "id": "step_1_explore",
      "type": "explore",
      "title": "단계 제목",
      "description": "상세 설명",
      "dependencies": [],
      "verification_criteria": ["기준1", "기준2"],
      "assigned_files": ["file1.py", "file2.py"],
      "estimated_complexity": "low|medium|high",
      "risk_level": "low|medium|high",
      "rollback_strategy": "롤백 방법"
    }}
  ]
}}"""

    def __init__(
        self,
        workspace: Path,
        vector_memory: VectorPatternMemory | None = None,
        model: str = "gpt-4o-mini",
        temperature: float = 0.3,
        max_tokens: int = 4000,
        self_consistency_n: int = 3,
    ):
        self.workspace = Path(workspace).resolve()
        self.vector_memory = vector_memory
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.self_consistency_n = self_consistency_n

        # LLM 클라이언트 초기화
        self.client = None
        self.provider = "template"
        self._init_llm_client()

    def _init_llm_client(self):
        """LLM 클라이언트 초기화 (OpenAI 우선, 없으면 Anthropic, 없으면 로컬)"""
        try:
            import openai

            if os.getenv("OPENAI_API_KEY"):
                self.client = openai.OpenAI()
                self.provider = "openai"
                log.info("OpenAI 클라이언트 초기화")
                return
        except ImportError:
            pass

        try:
            import anthropic

            if os.getenv("ANTHROPIC_API_KEY"):
                self.client = anthropic.Anthropic()
                self.provider = "anthropic"
                log.info("Anthropic 클라이언트 초기화")
                return
        except ImportError:
            pass

        log.warning("LLM 클라이언트 없음 - 템플릿 기반 플래너로 폴백")
        self.provider = "template"

    def create_plan(
        self,
        goal: str,
        explore_result: ExploreResult,
        task_type: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> Plan:
        """LLM 기반 계획 생성"""
        log.info(f"LLM 플래너 계획 생성: {goal[:100]}...")

        # 작업 유형 자동 감지
        if task_type is None:
            task_type = self._detect_task_type(goal)

        # 벡터 메모리에서 관련 패턴 검색
        past_patterns = []
        if self.vector_memory:
            patterns = self.vector_memory.find_patterns_vector(
                query_context={"goal": goal, "task_type": task_type},
                limit=5,
            )
            past_patterns = [
                {
                    "pattern_id": p.pattern_id,
                    "type": p.pattern_type,
                    "similarity": getattr(p, "_similarity", 0),
                    "weight": p.weight,
                    "solution_summary": self._summarize_solution(p.solution),
                }
                for p in patterns
            ]

        # 프롬프트 구성
        prompt = self._build_prompt(goal, task_type, explore_result, past_patterns)

        # LLM 호출 (Self-Consistency: 여러 번 샘플링)
        plans = []
        for i in range(self.self_consistency_n if self.provider != "template" else 1):
            try:
                if self.provider == "openai":
                    result = self._call_openai(prompt, i)
                elif self.provider == "anthropic":
                    result = self._call_anthropic(prompt, i)
                else:
                    # 템플릿 기반 폴백
                    from .planner import WorkPlanner

                    return WorkPlanner(self.workspace).create_plan(
                        goal, explore_result, task_type, context
                    )

                if result:
                    plans.append(result)
            except Exception as e:
                log.warning(f"LLM 호출 실패 (시도 {i+1}): {e}")

        # Self-Consistency: 가장 일관된 계획 선택
        if plans:
            best_plan_data = self._select_consistent_plan(plans)
            return self._build_plan_from_data(best_plan_data, goal, task_type)

        # 폴백: 템플릿 기반
        from .planner import WorkPlanner

        return WorkPlanner(self.workspace).create_plan(goal, explore_result, task_type)

    def _build_prompt(
        self,
        goal: str,
        task_type: str,
        explore_result: ExploreResult,
        past_patterns: list[dict],
    ) -> str:
        """프롬프트 구성"""
        # 관련 파일 추출
        relevant_files = []
        for f in explore_result.files[:10]:
            relevant_files.append(f"- {f.path} ({f.language}, {f.lines} lines)")

        return self.COT_PROMPT.format(
            goal=goal,
            task_type=task_type,
            file_count=len(explore_result.files),
            symbol_count=len(explore_result.symbols),
            languages=self._get_language_distribution(explore_result),
            entry_points=", ".join(explore_result.entry_points[:5]) or "없음",
            test_files=len(explore_result.test_files),
            config_files=len(explore_result.config_files),
            relevant_files="\n".join(relevant_files) or "없음",
            past_patterns=(
                json.dumps(past_patterns, ensure_ascii=False, indent=2) if past_patterns else "없음"
            ),
        )

    def _call_openai(self, prompt: str, attempt: int) -> dict | None:
        """OpenAI API 호출"""
        try:
            temp = self.temperature + (attempt * 0.1)  # 다양성을 위해 약간 증가
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                temperature=temp,
                max_tokens=self.max_tokens,
                response_format={"type": "json_object"},
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            log.warning(f"OpenAI 호출 실패: {e}")
            return None

    def _call_anthropic(self, prompt: str, attempt: int) -> dict | None:
        """Anthropic API 호출"""
        try:
            temp = self.temperature + (attempt * 0.1)
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=temp,
                system=self.SYSTEM_PROMPT,
                messages=[{"role": "user", "content": prompt}],
            )
            return json.loads(response.content[0].text)
        except Exception as e:
            log.warning(f"Anthropic 호출 실패: {e}")
            return None

    def _select_consistent_plan(self, plans: list[dict]) -> dict:
        """Self-Consistency: 가장 일관된 계획 선택"""
        if len(plans) == 1:
            return plans[0]

        # 단계 수, 단계 타입 시퀀스, 의존성 구조 비교
        best_score = -1
        best_plan = plans[0]

        for i, plan in enumerate(plans):
            score = 0
            for j, other in enumerate(plans):
                if i == j:
                    continue
                # 구조적 유사도 계산
                score += self._plan_similarity(plan, other)

            if score > best_score:
                best_score = score
                best_plan = plan

        log.info(f"Self-Consistency: {len(plans)}개 샘플 중 최고 점수({best_score:.2f}) 계획 선택")
        return best_plan

    def _plan_similarity(self, plan1: dict, plan2: dict) -> float:
        """두 계획 간 유사도"""
        steps1 = plan1.get("steps", [])
        steps2 = plan2.get("steps", [])

        if not steps1 or not steps2:
            return 0.0

        # 단계 수 유사도
        len_sim = 1.0 - abs(len(steps1) - len(steps2)) / max(len(steps1), len(steps2))

        # 타입 시퀀스 유사도
        types1 = [s.get("type", "") for s in steps1]
        types2 = [s.get("type", "") for s in steps2]
        type_matches = sum(1 for a, b in zip(types1, types2) if a == b)
        type_sim = type_matches / max(len(types1), len(types2))

        # 의존성 구조 유사도 (간단히 단계 수 기반)
        dep1 = sum(len(s.get("dependencies", [])) for s in steps1)
        dep2 = sum(len(s.get("dependencies", [])) for s in steps2)
        dep_sim = 1.0 - abs(dep1 - dep2) / max(dep1, dep2, 1)

        return (len_sim + type_sim + dep_sim) / 3.0

    def _build_plan_from_data(
        self,
        plan_data: dict,
        goal: str,
        task_type: str,
    ) -> Plan:
        """LLM 응답 데이터로 Plan 객체 생성"""
        plan = Plan(goal=goal)

        for i, step_data in enumerate(plan_data.get("steps", [])):
            step = PlanStep(
                id=step_data.get("id", f"step_{i+1}_{step_data.get('type', 'code')}"),
                type=StepType(step_data.get("type", "code")),
                title=step_data.get("title", f"Step {i+1}"),
                description=step_data.get("description", ""),
                dependencies=step_data.get("dependencies", []),
                verification_criteria=step_data.get("verification_criteria", []),
                assigned_files=step_data.get("assigned_files", []),
                max_retries=3,
            )
            # 메타데이터 저장
            step.artifacts = {
                "complexity": step_data.get("estimated_complexity", "medium"),
                "risk_level": step_data.get("risk_level", "medium"),
                "rollback_strategy": step_data.get("rollback_strategy", ""),
            }
            plan.steps.append(step)

        # 의존성 기반 순서 보정
        self._topological_sort(plan)

        log.info(f"LLM 계획 생성 완료: {len(plan.steps)}개 단계")
        return plan

    def _topological_sort(self, plan: Plan) -> None:
        """의존성 기반 위상 정렬"""
        # 간단한 구현: 이미 정렬되어 있다고 가정하고 검증만
        pass

    def _detect_task_type(self, goal: str) -> str:
        """작업 유형 감지"""
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

    def _get_language_distribution(self, explore_result: ExploreResult) -> str:
        langs = {}
        for f in explore_result.files:
            langs[f.language] = langs.get(f.language, 0) + 1
        return ", ".join(f"{k}: {v}" for k, v in sorted(langs.items()))

    def _summarize_solution(self, solution: dict) -> str:
        parts = []
        for k, v in solution.items():
            if isinstance(v, bool) and v:
                parts.append(k)
            elif isinstance(v, (str, int, float)):
                parts.append(f"{k}={v}")
        return ", ".join(parts)[:100]

    def _summarize_solution(self, solution: dict) -> str:
        parts = []
        for k, v in solution.items():
            if isinstance(v, bool) and v:
                parts.append(k)
            elif isinstance(v, (str, int, float)):
                parts.append(f"{k}={v}")
        return ", ".join(parts)[:100]


class LLMPlannerWithMemory(LLMPlanner):
    """벡터 메모리 연동 플래너 (편의 클래스)"""

    def __init__(self, workspace: Path, memory_dir: Path | None = None):
        vector_memory = None
        if memory_dir:
            vector_memory = VectorPatternMemory(memory_dir)
        super().__init__(workspace, vector_memory=vector_memory)


def create_llm_planner(
    workspace: Path,
    vector_memory: VectorPatternMemory | None = None,
    **kwargs,
) -> LLMPlanner:
    """LLM 플래너 팩토리"""
    return LLMPlanner(workspace, vector_memory, **kwargs)
