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
        """get_issue 함수.

        Args:
            self: 매개변수 설명.
            n: 매개변수 설명.

        Returns:
            결과값.
        """
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
    def __init__(self, workspace=None, wt_base="/tmp"):
        self.branches = []
        self.pushed = []
        self.worktrees = []
        self.removed = []
        self._ws = Path(workspace) if workspace else None
        self._wt_base = Path(wt_base)

    def create_feature_branch(self, n, title):
        b = f"issue-{n}-x"
        self.branches.append(b)
        return b

    def create_worktree(self, n, title, base="main"):
        b = f"issue-{n}-x"
        self.branches.append(b)
        wt = self._wt_base / f"wt-{n}"
        wt.mkdir(parents=True, exist_ok=True)
        self.worktrees.append(wt)
        return b, wt

    def remove_worktree(self, path, missing_ok=True):
        self.removed.append(Path(path))
        return True

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


def _wire(pilot, issues, agent_ok=True, wt_base="/tmp"):
    pilot.github = StubGitHub(issues)
    pilot.workflow = StubWorkflow(wt_base=wt_base)
    pilot._make_agent = lambda workspace=None: StubAgent(ok=agent_ok)  # noqa: SLF001
    pilot._make_workflow = StubWorkflow  # noqa: SLF001
    return pilot


class TestShouldProcess:
    def test_open_ok(self, pilot):
        ok, _ = pilot.should_process(_issue())
        assert ok

    def test_closed_skip(self, pilot):
        ok, reason = pilot.should_process(_issue(state="closed"))
        assert not ok and "closed" in reason

    def test_uppercase_open_ok(self, pilot):
        # gh CLI는 state를 "OPEN" 대문자로 반환 — 회귀 테스트
        ok, _ = pilot.should_process(_issue(state="OPEN"))
        assert ok

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
        assert pilot.workflow.branches == []  # 브랜치도 worktree도 안 만듦

    def test_full_merge(self, pilot, tmp_path):
        from autonomous_coding_agent.issue_parser import IssueParser

        pilot.parser = IssueParser()
        (Path(tmp_path) / "wt-1").mkdir(parents=True, exist_ok=True)
        (Path(tmp_path) / "wt-1" / "a.py").write_text("x = 1\nprint(x)\n")
        _wire(pilot, [_issue(1)], wt_base=str(tmp_path))
        r = pilot.run_issue(1)
        assert r.stage == "merged" and r.merged and r.pr_number == 99
        assert 99 in pilot.github.merged
        assert any("머지 완료" in c[1] for c in pilot.github.comments)

    def test_agent_failure(self, pilot, tmp_path):
        from autonomous_coding_agent.issue_parser import IssueParser

        pilot.parser = IssueParser()
        _wire(pilot, [_issue(1)], agent_ok=False, wt_base=str(tmp_path))
        r = pilot.run_issue(1)
        assert r.stage == "failed" and r.error == "boom"
        assert any("자동 처리 실패" in c[1] for c in pilot.github.comments)

    def test_gate_block(self, pilot, tmp_path):
        from autonomous_coding_agent.issue_parser import IssueParser

        pilot.parser = IssueParser()
        (Path(tmp_path) / "wt-1").mkdir(parents=True, exist_ok=True)
        (Path(tmp_path) / "wt-1" / "a.py").write_text("print(zzz_no_such_var_xyz)\n")
        _wire(pilot, [_issue(1)], wt_base=str(tmp_path))
        r = pilot.run_issue(1)
        assert r.stage == "failed" and "게이트 차단" in (r.error or "")
        assert r.pr_number is None  # PR 만들지 않음

    def test_gate_bypass_when_not_required(self, pilot, tmp_path):
        from autonomous_coding_agent.issue_parser import IssueParser

        pilot.parser = IssueParser()
        pilot.config.require_gate_pass = False
        (Path(tmp_path) / "wt-1").mkdir(parents=True, exist_ok=True)
        (Path(tmp_path) / "wt-1" / "a.py").write_text("print(zzz_no_such_var_xyz)\n")
        _wire(pilot, [_issue(1)], wt_base=str(tmp_path))
        r = pilot.run_issue(1)
        assert r.stage == "merged" and r.pr_number == 99

    def test_review_block(self, pilot, tmp_path):
        from autonomous_coding_agent.issue_parser import IssueParser
        from autonomous_coding_agent.pr_reviewer import PRReviewer

        pilot.parser = IssueParser()
        (Path(tmp_path) / "wt-1").mkdir(parents=True, exist_ok=True)
        (Path(tmp_path) / "wt-1" / "a.py").write_text("x = 1\nprint(x)\n")
        _wire(pilot, [_issue(1)], wt_base=str(tmp_path))
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
        pilot._make_reviewer = lambda wt: pilot.reviewer  # noqa: SLF001
        r = pilot.run_issue(1)
        assert r.stage == "failed" and "리뷰 차단" in (r.error or "")
        assert 99 not in pilot.github.merged


