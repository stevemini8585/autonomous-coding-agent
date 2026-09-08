"""
코드 예제 자동 적용 모듈
검색된 라이브러리 예제를 현재 프로젝트 컨텍스트에 맞게 변환 및 적용
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, ClassVar

from .issue_parser import ParsedTask
from .web_search import Documentation, DocumentationParser

log = logging.getLogger("autonomous_coding_agent.code_adapter")


@dataclass
class ProjectContext:
    """프로젝트 컨텍스트 분석 결과"""

    root_path: Path
    language: str = "python"  # python, javascript, typescript, etc.
    framework: str | None = None  # fastapi, django, express, react, etc.
    package_manager: str | None = None  # pip, poetry, npm, yarn, pnpm
    import_style: str = "absolute"  # absolute, relative
    naming_convention: str = "snake_case"  # snake_case, camelCase, PascalCase
    type_hints: bool = True
    async_pattern: bool = False
    test_framework: str | None = None  # pytest, jest, vitest
    lint_config: dict[str, Any] = field(default_factory=dict)
    common_imports: list[str] = field(default_factory=list)
    code_patterns: dict[str, list[str]] = field(default_factory=dict)


@dataclass
class AdaptedCode:
    """변환된 코드"""

    original: str
    adapted: str
    target_file: str | None = None
    insert_after: str | None = None  # 특정 패턴 뒤에 삽입
    replace_pattern: str | None = None  # 특정 패턴 대체
    explanation: str = ""
    confidence: float = 0.8


class ProjectAnalyzer:
    """프로젝트 구조 및 코드 스타일 분석"""

    def __init__(self, workspace: str | Path):
        self.workspace = Path(workspace).resolve()

    def analyze(self) -> ProjectContext:
        """프로젝트 전체 분석"""
        context = ProjectContext(root_path=self.workspace)

        # 언어 감지
        context.language = self._detect_language()

        # 프레임워크 감지
        context.framework = self._detect_framework(context.language)

        # 패키지 매니저 감지
        context.package_manager = self._detect_package_manager()

        # 코드 스타일 분석
        if context.language == "python":
            self._analyze_python_style(context)
        elif context.language in ("javascript", "typescript"):
            self._analyze_js_ts_style(context)

        # 공통 설정
        context.test_framework = self._detect_test_framework(context.language)
        context.lint_config = self._detect_lint_config()

        log.info(
            f"프로젝트 분석 완료: {context.language}, {context.framework}, {context.package_manager}"
        )
        return context

    def _detect_language(self) -> str:
        """주 언어 감지"""
        py_files = list(self.workspace.rglob("*.py"))
        js_files = list(self.workspace.rglob("*.js")) + list(self.workspace.rglob("*.ts"))
        rs_files = list(self.workspace.rglob("*.rs"))
        go_files = list(self.workspace.rglob("*.go"))

        counts = {
            "python": len(py_files),
            "javascript": len([f for f in js_files if f.suffix == ".js"]),
            "typescript": len([f for f in js_files if f.suffix == ".ts"]),
            "rust": len(rs_files),
            "go": len(go_files),
        }

        return max(counts, key=counts.get) if max(counts.values()) > 0 else "python"

    def _detect_framework(self, language: str) -> str | None:
        """프레임워크 감지"""
        if language == "python":
            # pyproject.toml, requirements.txt, setup.py 확인
            for req_file in [
                "pyproject.toml",
                "requirements.txt",
                "setup.py",
                "Pipfile",
            ]:
                path = self.workspace / req_file
                if path.exists():
                    content = path.read_text(encoding="utf-8", errors="ignore").lower()
                    if "fastapi" in content:
                        return "fastapi"
                    elif "django" in content:
                        return "django"
                    elif "flask" in content:
                        return "flask"
                    elif "starlette" in content:
                        return "starlette"
                    elif "aiohttp" in content:
                        return "aiohttp"
        elif language in ("javascript", "typescript"):
            pkg_json = self.workspace / "package.json"
            if pkg_json.exists():
                import json

                try:
                    data = json.loads(pkg_json.read_text())
                    deps = {
                        **data.get("dependencies", {}),
                        **data.get("devDependencies", {}),
                    }
                    if "next" in deps:
                        return "nextjs"
                    elif "react" in deps:
                        return "react"
                    elif "vue" in deps:
                        return "vue"
                    elif "express" in deps:
                        return "express"
                    elif "nestjs" in deps:
                        return "nestjs"
                    elif "svelte" in deps:
                        return "svelte"
                except json.JSONDecodeError:
                    pass
        return None

    def _detect_package_manager(self) -> str | None:
        """패키지 매니저 감지 - 우선순위 기반 정확한 감지"""
        workspace = self.workspace

        # 1. Poetry 감지 (최우선 - pyproject.toml + poetry.lock 또는 [tool.poetry])
        pyproject = workspace / "pyproject.toml"
        if pyproject.exists():
            content = pyproject.read_text(encoding="utf-8", errors="ignore")
            if "[tool.poetry]" in content or (workspace / "poetry.lock").exists():
                return "poetry"
            # pyproject.toml에 poetry 관련 설정이 있는 경우도 체크
            if (
                "poetry" in content.lower()
                and ("tool.poetry" in content or "poetry" in content)
                and (workspace / "poetry.lock").exists()
            ):
                return "poetry"

        # 2. PDM 감지 (pyproject.toml + pdm.lock 또는 [tool.pdm])
        if pyproject.exists():
            content = pyproject.read_text(encoding="utf-8", errors="ignore")
            if "[tool.pdm]" in content or (workspace / "pdm.lock").exists():
                return "pdm"

        # 3. Hatch 감지 (pyproject.toml + hatch.toml 또는 [tool.hatch])
        if pyproject.exists():
            content = pyproject.read_text(encoding="utf-8", errors="ignore")
            if "[tool.hatch]" in content or (workspace / "hatch.toml").exists():
                return "hatch"

        # 4. Rye 감지 (rye.toml 또는 rye.lock)
        if (workspace / "rye.toml").exists() or (workspace / "rye.lock").exists():
            return "rye"

        # 4. uv 감지 (uv.lock 또는 pyproject.toml의 [tool.uv])
        if (workspace / "uv.lock").exists():
            return "uv"
        if pyproject.exists():
            content = pyproject.read_text(encoding="utf-8", errors="ignore")
            if "[tool.uv]" in content:
                return "uv"

        # 5. Pipenv 감지 (Pipfile + Pipfile.lock)
        pipfile = workspace / "Pipfile"
        if pipfile.exists():
            return "pipenv"

        # 6. Conda 감지 (environment.yml, environment.yaml, conda-lock.yml)
        for conda_file in ["environment.yml", "environment.yaml", "conda-lock.yml"]:
            if (workspace / conda_file).exists():
                return "conda"

        # 6. requirements.txt 기반 pip 감지 (requirements*.txt 패턴)
        req_files = list(workspace.glob("requirements*.txt"))
        if req_files:
            return "pip"

        # 7. setup.py / setup.cfg 기반 pip 감지 (legacy)
        if (workspace / "setup.py").exists() or (workspace / "setup.cfg").exists():
            return "pip"

        # 8. pyproject.toml이 있지만 위 매니저가 아니면 기본 pip (build-system이 setuptools/wheel인 경우 또는 [project] 섹션이 있는 경우)
        if pyproject.exists():
            content = pyproject.read_text(encoding="utf-8", errors="ignore")
            if (
                "[build-system]" in content
                and ("setuptools" in content or "wheel" in content or "pip" in content)
            ) or "[project]" in content:
                return "pip"

        # 9. Node.js 패키지 매니저
        if (workspace / "package.json").exists():
            if (workspace / "pnpm-lock.yaml").exists():
                return "pnpm"
            elif (workspace / "yarn.lock").exists():
                return "yarn"
            elif (workspace / "package-lock.json").exists():
                return "npm"
            return "npm"

        # 10. Cargo (Rust)
        if (workspace / "Cargo.toml").exists():
            return "cargo"

        # 11. Go modules
        if (workspace / "go.mod").exists():
            return "go mod"

        return None

    def _analyze_python_style(self, context: ProjectContext) -> None:
        """파이썬 코드 스타일 분석"""
        py_files = list(self.workspace.rglob("*.py"))[:20]  # 최대 20개 파일만

        import_patterns = []
        naming_patterns = {"snake_case": 0, "camelCase": 0, "PascalCase": 0}
        type_hint_count = 0
        total_functions = 0
        async_count = 0

        for py_file in py_files:
            try:
                content = py_file.read_text(encoding="utf-8", errors="ignore")

                # import 스타일
                imports = re.findall(r"^(?:from\s+(\S+)\s+)?import\s+(.+)$", content, re.MULTILINE)
                for from_mod, imported in imports:
                    if from_mod:
                        import_patterns.append(f"from {from_mod} import {imported}")
                    else:
                        import_patterns.append(f"import {imported}")

                # 함수 정의 분석
                funcs = re.findall(
                    r"^\s*(?:async\s+)?def\s+(\w+)\s*\(([^)]*)\)", content, re.MULTILINE
                )
                for func_name, args in funcs:
                    total_functions += 1
                    if func_name.startswith("async "):
                        async_count += 1

                    # 네이밍 컨벤션
                    if "_" in func_name and func_name.islower():
                        naming_patterns["snake_case"] += 1
                    elif func_name[0].islower() and any(c.isupper() for c in func_name):
                        naming_patterns["camelCase"] += 1
                    elif func_name[0].isupper():
                        naming_patterns["PascalCase"] += 1

                    # 타입 힌트
                    if "->" in args or ":" in args:
                        type_hint_count += 1

            except (SyntaxError, UnicodeDecodeError, OSError):
                continue

        # 스타일 결정
        context.import_style = "absolute"  # 기본값
        context.naming_convention = max(naming_patterns, key=naming_patterns.get)
        context.type_hints = (type_hint_count / max(total_functions, 1)) > 0.3
        context.async_pattern = (async_count / max(total_functions, 1)) > 0.1
        context.common_imports = list(set(import_patterns))[:20]

    def _analyze_js_ts_style(self, context: ProjectContext) -> None:
        """JS/TS 코드 스타일 분석"""
        # TODO: 구현
        context.naming_convention = "camelCase"
        context.import_style = "esm"

    def _detect_test_framework(self, language: str) -> str | None:
        """테스트 프레임워크 감지"""
        if language == "python":
            if (self.workspace / "pytest.ini").exists() or (
                self.workspace / "pyproject.toml"
            ).exists():
                content = (
                    (self.workspace / "pyproject.toml").read_text(errors="ignore")
                    if (self.workspace / "pyproject.toml").exists()
                    else ""
                )
                if "pytest" in content:
                    return "pytest"
            return "pytest"  # 기본값
        elif language in ("javascript", "typescript"):
            pkg_json = self.workspace / "package.json"
            if pkg_json.exists():
                import json

                try:
                    data = json.loads(pkg_json.read_text())
                    deps = {
                        **data.get("dependencies", {}),
                        **data.get("devDependencies", {}),
                    }
                    if "vitest" in deps:
                        return "vitest"
                    elif "jest" in deps:
                        return "jest"
                    elif "mocha" in deps:
                        return "mocha"
                except json.JSONDecodeError:
                    pass
        return None

    def _detect_lint_config(self) -> dict[str, Any]:
        """린트 설정 감지"""
        config = {}
        # ruff
        if (self.workspace / "ruff.toml").exists() or (self.workspace / "pyproject.toml").exists():
            config["ruff"] = True
        # mypy
        if (self.workspace / "mypy.ini").exists() or (self.workspace / "pyproject.toml").exists():
            config["mypy"] = True
        # eslint
        if (self.workspace / ".eslintrc.js").exists() or (
            self.workspace / ".eslintrc.json"
        ).exists():
            config["eslint"] = True
        # prettier
        if (self.workspace / ".prettierrc").exists():
            config["prettier"] = True
        return config


class CodeExampleAdapter:
    """코드 예제 변환 및 적용"""

    # 변환 규칙 패턴
    IMPORT_PATTERNS: ClassVar[dict[str, list[tuple[str, str]]]] = {
        "python": [
            (r"^import\s+(\w+)$", "import {0}"),
            (r"^from\s+(\S+)\s+import\s+(.+)$", "from {0} import {1}"),
        ],
        "javascript": [
            (r"^import\s+(.+)\s+from\s+['\"](.+)['\"]$", "import {0} from '{1}'"),
            (
                r"^const\s+(.+)\s+=\s+require\(['\"](.+)['\"]\)$",
                "import {0} from '{1}'",
            ),
        ],
        "typescript": [
            (r"^import\s+(.+)\s+from\s+['\"](.+)['\"]$", "import {0} from '{1}'"),
        ],
    }

    def __init__(self, workspace: str | Path, context: ProjectContext | None = None):
        self.workspace = Path(workspace).resolve()
        self.context = context or ProjectAnalyzer(workspace).analyze()
        self.parser = DocumentationParser()

    def adapt_example(
        self,
        code: str,
        source_docs: Documentation,
        target_file: str | None = None,
        task: ParsedTask | None = None,
    ) -> AdaptedCode:
        """단일 코드 예제 변환"""
        log.info(f"코드 예제 변환: {len(code)} chars")

        # 1. 언어별 기본 변환
        adapted = self._apply_language_transformations(code)

        # 2. 프로젝트 스타일 적용
        adapted = self._apply_project_style(adapted)

        # 3. 컨텍스트 맞춤 변환 (태스크가 있는 경우)
        if task:
            adapted = self._apply_task_context(adapted, task)

        # 4. 타겟 파일 맞춤 변환
        if target_file:
            adapted = self._apply_file_context(adapted, target_file)

        # 5. 설명 생성
        explanation = self._generate_explanation(code, adapted)

        return AdaptedCode(
            original=code,
            adapted=adapted,
            target_file=target_file,
            explanation=explanation,
            confidence=0.85,
        )

    def _apply_language_transformations(self, code: str) -> str:
        """언어별 기본 변환"""
        if self.context.language == "python":
            return self._transform_python(code)
        elif self.context.language in ("javascript", "typescript"):
            return self._transform_js_ts(code)
        return code

    def _transform_python(self, code: str) -> str:
        """파이썬 코드 변환"""
        adapted = code

        # 1. 상대 import → 절대 import (필요시)
        if self.context.import_style == "absolute":
            adapted = re.sub(
                r"^from\s+\.(\.?)\s+import",
                lambda m: f"from {self._get_package_root()}{'.' * len(m.group(1))} import",
                adapted,
                flags=re.MULTILINE,
            )

        # 2. 타입 힌트 추가 (설정되어 있고 없는 경우)
        if self.context.type_hints:
            # 간단한 함수 시그니처에 타입 힌트 추가 로직은 복잡하므로 생략
            pass

        # 3. 비동기 패턴 적용 (프로젝트 설정 또는 코드 내 I/O 패턴 감지)
        should_async = self.context.async_pattern
        if not should_async:
            # 코드 자체에서 I/O 패턴 확인
            io_patterns = [
                "requests.",
                "httpx.",
                "aiohttp.",
                "asyncpg.",
                "redis.",
                "open(",
                "read(",
                "write(",
            ]
            should_async = any(p in adapted for p in io_patterns)

        if should_async and "async def" not in adapted and "def " in adapted:
            # I/O 작업이 보이는 함수에 async 추가 (단순 휴리스틱)
            adapted = re.sub(
                r"^(\s*)def\s+(\w+)(\s*\([^)]*\)):",
                r"\1async def \2\3:",
                adapted,
                flags=re.MULTILINE,
            )

        return adapted

    def _transform_js_ts(self, code: str) -> str:
        """JS/TS 코드 변환"""
        adapted = code

        # require → import 변환
        adapted = re.sub(
            r"const\s+(\w+)\s*=\s*require\(['\"](.+)['\"]\)",
            r"import \1 from '\2'",
            adapted,
        )

        # var/let → const (불변인 경우)
        adapted = re.sub(
            r"^\s*let\s+(\w+)\s*=",
            r"const \1 =",
            adapted,
            flags=re.MULTILINE,
        )

        # 네이밍 컨벤션 적용
        if self.context.naming_convention == "snake_case":
            # camelCase → snake_case (단순화)
            pass

        return adapted

    def _apply_project_style(self, code: str) -> str:
        """프로젝트 스타일 적용"""
        adapted = code

        # 프레임워크별 패턴 적용
        if self.context.framework == "fastapi" and self.context.language == "python":
            adapted = self._apply_fastapi_patterns(adapted)
        elif self.context.framework == "express" and self.context.language in (
            "javascript",
            "typescript",
        ):
            adapted = self._apply_express_patterns(adapted)
        elif self.context.framework == "django" and self.context.language == "python":
            adapted = self._apply_django_patterns(adapted)

        return adapted

    def _apply_fastapi_patterns(self, code: str) -> str:
        """FastAPI 패턴 적용"""
        adapted = code

        # 1. requests → httpx 변환 (모던 비동기 HTTP 클라이언트)
        adapted = re.sub(
            r"\bimport\s+requests\b",
            "import httpx",
            adapted,
        )
        adapted = re.sub(
            r"\bfrom\s+requests\s+import",
            "from httpx import",
            adapted,
        )
        # requests.get/post/put/delete → httpx.AsyncClient().get/post/put/delete
        adapted = re.sub(
            r"\brequests\.get\(",
            "await client.get(",
            adapted,
        )
        adapted = re.sub(
            r"\brequests\.post\(",
            "await client.post(",
            adapted,
        )
        adapted = re.sub(
            r"\brequests\.put\(",
            "await client.put(",
            adapted,
        )
        adapted = re.sub(
            r"\brequests\.delete\(",
            "await client.delete(",
            adapted,
        )
        # response.json() → response.json() (동일)
        # response.text → response.text (동일)

        # 2. Pydantic 모델 사용 패턴
        if "class " in adapted and "BaseModel" not in adapted and "pydantic" not in adapted:
            # 모델 클래스처럼 보이는 것에 BaseModel 상속 제안 (주석으로)
            pass

        # 3. 의존성 주입 패턴
        if "def " in adapted and "Depends" not in adapted:
            # 함수 매개변수에 Depends 추가 제안
            pass

        return adapted

    def _apply_express_patterns(self, code: str) -> str:
        """Express 패턴 적용"""
        return code

    def _apply_django_patterns(self, code: str) -> str:
        """Django 패턴 적용"""
        return code

    def _apply_task_context(self, code: str, task: ParsedTask) -> str:
        """태스크 컨텍스트 적용"""
        adapted = code

        # 태스크 타입별 변환
        if task.task_type.value == "test":
            adapted = self._add_test_structure(adapted)
        elif task.task_type.value == "docs":
            adapted = self._add_docstrings(adapted)

        return adapted

    def _add_test_structure(self, code: str) -> str:
        """테스트 구조 추가"""
        if self.context.test_framework == "pytest" and "def test_" not in code:
            # pytest 스타일로 변환: 함수명을 test_ 접두사 추가
            code = re.sub(
                r"^(\s*)def\s+(\w+)(\s*\([^)]*\)):",
                r"\1def test_\2\3:",
                code,
                flags=re.MULTILINE,
            )
        return code

    def _add_docstrings(self, code: str) -> str:
        """docstring 추가"""
        if self.context.language == "python":
            # Google 스타일 docstring 템플릿 추가
            pass
        return code

    def _apply_file_context(self, code: str, target_file: str) -> str:
        """타겟 파일 컨텍스트 적용"""
        adapted = code

        # 기존 파일 내용 분석
        file_path = self.workspace / target_file
        if file_path.exists():
            try:
                existing = file_path.read_text(encoding="utf-8", errors="ignore")

                # 기존 import 스타일 맞추기
                existing_imports = re.findall(
                    r"^(?:from\s+(\S+)\s+)?import\s+(.+)$", existing, re.MULTILINE
                )
                if existing_imports:
                    # import 순서/스타일 맞춤
                    pass

                # 기존 네이밍 컨벤션 확인
                func_names = re.findall(r"^\s*(?:async\s+)?def\s+(\w+)", existing, re.MULTILINE)
                if func_names:
                    snake_count = sum(1 for n in func_names if "_" in n and n.islower())
                    camel_count = sum(
                        1 for n in func_names if n[0].islower() and any(c.isupper() for c in n)
                    )
                    if camel_count > snake_count:
                        # camelCase로 변환 필요
                        pass
            except (OSError, UnicodeDecodeError):
                pass

        return adapted

    def _generate_explanation(self, original: str, adapted: str) -> str:
        """변경 사항 설명 생성"""
        changes = []
        if original != adapted:
            if "async def" in adapted and "async def" not in original:
                changes.append("비동기 함수로 변환 (I/O 작업 감지)")
            if "import" in adapted and "import" not in original:
                changes.append("import 문 추가/변경")
            if len(adapted) > len(original) * 1.2:
                changes.append("타입 힌트/문서화 추가")
        return "; ".join(changes) if changes else "변경 사항 없음"

    def _get_package_root(self) -> str:
        """패키지 루트 경로 추정"""
        # pyproject.toml에서 name 찾기
        pyproject = self.workspace / "pyproject.toml"
        if pyproject.exists():
            content = pyproject.read_text()
            match = re.search(r'name\s*=\s*["\']([^"\']+)["\']', content)
            if match:
                return match.group(1).replace("-", "_")
        # 디렉토리 이름 사용
        return self.workspace.name.replace("-", "_")


class CodeExampleApplier:
    """변환된 코드를 파일에 적용"""

    def __init__(self, workspace: str | Path):
        self.workspace = Path(workspace).resolve()

    def apply(self, adapted: AdaptedCode, dry_run: bool = False) -> bool:
        """코드 적용"""
        if not adapted.target_file:
            log.warning("타겟 파일이 지정되지 않음")
            return False

        target_path = self.workspace / adapted.target_file
        target_path.parent.mkdir(parents=True, exist_ok=True)

        if dry_run:
            log.info(f"[DRY RUN] {target_path}에 적용 예정")
            return True

        try:
            # 기존 내용 읽기
            existing = ""
            if target_path.exists():
                existing = target_path.read_text(encoding="utf-8")

            # 적용 전략 결정
            if adapted.replace_pattern:
                # 패턴 대체
                new_content = re.sub(
                    adapted.replace_pattern,
                    adapted.adapted,
                    existing,
                    flags=re.MULTILINE | re.DOTALL,
                )
            elif adapted.insert_after:
                # 특정 패턴 뒤에 삽입
                new_content = re.sub(
                    f"({re.escape(adapted.insert_after)})",
                    f"\\1\n\n{adapted.adapted}",
                    existing,
                    flags=re.MULTILINE | re.DOTALL,
                )
            else:
                # 파일 끝에 추가 (기본)
                new_content = existing.rstrip() + f"\n\n{adapted.adapted}\n"

            # 변경사항이 없으면 스킵
            if new_content == existing:
                log.info(f"변경사항 없음: {target_path}")
                return True

            # 백업 후 쓰기
            backup_path = target_path.with_suffix(target_path.suffix + ".bak")
            if target_path.exists():
                target_path.rename(backup_path)

            target_path.write_text(new_content, encoding="utf-8")
            log.info(f"적용 완료: {target_path}")
            return True

        except (OSError, UnicodeError, re.error) as e:
            log.error(f"적용 실패: {target_path} - {e}")
            # 복구
            backup_path = target_path.with_suffix(target_path.suffix + ".bak")
            if backup_path.exists():
                backup_path.rename(target_path)
            return False

    def apply_batch(
        self, adapted_codes: list[AdaptedCode], dry_run: bool = False
    ) -> dict[str, bool]:
        """여러 코드 일괄 적용"""
        results = {}
        for adapted in adapted_codes:
            results[adapted.target_file or "unknown"] = self.apply(adapted, dry_run)
        return results


def adapt_and_apply_examples(
    workspace: str | Path,
    docs: list[Documentation],
    target_files: list[str] | None = None,
    tasks: list[ParsedTask] | None = None,
    dry_run: bool = False,
) -> dict[str, bool]:
    """문서에서 코드 예제 추출 → 변환 → 적용 전체 파이프라인"""
    analyzer = ProjectAnalyzer(workspace)
    context = analyzer.analyze()

    adapter = CodeExampleAdapter(workspace, context)
    applier = CodeExampleApplier(workspace)

    all_adapted = []

    for doc in docs:
        for i, code in enumerate(doc.code_examples):
            # 태스크 매칭 (파일명 기반)
            task = None
            if tasks:
                for t in tasks:
                    if t.target_files and any(f in code.lower() for f in t.target_files):
                        task = t
                        break

            # 타겟 파일 결정
            target_file = None
            if target_files:
                target_file = target_files[0]  # 단순화: 첫 번째 파일에 적용
            elif task and task.target_files:
                target_file = task.target_files[0]

            adapted = adapter.adapt_example(code, doc, target_file, task)
            all_adapted.append(adapted)

    # 적용
    return applier.apply_batch(all_adapted, dry_run)


if __name__ == "__main__":
    # 테스트
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # 가상 프로젝트 생성
        (tmp_path / "pyproject.toml").write_text("""
[project]
name = "myapp"
dependencies = ["fastapi", "pydantic", "httpx"]

[tool.ruff]
line-length = 100
""")

        (tmp_path / "main.py").write_text("""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}
""")

        # 분석 테스트
        analyzer = ProjectAnalyzer(tmp_path)
        context = analyzer.analyze()
        print(f"Language: {context.language}")
        print(f"Framework: {context.framework}")
        print(f"Package manager: {context.package_manager}")
        print(f"Naming: {context.naming_convention}")
        print(f"Type hints: {context.type_hints}")
        print(f"Async pattern: {context.async_pattern}")
