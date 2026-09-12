"""
컨텍스트 관리 + 텔레메트리 + 에스컬레이션 (Week 3-4)
- ContextManager: 계층적 요약 + 토큰 예산 강제 + 관련도 프루닝
- Telemetry: 토큰/비용/레이턴시/호출횟수 수집·리포트
- EscalationManager: 자동화 한계 시 사람 개입 요청·승인·피드백 루프
"""

from __future__ import annotations

import json
import logging
import os
import threading
import time
import uuid
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from .llm_client import chat

log = logging.getLogger("autonomous_coding_agent.week3_4")


# ============================================================================
# 1. ContextManager — 계층적 컨텍스트 관리
# ============================================================================


@dataclass
class ContextLayer:
    """컨텍스트 레이어 (계층별)"""

    name: str  # "file", "module", "architecture", "goal"
    content: str  # 실제 텍스트
    tokens: int  # 예상 토큰 수
    priority: int  # 높을수록 유지 (0~100)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class ContextPackage:
    """LLM에 주입할 최종 컨텍스트 패키지"""

    layers: list[ContextLayer]
    total_tokens: int
    budget_tokens: int
    truncated: bool = False


class ContextManager:
    """
    계층적 컨텍스트 관리 + 토큰 예산 강제.
    - 레이어: goal(최고) > memory > codebase_rag > explore > recent_errors > history
    - 토큰 예산 초과 시 낮은 우선순위부터 프루닝
    - 관련도 점수로 동적 재정렬
    """

    # 레이어 우선순위 (높을수록 중요)
    LAYER_PRIORITIES = {
        "goal": 100,  # 작업 목표 (항상 포함)
        "memory_hint": 90,  # 과거 성공 패턴 힌트
        "codebase_rag": 80,  # RAG 검색 결과
        "explore_symbols": 70,  # 탐색된 심볼
        "assigned_files": 65,  # 담당 파일 내용
        "verification_errors": 60,  # 검증 에러/경고
        "critique_feedback": 55,  # 비평 피드백
        "recent_history": 30,  # 최근 대화/시도
        "full_files": 20,  # 전체 파일 내용 (마지막)
    }

    def __init__(
        self,
        max_tokens: int = 15000,
        token_per_char: float = 0.25,  # 대략적 추정 (한글/영문 혼합)
    ):
        self.max_tokens = max_tokens
        self.token_per_char = token_per_char
        self._layers: dict[str, ContextLayer] = {}
        self._lock = threading.Lock()

    def estimate_tokens(self, text: str) -> int:
        return int(len(text) * self.token_per_char)

    def set_layer(self, name: str, content: str, priority: int | None = None, **metadata) -> None:
        """레이어 설정/업데이트"""
        tokens = self.estimate_tokens(content)
        prio = priority if priority is not None else self.LAYER_PRIORITIES.get(name, 50)
        with self._lock:
            self._layers[name] = ContextLayer(
                name=name,
                content=content,
                tokens=tokens,
                priority=prio,
                metadata=metadata,
            )

    def get_layer(self, name: str) -> ContextLayer | None:
        with self._lock:
            return self._layers.get(name)

    def build_package(self, max_tokens: int | None = None) -> ContextPackage:
        """최종 컨텍스트 패키지 구성 (예산 내 프루닝)"""
        budget = max_tokens or self.max_tokens
        with self._lock:
            layers = list(self._layers.values())

        # 우선순위 내림차순 정렬
        layers.sort(key=lambda layer: layer.priority, reverse=True)

        selected = []
        total = 0
        truncated = False

        for layer in layers:
            if total + layer.tokens <= budget:
                selected.append(layer)
                total += layer.tokens
            else:
                # 잘라서라도 넣을 수 있으면 넣기 (goal 등 최상위만)
                if layer.priority >= 90 and total < budget:
                    remaining = budget - total
                    if remaining > 100:
                        cut_content = layer.content[: int(remaining / self.token_per_char)]
                        selected.append(
                            ContextLayer(
                                name=layer.name,
                                content=cut_content + "\n... (truncated)",
                                tokens=remaining,
                                priority=layer.priority,
                                metadata={**layer.metadata, "truncated": True},
                            )
                        )
                        total = budget
                truncated = True
                # 예산 초과면 이후 레이어는 버림

        return ContextPackage(
            layers=selected,
            total_tokens=total,
            budget_tokens=budget,
            truncated=truncated,
        )

    def format_for_prompt(self, pkg: ContextPackage | None = None) -> str:
        """프롬프트용 문자열 생성"""
        if pkg is None:
            pkg = self.build_package()
        parts = []
        for layer in pkg.layers:
            parts.append(
                f"=== {layer.name.upper()} (priority: {layer.priority}, tokens: {layer.tokens}) ==="
            )
            parts.append(layer.content)
            parts.append("")
        if pkg.truncated:
            parts.append("... (일부 컨텍스트는 토큰 예산 초과로 생략됨)")
        return "\n".join(parts).strip()

    def clear_layer(self, name: str) -> None:
        with self._lock:
            self._layers.pop(name, None)

    def clear_all(self) -> None:
        with self._lock:
            self._layers.clear()

    def get_stats(self) -> dict[str, Any]:
        with self._lock:
            return {
                "layers": len(self._layers),
                "total_tokens": sum(L.tokens for L in self._layers.values()),
                "budget": self.max_tokens,
                "layers_detail": {
                    name: {"tokens": L.tokens, "priority": L.priority}
                    for name, L in self._layers.items()
                },
            }


