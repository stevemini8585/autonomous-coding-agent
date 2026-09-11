"""week3_4 테스트 — ContextManager / Telemetry / EscalationManager"""

import pytest

from autonomous_coding_agent.week3_4 import (
    ContextManager,
    EscalationManager,
    Telemetry,
    create_context_manager,
    create_escalation_manager,
    create_telemetry,
)


class TestContextManager:
    def test_priority_order(self):
        cm = ContextManager(max_tokens=100000)
        cm.set_layer("recent_history", "히스토리")
        cm.set_layer("goal", "목표")
        pkg = cm.build_package()
        assert [l.name for l in pkg.layers] == ["goal", "recent_history"]

    def test_budget_enforced(self):
        cm = ContextManager(max_tokens=100)
        cm.set_layer("goal", "짧은 목표")
        cm.set_layer("full_files", "긴 내용 " * 5000)
        pkg = cm.build_package()
        assert pkg.total_tokens <= 100
        assert "goal" in [l.name for l in pkg.layers]
        assert pkg.truncated is True

    def test_goal_always_included(self):
        cm = ContextManager(max_tokens=50)
        cm.set_layer("goal", "반드시 포함될 목표")
        pkg = cm.build_package()
        assert "goal" in [l.name for l in pkg.layers]

    def test_format_prompt(self):
        cm = ContextManager()
        cm.set_layer("goal", "목표 텍스트")
        text = cm.format_for_prompt()
        assert "GOAL" in text and "목표 텍스트" in text

    def test_clear(self):
        cm = ContextManager()
        cm.set_layer("goal", "x")
        cm.clear_layer("goal")
        assert cm.get_layer("goal") is None
        cm.set_layer("a", "x")
        cm.clear_all()
        assert cm.get_stats()["layers"] == 0

    def test_stats(self):
        cm = ContextManager(max_tokens=500)
        cm.set_layer("goal", "목표")
        stats = cm.get_stats()
        assert stats["layers"] == 1 and stats["budget"] == 500

    def test_factory(self):
        assert isinstance(create_context_manager(), ContextManager)


class TestTelemetry:
    def test_record_and_summary(self, tmp_path):
        t = Telemetry(log_dir=tmp_path, flush_interval_sec=9999)
        try:
            t.record("ollama", "llama3.1:8b", 100, 50, 1200, True)
            t.record("ollama", "llama3.1:8b", 100, 0, 500, False, error="timeout")
            s = t.get_summary()
            assert s.total_calls == 2
            assert s.total_tokens == 250
            assert abs(s.success_rate - 0.5) < 0.01
            assert abs(s.avg_latency_ms - 850.0) < 0.01
            assert s.by_provider["ollama"]["calls"] == 2
            assert s.estimated_cost_usd == 0.0  # 로컬 무료
        finally:
            t.shutdown()

    def test_paid_cost(self, tmp_path):
        t = Telemetry(log_dir=tmp_path, flush_interval_sec=9999)
        try:
            t.record("openrouter", "openai/gpt-4o-mini", 1000, 500, 800, True)
            s = t.get_summary()
            expected = (1000 / 1000) * 0.15 + (500 / 1000) * 0.6
            assert abs(s.estimated_cost_usd - expected) < 1e-9
        finally:
            t.shutdown()

    def test_empty_summary(self, tmp_path):
        t = Telemetry(log_dir=tmp_path, flush_interval_sec=9999)
        try:
            s = t.get_summary()
            assert s.total_calls == 0 and s.success_rate == 1.0
        finally:
            t.shutdown()

    def test_flush_writes_jsonl(self, tmp_path):
        t = Telemetry(log_dir=tmp_path, flush_interval_sec=9999)
        try:
            t.record("ollama", "llama3.1:8b", 10, 5, 100, True)
            t.flush()
            files = list(tmp_path.glob("telemetry_*.jsonl"))
            assert len(files) == 1
            assert "llama3.1:8b" in files[0].read_text(encoding="utf-8")
        finally:
            t.shutdown()

    def test_factory(self, tmp_path):
        assert isinstance(create_telemetry(log_dir=tmp_path), Telemetry)


class TestEscalationManager:
    def test_max_retries_escalation(self, tmp_path):
        em = EscalationManager(tmp_path, notify_telegram=False)
        esc = em.check_and_escalate("s1", "에러", 3, 3, {})
        assert esc is not None
        assert esc.severity == "blocked"
        assert "3회" in esc.reason

    def test_repeated_error_escalation(self, tmp_path):
        em = EscalationManager(tmp_path, notify_telegram=False)
        esc = em.check_and_escalate("s1", "같은에러", 1, 5, {"recent_errors": ["같은에러"] * 3})
        assert esc is not None
        assert esc.severity == "degraded"

    def test_no_escalation_when_healthy(self, tmp_path):
        em = EscalationManager(tmp_path, notify_telegram=False)
        assert em.check_and_escalate("s1", "에러", 1, 5, {}) is None

    def test_lifecycle(self, tmp_path):
        em = EscalationManager(tmp_path, notify_telegram=False)
        esc = em.escalate("이유", {"k": "v"}, severity="uncertain")
        assert esc.status == "pending"
        assert em.acknowledge(esc.id, "steve") is True
        assert em.resolve(esc.id, "해결됨", "steve") is True
        assert em.get_pending() == []
        assert em.get_stats()["by_status"]["resolved"] == 1

    def test_reject(self, tmp_path):
        em = EscalationManager(tmp_path, notify_telegram=False)
        esc = em.escalate("이유", {})
        assert em.reject(esc.id, "계속 시도") is True
        assert em.get_stats()["by_status"]["rejected"] == 1

    def test_unknown_id(self, tmp_path):
        em = EscalationManager(tmp_path, notify_telegram=False)
        assert em.acknowledge("nope", "x") is False
        assert em.resolve("nope", "x", "y") is False
        assert em.reject("nope", "x") is False

    def test_factory(self, tmp_path):
        assert isinstance(create_escalation_manager(tmp_path), EscalationManager)
