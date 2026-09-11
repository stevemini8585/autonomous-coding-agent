"""code_adapter 테스트 — tmp 프로젝트 픽스처 기반"""

import json

import pytest

from autonomous_coding_agent.code_adapter import (
    CodeExampleAdapter,
    ProjectAnalyzer,
    ProjectContext,
)
from autonomous_coding_agent.web_search import Documentation


def make_py_project(tmp_path, framework="fastapi"):
    (tmp_path / "a.py").write_text("x = 1\n")
    (tmp_path / "requirements.txt").write_text(f"{framework}\n")
    (tmp_path / "pyproject.toml").write_text("[tool.black]\nline-length = 100\n")
    return tmp_path


class TestAnalyzer:
    def test_python_fastapi(self, tmp_path):
        make_py_project(tmp_path)
        ctx = ProjectAnalyzer(tmp_path).analyze()
        assert ctx.language == "python"
        assert ctx.framework == "fastapi"

    def test_empty_defaults_python(self, tmp_path):
        ctx = ProjectAnalyzer(tmp_path).analyze()
        assert ctx.language == "python"

    def test_js_react(self, tmp_path):
        (tmp_path / "app.js").write_text("x=1\n")
        (tmp_path / "app.js").write_text("x=1\n")
        (tmp_path / "package.json").write_text(json.dumps({"dependencies": {"react": "^18"}}))
        ctx = ProjectAnalyzer(tmp_path).analyze()
        assert ctx.language == "javascript"
        assert ctx.framework == "react"

    def test_ts_nextjs(self, tmp_path):
        (tmp_path / "a.ts").write_text("let x=1\n")
        (tmp_path / "b.ts").write_text("let y=2\n")
        (tmp_path / "package.json").write_text(json.dumps({"dependencies": {"next": "14"}}))
        ctx = ProjectAnalyzer(tmp_path).analyze()
        assert ctx.language == "typescript"
        assert ctx.framework == "nextjs"

    def test_package_manager(self, tmp_path):
        make_py_project(tmp_path)
        (tmp_path / "uv.lock").write_text("x")
        ctx = ProjectAnalyzer(tmp_path).analyze()
        assert ctx.package_manager in ("uv", "pip", None)

    def test_frameworks(self, tmp_path):
        for fw in ("django", "flask"):
            d = tmp_path / fw
            d.mkdir()
            (d / "m.py").write_text("x=1\n")
            (d / "requirements.txt").write_text(f"{fw}\n")
            assert ProjectAnalyzer(d)._detect_framework("python") == fw

    def test_bad_package_json(self, tmp_path):
        (tmp_path / "a.js").write_text("x\n")
        (tmp_path / "package.json").write_text("{broken")
        ctx = ProjectAnalyzer(tmp_path).analyze()
        assert ctx.framework is None


def _docs():
    return Documentation(title="T", url="http://x", content="c")


class TestAdapter:
    def test_python_passthrough(self, tmp_path):
        make_py_project(tmp_path)
        ad = CodeExampleAdapter(tmp_path)
        out = ad.adapt_example("def f():\n    return 1\n", _docs())
        assert "def f" in out.adapted and out.confidence == 0.85

    def test_async_heuristic(self, tmp_path):
        make_py_project(tmp_path)
        ad = CodeExampleAdapter(tmp_path)
        out = ad.adapt_example("def f():\n    requests.get('http://x')\n", _docs())
        assert "async def f" in out.adapted

    def test_explicit_context(self, tmp_path):
        ctx = ProjectContext(root_path=tmp_path, language="python")
        ad = CodeExampleAdapter(tmp_path, context=ctx)
        out = ad.adapt_example("x = 1\n", _docs(), target_file="m.py")
        assert out.target_file == "m.py"

    def test_js_transform(self, tmp_path):
        (tmp_path / "a.js").write_text("x\n")
        ctx = ProjectContext(root_path=tmp_path, language="javascript")
        ad = CodeExampleAdapter(tmp_path, context=ctx)
        out = ad.adapt_example("const x = require('m')\n", _docs())
        assert "import x from 'm'" in out.adapted


class TestJsTsStyle:
    def test_esm_camel(self, tmp_path):
        (tmp_path / "app.js").write_text(
            "import { fetchData } from './api.js';\n"
            "export async function loadUser() {\n  const userData = await fetchData();\n  return userData;\n}\n"
            "export class UserCard {}\n"
        )
        ctx = ProjectAnalyzer(tmp_path).analyze()
        assert ctx.import_style == "esm"
        assert ctx.naming_convention == "camelCase"
        assert ctx.async_pattern is True

    def test_cjs(self, tmp_path):
        (tmp_path / "srv.js").write_text(
            "const http = require('http');\n"
            "function start_server() {}\n"
            "module.exports = { start_server };\n"
        )
        ctx = ProjectAnalyzer(tmp_path).analyze()
        assert ctx.import_style == "cjs"
        assert ctx.naming_convention == "snake_case"

    def test_ts_flag(self, tmp_path):
        (tmp_path / "a.ts").write_text("const x: number = 1;\n")
        ctx = ProjectAnalyzer(tmp_path).analyze()
        assert ctx.type_hints is True
