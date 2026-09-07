"""
Git + GitHub 통합 모듈 - 에이전트 워크플로우 자동화
"""

from __future__ import annotations

import logging
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional
from dataclasses import dataclass

from .git import GitManager, get_git_manager, GitStatus, CommitInfo
from .github import GitHubClient, get_github_client, GitHubIssue, GitHubPR

log = logging.getLogger("autonomous_coding_agent.git_integration")


@dataclass
class WorkflowResult:
    """워크플로우 실행 결과"""
    success: bool
    branch: str
    commits: List[str]
    pr_number: Optional[int]
    pr_url: Optional[str]
    message: str


class GitWorkflow:
    """Git + GitHub 워크플로우 자동화"""
    
    def __init__(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.git = get_git_manager(workspace)
        self.github = get_github_client(workspace)
    
    def get_status(self) -> Dict[str, Any]:
        """현재 상태 종합"""
        git_status = self.git.get_status()
        
        return {
            "branch": git_status.branch,
            "is_clean": git_status.is_clean,
            "staged": git_status.staged_files,
            "unstaged": git_status.unstaged_files,
            "untracked": git_status.untracked_files,
            "ahead": git_status.ahead,
            "behind": git_status.behind,
        }
    
    def create_feature_branch(self, issue_number: int, issue_title: str) -> str:
        """이슈 기반 기능 브랜치 생성"""
        # 안전한 브랜치 이름 생성
        safe_title = "".join(c if c.isalnum() or c in "-_" else "-" for c in issue_title.lower())
        safe_title = safe_title[:50].strip("-")
        branch_name = f"issue-{issue_number}-{safe_title}"
        
        # 현재 브랜치가 main/master인지 확인
        current_status = self.git.get_status()
        base_branch = "main"
        
        # main/master 확인
        branches_result = subprocess.run(
            "git branch -a",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
        )
        if "master" in branches_result.stdout and "main" not in branches_result.stdout:
            base_branch = "master"
        
        # 브랜치 생성
        self.git.create_branch(branch_name, base_branch)
        log.info(f"브랜치 생성: {branch_name} (base: {base_branch})")
        
        return branch_name
    
    def commit_changes(self, message: str, files: Optional[List[str]] = None) -> Optional[str]:
        """변경사항 커밋"""
        return self.git.commit(message, files)
    
    def push_branch(self, branch: Optional[str] = None) -> bool:
        """브랜치 푸시"""
        return self.git.push(branch)
    
    def create_pr_from_issue(self, issue_number: int, branch: str, base: str = "main") -> Optional[int]:
        """이슈 기반 PR 생성"""
        # 이슈 정보 가져오기
        issue = self.github.get_issue(issue_number)
        if not issue:
            log.error(f"이슈를 찾을 수 없음: #{issue_number}")
            return None
        
        # PR 제목/본문 생성
        title = f"Fix #{issue_number}: {issue.title}"
        body = f"""## Summary
이 PR은 이슈 #{issue_number}을 해결합니다.

## Issue
{issue.body or "(본문 없음)"}

## Changes
- 관련 변경사항은 커밋 로그를 참고하세요.

## Testing
- 관련 테스트 통과 확인 필요

Closes #{issue_number}"""
        
        # PR 생성
        pr_number = self.github.create_pr(
            title=f"Fix #{issue_number}: {issue.title}",
            body=body,
            head=branch,
            base="main",
        )
        
        if pr_number:
            log.info(f"PR 생성 완료: #{pr_number}")
            # 이슈에 자동 코멘트
            self.github.add_comment(issue_number, f"관련 PR: #{pr_number}")
        
        return pr_number
    
    def run_full_workflow(self, issue_number: int, changes: List[Dict[str, Any]]) -> WorkflowResult:
        """전체 워크플로우 실행: 브랜치 생성 -> 변경 -> 커밋 -> 푸시 -> PR 생성"""
        try:
            # 1. 이슈 정보 가져오기
            issue = self.github.get_issue(issue_number)
            if not issue:
                return WorkflowResult(
                    success=False,
                    branch="",
                    commits=[],
                    pr_number=None,
                    pr_url=None,
                    message=f"이슈 #{issue_number}를 찾을 수 없음",
                )
            
            # 2. 브랜치 생성
            branch = self.create_feature_branch(issue_number, issue.title)
            
            # 2. 변경사항 적용 (변경사항은 외부에서 적용됨)
            # 이 함수는 변경사항이 이미 적용되었다고 가정
            
            # 3. 변경사항 커밋
            commit_msg = f"fix: resolve issue #{issue_number}\n\n{changes[0].get('description', '') if changes else ''}"
            commit_hash = self.git.commit(f"fix: resolve issue #{issue_number}")
            
            commits = [commit_hash] if commit_hash else []
            
            # 4. 푸시
            self.push_branch()
            
            # 5. PR 생성
            pr_number = self.create_pr_from_issue(issue_number, self.git.get_status().branch)
            
            pr_url = None
            if pr_number:
                repo_info = self.github.get_repo_info()
                if repo_info:
                    pr_url = f"https://github.com/{repo_info['owner']['login']}/{repo_info['name']}/pull/{pr_number}"
            
            return WorkflowResult(
                success=True,
                branch=self.git.get_status().branch,
                commits=commits,
                pr_number=pr_number,
                pr_url=pr_url,
                message=f"이슈 #{issue_number} 해결을 위한 PR 생성 완료",
            )
            
        except Exception as e:
            log.error(f"워크플로우 실행 실패: {e}")
            return WorkflowResult(
                success=False,
                branch="",
                commits=[],
                pr_number=None,
                pr_url=None,
                message=f"워크플로우 실패: {e}",
            )


def get_git_workflow(workspace: Path) -> "GitWorkflow":
    """Git 워크플로우 헬퍼"""
    return GitWorkflow(workspace)