"""검증기 스코핑 테스트 (변경 파일만 검사)"""

from pathlib import Path

from autonomous_coding_agent.models import PlanStep, StepType
from autonomous_coding_agent.verifier import Verifier


def _step(files):
    return PlanStep(id="s1", type=StepType.CODE, title="t", description="d", assigned_files=files)


class TestScoping:
    def test_is_test_file(self):
        v = Verifier.__new__(Verifier)
        assert v._is_test_file("tests/test_x.py")
        assert v._is_test_file("src/x_test.py")
        assert v._is_test_file("a/tests/b.py")
        assert not v._is_test_file("src/x.py")

    def test_lint_scoped(self, tmp_path):
        v = Verifier(tmp_path)
        (tmp_path / "good.py").write_text("x = 1\nprint(x)\n")
        r = v.verify_step(_step(["good.py"]), ["good.py"])
        assert r.lint_results.get("passed") is True
        assert r.format_results.get("passed") is True

    def test_lint_only_failure_does_not_block(self, tmp_path):
        v = Verifier(tmp_path)
        # E722(bare except)는 자동 수정 불가 + mypy 통과 → 경고만, 전체 통과
        (tmp_path / "ok.py").write_text("try:\n    x = 1\n    print(x)\nexcept:\n    pass\n")
        r = v.verify_step(_step(["ok.py"]), ["ok.py"])
        assert r.lint_results.get("passed") is False
        assert any("린트" in w for w in r.warnings)
        assert r.passed is True
        assert r.errors == []

    def test_type_failure_blocks(self, tmp_path):
        v = Verifier(tmp_path)
        # F821(미정의 이름)은 자동 수정 불가 → 린트 실패 유지
        # (mypy도 함께 실패하므로 전체는 실패 — 차단은 타입 체크가 담당)
        (tmp_path / "bad.py").write_text("print(undefined_var_xyz)\n")
        r = v.verify_step(_step(["bad.py"]), ["bad.py"])
        assert r.lint_results.get("passed") is False
        assert any("린트" in w for w in r.warnings)
        assert r.passed is False
        assert r.errors == ["타입 체크 실패"]

    def test_autofix_heals(self, tmp_path):
        v = Verifier(tmp_path)
        (tmp_path / "fixme.py").write_text("import os\nx = 1\nprint(x)\n")
        r = v.verify_step(_step(["fixme.py"]), ["fixme.py"])
        assert r.lint_results.get("passed") is True
        assert "import os" not in (tmp_path / "fixme.py").read_text()

    def test_no_test_files_skipped(self, tmp_path):
        v = Verifier(tmp_path)
        (tmp_path / "m.py").write_text("x = 1\n")
        r = v.verify_step(_step(["m.py"]), ["m.py"])
        assert r.test_results.get("passed") is True
        assert r.test_results.get("skipped") is True

    def test_other_project_errors_ignored(self, tmp_path, monkeypatch):
        # 지정 파일은 깨끗, 워크스페이스 다른 곳은 깨짐 → 통과해야 함
        v = Verifier(tmp_path)
        (tmp_path / "good.py").write_text("x = 1\nprint(x)\n")
        (tmp_path / "broken_other.py").write_text("def broken(:\n")
        monkeypatch.setattr(v, "verify_types_enabled", True, raising=False)
        r = v.verify_step(_step(["good.py"]), ["good.py"])
        assert r.passed is True

    def test_type_scoped(self, tmp_path):
        v = Verifier(tmp_path)
        (tmp_path / "t.py").write_text("def f(x: int) -> int:\n    return x\n")
        r = v.verify_step(_step(["t.py"]), ["t.py"])
        assert r.type_results.get("passed") is True


class TestTypeDiffAware:
    def _git(self, d, *args):
        import subprocess

        r = subprocess.run(["git", *args], cwd=d, capture_output=True, text=True, timeout=30)
        assert r.returncode == 0, r.stderr
        return r.stdout

    def _mk_repo(self, tmp_path):
        d = tmp_path / "repo"
        d.mkdir()
        self._git(d, "init")
        self._git(
            d, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "--allow-empty", "-m", "init"
        )
        return d

    def test_old_error_outside_hunk_ignored(self, tmp_path):
        from autonomous_coding_agent.verifier import Verifier

        d = self._mk_repo(tmp_path)
        (d / "m.py").write_text("print(undefined_old)\nx = 1\n")
        self._git(d, "add", "m.py")
        self._git(d, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-m", "base")
        (d / "m.py").write_text("print(undefined_old)\nx = 2\n")
        v = Verifier(d)
        out = "m.py:1: error: Name 'undefined_old' is not defined  [name-defined]"
        kept, dropped = v._new_type_errors(["m.py"], out)
        assert kept == [] and dropped == 1

    def test_new_error_inside_hunk_blocks(self, tmp_path):
        from autonomous_coding_agent.verifier import Verifier

        d = self._mk_repo(tmp_path)
        (d / "m.py").write_text("x = 1\ny = 2\n")
        self._git(d, "add", "m.py")
        self._git(d, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-m", "base")
        (d / "m.py").write_text("x = 1\nprint(undefined_new)\n")
        v = Verifier(d)
        out = "m.py:2: error: Name 'undefined_new' is not defined  [name-defined]"
        kept, dropped = v._new_type_errors(["m.py"], out)
        assert len(kept) == 1 and dropped == 0

    def test_nongit_fallback_keeps_all(self, tmp_path):
        from autonomous_coding_agent.verifier import Verifier

        v = Verifier(tmp_path)
        out = "m.py:3: error: Something bad  [misc]"
        kept, dropped = v._new_type_errors(["m.py"], out)
        assert len(kept) == 1 and dropped == 0
