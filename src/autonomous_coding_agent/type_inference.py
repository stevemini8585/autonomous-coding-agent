"""
AST 기반 타입 추론 (Semantic Code Analysis 1/4)
- 변수/함수 인자·반환값/클래스 속성의 타입 자동 추론
- 명시적 어노테이션 > 리터럴 > 내장함수 > 연산 규칙 > 사용 기반 순으로 근거 가중
- isinstance 내로잉, Optional/Union 조인, 신뢰도(confidence) 제공
- mypy 등 외부 도구에 의존하지 않는 순수 stdlib 구현
"""

from __future__ import annotations

import ast
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

log = logging.getLogger("autonomous_coding_agent.type_inference")

_NUMERIC_RANK = {"bool": 0, "int": 1, "float": 2, "complex": 3}

_BUILTIN_RETURNS: dict[str, str] = {
    "len": "int",
    "abs": "int",
    "round": "int",
    "ord": "int",
    "chr": "str",
    "str": "str",
    "repr": "str",
    "int": "int",
    "float": "float",
    "bool": "bool",
    "bytes": "bytes",
    "list": "list",
    "dict": "dict",
    "set": "set",
    "tuple": "tuple",
    "sorted": "list",
    "reversed": "Iterator",
    "enumerate": "Iterator",
    "zip": "Iterator",
    "map": "Iterator",
    "filter": "Iterator",
    "range": "range",
    "open": "TextIO",
    "print": "None",
    "isinstance": "bool",
    "issubclass": "bool",
    "hasattr": "bool",
    "callable": "bool",
    "id": "int",
    "hash": "int",
}


@dataclass
class TypeInfo:
    """단일 심볼에 대한 추론 결과"""

    name: str
    kind: str  # variable | argument | return | attribute | class
    inferred: str = "Any"
    confidence: float = 0.2
    lineno: int = 0
    scope: str = "module"
    evidence: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """to_dict 함수.

        Args:
            self: 매개변수 설명.

        Returns:
            결과값.
        """
        return {
            "name": self.name,
            "kind": self.kind,
            "inferred": self.inferred,
            "confidence": self.confidence,
            "lineno": self.lineno,
            "scope": self.scope,
            "evidence": self.evidence,
        }


@dataclass
class InferenceResult:
    """파일/소스 단위 추론 결과"""

    types: dict[str, TypeInfo] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)

    def get(self, name: str, scope: str = "module") -> TypeInfo | None:
        """get 함수.

        Args:
            self: 매개변수 설명.
            name: 매개변수 설명.
            scope: 매개변수 설명.

        Returns:
            결과값.
        """
        return self.types.get(f"{scope}.{name}") or self.types.get(name)

    def by_kind(self, kind: str) -> list[TypeInfo]:
        """by_kind 함수.

        Args:
            self: 매개변수 설명.
            kind: 매개변수 설명.

        Returns:
            결과값.
        """
        return [t for t in self.types.values() if t.kind == kind]

    def coverage(self) -> float:
        """Any가 아닌 비율 (추론 성공률)"""
        if not self.types:
            return 1.0
        known = sum(1 for t in self.types.values() if t.inferred != "Any")
        return known / len(self.types)

    def to_dict(self) -> dict[str, Any]:
        """to_dict 함수.

        Args:
            self: 매개변수 설명.

        Returns:
            결과값.
        """
        return {
            "types": {k: v.to_dict() for k, v in self.types.items()},
            "coverage": self.coverage(),
            "errors": self.errors,
        }


def join_types(a: str, b: str) -> str:
    """두 타입 후보를 하나로 조인"""
    if a == b:
        return a
    if a == "Any":
        return b
    if b == "Any":
        return a
    if a == "None" and b != "None":
        return f"Optional[{b}]"
    if b == "None" and a != "None":
        return f"Optional[{a}]"
    if a.startswith("Optional[") and a[9:-1] == b:
        return a
    if b.startswith("Optional[") and b[9:-1] == a:
        return b
    # 수치형 승격
    if a in _NUMERIC_RANK and b in _NUMERIC_RANK:
        rank = _NUMERIC_RANK
        return a if rank[a] >= rank[b] else b
    inner_a = a[6:-1].split(", ") if a.startswith("Union[") else [a]
    inner_b = b[6:-1].split(", ") if b.startswith("Union[") else [b]
    merged: list[str] = []
    for t in inner_a + inner_b:
        if t not in merged:
            merged.append(t)
    if len(merged) == 1:
        return merged[0]
    return f"Union[{', '.join(sorted(merged))}]"


