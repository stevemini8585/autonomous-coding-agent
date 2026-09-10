"""
Git 통합 모듈 - 브랜치, 커밋, PR 자동화
"""

from __future__ import annotations

import logging
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

log = logging.getLogger("autonomous_coding_agent.git")


@dataclass
class GitStatus:
    """Git 상태 정보"""

    branch: str
    is_clean: bool
    staged_files: list[str]
    unstaged_files: list[str]
    untracked_files: list[str]
    ahead: int
    behind: int


@dataclass
class CommitInfo:
    """커밋 정보"""

    hash: str
    short_hash: str
    message: str
    author: str
    date: str
    files_changed: list[str]


class GitManager:
    """Git 작업 관리자"""

    def __init__(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        if not (self.workspace / ".git").exists():
            raise ValueError(f"Git 저장소가 아님: {workspace}")

    def _run(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def get_status(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run("git branch --show-current")
        branch = branch_result.stdout.strip()

        # 상태
        status_result = self._run("git status --porcelain")
        lines = status_result.stdout.strip().split("\n") if status_result.stdout.strip() else []

        staged = []
        unstaged = []
        untracked = []

        for line in lines:
            if not line:
                continue
            status = line[:2]
            filepath = line[3:]
            if status[0] in ("M", "A", "D", "R", "C"):
                staged.append(filepath)
            if status[1] in ("M", "D"):
                unstaged.append(filepath)
            if status == "??":
                untracked.append(filepath)

        # ahead/behind
        ahead_behind = self._run(
            "git rev-list --left-right --count @{u}...HEAD 2>/dev/null || echo '0\t0'"
        )
        behind, ahead = map(int, ahead_behind.stdout.strip().split("\t"))

        return GitStatus(
            branch=branch,
            is_clean=len(lines) == 0,
            staged_files=staged,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def add(self, files: list[str]) -> bool:
        """파일 스테이징"""
        if not files:
            return True
        result = self._run(f"git add {' '.join(files)}")
        return result.returncode == 0

    def commit(self, message: str, files: list[str] | None = None) -> str | None:
        """커밋 생성"""
        if files:
            self.add(files)
        else:
            # 전체 변경사항 스테이징 및 커밋
            result = self._run("git add -A")
            if result.returncode != 0:
                return None

        result = self._run(f'git commit -m "{message}"')
        if result.returncode != 0:
            return None

        # 커밋 해시 반환
        hash_result = self._run("git rev-parse HEAD")
        return str(hash_result.stdout).strip()

    def create_branch(self, branch_name: str, base: str | None = None) -> str:
        """브랜치 생성"""
        cmd = f"git checkout -b {branch_name}"
        if base:
            cmd = f"git checkout -b {branch_name} {base}"
        result = self._run(cmd)
        if result.returncode != 0:
            raise RuntimeError(f"브랜치 생성 실패: {result.stderr}")
        return branch_name

    def push(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = "git push"
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd += " --force"
        result = self._run(cmd)
        return result.returncode == 0

    def get_diff(self, staged: bool = False) -> str:
        """변경사항 diff"""
        cmd = "git diff"
        if staged:
            cmd += " --cached"
        result = self._run(cmd)
        return str(result.stdout)

    def get_log(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.split("|", 3)
            if len(parts) == 4:
                commits.append(
                    CommitInfo(
                        hash=parts[0],
                        short_hash=parts[0],
                        message=parts[1],
                        author=parts[2],
                        date=parts[3],
                        files_changed=[],
                    )
                )
        return commits

    def get_file_diff(self, filepath: str, staged: bool = False) -> str:
        """특정 파일 diff"""
        cmd = f"git diff {'--cached ' if staged else ''}{filepath}"
        result = self._run(cmd)
        return str(result.stdout)


def get_git_manager(workspace: Path) -> GitManager:
    """Git 매니저 생성 헬퍼"""
    return GitManager(workspace)
