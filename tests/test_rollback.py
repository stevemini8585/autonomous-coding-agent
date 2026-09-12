"""오머지 롤백 자동화 테스트 (subprocess 스텁)"""

import subprocess

import pytest

from autonomous_coding_agent.rollback import (
    RollbackConfig,
    RollbackError,
    execute_rollback,
    main,
    plan_rollback,
    rollback_pr,
    working_tree_clean,
)

PR_VIEW = {
    "number": 10,
    "title": "feat X",
    "state": "MERGED",
    "mergeCommit": {"oid": "abc123"},
    "baseRefName": "main",
    "headRefName": "issue-10-x",
    "url": "https://github.com/o/r/pull/10",
    "closingIssuesReferences": [{"number": 7}],
}


class FakeCompleted:
    def __init__(self, returncode=0, stdout="", stderr=""):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


def _fake_run_factory(cmds, pr_view=None, dirty=False):
    import json

    def fake(cmd, **kwargs):
        cmds.append(cmd)
        if cmd[:3] == ["gh", "pr", "view"]:
            return FakeCompleted(0, json.dumps(pr_view if pr_view is not None else PR_VIEW))
        if cmd[:2] == ["git", "status"]:
            return FakeCompleted(0, " M x.py" if dirty else "")
        if cmd[:3] == ["gh", "pr", "create"]:
            return FakeCompleted(0, "https://github.com/o/r/pull/11\n")
        return FakeCompleted(0, "")

    return fake


class TestPlan:
    def test_plan_ok(self, tmp_path, monkeypatch):
        cmds = []
        monkeypatch.setattr(subprocess, "run", _fake_run_factory(cmds))
        plan = plan_rollback(10, tmp_path)
        assert plan.merge_sha == "abc123"
        assert plan.branch == "revert/pr-10"
        assert plan.linked_issues == [7]
        assert len(plan.steps) == 6  # 5 + 이슈 1
        assert cmds == [
            [
                "gh",
                "pr",
                "view",
                "10",
                "--json",
                "number,title,state,mergeCommit,baseRefName,headRefName,url,"
                "closingIssuesReferences",
            ]
        ]

    def test_not_merged(self, tmp_path, monkeypatch):
        view = dict(PR_VIEW, state="OPEN")
        monkeypatch.setattr(subprocess, "run", _fake_run_factory([], pr_view=view))
        with pytest.raises(RollbackError, match="머지 상태가 아님"):
            plan_rollback(10, tmp_path)

    def test_missing(self, tmp_path, monkeypatch):
        cmds = []
        monkeypatch.setattr(
            subprocess,
            "run",
            lambda cmd, **k: cmds.append(cmd) or FakeCompleted(1, "", "not found"),
        )
        with pytest.raises(RollbackError, match="조회 실패"):
            plan_rollback(99, tmp_path)
        assert cmds and cmds[0][:3] == ["gh", "pr", "view"]

    def test_no_merge_sha(self, tmp_path, monkeypatch):
        view = dict(PR_VIEW, mergeCommit=None)
        monkeypatch.setattr(subprocess, "run", _fake_run_factory([], pr_view=view))
        with pytest.raises(RollbackError, match="머지 커밋 없음"):
            plan_rollback(10, tmp_path)


class TestExecute:
    def test_dry_run_no_mutation(self, tmp_path, monkeypatch):
        cmds = []
        monkeypatch.setattr(subprocess, "run", _fake_run_factory(cmds))
        plan = plan_rollback(10, tmp_path)
        n_before = len(cmds)
        result = execute_rollback(plan, tmp_path, RollbackConfig(dry_run=True))
        assert result.success and result.dry_run
        assert len(cmds) == n_before  # 추가 명령 없음

    def test_full_sequence(self, tmp_path, monkeypatch):
        cmds = []
        monkeypatch.setattr(subprocess, "run", _fake_run_factory(cmds))
        plan = plan_rollback(10, tmp_path)
        n_plan = len(cmds)
        result = execute_rollback(plan, tmp_path, RollbackConfig(notify_telegram=False))
        assert result.success
        assert result.revert_pr_number == 11
        assert result.reopened_issues == [7]
        verbs = [(c[0], c[1]) for c in cmds[n_plan:]]
        assert verbs[0] == ("git", "status")  # 작업 트리 검사
        assert verbs[1] == ("git", "fetch")
        assert verbs[2] == ("git", "checkout")
        assert verbs[3] == ("git", "revert")
        assert verbs[4] == ("git", "push")
        assert ("gh", "pr") in verbs
        assert ("gh", "issue") in verbs

    def test_dirty_tree(self, tmp_path, monkeypatch):
        cmds = []
        monkeypatch.setattr(subprocess, "run", _fake_run_factory(cmds, dirty=True))
        plan = plan_rollback(10, tmp_path)
        result = execute_rollback(plan, tmp_path, RollbackConfig(notify_telegram=False))
        assert not result.success and "깨끗하지 않음" in (result.error or "")

    def test_revert_conflict(self, tmp_path, monkeypatch):
        import json

        def fake(cmd, **kwargs):
            if cmd[:3] == ["gh", "pr", "view"]:
                return FakeCompleted(0, json.dumps(PR_VIEW))
            if cmd[:2] == ["git", "status"]:
                return FakeCompleted(0, "")
            if cmd[:2] == ["git", "revert"]:
                return FakeCompleted(1, "", "CONFLICT (modify/delete)")
            return FakeCompleted(0, "")

        monkeypatch.setattr(subprocess, "run", fake)
        plan = plan_rollback(10, tmp_path)
        result = execute_rollback(plan, tmp_path, RollbackConfig(notify_telegram=False))
        assert not result.success and "CONFLICT" in (result.error or "")

    def test_working_tree_clean(self, tmp_path, monkeypatch):
        monkeypatch.setattr(subprocess, "run", _fake_run_factory([]))
        assert working_tree_clean(tmp_path) is True


class TestEntry:
    def test_rollback_pr_plan_fail(self, tmp_path, monkeypatch):
        monkeypatch.setattr(
            subprocess,
            "run",
            lambda cmd, **k: FakeCompleted(1, "", "nope"),
        )
        r = rollback_pr(99, tmp_path, RollbackConfig(notify_telegram=False))
        assert not r.success and r.error

    def test_main_dry_run(self, tmp_path, monkeypatch, capsys):
        monkeypatch.setattr(subprocess, "run", _fake_run_factory([], pr_view=PR_VIEW))
        code = main(["10", "--workspace", str(tmp_path), "--dry-run", "--quiet"])
        assert code == 0
        out = capsys.readouterr().out
        assert "revert/pr-10" in out and "변경 없음" in out

    def test_main_dry_run_fail_reason(self, tmp_path, monkeypatch, capsys):
        monkeypatch.setattr(subprocess, "run", lambda cmd, **k: FakeCompleted(1, "", "nope"))
        code = main(["99", "--workspace", str(tmp_path), "--dry-run", "--quiet"])
        assert code == 1
        assert "사유" in capsys.readouterr().out

    def test_main_fail(self, tmp_path, monkeypatch, capsys):
        monkeypatch.setattr(
            subprocess,
            "run",
            lambda cmd, **k: FakeCompleted(1, "", "nope"),
        )
        code = main(["99", "--workspace", str(tmp_path), "--quiet"])
        assert code == 1
        assert "실패" in capsys.readouterr().out

    def test_config_dict(self):
        assert RollbackConfig().to_dict()["remote"] == "origin"
