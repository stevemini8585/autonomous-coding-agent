"""데이터 플로우 분석 테스트"""

from autonomous_coding_agent.dataflow import (
    AnalysisResult,
    analyze_file,
    analyze_source,
)


def _ok(src: str) -> AnalysisResult:
    r = analyze_source(src)
    assert not r.errors, r.errors
    return r


class TestDefsUses:
    def test_assign_and_use(self):
        r = _ok("x = 1\ny = x + 1\n")
        assert [d.name for d in r.defs_of("x")] == ["x"]
        assert len(r.uses_of("x")) == 1
        chain = r.chain_of("x", 1)
        assert chain is not None and len(chain.uses) == 1

    def test_reassign_kill(self):
        r = _ok("x = 1\nx = 2\ny = x\n")
        defs = r.defs_of("x")
        assert len(defs) == 2
        assert defs[0].killed is True
        assert defs[1].killed is False
        chain = r.chain_of("x", 2)
        assert chain is not None and len(chain.uses) == 1

    def test_reaching_lines(self):
        r = _ok("x = 1\ny = x\n")
        uses = r.uses_of("x")
        assert uses and uses[0].reaching == [1]

    def test_tuple_unpack(self):
        r = _ok("a, b = 1, 2\nc = a + b\n")
        assert r.defs_of("a") and r.defs_of("b")
        assert r.uses_of("a") and r.uses_of("b")

    def test_for_target(self):
        r = _ok("for i in range(3):\n    print(i)\n")
        assert r.defs_of("i")[0].kind == "for"

    def test_with_target(self):
        r = _ok("with open('f') as fh:\n    data = fh.read()\n")
        assert r.defs_of("fh")[0].kind == "with"

    def test_import_def(self):
        r = _ok("import os\nprint(os.name)\n")
        assert r.defs_of("os")[0].kind == "import"


class TestFunctions:
    def test_args_are_defs(self):
        r = _ok("def f(a, b=1):\n    return a + b\n")
        assert r.defs_of("a", scope="module.f")
        assert r.uses_of("a", scope="module.f")

    def test_call_edge(self):
        r = _ok("def g():\n    return 1\ndef f():\n    return g()\n")
        kinds = {(e.src, e.dst, e.kind) for e in r.edges}
        assert ("module.f", "module.g", "call") in kinds

    def test_data_edge(self):
        r = _ok("x = 1\ny = x + 1\n")
        data = {(e.src, e.dst) for e in r.edges if e.kind == "data"}
        assert ("module.y", "module.x") in data

    def test_depends_queries(self):
        r = _ok("x = 1\ny = x + 1\n")
        assert "module.x" in r.depends_on("module.y")
        assert "module.y" in r.dependents_of("module.x")

    def test_class_attr(self):
        src = "class A:\n    def __init__(self):\n        self.v = 1\n"
        r = _ok(src)
        assert r.defs_of("A.v")


class TestDiagnostics:
    def test_unused(self):
        r = _ok("x = 1\ny = 2\nprint(y)\n")
        unused = {d.name for d in r.unused_definitions()}
        assert "x" in unused and "y" not in unused

    def test_use_before_def(self):
        r = _ok("print(zzz_missing)\n")
        bad = r.uses_before_def()
        assert any(u.name == "zzz_missing" for u in bad)

    def test_no_false_positive(self):
        r = _ok("x = 1\nprint(x)\n")
        assert r.uses_before_def() == []

    def test_topological_order(self):
        r = _ok("x = 1\ny = x + 1\nz = y * 2\n")
        order = r.topological_order()
        assert order.index("module.x") < order.index("module.y")
        assert order.index("module.y") < order.index("module.z")


class TestRobustness:
    def test_syntax_error(self):
        assert analyze_source("def broken(:\n").errors

    def test_empty(self):
        r = _ok("")
        assert r.definitions == [] and r.uses == []

    def test_to_dict(self):
        d = _ok("x = 1\nprint(x)\n").to_dict()
        for k in ("definitions", "uses", "chains", "edges", "unused", "uses_before_def", "errors"):
            assert k in d

    def test_chain_dict(self):
        r = _ok("x = 1\nprint(x)\n")
        c = r.chain_of("x", 1)
        assert c is not None and "definition" in c.to_dict()

    def test_base_edge(self):
        r = _ok("class B:\n    pass\nclass A(B):\n    pass\n")
        kinds = {(e.src, e.dst, e.kind) for e in r.edges}
        assert ("module.A", "module.B", "base") in kinds

    def test_real_file(self, tmp_path):
        p = tmp_path / "s.py"
        p.write_text("import os\nx = os.name\ny = x\nprint(y)\n")
        r = analyze_file(str(p))
        assert not r.errors
        assert r.defs_of("y")

    def test_missing_file(self, tmp_path):
        assert analyze_file(str(tmp_path / "nope.py")).errors


class TestLambdaComp:
    def test_lambda_args(self):
        from autonomous_coding_agent.dataflow import analyze_source

        r = analyze_source("f = lambda a, b: a + b\nprint(f(1, 2))\n")
        assert not r.errors
        assert r.uses_before_def() == []

    def test_comp_target(self):
        from autonomous_coding_agent.dataflow import analyze_source

        r = analyze_source(
            "xs = [1, 2]\nys = [x * 2 for x in xs if x]\n"
            "d = {k: v for k, v in zip(xs, ys)}\nprint(ys, d)\n"
        )
        assert r.uses_before_def() == []
        chains = {c.definition.name: len(c.uses) for c in r.chains}
        assert chains.get("x", 0) >= 2
        assert chains.get("k", 0) >= 1

    def test_dunder_ok(self):
        from autonomous_coding_agent.dataflow import analyze_source

        r = analyze_source('import pytest\n\npytest.main([__file__, "-v"])\n')
        assert r.uses_before_def() == []