# ============================================================================
# 2. Telemetry — 토큰/비용/레이턴시 관측
# ============================================================================


@dataclass
class LLMCallRecord:
    """단일 LLM 호출 기록"""

    timestamp: str
    provider: str
    model: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    latency_ms: int
    success: bool
    error: str | None = None
    context: dict[str, Any] = field(default_factory=dict)  # goal, step_id 등


@dataclass
class TelemetrySummary:
    """텔레메트리 요약"""

    total_calls: int
    total_tokens: int
    total_prompt_tokens: int
    total_completion_tokens: int
    avg_latency_ms: float
    success_rate: float
    by_provider: dict[str, dict[str, Any]]
    estimated_cost_usd: float


class Telemetry:
    """
    LLM 호출 텔레메트리 수집·리포트.
    - 스레드 세이프
    - 인메모리 + 주기적 디스크 플러시 (JSONL)
    - 제공자별/모델별 비용 추정 (가격표 내장)
    """

    # 제공자별 1K 토큰당 가격 (USD, 2024 기준 대략치)
    PRICING = {
        "openrouter": {
            "anthropic/claude-3.5-sonnet": {"input": 3.0, "output": 15.0},
            "anthropic/claude-3-opus": {"input": 15.0, "output": 75.0},
            "openai/gpt-4o": {"input": 5.0, "output": 15.0},
            "openai/gpt-4o-mini": {"input": 0.15, "output": 0.6},
        },
        "openai": {
            "gpt-4o": {"input": 5.0, "output": 15.0},
            "gpt-4o-mini": {"input": 0.15, "output": 0.6},
        },
        "anthropic": {
            "claude-3.5-sonnet": {"input": 3.0, "output": 15.0},
        },
        "ollama": {  # 로컬 = 비용 0
            "llama3.1:8b": {"input": 0.0, "output": 0.0},
        },
    }

    def __init__(
        self,
        log_dir: Path | None = None,
        flush_interval_sec: int = 60,
    ):
        self.log_dir = Path(log_dir or Path.cwd() / ".telemetry")
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.flush_interval = flush_interval_sec

        self._records: list[LLMCallRecord] = []
        self._lock = threading.Lock()
        self._flush_thread: threading.Thread | None = None
        self._stop_flush = threading.Event()

        self._start_flush_loop()

    def _start_flush_loop(self) -> None:
        def loop():
            while not self._stop_flush.wait(self.flush_interval):
                self.flush()

        self._flush_thread = threading.Thread(target=loop, daemon=True)
        self._flush_thread.start()

    def record(
        self,
        provider: str,
        model: str,
        prompt_tokens: int,
        completion_tokens: int,
        latency_ms: int,
        success: bool,
        error: str | None = None,
        **context,
    ) -> None:
        """호출 기록"""
        record = LLMCallRecord(
            timestamp=datetime.utcnow().isoformat() + "Z",
            provider=provider,
            model=model,
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=prompt_tokens + completion_tokens,
            latency_ms=latency_ms,
            success=success,
            error=error,
            context=context,
        )
        with self._lock:
            self._records.append(record)

    def flush(self) -> None:
        """디스크에 JSONL 기록"""
        with self._lock:
            if not self._records:
                return
            records = self._records[:]
            self._records.clear()

        log_file = self.log_dir / f"telemetry_{datetime.utcnow().strftime('%Y%m%d')}.jsonl"
        try:
            with log_file.open("a", encoding="utf-8") as f:
                for r in records:
                    f.write(json.dumps(r.__dict__, ensure_ascii=False) + "\n")
        except Exception as e:
            log.warning(f"텔레메트리 플러시 실패: {e}")

    def get_summary(self, since_hours: int = 24) -> TelemetrySummary:
        """요약 통계"""
        cutoff = time.time() - since_hours * 3600
        with self._lock:
            records = [
                r
                for r in self._records
                if datetime.fromisoformat(r.timestamp.replace("Z", "+00:00")).timestamp() > cutoff
            ]

        if not records:
            return TelemetrySummary(
                total_calls=0,
                total_tokens=0,
                total_prompt_tokens=0,
                total_completion_tokens=0,
                avg_latency_ms=0.0,
                success_rate=1.0,
                by_provider={},
                estimated_cost_usd=0.0,
            )

        total_calls = len(records)
        total_tokens = sum(r.total_tokens for r in records)
        total_prompt = sum(r.prompt_tokens for r in records)
        total_completion = sum(r.completion_tokens for r in records)
        avg_latency = sum(r.latency_ms for r in records) / total_calls
        success_rate = sum(1 for r in records if r.success) / total_calls

        # 제공자별 집계
        by_provider: dict[str, dict[str, float]] = defaultdict(
            lambda: {"calls": 0.0, "tokens": 0.0, "latency_sum": 0.0, "success": 0.0}
        )
        for r in records:
            by_provider[r.provider]["calls"] += 1
            by_provider[r.provider]["tokens"] += r.total_tokens
            by_provider[r.provider]["latency_sum"] += r.latency_ms
            if r.success:
                by_provider[r.provider]["success"] += 1

        for prov, stats in by_provider.items():
            stats["avg_latency_ms"] = float(stats["latency_sum"]) / stats["calls"]
            stats["success_rate"] = float(stats["success"]) / stats["calls"]

        # 비용 추정
        cost = 0.0
        for r in records:
            pricing = self.PRICING.get(r.provider, {}).get(r.model)
            if pricing:
                cost += (r.prompt_tokens / 1000) * pricing["input"]
                cost += (r.completion_tokens / 1000) * pricing["output"]

        return TelemetrySummary(
            total_calls=total_calls,
            total_tokens=total_tokens,
            total_prompt_tokens=total_prompt,
            total_completion_tokens=total_completion,
            avg_latency_ms=avg_latency,
            success_rate=success_rate,
            by_provider=dict(by_provider),
            estimated_cost_usd=cost,
        )

    def shutdown(self) -> None:
        self._stop_flush.set()
        if self._flush_thread:
            self._flush_thread.join(timeout=5)
        self.flush()


