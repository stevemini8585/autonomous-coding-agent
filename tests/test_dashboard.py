"""Tests for dashboard module"""

import pytest
from fastapi.testclient import TestClient

from autonomous_coding_agent import (
    AutopilotRun,
    DashboardServer,
    SessionProgress,
    StepProgress,
    get_dashboard,
)

# Test constants
TEST_PORT = 8899
TEST_TOTAL_STEPS = 5
EXPECTED_PROGRESS = 0.5
MIN_PATTERNS = 2


def test_session_progress():
    """Test SessionProgress dataclass"""
    session = SessionProgress(
        session_id="test-123",
        goal="Test goal",
        status="running",
        total_steps=TEST_TOTAL_STEPS,
    )

    assert session.session_id == "test-123"
    assert session.goal == "Test goal"
    assert session.status == "running"
    assert session.total_steps == TEST_TOTAL_STEPS
    assert session.current_step == 0
    assert session.overall_progress == 0.0

    # Test to_dict
    d = session.to_dict()
    assert d["session_id"] == "test-123"
    assert d["goal"] == "Test goal"


def test_step_progress():
    """Test StepProgress dataclass"""
    step = StepProgress(
        step_id="step-1",
        title="Test step",
        status="pending",
    )

    assert step.step_id == "step-1"
    assert step.title == "Test step"
    assert step.status == "pending"
    assert step.progress == 0.0


def test_dashboard_server_creation():
    """Test DashboardServer creation"""
    dashboard = DashboardServer(host="127.0.0.1", port=TEST_PORT)

    assert dashboard.host == "127.0.0.1"
    assert dashboard.port == TEST_PORT
    assert dashboard.app is not None
    assert len(dashboard.sessions) == 0


def test_dashboard_singleton():
    """Test get_dashboard singleton"""
    d1 = get_dashboard("127.0.0.1", TEST_PORT)
    d2 = get_dashboard("127.0.0.1", TEST_PORT)
    assert d1 is d2


def test_session_progress_update():
    """Test overall progress calculation"""
    session = SessionProgress(
        session_id="test",
        goal="Test",
        status="running",
        total_steps=3,
    )

    # Add steps
    session.steps["step1"] = StepProgress(
        step_id="step1", title="Step 1", status="completed", progress=1.0
    )
    session.steps["step2"] = StepProgress(
        step_id="step2", title="Step 2", status="running", progress=0.5
    )
    session.steps["step3"] = StepProgress(
        step_id="step3", title="Step 3", status="pending", progress=0.0
    )

    # Calculate overall
    total = sum(s.progress for s in session.steps.values())
    overall = total / len(session.steps)

    assert overall == (1.0 + 0.5 + 0.0) / 3
    assert overall == EXPECTED_PROGRESS


if __name__ == "__main__":
    pytest.main([__file__, "-v"])


class TestAutopilotTab:
    def test_run_dataclass(self):
        run = AutopilotRun(
            issue_number=7, stage="merged", merged=True, pr_number=9, pr_url="https://x/pull/9"
        )
        d = run.to_dict()
        assert d["issue_number"] == 7 and d["merged"] is True
        assert d["pr_url"] == "https://x/pull/9"

    def test_report_upsert(self):
        dash = DashboardServer(host="127.0.0.1", port=TEST_PORT)
        dash.report_autopilot({"issue_number": 1, "stage": "planned"})
        dash.report_autopilot({"issue_number": 1, "stage": "merged", "merged": True})
        assert len(dash.autopilot_runs) == 1
        assert dash.autopilot_runs[1].stage == "merged"

    def test_api_list(self):
        dash = DashboardServer(host="127.0.0.1", port=TEST_PORT)
        dash.report_autopilot({"issue_number": 3, "stage": "failed", "error": "boom"})
        client = TestClient(dash.app)
        res = client.get("/api/autopilot")
        assert res.status_code == 200
        runs = res.json()["runs"]
        assert len(runs) == 1 and runs[0]["issue_number"] == 3

    def test_api_report(self):
        dash = DashboardServer(host="127.0.0.1", port=TEST_PORT)
        client = TestClient(dash.app)
        res = client.post(
            "/api/autopilot/report", json={"issue_number": 5, "stage": "pr_opened", "pr_number": 11}
        )
        assert res.status_code == 200
        assert res.json()["run"]["pr_number"] == 11
        assert dash.autopilot_runs[5].stage == "pr_opened"

    def test_api_report_missing_number(self):
        dash = DashboardServer(host="127.0.0.1", port=TEST_PORT)
        client = TestClient(dash.app)
        res = client.post("/api/autopilot/report", json={"stage": "x"})
        assert res.status_code == 400

    def test_index_renders(self):
        dash = DashboardServer(host="127.0.0.1", port=TEST_PORT)
        client = TestClient(dash.app)
        res = client.get("/")
        assert res.status_code == 200
        assert "Autopilot Runs" in res.text
        assert "/api/autopilot" in res.text

    def test_broadcast_message(self):
        import asyncio

        dash = DashboardServer(host="127.0.0.1", port=TEST_PORT)
        received = []

        class FakeWS:
            async def send_json(self, msg):
                received.append(msg)

        run = dash.report_autopilot({"issue_number": 2, "stage": "merged"})
        dash.manager.active_connections.append(FakeWS())  # type: ignore[arg-type]
        asyncio.run(dash.broadcast_autopilot(run))
        assert received and received[0]["type"] == "autopilot_update"
        assert received[0]["run"]["issue_number"] == 2

    def test_autopilot_wiring(self, tmp_path):
        from autonomous_coding_agent.autopilot import Autopilot, AutopilotConfig
        from autonomous_coding_agent.github import GitHubIssue
        from autonomous_coding_agent.issue_parser import IssueParser

        class StubGitHub:
            def list_issues(self, state="open", labels=None, limit=20):
                return [
                    GitHubIssue(
                        number=1,
                        title="t",
                        body="b",
                        state="OPEN",
                        labels=[],
                        assignees=[],
                        created_at="",
                        updated_at="",
                        url="",
                    )
                ]

            def get_issue(self, n):
                return self.list_issues()[0]

        dash = DashboardServer(host="127.0.0.1", port=TEST_PORT)
        pilot = Autopilot.__new__(Autopilot)
        pilot.workspace = tmp_path
        pilot.config = AutopilotConfig(dry_run=True, notify_telegram=False)
        pilot.dashboard = dash
        pilot.parser = IssueParser()
        pilot.github = StubGitHub()  # type: ignore[assignment]
        out = pilot.run_once()
        assert out.runs and dash.autopilot_runs[1].stage == "planned"

    def test_no_dashboard_ok(self, tmp_path):
        from autonomous_coding_agent.autopilot import Autopilot, AutopilotConfig

        pilot = Autopilot.__new__(Autopilot)
        pilot.workspace = tmp_path
        pilot.config = AutopilotConfig(notify_telegram=False)
        pilot.dashboard = None
        from autonomous_coding_agent.autopilot import IssueRunResult

        pilot._report_dashboard(IssueRunResult(issue_number=1))  # 예외 없어야 함
