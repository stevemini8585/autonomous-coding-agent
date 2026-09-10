"""AST 타입 추론 테스트"""

from autonomous_coding_agent.type_inference import (
    InferenceResult,
    TypeInfo,
    infer_file,
    infer_source,
    join_types,
)


def _types(src: str) -> InferenceResult:
    r = infer_source(src)
    assert not r.errors, r.errors
    return r


def _g(r: InferenceResult, name: str, scope: str = "module") -> TypeInfo:
    info = r.get(name, scope=scope)
    assert info is not None, f"{scope}.{name} not found"
    return info


class TestJoinTypes:
    def test_same(self):
        """test_same 함수.

        Args:
            self: 매개변수 설명.

        Returns:
            결과값.
        """
        assert join_types("int", "int") == "int"

    def test_any(self):
        assert join_types("Any", "str") == "str"
        assert join_types("str", "Any") == "str"

    def test_optional(self):
        assert join_types("None", "int") == "Optional[int]"
        assert join_types("str", "None") == "Optional[str]"

    def test_numeric_promotion(self):
        assert join_types("int", "float") == "float"
        assert join_types("bool", "int") == "int"

    def test_union(self):
        assert join_types("int", "str") == "Union[int, str]"


class TestLiterals:
    def test_basic(self):
        r = _types("a = 1\nb = 'x'\nc = 3.14\nd = True\ne = None\n")
        assert _g(r, "a").inferred == "int"
        assert _g(r, "b").inferred == "str"
        assert _g(r, "c").inferred == "float"
        assert _g(r, "d").inferred == "bool"
        assert _g(r, "e").inferred == "None"

    def test_collections(self):
        r = _types("a = [1, 2]\nb = {'k': 1}\nc = (1, 'x')\n")
        assert _g(r, "a").inferred == "list[int]"
        assert _g(r, "b").inferred == "dict"
        assert _g(r, "c").inferred == "tuple"


class TestAnnotations:
    def test_annassign_wins(self):
        r = _types("x: int = 1\n")
        info = _g(r, "x")
        assert info.inferred == "int"
        assert info.confidence == 1.0

    def test_arg_annotations(self):
        r = _types("def f(a: int, b: str) -> bool:\n    return True\n")
        assert _g(r, "a", scope="module.f").inferred == "int"
        assert _g(r, "b", scope="module.f").inferred == "str"

    def test_default_value(self):
        r = _types("def f(n=10):\n    return n\n")
        assert _g(r, "n", scope="module.f").inferred == "int"


class TestFunctions:
    def test_return_inference(self):
        r = _types("def f():\n    return 42\n")
        found = [t for t in r.types.values() if t.name == "f"]
        assert found and "int" in found[0].inferred

    def test_no_return_is_none(self):
        r = _types("def f():\n    x = 1\n")
        found = [t for t in r.types.values() if t.name == "f"]
        assert found and "None" in found[0].inferred

    def test_optional_return(self):
        r = _types("def f(flag):\n    if flag:\n        return 1\n    return None\n")
        found = [t for t in r.types.values() if t.name == "f"]
        assert found and "Optional[int]" in found[0].inferred

    def test_builtin_call(self):
        r = _types("n = len([1, 2])\ns = str(42)\n")
        assert _g(r, "n").inferred == "int"
        assert _g(r, "s").inferred == "str"


class TestClasses:
    def test_self_attributes(self):
        src = "class A:\n    def __init__(self, name: str):\n        self.name = name\n        self.count = 0\n"
        r = _types(src)
        attrs = r.by_kind("attribute")
        by_name = {a.name: a for a in attrs}
        assert by_name["A.name"].inferred == "str"
        assert by_name["A.count"].inferred == "int"

    def test_class_symbol(self):
        r = _types("class Foo:\n    pass\n")
        info = _g(r, "Foo")
        assert info is not None and info.kind == "class"


class TestControlFlow:
    def test_for_loop(self):
        r = _types("for i in range(10):\n    x = i\n")
        assert _g(r, "i").inferred == "int"

    def test_for_list(self):
        r = _types("names = ['a']\nfor n in names:\n    y = n\n")
        assert _g(r, "n").inferred == "str"

    def test_isinstance_narrowing(self):
        src = "def f(x):\n    if isinstance(x, int):\n        y = x\n    return x\n"
        r = _types(src)
        assert _g(r, "x", scope="module.f").inferred == "int"

    def test_binop(self):
        r = _types("a = 1 + 2.0\nb = 'x' + 'y'\n")
        assert _g(r, "a").inferred == "float"
        assert _g(r, "b").inferred == "str"

    def test_subscript(self):
        r = _types("a = [1, 2]\nb = a[0]\n")
        assert _g(r, "b").inferred == "int"


class TestRobustness:
    def test_syntax_error(self):
        r = infer_source("def broken(:\n")
        assert r.errors

    def test_empty(self):
        r = _types("")
        assert r.coverage() == 1.0

    def test_coverage(self):
        r = _types("a = 1\nb = unknown_var\n")
        assert 0.0 < r.coverage() <= 1.0

    def test_to_dict(self):
        r = _types("a = 1\n")
        d = r.to_dict()
        assert "types" in d and "coverage" in d

    def test_typeinfo_dict(self):
        info = TypeInfo(name="x", kind="variable", inferred="int")
        assert info.to_dict()["inferred"] == "int"

    def test_infer_real_file(self, tmp_path):
        p = tmp_path / "sample.py"
        p.write_text("def add(a: int, b: int) -> int:\n    return a + b\n")
        r = infer_file(str(p))
        assert not r.errors
        assert _g(r, "a", scope="module.add").inferred == "int"

    def test_infer_missing_file(self, tmp_path):
        r = infer_file(str(tmp_path / "nope.py"))
        assert r.errors
