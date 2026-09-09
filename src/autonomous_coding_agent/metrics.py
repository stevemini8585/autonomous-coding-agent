"""
코드 품질 메트릭 (Semantic Code Analysis 3/4)
- McCabe 순환 복잡도 (함수/메서드/모듈 단위)
- Fan-in / Fan-out (dataflow 호출 그래프 기반 결합도)
- LCOM + TCC (클래스 응집도)
- 위험도 등급 판정 (McCabe 기준)
- 순수 stdlib(ast) 구현
"""

from __future__ import annotations

import ast
import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .dataflow import analyze_source as _analyze_dataflow

log = logging.getLogger("autonomous_coding_agent.metrics")

# McCabe 위험도 임계값 (고전 기준)
LOW_MAX = 10
MODERATE_MAX = 20
HIGH_MAX = 50


def risk_rank(complexity: int) -> str:
    """McCabe 기준 위험도 등급"""
    if complexity <= LOW_MAX:
        return "low"
    if complexity <= MODERATE_MAX:
        return "moderate"
    if complexity <= HIGH_MAX:
        return "high"
    return "untestable"


class _ComplexityVisitor(ast.NodeVisitor):
    """단일 함수 본문 순환 복잡도 계산"""

    def __init__(self) -> None:
        self.complexity = 1  # 기본 경로
        self.max_nesting = 0
        self._nesting = 0

    def _branch(self, node: ast.AST) -> None:
        self.complexity += 1
        self._nesting += 1
        self.max_nesting = max(self.max_nesting, self._nesting)
        self.generic_visit(node)
        self._nesting -= 1

    def visit_If(self, node: ast.If) -> None:
        self._branch(node)

    def visit_For(self, node: ast.For | ast.AsyncFor) -> None:
        self._branch(node)

    def visit_AsyncFor(self, node: ast.AsyncFor) -> None:
        self._branch(node)

    def visit_While(self, node: ast.While) -> None:
        self._branch(node)

    def visit_ExceptHandler(self, node: ast.ExceptHandler) -> None:
        self.complexity += 1
        self.generic_visit(node)

    def visit_IfExp(self, node: ast.IfExp) -> None:
        self.complexity += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node: ast.BoolOp) -> None:
        # a and b and c → 2 추가 결정점
        self.complexity += max(0, len(node.values) - 1)
        self.generic_visit(node)

    def visit_comprehension(self, node: ast.comprehension) -> None:  # noqa: N802
        self.complexity += 1 + len(node.ifs)
        self.generic_visit(node)

    def visit_Match(self, node: ast.Match) -> None:
        self.complexity += max(0, len(node.cases))
        self.generic_visit(node)

    def visit_Assert(self, node: ast.Assert) -> None:
        self.complexity += 1
        self.generic_visit(node)

    # 중첩 함수/클래스는 별도 단위로 측정 → 내부는 건너뜀
    def visit_FunctionDef(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        pass

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        pass

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        pass

    def visit_Lambda(self, node: ast.Lambda) -> None:
        pass


@dataclass
class FunctionMetrics:
    name: str
    scope: str = "module"
    lineno: int = 0
    cyclomatic: int = 1
    max_nesting: int = 0
    loc: int = 0
    params: int = 0
    returns: int = 0
    fan_in: int = 0
    fan_out: int = 0
    rank: str = "low"

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "scope": self.scope,
            "lineno": self.lineno,
            "cyclomatic": self.cyclomatic,
            "max_nesting": self.max_nesting,
            "loc": self.loc,
            "params": self.params,
            "returns": self.returns,
            "fan_in": self.fan_in,
            "fan_out": self.fan_out,
            "rank": self.rank,
        }


@dataclass
class ClassMetrics:
    name: str
    lineno: int = 0
    methods: int = 0
    attributes: int = 0
    lcom: int = 0
    tcc: float = 1.0
    rank: str = "good"  # good | fair | poor (응집도 등급)

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "lineno": self.lineno,
            "methods": self.methods,
            "attributes": self.attributes,
            "lcom": self.lcom,
            "tcc": self.tcc,
            "rank": self.rank,
        }


@dataclass
class MetricsResult:
    functions: list[FunctionMetrics] = field(default_factory=list)
    classes: list[ClassMetrics] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    # -- 집계 --
    def avg_complexity(self) -> float:
        if not self.functions:
            return 0.0
        return sum(f.cyclomatic for f in self.functions) / len(self.functions)

    def max_complexity(self) -> int:
        return max((f.cyclomatic for f in self.functions), default=0)

    def worst_offenders(self, n: int = 5) -> list[FunctionMetrics]:
        return sorted(self.functions, key=lambda f: -f.cyclomatic)[:n]

    def high_risk(self) -> list[FunctionMetrics]:
        return [f for f in self.functions if f.rank in ("high", "untestable")]

    def low_cohesion(self) -> list[ClassMetrics]:
        return [c for c in self.classes if c.rank == "poor"]

    def get_function(self, name: str) -> FunctionMetrics | None:
        for f in self.functions:
            if f.name == name or f.scope.endswith(f".{name}"):
                return f
        return None

    def to_dict(self) -> dict[str, Any]:
        return {
            "functions": [f.to_dict() for f in self.functions],
            "classes": [c.to_dict() for c in self.classes],
            "avg_complexity": self.avg_complexity(),
            "max_complexity": self.max_complexity(),
            "errors": self.errors,
        }


