"""
오머지 롤백 자동화 (Phase 3 Day 4)
- 머지된 PR → revert 브랜치 → revert PR 생성 → 연결 이슈 재오픈 → 알림
- 기본은 PR 경유 revert (main 직접 푸시 금지), 모든 단계 기록
- dry_run은 읽기(gh pr view, git status)만 수행, 변경 없음
"""

from __future__ import annotations

import logging
import subprocess
from contextlib import suppress
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .notify import send_telegram

log = logging.getLogger("autonomous_coding_agent.rollback")


@dataclass
class RollbackConfig:
    dry_run: bool = False
    base: str = "main"
    remote: str = "origin"
    reopen_issue: bool = True
    notify_telegram: bool = True

    def to_dict(self) -> dict[str, Any]:
        return {
            "dry_run": self.dry_run,
            "base": self.base,
            "remote": self.remote,
            "reopen_issue": self.reopen_issue,
            "notify_telegram": self.notify_telegram,
        }


@dataclass
class RollbackPlan:
    pr_number: int
    pr_title: str = ""
    pr_url: str = ""
    merge_sha: str = ""
    base: str = "main"
    head: str = ""
    branch: str = ""
    linked_issues: list[int] = field(default_factory=list)
    steps: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "pr_number": self.pr_number,
            "pr_title": self.pr_title,
            "pr_url": self.pr_url,
            "merge_sha": self.merge_sha,
            "base": self.base,
            "head": self.head,
            "branch": self.branch,
            "linked_issues": self.linked_issues,
            "steps": self.steps,
        }


@dataclass
class RollbackResult:
    pr_number: int
    success: bool = False
    dry_run: bool = False
    revert_pr_number: int | None = None
    revert_pr_url: str | None = None
    reopened_issues: list[int] = field(default_factory=list)
    error: str | None = None
    plan: RollbackPlan | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "pr_number": self.pr_number,
            "success": self.success,
            "dry_run": self.dry_run,
            "revert_pr_number": self.revert_pr_number,
            "revert_pr_url": self.revert_pr_url,
            "reopened_issues": self.reopened_issues,
            "error": self.error,
            "plan": self.plan.to_dict() if self.plan else None,
        }


class RollbackError(RuntimeError):
    pass


def _run(cmd: list[str], workspace: Path, timeout: int = 60) -> subprocess.CompletedProcess:
    log.debug("run: %s", " ".join(cmd))
    return subprocess.run(cmd, cwd=workspace, capture_output=True, text=True, timeout=timeout)


def _run_json(cmd: list[str], workspace: Path) -> dict[str, Any] | None:
    import json

    r = _run(cmd, workspace)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout or "{}")
    except ValueError:
        return None


def _run_checked(cmd: list[str], workspace: Path, timeout: int = 120) -> str:
    """실패 시 RollbackError (try 블록 밖 raise → TRY301 준수)"""
    r = _run(cmd, workspace, timeout=timeout)
    if r.returncode != 0:
        raise RollbackError(f"실패: {' '.join(cmd)}\n{r.stderr.strip()[:500]}")
    return r.stdout


def get_merged_pr(number: int, workspace: str | Path) -> dict[str, Any] | None:
    """머지된 PR 정보 조회 (읽기 전용)"""
    ws = Path(workspace)
    return _run_json(
        [
            "gh",
            "pr",
            "view",
            str(number),
            "--json",
            "number,title,state,mergeCommit,baseRefName,headRefName,url," "closingIssuesReferences",
        ],
        ws,
    )


def working_tree_clean(workspace: str | Path) -> bool:
    r = _run(["git", "status", "--porcelain"], Path(workspace))
    return r.returncode == 0 and not r.stdout.strip()


def plan_rollback(number: int, workspace: str | Path, base: str = "main") -> RollbackPlan:
    """롤백 계획 수립 (읽기 전용, 변경 없음)"""
    info = get_merged_pr(number, workspace)
    if not info:
        raise RollbackError(f"PR #{number} 조회 실패 (gh 인증/번호 확인)")
    if info.get("state") != "MERGED":
        raise RollbackError(f"PR #{number}는 머지 상태가 아님 (state={info.get('state')})")
    merge_sha = (info.get("mergeCommit") or {}).get("oid") or ""
    if not merge_sha:
        raise RollbackError(f"PR #{number} 머지 커밋 없음")
    linked = [
        ref.get("number") for ref in info.get("closingIssuesReferences", []) if ref.get("number")
    ]
    branch = f"revert/pr-{number}"
    real_base = info.get("baseRefName") or base
    steps = [
        f"git fetch origin {real_base}",
        f"git checkout -b {branch} origin/{real_base}",
        f"git revert -m 1 {merge_sha} --no-edit",
        f"git push -u origin {branch}",
        f"gh pr create --title 'Revert #{number}' --base {real_base} --head {branch}",
    ]
    for issue in linked:
        steps.append(f"gh issue reopen {issue} + 원인 코멘트")
    return RollbackPlan(
        pr_number=number,
        pr_title=info.get("title", ""),
        pr_url=info.get("url", ""),
        merge_sha=merge_sha,
        base=real_base,
        head=info.get("headRefName", ""),
        branch=branch,
        linked_issues=linked,
        steps=steps,
    )


