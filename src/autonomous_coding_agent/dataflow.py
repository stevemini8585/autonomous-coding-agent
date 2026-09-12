"""
데이터 플로우 분석 (Semantic Code Analysis 2/4)
- 변수 정의(Def)/사용(Use) 수집 및 Def-Use 체인 구축
- 변수·함수·클래스 단위 의존성 그래프 (data/call/import 엣지)
- reaching-definitions 기반 미사용 정의·정의 전 사용 탐지
- 순수 stdlib(ast) 구현, type_inference와 상호 보완
"""

from __future__ import annotations

import ast
import builtins
import logging
from collections import defaultdict, deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

log = logging.getLogger("autonomous_coding_agent.dataflow")

# 도달 정의가 없어도 정상인 이름 (내장 + 모듈 던더 + 관용구)
_BUILTIN_NAMES = (
    set(dir(builtins))
    | {"self", "cls"}
    | {
        "__name__",
        "__doc__",
        "__package__",
        "__loader__",
        "__spec__",
        "__file__",
        "__cached__",
        "__builtins__",
        "__annotations__",
    }
)


@dataclass
class Definition:
    """단일 정의 지점"""

    name: str
    lineno: int
    col: int = 0
    kind: str = "assign"  # assign | argument | import | for | with | function | class
    scope: str = "module"
    killed: bool = False  # 이후 재정의로 무효화됐는지

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "lineno": self.lineno,
            "col": self.col,
            "kind": self.kind,
            "scope": self.scope,
            "killed": self.killed,
        }


@dataclass
class Use:
    """단일 사용 지점"""

    name: str
    lineno: int
    col: int = 0
    ctx: str = "load"  # load | call | attribute | subscript
    scope: str = "module"
    reaching: list[int] = field(default_factory=list)  # 도달 가능한 정의 행 번호

    def to_dict(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "lineno": self.lineno,
            "col": self.col,
            "ctx": self.ctx,
            "scope": self.scope,
            "reaching": self.reaching,
        }


@dataclass
class DefUseChain:
    """정의 → 사용 목록 체인"""

    definition: Definition
    uses: list[Use] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {"definition": self.definition.to_dict(), "uses": [u.to_dict() for u in self.uses]}


@dataclass
class DependencyEdge:
    src: str
    dst: str
    kind: str = "data"  # data | call | import | base

    def to_dict(self) -> dict[str, Any]:
        return {"src": self.src, "dst": self.dst, "kind": self.kind}


@dataclass
class AnalysisResult:
    """파일/소스 단위 분석 결과"""

    definitions: list[Definition] = field(default_factory=list)
    uses: list[Use] = field(default_factory=list)
    chains: list[DefUseChain] = field(default_factory=list)
    edges: list[DependencyEdge] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    # -- 조회 API --
    def defs_of(self, name: str, scope: str | None = None) -> list[Definition]:
        return [
            d for d in self.definitions if d.name == name and (scope is None or d.scope == scope)
        ]

    def uses_of(self, name: str, scope: str | None = None) -> list[Use]:
        return [u for u in self.uses if u.name == name and (scope is None or u.scope == scope)]

    def chain_of(self, name: str, lineno: int) -> DefUseChain | None:
        for c in self.chains:
            if c.definition.name == name and c.definition.lineno == lineno:
                return c
        return None

    def depends_on(self, node: str) -> list[str]:
        """node가 의존하는 대상 목록 (엣지: 의존자 → 피의존자)"""
        return sorted({e.dst for e in self.edges if e.src == node})

    def dependents_of(self, node: str) -> list[str]:
        """node에 의존하는 주체 목록"""
        return sorted({e.src for e in self.edges if e.dst == node})

    def unused_definitions(self) -> list[Definition]:
        """한 번도 사용되지 않은 정의 (사망 코드 후보)"""
        used_keys = {(u.name, u.scope) for u in self.uses}
        out = []
        for d in self.definitions:
            if d.kind in ("import", "function", "class"):
                continue  # 공개 API일 수 있어 제외
            if (d.name, d.scope) not in used_keys and not any(u.name == d.name for u in self.uses):
                out.append(d)
        return out

    def uses_before_def(self) -> list[Use]:
        """도달 정의가 없는 사용 (정의 전 사용/미정의 변수 후보, 내장 제외)"""
        return [
            u
            for u in self.uses
            if not u.reaching and u.ctx in ("load", "call") and u.name not in _BUILTIN_NAMES
        ]

    def topological_order(self) -> list[str]:
        """피의존자가 먼저 오도록 위상 정렬 (사이클 시 잔여는 사전순 추가)"""
        nodes: set[str] = set()
        for e in self.edges:
            nodes.add(e.src)
            nodes.add(e.dst)
        indeg: dict[str, int] = dict.fromkeys(nodes, 0)
        adj: dict[str, set[str]] = defaultdict(set)
        # 엣지 src→dst = "src가 dst에 의존" → dst가 먼저
        for e in self.edges:
            if e.src not in adj[e.dst]:
                adj[e.dst].add(e.src)
                indeg[e.src] += 1
        queue: deque[str] = deque(sorted(n for n in nodes if indeg[n] == 0))
        order: list[str] = []
        while queue:
            n = queue.popleft()
            order.append(n)
            for m in sorted(adj[n]):
                indeg[m] -= 1
                if indeg[m] == 0:
                    queue.append(m)
        for n in sorted(nodes):
            if n not in order:
                order.append(n)
        return order

    def to_dict(self) -> dict[str, Any]:
        return {
            "definitions": [d.to_dict() for d in self.definitions],
            "uses": [u.to_dict() for u in self.uses],
            "chains": [c.to_dict() for c in self.chains],
            "edges": [e.to_dict() for e in self.edges],
            "unused": [d.to_dict() for d in self.unused_definitions()],
            "uses_before_def": [u.to_dict() for u in self.uses_before_def()],
            "errors": self.errors,
        }


