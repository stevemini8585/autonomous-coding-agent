"""
LLM-first 코더 + Self-Correction 루프 (Week 3-1)
- 규칙 기반(기존 CodeGenerator)을 보조로, LLM을 주(主)로 사용
- 검증 실패 → Critic 비평 → revise() → 재검증 자동 루프 (max_rounds=3)
- 기존 가드레일·워크트리·메모리 인프라 그대로 재사용
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .coder import CodeGenerator, _parses
from .llm_client import chat
from .models import PlanStep, StepStatus, StepType, VerificationResult

log = logging.getLogger("autonomous_coding_agent.llm_coder")


@dataclass
class RefinementContext:
    """Self-Correction 라운드 간 전달 컨텍스트"""

    round_num: int = 0
    critique_issues: list[dict[str, Any]] | None = None
    previous_attempts: list[str] | None = None  # 파일별 이전 시도 내용


class LLMCoder(CodeGenerator):
    """LLM-first 코드 생성기 + Self-Correction 루프 내장"""

    def __init__(
        self,
        workspace: Path,
        use_llm: bool = True,
        max_refinement_rounds: int = 3,
    ):
        super().__init__(workspace, use_llm=use_llm)
        self.max_refinement_rounds = max_refinement_rounds

    # ------------------------------------------------------------------
    # 공개 API: 에이전트/오토파일럿에서 호출
    # ------------------------------------------------------------------
    def execute_step_with_refinement(
        self,
        step: PlanStep,
        context: dict[str, Any],
        verifier: Any,  # Verifier 타입 순환 참조 방지
        critic: Any | None = None,  # Critic 선택적 주입
    ) -> dict[str, Any]:
        """
        LLM 생성 → 검증 → (실패 시) 비평 → 수정 → 재검증 루프.
        성공 시 artifacts 반환, 최종 실패 시 예외 발생(상위에서 잡음).
        """
        if not self.use_llm:
            # LLM 비활성 시 부모(규칙 기반) 경로로 폴백
            return super().execute_step(step, context)

        log.info(f"🤖 LLMCoder 시작: {step.id} (최대 {self.max_refinement_rounds} 라운드)")

        # 초기 컨텍스트 구성
        rctx = RefinementContext()
        last_verification = None

        for round_num in range(self.max_refinement_rounds + 1):
            rctx.round_num = round_num
            log.info(f"  🔄 라운드 {round_num + 1}/{self.max_refinement_rounds + 1}")

            # 1) LLM으로 구현 생성 (이전 라운드 피드백 반영)
            implementation = self._llm_implement(step, context, rctx)

            # 2) 파일 적용 (가드레일 통과 필수)
            artifacts = self._apply_implementation(step, implementation)
            if not artifacts.get("files_created") and not artifacts.get("files_modified"):
                log.warning("  ⚠ 적용된 변경 없음 — 다음 라운드 재시도")
                continue

            # 3) 검증 실행
            changed_files = artifacts.get("files_created", []) + artifacts.get("files_modified", [])
            verification = verifier.verify_step(step, changed_files)
            last_verification = verification

            if verification.passed:
                log.info(f"  ✅ 검증 통과 (라운드 {round_num + 1})")
                return artifacts

            log.warning(f"  ❌ 검증 실패: {verification.errors}")

            # 4) 마지막 라운드면 종료
            if round_num >= self.max_refinement_rounds:
                break

            # 5) Critic 비평 수집 (있으면)
            if critic is not None:
                try:
                    critique = critic.critique(step, verification, context)
                    rctx.critique_issues = self._critique_to_issues(critique)
                    log.info(f"  📋 비평 이슈 {len(rctx.critique_issues)}개 수신")
                except Exception as e:
                    log.warning(f"  ⚠ 비평 수집 실패: {e}")

            # 6) 검증 에러도 이슈로 변환
            rctx.critique_issues = (rctx.critique_issues or []) + [
                {"type": "verification_error", "message": err} for err in verification.errors
            ]

            # 7) 이전 시도 기록 (동일 파일 반복 방지)
            for f, content in implementation.items():
                rctx.previous_attempts = rctx.previous_attempts or []
                rctx.previous_attempts.append(f"--- {f} (round {round_num}) ---\n{content}")

        # 모든 라운드 실패
        raise RuntimeError(
            f"LLMCoder: {self.max_refinement_rounds + 1}라운드 내 검증 통과 실패 "
            f"(마지막 에러: {last_verification.errors if last_verification else 'unknown'})"
        )

    # ------------------------------------------------------------------
    # 내부 메서드
    # ------------------------------------------------------------------
    def _llm_implement(
        self,
        step: PlanStep,
        context: dict[str, Any],
        rctx: RefinementContext,
    ) -> dict[str, str]:
        """단일 라운드 LLM 구현 생성 (피드백 반영)"""
        goal = context.get("goal", "")
        explore_result = context.get("explore_result")
        implementations = {}

        for file_path in step.assigned_files:
            if not file_path.endswith(".py"):
                # 비파이썬은 기존 로직 위임
                implementations[file_path] = self._generate_task_specific_implementation(
                    step, goal, context
                ).get(file_path, "")
                continue

            full = self.workspace / file_path
            existing = full.read_text(encoding="utf-8") if full.exists() else ""

            # 프롬프트 구성
            prompt = self._build_implementation_prompt(
                file_path=file_path,
                existing=existing,
                goal=goal,
                explore_result=explore_result,
                rctx=rctx,
            )

            provider, text = chat(prompt, self._system_prompt())
            if provider == "none" or not text.strip():
                log.warning(f"  ⚠ LLM 응답 없음({provider}) — 기존 내용 유지: {file_path}")
                implementations[file_path] = existing
                continue

            content = self._clean_llm_output(text)
            if not _parses(content):
                log.warning(f"  ⚠ 신택스 오류로 버림: {file_path}")
                implementations[file_path] = existing
                continue

            implementations[file_path] = content

        return implementations

    def _build_implementation_prompt(
        self,
        file_path: str,
        existing: str,
        goal: str,
        explore_result: Any | None,
        rctx: RefinementContext,
    ) -> str:
        """구현 프롬프트 구성 (컨텍스트 압축 포함)"""
        # 탐색 결과 요약
        explore_summary = ""
        if explore_result and explore_result.symbols:
            symbols = [f"{s.name}({s.type})@{s.file_path}" for s in explore_result.symbols[:20]]
            explore_summary = f"관련 심볼: {', '.join(symbols)}"

        # 이전 시도 요약
        attempts_summary = ""
        if rctx.previous_attempts:
            attempts_summary = (
                f"\n이전 시도({len(rctx.previous_attempts)}회) — 동일 실수 반복 금지:\n"
                + "\n".join(rctx.previous_attempts[-3:])  # 최근 3회만
            )

        # 피드백 이슈
        feedback = ""
        if rctx.critique_issues:
            feedback = "\n수정해야 할 이슈:\n" + "\n".join(
                f"- [{i.get('type','?')}] {i.get('message','')}" for i in rctx.critique_issues[:10]
            )

        # 라운드 표시
        round_info = (
            f" (라운드 {rctx.round_num + 1}/{self.max_refinement_rounds + 1})"
            if rctx.round_num > 0
            else ""
        )

        return (
            f"파일: {file_path}{round_info}\n"
            f"목표: {goal}\n"
            f"{explore_summary}\n"
            f"{feedback}\n"
            f"{attempts_summary}\n\n"
            f"```python\n{existing[:12000]}\n```\n\n"
            f"위 파일을 목표에 맞게 수정해 **파일 전체**를 출력해. "
            f"설명·마크다운 펜스 없이 코드만. "
            f"이슈가 있으면 반드시 반영하고, 이미 잘 된 부분은 건드리지 마."
        )

    @staticmethod
    def _system_prompt() -> str:
        return (
            "너는 파이썬 코드 생성/수정 전문가다. "
            "요청된 목표만 최소 diff로 반영한 **파일 전체**를 출력한다. "
            "설명·마크다운 펜스 없이 코드만 출력한다. "
            "타입 힌트·docstring·에러 처리를 빠뜨리지 않는다."
        )

    @staticmethod
    def _clean_llm_output(text: str) -> str:
        text = text.strip()
        if text.startswith("```"):
            lines = text.split("\n")
            lines = lines[1:]
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            text = "\n".join(lines)
        return text

    @staticmethod
    def _critique_to_issues(critique: Any) -> list[dict[str, Any]]:
        """Critic 결과 → 구조화된 이슈 리스트"""
        issues = []
        if hasattr(critique, "issues"):
            for iss in critique.issues:
                issues.append(
                    {
                        "type": getattr(iss, "category", "critique"),
                        "severity": getattr(iss, "severity", "medium"),
                        "message": getattr(iss, "message", str(iss)),
                        "file": getattr(iss, "file_path", ""),
                        "line": getattr(iss, "line_start", 0),
                        "suggestion": getattr(iss, "suggestion", ""),
                    }
                )
        return issues

    def _apply_implementation(
        self,
        step: PlanStep,
        implementation: dict[str, str],
    ) -> dict[str, Any]:
        """구현 적용 (기존 _implement_code의 3단계 로직 재사용)"""
        artifacts = {"files_created": [], "files_modified": [], "patches_applied": []}

        # 백업
        for file_path in step.assigned_files:
            self._backup_file(file_path)

        patch_manager = self._make_patch_manager()
        operations = []

        for file_path, content in implementation.items():
            full = self.workspace / file_path
            if full.exists():
                operations.append(self._make_patch_operation(file_path, full.read_text(), content))
            else:
                if not _parses(content):
                    log.error("신규 파일 신택스 오류: %s", file_path)
                    artifacts.setdefault("files_rejected", []).append(file_path)
                    continue
                full.parent.mkdir(parents=True, exist_ok=True)
                full.write_text(content, encoding="utf-8")
                artifacts["files_created"].append(file_path)

        results = patch_manager.apply_patches(operations) if operations else []
        for r in results:
            if r.success and r.applied:
                artifacts["files_modified"].append(r.file_path)
            elif not r.success:
                log.error("패치 실패: %s - %s", r.file_path, r.error)
                artifacts.setdefault("files_rejected", []).append(r.file_path)

        artifacts["patches_applied"] = [
            {"file": r.file_path, "applied": r.applied, "hunks": r.hunks_applied}
            for r in results
            if r.applied
        ]
        return artifacts

    # 기존 private 메서드 위임용 래퍼
    def _make_patch_manager(self):
        from .patch_utils import PatchManager

        return PatchManager(self.workspace)

    def _make_patch_operation(self, file_path, old, new):
        from .patch_utils import PatchOperation

        return PatchOperation(
            file_path=file_path,
            old_content=old,
            new_content=new,
            description=f"LLM update {file_path}",
        )


# 편의 팩토리
def create_llm_coder(workspace: Path | str, **kwargs) -> LLMCoder:
    return LLMCoder(Path(workspace), **kwargs)