class TestWorktree:
    def test_uses_worktree_and_cleans_up(self, pilot, tmp_path):
        from autonomous_coding_agent.issue_parser import IssueParser

        pilot.parser = IssueParser()
        (tmp_path / "wt-1").mkdir(exist_ok=True)
        (tmp_path / "wt-1" / "a.py").write_text("x = 1\nprint(x)\n")
        _wire(pilot, [_issue(1)], wt_base=str(tmp_path))
        r = pilot.run_issue(1)
        assert r.merged
        assert pilot.workflow.worktrees != []  # worktree 경유
        assert pilot.workflow.removed != []  # 머지 후 정리

    def test_failure_keeps_worktree(self, pilot, tmp_path):
        from autonomous_coding_agent.issue_parser import IssueParser

        pilot.parser = IssueParser()
        _wire(pilot, [_issue(1)], agent_ok=False, wt_base=str(tmp_path))
        r = pilot.run_issue(1)
        assert r.stage == "failed"
        assert pilot.workflow.worktrees != []
        assert pilot.workflow.removed == []  # 실패 시 조사용 보존

    def test_real_git_worktree(self, tmp_path):
        import subprocess

        from autonomous_coding_agent.git_integration import GitWorkflow

        repo = tmp_path / "repo"
        repo.mkdir()
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        subprocess.run(["git", "config", "user.email", "t@t"], cwd=repo, check=True)
        subprocess.run(["git", "config", "user.name", "t"], cwd=repo, check=True)
        (repo / "a.txt").write_text("hi\n")
        subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
        subprocess.run(["git", "commit", "-qm", "init"], cwd=repo, check=True)
        subprocess.run(["git", "branch", "-M", "main"], cwd=repo, check=True)

        flow = GitWorkflow(repo)
        branch, wt = flow.create_worktree(7, "Add thing")
        try:
            assert branch == "issue-7-add-thing"
            assert (wt / "a.txt").read_text() == "hi\n"
            # 현재 체크아웃 불변
            cur = subprocess.run(
                ["git", "branch", "--show-current"],
                cwd=repo,
                capture_output=True,
                text=True,
            ).stdout.strip()
            assert cur == "main"
        finally:
            assert flow.remove_worktree(wt) is True
        assert not wt.exists()


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


class TestNotify:
    def test_merged_notifies(self, pilot, tmp_path, monkeypatch):
        import autonomous_coding_agent.autopilot as ap
        from autonomous_coding_agent.issue_parser import IssueParser

        sent = []
        monkeypatch.setattr(ap, "send_telegram", lambda msg: sent.append(msg) or True)
        pilot.parser = IssueParser()
        (tmp_path / "wt-1").mkdir(exist_ok=True)
        (tmp_path / "wt-1" / "a.py").write_text("x = 1\nprint(x)\n")
        _wire(pilot, [_issue(1)], wt_base=str(tmp_path))
        r = pilot.run_issue(1)
        assert r.merged
        assert any("머지 완료" in m for m in sent)

    def test_failure_notifies(self, pilot, tmp_path, monkeypatch):
        import autonomous_coding_agent.autopilot as ap
        from autonomous_coding_agent.issue_parser import IssueParser

        sent = []
        monkeypatch.setattr(ap, "send_telegram", lambda msg: sent.append(msg) or True)
        pilot.parser = IssueParser()
        _wire(pilot, [_issue(1)], agent_ok=False, wt_base=str(tmp_path))
        pilot.run_issue(1)
        assert any("구현 실패" in m for m in sent)

    def test_notify_disabled(self, pilot, tmp_path, monkeypatch):
        import autonomous_coding_agent.autopilot as ap
        from autonomous_coding_agent.issue_parser import IssueParser

        sent = []
        monkeypatch.setattr(ap, "send_telegram", lambda msg: sent.append(msg) or True)
        pilot.parser = IssueParser()
        pilot.config.notify_telegram = False
        _wire(pilot, [_issue(1)], agent_ok=False, wt_base=str(tmp_path))
        pilot.run_issue(1)
        assert sent == []