class _Collector(ast.NodeVisitor):
    """정의/사용 이벤트 수집 (순서 보존, 스코프 추적)"""

    def __init__(self) -> None:
        self.scope_stack: list[str] = ["module"]
        self.defs: list[Definition] = []
        self.uses: list[Use] = []
        self.func_stack: list[str] = []
        self.class_stack: list[str] = []

    @property
    def scope(self) -> str:
        return ".".join(self.scope_stack)

    def _add_def(
        self, name: str, node: ast.AST, kind: str, col_override: int | None = None
    ) -> None:
        self.defs.append(
            Definition(
                name=name,
                lineno=getattr(node, "lineno", 0),
                col=col_override if col_override is not None else getattr(node, "col_offset", 0),
                kind=kind,
                scope=self.scope,
            )
        )

    def _add_use(self, name: str, node: ast.AST, ctx: str = "load") -> None:
        self.uses.append(
            Use(
                name=name,
                lineno=getattr(node, "lineno", 0),
                col=getattr(node, "col_offset", 0),
                ctx=ctx,
                scope=self.scope,
            )
        )

    # -- 정의 노드 --
    def visit_FunctionDef(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        self._add_def(node.name, node, "function")
        for dec in node.decorator_list:
            self.visit(dec)
        self._visit_function(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.visit_FunctionDef(node)

    def _visit_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        self.scope_stack.append(node.name)
        self.func_stack.append(node.name)
        args = node.args
        posonly = getattr(args, "posonlyargs", [])
        for a in list(posonly) + list(args.args) + list(args.kwonlyargs):
            self._add_def(a.arg, a, "argument")
        if args.vararg:
            self._add_def(args.vararg.arg, args.vararg, "argument")
        if args.kwarg:
            self._add_def(args.kwarg.arg, args.kwarg, "argument")
        for d in list(args.defaults) + [x for x in args.kw_defaults if x]:
            self.visit(d)
        for stmt in node.body:
            self.visit(stmt)
        self.func_stack.pop()
        self.scope_stack.pop()

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self._add_def(node.name, node, "class")
        for dec in node.decorator_list:
            self.visit(dec)
        for b in node.bases:
            self.visit(b)
        for kw in node.keywords:
            self.visit(kw)
        self.scope_stack.append(node.name)
        self.class_stack.append(node.name)
        for stmt in node.body:
            self.visit(stmt)
        self.class_stack.pop()
        self.scope_stack.pop()

    def visit_Import(self, node: ast.Import) -> None:
        for a in node.names:
            self._add_def(a.asname or a.name.split(".")[0], node, "import")

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        for a in node.names:
            if a.name == "*":
                continue
            self._add_def(a.asname or a.name, node, "import")

    def visit_Assign(self, node: ast.Assign) -> None:
        self.visit(node.value)
        for t in node.targets:
            self._def_target(t, "assign")

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        if node.value:
            self.visit(node.value)
        self.visit(node.annotation)
        self._def_target(node.target, "assign")

    def visit_AugAssign(self, node: ast.AugAssign) -> None:
        # x += 1 은 사용 + 정의 동시
        if isinstance(node.target, ast.Name):
            self._add_use(node.target.id, node.target)
        self.visit(node.value)
        self._def_target(node.target, "assign")

    def visit_NamedExpr(self, node: ast.NamedExpr) -> None:
        self.visit(node.value)
        if isinstance(node.target, ast.Name):
            self._add_def(node.target.id, node, "assign")

    def visit_For(self, node: ast.For | ast.AsyncFor) -> None:
        self.visit(node.iter)
        self._def_target(node.target, "for")
        for s in node.body + node.orelse:
            self.visit(s)

    def visit_AsyncFor(self, node: ast.AsyncFor) -> None:
        self.visit_For(node)

    def visit_With(self, node: ast.With | ast.AsyncWith) -> None:
        for item in node.items:
            self.visit(item.context_expr)
            if item.optional_vars:
                self._def_target(item.optional_vars, "with")
        for s in node.body:
            self.visit(s)

    def visit_AsyncWith(self, node: ast.AsyncWith) -> None:
        self.visit_With(node)

    def visit_ExceptHandler(self, node: ast.ExceptHandler) -> None:
        if node.type:
            self.visit(node.type)
        if node.name:
            self._add_def(node.name, node, "assign")
        for s in node.body:
            self.visit(s)

    def visit_comprehension(self, node: ast.comprehension) -> None:  # noqa: N802
        self.visit(node.iter)
        # 내포 타겟은 같은 행의 elt/조건보다 텍스트상 뒤에 있어도
        # 의미상 먼저 정의되므로 col=0으로 기록 (오탐 방지)
        self._def_target(node.target, "assign", col_override=0)
        for cond in node.ifs:
            self.visit(cond)

    def visit_ListComp(self, node: ast.ListComp) -> None:
        for gen in node.generators:
            self.visit(gen)
        self.visit(node.elt)

    def visit_SetComp(self, node: ast.SetComp) -> None:
        for gen in node.generators:
            self.visit(gen)
        self.visit(node.elt)

    def visit_GeneratorExp(self, node: ast.GeneratorExp) -> None:
        for gen in node.generators:
            self.visit(gen)
        self.visit(node.elt)

    def visit_DictComp(self, node: ast.DictComp) -> None:
        for gen in node.generators:
            self.visit(gen)
        self.visit(node.key)
        self.visit(node.value)

    def _def_target(self, target: ast.expr, kind: str, col_override: int | None = None) -> None:
        if isinstance(target, ast.Name):
            self._add_def(target.id, target, kind, col_override=col_override)
        elif isinstance(target, ast.Starred):
            self._def_target(target.value, kind, col_override=col_override)
        elif isinstance(target, (ast.Tuple, ast.List)):
            for e in target.elts:
                self._def_target(e, kind, col_override=col_override)
        elif isinstance(target, ast.Attribute):
            # self.x = ... → 클래스 속성 정의로 기록
            if (
                isinstance(target.value, ast.Name)
                and target.value.id == "self"
                and self.class_stack
            ):
                cls = self.class_stack[-1]
                self.defs.append(
                    Definition(
                        name=f"{cls}.{target.attr}",
                        lineno=target.lineno,
                        col=target.col_offset,
                        kind="assign",
                        scope=self.scope,
                    )
                )
                self.visit(target.value)
            else:
                self.generic_visit(target)
        elif isinstance(target, ast.Subscript):
            self.generic_visit(target)

    # -- 사용 노드 --
    def visit_Name(self, node: ast.Name) -> None:
        if isinstance(node.ctx, ast.Load):
            self._add_use(node.id, node)

    def visit_Call(self, node: ast.Call) -> None:
        func = node.func
        if isinstance(func, ast.Name):
            self._add_use(func.id, func, ctx="call")
        else:
            self.visit(func)
        for a in node.args:
            self.visit(a)
        for kw in node.keywords:
            self.visit(kw)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if isinstance(node.value, ast.Name):
            self._add_use(node.value.id, node.value, ctx="attribute")
        else:
            self.visit(node.value)

    def visit_Lambda(self, node: ast.Lambda) -> None:
        # 람다 인자는 정의로 기록 (미기록 시 본문 사용이 오탐됨)
        posonly = getattr(node.args, "posonlyargs", [])
        for a in list(posonly) + list(node.args.args) + list(node.args.kwonlyargs):
            self._add_def(a.arg, a, "argument")
        if node.args.vararg:
            self._add_def(node.args.vararg.arg, node.args.vararg, "argument")
        if node.args.kwarg:
            self._add_def(node.args.kwarg.arg, node.args.kwarg, "argument")
        self.visit(node.body)

    def visit_Return(self, node: ast.Return) -> None:
        if node.value:
            self.visit(node.value)

    def visit_Delete(self, node: ast.Delete) -> None:
        for t in node.targets:
            if isinstance(t, ast.Name):
                self._add_use(t.id, t)
            else:
                self.visit(t)


def _scope_visible(def_scope: str, use_scope: str) -> bool:
    """use 위치에서 def 스코프가 보이는지 (자신/조상 스코프)"""
    if def_scope == "module":
        return True
    return use_scope == def_scope or use_scope.startswith(def_scope + ".")


def analyze_source(source: str, filename: str = "<string>") -> AnalysisResult:
    """소스 문자열 데이터 플로우 분석"""
    result = AnalysisResult()
    try:
        tree = ast.parse(source, filename=filename)
    except SyntaxError as e:
        result.errors.append(f"SyntaxError: {e}")
        return result
    collector = _Collector()
    try:
        collector.visit(tree)
    except Exception as e:  # 수집 실패가 전체를 깨지 않도록
        log.warning("dataflow collection partial failure in %s: %s", filename, e)
        result.errors.append(f"collection error: {e}")
    result.definitions = collector.defs
    result.uses = collector.uses

    # -- reaching 정의 계산 + 체인 구축 --
    # (name)별 정의 목록: 같은 이름 정의는 시간순, kill 표시
    defs_by_name: dict[str, list[Definition]] = defaultdict(list)
    for d in result.definitions:
        defs_by_name[d.name].append(d)
    for dlist in defs_by_name.values():
        dlist.sort(key=lambda d: (d.lineno, d.col))
        for i, d in enumerate(dlist):
            # 같은 스코프 내 이후 정의가 있으면 kill
            later = [x for x in dlist[i + 1 :] if x.scope == d.scope]
            d.killed = bool(later)

    chains: dict[tuple[str, int, str], DefUseChain] = {}
    for d in result.definitions:
        chains[(d.name, d.lineno, d.scope)] = DefUseChain(definition=d)

    for u in result.uses:
        cands = [
            d
            for d in defs_by_name.get(u.name, [])
            if (d.lineno, d.col) < (u.lineno, u.col) and _scope_visible(d.scope, u.scope)
        ]
        # 같은 스코프 정의를 우선, 없으면 조상/모듈 스코프
        same = [d for d in cands if d.scope == u.scope]
        pool = same or cands
        if pool:
            # 가장 가까운(마지막) 정의가 reaching, 같은 행 이전 정의도 포함
            pool.sort(key=lambda d: (d.lineno, d.col))
            u.reaching = [d.lineno for d in pool if d.lineno <= u.lineno]
            last = pool[-1]
            key = (last.name, last.lineno, last.scope)
            if key in chains:
                chains[key].uses.append(u)
    result.chains = list(chains.values())

    # -- 의존성 그래프 --
    edges: dict[tuple[str, str, str], DependencyEdge] = {}

    def add_edge(src: str, dst: str, kind: str) -> None:
        if src and dst and src != dst:
            edges[(src, dst, kind)] = DependencyEdge(src, dst, kind)

    # 1) data 엣지: 같은 스코프 내 정의 행 → 그 값을 읽는 정의 행
    #    (행 번호 기반: def 라인 집합 → use 라인)
    line_defs: dict[int, list[Definition]] = defaultdict(list)
    for d in result.definitions:
        line_defs[d.lineno].append(d)
    for u in result.uses:
        if not u.reaching:
            continue
        src_def = None
        for d in defs_by_name.get(u.name, []):
            if d.lineno == u.reaching[-1] and _scope_visible(d.scope, u.scope):
                src_def = d
                break
        if src_def is None:
            continue
        for consumer in line_defs.get(u.lineno, []):
            if consumer.name != u.name:
                dst_node = f"{src_def.scope}.{src_def.name}"
                src_node = f"{consumer.scope}.{consumer.name}"
                add_edge(src_node, dst_node, "data")

    # 2) call 엣지: 호출자 스코프 → 피호출 함수
    func_names = {d.name for d in result.definitions if d.kind == "function"}
    for u in result.uses:
        if u.ctx == "call" and u.name in func_names:
            add_edge(u.scope, f"module.{u.name}" if "." not in u.name else u.name, "call")

    # 3) import 엣지: 정의된 import 이름 → 원본 모듈(근사: 이름 자체)
    for d in result.definitions:
        if d.kind == "import":
            add_edge(f"{d.scope}.{d.name}", f"<import>.{d.name}", "import")

    # 4) base 엣지: 서브클래스 → 베이스 (소스 재파싱 없이 Collector에서 불가 → 생략)
    result.edges = list(edges.values())
    _add_base_edges(source, result, edges)
    result.edges = list(edges.values())
    return result


def _add_base_edges(
    source: str, result: AnalysisResult, edges: dict[tuple[str, str, str], DependencyEdge]
) -> None:
    """클래스 상속 엣지 추가 (경량 재파싱)"""
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for b in node.bases:
                if isinstance(b, ast.Name):
                    key = (f"module.{node.name}", f"module.{b.id}", "base")
                    edges[key] = DependencyEdge(*key)


def analyze_file(path: str | Path) -> AnalysisResult:
    """파일 데이터 플로우 분석"""
    p = Path(path)
    result = AnalysisResult()
    try:
        source = p.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        result.errors.append(f"read error: {e}")
        return result
    return analyze_source(source, filename=str(p))


def create_dataflow_analyzer() -> _Collector:
    """수집기 팩토리 (외부 연동용)"""
    return _Collector()
