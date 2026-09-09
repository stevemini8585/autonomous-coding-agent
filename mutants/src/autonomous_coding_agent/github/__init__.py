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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict


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
mutants_xǁGitHubClientǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁ_run__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁ_run_json__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁget_issue__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁlist_issues__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁcreate_issue__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁclose_issue__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁadd_comment__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁcreate_pr__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁget_pr__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁlist_prs__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁmerge_pr__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁadd_review_comment__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁget_repo_info__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGitHubClientǁget_file_content__mutmut: MutantDict = {}  # type: ignore


class GitHubClient:
    """GitHub CLI (gh) 래퍼"""

    @_mutmut_mutated(mutants_xǁGitHubClientǁ__init____mutmut)
    def __init__(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self._check_gh_cli()

    def xǁGitHubClientǁ__init____mutmut_orig(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self._check_gh_cli()

    def xǁGitHubClientǁ__init____mutmut_1(self, workspace: Path):
        self.workspace = None
        self._check_gh_cli()

    def xǁGitHubClientǁ__init____mutmut_2(self, workspace: Path):
        self.workspace = Path(None).resolve()
        self._check_gh_cli()

    @_mutmut_mutated(mutants_xǁGitHubClientǁ_check_gh_cli__mutmut)
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

    def xǁGitHubClientǁ_check_gh_cli__mutmut_orig(self) -> None:
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

    def xǁGitHubClientǁ_check_gh_cli__mutmut_1(self) -> None:
        """gh CLI 확인"""
        result = None
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_2(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            None,
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_3(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=None,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_4(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=True,
            capture_output=None,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_5(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=True,
            capture_output=True,
            text=None,
        )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_6(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_7(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_8(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_9(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=True,
            capture_output=True,
            )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_10(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "XXgh --versionXX",
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_11(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "GH --VERSION",
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_12(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_13(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=True,
            capture_output=False,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_14(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=True,
            capture_output=True,
            text=False,
        )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_15(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_16(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode != 1:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_17(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(None)
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_18(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("XXGitHub CLI (gh)가 설치되지 않음: https://cli.github.comXX")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_19(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("github cli (gh)가 설치되지 않음: https://cli.github.com")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_20(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("GITHUB CLI (GH)가 설치되지 않음: HTTPS://CLI.GITHUB.COM")
        log.info(f"GitHub CLI 사용 가능: {result.stdout.strip()}")

    def xǁGitHubClientǁ_check_gh_cli__mutmut_21(self) -> None:
        """gh CLI 확인"""
        result = subprocess.run(
            "gh --version",
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError("GitHub CLI (gh)가 설치되지 않음: https://cli.github.com")
        log.info(None)

    @_mutmut_mutated(mutants_xǁGitHubClientǁ_run__mutmut)
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

    def xǁGitHubClientǁ_run__mutmut_orig(self, cmd: str) -> subprocess.CompletedProcess:
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

    def xǁGitHubClientǁ_run__mutmut_1(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(None)
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitHubClientǁ_run__mutmut_2(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            None,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitHubClientǁ_run__mutmut_3(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=None,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitHubClientǁ_run__mutmut_4(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=None,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitHubClientǁ_run__mutmut_5(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=None,
            text=True,
            timeout=60,
        )

    def xǁGitHubClientǁ_run__mutmut_6(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=None,
            timeout=60,
        )

    def xǁGitHubClientǁ_run__mutmut_7(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=None,
        )

    def xǁGitHubClientǁ_run__mutmut_8(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitHubClientǁ_run__mutmut_9(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitHubClientǁ_run__mutmut_10(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitHubClientǁ_run__mutmut_11(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            text=True,
            timeout=60,
        )

    def xǁGitHubClientǁ_run__mutmut_12(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            timeout=60,
        )

    def xǁGitHubClientǁ_run__mutmut_13(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            )

    def xǁGitHubClientǁ_run__mutmut_14(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=False,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )

    def xǁGitHubClientǁ_run__mutmut_15(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=False,
            text=True,
            timeout=60,
        )

    def xǁGitHubClientǁ_run__mutmut_16(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=False,
            timeout=60,
        )

    def xǁGitHubClientǁ_run__mutmut_17(self, cmd: str) -> subprocess.CompletedProcess:
        """gh 명령 실행"""
        log.info(f"GitHub CLI 실행: {cmd}")
        return subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=61,
        )

    @_mutmut_mutated(mutants_xǁGitHubClientǁ_run_json__mutmut)
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

    def xǁGitHubClientǁ_run_json__mutmut_orig(self, cmd: str) -> dict | None:
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

    def xǁGitHubClientǁ_run_json__mutmut_1(self, cmd: str) -> dict | None:
        """JSON 출력 명령 실행"""
        # 명령에 이미 --json이 있는지 확인
        if "XX--jsonXX" not in cmd:
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

    def xǁGitHubClientǁ_run_json__mutmut_2(self, cmd: str) -> dict | None:
        """JSON 출력 명령 실행"""
        # 명령에 이미 --json이 있는지 확인
        if "--JSON" not in cmd:
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

    def xǁGitHubClientǁ_run_json__mutmut_3(self, cmd: str) -> dict | None:
        """JSON 출력 명령 실행"""
        # 명령에 이미 --json이 있는지 확인
        if "--json" in cmd:
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

    def xǁGitHubClientǁ_run_json__mutmut_4(self, cmd: str) -> dict | None:
        """JSON 출력 명령 실행"""
        # 명령에 이미 --json이 있는지 확인
        if "--json" not in cmd:
            cmd = None
        result = self._run(cmd)
        if result.returncode != 0:
            log.error(f"GitHub CLI 실패: {result.stderr}")
            return None
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as e:
            log.error(f"JSON 파싱 실패: {e}, stdout: {result.stdout[:200]}")
            return None

    def xǁGitHubClientǁ_run_json__mutmut_5(self, cmd: str) -> dict | None:
        """JSON 출력 명령 실행"""
        # 명령에 이미 --json이 있는지 확인
        if "--json" not in cmd:
            cmd = cmd - " --json"
        result = self._run(cmd)
        if result.returncode != 0:
            log.error(f"GitHub CLI 실패: {result.stderr}")
            return None
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as e:
            log.error(f"JSON 파싱 실패: {e}, stdout: {result.stdout[:200]}")
            return None

    def xǁGitHubClientǁ_run_json__mutmut_6(self, cmd: str) -> dict | None:
        """JSON 출력 명령 실행"""
        # 명령에 이미 --json이 있는지 확인
        if "--json" not in cmd:
            cmd = cmd + "XX --jsonXX"
        result = self._run(cmd)
        if result.returncode != 0:
            log.error(f"GitHub CLI 실패: {result.stderr}")
            return None
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as e:
            log.error(f"JSON 파싱 실패: {e}, stdout: {result.stdout[:200]}")
            return None

    def xǁGitHubClientǁ_run_json__mutmut_7(self, cmd: str) -> dict | None:
        """JSON 출력 명령 실행"""
        # 명령에 이미 --json이 있는지 확인
        if "--json" not in cmd:
            cmd = cmd + " --JSON"
        result = self._run(cmd)
        if result.returncode != 0:
            log.error(f"GitHub CLI 실패: {result.stderr}")
            return None
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as e:
            log.error(f"JSON 파싱 실패: {e}, stdout: {result.stdout[:200]}")
            return None

    def xǁGitHubClientǁ_run_json__mutmut_8(self, cmd: str) -> dict | None:
        """JSON 출력 명령 실행"""
        # 명령에 이미 --json이 있는지 확인
        if "--json" not in cmd:
            cmd = cmd + " --json"
        result = None
        if result.returncode != 0:
            log.error(f"GitHub CLI 실패: {result.stderr}")
            return None
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as e:
            log.error(f"JSON 파싱 실패: {e}, stdout: {result.stdout[:200]}")
            return None

    def xǁGitHubClientǁ_run_json__mutmut_9(self, cmd: str) -> dict | None:
        """JSON 출력 명령 실행"""
        # 명령에 이미 --json이 있는지 확인
        if "--json" not in cmd:
            cmd = cmd + " --json"
        result = self._run(None)
        if result.returncode != 0:
            log.error(f"GitHub CLI 실패: {result.stderr}")
            return None
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as e:
            log.error(f"JSON 파싱 실패: {e}, stdout: {result.stdout[:200]}")
            return None

    def xǁGitHubClientǁ_run_json__mutmut_10(self, cmd: str) -> dict | None:
        """JSON 출력 명령 실행"""
        # 명령에 이미 --json이 있는지 확인
        if "--json" not in cmd:
            cmd = cmd + " --json"
        result = self._run(cmd)
        if result.returncode == 0:
            log.error(f"GitHub CLI 실패: {result.stderr}")
            return None
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as e:
            log.error(f"JSON 파싱 실패: {e}, stdout: {result.stdout[:200]}")
            return None

    def xǁGitHubClientǁ_run_json__mutmut_11(self, cmd: str) -> dict | None:
        """JSON 출력 명령 실행"""
        # 명령에 이미 --json이 있는지 확인
        if "--json" not in cmd:
            cmd = cmd + " --json"
        result = self._run(cmd)
        if result.returncode != 1:
            log.error(f"GitHub CLI 실패: {result.stderr}")
            return None
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as e:
            log.error(f"JSON 파싱 실패: {e}, stdout: {result.stdout[:200]}")
            return None

    def xǁGitHubClientǁ_run_json__mutmut_12(self, cmd: str) -> dict | None:
        """JSON 출력 명령 실행"""
        # 명령에 이미 --json이 있는지 확인
        if "--json" not in cmd:
            cmd = cmd + " --json"
        result = self._run(cmd)
        if result.returncode != 0:
            log.error(None)
            return None
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as e:
            log.error(f"JSON 파싱 실패: {e}, stdout: {result.stdout[:200]}")
            return None

    def xǁGitHubClientǁ_run_json__mutmut_13(self, cmd: str) -> dict | None:
        """JSON 출력 명령 실행"""
        # 명령에 이미 --json이 있는지 확인
        if "--json" not in cmd:
            cmd = cmd + " --json"
        result = self._run(cmd)
        if result.returncode != 0:
            log.error(f"GitHub CLI 실패: {result.stderr}")
            return None
        try:
            return json.loads(None)
        except json.JSONDecodeError as e:
            log.error(f"JSON 파싱 실패: {e}, stdout: {result.stdout[:200]}")
            return None

    def xǁGitHubClientǁ_run_json__mutmut_14(self, cmd: str) -> dict | None:
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
            log.error(None)
            return None

    def xǁGitHubClientǁ_run_json__mutmut_15(self, cmd: str) -> dict | None:
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
            log.error(f"JSON 파싱 실패: {e}, stdout: {result.stdout[:201]}")
            return None

    # === Issue 관련 ===

    @_mutmut_mutated(mutants_xǁGitHubClientǁget_issue__mutmut)
    def get_issue(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
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

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_orig(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
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

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_1(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = None
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

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_2(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            None
        )
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

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_3(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if data:
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

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_4(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=None,
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_5(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=None,
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_6(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=None,
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_7(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=None,
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_8(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=None,
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_9(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=None,
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_10(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=None,
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_11(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
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
            updated_at=None,
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_12(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
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
            url=None,
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_13(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_14(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_15(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_16(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_17(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_18(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_19(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_20(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
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
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_21(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
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
            )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_22(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["XXnumberXX"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_23(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["NUMBER"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_24(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["XXtitleXX"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_25(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["TITLE"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_26(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get(None, ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_27(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", None),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_28(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get(""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_29(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_30(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("XXbodyXX", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_31(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("BODY", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_32(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", "XXXX"),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_33(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["XXstateXX"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_34(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["STATE"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_35(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["XXnameXX"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_36(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["NAME"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_37(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get(None, [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_38(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", None)],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_39(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get([])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_40(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", )],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_41(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("XXlabelsXX", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_42(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("LABELS", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_43(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["XXloginXX"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_44(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["LOGIN"] for a in data.get("assignees", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_45(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get(None, [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_46(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", None)],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_47(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get([])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_48(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", )],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_49(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("XXassigneesXX", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_50(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("ASSIGNEES", [])],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_51(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["XXcreatedAtXX"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_52(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["createdat"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_53(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
        if not data:
            return None

        return GitHubIssue(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ""),
            state=data["state"],
            labels=[l["name"] for l in data.get("labels", [])],
            assignees=[a["login"] for a in data.get("assignees", [])],
            created_at=data["CREATEDAT"],
            updated_at=data["updatedAt"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_54(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
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
            updated_at=data["XXupdatedAtXX"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_55(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
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
            updated_at=data["updatedat"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_56(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
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
            updated_at=data["UPDATEDAT"],
            url=data["url"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_57(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
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
            url=data["XXurlXX"],
        )

    # === Issue 관련 ===

    def xǁGitHubClientǁget_issue__mutmut_58(self, number: int) -> GitHubIssue | None:
        """이슈 조회"""
        data = self._run_json(
            f"gh issue view {number} --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"
        )
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
            url=data["URL"],
        )

    @_mutmut_mutated(mutants_xǁGitHubClientǁlist_issues__mutmut)
    def list_issues(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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

    def xǁGitHubClientǁlist_issues__mutmut_orig(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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

    def xǁGitHubClientǁlist_issues__mutmut_1(
        self, state: str = "XXopenXX", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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

    def xǁGitHubClientǁlist_issues__mutmut_2(
        self, state: str = "OPEN", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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

    def xǁGitHubClientǁlist_issues__mutmut_3(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 21
    ) -> list[GitHubIssue]:
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

    def xǁGitHubClientǁlist_issues__mutmut_4(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = None
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

    def xǁGitHubClientǁlist_issues__mutmut_5(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd = " --label " + " --label ".join(labels)
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

    def xǁGitHubClientǁlist_issues__mutmut_6(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd -= " --label " + " --label ".join(labels)
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

    def xǁGitHubClientǁlist_issues__mutmut_7(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += " --label " - " --label ".join(labels)
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

    def xǁGitHubClientǁlist_issues__mutmut_8(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += "XX --label XX" + " --label ".join(labels)
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

    def xǁGitHubClientǁlist_issues__mutmut_9(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += " --LABEL " + " --label ".join(labels)
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

    def xǁGitHubClientǁlist_issues__mutmut_10(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += " --label " + " --label ".join(None)
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

    def xǁGitHubClientǁlist_issues__mutmut_11(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += " --label " + "XX --label XX".join(labels)
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

    def xǁGitHubClientǁlist_issues__mutmut_12(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += " --label " + " --LABEL ".join(labels)
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

    def xǁGitHubClientǁlist_issues__mutmut_13(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += " --label " + " --label ".join(labels)
        cmd = " --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"

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

    def xǁGitHubClientǁlist_issues__mutmut_14(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += " --label " + " --label ".join(labels)
        cmd -= " --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"

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

    def xǁGitHubClientǁlist_issues__mutmut_15(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += " --label " + " --label ".join(labels)
        cmd += "XX --json number,title,body,state,labels,assignees,createdAt,updatedAt,urlXX"

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

    def xǁGitHubClientǁlist_issues__mutmut_16(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += " --label " + " --label ".join(labels)
        cmd += " --json number,title,body,state,labels,assignees,createdat,updatedat,url"

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

    def xǁGitHubClientǁlist_issues__mutmut_17(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += " --label " + " --label ".join(labels)
        cmd += " --JSON NUMBER,TITLE,BODY,STATE,LABELS,ASSIGNEES,CREATEDAT,UPDATEDAT,URL"

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

    def xǁGitHubClientǁlist_issues__mutmut_18(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += " --label " + " --label ".join(labels)
        cmd += " --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"

        data = None
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

    def xǁGitHubClientǁlist_issues__mutmut_19(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += " --label " + " --label ".join(labels)
        cmd += " --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"

        data = self._run_json(None)
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

    def xǁGitHubClientǁlist_issues__mutmut_20(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
        """이슈 목록 조회"""
        cmd = f"gh issue list --state {state} --limit {limit}"
        if labels:
            cmd += " --label " + " --label ".join(labels)
        cmd += " --json number,title,body,state,labels,assignees,createdAt,updatedAt,url"

        data = self._run_json(cmd)
        if data:
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

    def xǁGitHubClientǁlist_issues__mutmut_21(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                number=None,
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

    def xǁGitHubClientǁlist_issues__mutmut_22(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                title=None,
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

    def xǁGitHubClientǁlist_issues__mutmut_23(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                body=None,
                state=d["state"],
                labels=[l["name"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_24(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                state=None,
                labels=[l["name"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_25(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                labels=None,
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_26(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                assignees=None,
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_27(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                created_at=None,
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_28(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                updated_at=None,
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_29(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                url=None,
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_30(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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

    def xǁGitHubClientǁlist_issues__mutmut_31(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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

    def xǁGitHubClientǁlist_issues__mutmut_32(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                state=d["state"],
                labels=[l["name"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_33(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                labels=[l["name"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_34(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_35(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_36(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_37(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_38(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_39(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                number=d["XXnumberXX"],
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

    def xǁGitHubClientǁlist_issues__mutmut_40(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                number=d["NUMBER"],
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

    def xǁGitHubClientǁlist_issues__mutmut_41(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                title=d["XXtitleXX"],
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

    def xǁGitHubClientǁlist_issues__mutmut_42(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                title=d["TITLE"],
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

    def xǁGitHubClientǁlist_issues__mutmut_43(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                body=d.get(None, ""),
                state=d["state"],
                labels=[l["name"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_44(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                body=d.get("body", None),
                state=d["state"],
                labels=[l["name"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_45(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                body=d.get(""),
                state=d["state"],
                labels=[l["name"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_46(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                body=d.get("body", ),
                state=d["state"],
                labels=[l["name"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_47(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                body=d.get("XXbodyXX", ""),
                state=d["state"],
                labels=[l["name"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_48(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                body=d.get("BODY", ""),
                state=d["state"],
                labels=[l["name"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_49(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                body=d.get("body", "XXXX"),
                state=d["state"],
                labels=[l["name"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_50(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                state=d["XXstateXX"],
                labels=[l["name"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_51(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                state=d["STATE"],
                labels=[l["name"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_52(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                labels=[l["XXnameXX"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_53(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                labels=[l["NAME"] for l in d.get("labels", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_54(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                labels=[l["name"] for l in d.get(None, [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_55(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                labels=[l["name"] for l in d.get("labels", None)],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_56(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                labels=[l["name"] for l in d.get([])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_57(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                labels=[l["name"] for l in d.get("labels", )],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_58(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                labels=[l["name"] for l in d.get("XXlabelsXX", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_59(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                labels=[l["name"] for l in d.get("LABELS", [])],
                assignees=[a["login"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_60(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                assignees=[a["XXloginXX"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_61(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                assignees=[a["LOGIN"] for a in d.get("assignees", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_62(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                assignees=[a["login"] for a in d.get(None, [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_63(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                assignees=[a["login"] for a in d.get("assignees", None)],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_64(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                assignees=[a["login"] for a in d.get([])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_65(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                assignees=[a["login"] for a in d.get("assignees", )],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_66(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                assignees=[a["login"] for a in d.get("XXassigneesXX", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_67(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                assignees=[a["login"] for a in d.get("ASSIGNEES", [])],
                created_at=d["createdAt"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_68(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                created_at=d["XXcreatedAtXX"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_69(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                created_at=d["createdat"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_70(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                created_at=d["CREATEDAT"],
                updated_at=d["updatedAt"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_71(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                updated_at=d["XXupdatedAtXX"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_72(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                updated_at=d["updatedat"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_73(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                updated_at=d["UPDATEDAT"],
                url=d["url"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_74(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                url=d["XXurlXX"],
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_issues__mutmut_75(
        self, state: str = "open", labels: list[str] | None = None, limit: int = 20
    ) -> list[GitHubIssue]:
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
                url=d["URL"],
            )
            for d in data
        ]

    @_mutmut_mutated(mutants_xǁGitHubClientǁcreate_issue__mutmut)
    def create_issue(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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

    def xǁGitHubClientǁcreate_issue__mutmut_orig(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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

    def xǁGitHubClientǁcreate_issue__mutmut_1(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = None
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

    def xǁGitHubClientǁcreate_issue__mutmut_2(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd = " --label " + " --label ".join(labels)
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

    def xǁGitHubClientǁcreate_issue__mutmut_3(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd -= " --label " + " --label ".join(labels)
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

    def xǁGitHubClientǁcreate_issue__mutmut_4(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " - " --label ".join(labels)
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

    def xǁGitHubClientǁcreate_issue__mutmut_5(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += "XX --label XX" + " --label ".join(labels)
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

    def xǁGitHubClientǁcreate_issue__mutmut_6(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --LABEL " + " --label ".join(labels)
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

    def xǁGitHubClientǁcreate_issue__mutmut_7(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(None)
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

    def xǁGitHubClientǁcreate_issue__mutmut_8(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + "XX --label XX".join(labels)
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

    def xǁGitHubClientǁcreate_issue__mutmut_9(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --LABEL ".join(labels)
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

    def xǁGitHubClientǁcreate_issue__mutmut_10(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd = " --assignee " + " --assignee ".join(assignees)

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

    def xǁGitHubClientǁcreate_issue__mutmut_11(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd -= " --assignee " + " --assignee ".join(assignees)

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

    def xǁGitHubClientǁcreate_issue__mutmut_12(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += " --assignee " - " --assignee ".join(assignees)

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

    def xǁGitHubClientǁcreate_issue__mutmut_13(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += "XX --assignee XX" + " --assignee ".join(assignees)

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

    def xǁGitHubClientǁcreate_issue__mutmut_14(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += " --ASSIGNEE " + " --assignee ".join(assignees)

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

    def xǁGitHubClientǁcreate_issue__mutmut_15(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += " --assignee " + " --assignee ".join(None)

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

    def xǁGitHubClientǁcreate_issue__mutmut_16(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += " --assignee " + "XX --assignee XX".join(assignees)

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

    def xǁGitHubClientǁcreate_issue__mutmut_17(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += " --assignee " + " --ASSIGNEE ".join(assignees)

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

    def xǁGitHubClientǁcreate_issue__mutmut_18(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += " --assignee " + " --assignee ".join(assignees)

        result = None
        if result.returncode != 0:
            log.error(f"이슈 생성 실패: {result.stderr}")
            return None

        # URL에서 번호 추출
        url = result.stdout.strip()
        if "/issues/" in url:
            return int(url.split("/issues/")[-1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_19(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += " --assignee " + " --assignee ".join(assignees)

        result = subprocess.run(
            None,
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

    def xǁGitHubClientǁcreate_issue__mutmut_20(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += " --assignee " + " --assignee ".join(assignees)

        result = subprocess.run(
            cmd,
            shell=None,
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

    def xǁGitHubClientǁcreate_issue__mutmut_21(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += " --assignee " + " --assignee ".join(assignees)

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=None,
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

    def xǁGitHubClientǁcreate_issue__mutmut_22(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
            capture_output=None,
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

    def xǁGitHubClientǁcreate_issue__mutmut_23(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
            text=None,
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

    def xǁGitHubClientǁcreate_issue__mutmut_24(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
            timeout=None,
        )
        if result.returncode != 0:
            log.error(f"이슈 생성 실패: {result.stderr}")
            return None

        # URL에서 번호 추출
        url = result.stdout.strip()
        if "/issues/" in url:
            return int(url.split("/issues/")[-1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_25(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += " --assignee " + " --assignee ".join(assignees)

        result = subprocess.run(
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

    def xǁGitHubClientǁcreate_issue__mutmut_26(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += " --assignee " + " --assignee ".join(assignees)

        result = subprocess.run(
            cmd,
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

    def xǁGitHubClientǁcreate_issue__mutmut_27(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += " --assignee " + " --assignee ".join(assignees)

        result = subprocess.run(
            cmd,
            shell=True,
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

    def xǁGitHubClientǁcreate_issue__mutmut_28(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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

    def xǁGitHubClientǁcreate_issue__mutmut_29(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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

    def xǁGitHubClientǁcreate_issue__mutmut_30(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
            )
        if result.returncode != 0:
            log.error(f"이슈 생성 실패: {result.stderr}")
            return None

        # URL에서 번호 추출
        url = result.stdout.strip()
        if "/issues/" in url:
            return int(url.split("/issues/")[-1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_31(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
        """이슈 생성"""
        cmd = f'gh issue create --title "{title}" --body "{body}"'
        if labels:
            cmd += " --label " + " --label ".join(labels)
        if assignees:
            cmd += " --assignee " + " --assignee ".join(assignees)

        result = subprocess.run(
            cmd,
            shell=False,
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

    def xǁGitHubClientǁcreate_issue__mutmut_32(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
            capture_output=False,
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

    def xǁGitHubClientǁcreate_issue__mutmut_33(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
            text=False,
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

    def xǁGitHubClientǁcreate_issue__mutmut_34(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
            timeout=31,
        )
        if result.returncode != 0:
            log.error(f"이슈 생성 실패: {result.stderr}")
            return None

        # URL에서 번호 추출
        url = result.stdout.strip()
        if "/issues/" in url:
            return int(url.split("/issues/")[-1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_35(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
        if result.returncode == 0:
            log.error(f"이슈 생성 실패: {result.stderr}")
            return None

        # URL에서 번호 추출
        url = result.stdout.strip()
        if "/issues/" in url:
            return int(url.split("/issues/")[-1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_36(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
        if result.returncode != 1:
            log.error(f"이슈 생성 실패: {result.stderr}")
            return None

        # URL에서 번호 추출
        url = result.stdout.strip()
        if "/issues/" in url:
            return int(url.split("/issues/")[-1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_37(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
            log.error(None)
            return None

        # URL에서 번호 추출
        url = result.stdout.strip()
        if "/issues/" in url:
            return int(url.split("/issues/")[-1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_38(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
        url = None
        if "/issues/" in url:
            return int(url.split("/issues/")[-1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_39(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
        if "XX/issues/XX" in url:
            return int(url.split("/issues/")[-1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_40(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
        if "/ISSUES/" in url:
            return int(url.split("/issues/")[-1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_41(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
        if "/issues/" not in url:
            return int(url.split("/issues/")[-1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_42(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
            return int(None)
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_43(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
            return int(url.split(None)[-1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_44(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
            return int(url.split("XX/issues/XX")[-1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_45(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
            return int(url.split("/ISSUES/")[-1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_46(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
            return int(url.split("/issues/")[+1])
        return None

    def xǁGitHubClientǁcreate_issue__mutmut_47(
        self,
        title: str,
        body: str,
        labels: list[str] | None = None,
        assignees: list[str] | None = None,
    ) -> int | None:
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
            return int(url.split("/issues/")[-2])
        return None

    @_mutmut_mutated(mutants_xǁGitHubClientǁclose_issue__mutmut)
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

    def xǁGitHubClientǁclose_issue__mutmut_orig(self, number: int, reason: str = "completed") -> bool:
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

    def xǁGitHubClientǁclose_issue__mutmut_1(self, number: int, reason: str = "XXcompletedXX") -> bool:
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

    def xǁGitHubClientǁclose_issue__mutmut_2(self, number: int, reason: str = "COMPLETED") -> bool:
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

    def xǁGitHubClientǁclose_issue__mutmut_3(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = None
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_4(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            None,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_5(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=None,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_6(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=True,
            cwd=None,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_7(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=True,
            cwd=self.workspace,
            capture_output=None,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_8(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=None,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_9(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=None,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_10(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_11(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_12(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_13(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=True,
            cwd=self.workspace,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_14(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_15(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_16(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=False,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_17(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=True,
            cwd=self.workspace,
            capture_output=False,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_18(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=False,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_19(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=31,
        )
        return result.returncode == 0

    def xǁGitHubClientǁclose_issue__mutmut_20(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode != 0

    def xǁGitHubClientǁclose_issue__mutmut_21(self, number: int, reason: str = "completed") -> bool:
        """이슈 닫기"""
        result = subprocess.run(
            f"gh issue close {number} --reason {reason}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 1

    @_mutmut_mutated(mutants_xǁGitHubClientǁadd_comment__mutmut)
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

    def xǁGitHubClientǁadd_comment__mutmut_orig(self, number: int, body: str) -> bool:
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

    def xǁGitHubClientǁadd_comment__mutmut_1(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = None
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_2(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            None,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_3(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=None,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_4(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=True,
            cwd=None,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_5(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=True,
            cwd=self.workspace,
            capture_output=None,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_6(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=None,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_7(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=None,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_8(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_9(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_10(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_11(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=True,
            cwd=self.workspace,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_12(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_13(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_14(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=False,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_15(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=True,
            cwd=self.workspace,
            capture_output=False,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_16(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=False,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_17(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=31,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_comment__mutmut_18(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode != 0

    def xǁGitHubClientǁadd_comment__mutmut_19(self, number: int, body: str) -> bool:
        """코멘트 추가"""
        result = subprocess.run(
            f'gh issue comment {number} --body "{body}"',
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 1

    # === PR 관련 ===

    @_mutmut_mutated(mutants_xǁGitHubClientǁcreate_pr__mutmut)
    def create_pr(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_orig(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_1(
        self, title: str, body: str, head: str, base: str = "XXmainXX", draft: bool = False
    ) -> int | None:
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_2(
        self, title: str, body: str, head: str, base: str = "MAIN", draft: bool = False
    ) -> int | None:
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_3(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = True
    ) -> int | None:
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_4(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = None
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_5(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd = " --draft"

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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_6(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd -= " --draft"

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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_7(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += "XX --draftXX"

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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_8(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --DRAFT"

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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_9(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = None
        if result.returncode != 0:
            log.error(f"PR 생성 실패: {result.stderr}")
            return None

        url = result.stdout.strip()
        if "/pull/" in url:
            return int(url.split("/pull/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_10(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = subprocess.run(
            None,
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_11(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = subprocess.run(
            cmd,
            shell=None,
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_12(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=None,
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_13(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=None,
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_14(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=None,
            timeout=30,
        )
        if result.returncode != 0:
            log.error(f"PR 생성 실패: {result.stderr}")
            return None

        url = result.stdout.strip()
        if "/pull/" in url:
            return int(url.split("/pull/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_15(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
            timeout=None,
        )
        if result.returncode != 0:
            log.error(f"PR 생성 실패: {result.stderr}")
            return None

        url = result.stdout.strip()
        if "/pull/" in url:
            return int(url.split("/pull/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_16(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = subprocess.run(
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_17(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = subprocess.run(
            cmd,
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_18(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = subprocess.run(
            cmd,
            shell=True,
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_19(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_20(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            timeout=30,
        )
        if result.returncode != 0:
            log.error(f"PR 생성 실패: {result.stderr}")
            return None

        url = result.stdout.strip()
        if "/pull/" in url:
            return int(url.split("/pull/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_21(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
            )
        if result.returncode != 0:
            log.error(f"PR 생성 실패: {result.stderr}")
            return None

        url = result.stdout.strip()
        if "/pull/" in url:
            return int(url.split("/pull/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_22(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = subprocess.run(
            cmd,
            shell=False,
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_23(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=False,
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

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_24(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
        """PR 생성"""
        cmd = f'gh pr create --title "{title}" --body "{body}" --head {head} --base {base}'
        if draft:
            cmd += " --draft"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=False,
            timeout=30,
        )
        if result.returncode != 0:
            log.error(f"PR 생성 실패: {result.stderr}")
            return None

        url = result.stdout.strip()
        if "/pull/" in url:
            return int(url.split("/pull/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_25(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
            timeout=31,
        )
        if result.returncode != 0:
            log.error(f"PR 생성 실패: {result.stderr}")
            return None

        url = result.stdout.strip()
        if "/pull/" in url:
            return int(url.split("/pull/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_26(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
        if result.returncode == 0:
            log.error(f"PR 생성 실패: {result.stderr}")
            return None

        url = result.stdout.strip()
        if "/pull/" in url:
            return int(url.split("/pull/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_27(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
        if result.returncode != 1:
            log.error(f"PR 생성 실패: {result.stderr}")
            return None

        url = result.stdout.strip()
        if "/pull/" in url:
            return int(url.split("/pull/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_28(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
            log.error(None)
            return None

        url = result.stdout.strip()
        if "/pull/" in url:
            return int(url.split("/pull/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_29(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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

        url = None
        if "/pull/" in url:
            return int(url.split("/pull/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_30(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
        if "XX/pull/XX" in url:
            return int(url.split("/pull/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_31(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
        if "/PULL/" in url:
            return int(url.split("/pull/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_32(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
        if "/pull/" not in url:
            return int(url.split("/pull/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_33(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
            return int(None)
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_34(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
            return int(url.split(None)[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_35(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
            return int(url.split("XX/pull/XX")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_36(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
            return int(url.split("/PULL/")[-1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_37(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
            return int(url.split("/pull/")[+1])
        return None

    # === PR 관련 ===

    def xǁGitHubClientǁcreate_pr__mutmut_38(
        self, title: str, body: str, head: str, base: str = "main", draft: bool = False
    ) -> int | None:
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
            return int(url.split("/pull/")[-2])
        return None

    @_mutmut_mutated(mutants_xǁGitHubClientǁget_pr__mutmut)
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

    def xǁGitHubClientǁget_pr__mutmut_orig(self, number: int) -> GitHubPR | None:
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

    def xǁGitHubClientǁget_pr__mutmut_1(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = None
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

    def xǁGitHubClientǁget_pr__mutmut_2(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            None
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

    def xǁGitHubClientǁget_pr__mutmut_3(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if data:
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

    def xǁGitHubClientǁget_pr__mutmut_4(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=None,
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

    def xǁGitHubClientǁget_pr__mutmut_5(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["number"],
            title=None,
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

    def xǁGitHubClientǁget_pr__mutmut_6(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["number"],
            title=data["title"],
            body=None,
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

    def xǁGitHubClientǁget_pr__mutmut_7(self, number: int) -> GitHubPR | None:
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
            state=None,
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

    def xǁGitHubClientǁget_pr__mutmut_8(self, number: int) -> GitHubPR | None:
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
            head_branch=None,
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

    def xǁGitHubClientǁget_pr__mutmut_9(self, number: int) -> GitHubPR | None:
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
            base_branch=None,
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

    def xǁGitHubClientǁget_pr__mutmut_10(self, number: int) -> GitHubPR | None:
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
            draft=None,
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_11(self, number: int) -> GitHubPR | None:
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
            created_at=None,
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_12(self, number: int) -> GitHubPR | None:
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
            updated_at=None,
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_13(self, number: int) -> GitHubPR | None:
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
            url=None,
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_14(self, number: int) -> GitHubPR | None:
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
            head_sha=None,
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_15(self, number: int) -> GitHubPR | None:
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
            base_sha=None,
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_16(self, number: int) -> GitHubPR | None:
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
            additions=None,
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_17(self, number: int) -> GitHubPR | None:
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
            deletions=None,
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_18(self, number: int) -> GitHubPR | None:
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
            changed_files=None,
        )

    def xǁGitHubClientǁget_pr__mutmut_19(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
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

    def xǁGitHubClientǁget_pr__mutmut_20(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["number"],
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

    def xǁGitHubClientǁget_pr__mutmut_21(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["number"],
            title=data["title"],
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

    def xǁGitHubClientǁget_pr__mutmut_22(self, number: int) -> GitHubPR | None:
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

    def xǁGitHubClientǁget_pr__mutmut_23(self, number: int) -> GitHubPR | None:
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

    def xǁGitHubClientǁget_pr__mutmut_24(self, number: int) -> GitHubPR | None:
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

    def xǁGitHubClientǁget_pr__mutmut_25(self, number: int) -> GitHubPR | None:
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
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_26(self, number: int) -> GitHubPR | None:
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
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_27(self, number: int) -> GitHubPR | None:
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
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_28(self, number: int) -> GitHubPR | None:
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
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_29(self, number: int) -> GitHubPR | None:
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
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_30(self, number: int) -> GitHubPR | None:
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
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_31(self, number: int) -> GitHubPR | None:
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
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_32(self, number: int) -> GitHubPR | None:
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
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_33(self, number: int) -> GitHubPR | None:
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
            )

    def xǁGitHubClientǁget_pr__mutmut_34(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["XXnumberXX"],
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

    def xǁGitHubClientǁget_pr__mutmut_35(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["NUMBER"],
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

    def xǁGitHubClientǁget_pr__mutmut_36(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["number"],
            title=data["XXtitleXX"],
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

    def xǁGitHubClientǁget_pr__mutmut_37(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["number"],
            title=data["TITLE"],
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

    def xǁGitHubClientǁget_pr__mutmut_38(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["number"],
            title=data["title"],
            body=data.get(None, ""),
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

    def xǁGitHubClientǁget_pr__mutmut_39(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["number"],
            title=data["title"],
            body=data.get("body", None),
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

    def xǁGitHubClientǁget_pr__mutmut_40(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["number"],
            title=data["title"],
            body=data.get(""),
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

    def xǁGitHubClientǁget_pr__mutmut_41(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["number"],
            title=data["title"],
            body=data.get("body", ),
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

    def xǁGitHubClientǁget_pr__mutmut_42(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["number"],
            title=data["title"],
            body=data.get("XXbodyXX", ""),
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

    def xǁGitHubClientǁget_pr__mutmut_43(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["number"],
            title=data["title"],
            body=data.get("BODY", ""),
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

    def xǁGitHubClientǁget_pr__mutmut_44(self, number: int) -> GitHubPR | None:
        """PR 조회"""
        data = self._run_json(
            f"gh pr view {number} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        )
        if not data:
            return None

        return GitHubPR(
            number=data["number"],
            title=data["title"],
            body=data.get("body", "XXXX"),
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

    def xǁGitHubClientǁget_pr__mutmut_45(self, number: int) -> GitHubPR | None:
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
            state=data["XXstateXX"],
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

    def xǁGitHubClientǁget_pr__mutmut_46(self, number: int) -> GitHubPR | None:
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
            state=data["STATE"],
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

    def xǁGitHubClientǁget_pr__mutmut_47(self, number: int) -> GitHubPR | None:
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
            head_branch=data.get(None, ""),
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

    def xǁGitHubClientǁget_pr__mutmut_48(self, number: int) -> GitHubPR | None:
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
            head_branch=data.get("headRefName", None),
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

    def xǁGitHubClientǁget_pr__mutmut_49(self, number: int) -> GitHubPR | None:
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
            head_branch=data.get(""),
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

    def xǁGitHubClientǁget_pr__mutmut_50(self, number: int) -> GitHubPR | None:
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
            head_branch=data.get("headRefName", ),
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

    def xǁGitHubClientǁget_pr__mutmut_51(self, number: int) -> GitHubPR | None:
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
            head_branch=data.get("XXheadRefNameXX", ""),
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

    def xǁGitHubClientǁget_pr__mutmut_52(self, number: int) -> GitHubPR | None:
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
            head_branch=data.get("headrefname", ""),
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

    def xǁGitHubClientǁget_pr__mutmut_53(self, number: int) -> GitHubPR | None:
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
            head_branch=data.get("HEADREFNAME", ""),
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

    def xǁGitHubClientǁget_pr__mutmut_54(self, number: int) -> GitHubPR | None:
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
            head_branch=data.get("headRefName", "XXXX"),
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

    def xǁGitHubClientǁget_pr__mutmut_55(self, number: int) -> GitHubPR | None:
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
            base_branch=data.get(None, ""),
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

    def xǁGitHubClientǁget_pr__mutmut_56(self, number: int) -> GitHubPR | None:
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
            base_branch=data.get("baseRefName", None),
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

    def xǁGitHubClientǁget_pr__mutmut_57(self, number: int) -> GitHubPR | None:
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
            base_branch=data.get(""),
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

    def xǁGitHubClientǁget_pr__mutmut_58(self, number: int) -> GitHubPR | None:
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
            base_branch=data.get("baseRefName", ),
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

    def xǁGitHubClientǁget_pr__mutmut_59(self, number: int) -> GitHubPR | None:
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
            base_branch=data.get("XXbaseRefNameXX", ""),
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

    def xǁGitHubClientǁget_pr__mutmut_60(self, number: int) -> GitHubPR | None:
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
            base_branch=data.get("baserefname", ""),
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

    def xǁGitHubClientǁget_pr__mutmut_61(self, number: int) -> GitHubPR | None:
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
            base_branch=data.get("BASEREFNAME", ""),
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

    def xǁGitHubClientǁget_pr__mutmut_62(self, number: int) -> GitHubPR | None:
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
            base_branch=data.get("baseRefName", "XXXX"),
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

    def xǁGitHubClientǁget_pr__mutmut_63(self, number: int) -> GitHubPR | None:
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
            draft=data.get(None, False),
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_64(self, number: int) -> GitHubPR | None:
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
            draft=data.get("isDraft", None),
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_65(self, number: int) -> GitHubPR | None:
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
            draft=data.get(False),
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_66(self, number: int) -> GitHubPR | None:
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
            draft=data.get("isDraft", ),
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_67(self, number: int) -> GitHubPR | None:
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
            draft=data.get("XXisDraftXX", False),
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_68(self, number: int) -> GitHubPR | None:
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
            draft=data.get("isdraft", False),
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_69(self, number: int) -> GitHubPR | None:
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
            draft=data.get("ISDRAFT", False),
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_70(self, number: int) -> GitHubPR | None:
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
            draft=data.get("isDraft", True),
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_71(self, number: int) -> GitHubPR | None:
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
            created_at=data["XXcreatedAtXX"],
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_72(self, number: int) -> GitHubPR | None:
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
            created_at=data["createdat"],
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_73(self, number: int) -> GitHubPR | None:
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
            created_at=data["CREATEDAT"],
            updated_at=data["updatedAt"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_74(self, number: int) -> GitHubPR | None:
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
            updated_at=data["XXupdatedAtXX"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_75(self, number: int) -> GitHubPR | None:
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
            updated_at=data["updatedat"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_76(self, number: int) -> GitHubPR | None:
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
            updated_at=data["UPDATEDAT"],
            url=data["url"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_77(self, number: int) -> GitHubPR | None:
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
            url=data["XXurlXX"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_78(self, number: int) -> GitHubPR | None:
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
            url=data["URL"],
            head_sha="",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_79(self, number: int) -> GitHubPR | None:
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
            head_sha="XXXX",
            base_sha="",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_80(self, number: int) -> GitHubPR | None:
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
            base_sha="XXXX",
            additions=data.get("additions", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_81(self, number: int) -> GitHubPR | None:
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
            additions=data.get(None, 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_82(self, number: int) -> GitHubPR | None:
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
            additions=data.get("additions", None),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_83(self, number: int) -> GitHubPR | None:
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
            additions=data.get(0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_84(self, number: int) -> GitHubPR | None:
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
            additions=data.get("additions", ),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_85(self, number: int) -> GitHubPR | None:
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
            additions=data.get("XXadditionsXX", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_86(self, number: int) -> GitHubPR | None:
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
            additions=data.get("ADDITIONS", 0),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_87(self, number: int) -> GitHubPR | None:
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
            additions=data.get("additions", 1),
            deletions=data.get("deletions", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_88(self, number: int) -> GitHubPR | None:
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
            deletions=data.get(None, 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_89(self, number: int) -> GitHubPR | None:
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
            deletions=data.get("deletions", None),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_90(self, number: int) -> GitHubPR | None:
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
            deletions=data.get(0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_91(self, number: int) -> GitHubPR | None:
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
            deletions=data.get("deletions", ),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_92(self, number: int) -> GitHubPR | None:
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
            deletions=data.get("XXdeletionsXX", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_93(self, number: int) -> GitHubPR | None:
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
            deletions=data.get("DELETIONS", 0),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_94(self, number: int) -> GitHubPR | None:
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
            deletions=data.get("deletions", 1),
            changed_files=data.get("changedFiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_95(self, number: int) -> GitHubPR | None:
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
            changed_files=data.get(None, 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_96(self, number: int) -> GitHubPR | None:
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
            changed_files=data.get("changedFiles", None),
        )

    def xǁGitHubClientǁget_pr__mutmut_97(self, number: int) -> GitHubPR | None:
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
            changed_files=data.get(0),
        )

    def xǁGitHubClientǁget_pr__mutmut_98(self, number: int) -> GitHubPR | None:
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
            changed_files=data.get("changedFiles", ),
        )

    def xǁGitHubClientǁget_pr__mutmut_99(self, number: int) -> GitHubPR | None:
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
            changed_files=data.get("XXchangedFilesXX", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_100(self, number: int) -> GitHubPR | None:
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
            changed_files=data.get("changedfiles", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_101(self, number: int) -> GitHubPR | None:
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
            changed_files=data.get("CHANGEDFILES", 0),
        )

    def xǁGitHubClientǁget_pr__mutmut_102(self, number: int) -> GitHubPR | None:
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
            changed_files=data.get("changedFiles", 1),
        )

    @_mutmut_mutated(mutants_xǁGitHubClientǁlist_prs__mutmut)
    def list_prs(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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

    def xǁGitHubClientǁlist_prs__mutmut_orig(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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

    def xǁGitHubClientǁlist_prs__mutmut_1(
        self, state: str = "XXopenXX", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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

    def xǁGitHubClientǁlist_prs__mutmut_2(
        self, state: str = "OPEN", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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

    def xǁGitHubClientǁlist_prs__mutmut_3(
        self, state: str = "open", base: str | None = None, limit: int = 21
    ) -> list[GitHubPR]:
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

    def xǁGitHubClientǁlist_prs__mutmut_4(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
        """PR 목록 조회"""
        cmd = None
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

    def xǁGitHubClientǁlist_prs__mutmut_5(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
        """PR 목록 조회"""
        cmd = f"gh pr list --state {state} --limit {limit} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        if base:
            cmd = f" --base {base}"

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

    def xǁGitHubClientǁlist_prs__mutmut_6(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
        """PR 목록 조회"""
        cmd = f"gh pr list --state {state} --limit {limit} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        if base:
            cmd -= f" --base {base}"

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

    def xǁGitHubClientǁlist_prs__mutmut_7(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
        """PR 목록 조회"""
        cmd = f"gh pr list --state {state} --limit {limit} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        if base:
            cmd += f" --base {base}"

        data = None
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

    def xǁGitHubClientǁlist_prs__mutmut_8(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
        """PR 목록 조회"""
        cmd = f"gh pr list --state {state} --limit {limit} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        if base:
            cmd += f" --base {base}"

        data = self._run_json(None)
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

    def xǁGitHubClientǁlist_prs__mutmut_9(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
        """PR 목록 조회"""
        cmd = f"gh pr list --state {state} --limit {limit} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        if base:
            cmd += f" --base {base}"

        data = self._run_json(cmd)
        if data:
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

    def xǁGitHubClientǁlist_prs__mutmut_10(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
        """PR 목록 조회"""
        cmd = f"gh pr list --state {state} --limit {limit} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        if base:
            cmd += f" --base {base}"

        data = self._run_json(cmd)
        if not data:
            return []

        return [
            GitHubPR(
                number=None,
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

    def xǁGitHubClientǁlist_prs__mutmut_11(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                title=None,
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

    def xǁGitHubClientǁlist_prs__mutmut_12(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                body=None,
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

    def xǁGitHubClientǁlist_prs__mutmut_13(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                state=None,
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

    def xǁGitHubClientǁlist_prs__mutmut_14(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                head_branch=None,
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

    def xǁGitHubClientǁlist_prs__mutmut_15(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                base_branch=None,
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

    def xǁGitHubClientǁlist_prs__mutmut_16(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                draft=None,
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

    def xǁGitHubClientǁlist_prs__mutmut_17(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                created_at=None,
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

    def xǁGitHubClientǁlist_prs__mutmut_18(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                updated_at=None,
                url=d["url"],
                head_sha="",
                base_sha="",
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_19(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                url=None,
                head_sha="",
                base_sha="",
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_20(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                head_sha=None,
                base_sha="",
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_21(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                base_sha=None,
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_22(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                additions=None,
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_23(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                deletions=None,
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_24(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                changed_files=None,
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_25(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
        """PR 목록 조회"""
        cmd = f"gh pr list --state {state} --limit {limit} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        if base:
            cmd += f" --base {base}"

        data = self._run_json(cmd)
        if not data:
            return []

        return [
            GitHubPR(
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

    def xǁGitHubClientǁlist_prs__mutmut_26(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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

    def xǁGitHubClientǁlist_prs__mutmut_27(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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

    def xǁGitHubClientǁlist_prs__mutmut_28(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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

    def xǁGitHubClientǁlist_prs__mutmut_29(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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

    def xǁGitHubClientǁlist_prs__mutmut_30(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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

    def xǁGitHubClientǁlist_prs__mutmut_31(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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

    def xǁGitHubClientǁlist_prs__mutmut_32(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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

    def xǁGitHubClientǁlist_prs__mutmut_33(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                url=d["url"],
                head_sha="",
                base_sha="",
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_34(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                head_sha="",
                base_sha="",
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_35(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                base_sha="",
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_36(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_37(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_38(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_39(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_40(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
        """PR 목록 조회"""
        cmd = f"gh pr list --state {state} --limit {limit} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        if base:
            cmd += f" --base {base}"

        data = self._run_json(cmd)
        if not data:
            return []

        return [
            GitHubPR(
                number=d["XXnumberXX"],
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

    def xǁGitHubClientǁlist_prs__mutmut_41(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
        """PR 목록 조회"""
        cmd = f"gh pr list --state {state} --limit {limit} --json number,title,body,state,headRefName,baseRefName,isDraft,createdAt,updatedAt,url,additions,deletions,changedFiles"
        if base:
            cmd += f" --base {base}"

        data = self._run_json(cmd)
        if not data:
            return []

        return [
            GitHubPR(
                number=d["NUMBER"],
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

    def xǁGitHubClientǁlist_prs__mutmut_42(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                title=d["XXtitleXX"],
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

    def xǁGitHubClientǁlist_prs__mutmut_43(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                title=d["TITLE"],
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

    def xǁGitHubClientǁlist_prs__mutmut_44(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                body=d.get(None, ""),
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

    def xǁGitHubClientǁlist_prs__mutmut_45(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                body=d.get("body", None),
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

    def xǁGitHubClientǁlist_prs__mutmut_46(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                body=d.get(""),
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

    def xǁGitHubClientǁlist_prs__mutmut_47(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                body=d.get("body", ),
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

    def xǁGitHubClientǁlist_prs__mutmut_48(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                body=d.get("XXbodyXX", ""),
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

    def xǁGitHubClientǁlist_prs__mutmut_49(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                body=d.get("BODY", ""),
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

    def xǁGitHubClientǁlist_prs__mutmut_50(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                body=d.get("body", "XXXX"),
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

    def xǁGitHubClientǁlist_prs__mutmut_51(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                state=d["XXstateXX"],
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

    def xǁGitHubClientǁlist_prs__mutmut_52(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                state=d["STATE"],
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

    def xǁGitHubClientǁlist_prs__mutmut_53(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                head_branch=d.get(None, ""),
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

    def xǁGitHubClientǁlist_prs__mutmut_54(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                head_branch=d.get("headRefName", None),
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

    def xǁGitHubClientǁlist_prs__mutmut_55(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                head_branch=d.get(""),
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

    def xǁGitHubClientǁlist_prs__mutmut_56(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                head_branch=d.get("headRefName", ),
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

    def xǁGitHubClientǁlist_prs__mutmut_57(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                head_branch=d.get("XXheadRefNameXX", ""),
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

    def xǁGitHubClientǁlist_prs__mutmut_58(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                head_branch=d.get("headrefname", ""),
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

    def xǁGitHubClientǁlist_prs__mutmut_59(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                head_branch=d.get("HEADREFNAME", ""),
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

    def xǁGitHubClientǁlist_prs__mutmut_60(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                head_branch=d.get("headRefName", "XXXX"),
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

    def xǁGitHubClientǁlist_prs__mutmut_61(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                base_branch=d.get(None, ""),
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

    def xǁGitHubClientǁlist_prs__mutmut_62(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                base_branch=d.get("baseRefName", None),
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

    def xǁGitHubClientǁlist_prs__mutmut_63(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                base_branch=d.get(""),
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

    def xǁGitHubClientǁlist_prs__mutmut_64(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                base_branch=d.get("baseRefName", ),
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

    def xǁGitHubClientǁlist_prs__mutmut_65(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                base_branch=d.get("XXbaseRefNameXX", ""),
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

    def xǁGitHubClientǁlist_prs__mutmut_66(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                base_branch=d.get("baserefname", ""),
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

    def xǁGitHubClientǁlist_prs__mutmut_67(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                base_branch=d.get("BASEREFNAME", ""),
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

    def xǁGitHubClientǁlist_prs__mutmut_68(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                base_branch=d.get("baseRefName", "XXXX"),
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

    def xǁGitHubClientǁlist_prs__mutmut_69(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                draft=d.get(None, False),
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

    def xǁGitHubClientǁlist_prs__mutmut_70(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                draft=d.get("isDraft", None),
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

    def xǁGitHubClientǁlist_prs__mutmut_71(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                draft=d.get(False),
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

    def xǁGitHubClientǁlist_prs__mutmut_72(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                draft=d.get("isDraft", ),
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

    def xǁGitHubClientǁlist_prs__mutmut_73(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                draft=d.get("XXisDraftXX", False),
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

    def xǁGitHubClientǁlist_prs__mutmut_74(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                draft=d.get("isdraft", False),
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

    def xǁGitHubClientǁlist_prs__mutmut_75(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                draft=d.get("ISDRAFT", False),
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

    def xǁGitHubClientǁlist_prs__mutmut_76(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                draft=d.get("isDraft", True),
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

    def xǁGitHubClientǁlist_prs__mutmut_77(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                created_at=d["XXcreatedAtXX"],
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

    def xǁGitHubClientǁlist_prs__mutmut_78(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                created_at=d["createdat"],
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

    def xǁGitHubClientǁlist_prs__mutmut_79(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                created_at=d["CREATEDAT"],
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

    def xǁGitHubClientǁlist_prs__mutmut_80(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                updated_at=d["XXupdatedAtXX"],
                url=d["url"],
                head_sha="",
                base_sha="",
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_81(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                updated_at=d["updatedat"],
                url=d["url"],
                head_sha="",
                base_sha="",
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_82(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                updated_at=d["UPDATEDAT"],
                url=d["url"],
                head_sha="",
                base_sha="",
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_83(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                url=d["XXurlXX"],
                head_sha="",
                base_sha="",
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_84(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                url=d["URL"],
                head_sha="",
                base_sha="",
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_85(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                head_sha="XXXX",
                base_sha="",
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_86(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                base_sha="XXXX",
                additions=d.get("additions", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_87(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                additions=d.get(None, 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_88(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                additions=d.get("additions", None),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_89(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                additions=d.get(0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_90(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                additions=d.get("additions", ),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_91(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                additions=d.get("XXadditionsXX", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_92(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                additions=d.get("ADDITIONS", 0),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_93(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                additions=d.get("additions", 1),
                deletions=d.get("deletions", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_94(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                deletions=d.get(None, 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_95(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                deletions=d.get("deletions", None),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_96(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                deletions=d.get(0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_97(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                deletions=d.get("deletions", ),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_98(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                deletions=d.get("XXdeletionsXX", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_99(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                deletions=d.get("DELETIONS", 0),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_100(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                deletions=d.get("deletions", 1),
                changed_files=d.get("changedFiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_101(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                changed_files=d.get(None, 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_102(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                changed_files=d.get("changedFiles", None),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_103(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                changed_files=d.get(0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_104(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                changed_files=d.get("changedFiles", ),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_105(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                changed_files=d.get("XXchangedFilesXX", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_106(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                changed_files=d.get("changedfiles", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_107(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                changed_files=d.get("CHANGEDFILES", 0),
            )
            for d in data
        ]

    def xǁGitHubClientǁlist_prs__mutmut_108(
        self, state: str = "open", base: str | None = None, limit: int = 20
    ) -> list[GitHubPR]:
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
                changed_files=d.get("changedFiles", 1),
            )
            for d in data
        ]

    @_mutmut_mutated(mutants_xǁGitHubClientǁmerge_pr__mutmut)
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

    def xǁGitHubClientǁmerge_pr__mutmut_orig(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
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

    def xǁGitHubClientǁmerge_pr__mutmut_1(self, number: int, method: str = "XXsquashXX", delete_branch: bool = True) -> bool:
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

    def xǁGitHubClientǁmerge_pr__mutmut_2(self, number: int, method: str = "SQUASH", delete_branch: bool = True) -> bool:
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

    def xǁGitHubClientǁmerge_pr__mutmut_3(self, number: int, method: str = "squash", delete_branch: bool = False) -> bool:
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

    def xǁGitHubClientǁmerge_pr__mutmut_4(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = None
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

    def xǁGitHubClientǁmerge_pr__mutmut_5(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd = " --delete-branch"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_6(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd -= " --delete-branch"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_7(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += "XX --delete-branchXX"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_8(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --DELETE-BRANCH"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_9(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = None
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_10(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = subprocess.run(
            None,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_11(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = subprocess.run(
            cmd,
            shell=None,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_12(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=None,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_13(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=None,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_14(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=None,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_15(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
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
            timeout=None,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_16(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = subprocess.run(
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_17(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = subprocess.run(
            cmd,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_18(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_19(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_20(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_21(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
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
            )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_22(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = subprocess.run(
            cmd,
            shell=False,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_23(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=False,
            text=True,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_24(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
        """PR 병합"""
        cmd = f"gh pr merge {number} --{method}"
        if delete_branch:
            cmd += " --delete-branch"

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=False,
            timeout=60,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_25(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
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
            timeout=61,
        )
        return result.returncode == 0

    def xǁGitHubClientǁmerge_pr__mutmut_26(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
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
        return result.returncode != 0

    def xǁGitHubClientǁmerge_pr__mutmut_27(self, number: int, method: str = "squash", delete_branch: bool = True) -> bool:
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
        return result.returncode == 1

    @_mutmut_mutated(mutants_xǁGitHubClientǁadd_review_comment__mutmut)
    def add_review_comment(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_orig(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_1(
        self, number: int, body: str, path: str, line: int, side: str = "XXRIGHTXX"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_2(
        self, number: int, body: str, path: str, line: int, side: str = "right"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_3(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = None
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_4(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "XXbodyXX": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_5(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "BODY": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_6(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "XXpathXX": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_7(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "PATH": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_8(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "XXlineXX": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_9(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "LINE": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_10(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "XXsideXX": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_11(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "SIDE": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_12(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = None
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_13(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            None,
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_14(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=None,
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_15(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=None,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_16(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=None,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_17(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=None,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_18(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=None,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_19(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=None,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_20(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_21(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_22(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_23(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_24(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_25(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_26(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_27(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(None),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_28(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=False,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_29(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=False,
            text=True,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_30(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=False,
            timeout=30,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_31(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=31,
        )
        return result.returncode == 0

    def xǁGitHubClientǁadd_review_comment__mutmut_32(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode != 0

    def xǁGitHubClientǁadd_review_comment__mutmut_33(
        self, number: int, body: str, path: str, line: int, side: str = "RIGHT"
    ) -> bool:
        """PR 리뷰 코멘트 추가"""
        # gh api를 사용한 코멘트 추가
        comment_data = {
            "body": body,
            "path": path,
            "line": line,
            "side": side,
        }
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/pulls/{number}/comments --input -",
            input=json.dumps(comment_data),
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode == 1

    # === 리포지토리 ===

    @_mutmut_mutated(mutants_xǁGitHubClientǁget_repo_info__mutmut)
    def get_repo_info(self) -> dict | None:
        """저장소 정보"""
        return self._run_json("gh repo view --json name,owner,description,url,defaultBranchRef")

    # === 리포지토리 ===

    def xǁGitHubClientǁget_repo_info__mutmut_orig(self) -> dict | None:
        """저장소 정보"""
        return self._run_json("gh repo view --json name,owner,description,url,defaultBranchRef")

    # === 리포지토리 ===

    def xǁGitHubClientǁget_repo_info__mutmut_1(self) -> dict | None:
        """저장소 정보"""
        return self._run_json(None)

    # === 리포지토리 ===

    def xǁGitHubClientǁget_repo_info__mutmut_2(self) -> dict | None:
        """저장소 정보"""
        return self._run_json("XXgh repo view --json name,owner,description,url,defaultBranchRefXX")

    # === 리포지토리 ===

    def xǁGitHubClientǁget_repo_info__mutmut_3(self) -> dict | None:
        """저장소 정보"""
        return self._run_json("gh repo view --json name,owner,description,url,defaultbranchref")

    # === 리포지토리 ===

    def xǁGitHubClientǁget_repo_info__mutmut_4(self) -> dict | None:
        """저장소 정보"""
        return self._run_json("GH REPO VIEW --JSON NAME,OWNER,DESCRIPTION,URL,DEFAULTBRANCHREF")

    @_mutmut_mutated(mutants_xǁGitHubClientǁget_file_content__mutmut)
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

    def xǁGitHubClientǁget_file_content__mutmut_orig(self, path: str, ref: str = "HEAD") -> str | None:
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

    def xǁGitHubClientǁget_file_content__mutmut_1(self, path: str, ref: str = "XXHEADXX") -> str | None:
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

    def xǁGitHubClientǁget_file_content__mutmut_2(self, path: str, ref: str = "head") -> str | None:
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

    def xǁGitHubClientǁget_file_content__mutmut_3(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = None
        if result.returncode != 0:
            return None
        try:
            data = json.loads(result.stdout)
            import base64

            return base64.b64decode(data["content"]).decode("utf-8")
        except Exception:
            return None

    def xǁGitHubClientǁget_file_content__mutmut_4(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            None,
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

    def xǁGitHubClientǁget_file_content__mutmut_5(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=None,
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

    def xǁGitHubClientǁget_file_content__mutmut_6(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=True,
            cwd=None,
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

    def xǁGitHubClientǁget_file_content__mutmut_7(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=True,
            cwd=self.workspace,
            capture_output=None,
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

    def xǁGitHubClientǁget_file_content__mutmut_8(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=None,
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

    def xǁGitHubClientǁget_file_content__mutmut_9(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=None,
        )
        if result.returncode != 0:
            return None
        try:
            data = json.loads(result.stdout)
            import base64

            return base64.b64decode(data["content"]).decode("utf-8")
        except Exception:
            return None

    def xǁGitHubClientǁget_file_content__mutmut_10(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
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

    def xǁGitHubClientǁget_file_content__mutmut_11(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
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

    def xǁGitHubClientǁget_file_content__mutmut_12(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=True,
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

    def xǁGitHubClientǁget_file_content__mutmut_13(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=True,
            cwd=self.workspace,
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

    def xǁGitHubClientǁget_file_content__mutmut_14(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
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

    def xǁGitHubClientǁget_file_content__mutmut_15(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            )
        if result.returncode != 0:
            return None
        try:
            data = json.loads(result.stdout)
            import base64

            return base64.b64decode(data["content"]).decode("utf-8")
        except Exception:
            return None

    def xǁGitHubClientǁget_file_content__mutmut_16(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=False,
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

    def xǁGitHubClientǁget_file_content__mutmut_17(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=True,
            cwd=self.workspace,
            capture_output=False,
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

    def xǁGitHubClientǁget_file_content__mutmut_18(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=False,
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

    def xǁGitHubClientǁget_file_content__mutmut_19(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=31,
        )
        if result.returncode != 0:
            return None
        try:
            data = json.loads(result.stdout)
            import base64

            return base64.b64decode(data["content"]).decode("utf-8")
        except Exception:
            return None

    def xǁGitHubClientǁget_file_content__mutmut_20(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode == 0:
            return None
        try:
            data = json.loads(result.stdout)
            import base64

            return base64.b64decode(data["content"]).decode("utf-8")
        except Exception:
            return None

    def xǁGitHubClientǁget_file_content__mutmut_21(self, path: str, ref: str = "HEAD") -> str | None:
        """파일 내용 조회"""
        result = subprocess.run(
            f"gh api repos/{{owner}}/{{repo}}/contents/{path}?ref={ref}",
            shell=True,
            cwd=self.workspace,
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 1:
            return None
        try:
            data = json.loads(result.stdout)
            import base64

            return base64.b64decode(data["content"]).decode("utf-8")
        except Exception:
            return None

    def xǁGitHubClientǁget_file_content__mutmut_22(self, path: str, ref: str = "HEAD") -> str | None:
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
            data = None
            import base64

            return base64.b64decode(data["content"]).decode("utf-8")
        except Exception:
            return None

    def xǁGitHubClientǁget_file_content__mutmut_23(self, path: str, ref: str = "HEAD") -> str | None:
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
            data = json.loads(None)
            import base64

            return base64.b64decode(data["content"]).decode("utf-8")
        except Exception:
            return None

    def xǁGitHubClientǁget_file_content__mutmut_24(self, path: str, ref: str = "HEAD") -> str | None:
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

            return base64.b64decode(data["content"]).decode(None)
        except Exception:
            return None

    def xǁGitHubClientǁget_file_content__mutmut_25(self, path: str, ref: str = "HEAD") -> str | None:
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

            return base64.b64decode(None).decode("utf-8")
        except Exception:
            return None

    def xǁGitHubClientǁget_file_content__mutmut_26(self, path: str, ref: str = "HEAD") -> str | None:
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

            return base64.b64decode(data["XXcontentXX"]).decode("utf-8")
        except Exception:
            return None

    def xǁGitHubClientǁget_file_content__mutmut_27(self, path: str, ref: str = "HEAD") -> str | None:
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

            return base64.b64decode(data["CONTENT"]).decode("utf-8")
        except Exception:
            return None

    def xǁGitHubClientǁget_file_content__mutmut_28(self, path: str, ref: str = "HEAD") -> str | None:
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

            return base64.b64decode(data["content"]).decode("XXutf-8XX")
        except Exception:
            return None

    def xǁGitHubClientǁget_file_content__mutmut_29(self, path: str, ref: str = "HEAD") -> str | None:
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

            return base64.b64decode(data["content"]).decode("UTF-8")
        except Exception:
            return None

mutants_xǁGitHubClientǁ__init____mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ__init____mutmut['xǁGitHubClientǁ__init____mutmut_1'] = GitHubClient.xǁGitHubClientǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ__init____mutmut['xǁGitHubClientǁ__init____mutmut_2'] = GitHubClient.xǁGitHubClientǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_1'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_2'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_3'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_4'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_5'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_6'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_7'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_8'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_9'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_10'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_11'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_12'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_13'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_14'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_15'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_16'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_17'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_18'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_19'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_20'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_check_gh_cli__mutmut['xǁGitHubClientǁ_check_gh_cli__mutmut_21'] = GitHubClient.xǁGitHubClientǁ_check_gh_cli__mutmut_21 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁ_run__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_1'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_2'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_3'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_4'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_5'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_6'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_7'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_8'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_9'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_10'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_11'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_12'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_13'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_14'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_15'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_16'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run__mutmut['xǁGitHubClientǁ_run__mutmut_17'] = GitHubClient.xǁGitHubClientǁ_run__mutmut_17 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁ_run_json__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_1'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_2'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_3'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_4'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_5'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_6'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_7'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_8'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_9'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_10'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_11'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_12'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_13'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_14'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁ_run_json__mutmut['xǁGitHubClientǁ_run_json__mutmut_15'] = GitHubClient.xǁGitHubClientǁ_run_json__mutmut_15 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁget_issue__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_1'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_2'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_3'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_4'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_5'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_6'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_7'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_8'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_9'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_10'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_11'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_12'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_13'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_14'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_15'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_16'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_17'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_18'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_19'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_20'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_21'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_22'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_23'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_24'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_25'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_26'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_27'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_28'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_29'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_30'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_31'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_32'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_33'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_34'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_35'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_36'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_37'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_38'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_39'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_40'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_41'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_42'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_43'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_44'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_45'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_46'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_47'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_48'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_49'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_50'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_51'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_51 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_52'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_52 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_53'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_53 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_54'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_54 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_55'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_55 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_56'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_56 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_57'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_57 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_issue__mutmut['xǁGitHubClientǁget_issue__mutmut_58'] = GitHubClient.xǁGitHubClientǁget_issue__mutmut_58 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁlist_issues__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_1'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_2'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_3'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_4'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_5'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_6'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_7'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_8'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_9'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_10'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_11'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_12'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_13'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_14'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_15'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_16'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_17'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_18'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_19'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_20'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_21'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_22'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_23'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_24'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_25'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_26'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_27'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_28'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_29'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_30'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_31'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_32'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_33'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_34'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_35'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_36'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_37'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_38'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_39'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_40'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_41'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_42'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_43'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_44'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_45'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_46'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_47'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_48'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_49'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_50'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_51'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_51 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_52'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_52 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_53'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_53 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_54'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_54 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_55'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_55 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_56'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_56 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_57'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_57 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_58'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_58 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_59'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_59 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_60'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_60 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_61'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_61 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_62'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_62 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_63'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_63 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_64'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_64 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_65'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_65 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_66'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_66 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_67'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_67 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_68'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_68 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_69'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_69 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_70'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_70 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_71'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_71 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_72'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_72 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_73'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_73 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_74'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_74 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_issues__mutmut['xǁGitHubClientǁlist_issues__mutmut_75'] = GitHubClient.xǁGitHubClientǁlist_issues__mutmut_75 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁcreate_issue__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_1'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_2'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_3'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_4'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_5'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_6'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_7'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_8'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_9'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_10'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_11'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_12'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_13'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_14'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_15'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_16'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_17'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_18'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_19'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_20'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_21'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_22'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_23'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_24'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_25'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_26'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_27'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_28'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_29'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_30'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_31'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_32'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_33'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_34'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_35'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_36'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_37'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_38'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_39'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_40'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_41'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_42'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_43'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_44'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_45'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_46'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_issue__mutmut['xǁGitHubClientǁcreate_issue__mutmut_47'] = GitHubClient.xǁGitHubClientǁcreate_issue__mutmut_47 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁclose_issue__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_1'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_2'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_3'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_4'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_5'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_6'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_7'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_8'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_9'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_10'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_11'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_12'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_13'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_14'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_15'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_16'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_17'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_18'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_19'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_20'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁclose_issue__mutmut['xǁGitHubClientǁclose_issue__mutmut_21'] = GitHubClient.xǁGitHubClientǁclose_issue__mutmut_21 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁadd_comment__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_1'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_2'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_3'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_4'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_5'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_6'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_7'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_8'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_9'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_10'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_11'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_12'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_13'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_14'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_15'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_16'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_17'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_18'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_comment__mutmut['xǁGitHubClientǁadd_comment__mutmut_19'] = GitHubClient.xǁGitHubClientǁadd_comment__mutmut_19 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁcreate_pr__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_1'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_2'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_3'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_4'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_5'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_6'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_7'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_8'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_9'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_10'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_11'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_12'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_13'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_14'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_15'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_16'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_17'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_18'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_19'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_20'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_21'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_22'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_23'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_24'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_25'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_26'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_27'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_28'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_29'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_30'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_31'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_32'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_33'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_34'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_35'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_36'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_37'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁcreate_pr__mutmut['xǁGitHubClientǁcreate_pr__mutmut_38'] = GitHubClient.xǁGitHubClientǁcreate_pr__mutmut_38 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁget_pr__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_1'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_2'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_3'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_4'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_5'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_6'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_7'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_8'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_9'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_10'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_11'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_12'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_13'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_14'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_15'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_16'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_17'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_18'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_19'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_20'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_21'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_22'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_23'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_24'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_25'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_26'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_27'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_28'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_29'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_30'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_31'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_32'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_33'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_34'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_35'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_36'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_37'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_38'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_39'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_40'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_41'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_42'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_43'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_44'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_45'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_46'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_47'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_48'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_49'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_50'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_51'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_51 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_52'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_52 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_53'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_53 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_54'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_54 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_55'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_55 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_56'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_56 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_57'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_57 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_58'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_58 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_59'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_59 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_60'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_60 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_61'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_61 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_62'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_62 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_63'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_63 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_64'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_64 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_65'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_65 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_66'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_66 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_67'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_67 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_68'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_68 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_69'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_69 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_70'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_70 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_71'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_71 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_72'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_72 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_73'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_73 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_74'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_74 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_75'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_75 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_76'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_76 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_77'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_77 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_78'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_78 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_79'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_79 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_80'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_80 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_81'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_81 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_82'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_82 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_83'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_83 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_84'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_84 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_85'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_85 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_86'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_86 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_87'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_87 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_88'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_88 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_89'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_89 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_90'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_90 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_91'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_91 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_92'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_92 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_93'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_93 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_94'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_94 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_95'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_95 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_96'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_96 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_97'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_97 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_98'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_98 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_99'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_99 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_100'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_100 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_101'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_101 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_pr__mutmut['xǁGitHubClientǁget_pr__mutmut_102'] = GitHubClient.xǁGitHubClientǁget_pr__mutmut_102 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁlist_prs__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_1'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_2'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_3'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_4'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_5'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_6'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_7'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_8'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_9'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_10'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_11'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_12'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_13'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_14'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_15'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_16'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_17'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_18'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_19'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_20'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_21'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_22'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_23'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_24'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_25'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_26'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_27'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_28'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_29'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_30'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_31'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_32'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_33'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_33 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_34'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_34 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_35'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_35 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_36'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_36 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_37'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_37 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_38'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_38 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_39'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_39 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_40'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_40 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_41'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_41 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_42'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_42 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_43'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_43 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_44'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_44 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_45'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_45 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_46'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_46 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_47'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_47 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_48'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_48 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_49'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_49 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_50'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_50 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_51'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_51 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_52'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_52 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_53'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_53 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_54'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_54 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_55'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_55 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_56'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_56 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_57'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_57 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_58'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_58 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_59'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_59 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_60'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_60 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_61'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_61 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_62'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_62 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_63'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_63 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_64'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_64 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_65'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_65 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_66'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_66 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_67'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_67 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_68'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_68 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_69'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_69 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_70'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_70 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_71'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_71 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_72'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_72 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_73'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_73 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_74'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_74 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_75'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_75 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_76'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_76 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_77'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_77 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_78'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_78 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_79'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_79 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_80'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_80 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_81'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_81 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_82'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_82 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_83'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_83 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_84'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_84 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_85'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_85 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_86'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_86 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_87'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_87 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_88'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_88 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_89'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_89 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_90'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_90 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_91'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_91 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_92'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_92 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_93'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_93 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_94'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_94 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_95'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_95 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_96'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_96 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_97'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_97 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_98'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_98 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_99'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_99 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_100'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_100 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_101'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_101 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_102'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_102 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_103'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_103 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_104'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_104 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_105'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_105 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_106'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_106 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_107'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_107 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁlist_prs__mutmut['xǁGitHubClientǁlist_prs__mutmut_108'] = GitHubClient.xǁGitHubClientǁlist_prs__mutmut_108 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁmerge_pr__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_1'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_2'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_3'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_4'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_5'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_6'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_7'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_8'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_9'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_10'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_11'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_12'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_13'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_14'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_15'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_16'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_17'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_18'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_19'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_20'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_21'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_22'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_23'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_24'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_25'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_26'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁmerge_pr__mutmut['xǁGitHubClientǁmerge_pr__mutmut_27'] = GitHubClient.xǁGitHubClientǁmerge_pr__mutmut_27 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁadd_review_comment__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_1'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_2'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_3'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_4'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_5'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_6'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_7'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_8'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_9'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_10'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_11'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_12'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_13'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_14'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_15'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_16'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_17'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_18'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_19'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_20'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_21'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_22'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_23'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_24'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_25'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_26'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_27'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_28'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_29'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_29 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_30'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_30 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_31'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_31 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_32'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_32 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁadd_review_comment__mutmut['xǁGitHubClientǁadd_review_comment__mutmut_33'] = GitHubClient.xǁGitHubClientǁadd_review_comment__mutmut_33 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁget_repo_info__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁget_repo_info__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_repo_info__mutmut['xǁGitHubClientǁget_repo_info__mutmut_1'] = GitHubClient.xǁGitHubClientǁget_repo_info__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_repo_info__mutmut['xǁGitHubClientǁget_repo_info__mutmut_2'] = GitHubClient.xǁGitHubClientǁget_repo_info__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_repo_info__mutmut['xǁGitHubClientǁget_repo_info__mutmut_3'] = GitHubClient.xǁGitHubClientǁget_repo_info__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_repo_info__mutmut['xǁGitHubClientǁget_repo_info__mutmut_4'] = GitHubClient.xǁGitHubClientǁget_repo_info__mutmut_4 # type: ignore # mutmut generated

mutants_xǁGitHubClientǁget_file_content__mutmut['_mutmut_orig'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_1'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_2'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_3'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_4'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_5'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_6'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_7'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_8'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_9'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_10'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_11'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_12'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_13'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_14'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_15'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_16'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_17'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_18'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_19'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_20'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_20 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_21'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_21 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_22'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_22 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_23'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_23 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_24'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_24 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_25'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_25 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_26'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_26 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_27'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_27 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_28'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_28 # type: ignore # mutmut generated
mutants_xǁGitHubClientǁget_file_content__mutmut['xǁGitHubClientǁget_file_content__mutmut_29'] = GitHubClient.xǁGitHubClientǁget_file_content__mutmut_29 # type: ignore # mutmut generated
mutants_x_get_github_client__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_github_client__mutmut)
def get_github_client(workspace: Path) -> GitHubClient:
    """GitHub 클라이언트 생성 헬퍼"""
    return GitHubClient(workspace)


def x_get_github_client__mutmut_orig(workspace: Path) -> GitHubClient:
    """GitHub 클라이언트 생성 헬퍼"""
    return GitHubClient(workspace)


def x_get_github_client__mutmut_1(workspace: Path) -> GitHubClient:
    """GitHub 클라이언트 생성 헬퍼"""
    return GitHubClient(None)

mutants_x_get_github_client__mutmut['_mutmut_orig'] = x_get_github_client__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_github_client__mutmut['x_get_github_client__mutmut_1'] = x_get_github_client__mutmut_1 # type: ignore # mutmut generated