class TestNotifyModule:
    def test_no_credentials_returns_false(self, monkeypatch):
        from autonomous_coding_agent.notify import send_telegram

        monkeypatch.delenv("TELEGRAM_BOT_TOKEN", raising=False)
        monkeypatch.delenv("TELEGRAM_CHAT_ID", raising=False)
        assert send_telegram("hi") is False

    def test_network_failure_returns_false(self, monkeypatch):
        import urllib.request

        from autonomous_coding_agent.notify import send_telegram

        monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "x")
        monkeypatch.setenv("TELEGRAM_CHAT_ID", "y")

        def boom(*a, **k):
            raise OSError("net down")

        monkeypatch.setattr(urllib.request, "urlopen", boom)
        assert send_telegram("hi") is False


class TestReviewScoping:
    def test_make_reviewer_binds_workspace(self):
        from autonomous_coding_agent.autopilot import Autopilot

        pilot = Autopilot(".")
        rev = pilot._make_reviewer(".")  # noqa: SLF001
        assert Path(rev.workspace).resolve() == Path().resolve()

    def test_create_pr_base_passthrough(self, tmp_path):
        import subprocess

        from autonomous_coding_agent.git_integration import GitWorkflow

        repo = tmp_path / "r"
        repo.mkdir()
        subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
        subprocess.run(["git", "config", "user.email", "t@t"], cwd=repo, check=True)
        subprocess.run(["git", "config", "user.name", "t"], cwd=repo, check=True)
        (repo / "a.txt").write_text("hi\n")
        subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
        subprocess.run(["git", "commit", "-qm", "init"], cwd=repo, check=True)

        seen = {}

        class FakeGH:
            def get_issue(self, n):
                from autonomous_coding_agent.github import GitHubIssue

                return GitHubIssue(
                    number=n,
                    title="t",
                    body="b",
                    state="open",
                    labels=[],
                    assignees=[],
                    created_at="",
                    updated_at="",
                    url="",
                )

            def create_pr(self, title, body, head, base="main", draft=False):
                seen["base"] = base
                return 99

            def add_comment(self, n, body):
                return True

        wf = GitWorkflow(repo)
        wf.github = FakeGH()  # type: ignore[assignment]
        wf.create_pr_from_issue(1, "b", base="test/feature-hello")
        assert seen["base"] == "test/feature-hello"


class TestMemoryWire:
    def test_disabled(self):
        from autonomous_coding_agent.autopilot import Autopilot, AutopilotConfig

        p = Autopilot(".", AutopilotConfig(use_memory=False))
        assert p.memory is None
        assert p._recall_hint("x") == ""  # noqa: SLF001

    def test_record_and_recall(self, tmp_path):
        import shutil

        from autonomous_coding_agent.autopilot import Autopilot, AutopilotConfig
        from autonomous_coding_agent.models import AgentResult

        p = Autopilot(".", AutopilotConfig(use_memory=True))
        if p.memory is None:
            pytest.skip("벡터 메모리 비활성 환경")
        n0 = len(p.memory.vector_patterns)
        p.memory.store_pattern(
            "autopilot_issue",
            {"goal": "리팩토링 테스트 목표", "title": "t"},
            {"stage": "merged"},
            {"success_rate": 1.0},
            tags=["merged"],
        )
        assert len(p.memory.vector_patterns) == n0 + 1
        hint = p._recall_hint("리팩토링 테스트 목표")  # noqa: SLF001
        assert isinstance(hint, str)
        shutil.rmtree(p.memory.memory_dir / "chroma", ignore_errors=True)
