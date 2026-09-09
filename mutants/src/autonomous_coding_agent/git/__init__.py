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


from mutmut.mutation.trampoline import MutantDict
from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated


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


mutants_xǁGitManagerǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitManagerǁ_run__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitManagerǁget_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitManagerǁadd__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitManagerǁcommit__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitManagerǁcreate_branch__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitManagerǁpush__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitManagerǁget_diff__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitManagerǁget_log__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitManagerǁget_file_diff__mutmut: MutantDict = {}  # type: ignore


class GitManager:
    """Git 작업 관리자"""

    @_mutmut_mutated(mutants_xǁGitManagerǁ__init____mutmut)
    def __init__(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        if not (self.workspace / ".git").exists():
            raise ValueError(f"Git 저장소가 아님: {workspace}")

    def xǁGitManagerǁ__init____mutmut_orig(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        if not (self.workspace / ".git").exists():
            raise ValueError(f"Git 저장소가 아님: {workspace}")

    def xǁGitManagerǁ__init____mutmut_1(self, workspace: Path):
        self.workspace = None
        if not (self.workspace / ".git").exists():
            raise ValueError(f"Git 저장소가 아님: {workspace}")

    def xǁGitManagerǁ__init____mutmut_2(self, workspace: Path):
        self.workspace = Path(None).resolve()
        if not (self.workspace / ".git").exists():
            raise ValueError(f"Git 저장소가 아님: {workspace}")

    def xǁGitManagerǁ__init____mutmut_3(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        if (self.workspace / ".git").exists():
            raise ValueError(f"Git 저장소가 아님: {workspace}")

    def xǁGitManagerǁ__init____mutmut_4(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        if not (self.workspace * ".git").exists():
            raise ValueError(f"Git 저장소가 아님: {workspace}")

    def xǁGitManagerǁ__init____mutmut_5(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        if not (self.workspace / "XX.gitXX").exists():
            raise ValueError(f"Git 저장소가 아님: {workspace}")

    def xǁGitManagerǁ__init____mutmut_6(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        if not (self.workspace / ".GIT").exists():
            raise ValueError(f"Git 저장소가 아님: {workspace}")

    def xǁGitManagerǁ__init____mutmut_7(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        if not (self.workspace / ".git").exists():
            raise ValueError(None)

    @_mutmut_mutated(mutants_xǁGitManagerǁ_run__mutmut)
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

    def xǁGitManagerǁ_run__mutmut_orig(self, cmd: str) -> subprocess.CompletedProcess:
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

    def xǁGitManagerǁ_run__mutmut_1(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(None)
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitManagerǁ_run__mutmut_2(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            None,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitManagerǁ_run__mutmut_3(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=None,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitManagerǁ_run__mutmut_4(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=None,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitManagerǁ_run__mutmut_5(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=None,
            text=True,
            timeout=60,
        )

    def xǁGitManagerǁ_run__mutmut_6(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=None,
            timeout=60,
        )

    def xǁGitManagerǁ_run__mutmut_7(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=None,
        )

    def xǁGitManagerǁ_run__mutmut_8(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitManagerǁ_run__mutmut_9(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitManagerǁ_run__mutmut_10(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitManagerǁ_run__mutmut_11(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            text=True,
            timeout=60,
        )

    def xǁGitManagerǁ_run__mutmut_12(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            timeout=60,
        )

    def xǁGitManagerǁ_run__mutmut_13(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
        )

    def xǁGitManagerǁ_run__mutmut_14(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=False,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitManagerǁ_run__mutmut_15(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=False,
            text=True,
            timeout=60,
        )

    def xǁGitManagerǁ_run__mutmut_16(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=False,
            timeout=60,
        )

    def xǁGitManagerǁ_run__mutmut_17(self, cmd: str) -> subprocess.CompletedProcess:
        """Git 명령 실행"""
        log.info(f"Git 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=61,
        )

    @_mutmut_mutated(mutants_xǁGitManagerǁget_status__mutmut)
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

    def xǁGitManagerǁget_status__mutmut_orig(self) -> GitStatus:
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

    def xǁGitManagerǁget_status__mutmut_1(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = None
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

    def xǁGitManagerǁget_status__mutmut_2(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run(None)
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

    def xǁGitManagerǁget_status__mutmut_3(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run("XXgit branch --show-currentXX")
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

    def xǁGitManagerǁget_status__mutmut_4(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run("GIT BRANCH --SHOW-CURRENT")
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

    def xǁGitManagerǁget_status__mutmut_5(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run("git branch --show-current")
        branch = None

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

    def xǁGitManagerǁget_status__mutmut_6(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run("git branch --show-current")
        branch = branch_result.stdout.strip()

        # 상태
        status_result = None
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

    def xǁGitManagerǁget_status__mutmut_7(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run("git branch --show-current")
        branch = branch_result.stdout.strip()

        # 상태
        status_result = self._run(None)
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

    def xǁGitManagerǁget_status__mutmut_8(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run("git branch --show-current")
        branch = branch_result.stdout.strip()

        # 상태
        status_result = self._run("XXgit status --porcelainXX")
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

    def xǁGitManagerǁget_status__mutmut_9(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run("git branch --show-current")
        branch = branch_result.stdout.strip()

        # 상태
        status_result = self._run("GIT STATUS --PORCELAIN")
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

    def xǁGitManagerǁget_status__mutmut_10(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run("git branch --show-current")
        branch = branch_result.stdout.strip()

        # 상태
        status_result = self._run("git status --porcelain")
        lines = None

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

    def xǁGitManagerǁget_status__mutmut_11(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run("git branch --show-current")
        branch = branch_result.stdout.strip()

        # 상태
        status_result = self._run("git status --porcelain")
        lines = status_result.stdout.strip().split(None) if status_result.stdout.strip() else []

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

    def xǁGitManagerǁget_status__mutmut_12(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run("git branch --show-current")
        branch = branch_result.stdout.strip()

        # 상태
        status_result = self._run("git status --porcelain")
        lines = status_result.stdout.strip().split("XX\nXX") if status_result.stdout.strip() else []

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

    def xǁGitManagerǁget_status__mutmut_13(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run("git branch --show-current")
        branch = branch_result.stdout.strip()

        # 상태
        status_result = self._run("git status --porcelain")
        lines = status_result.stdout.strip().split("\n") if status_result.stdout.strip() else []

        staged = None
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

    def xǁGitManagerǁget_status__mutmut_14(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run("git branch --show-current")
        branch = branch_result.stdout.strip()

        # 상태
        status_result = self._run("git status --porcelain")
        lines = status_result.stdout.strip().split("\n") if status_result.stdout.strip() else []

        staged = []
        unstaged = None
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

    def xǁGitManagerǁget_status__mutmut_15(self) -> GitStatus:
        """작업 트리 상태 조회"""
        # 현재 브랜치
        branch_result = self._run("git branch --show-current")
        branch = branch_result.stdout.strip()

        # 상태
        status_result = self._run("git status --porcelain")
        lines = status_result.stdout.strip().split("\n") if status_result.stdout.strip() else []

        staged = []
        unstaged = []
        untracked = None

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

    def xǁGitManagerǁget_status__mutmut_16(self) -> GitStatus:
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
            if line:
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

    def xǁGitManagerǁget_status__mutmut_17(self) -> GitStatus:
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
                break
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

    def xǁGitManagerǁget_status__mutmut_18(self) -> GitStatus:
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
            status = None
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

    def xǁGitManagerǁget_status__mutmut_19(self) -> GitStatus:
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
            status = line[:3]
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

    def xǁGitManagerǁget_status__mutmut_20(self) -> GitStatus:
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
            filepath = None
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

    def xǁGitManagerǁget_status__mutmut_21(self) -> GitStatus:
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
            filepath = line[4:]
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

    def xǁGitManagerǁget_status__mutmut_22(self) -> GitStatus:
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
            if status[1] in ("M", "A", "D", "R", "C"):
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

    def xǁGitManagerǁget_status__mutmut_23(self) -> GitStatus:
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
            if status[0] not in ("M", "A", "D", "R", "C"):
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

    def xǁGitManagerǁget_status__mutmut_24(self) -> GitStatus:
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
            if status[0] in ("XXMXX", "A", "D", "R", "C"):
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

    def xǁGitManagerǁget_status__mutmut_25(self) -> GitStatus:
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
            if status[0] in ("m", "A", "D", "R", "C"):
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

    def xǁGitManagerǁget_status__mutmut_26(self) -> GitStatus:
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
            if status[0] in ("M", "XXAXX", "D", "R", "C"):
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

    def xǁGitManagerǁget_status__mutmut_27(self) -> GitStatus:
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
            if status[0] in ("M", "a", "D", "R", "C"):
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

    def xǁGitManagerǁget_status__mutmut_28(self) -> GitStatus:
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
            if status[0] in ("M", "A", "XXDXX", "R", "C"):
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

    def xǁGitManagerǁget_status__mutmut_29(self) -> GitStatus:
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
            if status[0] in ("M", "A", "d", "R", "C"):
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

    def xǁGitManagerǁget_status__mutmut_30(self) -> GitStatus:
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
            if status[0] in ("M", "A", "D", "XXRXX", "C"):
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

    def xǁGitManagerǁget_status__mutmut_31(self) -> GitStatus:
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
            if status[0] in ("M", "A", "D", "r", "C"):
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

    def xǁGitManagerǁget_status__mutmut_32(self) -> GitStatus:
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
            if status[0] in ("M", "A", "D", "R", "XXCXX"):
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

    def xǁGitManagerǁget_status__mutmut_33(self) -> GitStatus:
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
            if status[0] in ("M", "A", "D", "R", "c"):
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

    def xǁGitManagerǁget_status__mutmut_34(self) -> GitStatus:
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
                staged.append(None)
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

    def xǁGitManagerǁget_status__mutmut_35(self) -> GitStatus:
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
            if status[2] in ("M", "D"):
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

    def xǁGitManagerǁget_status__mutmut_36(self) -> GitStatus:
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
            if status[1] not in ("M", "D"):
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

    def xǁGitManagerǁget_status__mutmut_37(self) -> GitStatus:
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
            if status[1] in ("XXMXX", "D"):
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

    def xǁGitManagerǁget_status__mutmut_38(self) -> GitStatus:
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
            if status[1] in ("m", "D"):
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

    def xǁGitManagerǁget_status__mutmut_39(self) -> GitStatus:
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
            if status[1] in ("M", "XXDXX"):
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

    def xǁGitManagerǁget_status__mutmut_40(self) -> GitStatus:
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
            if status[1] in ("M", "d"):
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

    def xǁGitManagerǁget_status__mutmut_41(self) -> GitStatus:
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
                unstaged.append(None)
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

    def xǁGitManagerǁget_status__mutmut_42(self) -> GitStatus:
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
            if status != "??":
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

    def xǁGitManagerǁget_status__mutmut_43(self) -> GitStatus:
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
            if status == "XX??XX":
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

    def xǁGitManagerǁget_status__mutmut_44(self) -> GitStatus:
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
                untracked.append(None)

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

    def xǁGitManagerǁget_status__mutmut_45(self) -> GitStatus:
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
        ahead_behind = None
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

    def xǁGitManagerǁget_status__mutmut_46(self) -> GitStatus:
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
        ahead_behind = self._run(None)
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

    def xǁGitManagerǁget_status__mutmut_47(self) -> GitStatus:
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
            "XXgit rev-list --left-right --count @{u}...HEAD 2>/dev/null || echo '0\t0'XX"
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

    def xǁGitManagerǁget_status__mutmut_48(self) -> GitStatus:
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
            "git rev-list --left-right --count @{u}...head 2>/dev/null || echo '0\t0'"
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

    def xǁGitManagerǁget_status__mutmut_49(self) -> GitStatus:
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
            "GIT REV-LIST --LEFT-RIGHT --COUNT @{U}...HEAD 2>/DEV/NULL || ECHO '0\t0'"
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

    def xǁGitManagerǁget_status__mutmut_50(self) -> GitStatus:
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
        behind, ahead = None

        return GitStatus(
            branch=branch,
            is_clean=len(lines) == 0,
            staged_files=staged,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_51(self) -> GitStatus:
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
        behind, ahead = map(None, ahead_behind.stdout.strip().split("\t"))

        return GitStatus(
            branch=branch,
            is_clean=len(lines) == 0,
            staged_files=staged,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_52(self) -> GitStatus:
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
        behind, ahead = map(int, None)

        return GitStatus(
            branch=branch,
            is_clean=len(lines) == 0,
            staged_files=staged,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_53(self) -> GitStatus:
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
        behind, ahead = map(ahead_behind.stdout.strip().split("\t"))

        return GitStatus(
            branch=branch,
            is_clean=len(lines) == 0,
            staged_files=staged,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_54(self) -> GitStatus:
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
        behind, ahead = map(
            int,
        )

        return GitStatus(
            branch=branch,
            is_clean=len(lines) == 0,
            staged_files=staged,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_55(self) -> GitStatus:
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
        behind, ahead = map(int, ahead_behind.stdout.strip().split(None))

        return GitStatus(
            branch=branch,
            is_clean=len(lines) == 0,
            staged_files=staged,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_56(self) -> GitStatus:
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
        behind, ahead = map(int, ahead_behind.stdout.strip().split("XX\tXX"))

        return GitStatus(
            branch=branch,
            is_clean=len(lines) == 0,
            staged_files=staged,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_57(self) -> GitStatus:
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
            branch=None,
            is_clean=len(lines) == 0,
            staged_files=staged,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_58(self) -> GitStatus:
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
            is_clean=None,
            staged_files=staged,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_59(self) -> GitStatus:
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
            staged_files=None,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_60(self) -> GitStatus:
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
            unstaged_files=None,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_61(self) -> GitStatus:
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
            untracked_files=None,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_62(self) -> GitStatus:
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
            ahead=None,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_63(self) -> GitStatus:
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
            behind=None,
        )

    def xǁGitManagerǁget_status__mutmut_64(self) -> GitStatus:
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
            is_clean=len(lines) == 0,
            staged_files=staged,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_65(self) -> GitStatus:
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
            staged_files=staged,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_66(self) -> GitStatus:
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
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_67(self) -> GitStatus:
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
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_68(self) -> GitStatus:
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
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_69(self) -> GitStatus:
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
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_70(self) -> GitStatus:
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
        )

    def xǁGitManagerǁget_status__mutmut_71(self) -> GitStatus:
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
            is_clean=len(lines) != 0,
            staged_files=staged,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    def xǁGitManagerǁget_status__mutmut_72(self) -> GitStatus:
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
            is_clean=len(lines) == 1,
            staged_files=staged,
            unstaged_files=unstaged,
            untracked_files=untracked,
            ahead=ahead,
            behind=behind,
        )

    @_mutmut_mutated(mutants_xǁGitManagerǁadd__mutmut)
    def add(self, files: list[str]) -> bool:
        """파일 스테이징"""
        if not files:
            return True
        result = self._run(f"git add {' '.join(files)}")
        return result.returncode == 0

    def xǁGitManagerǁadd__mutmut_orig(self, files: list[str]) -> bool:
        """파일 스테이징"""
        if not files:
            return True
        result = self._run(f"git add {' '.join(files)}")
        return result.returncode == 0

    def xǁGitManagerǁadd__mutmut_1(self, files: list[str]) -> bool:
        """파일 스테이징"""
        if files:
            return True
        result = self._run(f"git add {' '.join(files)}")
        return result.returncode == 0

    def xǁGitManagerǁadd__mutmut_2(self, files: list[str]) -> bool:
        """파일 스테이징"""
        if not files:
            return False
        result = self._run(f"git add {' '.join(files)}")
        return result.returncode == 0

    def xǁGitManagerǁadd__mutmut_3(self, files: list[str]) -> bool:
        """파일 스테이징"""
        if not files:
            return True
        result = None
        return result.returncode == 0

    def xǁGitManagerǁadd__mutmut_4(self, files: list[str]) -> bool:
        """파일 스테이징"""
        if not files:
            return True
        result = self._run(None)
        return result.returncode == 0

    def xǁGitManagerǁadd__mutmut_5(self, files: list[str]) -> bool:
        """파일 스테이징"""
        if not files:
            return True
        result = self._run(f"git add {' '.join(None)}")
        return result.returncode == 0

    def xǁGitManagerǁadd__mutmut_6(self, files: list[str]) -> bool:
        """파일 스테이징"""
        if not files:
            return True
        result = self._run(f"git add {'XX XX'.join(files)}")
        return result.returncode == 0

    def xǁGitManagerǁadd__mutmut_7(self, files: list[str]) -> bool:
        """파일 스테이징"""
        if not files:
            return True
        result = self._run(f"git add {' '.join(files)}")
        return result.returncode != 0

    def xǁGitManagerǁadd__mutmut_8(self, files: list[str]) -> bool:
        """파일 스테이징"""
        if not files:
            return True
        result = self._run(f"git add {' '.join(files)}")
        return result.returncode == 1

    @_mutmut_mutated(mutants_xǁGitManagerǁcommit__mutmut)
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
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_orig(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
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
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_1(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
        """커밋 생성"""
        if files:
            self.add(None)
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
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_2(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
        """커밋 생성"""
        if files:
            self.add(files)
        else:
            # 전체 변경사항 스테이징 및 커밋
            result = None
            if result.returncode != 0:
                return None

        result = self._run(f'git commit -m "{message}"')
        if result.returncode != 0:
            return None

        # 커밋 해시 반환
        hash_result = self._run("git rev-parse HEAD")
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_3(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
        """커밋 생성"""
        if files:
            self.add(files)
        else:
            # 전체 변경사항 스테이징 및 커밋
            result = self._run(None)
            if result.returncode != 0:
                return None

        result = self._run(f'git commit -m "{message}"')
        if result.returncode != 0:
            return None

        # 커밋 해시 반환
        hash_result = self._run("git rev-parse HEAD")
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_4(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
        """커밋 생성"""
        if files:
            self.add(files)
        else:
            # 전체 변경사항 스테이징 및 커밋
            result = self._run("XXgit add -AXX")
            if result.returncode != 0:
                return None

        result = self._run(f'git commit -m "{message}"')
        if result.returncode != 0:
            return None

        # 커밋 해시 반환
        hash_result = self._run("git rev-parse HEAD")
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_5(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
        """커밋 생성"""
        if files:
            self.add(files)
        else:
            # 전체 변경사항 스테이징 및 커밋
            result = self._run("git add -a")
            if result.returncode != 0:
                return None

        result = self._run(f'git commit -m "{message}"')
        if result.returncode != 0:
            return None

        # 커밋 해시 반환
        hash_result = self._run("git rev-parse HEAD")
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_6(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
        """커밋 생성"""
        if files:
            self.add(files)
        else:
            # 전체 변경사항 스테이징 및 커밋
            result = self._run("GIT ADD -A")
            if result.returncode != 0:
                return None

        result = self._run(f'git commit -m "{message}"')
        if result.returncode != 0:
            return None

        # 커밋 해시 반환
        hash_result = self._run("git rev-parse HEAD")
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_7(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
        """커밋 생성"""
        if files:
            self.add(files)
        else:
            # 전체 변경사항 스테이징 및 커밋
            result = self._run("git add -A")
            if result.returncode == 0:
                return None

        result = self._run(f'git commit -m "{message}"')
        if result.returncode != 0:
            return None

        # 커밋 해시 반환
        hash_result = self._run("git rev-parse HEAD")
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_8(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
        """커밋 생성"""
        if files:
            self.add(files)
        else:
            # 전체 변경사항 스테이징 및 커밋
            result = self._run("git add -A")
            if result.returncode != 1:
                return None

        result = self._run(f'git commit -m "{message}"')
        if result.returncode != 0:
            return None

        # 커밋 해시 반환
        hash_result = self._run("git rev-parse HEAD")
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_9(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
        """커밋 생성"""
        if files:
            self.add(files)
        else:
            # 전체 변경사항 스테이징 및 커밋
            result = self._run("git add -A")
            if result.returncode != 0:
                return None

        result = None
        if result.returncode != 0:
            return None

        # 커밋 해시 반환
        hash_result = self._run("git rev-parse HEAD")
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_10(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
        """커밋 생성"""
        if files:
            self.add(files)
        else:
            # 전체 변경사항 스테이징 및 커밋
            result = self._run("git add -A")
            if result.returncode != 0:
                return None

        result = self._run(None)
        if result.returncode != 0:
            return None

        # 커밋 해시 반환
        hash_result = self._run("git rev-parse HEAD")
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_11(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
        """커밋 생성"""
        if files:
            self.add(files)
        else:
            # 전체 변경사항 스테이징 및 커밋
            result = self._run("git add -A")
            if result.returncode != 0:
                return None

        result = self._run(f'git commit -m "{message}"')
        if result.returncode == 0:
            return None

        # 커밋 해시 반환
        hash_result = self._run("git rev-parse HEAD")
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_12(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
        """커밋 생성"""
        if files:
            self.add(files)
        else:
            # 전체 변경사항 스테이징 및 커밋
            result = self._run("git add -A")
            if result.returncode != 0:
                return None

        result = self._run(f'git commit -m "{message}"')
        if result.returncode != 1:
            return None

        # 커밋 해시 반환
        hash_result = self._run("git rev-parse HEAD")
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_13(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
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
        hash_result = None
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_14(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
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
        hash_result = self._run(None)
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_15(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
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
        hash_result = self._run("XXgit rev-parse HEADXX")
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_16(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
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
        hash_result = self._run("git rev-parse head")
        return hash_result.stdout.strip()

    def xǁGitManagerǁcommit__mutmut_17(
        self, message: str, files: list[str] | None = None
    ) -> str | None:
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
        hash_result = self._run("GIT REV-PARSE HEAD")
        return hash_result.stdout.strip()

    @_mutmut_mutated(mutants_xǁGitManagerǁcreate_branch__mutmut)
    def create_branch(self, branch_name: str, base: str | None = None) -> str:
        """브랜치 생성"""
        cmd = f"git checkout -b {branch_name}"
        if base:
            cmd = f"git checkout -b {branch_name} {base}"
        result = self._run(cmd)
        if result.returncode != 0:
            raise RuntimeError(f"브랜치 생성 실패: {result.stderr}")
        return branch_name

    def xǁGitManagerǁcreate_branch__mutmut_orig(
        self, branch_name: str, base: str | None = None
    ) -> str:
        """브랜치 생성"""
        cmd = f"git checkout -b {branch_name}"
        if base:
            cmd = f"git checkout -b {branch_name} {base}"
        result = self._run(cmd)
        if result.returncode != 0:
            raise RuntimeError(f"브랜치 생성 실패: {result.stderr}")
        return branch_name

    def xǁGitManagerǁcreate_branch__mutmut_1(
        self, branch_name: str, base: str | None = None
    ) -> str:
        """브랜치 생성"""
        cmd = None
        if base:
            cmd = f"git checkout -b {branch_name} {base}"
        result = self._run(cmd)
        if result.returncode != 0:
            raise RuntimeError(f"브랜치 생성 실패: {result.stderr}")
        return branch_name

    def xǁGitManagerǁcreate_branch__mutmut_2(
        self, branch_name: str, base: str | None = None
    ) -> str:
        """브랜치 생성"""
        cmd = f"git checkout -b {branch_name}"
        if base:
            cmd = None
        result = self._run(cmd)
        if result.returncode != 0:
            raise RuntimeError(f"브랜치 생성 실패: {result.stderr}")
        return branch_name

    def xǁGitManagerǁcreate_branch__mutmut_3(
        self, branch_name: str, base: str | None = None
    ) -> str:
        """브랜치 생성"""
        cmd = f"git checkout -b {branch_name}"
        if base:
            cmd = f"git checkout -b {branch_name} {base}"
        result = None
        if result.returncode != 0:
            raise RuntimeError(f"브랜치 생성 실패: {result.stderr}")
        return branch_name

    def xǁGitManagerǁcreate_branch__mutmut_4(
        self, branch_name: str, base: str | None = None
    ) -> str:
        """브랜치 생성"""
        cmd = f"git checkout -b {branch_name}"
        if base:
            cmd = f"git checkout -b {branch_name} {base}"
        result = self._run(None)
        if result.returncode != 0:
            raise RuntimeError(f"브랜치 생성 실패: {result.stderr}")
        return branch_name

    def xǁGitManagerǁcreate_branch__mutmut_5(
        self, branch_name: str, base: str | None = None
    ) -> str:
        """브랜치 생성"""
        cmd = f"git checkout -b {branch_name}"
        if base:
            cmd = f"git checkout -b {branch_name} {base}"
        result = self._run(cmd)
        if result.returncode == 0:
            raise RuntimeError(f"브랜치 생성 실패: {result.stderr}")
        return branch_name

    def xǁGitManagerǁcreate_branch__mutmut_6(
        self, branch_name: str, base: str | None = None
    ) -> str:
        """브랜치 생성"""
        cmd = f"git checkout -b {branch_name}"
        if base:
            cmd = f"git checkout -b {branch_name} {base}"
        result = self._run(cmd)
        if result.returncode != 1:
            raise RuntimeError(f"브랜치 생성 실패: {result.stderr}")
        return branch_name

    def xǁGitManagerǁcreate_branch__mutmut_7(
        self, branch_name: str, base: str | None = None
    ) -> str:
        """브랜치 생성"""
        cmd = f"git checkout -b {branch_name}"
        if base:
            cmd = f"git checkout -b {branch_name} {base}"
        result = self._run(cmd)
        if result.returncode != 0:
            raise RuntimeError(None)
        return branch_name

    @_mutmut_mutated(mutants_xǁGitManagerǁpush__mutmut)
    def push(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = "git push"
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd += " --force"
        result = self._run(cmd)
        return result.returncode == 0

    def xǁGitManagerǁpush__mutmut_orig(
        self, branch: str | None = None, force: bool = False
    ) -> bool:
        """푸시"""
        cmd = "git push"
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd += " --force"
        result = self._run(cmd)
        return result.returncode == 0

    def xǁGitManagerǁpush__mutmut_1(self, branch: str | None = None, force: bool = True) -> bool:
        """푸시"""
        cmd = "git push"
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd += " --force"
        result = self._run(cmd)
        return result.returncode == 0

    def xǁGitManagerǁpush__mutmut_2(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = None
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd += " --force"
        result = self._run(cmd)
        return result.returncode == 0

    def xǁGitManagerǁpush__mutmut_3(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = "XXgit pushXX"
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd += " --force"
        result = self._run(cmd)
        return result.returncode == 0

    def xǁGitManagerǁpush__mutmut_4(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = "GIT PUSH"
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd += " --force"
        result = self._run(cmd)
        return result.returncode == 0

    def xǁGitManagerǁpush__mutmut_5(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = "git push"
        if branch:
            cmd = f" origin {branch}"
        if force:
            cmd += " --force"
        result = self._run(cmd)
        return result.returncode == 0

    def xǁGitManagerǁpush__mutmut_6(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = "git push"
        if branch:
            cmd -= f" origin {branch}"
        if force:
            cmd += " --force"
        result = self._run(cmd)
        return result.returncode == 0

    def xǁGitManagerǁpush__mutmut_7(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = "git push"
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd = " --force"
        result = self._run(cmd)
        return result.returncode == 0

    def xǁGitManagerǁpush__mutmut_8(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = "git push"
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd -= " --force"
        result = self._run(cmd)
        return result.returncode == 0

    def xǁGitManagerǁpush__mutmut_9(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = "git push"
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd += "XX --forceXX"
        result = self._run(cmd)
        return result.returncode == 0

    def xǁGitManagerǁpush__mutmut_10(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = "git push"
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd += " --FORCE"
        result = self._run(cmd)
        return result.returncode == 0

    def xǁGitManagerǁpush__mutmut_11(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = "git push"
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd += " --force"
        result = None
        return result.returncode == 0

    def xǁGitManagerǁpush__mutmut_12(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = "git push"
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd += " --force"
        result = self._run(None)
        return result.returncode == 0

    def xǁGitManagerǁpush__mutmut_13(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = "git push"
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd += " --force"
        result = self._run(cmd)
        return result.returncode != 0

    def xǁGitManagerǁpush__mutmut_14(self, branch: str | None = None, force: bool = False) -> bool:
        """푸시"""
        cmd = "git push"
        if branch:
            cmd += f" origin {branch}"
        if force:
            cmd += " --force"
        result = self._run(cmd)
        return result.returncode == 1

    @_mutmut_mutated(mutants_xǁGitManagerǁget_diff__mutmut)
    def get_diff(self, staged: bool = False) -> str:
        """변경사항 diff"""
        cmd = "git diff"
        if staged:
            cmd += " --cached"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_diff__mutmut_orig(self, staged: bool = False) -> str:
        """변경사항 diff"""
        cmd = "git diff"
        if staged:
            cmd += " --cached"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_diff__mutmut_1(self, staged: bool = True) -> str:
        """변경사항 diff"""
        cmd = "git diff"
        if staged:
            cmd += " --cached"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_diff__mutmut_2(self, staged: bool = False) -> str:
        """변경사항 diff"""
        cmd = None
        if staged:
            cmd += " --cached"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_diff__mutmut_3(self, staged: bool = False) -> str:
        """변경사항 diff"""
        cmd = "XXgit diffXX"
        if staged:
            cmd += " --cached"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_diff__mutmut_4(self, staged: bool = False) -> str:
        """변경사항 diff"""
        cmd = "GIT DIFF"
        if staged:
            cmd += " --cached"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_diff__mutmut_5(self, staged: bool = False) -> str:
        """변경사항 diff"""
        cmd = "git diff"
        if staged:
            cmd = " --cached"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_diff__mutmut_6(self, staged: bool = False) -> str:
        """변경사항 diff"""
        cmd = "git diff"
        if staged:
            cmd -= " --cached"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_diff__mutmut_7(self, staged: bool = False) -> str:
        """변경사항 diff"""
        cmd = "git diff"
        if staged:
            cmd += "XX --cachedXX"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_diff__mutmut_8(self, staged: bool = False) -> str:
        """변경사항 diff"""
        cmd = "git diff"
        if staged:
            cmd += " --CACHED"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_diff__mutmut_9(self, staged: bool = False) -> str:
        """변경사항 diff"""
        cmd = "git diff"
        if staged:
            cmd += " --cached"
        result = None
        return result.stdout

    def xǁGitManagerǁget_diff__mutmut_10(self, staged: bool = False) -> str:
        """변경사항 diff"""
        cmd = "git diff"
        if staged:
            cmd += " --cached"
        result = self._run(None)
        return result.stdout

    @_mutmut_mutated(mutants_xǁGitManagerǁget_log__mutmut)
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

    def xǁGitManagerǁget_log__mutmut_orig(self, limit: int = 10) -> list[CommitInfo]:
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

    def xǁGitManagerǁget_log__mutmut_1(self, limit: int = 11) -> list[CommitInfo]:
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

    def xǁGitManagerǁget_log__mutmut_2(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = None
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

    def xǁGitManagerǁget_log__mutmut_3(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(None)
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

    def xǁGitManagerǁget_log__mutmut_4(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = None
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

    def xǁGitManagerǁget_log__mutmut_5(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split(None):
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

    def xǁGitManagerǁget_log__mutmut_6(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split("XX\nXX"):
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

    def xǁGitManagerǁget_log__mutmut_7(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if line:
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

    def xǁGitManagerǁget_log__mutmut_8(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                break
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

    def xǁGitManagerǁget_log__mutmut_9(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            parts = None
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

    def xǁGitManagerǁget_log__mutmut_10(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.split(None, 3)
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

    def xǁGitManagerǁget_log__mutmut_11(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.split("|", None)
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

    def xǁGitManagerǁget_log__mutmut_12(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.split(3)
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

    def xǁGitManagerǁget_log__mutmut_13(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.split(
                "|",
            )
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

    def xǁGitManagerǁget_log__mutmut_14(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.rsplit("|", 3)
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

    def xǁGitManagerǁget_log__mutmut_15(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.split("XX|XX", 3)
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

    def xǁGitManagerǁget_log__mutmut_16(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.split("|", 4)
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

    def xǁGitManagerǁget_log__mutmut_17(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.split("|", 3)
            if len(parts) != 4:
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

    def xǁGitManagerǁget_log__mutmut_18(self, limit: int = 10) -> list[CommitInfo]:
        """커밋 로그"""
        result = self._run(
            f"git log --oneline -{limit} --pretty=format:'%h|%s|%an|%ad' --date=short"
        )
        commits = []
        for line in result.stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.split("|", 3)
            if len(parts) == 5:
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

    def xǁGitManagerǁget_log__mutmut_19(self, limit: int = 10) -> list[CommitInfo]:
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
                commits.append(None)
        return commits

    def xǁGitManagerǁget_log__mutmut_20(self, limit: int = 10) -> list[CommitInfo]:
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
                        hash=None,
                        short_hash=parts[0],
                        message=parts[1],
                        author=parts[2],
                        date=parts[3],
                        files_changed=[],
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_21(self, limit: int = 10) -> list[CommitInfo]:
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
                        short_hash=None,
                        message=parts[1],
                        author=parts[2],
                        date=parts[3],
                        files_changed=[],
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_22(self, limit: int = 10) -> list[CommitInfo]:
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
                        message=None,
                        author=parts[2],
                        date=parts[3],
                        files_changed=[],
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_23(self, limit: int = 10) -> list[CommitInfo]:
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
                        author=None,
                        date=parts[3],
                        files_changed=[],
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_24(self, limit: int = 10) -> list[CommitInfo]:
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
                        date=None,
                        files_changed=[],
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_25(self, limit: int = 10) -> list[CommitInfo]:
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
                        files_changed=None,
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_26(self, limit: int = 10) -> list[CommitInfo]:
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
                        short_hash=parts[0],
                        message=parts[1],
                        author=parts[2],
                        date=parts[3],
                        files_changed=[],
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_27(self, limit: int = 10) -> list[CommitInfo]:
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
                        message=parts[1],
                        author=parts[2],
                        date=parts[3],
                        files_changed=[],
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_28(self, limit: int = 10) -> list[CommitInfo]:
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
                        author=parts[2],
                        date=parts[3],
                        files_changed=[],
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_29(self, limit: int = 10) -> list[CommitInfo]:
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
                        date=parts[3],
                        files_changed=[],
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_30(self, limit: int = 10) -> list[CommitInfo]:
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
                        files_changed=[],
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_31(self, limit: int = 10) -> list[CommitInfo]:
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
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_32(self, limit: int = 10) -> list[CommitInfo]:
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
                        hash=parts[1],
                        short_hash=parts[0],
                        message=parts[1],
                        author=parts[2],
                        date=parts[3],
                        files_changed=[],
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_33(self, limit: int = 10) -> list[CommitInfo]:
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
                        short_hash=parts[1],
                        message=parts[1],
                        author=parts[2],
                        date=parts[3],
                        files_changed=[],
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_34(self, limit: int = 10) -> list[CommitInfo]:
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
                        message=parts[2],
                        author=parts[2],
                        date=parts[3],
                        files_changed=[],
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_35(self, limit: int = 10) -> list[CommitInfo]:
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
                        author=parts[3],
                        date=parts[3],
                        files_changed=[],
                    )
                )
        return commits

    def xǁGitManagerǁget_log__mutmut_36(self, limit: int = 10) -> list[CommitInfo]:
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
                        date=parts[4],
                        files_changed=[],
                    )
                )
        return commits

    @_mutmut_mutated(mutants_xǁGitManagerǁget_file_diff__mutmut)
    def get_file_diff(self, filepath: str, staged: bool = False) -> str:
        """특정 파일 diff"""
        cmd = f"git diff {'--cached ' if staged else ''}{filepath}"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_file_diff__mutmut_orig(self, filepath: str, staged: bool = False) -> str:
        """특정 파일 diff"""
        cmd = f"git diff {'--cached ' if staged else ''}{filepath}"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_file_diff__mutmut_1(self, filepath: str, staged: bool = True) -> str:
        """특정 파일 diff"""
        cmd = f"git diff {'--cached ' if staged else ''}{filepath}"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_file_diff__mutmut_2(self, filepath: str, staged: bool = False) -> str:
        """특정 파일 diff"""
        cmd = None
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_file_diff__mutmut_3(self, filepath: str, staged: bool = False) -> str:
        """특정 파일 diff"""
        cmd = f"git diff {'XX--cached XX' if staged else ''}{filepath}"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_file_diff__mutmut_4(self, filepath: str, staged: bool = False) -> str:
        """특정 파일 diff"""
        cmd = f"git diff {'--CACHED ' if staged else ''}{filepath}"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_file_diff__mutmut_5(self, filepath: str, staged: bool = False) -> str:
        """특정 파일 diff"""
        cmd = f"git diff {'--cached ' if staged else 'XXXX'}{filepath}"
        result = self._run(cmd)
        return result.stdout

    def xǁGitManagerǁget_file_diff__mutmut_6(self, filepath: str, staged: bool = False) -> str:
        """특정 파일 diff"""
        cmd = f"git diff {'--cached ' if staged else ''}{filepath}"
        result = None
        return result.stdout

    def xǁGitManagerǁget_file_diff__mutmut_7(self, filepath: str, staged: bool = False) -> str:
        """특정 파일 diff"""
        cmd = f"git diff {'--cached ' if staged else ''}{filepath}"
        result = self._run(None)
        return result.stdout


mutants_xǁGitManagerǁ__init____mutmut["_mutmut_orig"] = GitManager.xǁGitManagerǁ__init____mutmut_orig  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ__init____mutmut["xǁGitManagerǁ__init____mutmut_1"] = GitManager.xǁGitManagerǁ__init____mutmut_1  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ__init____mutmut["xǁGitManagerǁ__init____mutmut_2"] = GitManager.xǁGitManagerǁ__init____mutmut_2  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ__init____mutmut["xǁGitManagerǁ__init____mutmut_3"] = GitManager.xǁGitManagerǁ__init____mutmut_3  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ__init____mutmut["xǁGitManagerǁ__init____mutmut_4"] = GitManager.xǁGitManagerǁ__init____mutmut_4  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ__init____mutmut["xǁGitManagerǁ__init____mutmut_5"] = GitManager.xǁGitManagerǁ__init____mutmut_5  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ__init____mutmut["xǁGitManagerǁ__init____mutmut_6"] = GitManager.xǁGitManagerǁ__init____mutmut_6  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ__init____mutmut["xǁGitManagerǁ__init____mutmut_7"] = GitManager.xǁGitManagerǁ__init____mutmut_7  # type: ignore # mutmut generated

mutants_xǁGitManagerǁ_run__mutmut["_mutmut_orig"] = GitManager.xǁGitManagerǁ_run__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_1"] = GitManager.xǁGitManagerǁ_run__mutmut_1  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_2"] = GitManager.xǁGitManagerǁ_run__mutmut_2  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_3"] = GitManager.xǁGitManagerǁ_run__mutmut_3  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_4"] = GitManager.xǁGitManagerǁ_run__mutmut_4  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_5"] = GitManager.xǁGitManagerǁ_run__mutmut_5  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_6"] = GitManager.xǁGitManagerǁ_run__mutmut_6  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_7"] = GitManager.xǁGitManagerǁ_run__mutmut_7  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_8"] = GitManager.xǁGitManagerǁ_run__mutmut_8  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_9"] = GitManager.xǁGitManagerǁ_run__mutmut_9  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_10"] = GitManager.xǁGitManagerǁ_run__mutmut_10  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_11"] = GitManager.xǁGitManagerǁ_run__mutmut_11  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_12"] = GitManager.xǁGitManagerǁ_run__mutmut_12  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_13"] = GitManager.xǁGitManagerǁ_run__mutmut_13  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_14"] = GitManager.xǁGitManagerǁ_run__mutmut_14  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_15"] = GitManager.xǁGitManagerǁ_run__mutmut_15  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_16"] = GitManager.xǁGitManagerǁ_run__mutmut_16  # type: ignore # mutmut generated
mutants_xǁGitManagerǁ_run__mutmut["xǁGitManagerǁ_run__mutmut_17"] = GitManager.xǁGitManagerǁ_run__mutmut_17  # type: ignore # mutmut generated

mutants_xǁGitManagerǁget_status__mutmut["_mutmut_orig"] = GitManager.xǁGitManagerǁget_status__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_1"] = GitManager.xǁGitManagerǁget_status__mutmut_1  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_2"] = GitManager.xǁGitManagerǁget_status__mutmut_2  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_3"] = GitManager.xǁGitManagerǁget_status__mutmut_3  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_4"] = GitManager.xǁGitManagerǁget_status__mutmut_4  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_5"] = GitManager.xǁGitManagerǁget_status__mutmut_5  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_6"] = GitManager.xǁGitManagerǁget_status__mutmut_6  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_7"] = GitManager.xǁGitManagerǁget_status__mutmut_7  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_8"] = GitManager.xǁGitManagerǁget_status__mutmut_8  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_9"] = GitManager.xǁGitManagerǁget_status__mutmut_9  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_10"] = GitManager.xǁGitManagerǁget_status__mutmut_10  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_11"] = GitManager.xǁGitManagerǁget_status__mutmut_11  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_12"] = GitManager.xǁGitManagerǁget_status__mutmut_12  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_13"] = GitManager.xǁGitManagerǁget_status__mutmut_13  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_14"] = GitManager.xǁGitManagerǁget_status__mutmut_14  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_15"] = GitManager.xǁGitManagerǁget_status__mutmut_15  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_16"] = GitManager.xǁGitManagerǁget_status__mutmut_16  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_17"] = GitManager.xǁGitManagerǁget_status__mutmut_17  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_18"] = GitManager.xǁGitManagerǁget_status__mutmut_18  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_19"] = GitManager.xǁGitManagerǁget_status__mutmut_19  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_20"] = GitManager.xǁGitManagerǁget_status__mutmut_20  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_21"] = GitManager.xǁGitManagerǁget_status__mutmut_21  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_22"] = GitManager.xǁGitManagerǁget_status__mutmut_22  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_23"] = GitManager.xǁGitManagerǁget_status__mutmut_23  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_24"] = GitManager.xǁGitManagerǁget_status__mutmut_24  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_25"] = GitManager.xǁGitManagerǁget_status__mutmut_25  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_26"] = GitManager.xǁGitManagerǁget_status__mutmut_26  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_27"] = GitManager.xǁGitManagerǁget_status__mutmut_27  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_28"] = GitManager.xǁGitManagerǁget_status__mutmut_28  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_29"] = GitManager.xǁGitManagerǁget_status__mutmut_29  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_30"] = GitManager.xǁGitManagerǁget_status__mutmut_30  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_31"] = GitManager.xǁGitManagerǁget_status__mutmut_31  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_32"] = GitManager.xǁGitManagerǁget_status__mutmut_32  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_33"] = GitManager.xǁGitManagerǁget_status__mutmut_33  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_34"] = GitManager.xǁGitManagerǁget_status__mutmut_34  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_35"] = GitManager.xǁGitManagerǁget_status__mutmut_35  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_36"] = GitManager.xǁGitManagerǁget_status__mutmut_36  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_37"] = GitManager.xǁGitManagerǁget_status__mutmut_37  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_38"] = GitManager.xǁGitManagerǁget_status__mutmut_38  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_39"] = GitManager.xǁGitManagerǁget_status__mutmut_39  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_40"] = GitManager.xǁGitManagerǁget_status__mutmut_40  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_41"] = GitManager.xǁGitManagerǁget_status__mutmut_41  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_42"] = GitManager.xǁGitManagerǁget_status__mutmut_42  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_43"] = GitManager.xǁGitManagerǁget_status__mutmut_43  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_44"] = GitManager.xǁGitManagerǁget_status__mutmut_44  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_45"] = GitManager.xǁGitManagerǁget_status__mutmut_45  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_46"] = GitManager.xǁGitManagerǁget_status__mutmut_46  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_47"] = GitManager.xǁGitManagerǁget_status__mutmut_47  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_48"] = GitManager.xǁGitManagerǁget_status__mutmut_48  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_49"] = GitManager.xǁGitManagerǁget_status__mutmut_49  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_50"] = GitManager.xǁGitManagerǁget_status__mutmut_50  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_51"] = GitManager.xǁGitManagerǁget_status__mutmut_51  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_52"] = GitManager.xǁGitManagerǁget_status__mutmut_52  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_53"] = GitManager.xǁGitManagerǁget_status__mutmut_53  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_54"] = GitManager.xǁGitManagerǁget_status__mutmut_54  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_55"] = GitManager.xǁGitManagerǁget_status__mutmut_55  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_56"] = GitManager.xǁGitManagerǁget_status__mutmut_56  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_57"] = GitManager.xǁGitManagerǁget_status__mutmut_57  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_58"] = GitManager.xǁGitManagerǁget_status__mutmut_58  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_59"] = GitManager.xǁGitManagerǁget_status__mutmut_59  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_60"] = GitManager.xǁGitManagerǁget_status__mutmut_60  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_61"] = GitManager.xǁGitManagerǁget_status__mutmut_61  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_62"] = GitManager.xǁGitManagerǁget_status__mutmut_62  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_63"] = GitManager.xǁGitManagerǁget_status__mutmut_63  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_64"] = GitManager.xǁGitManagerǁget_status__mutmut_64  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_65"] = GitManager.xǁGitManagerǁget_status__mutmut_65  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_66"] = GitManager.xǁGitManagerǁget_status__mutmut_66  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_67"] = GitManager.xǁGitManagerǁget_status__mutmut_67  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_68"] = GitManager.xǁGitManagerǁget_status__mutmut_68  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_69"] = GitManager.xǁGitManagerǁget_status__mutmut_69  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_70"] = GitManager.xǁGitManagerǁget_status__mutmut_70  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_71"] = GitManager.xǁGitManagerǁget_status__mutmut_71  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_status__mutmut["xǁGitManagerǁget_status__mutmut_72"] = GitManager.xǁGitManagerǁget_status__mutmut_72  # type: ignore # mutmut generated

mutants_xǁGitManagerǁadd__mutmut["_mutmut_orig"] = GitManager.xǁGitManagerǁadd__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁGitManagerǁadd__mutmut["xǁGitManagerǁadd__mutmut_1"] = GitManager.xǁGitManagerǁadd__mutmut_1  # type: ignore # mutmut generated
mutants_xǁGitManagerǁadd__mutmut["xǁGitManagerǁadd__mutmut_2"] = GitManager.xǁGitManagerǁadd__mutmut_2  # type: ignore # mutmut generated
mutants_xǁGitManagerǁadd__mutmut["xǁGitManagerǁadd__mutmut_3"] = GitManager.xǁGitManagerǁadd__mutmut_3  # type: ignore # mutmut generated
mutants_xǁGitManagerǁadd__mutmut["xǁGitManagerǁadd__mutmut_4"] = GitManager.xǁGitManagerǁadd__mutmut_4  # type: ignore # mutmut generated
mutants_xǁGitManagerǁadd__mutmut["xǁGitManagerǁadd__mutmut_5"] = GitManager.xǁGitManagerǁadd__mutmut_5  # type: ignore # mutmut generated
mutants_xǁGitManagerǁadd__mutmut["xǁGitManagerǁadd__mutmut_6"] = GitManager.xǁGitManagerǁadd__mutmut_6  # type: ignore # mutmut generated
mutants_xǁGitManagerǁadd__mutmut["xǁGitManagerǁadd__mutmut_7"] = GitManager.xǁGitManagerǁadd__mutmut_7  # type: ignore # mutmut generated
mutants_xǁGitManagerǁadd__mutmut["xǁGitManagerǁadd__mutmut_8"] = GitManager.xǁGitManagerǁadd__mutmut_8  # type: ignore # mutmut generated

mutants_xǁGitManagerǁcommit__mutmut["_mutmut_orig"] = GitManager.xǁGitManagerǁcommit__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_1"] = GitManager.xǁGitManagerǁcommit__mutmut_1  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_2"] = GitManager.xǁGitManagerǁcommit__mutmut_2  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_3"] = GitManager.xǁGitManagerǁcommit__mutmut_3  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_4"] = GitManager.xǁGitManagerǁcommit__mutmut_4  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_5"] = GitManager.xǁGitManagerǁcommit__mutmut_5  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_6"] = GitManager.xǁGitManagerǁcommit__mutmut_6  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_7"] = GitManager.xǁGitManagerǁcommit__mutmut_7  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_8"] = GitManager.xǁGitManagerǁcommit__mutmut_8  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_9"] = GitManager.xǁGitManagerǁcommit__mutmut_9  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_10"] = GitManager.xǁGitManagerǁcommit__mutmut_10  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_11"] = GitManager.xǁGitManagerǁcommit__mutmut_11  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_12"] = GitManager.xǁGitManagerǁcommit__mutmut_12  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_13"] = GitManager.xǁGitManagerǁcommit__mutmut_13  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_14"] = GitManager.xǁGitManagerǁcommit__mutmut_14  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_15"] = GitManager.xǁGitManagerǁcommit__mutmut_15  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_16"] = GitManager.xǁGitManagerǁcommit__mutmut_16  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcommit__mutmut["xǁGitManagerǁcommit__mutmut_17"] = GitManager.xǁGitManagerǁcommit__mutmut_17  # type: ignore # mutmut generated

mutants_xǁGitManagerǁcreate_branch__mutmut["_mutmut_orig"] = GitManager.xǁGitManagerǁcreate_branch__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcreate_branch__mutmut["xǁGitManagerǁcreate_branch__mutmut_1"] = GitManager.xǁGitManagerǁcreate_branch__mutmut_1  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcreate_branch__mutmut["xǁGitManagerǁcreate_branch__mutmut_2"] = GitManager.xǁGitManagerǁcreate_branch__mutmut_2  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcreate_branch__mutmut["xǁGitManagerǁcreate_branch__mutmut_3"] = GitManager.xǁGitManagerǁcreate_branch__mutmut_3  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcreate_branch__mutmut["xǁGitManagerǁcreate_branch__mutmut_4"] = GitManager.xǁGitManagerǁcreate_branch__mutmut_4  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcreate_branch__mutmut["xǁGitManagerǁcreate_branch__mutmut_5"] = GitManager.xǁGitManagerǁcreate_branch__mutmut_5  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcreate_branch__mutmut["xǁGitManagerǁcreate_branch__mutmut_6"] = GitManager.xǁGitManagerǁcreate_branch__mutmut_6  # type: ignore # mutmut generated
mutants_xǁGitManagerǁcreate_branch__mutmut["xǁGitManagerǁcreate_branch__mutmut_7"] = GitManager.xǁGitManagerǁcreate_branch__mutmut_7  # type: ignore # mutmut generated

mutants_xǁGitManagerǁpush__mutmut["_mutmut_orig"] = GitManager.xǁGitManagerǁpush__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁGitManagerǁpush__mutmut["xǁGitManagerǁpush__mutmut_1"] = GitManager.xǁGitManagerǁpush__mutmut_1  # type: ignore # mutmut generated
mutants_xǁGitManagerǁpush__mutmut["xǁGitManagerǁpush__mutmut_2"] = GitManager.xǁGitManagerǁpush__mutmut_2  # type: ignore # mutmut generated
mutants_xǁGitManagerǁpush__mutmut["xǁGitManagerǁpush__mutmut_3"] = GitManager.xǁGitManagerǁpush__mutmut_3  # type: ignore # mutmut generated
mutants_xǁGitManagerǁpush__mutmut["xǁGitManagerǁpush__mutmut_4"] = GitManager.xǁGitManagerǁpush__mutmut_4  # type: ignore # mutmut generated
mutants_xǁGitManagerǁpush__mutmut["xǁGitManagerǁpush__mutmut_5"] = GitManager.xǁGitManagerǁpush__mutmut_5  # type: ignore # mutmut generated
mutants_xǁGitManagerǁpush__mutmut["xǁGitManagerǁpush__mutmut_6"] = GitManager.xǁGitManagerǁpush__mutmut_6  # type: ignore # mutmut generated
mutants_xǁGitManagerǁpush__mutmut["xǁGitManagerǁpush__mutmut_7"] = GitManager.xǁGitManagerǁpush__mutmut_7  # type: ignore # mutmut generated
mutants_xǁGitManagerǁpush__mutmut["xǁGitManagerǁpush__mutmut_8"] = GitManager.xǁGitManagerǁpush__mutmut_8  # type: ignore # mutmut generated
mutants_xǁGitManagerǁpush__mutmut["xǁGitManagerǁpush__mutmut_9"] = GitManager.xǁGitManagerǁpush__mutmut_9  # type: ignore # mutmut generated
mutants_xǁGitManagerǁpush__mutmut["xǁGitManagerǁpush__mutmut_10"] = GitManager.xǁGitManagerǁpush__mutmut_10  # type: ignore # mutmut generated
mutants_xǁGitManagerǁpush__mutmut["xǁGitManagerǁpush__mutmut_11"] = GitManager.xǁGitManagerǁpush__mutmut_11  # type: ignore # mutmut generated
mutants_xǁGitManagerǁpush__mutmut["xǁGitManagerǁpush__mutmut_12"] = GitManager.xǁGitManagerǁpush__mutmut_12  # type: ignore # mutmut generated
mutants_xǁGitManagerǁpush__mutmut["xǁGitManagerǁpush__mutmut_13"] = GitManager.xǁGitManagerǁpush__mutmut_13  # type: ignore # mutmut generated
mutants_xǁGitManagerǁpush__mutmut["xǁGitManagerǁpush__mutmut_14"] = GitManager.xǁGitManagerǁpush__mutmut_14  # type: ignore # mutmut generated

mutants_xǁGitManagerǁget_diff__mutmut["_mutmut_orig"] = GitManager.xǁGitManagerǁget_diff__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_diff__mutmut["xǁGitManagerǁget_diff__mutmut_1"] = GitManager.xǁGitManagerǁget_diff__mutmut_1  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_diff__mutmut["xǁGitManagerǁget_diff__mutmut_2"] = GitManager.xǁGitManagerǁget_diff__mutmut_2  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_diff__mutmut["xǁGitManagerǁget_diff__mutmut_3"] = GitManager.xǁGitManagerǁget_diff__mutmut_3  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_diff__mutmut["xǁGitManagerǁget_diff__mutmut_4"] = GitManager.xǁGitManagerǁget_diff__mutmut_4  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_diff__mutmut["xǁGitManagerǁget_diff__mutmut_5"] = GitManager.xǁGitManagerǁget_diff__mutmut_5  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_diff__mutmut["xǁGitManagerǁget_diff__mutmut_6"] = GitManager.xǁGitManagerǁget_diff__mutmut_6  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_diff__mutmut["xǁGitManagerǁget_diff__mutmut_7"] = GitManager.xǁGitManagerǁget_diff__mutmut_7  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_diff__mutmut["xǁGitManagerǁget_diff__mutmut_8"] = GitManager.xǁGitManagerǁget_diff__mutmut_8  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_diff__mutmut["xǁGitManagerǁget_diff__mutmut_9"] = GitManager.xǁGitManagerǁget_diff__mutmut_9  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_diff__mutmut["xǁGitManagerǁget_diff__mutmut_10"] = GitManager.xǁGitManagerǁget_diff__mutmut_10  # type: ignore # mutmut generated

mutants_xǁGitManagerǁget_log__mutmut["_mutmut_orig"] = GitManager.xǁGitManagerǁget_log__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_1"] = GitManager.xǁGitManagerǁget_log__mutmut_1  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_2"] = GitManager.xǁGitManagerǁget_log__mutmut_2  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_3"] = GitManager.xǁGitManagerǁget_log__mutmut_3  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_4"] = GitManager.xǁGitManagerǁget_log__mutmut_4  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_5"] = GitManager.xǁGitManagerǁget_log__mutmut_5  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_6"] = GitManager.xǁGitManagerǁget_log__mutmut_6  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_7"] = GitManager.xǁGitManagerǁget_log__mutmut_7  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_8"] = GitManager.xǁGitManagerǁget_log__mutmut_8  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_9"] = GitManager.xǁGitManagerǁget_log__mutmut_9  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_10"] = GitManager.xǁGitManagerǁget_log__mutmut_10  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_11"] = GitManager.xǁGitManagerǁget_log__mutmut_11  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_12"] = GitManager.xǁGitManagerǁget_log__mutmut_12  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_13"] = GitManager.xǁGitManagerǁget_log__mutmut_13  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_14"] = GitManager.xǁGitManagerǁget_log__mutmut_14  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_15"] = GitManager.xǁGitManagerǁget_log__mutmut_15  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_16"] = GitManager.xǁGitManagerǁget_log__mutmut_16  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_17"] = GitManager.xǁGitManagerǁget_log__mutmut_17  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_18"] = GitManager.xǁGitManagerǁget_log__mutmut_18  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_19"] = GitManager.xǁGitManagerǁget_log__mutmut_19  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_20"] = GitManager.xǁGitManagerǁget_log__mutmut_20  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_21"] = GitManager.xǁGitManagerǁget_log__mutmut_21  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_22"] = GitManager.xǁGitManagerǁget_log__mutmut_22  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_23"] = GitManager.xǁGitManagerǁget_log__mutmut_23  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_24"] = GitManager.xǁGitManagerǁget_log__mutmut_24  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_25"] = GitManager.xǁGitManagerǁget_log__mutmut_25  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_26"] = GitManager.xǁGitManagerǁget_log__mutmut_26  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_27"] = GitManager.xǁGitManagerǁget_log__mutmut_27  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_28"] = GitManager.xǁGitManagerǁget_log__mutmut_28  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_29"] = GitManager.xǁGitManagerǁget_log__mutmut_29  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_30"] = GitManager.xǁGitManagerǁget_log__mutmut_30  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_31"] = GitManager.xǁGitManagerǁget_log__mutmut_31  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_32"] = GitManager.xǁGitManagerǁget_log__mutmut_32  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_33"] = GitManager.xǁGitManagerǁget_log__mutmut_33  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_34"] = GitManager.xǁGitManagerǁget_log__mutmut_34  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_35"] = GitManager.xǁGitManagerǁget_log__mutmut_35  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_log__mutmut["xǁGitManagerǁget_log__mutmut_36"] = GitManager.xǁGitManagerǁget_log__mutmut_36  # type: ignore # mutmut generated

mutants_xǁGitManagerǁget_file_diff__mutmut["_mutmut_orig"] = GitManager.xǁGitManagerǁget_file_diff__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_file_diff__mutmut["xǁGitManagerǁget_file_diff__mutmut_1"] = GitManager.xǁGitManagerǁget_file_diff__mutmut_1  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_file_diff__mutmut["xǁGitManagerǁget_file_diff__mutmut_2"] = GitManager.xǁGitManagerǁget_file_diff__mutmut_2  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_file_diff__mutmut["xǁGitManagerǁget_file_diff__mutmut_3"] = GitManager.xǁGitManagerǁget_file_diff__mutmut_3  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_file_diff__mutmut["xǁGitManagerǁget_file_diff__mutmut_4"] = GitManager.xǁGitManagerǁget_file_diff__mutmut_4  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_file_diff__mutmut["xǁGitManagerǁget_file_diff__mutmut_5"] = GitManager.xǁGitManagerǁget_file_diff__mutmut_5  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_file_diff__mutmut["xǁGitManagerǁget_file_diff__mutmut_6"] = GitManager.xǁGitManagerǁget_file_diff__mutmut_6  # type: ignore # mutmut generated
mutants_xǁGitManagerǁget_file_diff__mutmut["xǁGitManagerǁget_file_diff__mutmut_7"] = GitManager.xǁGitManagerǁget_file_diff__mutmut_7  # type: ignore # mutmut generated
mutants_x_get_git_manager__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_git_manager__mutmut)
def get_git_manager(workspace: Path) -> GitManager:
    """Git 매니저 생성 헬퍼"""
    return GitManager(workspace)


def x_get_git_manager__mutmut_orig(workspace: Path) -> GitManager:
    """Git 매니저 생성 헬퍼"""
    return GitManager(workspace)


def x_get_git_manager__mutmut_1(workspace: Path) -> GitManager:
    """Git 매니저 생성 헬퍼"""
    return GitManager(None)


mutants_x_get_git_manager__mutmut["_mutmut_orig"] = x_get_git_manager__mutmut_orig  # type: ignore # mutmut generated
mutants_x_get_git_manager__mutmut["x_get_git_manager__mutmut_1"] = x_get_git_manager__mutmut_1  # type: ignore # mutmut generated
