"""
GitHub 연동 모듈 - Issue/PR 자동화
"""

from __future__ import annotations

import json
import logging
import os
import subprocess
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

log = logging.getLogger("autonomous_coding_agent.github")


@dataclass
class GitHubIssue:
    """GitHub Issue"""
    number: int
    title: str
    body: str
    state: str
    labels: list[str]
    assignees: list[str]
    created_at: str
    updated_at: str
    url: str


@dataclass
class GitHubPR:
    """GitHub Pull Request"""
    number: int
    title: str
    body: str
    state: str
    head_branch: str
    base_branch: str
    draft: bool
    created_at: str
    updated_at: str
    url: str
    head_sha: str
    base_sha: str
    additions: int
    deletions: int
    changed_files: int


class GitHubClient:
    """GitHub CLI (gh) 래퍼"""

    def __init__(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self._check_gh_cli()

    def _check_gh_cli(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def _run(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def _run_json(self, cmd: str) -> dict | None:
        """JSON 출력 명령 실행"""
        # 명령에 이미 --json이 있는지 확인
        if "--json" not in cmd:
            cmd = cmd + " --json"
        result = self._run(cmd)
        if result.returncode != 0:
            log.error(f"GitHub CLI 실패: {result.stderr}")
            return None
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as e:
            log.error(f"JSON 파싱 실패: {e}, stdout: {result.stdout[:200]}")
            return None

    # === Issue 관련 ===

    def get_issue(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url")
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    def list_issues(self, state: str = "open", labels: list[str] | None = None, limit: int = 20) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += " --label " + " --label ".join(labels)
        cmd += " --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"

        data = self._run_json(cmd)
        if not data:
            return []

        return [
            GitHubIssue(
                number=d["number"],
                title=d["title"],
                body=d.get("body", ""),
                state=d["state"],
                labels=[l["name"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def create_issue(self, title: str, body: str, labels: list[str] | None = None, assignees: list[str] | None = None) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += " --assignee " + " --assignee ".join(assignees)

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0:
            log.error(f"이슈 생성 실패: {result.stderr}")
            return None

        # URL에서 번호 추출
        url = result.stdout.strip()
        if "/issues/" in url:
            return int(url.split("/issues/")[-1])
        return None

    def close_issue(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def add_comment(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    # === PR 관련 ===

    def create_pr(self, title: str, body: str, head: str, base: str = "main", draft: bool = False) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0:
            log.error(f"PR 생성 실패: {result.stderr}")
            return None

        url = result.stdout.strip()
        if "/pull/" in url:
            return int(url.split("/pull/")[-1])
        return None

    def get_pr(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            head_branch=data.get("headRefName", ""),
            base_branch=data.get("baseRefName", ""),
            draft=data.get("isDraft", False),
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def list_prs(self, state: str = "open", base: str | None = None, limit: int = 20) -> list[GitHubPR]:
        """PR 목록 조회"""
        cmd = f"gh pr list --state {state} --limit {limit} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        if base:
            cmd += f" --base {base}"

        data = self._run_json(cmd)
        if not data:
            return []

        return [
            GitHubPR(
                number=d["number"],
                title=d["title"],
                body=d.get("body", ""),
                state=d["state"],
                head_branch=d.get("headRefName", ""),
                base_branch=d.get("baseRefName", ""),
                draft=d.get("isDraft", False),
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
                head_sha="",
                base_sha="",
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def merge_pr(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def add_review_comment(self, number: int, body: str, path: str, line: int, side: str = "RIGHT") -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f'gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -',
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    # === 리포지토리 ===

    def get_repo_info(self) -> dict | None:
        """저장소 정보"""
        return self._run_json("gh repo view --json name,owner,description,url,defaultBranchRef")

    def get_file_content(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0:
            return None
        try:
            data = json.loads(result.stdout)
            import base64
            return base64.b64decode(data["content"]).decode("utf-8")
        except Exception:
            return None


def get_github_client(workspace: Path) -> GitHubClient:
    """GitHub 클라이언트 생성 헬퍼"""
    return GitHubClient(workspace)
