"""
코드 품질 게이트 (Semantic Code Analysis 4/4)
- 복잡도·규모·결합·응집·데이터플로우·타입커버리지 임계값 검사
- warn(경고) / block(차단) 2단계 심각도 → CI 게이트로 직결
- metrics + dataflow + type_inference 결과를 통합 판정
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .dataflow import analyze_source as _flow_source
from .metrics import MetricsResult
from .metrics import analyze_source as _metrics_source
from .type_inference import infer_source as _infer_source

log = logging.getLogger("autonomous_coding_agent.quality_gate")


@dataclass
class GateConfig:
    """임계값 설정 (warn 초과 → 경고, block 초과 → 차단)"""

    max_complexity_warn: int = 10
    max_complexity_block: int = 20
    max_avg_complexity_warn: float = 7.0
    max_loc_warn: int = 200
    max_loc_block: int = 500
    max_params_warn: int = 5
    max_params_block: int = 8
    max_fan_out_warn: int = 7
    min_tcc_warn: float = 0.25
    max_unused_warn: int = 5
    max_use_before_def_block: int = 0
    min_type_coverage_warn: float = 0.5

    def to_dict(self) -> dict[str, Any]:
        return {
            "max_complexity_warn": self.max_complexity_warn,
            "max_complexity_block": self.max_complexity_block,
            "max_avg_complexity_warn": self.max_avg_complexity_warn,
            "max_loc_warn": self.max_loc_warn,
            "max_loc_block": self.max_loc_block,
            "max_params_warn": self.max_params_warn,
            "max_params_block": self.max_params_block,
            "max_fan_out_warn": self.max_fan_out_warn,
            "min_tcc_warn": self.min_tcc_warn,
            "max_unused_warn": self.max_unused_warn,
            "max_use_before_def_block": self.max_use_before_def_block,
            "min_type_coverage_warn": self.min_type_coverage_warn,
        }

    @classmethod
    def strict(cls) -> GateConfig:
        """엄격 프리셋 (핵심 모듈용)"""
        return cls(
            max_complexity_warn=7,
            max_complexity_block=10,
            max_avg_complexity_warn=4.0,
            max_params_warn=4,
            max_params_block=5,
            min_tcc_warn=0.5,
            min_type_coverage_warn=0.7,
        )

    @classmethod
    def lenient(cls) -> GateConfig:
        """관대 프리셋 (레거시/스크립트용)"""
        return cls(
            max_complexity_warn=15,
            max_complexity_block=30,
            max_avg_complexity_warn=10.0,
            max_loc_warn=400,
            max_loc_block=1000,
            max_params_warn=7,
            max_params_block=10,
            min_tcc_warn=0.1,
            min_type_coverage_warn=0.3,
        )


@dataclass
class Finding:
    rule: str
    target: str
    actual: Any
    threshold: Any
    severity: str  # warn | block
    message: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "rule": self.rule,
            "target": self.target,
            "actual": self.actual,
            "threshold": self.threshold,
            "severity": self.severity,
            "message": self.message,
        }


@dataclass
class GateResult:
    filename: str = "<string>"
    findings: list[Finding] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    @property
    def blocked(self) -> bool:
        return any(f.severity == "block" for f in self.findings)

    @property
    def passed(self) -> bool:
        return not self.blocked

    def warnings(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "warn"]

    def blocks(self) -> list[Finding]:
        return [f for f in self.findings if f.severity == "block"]

    def summary(self) -> str:
        w, b = len(self.warnings()), len(self.blocks())
        if self.errors:
            return f"{self.filename}: ERROR ({'; '.join(self.errors)})"
        if b:
            return f"{self.filename}: BLOCK ({b} 차단, {w} 경고)"
        if w:
            return f"{self.filename}: WARN ({w} 경고)"
        return f"{self.filename}: PASS"

    def to_dict(self) -> dict[str, Any]:
        return {
            "filename": self.filename,
            "passed": self.passed,
            "blocked": self.blocked,
            "findings": [f.to_dict() for f in self.findings],
            "errors": self.errors,
            "summary": self.summary(),
        }


def check_source(
    source: str,
    filename: str = "<string>",
    config: GateConfig | None = None,
) -> GateResult:
    """소스 문자열 품질 게이트 판정"""
    cfg = config or GateConfig()
    result = GateResult(filename=filename)
    metrics = _metrics_source(source, filename=filename)
    flow = _flow_source(source, filename=filename)
    inferred = _infer_source(source, filename=filename)
    result.errors = metrics.errors or flow.errors or inferred.errors

    def add(
        rule: str, target: str, actual: Any, threshold: Any, severity: str, message: str
    ) -> None:
        result.findings.append(Finding(rule, target, actual, threshold, severity, message))

    for f in metrics.functions:
        if f.cyclomatic > cfg.max_complexity_block:
            add(
                "complexity",
                f.scope,
                f.cyclomatic,
                cfg.max_complexity_block,
                "block",
                f"순환 복잡도 {f.cyclomatic} > 차단선 {cfg.max_complexity_block}",
            )
        elif f.cyclomatic > cfg.max_complexity_warn:
            add(
                "complexity",
                f.scope,
                f.cyclomatic,
                cfg.max_complexity_warn,
                "warn",
                f"순환 복잡도 {f.cyclomatic} > 경고선 {cfg.max_complexity_warn}",
            )
        if f.loc > cfg.max_loc_block:
            add(
                "loc",
                f.scope,
                f.loc,
                cfg.max_loc_block,
                "block",
                f"함수 길이 {f.loc}줄 > 차단선 {cfg.max_loc_block}",
            )
        elif f.loc > cfg.max_loc_warn:
            add(
                "loc",
                f.scope,
                f.loc,
                cfg.max_loc_warn,
                "warn",
                f"함수 길이 {f.loc}줄 > 경고선 {cfg.max_loc_warn}",
            )
        if f.params > cfg.max_params_block:
            add(
                "params",
                f.scope,
                f.params,
                cfg.max_params_block,
                "block",
                f"파라미터 {f.params}개 > 차단선 {cfg.max_params_block}",
            )
        elif f.params > cfg.max_params_warn:
            add(
                "params",
                f.scope,
                f.params,
                cfg.max_params_warn,
                "warn",
                f"파라미터 {f.params}개 > 경고선 {cfg.max_params_warn}",
            )
        if f.fan_out > cfg.max_fan_out_warn:
            add(
                "fan-out",
                f.scope,
                f.fan_out,
                cfg.max_fan_out_warn,
                "warn",
                f"Fan-out {f.fan_out} > 경고선 {cfg.max_fan_out_warn}",
            )

    avg = metrics.avg_complexity()
    if metrics.functions and avg > cfg.max_avg_complexity_warn:
        add(
            "avg-complexity",
            filename,
            round(avg, 2),
            cfg.max_avg_complexity_warn,
            "warn",
            f"평균 복잡도 {avg:.2f} > 경고선 {cfg.max_avg_complexity_warn}",
        )

    for c in metrics.classes:
        if c.methods > 1 and c.tcc < cfg.min_tcc_warn:
            add(
                "cohesion",
                f"{filename}:{c.name}",
                c.tcc,
                cfg.min_tcc_warn,
                "warn",
                f"클래스 {c.name} TCC {c.tcc} < 경고선 {cfg.min_tcc_warn} (LCOM {c.lcom})",
            )

    unused = flow.unused_definitions()
    if len(unused) > cfg.max_unused_warn:
        add(
            "unused",
            filename,
            len(unused),
            cfg.max_unused_warn,
            "warn",
            f"미사용 정의 {len(unused)}개 > 경고선 {cfg.max_unused_warn}",
        )

    bad_uses = flow.uses_before_def()
    if len(bad_uses) > cfg.max_use_before_def_block:
        names = sorted({u.name for u in bad_uses})[:5]
        add(
            "use-before-def",
            filename,
            len(bad_uses),
            cfg.max_use_before_def_block,
            "block",
            f"정의 없는 사용 {len(bad_uses)}개: {', '.join(names)}",
        )

    cov = inferred.coverage()
    if cov < cfg.min_type_coverage_warn:
        add(
            "type-coverage",
            filename,
            round(cov, 2),
            cfg.min_type_coverage_warn,
            "warn",
            f"타입 추론율 {cov:.0%} < 경고선 {cfg.min_type_coverage_warn:.0%}",
        )

    return result


def check_file(path: str | Path, config: GateConfig | None = None) -> GateResult:
    """파일 품질 게이트 판정"""
    p = Path(path)
    try:
        source = p.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        result = GateResult(filename=str(p))
        result.errors.append(f"read error: {e}")
        return result
    return check_source(source, filename=str(p), config=config)


def check_paths(
    paths: list[str | Path],
    config: GateConfig | None = None,
) -> list[GateResult]:
    """여러 파일/디렉토리 일괄 판정 (디렉토리는 재귀 *.py)"""
    cfg = config or GateConfig()
    files: list[Path] = []
    for p in paths:
        path = Path(p)
        if path.is_dir():
            files.extend(sorted(path.rglob("*.py")))
        elif path.is_file():
            files.append(path)
    return [check_file(f, config=cfg) for f in files]


def new_findings(baseline: GateResult, current: GateResult) -> list[Finding]:
    """baseline에 없던 차단 finding만 반환 (diff-aware 게이팅).

    기존 위반이 있는 파일도 다룰 수 있게, 새로 생긴 차단에만 반응한다.
    비교 키는 (rule, target) — 메시지의 행번호 변동은 무시.
    """
    base_keys = {(f.rule, f.target) for f in baseline.findings if f.severity == "block"}
    return [f for f in current.blocks() if (f.rule, f.target) not in base_keys]


def check_against_baseline(
    path: str | Path,
    baseline_source: str | None,
    config: GateConfig | None = None,
) -> tuple[GateResult, list[Finding]]:
    """현재 파일 vs 기준 소스 비교 판정. 신규 파일(baseline 없음)은 전체 적용."""
    current = check_file(path, config=config)
    if baseline_source is None:
        return current, current.blocks()
    base = check_source(baseline_source, filename=str(path), config=config)
    return current, new_findings(base, current)


def gate_summary(results: list[GateResult]) -> dict[str, Any]:
    """일괄 판정 요약 (CI 리포트용)"""
    passed = sum(1 for r in results if r.passed and not r.errors)
    blocked = [r.filename for r in results if r.blocked]
    errored = [r.filename for r in results if r.errors]
    warns = sum(len(r.warnings()) for r in results)
    return {
        "total": len(results),
        "passed": passed,
        "blocked": blocked,
        "errored": errored,
        "warning_count": warns,
        "all_passed": not blocked and not errored,
    }


def create_quality_gate(config: GateConfig | None = None) -> GateConfig:
    """게이트 설정 팩토리 (외부 연동용)"""
    return config or GateConfig()


__all__ = [
    "GateConfig",
    "Finding",
    "GateResult",
    "MetricsResult",
    "check_source",
    "check_file",
    "check_paths",
    "check_against_baseline",
    "new_findings",
    "gate_summary",
    "create_quality_gate",
]