# 전역 텔레메트리 인스턴스 (싱글톤 패턴)
_global_telemetry: Telemetry | None = None
_telemetry_lock = threading.Lock()


def get_telemetry(log_dir: Path | None = None) -> Telemetry:
    """전역 텔레메트리 인스턴스 획득"""
    global _global_telemetry
    with _telemetry_lock:
        if _global_telemetry is None:
            _global_telemetry = Telemetry(log_dir)
        return _global_telemetry


def record_llm_call(
    provider: str,
    model: str,
    prompt_tokens: int,
    completion_tokens: int,
    latency_ms: int,
    success: bool,
    error: str | None = None,
    **context,
) -> None:
    """편의 함수: 전역 텔레메트리에 기록"""
    get_telemetry().record(
        provider, model, prompt_tokens, completion_tokens, latency_ms, success, error, **context
    )


# ============================================================================
# 3. EscalationManager — 사람 개입 에스컬레이션
# ============================================================================


@dataclass
class EscalationRequest:
    """에스컬레이션 요청"""

    id: str
    timestamp: str
    reason: str  # 왜 에스컬레이션이 필요한가
    context: dict[str, Any]  # 관련 컨텍스트 (goal, errors, attempt 등)
    severity: str  # "blocked", "degraded", "uncertain", "policy"
    proposed_actions: list[str] = field(default_factory=list)  # 제안 행동
    status: str = "pending"  # "pending", "acknowledged", "resolved", "rejected"
    assignee: str | None = None  # 담당자 (슬랙/이메일/깃헙 유저)
    resolution: str | None = None  # 해결 내용
    resolved_at: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


