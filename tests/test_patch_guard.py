"""패치 가드레일 테스트 (Day 5 처방 1번)"""

from pathlib import Path

from autonomous_coding_agent.coder import CodeGenerator, _parses
from autonomous_coding_agent.models import PlanStep, StepType
from autonomous_coding_agent.patch_utils import PatchManager, PatchOperation


def _mgr(tmp_path: Path, **kwargs) -> PatchManager:
    return PatchManager(tmp_path, **kwargs)


class TestDeletionRatio:
    def test_mass_deletion_rejected(self, tmp_path):
        old = "".join(f"line {i}\n" for i in range(471))
        (tmp_path / "page.html").write_text(old)
        new = "<p>hello</p>\n"
        res = _mgr(tmp_path).apply_single_patch("page.html", old, new)
        assert not res.success and "삭제율 초과" in (res.error or "")
        assert (tmp_path / "page.html").read_text() == old  # 원본 보존

    def test_normal_edit_passes(self, tmp_path):
        old = "".join(f"v{i} = {i}\n" for i in range(50))
        (tmp_path / "a.py").write_text(old)
        new = old.replace("v5 = 5\n", "v5 = 555\n") + "extra = 1\n"
        res = _mgr(tmp_path).apply_single_patch("a.py", old, new)
        assert res.success and res.applied

    def test_small_file_exempt(self, tmp_path):
        old = "a = 1\nb = 2\n"
        (tmp_path / "s.py").write_text(old)
        res = _mgr(tmp_path).apply_single_patch("s.py", old, "x = 9\n")
        assert res.success  # 20줄 미만은 삭제율 검사 면제 (단 신택스는 통과)

    def test_custom_threshold(self, tmp_path):
        old = "".join(f"line {i}\n" for i in range(100))
        (tmp_path / "a.txt").write_text(old)
        new = "".join(f"line {i}\n" for i in range(70))  # 30% 삭제
        assert (
            not _mgr(tmp_path, max_deletion_ratio=0.2).apply_single_patch("a.txt", old, new).success
        )
        assert _mgr(tmp_path, max_deletion_ratio=0.4).apply_single_patch("a.txt", old, new).success

    def test_check_direct(self, tmp_path):
        m = _mgr(tmp_path)
        assert m.check_guardrails("f.txt", "a\n", "b\n") is None


class TestSyntaxGuard:
    def test_broken_python_rejected(self, tmp_path):
        old = "".join(f"v{i} = {i}\n" for i in range(30))
        (tmp_path / "m.py").write_text(old)
        bad = "def f():\nreturn 1\n" + old  # 들여쓰기 오류
        res = _mgr(tmp_path).apply_single_patch("m.py", old, bad)
        assert not res.success and "신택스 오류" in (res.error or "")
        assert (tmp_path / "m.py").read_text() == old

    def test_non_python_skips_syntax(self, tmp_path):
        old = "plain\n" * 30
        (tmp_path / "n.txt").write_text(old)
        res = _mgr(tmp_path).apply_single_patch("n.txt", old, old + "def broken(:\n")
        assert res.success  # .py 아니면 신택스 검사 안 함

    def test_parses_helper(self):
        assert _parses("x = 1\n")
        assert not _parses("def f(:\n")


class TestCoderNewFile:
    def _step(self):
        return PlanStep(
            id="s1",
            type=StepType.CODE,
            title="t",
            description="d",
            assigned_files=["new_mod_xyz.py"],
        )

    def test_bad_new_file_rejected(self, tmp_path, monkeypatch):
        gen = CodeGenerator(tmp_path)
        monkeypatch.setattr(
            gen,
            "_generate_task_specific_implementation",
            lambda step, goal, ctx: {"new_mod_xyz.py": "def broken(:\n"},
        )
        out = gen._implement_code(self._step(), {"goal": "g"})
        assert not (tmp_path / "new_mod_xyz.py").exists()
        assert out.get("files_rejected") == ["new_mod_xyz.py"]

    def test_good_new_file_written(self, tmp_path, monkeypatch):
        gen = CodeGenerator(tmp_path)
        monkeypatch.setattr(
            gen,
            "_generate_task_specific_implementation",
            lambda step, goal, ctx: {"new_mod_xyz.py": "VALUE = 42\n"},
        )
        out = gen._implement_code(self._step(), {"goal": "g"})
        assert (tmp_path / "new_mod_xyz.py").read_text() == "VALUE = 42\n"
        assert "new_mod_xyz.py" in out["files_created"]


FASTAPI_APP = """\
from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def get_health():
    return {"status": "ok"}
"""

FASTAPI_FACTORY = """\
from fastapi import FastAPI


def create_app():
    app = FastAPI()

    @app.get("/health")
    async def get_health():
        return {"status": "ok"}

    return app
"""


class TestFastAPIInsert:
    def test_module_level_append(self, tmp_path):
        import ast

        gen = CodeGenerator(tmp_path)
        out = gen._add_fastapi_endpoint(
            FASTAPI_APP, 'GET /ping 추가. 응답: {"status": "ok"}.', "x.py"
        )
        tree = ast.parse(out)  # 파싱 필수
        assert '"/ping"' in out and "async def get_ping" in out
        assert out.index('"/ping"') > out.index('"/health"')  # 末尾 추가

    def test_factory_insert_before_return(self, tmp_path):
        import ast

        gen = CodeGenerator(tmp_path)
        out = gen._add_fastapi_endpoint(
            FASTAPI_FACTORY, 'GET /ping 추가. 응답: {"status": "ok"}.', "x.py"
        )
        ast.parse(out)
        lines = out.split("\n")
        ping_idx = next(i for i, l in enumerate(lines) if '"/ping"' in l)
        ret_idx = next(i for i, l in enumerate(lines) if l.strip() == "return app")
        assert ping_idx < ret_idx  # return 직전
        assert lines[ping_idx].startswith("    @app.get")  # 함수 들여쓰기

    def test_duplicate_skipped(self, tmp_path):
        gen = CodeGenerator(tmp_path)
        out = gen._add_fastapi_endpoint(FASTAPI_APP, "GET /health 추가.", "x.py")
        assert out == FASTAPI_APP

    def test_broken_source_unchanged(self, tmp_path):
        gen = CodeGenerator(tmp_path)
        bad = "def broken(:\n"
        assert gen._add_fastapi_endpoint(bad, "GET /x 추가.", "x.py") == bad

    def test_name_collision_suffix(self, tmp_path):
        import ast

        gen = CodeGenerator(tmp_path)
        out = gen._add_fastapi_endpoint(
            FASTAPI_APP + "\nasync def get_ping():\n    return 1\n",
            "GET /ping 추가.",
            "x.py",
        )
        ast.parse(out)
        assert "async def get_ping_2" in out
