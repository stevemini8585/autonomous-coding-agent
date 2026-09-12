"""자체 벤치 v1 — 과거 머지 이슈로 플래너 파일 재현율 측정 (결정적, LLM 없음).

측정 대상: 플래닝(어떤 파일을 고칠지 맞추나). 생성 품질은 측정하지 않음.
실행: PYTHONPATH=src venv/bin/python eval/bench_plan.py
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).parent.parent
sys.path.insert(0, str(REPO / "src"))

# issue: (goal, fix_commit) — base = fix_commit^, gold = base..fix diff
CASES = {
    "issue-3": ("Add GET /ping endpoint to dashboard", "46e50db"),
    "issue-5": ("Add edge case unit test for join_types", "31aff48"),
    "issue-15": ("Rename single letter locals in notify send_telegram", "8dc1a4c"),
    "issue-17": ("Add retry counter to send_telegram docstring usage", "ea4857b"),
}

THRESHOLD = 0.6


def sh(*args: str) -> str:
    r = subprocess.run(args, cwd=REPO, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        raise RuntimeError(f"{' '.join(args)} -> {r.returncode}: {r.stderr[:300]}")
    return r.stdout.strip()


def gold_files(fix: str) -> list[str]:
    out = sh("git", "diff", f"{fix}^", fix, "--name-only")
    gold = []
    for f in out.splitlines():
        base = f.split("/")[-1]
        if not f.endswith(".py"):
            continue
        if "/tests/" in f or base.startswith("test_") or base.endswith("_test.py"):
            continue  # 테스트·오염 부산물 제외
        gold.append(f)
    return gold


def plan_files(goal: str, base: str) -> list[str]:
    from autonomous_coding_agent.explorer import CodeExplorer
    from autonomous_coding_agent.planner import WorkPlanner

    tmp = Path(tempfile.mkdtemp(prefix="eval_wt_"))
    wt = tmp / "wt"
    sh("git", "worktree", "add", "--detach", str(wt), base)
    try:
        explorer = CodeExplorer(wt)
        result = explorer.explore()
        plan = WorkPlanner(wt).create_plan(goal, result)
        files: list[str] = []
        for step in plan.steps:
            files.extend(getattr(step, "assigned_files", []) or [])
        return files
    finally:
        subprocess.run(
            ["git", "worktree", "remove", "--force", str(wt)],
            cwd=REPO,
            capture_output=True,
            timeout=60,
        )


def main() -> int:
    report = {"cases": [], "threshold": THRESHOLD}
    recalls = []
    for name, (goal, fix) in CASES.items():
        base = sh("git", "rev-parse", "--short", f"{fix}^")
        gold = gold_files(fix)
        planned = plan_files(goal, base)
        hit = [g for g in gold if any(p.endswith(g.split("/")[-1]) for p in planned)]
        recall = len(hit) / len(gold) if gold else 1.0
        recalls.append(recall)
        report["cases"].append(
            {
                "issue": name,
                "goal": goal,
                "base": base,
                "fix": fix[:7],
                "gold": gold,
                "planned": sorted(set(planned)),
                "recall": round(recall, 3),
            }
        )
        print(f"{name}: recall={recall:.2f} gold={gold}", flush=True)
    macro = sum(recalls) / len(recalls) if recalls else 0.0
    report["macro_recall"] = round(macro, 3)
    report["pass"] = macro >= THRESHOLD
    out = REPO / "eval" / "results.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"macro_recall={macro:.3f} pass={report['pass']} -> {out}")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
