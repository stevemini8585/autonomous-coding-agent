"""완전 자동화 파이프라인(Autopilot) 테스트 — 외부(gh/LLM) 스텁"""

from pathlib import Path

import pytest

from autonomous_coding_agent.autopilot import (
    Autopilot,
    AutopilotConfig,
    create_autopilot,
)
from autonomous_coding_agent.github import GitHubIssue
from autonomous_coding_agent.models import AgentResult
from autonomous_coding_agent.pr_reviewer import PRReviewResult


def _issue(n=1, labels=None, state="open"):
    return GitHubIssue(
        number=n,
        title=f"버그 {n}",
        body="버그 수정",
        state=state,
        labels=labels or [],
        assignees=[],
        created_at="",
        updated_at="",
        url=f"https://x/{n}",
    )


class StubGitHub:
    def __init__(self, issues=None):
        self.issues = {i.number: i for i in (issues or [])}
        self.comments = []
        self.merged = []

    def get_issue(self, n):
        return self.issues.get(n)

    def list_issues(self, state="open", labels=None, limit=20):
        return [i for i in self.issues.values() if i.state == state][:limit]

    def add_comment(self, n, body):
        self.comments.append((n, body))
        return True

    def create_pr(self, **kwargs):
        return 99

    def get_pr(self, n):
        return None

    def get_repo_info(self):
        return None  # 리뷰 생략 경로

    def merge_pr(self, n, method="squash", delete_branch=True):
        self.merged.append(n)
        return True


class StubWorkflow:
    def __init__(self):
        self.branches = []
        self.pushed = []

    def create_feature_branch(self, n, title):
        b = f"issue-{n}-x"
        self.branches.append(b)
        return b

    def commit_changes(self, msg, files=None):
        return "abc123"

    def push_branch(self, branch=None):
        self.pushed.append(branch)
        return True

    def create_pr_from_issue(self, n, branch, base="main"):
        return 99


class StubAgent:
    def __init__(self, ok=True):
        self.ok = ok

    def run(self, goal):
        if self.ok:
            return AgentResult(success=True, summary="done", files_changed=["a.py"])
        return AgentResult(success=False, summary="fail", error="boom")


@pytest.fixture
def pilot(tmp_path):
    p = Autopilot.__new__(Autopilot)
    p.workspace = Path(tmp_path)
    p.config = AutopilotConfig()
    return p


def _wire(pilot, issues, agent_ok=True):
    pilot.github = StubGitHub(issues)
    pilot.workflow = StubWorkflow()
    pilot._make_agent = lambda: StubAgent(ok=agent_ok)  # noqa: SLF001
    return pilot


class TestShouldProcess:
    def test_open_ok(self, pilot):
        ok, _ = pilot.should_process(_issue())
        assert ok

    def test_closed_skip(self, pilot):
        ok, reason = pilot.should_process(_issue(state="closed"))
        assert not ok and "closed" in reason

    def test_skip_label(self, pilot):
        ok, reason = pilot.should_process(_issue(labels=["needs-human"]))
        assert not ok and "needs-human" in reason

    def test_only_labels(self, pilot):
        pilot.config.only_labels = ["auto"]
        assert pilot.should_process(_issue(labels=["auto"]))[0]
        assert not pilot.should_process(_issue(labels=["other"]))[0]


class TestBuildGoal:
    def test_goal_contains_issue(self, pilot):
        from autonomous_coding_agent.issue_parser import IssueParser

        pilot.parser = IssueParser()
        goal = pilot.build_goal(_issue(7))
        assert "#7" in goal and "버그 7" in goal