def execute_rollback(
    plan: RollbackPlan, workspace: str | Path, config: RollbackConfig | None = None
) -> RollbackResult:
    """계획 실행 (dry_run이면 명령 없이 계획만 반환)"""
    cfg = config or RollbackConfig()
    ws = Path(workspace)
    result = RollbackResult(pr_number=plan.pr_number, dry_run=cfg.dry_run, plan=plan)
    if cfg.dry_run:
        result.success = True
        return result
    if not working_tree_clean(ws):
        result.error = "작업 트리가 깨끗하지 않음 (커밋/스태시 후 재시도)"
        return result
    try:
        seq: list[list[str]] = [
            ["git", "fetch", cfg.remote, plan.base],
            ["git", "checkout", "-b", plan.branch, f"{cfg.remote}/{plan.base}"],
            ["git", "revert", "-m", "1", plan.merge_sha, "--no-edit"],
            ["git", "push", "-u", cfg.remote, plan.branch],
        ]
        for cmd in seq:
            _run_checked(cmd, ws)
        out = _run_checked(
            [
                "gh",
                "pr",
                "create",
                "--title",
                f"Revert #{plan.pr_number}: {plan.pr_title}",
                "--body",
                f"오머지 롤백 (원본 PR #{plan.pr_number} revert).\n\n{plan.pr_url}",
                "--base",
                plan.base,
                "--head",
                plan.branch,
            ],
            ws,
        )
        url = out.strip().splitlines()[-1] if out.strip() else ""
        result.revert_pr_url = url or None
        if "/pull/" in url:
            with suppress(ValueError):
                result.revert_pr_number = int(url.split("/pull/")[-1].strip("/"))
        if cfg.reopen_issue:
            for issue in plan.linked_issues:
                r1 = _run(["gh", "issue", "reopen", str(issue)], ws)
                _run(
                    [
                        "gh",
                        "issue",
                        "comment",
                        str(issue),
                        "--body",
                        f"🔄 오머지 롤백됨 (PR #{plan.pr_number}). "
                        f"revert PR: {url or '(생성됨)'}",
                    ],
                    ws,
                )
                if r1.returncode == 0:
                    result.reopened_issues.append(issue)
        result.success = True
        log.info("PR #%d 롤백 완료 → %s", plan.pr_number, url)
    except RollbackError as e:
        result.error = str(e)
        log.error("롤백 실패: %s", e)
    if cfg.notify_telegram:
        status = "✅" if result.success else "❌"
        send_telegram(
            f"{status} 롤백 PR #{plan.pr_number}: "
            f"{'revert PR ' + (result.revert_pr_url or '') if result.success else result.error}"
        )
    return result


def rollback_pr(
    number: int, workspace: str | Path, config: RollbackConfig | None = None
) -> RollbackResult:
    """계획+실행 일괄 (Day 4 진입점)"""
    cfg = config or RollbackConfig()
    try:
        plan = plan_rollback(number, workspace, base=cfg.base)
    except RollbackError as e:
        return RollbackResult(pr_number=number, dry_run=cfg.dry_run, error=str(e))
    return execute_rollback(plan, workspace, cfg)


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(description="오머지 롤백 (revert PR + 이슈 재오픈)")
    ap.add_argument("pr", type=int, help="머지된 PR 번호")
    ap.add_argument("--workspace", default=".", help="git/gh 작업 디렉토리")
    ap.add_argument("--base", default="main")
    ap.add_argument("--dry-run", action="store_true", help="계획만 출력, 변경 없음")
    ap.add_argument("--no-reopen", action="store_true", help="이슈 재오픈 생략")
    ap.add_argument("--quiet", action="store_true", help="텔레그램 알림 생략")
    args = ap.parse_args(argv)

    cfg = RollbackConfig(
        dry_run=args.dry_run,
        base=args.base,
        reopen_issue=not args.no_reopen,
        notify_telegram=not args.quiet,
    )
    result = rollback_pr(args.pr, args.workspace, cfg)
    if result.plan:
        print(f"PR #{result.pr_number}: {result.plan.pr_title}")
        print(f"머지 커밋: {result.plan.merge_sha} / 브랜치: {result.plan.branch}")
        print(f"연결 이슈: {result.plan.linked_issues or '없음'}")
        print("단계:")
        for s in result.plan.steps:
            print(f"  - {s}")
    if cfg.dry_run:
        print("dry-run: 변경 없음")
        if not result.success:
            print(f"사유: {result.error}")
        return 0 if result.success else 1
    if result.success:
        print(f"revert PR: {result.revert_pr_url}")
        print(f"재오픈 이슈: {result.reopened_issues or '없음'}")
        return 0
    print(f"실패: {result.error}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
