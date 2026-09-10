"""
완전 자동화 파이프라인 (Autopilot)
- GitHub Issue → 파싱 → 계획/구현(Agent) → 품질 게이트 → PR → 자동 리뷰 → 머지
- 무인 운영 안전장치: dry-run, 라벨 필터, 이슈당 1회, 게이트/리뷰 차단 시 머지 금지
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .agent import AutonomousCodingAgent
from .git_integration import GitWorkflow
from .github import GitHubIssue, get_github_client
from .issue_parser import IssueParser
from .notify import send_telegram
from .pr_reviewer import PRReviewer
from .quality_gate import GateConfig, check_paths

log = logging.getLogger("autonomous_coding_agent.autopilot")

# 무인 처리 제외 라벨 (사람 손 필요)
DEFAULT_SKIP_LABELS = frozenset({"needs-human", "blocked", "wontfix", "duplicate", "question"})


@dataclass
class AutopilotConfig:
    """무인 운영 설정"""

    only_labels: list[str] = field(default_factory=list)  # 비어 있으면 전체 대상
    skip_labels: set[str] = field(default_factory=lambda: set(DEFAULT_SKIP_LABELS))
    max_issues: int = 5  # 1회 실행당 최대 처리 이슈 수
    dry_run: bool = False  # True면 계획까지만, 실제 변경/PR/머지 없음
    require_gate_pass: bool = True  # 게이트 차단 시 PR/머지 금지
    require_review_pass: bool = True  # 리뷰 critical/error 시 머지 금지
    merge_method: str = "squash"
    delete_branch: bool = True
    base_branch: str = "main"
    max_iterations: int = 6  # 4단계 계획 + 재시도 여유
    notify_telegram: bool = True  # 차단/실패/머지 시 텔레그램 알림
    gate_config: GateConfig = field(default_factory=GateConfig)

    def to_dict(self) -> dict[str, Any]:
        return {
            "only_labels": self.only_labels,
            "skip_labels": sorted(self.skip_labels),
            "max_issues": self.max_issues,
            "dry_run": self.dry_run,
            "require_gate_pass": self.require_gate_pass,
            "require_review_pass": self.require_review_pass,
            "merge_method": self.merge_method,
            "delete_branch": self.delete_branch,
            "base_branch": self.base_branch,
            "max_iterations": self.max_iterations,
            "notify_telegram": self.notify_telegram,
        }


@dataclass
class IssueRunResult:
    issue_number: int
    stage: str = "fetched"  # …/planned/implemented/gated/pr_opened/reviewed/merged/skipped/failed
    pr_number: int | None = None
    pr_url: str | None = None
    merged: bool = False
    gate_summary: str = ""
    review_summary: str = ""
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "issue_number": self.issue_number,
            "stage": self.stage,
            "pr_number": self.pr_number,
            "pr_url": self.pr_url,
            "merged": self.merged,
            "gate_summary": self.gate_summary,
            "review_summary": self.review_summary,
            "error": self.error,
        }


@dataclass
class AutopilotResult:
    runs: list[IssueRunResult] = field(default_factory=list)

    @property
    def merged(self) -> list[int]:
        return [r.issue_number for r in self.runs if r.merged]

    @property
    def failed(self) -> list[int]:
        return [r.issue_number for r in self.runs if r.stage == "failed"]

    @property
    def skipped(self) -> list[int]:
        return [r.issue_number for r in self.runs if r.stage == "skipped"]

    def to_dict(self) -> dict[str, Any]:
        return {
            "runs": [r.to_dict() for r in self.runs],
            "merged": self.merged,
            "failed": self.failed,
            "skipped": self.skipped,
        }


class Autopilot:
    """Issue → Merge 무인 파이프라인"""

    def __init__(
        self,
        workspace: str | Path,
        config: AutopilotConfig | None = None,
        dashboard: Any | None = None,
    ):
        self.workspace = Path(workspace).resolve()
        self.config = config or AutopilotConfig()
        self.dashboard = dashboard
        self.github = get_github_client(self.workspace)
        self.workflow = GitWorkflow(self.workspace)
        self.parser = IssueParser()
        self.reviewer = PRReviewer(self.workspace)

    # -- 조회/판정 (테스트 용이성을 위해 분리) --
    def should_process(self, issue: GitHubIssue) -> tuple[bool, str]:
        """이슈 처리 여부 판정"""
        if issue.state.lower() != "open":
            return False, f"state={issue.state}"
        if set(issue.labels) & self.config.skip_labels:
            hit = sorted(set(issue.labels) & self.config.skip_labels)
            return False, f"skip label: {hit}"
        if self.config.only_labels and not (set(issue.labels) & set(self.config.only_labels)):
            return False, f"only_labels={self.config.only_labels} 불일치"
        return True, "ok"

    def build_goal(self, issue: GitHubIssue) -> str:
        """이슈 → 에이전트 목표 문장"""
        analysis = self.parser.parse_issue(issue.number, issue.title, issue.body)
        lines = [f"GitHub 이슈 #{issue.number}: {issue.title}", "", analysis.summary]
        if analysis.parsed_tasks:
            lines.append("\n작업 항목:")
            for t in analysis.parsed_tasks:
                lines.append(f"- [{t.task_type.value}] {t.title}: {t.description}")
        if analysis.suggested_files:
            lines.append(f"\n관련 파일 후보: {', '.join(analysis.suggested_files)}")
        criteria = [c for t in analysis.parsed_tasks for c in t.acceptance_criteria]
        if criteria:
            lines.append("\n수용 기준:")
            for c in criteria:
                lines.append(f"- {c}")
        return "\n".join(lines).strip()

    def _make_agent(self, workspace: Path | None = None) -> AutonomousCodingAgent:
        return AutonomousCodingAgent(
            workspace=workspace or self.workspace,
            max_iterations=self.config.max_iterations,
            hitl_on_failure=False,  # 무인: 사람 개입 없이 실패 반환
        )

    def _make_workflow(self, workspace: str | Path) -> GitWorkflow:
        """worktree용 워크플로우 (테스트에서 스텁 교체 가능)"""
        return GitWorkflow(Path(workspace))

    def _notify(self, message: str) -> None:
        """텔레그램 알림 (설정 꺼져 있으면 무음, 실패해도 본류 무영향)"""
        if self.config.notify_telegram:
            send_telegram(message)

    def _report_dashboard(self, result: IssueRunResult) -> None:
        """대시보드 현황 보고 (없으면 무시, 실패해도 본류 무영향)"""
        dashboard = getattr(self, "dashboard", None)
        if dashboard is None:
            return
        try:
            dashboard.report_autopilot(result.to_dict())
        except Exception as e:
            log.warning("dashboard report failed: %s", e)

    # -- 단일 이슈 처리 --
    def run_issue(self, number: int) -> IssueRunResult:
        result = IssueRunResult(issue_number=number)
        try:
            issue = self.github.get_issue(number)
            if not issue:
                result.stage = "failed"
                result.error = f"이슈 #{number} 조회 실패"
                return result
            ok, reason = self.should_process(issue)
            if not ok:
                result.stage = "skipped"
                result.error = reason
                log.info("이슈 #%d 스킵: %s", number, reason)
                return result

            goal = self.build_goal(issue)
            result.stage = "planned"
            log.info("이슈 #%d 계획 완료: %s", number, issue.title)
            if self.config.dry_run:
                result.gate_summary = "dry-run: 계획까지만 수행"
                return result

            # 1) 격리 worktree (현재 체크아웃을 건드리지 않음 — E2E 교훈)
            try:
                branch, wt = self.workflow.create_worktree(
                    number, issue.title, base=self.config.base_branch
                )
            except RuntimeError as e:
                result.stage = "failed"
                result.error = f"worktree 생성 실패: {e}"
                return result
            wt_flow = self._make_workflow(wt)

            # 2) 구현
            agent = self._make_agent(wt)
            agent_result = agent.run(goal)
            if not agent_result.success:
                result.stage = "failed"
                result.error = agent_result.error or "에이전트 구현 실패"
                self.github.add_comment(number, f"🤖 자동 처리 실패: {result.error}")
                self._notify(f"🤖 Autopilot #{number} 구현 실패: {result.error}")
                return result
            result.stage = "implemented"

            # 3) 품질 게이트 (변경된 .py 파일)
            changed = [f for f in (agent_result.files_changed or []) if f.endswith(".py")]
            gate_results = (
                check_paths(
                    [wt / f for f in changed],
                    config=self.config.gate_config,
                )
                if changed
                else []
            )
            blocks = [g for g in gate_results if g.blocked]
            warns = sum(len(g.warnings()) for g in gate_results)
            result.gate_summary = f"{len(gate_results)}개 파일: 차단 {len(blocks)}, 경고 {warns}"
            result.stage = "gated"
            # 커밋+푸시는 게이트 전 수행 (흔적 보존)
            wt_flow.commit_changes(f"fix: resolve issue #{number}\n\n{issue.title}")
            wt_flow.push_branch(branch)
            if blocks and self.config.require_gate_pass:
                detail = "; ".join(b.summary() for b in blocks[:3])
                self.github.add_comment(number, f"🛑 품질 게이트 차단:\n{detail}")
                result.stage = "failed"
                result.error = f"게이트 차단: {detail}"
                self._notify(f"🛑 Autopilot #{number} 게이트 차단: {detail}")
                return result

            # 4) PR 생성
            pr_number = wt_flow.create_pr_from_issue(number, branch, base=self.config.base_branch)
            if not pr_number:
                result.stage = "failed"
                result.error = "PR 생성 실패"
                self._notify(f"🤖 Autopilot #{number} PR 생성 실패")
                return result
            result.pr_number = pr_number
            result.stage = "pr_opened"
            pr = self.github.get_pr(pr_number)
            result.pr_url = pr.url if pr else None

            # 5) 자동 리뷰
            repo_info = self.github.get_repo_info()
            if repo_info:
                repo = f"{repo_info['owner']['login']}/{repo_info['name']}"
                review = self.reviewer.review_pr(
                    pr_number, repo, base_branch=self.config.base_branch
                )
                result.review_summary = (
                    f"critical {review.critical_count}, "
                    f"error {review.error_count}, warning {review.warning_count}"
                )
                result.stage = "reviewed"
                if (
                    review.critical_count or review.error_count
                ) and self.config.require_review_pass:
                    self.github.add_comment(
                        number,
                        f"🔍 자동 리뷰 차단 (PR #{pr_number}): {result.review_summary}",
                    )
                    result.stage = "failed"
                    result.error = f"리뷰 차단: {result.review_summary}"
                    self._notify(
                        f"🔍 Autopilot #{number} 리뷰 차단 "
                        f"(PR #{pr_number}): {result.review_summary}"
                    )
                    return result
            else:
                result.review_summary = "repo 정보 없음: 리뷰 생략"

            # 6) 머지
            merged = self.github.merge_pr(
                pr_number,
                method=self.config.merge_method,
                delete_branch=self.config.delete_branch,
            )
            if not merged:
                result.stage = "failed"
                result.error = f"PR #{pr_number} 머지 실패"
                self._notify(f"🤖 Autopilot #{number} 머지 실패 (PR #{pr_number})")
                return result
            result.merged = True
            result.stage = "merged"
            self.github.add_comment(number, f"✅ 자동 머지 완료: PR #{pr_number}")
            self._notify(f"✅ Autopilot #{number} 자동 머지 완료 (PR #{pr_number})")
            log.info("이슈 #%d 자동 머지 완료 (PR #%d)", number, pr_number)
            if self.config.delete_branch:
                self.workflow.remove_worktree(wt)
            return result
        except Exception as e:
            log.error("이슈 #%d 처리 중 예외: %s", number, e)
            result.stage = "failed"
            result.error = str(e)
            self._notify(f"🤖 Autopilot #{number} 예외: {e}")
            return result

    # -- 일괄 실행 --
    def run_once(self) -> AutopilotResult:
        """열린 이슈 목록 → 최대 max_issues개 처리"""
        out = AutopilotResult()
        issues = self.github.list_issues(
            state="open", labels=self.config.only_labels or None, limit=50
        )
        count = 0
        for issue in issues:
            if count >= self.config.max_issues:
                break
            res = self.run_issue(issue.number)
            out.runs.append(res)
            self._report_dashboard(res)
            if res.stage != "skipped":
                count += 1
        log.info(
            "Autopilot 1회 실행: %d건 처리 (머지 %d, 실패 %d, 스킵 %d)",
            len(out.runs),
            len(out.merged),
            len(out.failed),
            len(out.skipped),
        )
        return out


def create_autopilot(workspace: str | Path, config: AutopilotConfig | None = None) -> Autopilot:
    return Autopilot(workspace, config)
