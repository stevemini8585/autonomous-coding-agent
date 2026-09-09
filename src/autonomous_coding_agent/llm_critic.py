"""
LLM 기반 지능형 크리틱 (Critic v2)
- Chain-of-Thought 프롬프팅으로 깊은 코드 분석
- Self-Correction 루프 (반복적 개선)
- 벡터 메모리 연동 (과거 크리틱 패턴 학습)
- 의미적 코드 품질 메트릭 (AST 기반)
- 자동 리팩토링 제안
"""

from __future__ import annotations

import ast
import json
import logging
import os
import re
from pathlib import Path
from typing import Any

from .models import CritiqueResult, PlanStep, VerificationResult
from .vector_memory import VectorPatternMemory

log = logging.getLogger("autonomous_coding_agent.llm_critic")


class LLMCritic:
    """LLM 기반 지능형 크리틱"""

    SYSTEM_PROMPT = """당신은 세계 최고 수준의 코드 리뷰어이자 소프트웨어 품질 전문가입니다.
코드의 기능적 정확성, 가독성, 유지보수성, 성능, 보안을 종합적으로 평가하세요.

리뷰 원칙:
1. **기능적 정확성**: 요구사항 충족, 경계값 처리, 예외 상황 대응
2. **가독성**: 명명 규칙, 구조, 주석, 문서화
3. **유지보수성**: 모듈화, 결합도, 응집도, SOLID 원칙
4. **성능**: 알고리즘 복잡도, 메모리 효율, 불필요한 연산
5. **보안**: 입력 검증, 인젝션 방지, 시크릿 관리, 권한 제어
6. **테스트 가능성**: 단위 테스트 용이성, 모킹 용이성, 결정론적 동작

출력 형식: JSON (CritiqueResult 스키마 준수)"""

    COT_PROMPT = """검토 대상 코드:
```{language}
{code}
```

작업 컨텍스트:
- 목표: {goal}
- 단계: {step_title}
- 작업 유형: {task_type}

검증 결과:
- 테스트: {test_status} (커버리지: {coverage:.1f}%)
- 타입 체크: {type_status}
- 린트/포맷: {lint_status}
- 에러: {error_count}개
- 경고: {warning_count}개

과거 크리틱 패턴 (벡터 검색):
{past_critiques}

관련 파일:
{related_files}

---

다음 Chain-of-Thought로 깊이 분석하세요:

1. **기능적 정확성 검토**: 코드가 목표를 달성하는가? 경계값/예외 처리는?
2. **코드 품질 분석**: 가독성, 명명, 구조, 주석, 문서화 수준은?
3. **아키텍처/설계 평가**: 모듈화, 결합도/응집도, SOLID 원칙 준수는?
4. **성능/리소스 분석**: 알고리즘 복잡도, 메모리, 불필요한 연산, N+1 문제 등
5. **보안 취약점 스캔**: 입력 검증, 인젝션, 시크릿 하드코딩, 권한 처리
6. **테스트 품질**: 커버리지 충분? 경계값/예외/엣지케이스 커버?
6. **유지보수성**: 모듈화, 결합도/응집도, 문서화, 기술 부채
7. **과거 패턴 적용**: 유사한 과거 크리틱에서 배운 교훈 적용

출력 JSON 스키마:
{{
  "reasoning": "위 1-7번 분석 요약",
  "score": 0.85,
  "issues": [
    {{
      "type": "security|performance|maintainability|correctness|style",
      "severity": "critical|error|warning|info",
      "file": "path/to/file.py",
      "line": 42,
      "message": "구체적 이슈 설명",
      "suggestion": "구체적 수정 제안",
      "code_snippet": "문제의 코드 조각"
    }}
  ],
  "improvements": [
    "구체적 개선 제안 1",
    "구체적 개선 제안 2"
  ],
  "should_retry": false,
  "retry_feedback": "재시도 시 집중할 포인트"
}}"""

    def __init__(
        self,
        workspace: Path,
        vector_memory: VectorPatternMemory | None = None,
        model: str = "gpt-4o-mini",
        temperature: float = 0.2,
        max_tokens: int = 4000,
        self_correction_rounds: int = 2,
    ):
        self.workspace = Path(workspace).resolve()
        self.vector_memory = vector_memory
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.self_correction_rounds = self_correction_rounds

        self.client = None
        self.provider = "template"
        self._init_llm_client()

    def _init_llm_client(self):
        try:
            import openai

            if os.getenv("OPENAI_API_KEY"):
                self.client = openai.OpenAI()
                self.provider = "openai"
                log.info("OpenAI 클라이언트 초기화 (Critic)")
                return
        except ImportError:
            pass

        try:
            import anthropic

            if os.getenv("ANTHROPIC_API_KEY"):
                self.client = anthropic.Anthropic()
                self.provider = "anthropic"
                log.info("Anthropic 클라이언트 초기화 (Critic)")
                return
        except ImportError:
            pass

        log.warning("LLM 클라이언트 없음 - 템플릿 기반 크리틱으로 폴백")
        self.provider = "template"

    def critique(
        self,
        step: PlanStep,
        verification: VerificationResult,
        context: dict[str, Any],
    ) -> CritiqueResult:
        """LLM 기반 비평 수행 (Self-Correction 루프 포함)"""
        log.info(f"LLM 크리틱 시작: {step.id}")

        # 코드 수집
        code_files = self._collect_code_files(step, context)

        # 벡터 메모리에서 과거 크리틱 패턴 검색
        past_critiques = []
        if self.vector_memory:
            patterns = self.vector_memory.find_patterns_vector(
                query_context={"goal": context.get("goal", ""), "step_type": "critique"},
                limit=5,
            )
            past_critiques = [
                {
                    "pattern_id": p.pattern_id,
                    "type": p.pattern_type,
                    "similarity": getattr(p, "_similarity", 0),
                    "weight": p.weight,
                    "summary": self._summarize_solution(p.solution),
                }
                for p in patterns
            ]

        # Self-Correction 루프
        best_critique = None
        best_score = -1

        for round_num in range(self.self_correction_rounds + 1):
            log.info(f"크리틱 라운드 {round_num + 1}/{self.self_correction_rounds + 1}")

            try:
                if self.provider == "openai":
                    result = self._call_openai_critique(
                        step, verification, context, code_files, past_critiques, round_num
                    )
                elif self.provider == "anthropic":
                    result = self._call_anthropic_critique(
                        step, verification, context, code_files, past_critiques, round_num
                    )
                else:
                    # 템플릿 기반 폴백
                    from .critic import Critic

                    return Critic(self.workspace).critique(step, verification, context)

                if result:
                    # 품질 점수로 평가 (이슈 수, 심각도, 구체성)
                    quality = self._evaluate_critique_quality(result)
                    if quality > best_score:
                        best_score = quality
                        best_critique = result
                        log.info(f"라운드 {round_num + 1}: 품질 점수 {quality:.2f} (최고 갱신)")
                    else:
                        log.info(
                            f"라운드 {round_num + 1}: 품질 점수 {quality:.2f} (최고 {best_score:.2f} 유지)"
                        )

            except Exception as e:
                log.warning(f"크리틱 라운드 {round_num + 1} 실패: {e}")

        if best_critique:
            critique_result = self._build_critique_result(best_critique, step.id)
            log.info(
                f"크리틱 완료: 점수={critique_result.score:.2f}, 이슈={len(critique_result.issues)}개"
            )
            return critique_result

        # 폴백: 템플릿 기반
        from .critic import Critic

        return Critic(self.workspace).critique(step, verification, context)

    def _collect_code_files(self, step: PlanStep, context: dict[str, Any]) -> dict[str, str]:
        """단계 관련 코드 파일 수집"""
        import contextlib

        code_files = {}

        # 할당된 파일들
        for file_path in step.assigned_files:
            full_path = self.workspace / file_path
            if full_path.exists():
                with contextlib.suppress(Exception):
                    code_files[file_path] = full_path.read_text(encoding="utf-8")

        # 아티팩트에서 생성/수정된 파일들
        for file_path in step.artifacts.get("files_created", []):
            full_path = self.workspace / file_path
            if full_path.exists():
                with contextlib.suppress(Exception):
                    code_files[file_path] = full_path.read_text(encoding="utf-8")

        for file_path in step.artifacts.get("files_modified", []):
            full_path = self.workspace / file_path
            if full_path.exists():
                with contextlib.suppress(Exception):
                    code_files[file_path] = full_path.read_text(encoding="utf-8")

        return code_files

    def _build_critique_prompt(
        self,
        step: PlanStep,
        verification: VerificationResult,
        context: dict[str, Any],
        code_files: dict[str, str],
        past_critiques: list[dict],
    ) -> str:
        """크리틱 프롬프트 구성"""
        # 코드 통합
        code_combined = ""
        for path, content in code_files.items():
            lang = self._detect_language(Path(path))
            code_combined += f"\n--- {path} ---\n```{lang}\n{content}\n```\n"

        if not code_combined:
            code_combined = "코드 파일이 없습니다 (탐색 단계 등)"

        # 검증 상태 문자열
        test_status = "통과" if verification.test_results.get("passed", True) else "실패"
        type_status = "통과" if verification.type_results.get("passed", True) else "실패"
        lint_status = "통과" if verification.lint_results.get("passed", True) else "실패"

        # 관련 파일 목록
        related = "\n".join(f"- {p}" for p in code_files) or "없음"

        return self.COT_PROMPT.format(
            language=self._detect_main_language(code_files),
            code=code_combined[:15000],  # 토큰 제한 고려
            goal=context.get("goal", "알 수 없음"),
            step_title=step.title,
            task_type=context.get("task_type", "feature"),
            test_status=test_status,
            coverage=verification.coverage,
            type_status="통과" if verification.type_results.get("passed", True) else "실패",
            lint_status="통과" if verification.lint_results.get("passed", True) else "실패",
            error_count=len(verification.errors),
            warning_count=len(verification.warnings),
            past_critiques=(
                json.dumps(past_critiques, ensure_ascii=False, indent=2)
                if past_critiques
                else "없음"
            ),
            related_files=related or "없음",
        )

    def _call_openai_critique(
        self,
        step: PlanStep,
        verification: VerificationResult,
        context: dict[str, Any],
        code_files: dict[str, str],
        past_critiques: list[dict],
        round_num: int,
    ) -> dict | None:
        """OpenAI API로 크리틱 수행"""
        try:
            import openai

            prompt = self._build_critique_prompt(
                step, verification, context, code_files, past_critiques
            )

            temp = self.temperature + (round_num * 0.05)
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                temperature=self.temperature + (round_num * 0.05),
                max_tokens=self.max_tokens,
                response_format={"type": "json_object"},
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            log.warning(f"OpenAI 크리틱 호출 실패: {e}")
            return None

    def _call_anthropic_critique(
        self,
        step: PlanStep,
        verification: VerificationResult,
        context: dict[str, Any],
        code_files: dict[str, str],
        past_critiques: list[dict],
        round_num: int,
    ) -> dict | None:
        try:
            import anthropic

            prompt = self._build_critique_prompt(
                step, verification, context, code_files, past_critiques
            )

            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                temperature=self.temperature + (round_num * 0.05),
                system=self.SYSTEM_PROMPT,
                messages=[{"role": "user", "content": prompt}],
            )
            return json.loads(response.content[0].text)
        except Exception as e:
            log.warning(f"Anthropic 크리틱 호출 실패: {e}")
            return None

    def _evaluate_critique_quality(self, critique: dict) -> float:
        """크리틱 품질 평가 (Self-Correction용)"""
        score = 0.0

        # 이슈 구체성 (파일, 라인, 코드 스니펫 포함 여부)
        issues = critique.get("issues", [])
        if issues:
            specificity = sum(
                1 for i in issues if i.get("file") and i.get("line") and i.get("code_snippet")
            ) / len(issues)
            score += specificity * 0.3

        # 이슈 다양성 (타입별 분포)
        types = {i.get("type", "") for i in issues}
        score += min(len(types) / 5.0, 1.0) * 0.2

        # 개선 제안 구체성
        improvements = critique.get("improvements", [])
        if improvements:
            avg_len = sum(len(imp) for imp in improvements) / len(improvements)
            score += min(avg_len / 100.0, 1.0) * 0.2

        # 추론 과정 품질
        reasoning = critique.get("reasoning", "")
        score += min(len(reasoning) / 500.0, 1.0) * 0.3

        return min(score, 1.0)

    def _build_critique_result(self, critique: dict, step_id: str) -> CritiqueResult:
        """딕셔너리를 CritiqueResult 객체로 변환"""
        result = CritiqueResult(step_id=step_id)
        result.score = critique.get("score", 0.5)

        # 이슈 변환
        for issue in critique.get("issues", []):
            result.issues.append(
                {
                    "type": issue.get("type", "style"),
                    "severity": issue.get("severity", "info"),
                    "file": issue.get("file", ""),
                    "line": issue.get("line", 0),
                    "message": issue.get("message", ""),
                    "suggestion": issue.get("suggestion", ""),
                }
            )

        result.improvements = critique.get("improvements", [])
        result.should_retry = critique.get("should_retry", False)
        result.retry_feedback = critique.get("retry_feedback", "")

        # 메타데이터 저장
        result.artifacts = {
            "reasoning": critique.get("reasoning", ""),
        }

        return result

    def _detect_language(self, file_path: Path) -> str:
        suffix = file_path.suffix.lower()
        lang_map = {
            ".py": "python",
            ".js": "javascript",
            ".ts": "typescript",
            ".go": "go",
            ".rs": "rust",
            ".java": "java",
            ".cpp": "cpp",
            ".c": "c",
            ".cs": "csharp",
        }
        return lang_map.get(suffix, "text")

    def _detect_main_language(self, code_files: dict[str, str]) -> str:
        for path in code_files:
            lang = self._detect_language(Path(path))
            if lang != "text":
                return lang
        return "python"

    def _summarize_solution(self, solution: dict) -> str:
        parts = []
        for k, v in solution.items():
            if isinstance(v, bool) and v:
                parts.append(k)
            elif isinstance(v, (str, int, float)):
                parts.append(f"{k}={v}")
        return ", ".join(parts)[:100]


class LLMCriticWithMemory(LLMCritic):
    """벡터 메모리 연동 크리틱 (편의 클래스)"""

    def __init__(self, workspace: Path, memory_dir: Path | None = None):
        vector_memory = None
        if memory_dir:
            vector_memory = VectorPatternMemory(memory_dir)
        super().__init__(workspace, vector_memory=vector_memory)


def create_llm_critic(
    workspace: Path,
    vector_memory: VectorPatternMemory | None = None,
    **kwargs,
) -> LLMCritic:
    """LLM 크리틱 팩토리"""
    return LLMCritic(workspace, vector_memory, **kwargs)