class TestRunIssue:
    def test_missing_issue(self, pilot):
        _wire(pilot, [])
        r = pilot.run_issue(42)
        assert r.stage == "failed" and "조회 실패" in (r.error or "")

    def test_skipped(self, pilot):
        _wire(pilot, [_issue(1, state="closed")])
        r = pilot.run_issue(1)
        assert r.stage == "skipped"

    def test_dry_run(self, pilot):
        from autonomous_coding_agent.issue_parser import IssueParser

        pilot.config.dry_run = True
        pilot.parser = IssueParser()
        _wire(pilot, [_issue(1)])
        r = pilot.run_issue(1)
        assert r.stage == "planned" and "dry-run" in r.gate_summary
        assert pilot.workflow.branches == []  # 브랜치도 안 만듦

    def test_full_merge(self, pilot, tmp_path):
        from autonomous_coding_agent.issue_parser import IssueParser

        pilot.parser = IssueParser()
        (Path(tmp_path) / "a.py").write_text("x = 1\nprint(x)\n")
        _wire(pilot, [_issue(1)])
        r = pilot.run_issue(1)
        assert r.stage == "merged" and r.merged and r.pr_number == 99
        assert 99 in pilot.github.merged
        assert any("머지 완료" in c[1] for c in pilot.github.comments)

    def test_agent_failure(self, pilot):
        from autonomous_coding_agent.issue_parser import IssueParser

        pilot.parser = IssueParser()
        _wire(pilot, [_issue(1)], agent_ok=False)
        r = pilot.run_issue(1)
        assert r.stage == "failed" and r.error == "boom"
        assert any("자동 처리 실패" in c[1] for c in pilot.github.comments)

    def test_gate_block(self, pilot, tmp_path):
        from autonomous_coding_agent.issue_parser import IssueParser

        pilot.parser = IssueParser()
        (Path(tmp_path) / "a.py").write_text("print(zzz_no_such_var_xyz)\n")
        _wire(pilot, [_issue(1)])
        r = pilot.run_issue(1)
        assert r.stage == "failed" and "게이트 차단" in (r.error or "")
        assert r.pr_number is None  # PR 만들지 않음

    def test_gate_bypass_when_not_required(self, pilot, tmp_path):
        from autonomous_coding_agent.issue_parser import IssueParser

        pilot.parser = IssueParser()
        pilot.config.require_gate_pass = False
        (Path(tmp_path) / "a.py").write_text("print(zzz_no_such_var_xyz)\n")
        _wire(pilot, [_issue(1)])
        r = pilot.run_issue(1)
        assert r.stage == "merged" and r.pr_number == 99

    def test_review_block(self, pilot, tmp_path):
        from autonomous_coding_agent.issue_parser import IssueParser
        from autonomous_coding_agent.pr_reviewer import PRReviewer

        pilot.parser = IssueParser()
        (Path(tmp_path) / "a.py").write_text("x = 1\nprint(x)\n")
        _wire(pilot, [_issue(1)])
        pilot.github.get_repo_info = lambda: {"owner": {"login": "o"}, "name": "r"}
        bad = PRReviewResult(
            pr_number=99,
            repo="o/r",
            total_comments=1,
            critical_count=1,
            error_count=0,
            warning_count=0,
            info_count=0,
            nit_count=0,
        )
        pilot.reviewer = PRReviewer(str(tmp_path))
        pilot.reviewer.review_pr = lambda *a, **k: bad
        r = pilot.run_issue(1)
        assert r.stage == "failed" and "리뷰 차단" in (r.error or "")
        assert 99 not in pilot.github.merged


class TestRunOnce:
    def test_max_issues(self, pilot):
        from autonomous_coding_agent.issue_parser import IssueParser

        pilot.parser = IssueParser()
        pilot.config.max_issues = 2
        issues = [_issue(1), _issue(2), _issue(3)]
        _wire(pilot, issues)
        out = pilot.run_once()
        assert len(out.runs) == 2

    def test_skipped_not_counted(self, pilot):
        from autonomous_coding_agent.issue_parser import IssueParser

        pilot.parser = IssueParser()
        pilot.config.max_issues = 2
        issues = [_issue(1, labels=["needs-human"]), _issue(2), _issue(3)]
        _wire(pilot, issues)
        out = pilot.run_once()
        assert len(out.runs) == 3  # 스킵은上限 미포함
        assert out.skipped == [1]

    def test_result_dict(self, pilot):
        _wire(pilot, [_issue(1, labels=["wontfix"])])
        d = pilot.run_once().to_dict()
        assert d["skipped"] == [1] and d["merged"] == []

    def test_factory(self, tmp_path):
        import subprocess

        subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
        assert isinstance(create_autopilot(tmp_path), Autopilot)
        assert "max_issues" in AutopilotConfig().to_dict()
