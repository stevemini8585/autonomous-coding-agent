"""코드 품질 메트릭 테스트"""

from autonomous_coding_agent.metrics import (
    analyze_file,
    analyze_source,
    risk_rank,
)


def _ok(src: str):
    r = analyze_source(src)
    assert not r.errors, r.errors
    return r


def _func(src: str, name: str):
    r = _ok(src)
    f = r.get_function(name)
    assert f is not None, f"{name} not found"
    return f


class TestRiskRank:
    def test_bounds(self):
        assert risk_rank(1) == "low"
        assert risk_rank(10) == "low"
        assert risk_rank(11) == "moderate"
        assert risk_rank(20) == "moderate"
        assert risk_rank(21) == "high"
        assert risk_rank(51) == "untestable"


class TestCyclomatic:
    def test_straight_line(self):
        f = _func("def f():\n    x = 1\n    return x\n", "f")
        assert f.cyclomatic == 1 and f.rank == "low"

    def test_if_elif(self):
        src = "def f(x):\n    if x:\n        return 1\n    elif x > 1:\n        return 2\n    return 0\n"
        assert _func(src, "f").cyclomatic == 3

    def test_loops(self):
        src = "def f(xs):\n    for x in xs:\n        while x:\n            x -= 1\n    return 0\n"
        assert _func(src, "f").cyclomatic == 3

    def test_boolop(self):
        src = "def f(a, b, c):\n    if a and b or c:\n        return 1\n    return 0\n"
        # if(1) + and(1) + or(1) = 4
        assert _func(src, "f").cyclomatic == 4

    def test_ternary_and_assert(self):
        src = "def f(x):\n    assert x\n    return 1 if x else 0\n"
        assert _func(src, "f").cyclomatic == 3

    def test_except(self):
        src = "def f():\n    try:\n        x = 1\n    except ValueError:\n        x = 2\n    except TypeError:\n        x = 3\n    return x\n"
        assert _func(src, "f").cyclomatic == 3

    def test_comprehension(self):
        src = "def f(xs):\n    return [x for x in xs if x]\n"
        # gen(1) + if(1) = 3
        assert _func(src, "f").cyclomatic == 3

    def test_nested_function_isolated(self):
        src = "def f():\n    def g():\n        if True:\n            return 1\n        return 0\n    return g()\n"
        assert _func(src, "f").cyclomatic == 1
        assert _func(src, "g").cyclomatic == 2

    def test_nesting_depth(self):
        src = "def f(x):\n    if x:\n        for i in x:\n            if i:\n                return i\n    return None\n"
        assert _func(src, "f").max_nesting == 3

    def test_loc_params(self):
        src = "def f(a, b=1, *args):\n    return a\n"
        f = _func(src, "f")
        assert f.loc == 2 and f.params == 3

    def test_self_excluded(self):
        src = "class A:\n    def m(self, x):\n        return x\n"
        assert _func(src, "m").params == 1


class TestFan:
    def test_fan_out(self):
        src = "def g():\n    return 1\ndef h():\n    return 2\ndef f():\n    return g() + h()\n"
        assert _func(src, "f").fan_out == 2

    def test_fan_in(self):
        src = "def g():\n    return 1\ndef f():\n    return g()\ndef h():\n    return g()\n"
        assert _func(src, "g").fan_in == 2

    def test_no_calls(self):
        f = _func("def f():\n    return 1\n", "f")
        assert f.fan_in == 0 and f.fan_out == 0


class TestCohesion:
    def test_cohesive(self):
        src = (
            "class A:\n    def __init__(self):\n        self.x = 1\n"
            "    def get(self):\n        return self.x\n"
            "    def put(self, v):\n        self.x = v\n"
        )
        r = _ok(src)
        assert len(r.classes) == 1
        c = r.classes[0]
        assert c.methods == 3 and c.lcom == 0 and c.tcc == 1.0
        assert c.rank == "good"

    def test_incohesive(self):
        src = (
            "class B:\n    def m1(self):\n        return self.a\n"
            "    def m2(self):\n        return self.b\n"
            "    def m3(self):\n        return self.c\n"
        )
        c = _ok(src).classes[0]
        assert c.lcom == 3 and c.tcc == 0.0 and c.rank == "poor"

    def test_partial(self):
        src = (
            "class C:\n    def m1(self):\n        return self.a\n"
            "    def m2(self):\n        self.a = 1\n        return self.b\n"
            "    def m3(self):\n        return self.c\n"
        )
        c = _ok(src).classes[0]
        # 공유 쌍: (m1,m2)만 → tcc=1/3, lcom = 2-1 = 1
        assert c.lcom == 1 and c.rank == "fair"

    def test_single_method(self):
        c = _ok("class D:\n    def m(self):\n        return 1\n").classes[0]
        assert c.lcom == 0 and c.tcc == 1.0


class TestAggregate:
    def test_avg_max(self):
        src = "def f():\n    return 1\ndef g(x):\n    if x:\n        return 1\n    return 0\n"
        r = _ok(src)
        assert r.avg_complexity() == 1.5
        assert r.max_complexity() == 2

    def test_worst_offenders(self):
        src = "def f():\n    return 1\ndef g(x):\n    if x:\n        return 1\n    return 0\n"
        assert _ok(src).worst_offenders(1)[0].name == "g"

    def test_empty(self):
        r = _ok("")
        assert r.avg_complexity() == 0.0 and r.max_complexity() == 0
        assert r.functions == [] and r.classes == []

    def test_syntax_error(self):
        assert analyze_source("def broken(:\n").errors

    def test_to_dict(self):
        d = _ok("def f():\n    return 1\n").to_dict()
        for k in ("functions", "classes", "avg_complexity", "max_complexity", "errors"):
            assert k in d

    def test_high_risk_empty(self):
        assert _ok("def f():\n    return 1\n").high_risk() == []

    def test_real_file(self, tmp_path):
        p = tmp_path / "s.py"
        p.write_text("def f(x):\n    if x:\n        return 1\n    return 0\n")
        r = analyze_file(str(p))
        assert not r.errors and r.max_complexity() == 2

    def test_missing_file(self, tmp_path):
        assert analyze_file(str(tmp_path / "nope.py")).errors
