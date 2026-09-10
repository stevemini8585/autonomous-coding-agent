"""코드 품질 게이트 테스트"""

from autonomous_coding_agent.quality_gate import (
    GateConfig,
    check_file,
    check_paths,
    check_source,
    create_quality_gate,
    gate_summary,
)


def _ok(src: str, **kwargs):
    return check_source(src, **kwargs)


class TestVerdicts:
    def test_clean_pass(self):
        r = _ok("def f(x):\n    return x + 1\nprint(f(1))\n")
        assert r.passed and not r.blocked
        assert r.findings == []
        assert "PASS" in r.summary()

    def test_warn_complexity(self):
        src = (
            "def f(x):\n"
            + "".join(f"    if x == {i}:\n        x += {i}\n" for i in range(12))
            + "    return x\n"
        )
        r = _ok(src)
        assert r.passed and not r.blocked
        assert any(f.rule == "complexity" and f.severity == "warn" for f in r.findings)
        assert "WARN" in r.summary()

    def test_block_complexity(self):
        src = (
            "def f(x):\n"
            + "".join(f"    if x == {i}:\n        x += {i}\n" for i in range(25))
            + "    return x\n"
        )
        r = _ok(src)
        assert r.blocked and not r.passed
        assert any(f.rule == "complexity" and f.severity == "block" for f in r.findings)
        assert "BLOCK" in r.summary()

    def test_block_use_before_def(self):
        r = _ok("print(zzz_undefined_var)\n")
        assert r.blocked
        assert any(f.rule == "use-before-def" for f in r.blocks())

    def test_warn_params(self):
        src = "def f(a, b, c, d, e, g):\n    return a\nprint(f(1, 2, 3, 4, 5, 6))\n"
        r = _ok(src)
        assert any(f.rule == "params" and f.severity == "warn" for f in r.findings)

    def test_block_params(self):
        src = "def f(a, b, c, d, e, g, h, i, j):\n    return a\nprint(f(1,2,3,4,5,6,7,8,9))\n"
        r = _ok(src)
        assert r.blocked
        assert any(f.rule == "params" and f.severity == "block" for f in r.findings)

    def test_warn_cohesion(self):
        src = (
            "class B:\n    def m1(self):\n        return self.a\n"
            "    def m2(self):\n        return self.b\n"
            "    def m3(self):\n        return self.c\n"
        )
        r = _ok(src)
        assert any(f.rule == "cohesion" for f in r.warnings())

    def test_warn_type_coverage(self):
        r = _ok("x = unknown_thing\ny = another_unknown\nprint(x, y)\n")
        assert any(f.rule == "type-coverage" for f in r.warnings())

    def test_warn_fan_out(self):
        defs = "".join(f"def h{i}():\n    return {i}\n" for i in range(9))
        calls = "".join(f"    h{i}()\n" for i in range(9))
        r = _ok(defs + f"def f():\n{calls}    return 0\nprint(f())\n")
        assert any(f.rule == "fan-out" for f in r.warnings())


class TestConfig:
    def test_strict_blocks_earlier(self):
        src = (
            "def f(x):\n"
            + "".join(f"    if x == {i}:\n        x += {i}\n" for i in range(12))
            + "    return x\n"
        )
        assert _ok(src).passed  # 기본은 warn
        assert _ok(src, config=GateConfig.strict()).blocked  # strict는 block

    def test_lenient_passes(self):
        src = (
            "def f(x):\n"
            + "".join(f"    if x == {i}:\n        x += {i}\n" for i in range(12))
            + "    return x\n"
        )
        r = _ok(src, config=GateConfig.lenient())
        assert r.passed and not r.blocked  # warn만, 차단 없음

    def test_custom_threshold(self):
        cfg = GateConfig(max_complexity_warn=1, max_complexity_block=100)
        r = _ok("def f(x):\n    if x:\n        return 1\n    return 0\n", config=cfg)
        assert any(f.rule == "complexity" and f.severity == "warn" for f in r.findings)
        assert r.passed

    def test_config_dict_and_factory(self):
        assert "max_complexity_block" in GateConfig().to_dict()
        assert isinstance(create_quality_gate(), GateConfig)
        assert create_quality_gate(GateConfig.strict()).max_complexity_block == 10


class TestFiles:
    def test_check_file(self, tmp_path):
        p = tmp_path / "s.py"
        p.write_text("def f(x):\n    return x\nprint(f(1))\n")
        r = check_file(str(p))
        assert r.passed and r.filename == str(p)

    def test_missing_file(self, tmp_path):
        r = check_file(str(tmp_path / "nope.py"))
        assert r.errors and r.summary().startswith(str(tmp_path))

    def test_check_paths_dir(self, tmp_path):
        (tmp_path / "a.py").write_text("x = 1\nprint(x)\n")
        (tmp_path / "b.py").write_text("print(zzz_nope)\n")
        results = check_paths([tmp_path])
        assert len(results) == 2
        s = gate_summary(results)
        assert s["total"] == 2 and not s["all_passed"]
        assert len(s["blocked"]) == 1

    def test_gate_summary_all_pass(self, tmp_path):
        (tmp_path / "a.py").write_text("x = 1\nprint(x)\n")
        s = gate_summary(check_paths([tmp_path]))
        assert s["all_passed"] and s["passed"] == 1

    def test_finding_dict(self):
        r = _ok("print(zzz_nope)\n")
        d = r.to_dict()
        assert d["blocked"] and "summary" in d
        assert d["findings"] and "rule" in d["findings"][0]


class TestDiffAware:
    def test_new_findings_only(self):
        from autonomous_coding_agent.quality_gate import (
            Finding,
            GateResult,
            new_findings,
        )

        def f(rule, target, sev="block"):
            return Finding(
                rule=rule,
                target=target,
                actual=1,
                threshold=0,
                severity=sev,
                message=f"{rule}@{target}",
            )

        base = GateResult(filename="a.py", findings=[f("complexity", "m.f")])
        cur = GateResult(
            filename="a.py",
            findings=[f("complexity", "m.f"), f("use-before-def", "m.g")],
        )
        new = new_findings(base, cur)
        assert [(x.rule, x.target) for x in new] == [("use-before-def", "m.g")]

    def test_warns_ignored(self):
        from autonomous_coding_agent.quality_gate import (
            Finding,
            GateResult,
            new_findings,
        )

        base = GateResult(filename="a.py", findings=[])
        cur = GateResult(
            filename="a.py",
            findings=[
                Finding(
                    rule="complexity",
                    target="m.f",
                    actual=11,
                    threshold=10,
                    severity="warn",
                    message="w",
                )
            ],
        )
        assert new_findings(base, cur) == []

    def test_against_baseline_new_file(self, tmp_path):
        from autonomous_coding_agent.quality_gate import check_against_baseline

        p = tmp_path / "n.py"
        p.write_text("print(zzz_undefined_abc)\n")
        cur, new = check_against_baseline(str(p), None)
        assert cur.blocked and len(new) == 1

    def test_against_baseline_same(self, tmp_path):
        from autonomous_coding_agent.quality_gate import check_against_baseline

        src = "x = 1\nprint(x)\n"
        p = tmp_path / "s.py"
        p.write_text(src)
        cur, new = check_against_baseline(str(p), src)
        assert new == []