def annotation_to_str(node: ast.expr | None) -> str | None:
    """어노테이션 AST를 문자열로 변환"""
    if node is None:
        return None
    try:
        return ast.unparse(node).strip()
    except Exception:
        return None


class TypeInferenceVisitor(ast.NodeVisitor):
    """스코프 스택 기반 타입 추론 방문자"""

    def __init__(self) -> None:
        self.result = InferenceResult()
        self.scope_stack: list[str] = ["module"]
        self.symbols: dict[str, TypeInfo] = {}  # key: scope.name
        self.func_returns: dict[str, list[str]] = {}  # scope -> return 후보
        self.class_stack: list[str] = []

    # -- 스코프/기록 헬퍼 --
    @property
    def scope(self) -> str:
        """scope 함수.

        Args:
            self: 매개변수 설명.

        Returns:
            결과값.
        """
        return ".".join(self.scope_stack)

    def _key(self, name: str, scope: str | None = None) -> str:
        return f"{scope or self.scope}.{name}"

    def _record(
        self,
        name: str,
        inferred: str,
        confidence: float,
        kind: str,
        lineno: int,
        evidence: str,
        scope: str | None = None,
    ) -> TypeInfo:
        key = self._key(name, scope)
        existing = self.symbols.get(key)
        if existing is not None and existing.kind == kind:
            merged = join_types(existing.inferred, inferred)
            existing.confidence = max(existing.confidence, confidence)
            if merged != existing.inferred:
                existing.inferred = merged
                existing.evidence.append(f"join: {evidence}")
            elif evidence not in existing.evidence:
                existing.evidence.append(evidence)
            self.result.types[key] = existing
            return existing
        info = TypeInfo(
            name=name,
            kind=kind,
            inferred=inferred,
            confidence=confidence,
            lineno=lineno,
            scope=scope or self.scope,
            evidence=[evidence],
        )
        self.symbols[key] = info
        self.result.types[key] = info
        return info

    def _lookup(self, name: str) -> TypeInfo | None:
        for i in range(len(self.scope_stack), 0, -1):
            scope = ".".join(self.scope_stack[:i])
            info = self.symbols.get(f"{scope}.{name}")
            if info is not None:
                return info
        return self.symbols.get(name)

    # -- 식 추론 --
    def infer_expr(self, node: ast.expr | None) -> tuple[str, float]:
        """infer_expr 함수.

        Args:
            self: 매개변수 설명.
            node: 매개변수 설명.

        Returns:
            결과값.
        """
        if node is None:
            return "Any", 0.2
        if isinstance(node, ast.Constant):
            v = node.value
            if v is None or node.kind is None and v is None:
                return "None", 0.99
            if isinstance(v, bool):
                return "bool", 0.99
            if isinstance(v, int):
                return "int", 0.99
            if isinstance(v, float):
                return "float", 0.99
            if isinstance(v, complex):
                return "complex", 0.99
            if isinstance(v, str):
                return "str", 0.99
            if isinstance(v, bytes):
                return "bytes", 0.99
            if v is Ellipsis:
                return "Any", 0.3
            return "Any", 0.2
        if isinstance(node, ast.Name):
            if node.id in ("True", "False"):
                return "bool", 0.99
            if node.id == "None":
                return "None", 0.99
            found = self._lookup(node.id)
            if found is not None:
                return found.inferred, max(0.3, found.confidence * 0.9)
            return "Any", 0.2
        if isinstance(node, (ast.List, ast.ListComp)):
            return self._infer_sequence(node, "list")
        if isinstance(node, (ast.Set, ast.SetComp)):
            return self._infer_sequence(node, "set")
        if isinstance(node, (ast.Tuple, ast.GeneratorExp)):
            elts = node.elts if isinstance(node, ast.Tuple) else [node.elt]
            if not elts:
                return "tuple", 0.9
            parts = {self.infer_expr(e)[0] for e in elts}
            if len(parts) == 1:
                return f"tuple[{next(iter(parts))}, ...]", 0.85
            return "tuple", 0.7
        if isinstance(node, (ast.Dict, ast.DictComp)):
            return "dict", 0.85
        if isinstance(node, ast.JoinedStr):
            return "str", 0.95
        if isinstance(node, ast.NamedExpr):
            t, c = self.infer_expr(node.value)
            self._record(node.target.id, t, c, "variable", node.lineno, "walrus assignment")
            return t, c
        if isinstance(node, ast.BoolOp):
            vals = [self.infer_expr(v) for v in node.values]
            merged = vals[0][0]
            for t, _ in vals[1:]:
                merged = join_types(merged, t)
            conf = min(c for _, c in vals) * 0.8 if vals else 0.3
            return merged, conf
        if isinstance(node, ast.Compare):
            return "bool", 0.95
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.Not):
                return "bool", 0.95
            return self.infer_expr(node.operand)
        if isinstance(node, ast.BinOp):
            return self._infer_binop(node)
        if isinstance(node, ast.IfExp):
            tb, cb = self.infer_expr(node.body)[0], self.infer_expr(node.orelse)[0]
            return join_types(tb, cb), 0.7
        if isinstance(node, ast.Await):
            t, c = self.infer_expr(node.value)
            return t, c * 0.9
        if isinstance(node, ast.Starred):
            t, c = self.infer_expr(node.value)
            return t, c * 0.8
        if isinstance(node, ast.Call):
            return self._infer_call(node)
        if isinstance(node, ast.Subscript):
            return self._infer_subscript(node)
        if isinstance(node, ast.Attribute):
            return self._infer_attribute(node)
        if isinstance(node, ast.Lambda):
            return "Callable", 0.7
        if isinstance(node, ast.Slice):
            return "slice", 0.9
        return "Any", 0.2

    def _infer_sequence(
        self, node: ast.List | ast.Set | ast.ListComp | ast.SetComp, kind: str
    ) -> tuple[str, float]:
        elts: list[ast.expr] = []
        if isinstance(node, (ast.List, ast.Set)):
            elts = list(node.elts)
        elif isinstance(node, (ast.ListComp, ast.SetComp)):
            elts = [node.elt]
        if not elts:
            return kind, 0.8
        parts = {self.infer_expr(e)[0] for e in elts}
        parts.discard("Any")
        if not parts:
            return kind, 0.6
        if len(parts) == 1:
            return f"{kind}[{next(iter(parts))}]", 0.9
        return kind, 0.7

    def _infer_binop(self, node: ast.BinOp) -> tuple[str, float]:
        lt, _ = self.infer_expr(node.left)
        rt, _ = self.infer_expr(node.right)
        lbase, rbase = lt.split("[")[0], rt.split("[")[0]
        if isinstance(node.op, (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Mod, ast.Pow)):
            if lbase == "str" and rbase == "str" and isinstance(node.op, ast.Add):
                return "str", 0.9
            if lbase == "str" and isinstance(node.op, ast.Mult):
                return "str", 0.85
            if lbase in _NUMERIC_RANK and rbase in _NUMERIC_RANK:
                rank = _NUMERIC_RANK
                wider = lbase if rank[lbase] >= rank[rbase] else rbase
                return wider, 0.85
            if lbase == rbase and lbase in ("list", "tuple"):
                return lt, 0.8
            if "str" in (lbase, rbase):
                return "str", 0.5
            return "Any", 0.3
        if isinstance(node.op, (ast.BitOr, ast.BitAnd, ast.BitXor, ast.LShift, ast.RShift)):
            if lbase == "int" and rbase == "int":
                return "int", 0.85
            if lbase == rbase and lbase != "Any":
                return lbase, 0.6
            return "Any", 0.3
        if isinstance(node.op, (ast.FloorDiv, ast.MatMult)):
            if lbase in _NUMERIC_RANK and rbase in _NUMERIC_RANK:
                return lbase, 0.8
            return "Any", 0.3
        return "Any", 0.3

    def _infer_call(self, node: ast.Call) -> tuple[str, float]:
        func_name: str | None = None
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            recv_t, _ = self.infer_expr(node.func.value)
            method = node.func.attr
            recv_base = recv_t.split("[")[0]
            method_map = {
                "str": {
                    "split": "list[str]",
                    "strip": "str",
                    "join": "str",
                    "format": "str",
                    "upper": "str",
                    "lower": "str",
                    "replace": "str",
                    "get": "str",
                },
                "list": {"copy": "list", "count": "int", "index": "int", "pop": "Any"},
                "dict": {
                    "get": "Any",
                    "keys": "dict_keys",
                    "values": "dict_values",
                    "items": "dict_items",
                    "copy": "dict",
                },
                "set": {"copy": "set"},
            }
            if recv_base in method_map and method in method_map[recv_base]:
                return method_map[recv_base][method], 0.75
            return "Any", 0.3
        if func_name is None:
            return "Any", 0.2
        if func_name in _BUILTIN_RETURNS:
            base = _BUILTIN_RETURNS[func_name]
            if func_name in ("list", "dict", "set", "tuple") and node.args:
                arg_t, _ = self.infer_expr(node.args[0])
                if func_name == "list" and arg_t.startswith(("list[", "tuple[")):
                    return arg_t.replace("tuple[", "list[", 1), 0.8
                if arg_t != "Any":
                    return f"{base}[{arg_t}]" if base in ("list", "set") else base, 0.75
            return base, 0.8
        # 사용자 정의 함수: 기록된 반환 타입 참조
        for scope_key, returns in self.func_returns.items():
            if scope_key.endswith(f".{func_name}") or scope_key == func_name:
                merged = "None"
                for r in returns:
                    merged = join_types(merged, r)
                return merged, 0.6
        found = self._lookup(func_name)
        if found is not None and found.kind == "class":
            return func_name, 0.85
        return "Any", 0.25

    def _infer_subscript(self, node: ast.Subscript) -> tuple[str, float]:
        vt, _ = self.infer_expr(node.value)
        vbase = vt.split("[")[0]
        if vbase in ("list", "tuple", "set") and "[" in vt and vt.endswith("]"):
            inner = vt[len(vbase) + 1 : -1]
            if ", ..." not in inner and ", " not in inner:
                return inner, 0.8
            return inner.split(",")[0].strip(), 0.6
        if vbase == "dict":
            return "Any", 0.4
        if vbase == "str":
            return "str", 0.85
        if vbase in ("bytes",):
            return "int", 0.8
        return "Any", 0.3

    def _infer_attribute(self, node: ast.Attribute) -> tuple[str, float]:
        if isinstance(node.value, ast.Name) and node.value.id == "self" and self.class_stack:
            cls = self.class_stack[-1]
            for key, info in self.symbols.items():
                if info.kind == "attribute" and info.name == f"{cls}.{node.attr}":
                    _ = key
                    return info.inferred, max(0.4, info.confidence * 0.9)
            return "Any", 0.25
        recv_t, _ = self.infer_expr(node.value)
        if recv_t.split("[")[0] == "str" and node.attr in ("upper", "lower"):
            return "Callable", 0.5
        return "Any", 0.25

    # -- 문 방문 --
    def visit_Assign(self, node: ast.Assign) -> None:
        inferred, conf = self.infer_expr(node.value)
        for target in node.targets:
            self._assign_target(target, inferred, conf, node.lineno, "assignment")
        self.generic_visit(node.value)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        ann = annotation_to_str(node.annotation) or "Any"
        target = node.target
        if isinstance(target, ast.Name):
            if node.value is not None:
                val_t, _ = self.infer_expr(node.value)
                merged = join_types(ann, val_t) if val_t != "Any" else ann
                self._record(target.id, merged, 1.0, "variable", node.lineno, f"annotation: {ann}")
                self.generic_visit(node.value)
            else:
                self._record(target.id, ann, 1.0, "variable", node.lineno, f"annotation: {ann}")
        elif (
            isinstance(target, ast.Attribute)
            and isinstance(target.value, ast.Name)
            and target.value.id == "self"
            and self.class_stack
        ):
            cls = self.class_stack[-1]
            self._record(
                f"{cls}.{target.attr}",
                ann,
                1.0,
                "attribute",
                node.lineno,
                f"annotation: {ann}",
                scope=self.scope,
            )
            if node.value is not None:
                self.generic_visit(node.value)
        else:
            self.generic_visit(node)

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        if isinstance(node.target, ast.Name):
            val_t, _ = self.infer_expr(node.value)
            old = self._lookup(node.target.id)
            base = old.inferred if old else "Any"
            merged = join_types(base, val_t) if base != "Any" else val_t
            self._record(
                node.target.id, merged, 0.7, "variable", node.lineno, "augmented assignment"
            )
        self.generic_visit(node.value)

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        self.infer_expr(node)

    def visit_For(self, node: ast.For | ast.AsyncFor) -> None:
        iter_t, _ = self.infer_expr(node.iter)
        elem = "Any"
        if "[" in iter_t and iter_t.endswith("]"):
            elem = iter_t.split("[", 1)[1][:-1].split(",")[0].strip()
        elif iter_t in ("str", "bytes"):
            elem = iter_t
        elif iter_t in ("dict", "dict_keys", "set"):
            elem = "Any"
        elif iter_t == "range":
            elem = "int"
        self._assign_target(node.target, elem, 0.75, node.lineno, f"for-loop over {iter_t}")
        for stmt in node.body + node.orelse:
            self.visit(stmt)

    def visit_With(self, node: ast.With | ast.AsyncWith) -> None:
        for item in node.items:
            if item.optional_vars is not None:
                ctx_t, _ = self.infer_expr(item.context_expr)
                var_t = "TextIO" if ctx_t == "TextIO" else "Any"
                conf = 0.8 if var_t != "Any" else 0.3
                self._assign_target(
                    item.optional_vars, var_t, conf, node.lineno, f"with-statement ({ctx_t})"
                )
        for stmt in node.body:
            self.visit(stmt)

    def visit_FunctionDef(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        self._visit_function(node)
        # 데코레이터는 방문하지 않음 (추론과 무관)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._visit_function(node)

    def _visit_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        func_scope = f"{self.scope}.{node.name}"
        ret_ann = annotation_to_str(node.returns)
        # 인자 기록
        all_args = list(node.args.args) + list(node.args.kwonlyargs)
        defaults = [None] * (len(node.args.args) - len(node.args.defaults)) + list(
            node.args.defaults
        )
        for arg, default in zip(node.args.args, defaults):
            self._record_arg(func_scope, arg, default, node.lineno)
        for arg, default in zip(node.args.kwonlyargs, node.args.kw_defaults):
            self._record_arg(func_scope, arg, default, node.lineno)
        if node.args.vararg:
            ann = annotation_to_str(node.args.vararg.annotation)
            self._record(
                node.args.vararg.arg,
                ann or "Any",
                0.9 if ann else 0.4,
                "argument",
                node.lineno,
                "vararg",
                scope=func_scope,
            )
        if node.args.kwarg:
            ann = annotation_to_str(node.args.kwarg.annotation)
            self._record(
                node.args.kwarg.arg,
                ann or "Any",
                0.9 if ann else 0.4,
                "argument",
                node.lineno,
                "kwarg",
                scope=func_scope,
            )
        # 본문 방문 (return 수집)
        self.scope_stack.append(node.name)
        self.func_returns.setdefault(func_scope, [])
        for stmt in node.body:
            self.visit(stmt)
        self.scope_stack.pop()
        # 반환 타입 확정
        returns = self.func_returns.get(func_scope, [])
        if ret_ann:
            final = ret_ann
            conf, ev = 1.0, f"return annotation: {ret_ann}"
        elif not returns:
            final, conf, ev = "None", 0.9, "no return statement"
        else:
            final = "None"
            for r in returns:
                final = join_types(final, r)
            conf, ev = 0.75, f"inferred from {len(returns)} return(s)"
        # 함수 심볼 자체를 module 스코프에 기록 (호출 추론용)
        sig_args = ", ".join(a.arg for a in list(node.args.args) + list(node.args.kwonlyargs))
        self._record(
            node.name,
            f"Callable[[{sig_args}], {final}]",
            conf,
            "variable",
            node.lineno,
            f"function def -> {final}",
        )
        self.func_returns[func_scope] = [final]

    def _record_arg(
        self, func_scope: str, arg: ast.arg, default: ast.expr | None, lineno: int
    ) -> None:
        ann = annotation_to_str(arg.annotation)
        if ann:
            self._record(
                arg.arg,
                ann,
                1.0,
                "argument",
                arg.lineno or lineno,
                f"annotation: {ann}",
                scope=func_scope,
            )
        elif default is not None:
            t, _ = self.infer_expr(default)
            self._record(
                arg.arg,
                t,
                0.85,
                "argument",
                arg.lineno or lineno,
                "default value",
                scope=func_scope,
            )
        else:
            self._record(
                arg.arg,
                "Any",
                0.2,
                "argument",
                arg.lineno or lineno,
                "unannotated",
                scope=func_scope,
            )

    def visit_Return(self, node: ast.Return) -> None:
        func_scope = self.scope
        if node.value is None:
            t = "None"
        else:
            t, _ = self.infer_expr(node.value)
        self.func_returns.setdefault(func_scope, []).append(t)

    def visit_Yield(self, node: ast.Yield) -> None:
        func_scope = self.scope
        t = self.infer_expr(node.value)[0] if node.value else "None"
        self.func_returns.setdefault(func_scope, []).append(f"Iterator[{t}]")
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        bases = [annotation_to_str(b) or "?" for b in node.bases]
        self._record(
            node.name,
            node.name,
            1.0,
            "class",
            node.lineno,
            f"class def (bases: {', '.join(bases) or 'object'})",
        )
        self.class_stack.append(node.name)
        self.scope_stack.append(node.name)
        for stmt in node.body:
            self.visit(stmt)
        self.scope_stack.pop()
        self.class_stack.pop()

    def visit_If(self, node: ast.If) -> None:
        narrowed = self._detect_isinstance(node.test)
        if narrowed:
            name, types = narrowed
            old = self._lookup(name)
            base = old.inferred if old else "Any"
            joined = types[0]
            for t in types[1:]:
                joined = join_types(joined, t)
            self._record(
                name,
                joined,
                0.9,
                old.kind if old else "variable",
                node.lineno,
                f"isinstance narrowing: {joined} (was {base})",
            )
        for stmt in node.body + node.orelse:
            self.visit(stmt)

    @staticmethod
    def _detect_isinstance(test: ast.expr) -> tuple[str, list[str]] | None:
        """isinstance(x, T) / isinstance(x, (A, B)) 패턴 감지"""
        call = test
        if isinstance(test, ast.BoolOp):
            for v in test.values:
                r = TypeInferenceVisitor._detect_isinstance(v)
                if r:
                    return r
            return None
        if isinstance(test, ast.UnaryOp) and isinstance(test.op, ast.Not):
            return None  # else 브랜치 내로잉은 미지원 (보수적)
        if not (
            isinstance(call, ast.Call)
            and isinstance(call.func, ast.Name)
            and call.func.id == "isinstance"
            and len(call.args) == 2
        ):
            return None
        target, types_node = call.args
        if not isinstance(target, ast.Name):
            return None
        if isinstance(types_node, ast.Name):
            return target.id, [types_node.id]
        if isinstance(types_node, ast.Tuple):
            names = [e.id for e in types_node.elts if isinstance(e, ast.Name)]
            if names:
                return target.id, names
        return None

    def _assign_target(
        self, target: ast.expr, inferred: str, conf: float, lineno: int, evidence: str
    ) -> None:
        if isinstance(target, ast.Name):
            self._record(target.id, inferred, conf, "variable", lineno, evidence)
        elif isinstance(target, ast.Starred):
            self._assign_target(target.value, inferred, conf * 0.8, lineno, evidence)
        elif isinstance(target, (ast.Tuple, ast.List)):
            elem = "Any"
            if "[" in inferred and inferred.endswith("]"):
                elem = inferred.split("[", 1)[1][:-1].split(",", maxsplit=1)[0].strip()
            for elt in target.elts:
                self._assign_target(elt, elem, conf * 0.8, lineno, f"unpack from {inferred}")
        elif isinstance(target, ast.Attribute):
            if (
                isinstance(target.value, ast.Name)
                and target.value.id == "self"
                and self.class_stack
            ):
                cls = self.class_stack[-1]
                self._record(
                    f"{cls}.{target.attr}",
                    inferred,
                    conf,
                    "attribute",
                    lineno,
                    f"self assignment ({evidence})",
                    scope=self.scope,
                )
        elif isinstance(target, ast.Subscript):
            self.infer_expr(target)


def infer_source(source: str, filename: str = "<string>") -> InferenceResult:
    """소스 문자열에서 타입 추론"""
    try:
        tree = ast.parse(source, filename=filename)
    except SyntaxError as e:
        result = InferenceResult()
        result.errors.append(f"SyntaxError: {e}")
        return result
    visitor = TypeInferenceVisitor()
    try:
        visitor.visit(tree)
    except Exception as e:  # 추론 실패가 전체를 깨지 않도록
        log.warning("type inference partial failure in %s: %s", filename, e)
        visitor.result.errors.append(f"inference error: {e}")
    return visitor.result


def infer_file(path: str | Path) -> InferenceResult:
    """파일에서 타입 추론"""
    p = Path(path)
    try:
        source = p.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        result = InferenceResult()
        result.errors.append(f"read error: {e}")
        return result
    return infer_source(source, filename=str(p))


def create_type_analyzer() -> TypeInferenceVisitor:
    """방문자 인스턴스 팩토리 (외부 연동용)"""
    return TypeInferenceVisitor()