def _loc(node: ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef) -> int:
    end = getattr(node, "end_lineno", None) or node.lineno
    return max(1, end - node.lineno + 1)


def _count_params(node: ast.FunctionDef | ast.AsyncFunctionDef) -> int:
    a = node.args
    n = len(a.args) + len(a.kwonlyargs)
    if a.vararg:
        n += 1
    if a.kwarg:
        n += 1
    # self/cls 제외
    if a.args and a.args[0].arg in ("self", "cls"):
        n -= 1
    return max(0, n)


def _method_attributes(method: ast.FunctionDef | ast.AsyncFunctionDef) -> set[str]:
    """메서드 내 self.x 접근 집합"""
    attrs: set[str] = set()
    for n in ast.walk(method):
        if isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name) and n.value.id == "self":
            attrs.add(n.attr)
    return attrs


def _class_metrics(node: ast.ClassDef) -> ClassMetrics:
    methods = [n for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    attr_sets = [_method_attributes(m) for m in methods]
    all_attrs = set().union(*attr_sets) if attr_sets else set()
    n = len(methods)
    pairs = n * (n - 1) // 2
    if pairs == 0:
        return ClassMetrics(
            name=node.name,
            lineno=node.lineno,
            methods=n,
            attributes=len(all_attrs),
            lcom=0,
            tcc=1.0,
            rank="good",
        )
    shared = sum(1 for i in range(n) for j in range(i + 1, n) if attr_sets[i] & attr_sets[j])
    disjoint = pairs - shared
    lcom = max(0, disjoint - shared)  # CK LCOM
    tcc = shared / pairs
    rank = "good" if tcc >= 0.5 else ("fair" if tcc >= 0.25 else "poor")
    return ClassMetrics(
        name=node.name,
        lineno=node.lineno,
        methods=n,
        attributes=len(all_attrs),
        lcom=lcom,
        tcc=round(tcc, 3),
        rank=rank,
    )


def analyze_source(source: str, filename: str = "<string>") -> MetricsResult:
    """소스 문자열 메트릭 분석"""
    result = MetricsResult()
    try:
        tree = ast.parse(source, filename=filename)
    except SyntaxError as e:
        result.errors.append(f"SyntaxError: {e}")
        return result

    # 함수/클래스 수집 (스코프 추적)
    func_nodes: list[tuple[str, ast.FunctionDef | ast.AsyncFunctionDef]] = []
    class_nodes: list[ast.ClassDef] = []
    stack: list[str] = ["module"]

    def visit_block(stmts: list[ast.stmt]) -> None:
        for stmt in stmts:
            if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                scope = ".".join(stack + [stmt.name])
                func_nodes.append((scope, stmt))
                stack.append(stmt.name)
                visit_block(stmt.body)
                stack.pop()
            elif isinstance(stmt, ast.ClassDef):
                class_nodes.append(stmt)
                stack.append(stmt.name)
                visit_block(stmt.body)
                stack.pop()
            else:
                for child in ast.iter_child_nodes(stmt):
                    if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        scope = ".".join(stack + [child.name])
                        func_nodes.append((scope, child))
                        stack.append(child.name)
                        visit_block(child.body)
                        stack.pop()
                    elif isinstance(child, ast.ClassDef):
                        class_nodes.append(child)
                        stack.append(child.name)
                        visit_block(child.body)
                        stack.pop()

    try:
        visit_block(tree.body)
    except Exception as e:
        log.warning("metrics collection partial failure in %s: %s", filename, e)
        result.errors.append(f"collection error: {e}")

    for scope, node in func_nodes:
        v = _ComplexityVisitor()
        for stmt in node.body:
            v.visit(stmt)
        f = FunctionMetrics(
            name=node.name,
            scope=scope,
            lineno=node.lineno,
            cyclomatic=v.complexity,
            max_nesting=v.max_nesting,
            loc=_loc(node),
            params=_count_params(node),
            returns=sum(isinstance(n, ast.Return) for n in node.body for n in ast.walk(n)),
            rank=risk_rank(v.complexity),
        )
        result.functions.append(f)

    for cls in class_nodes:
        result.classes.append(_class_metrics(cls))

    # Fan-in / Fan-out (dataflow 호출 엣지)
    try:
        flow = _analyze_dataflow(source, filename=filename)
        call_edges = [(e.src, e.dst) for e in flow.edges if e.kind == "call"]
        for f in result.functions:
            callees = {dst.split(".")[-1] for src, dst in call_edges if src == f.scope}
            callers = {src for src, dst in call_edges if dst.split(".")[-1] == f.name}
            f.fan_out = len(callees)
            f.fan_in = len(callers)
    except Exception as e:  # 팬 분석 실패는 메트릭 전체를 깨지 않음
        log.warning("fan analysis failed in %s: %s", filename, e)

    return result


def analyze_file(path: str | Path) -> MetricsResult:
    """파일 메트릭 분석"""
    p = Path(path)
    result = MetricsResult()
    try:
        source = p.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        result.errors.append(f"read error: {e}")
        return result
    return analyze_source(source, filename=str(p))


def create_metrics_analyzer() -> type[MetricsResult]:
    """결과 타입 팩토리 (외부 연동용)"""
    return MetricsResult