class EscalationManager:
    """
    자동화 한계 도달 시 사람 개입 요청·승인·피드백 루프.
    - 트리거: max_retries 초과, 게이트 지속 차단, LLM 실패 반복, 정책 위반
    - 알림 채널: 텔레그램, 깃헙 이슈 코멘트, (향후 슬랙/이메일)
    - 승인/거절/피드백 수신 → 자동 재시도 또는 계획 변경
    """

    def __init__(
        self,
        workspace: Path,
        notify_telegram: bool = True,
        github_repo: str | None = None,
    ):
        self.workspace = Path(workspace).resolve()
        self.notify_telegram = notify_telegram
        self.github_repo = github_repo
        self._escalations: dict[str, EscalationRequest] = {}
        self._lock = threading.Lock()

        # 텔레그램 알림 함수 (지연 임포트)
        self._notify_fn = None
        if notify_telegram:
            try:
                from .notify import send_telegram

                self._notify_fn = send_telegram
            except ImportError:
                pass

    def escalate(
        self,
        reason: str,
        context: dict[str, Any],
        severity: str = "blocked",
        proposed_actions: list[str] | None = None,
        assignee: str | None = None,
    ) -> EscalationRequest:
        """새 에스컬레이션 생성"""
        esc = EscalationRequest(
            id=f"esc_{uuid.uuid4().hex[:8]}",
            timestamp=datetime.utcnow().isoformat() + "Z",
            reason=reason,
            context=context,
            severity=severity,
            proposed_actions=proposed_actions or [],
            assignee=assignee,
        )
        with self._lock:
            self._escalations[esc.id] = esc

        # 알림 발송
        self._notify(esc)

        log.warning(f"🚨 에스컬레이션 생성: {esc.id} ({severity}) - {reason}")
        return esc

    def _notify(self, esc: EscalationRequest) -> None:
        """알림 발송 (텔레그램 + 깃헙 이슈 코멘트)"""
        msg = (
            f"🚨 <b>에스컬레이션 발생</b> [{esc.severity.upper()}]\n"
            f"ID: {esc.id}\n"
            f"사유: {esc.reason}\n"
            f"심각도: {esc.severity}\n"
            f"제안 행동:\n" + "\n".join(f"  - {a}" for a in esc.proposed_actions) + "\n"
            f"컨텍스트: {json.dumps(esc.context, ensure_ascii=False)[:500]}"
        )

        # 텔레그램
        if self._notify_fn:
            try:
                self._notify_fn(msg)
            except Exception as e:
                log.warning(f"텔레그램 에스컬레이션 알림 실패: {e}")

        # 깃헙 이슈에 코멘트 (이슈 번호가 컨텍스트에 있는 경우)
        if self.github_repo and "issue_number" in esc.context:
            try:
                import subprocess

                issue_num = esc.context["issue_number"]
                comment = f"🚨 자동 에스컬레이션 발생\n\n{msg}"
                subprocess.run(
                    [
                        "gh",
                        "issue",
                        "comment",
                        str(issue_num),
                        "-R",
                        self.github_repo,
                        "--body",
                        comment,
                    ],
                    cwd=self.workspace,
                    capture_output=True,
                    timeout=30,
                )
            except Exception as e:
                log.warning(f"깃헙 에스컬레이션 코멘트 실패: {e}")

    def acknowledge(self, esc_id: str, assignee: str) -> bool:
        """담당자 확인"""
        with self._lock:
            esc = self._escalations.get(esc_id)
            if not esc:
                return False
            esc.status = "acknowledged"
            esc.assignee = assignee
            return True

    def resolve(self, esc_id: str, resolution: str, resolved_by: str) -> bool:
        """해결 처리"""
        with self._lock:
            esc = self._escalations.get(esc_id)
            if not esc:
                return False
            esc.status = "resolved"
            esc.resolution = resolution
            esc.resolved_at = datetime.utcnow().isoformat() + "Z"
            esc.assignee = resolved_by
            return True

    def reject(self, esc_id: str, reason: str) -> bool:
        """거절 (자동화 계속 시도 또는 다른 경로)"""
        with self._lock:
            esc = self._escalations.get(esc_id)
            if not esc:
                return False
            esc.status = "rejected"
            esc.resolution = f"거절: {reason}"
            esc.resolved_at = datetime.utcnow().isoformat() + "Z"
            return True

    def get_pending(self) -> list[EscalationRequest]:
        """대기 중인 에스컬레이션 목록"""
        with self._lock:
            return [e for e in self._escalations.values() if e.status == "pending"]

    def get_stats(self) -> dict[str, Any]:
        with self._lock:
            statuses = defaultdict(int)
            for e in self._escalations.values():
                statuses[e.status] += 1
            return {
                "total": len(self._escalations),
                "by_status": dict(statuses),
                "pending": len([e for e in self._escalations.values() if e.status == "pending"]),
            }

    # 자동 트리거 헬퍼 (에이전트/오토파일럿에서 호출)
    def check_and_escalate(
        self,
        step_id: str,
        error: str,
        retry_count: int,
        max_retries: int,
        context: dict[str, Any],
    ) -> EscalationRequest | None:
        """자동 에스컬레이션 조건 확인 및 생성"""
        # 1. 최대 재시도 초과
        if retry_count >= max_retries:
            return self.escalate(
                reason=f"단계 {step_id} 최대 재시도({max_retries}회) 초과",
                context={
                    **context,
                    "step_id": step_id,
                    "retry_count": retry_count,
                    "last_error": error,
                },
                severity="blocked",
                proposed_actions=[
                    "이슈 분해 후 서브태스크로 재시도",
                    "사람이 직접 코드 수정 후 PR",
                    "목표 범위 축소 후 재시도",
                ],
            )

        # 2. 동일 에러 반복 (3회 이상)
        recent_errors = context.get("recent_errors", [])
        if recent_errors.count(error) >= 3:
            return self.escalate(
                reason=f"동일 에러 3회 반복: {error[:100]}",
                context={
                    **context,
                    "step_id": step_id,
                    "error": error,
                    "repeat_count": recent_errors.count(error),
                },
                severity="degraded",
                proposed_actions=[
                    "에러 원인 수동 분석 후 패치",
                    "다른 접근법(라이브러리/알고리즘) 시도",
                ],
            )

        return None


def create_context_manager(**kwargs) -> ContextManager:
    return ContextManager(**kwargs)


def create_telemetry(**kwargs) -> Telemetry:
    return Telemetry(**kwargs)


def get_global_telemetry(**kwargs) -> Telemetry:
    return get_telemetry(**kwargs)


def create_escalation_manager(workspace: Path | str, **kwargs) -> EscalationManager:
    return EscalationManager(Path(workspace), **kwargs)
