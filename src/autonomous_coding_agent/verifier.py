"""
자율 코딩 에이전트 - 검증 실행기 (Verifier)
"""

from __future__ import annotations

import logging
import subprocess
import time
from pathlib import Path
from typing import Any

from .models import PlanStep, VerificationResult

log = logging.getLogger("autonomous_coding_agent.verifier")


class Verifier:
    """테스트, 린트, 타입체크, 빌드 실행 및 검증"""

    def __init__(self, workspace: Path):
        self.workspace = Path(workspace).resolve()
        self.language_configs = self._default_language_configs()

    def _default_language_configs(self) -> dict[str, dict[str, str]]:
        """기본 언어별 검증 명령어"""
        return {
            "python": {
                "test": "pytest -xvs --tb=short",
                "lint": "ruff check .",
                "format": "black --check .",
                "type": "mypy --explicit-package-bases",
                "coverage": "pytest --cov=. --cov-report=term-missing",
            },
            "javascript": {
                "test": "npm test -- --run",
                "lint": "eslint .",
                "format": "prettier --check .",
                "type": "tsc --noEmit",
            },
            "typescript": {
                "test": "npm test -- --run",
                "lint": "eslint .",
                "format": "prettier --check .",
                "type": "tsc --noEmit",
            },
            "go": {
                "test": "go test ./...",
                "lint": "golangci-lint run",
                "format": "gofmt -l .",
                "type": "go vet ./...",
            },
            "rust": {
                "test": "cargo test",
                "lint": "cargo clippy -- -D warnings",
                "format": "cargo fmt --check",
                "type": "cargo check",
            },
        }

    def verify_step(self, step: PlanStep, project_files: list[str]) -> VerificationResult:
        """단계 검증 실행"""
        log.info(f"검증 시작: {step.id}")
        start_time = time.time()

        # 언어 감지
        language = self._detect_language(project_files)
        config = self.language_configs.get(language, {})

        result = VerificationResult(step_id=step.id)

        try:
            # 테스트 실행
            if "test" in config:
                result.test_results = self._run_command(config["test"], "테스트", project_files)
                result.passed = result.test_results.get("passed", False)

            # 린트 실행
            if "lint" in config:
                result.lint_results = self._run_command(config["lint"], "린트", project_files)
                if not result.lint_results.get("passed", False):
                    result.warnings.append("린트 경고/오류 발견")

            # 포맷 체크
            if "format" in config:
                result.format_results = self._run_command(config["format"], "포맷", project_files)
                if not result.format_results.get("passed", False):
                    result.warnings.append("포맷팅 필요")

            # 타입 체크
            if "type" in config:
                result.type_results = self._run_command(config["type"], "타입 체크", project_files)
                if not result.type_results.get("passed", False):
                    result.errors.append("타입 체크 실패")
                    result.passed = False

            # 커버리지 추출
            result.coverage = self._extract_coverage(result.test_results)

        except Exception as e:
            log.error(f"검증 중 오류: {e}")
            result.passed = False
            result.errors.append(f"검증 실행 오류: {e}")

        result.duration_seconds = time.time() - start_time

        log.info(
            f"  검증 완료: {'PASS' if result.passed else 'FAIL'} ({result.duration_seconds:.1f}초)"
        )

        return result

    def _detect_language(self, files: list[str]) -> str:
        """파일 확장자로 언어 감지"""
        ext_counts = {}
        for f in files:
            ext = Path(f).suffix.lower()
            ext_counts[ext] = ext_counts.get(ext, 0) + 1

        if not ext_counts:
            return "python"

        top_ext = max(ext_counts, key=ext_counts.get)

        lang_map = {
            ".py": "python",
            ".js": "javascript",
            ".jsx": "javascript",
            ".ts": "typescript",
            ".tsx": "typescript",
            ".go": "go",
            ".rs": "rust",
            ".java": "java",
            ".kt": "kotlin",
            ".cs": "csharp",
            ".cpp": "cpp",
            ".cc": "cpp",
            ".cxx": "cpp",
            ".c": "c",
            ".h": "c",
            ".rb": "ruby",
            ".php": "php",
            ".swift": "swift",
        }

        return lang_map.get(top_ext, "python")

    def _run_command(
        self, command: str, name: str, files: list[str] | None = None
    ) -> dict[str, Any]:
        """명령어 실행 및 결과 파싱"""
        log.info(f"  {name} 실행: {command}")

        try:
            # 테스트 명령어는 전체 프로젝트에서 실행 (특정 파일 지정 안 함)
            if name == "테스트":
                full_command = command
            # 린트/포맷/타입 체크는 특정 파일이 있으면 그 파일들만, 없으면 전체
            elif files:
                file_args = " ".join(files)
                full_command = f"{command} {file_args}"
            else:
                full_command = command

            log.info(f"  {name} 실행: {full_command}")

            # For lint/format, first try to auto-fix
            if name in ("린트", "포맷") and not name == "테스트":
                fix_command = ""
                if name == "린트":
                    fix_command = "ruff check --fix ."
                elif name == "포맷":
                    fix_command = "black ."
                
                if fix_command:
                    log.info(f"  {name} 자동 수정 시도: {fix_command}")
                    subprocess.run(
                        fix_command,
                        shell=True,
                        cwd=self.workspace,
                        capture_output=True,
                        text=True,
                        timeout=60,
                    )

            proc = subprocess.run(
                full_command,
                shell=True,
                cwd=self.workspace,
                capture_output=True,
                text=True,
                timeout=300,
            )

            # pytest exit code 5 = no tests collected -> treat as passed
            passed = proc.returncode == 0 or (name == "테스트" and proc.returncode == 5)

            return {
                "passed": passed,
                "returncode": proc.returncode,
                "stdout": proc.stdout[-5000:] if proc.stdout else "",
                "stderr": proc.stderr[-5000:] if proc.stderr else "",
            }

        except subprocess.TimeoutExpired:
            return {
                "passed": False,
                "error": f"{name} 타임아웃 (300초)",
            }
        except Exception as e:
            return {
                "passed": False,
                "error": f"{name} 실행 오류: {e}",
            }

    def _extract_coverage(self, test_results: dict[str, Any]) -> float:
        """테스트 결과에서 커버리지 추출"""
        stdout = test_results.get("stdout", "")

        # pytest 커버리지 패턴
        import re

        patterns = [
            r"TOTAL\s+\d+\s+\d+\s+(\d+)%",
            r"coverage:\s*(\d+(?:\.\d+)?)%",
            r"(\d+(?:\.\d+)?)%\s+covered",
        ]

        for pattern in patterns:
            match = re.search(pattern, stdout)
            if match:
                return float(match.group(1))

        return 0.0

    def verify_project(self, project_files: list[str]) -> dict[str, VerificationResult]:
        """전체 프로젝트 검증 (단계별이 아닌 전체)"""
        # Filter to only Python files for Python language
        python_files = [f for f in project_files if f.endswith('.py')]
        language = self._detect_language(python_files)
        config = self.language_configs.get(language, {})

        results = {}

        for check_name in ["test", "lint", "format", "type"]:
            if check_name in config:
                step_id = f"verify_{check_name}"
                start_time = time.time()

                result = VerificationResult(step_id=step_id)
                # Use Korean name for auto-fix logic
                korean_name = {"test": "테스트", "lint": "린트", "format": "포맷", "type": "타입 체크"}[check_name]
                # For type check, need to pass files to mypy; for others, run on whole project
                if check_name == "type":
                    cmd_result = self._run_command(config[check_name], korean_name, python_files)
                else:
                    cmd_result = self._run_command(config[check_name], korean_name, None)

                if check_name == "test":
                    result.test_results = cmd_result
                    result.passed = cmd_result.get("passed", False)
                    result.coverage = self._extract_coverage(cmd_result)
                elif check_name == "lint":
                    result.lint_results = cmd_result
                    result.passed = cmd_result.get("passed", False)
                    if not cmd_result.get("passed", False):
                        result.warnings.append("린트 경고/오류 발견")
                elif check_name == "format":
                    result.format_results = cmd_result
                    result.passed = cmd_result.get("passed", False)
                    if not cmd_result.get("passed", False):
                        result.warnings.append("포맷팅 필요")
                elif check_name == "type":
                    result.type_results = cmd_result
                    result.passed = cmd_result.get("passed", False)
                    if not cmd_result.get("passed", False):
                        result.errors.append("타입 체크 실패")

                result.duration_seconds = time.time() - start_time
                results[check_name] = result

        return results


def run_verification(
    workspace: Path, step: PlanStep, project_files: list[str]
) -> VerificationResult:
    """검증 헬퍼"""
    verifier = Verifier(workspace)
    return verifier.verify_step(step, project_files)
