"""
이슈 파싱 및 작업 분해 모듈
GitHub 이슈 본문에서 작업 항목 추출 및 파일 단위 작업 분해
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, ClassVar

log = logging.getLogger("autonomous_coding_agent.issue_parser")


from mutmut.mutation.trampoline import MutantDict
from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated


class TaskType(Enum):
    """작업 유형"""

    CREATE = "create"  # 새 파일 생성
    MODIFY = "modify"  # 기존 파일 수정
    DELETE = "delete"  # 파일 삭제
    REFACTOR = "refactor"  # 리팩토링
    TEST = "test"  # 테스트 작성
    DOCS = "docs"  # 문서화
    CONFIG = "config"  # 설정 변경


class TaskPriority(Enum):
    """작업 우선순위"""

    CRITICAL = 0
    HIGH = 1
    MEDIUM = 2
    LOW = 3


@dataclass
class ParsedTask:
    """파싱된 작업 항목"""

    id: str
    title: str
    description: str
    task_type: TaskType
    priority: TaskPriority
    target_files: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)  # 의존 작업 ID
    estimated_hours: float = 1.0
    acceptance_criteria: list[str] = field(default_factory=list)
    labels: list[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class IssueAnalysis:
    """이슈 분석 결과"""

    issue_number: int
    title: str
    summary: str
    parsed_tasks: list[ParsedTask] = field(default_factory=list)
    suggested_files: list[str] = field(default_factory=list)
    tech_stack_hints: list[str] = field(default_factory=list)
    complexity: str = "medium"  # low, medium, high
    estimated_total_hours: float = 0.0


mutants_xǁIssueParserǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁIssueParserǁ_compile_patterns__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIssueParserǁparse_issue__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIssueParserǁ_extract_summary__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIssueParserǁ_extract_file_hints__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIssueParserǁ_extract_tasks__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIssueParserǁ_parse_task_text__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIssueParserǁ_estimate_hours__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIssueParserǁ_infer_dependencies__mutmut: MutantDict = {}  # type: ignore
mutants_xǁIssueParserǁ_assess_complexity__mutmut: MutantDict = {}  # type: ignore


class IssueParser:
    """이슈 본문 파싱 및 작업 분해"""

    # 기술 스택 키워드 매핑
    TECH_STACK_PATTERNS: ClassVar[dict[str, list[str]]] = {
        "python": [
            "python",
            "py",
            "django",
            "flask",
            "fastapi",
            "pytest",
            "pip",
            "requirements",
        ],
        "javascript": ["javascript", "js", "node", "npm", "react", "vue", "webpack"],
        "typescript": ["typescript", "ts", "tsx"],
        "go": ["golang", "go ", "goroutine", "go.mod"],
        "rust": ["rust", "cargo", "rustc"],
        "java": ["java", "spring", "maven", "gradle"],
        "database": [
            "sql",
            "postgres",
            "mysql",
            "redis",
            "mongodb",
            "orm",
            "migration",
        ],
        "docker": ["docker", "container", "kubernetes", "k8s"],
        "aws": ["aws", "lambda", "ec2", "s3", "rds", "cloudformation"],
        "auth": ["auth", "oauth", "jwt", "login", "register", "password", "token"],
        "api": ["api", "rest", "graphql", "endpoint", "route", "controller"],
        "test": ["test", "pytest", "jest", "unit test", "integration test", "e2e"],
        "ci/cd": ["ci", "cd", "github actions", "gitlab ci", "jenkins", "pipeline"],
    }

    # 작업 유형 키워드
    TASK_TYPE_KEYWORDS: ClassVar[dict[TaskType, list[str]]] = {
        TaskType.CREATE: ["create", "add", "implement", "build", "new", "generate"],
        TaskType.MODIFY: [
            "modify",
            "update",
            "change",
            "fix",
            "refactor",
            "improve",
            "edit",
        ],
        TaskType.DELETE: ["delete", "remove", "drop", "cleanup"],
        TaskType.REFACTOR: ["refactor", "restructure", "reorganize", "clean up"],
        TaskType.TEST: ["test", "unit test", "integration test", "e2e", "coverage"],
        TaskType.DOCS: ["document", "readme", "docstring", "comment", "wiki"],
        TaskType.CONFIG: ["config", "setting", "env", "yaml", "toml", "ini", "dotenv"],
    }

    # 파일 유형 추론 패턴
    FILE_TYPE_PATTERNS: ClassVar[dict[str, list[str]]] = {
        "model": ["model", "entity", "schema", "database", "orm"],
        "service": ["service", "business logic", "business rule"],
        "controller": ["controller", "handler", "endpoint", "route", "api"],
        "repository": ["repository", "dao", "data access", "query"],
        "dto": ["dto", "request", "response", "schema", "payload"],
        "util": ["util", "helper", "common", "shared"],
        "config": ["config", "setting", "configuration"],
        "test": ["test", "spec", "mock", "fixture"],
        "middleware": ["middleware", "interceptor", "filter"],
        "auth": ["auth", "authentication", "authorization", "login", "jwt", "token"],
    }

    @_mutmut_mutated(mutants_xǁIssueParserǁ__init____mutmut)
    def __init__(self):
        self._compiled_patterns = self._compile_patterns()

    def xǁIssueParserǁ__init____mutmut_orig(self):
        self._compiled_patterns = self._compile_patterns()

    def xǁIssueParserǁ__init____mutmut_1(self):
        self._compiled_patterns = None

    @_mutmut_mutated(mutants_xǁIssueParserǁ_compile_patterns__mutmut)
    def _compile_patterns(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_orig(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_1(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = None

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_2(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = None
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_3(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) - r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_4(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" - "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_5(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"XX\b(XX" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_6(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(None) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_7(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "XX|XX".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_8(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(None) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_9(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r"XX)\bXX"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_10(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = None

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_11(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(None, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_12(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, None)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_13(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_14(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(
                pattern,
            )

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_15(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = None
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_16(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) - r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_17(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" - "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_18(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"XX\b(XX" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_19(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(None) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_20(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "XX|XX".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_21(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(None) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_22(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r"XX)\bXX"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_23(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = None

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_24(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(None, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_25(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, None)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_26(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_27(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(
                pattern,
            )

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_28(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = None
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_29(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) - r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_30(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" - "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_31(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"XX\b(XX" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_32(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(None) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_33(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "XX|XX".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_34(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(None) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_35(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r"XX)\bXX"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_36(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = None

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_37(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(None, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_38(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, None)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_39(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_40(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(
                pattern,
            )

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_41(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = None

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_42(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["XXtask_itemsXX"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_43(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["TASK_ITEMS"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_44(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            None,
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_45(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            None,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_46(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_47(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_48(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"XX(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)XX",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_49(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE & re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_50(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = None
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_51(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["XXcode_blocksXX"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_52(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["CODE_BLOCKS"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_53(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(None)
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_54(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"XX`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`XX"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_55(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:PY|JS|TS|TSX|GO|RS|JAVA|YML|YAML|JSON|TOML|INI|MD|TXT|SQL))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_56(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = None

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_57(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["XXfile_mentionsXX"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_58(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["FILE_MENTIONS"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_59(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(None)

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_60(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"XX(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-zA-Z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)XX"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_61(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`|\b([a-za-z_][\w/.-]*\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))\b)"
        )

        return patterns

    def xǁIssueParserǁ_compile_patterns__mutmut_62(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(pattern, re.IGNORECASE)

        # 기술 스택 패턴
        for stack, keywords in self.TECH_STACK_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"tech_{stack}"] = re.compile(pattern, re.IGNORECASE)

        # 파일 유형 패턴
        for file_type, keywords in self.FILE_TYPE_PATTERNS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"file_{file_type}"] = re.compile(pattern, re.IGNORECASE)

        # 작업 항목 추출 패턴 (불릿 포인트, 번호 목록 등)
        patterns["task_items"] = re.compile(
            r"(?:^|\n)\s*[-*•\d+\.]\s*(.+?)(?=\n\s*[-*•\d+\.]|\n\n|$)",
            re.MULTILINE | re.DOTALL,
        )

        # 코드 블록/파일명 패턴
        patterns["code_blocks"] = re.compile(
            r"`([^`]+\.(?:py|js|ts|tsx|go|rs|java|yml|yaml|json|toml|ini|md|txt|sql))`"
        )
        patterns["file_mentions"] = re.compile(
            r"(?:`([^`]+\.(?:PY|JS|TS|TSX|GO|RS|JAVA|YML|YAML|JSON|TOML|INI|MD|TXT|SQL))`|\b([A-ZA-Z_][\w/.-]*\.(?:PY|JS|TS|TSX|GO|RS|JAVA|YML|YAML|JSON|TOML|INI|MD|TXT|SQL))\b)"
        )

        return patterns

    @_mutmut_mutated(mutants_xǁIssueParserǁparse_issue__mutmut)
    def parse_issue(self, issue_number: int, title: str, body: str) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_orig(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_1(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(None)

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_2(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = None

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_3(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=None,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_4(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=None,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_5(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=None,
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_6(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_7(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_8(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_9(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(None),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_10(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = None

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_11(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(None)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_12(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = None

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_13(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(None)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_14(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = None

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_15(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(None)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_16(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(None)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_17(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = None
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_18(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(None)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_19(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = None

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_20(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(None)

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def xǁIssueParserǁparse_issue__mutmut_21(
        self, issue_number: int, title: str, body: str
    ) -> IssueAnalysis:
        """이슈 본문 파싱 및 작업 분해"""
        log.info(f"이슈 #{issue_number} 파싱 시작")

        analysis = IssueAnalysis(
            issue_number=issue_number,
            title=title,
            summary=self._extract_summary(body),
        )

        # 1. 기술 스택 힌트 추출
        analysis.tech_stack_hints = self._extract_tech_stack(body)

        # 2. 파일 유형 힌트 추출
        analysis.suggested_files = self._extract_file_hints(body)

        # 3. 작업 항목 추출
        analysis.parsed_tasks = self._extract_tasks(body)

        # 4. 작업 간 의존성 추론
        self._infer_dependencies(analysis.parsed_tasks)

        # 5. 복잡도 및 예상 시간 계산
        analysis.complexity = self._assess_complexity(analysis.parsed_tasks)
        analysis.estimated_total_hours = sum(t.estimated_hours for t in analysis.parsed_tasks)

        log.info(None)

        return analysis

    @_mutmut_mutated(mutants_xǁIssueParserǁ_extract_summary__mutmut)
    def _extract_summary(self, body: str) -> str:
        """본문에서 요약 추출 (첫 문단 또는 첫 200자)"""
        paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
        if paragraphs:
            return paragraphs[0][:200]
        return body[:200]

    def xǁIssueParserǁ_extract_summary__mutmut_orig(self, body: str) -> str:
        """본문에서 요약 추출 (첫 문단 또는 첫 200자)"""
        paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
        if paragraphs:
            return paragraphs[0][:200]
        return body[:200]

    def xǁIssueParserǁ_extract_summary__mutmut_1(self, body: str) -> str:
        """본문에서 요약 추출 (첫 문단 또는 첫 200자)"""
        paragraphs = None
        if paragraphs:
            return paragraphs[0][:200]
        return body[:200]

    def xǁIssueParserǁ_extract_summary__mutmut_2(self, body: str) -> str:
        """본문에서 요약 추출 (첫 문단 또는 첫 200자)"""
        paragraphs = [p.strip() for p in body.split(None) if p.strip()]
        if paragraphs:
            return paragraphs[0][:200]
        return body[:200]

    def xǁIssueParserǁ_extract_summary__mutmut_3(self, body: str) -> str:
        """본문에서 요약 추출 (첫 문단 또는 첫 200자)"""
        paragraphs = [p.strip() for p in body.split("XX\n\nXX") if p.strip()]
        if paragraphs:
            return paragraphs[0][:200]
        return body[:200]

    def xǁIssueParserǁ_extract_summary__mutmut_4(self, body: str) -> str:
        """본문에서 요약 추출 (첫 문단 또는 첫 200자)"""
        paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
        if paragraphs:
            return paragraphs[1][:200]
        return body[:200]

    def xǁIssueParserǁ_extract_summary__mutmut_5(self, body: str) -> str:
        """본문에서 요약 추출 (첫 문단 또는 첫 200자)"""
        paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
        if paragraphs:
            return paragraphs[0][:201]
        return body[:200]

    def xǁIssueParserǁ_extract_summary__mutmut_6(self, body: str) -> str:
        """본문에서 요약 추출 (첫 문단 또는 첫 200자)"""
        paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
        if paragraphs:
            return paragraphs[0][:200]
        return body[:201]

    @_mutmut_mutated(mutants_xǁIssueParserǁ_extract_tech_stack__mutmut)
    def _extract_tech_stack(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(body_lower):
                found.append(stack.replace("tech_", ""))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_orig(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(body_lower):
                found.append(stack.replace("tech_", ""))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_1(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = None
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(body_lower):
                found.append(stack.replace("tech_", ""))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_2(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = None
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(body_lower):
                found.append(stack.replace("tech_", ""))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_3(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.upper()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(body_lower):
                found.append(stack.replace("tech_", ""))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_4(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") or pattern.search(body_lower):
                found.append(stack.replace("tech_", ""))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_5(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith(None) and pattern.search(body_lower):
                found.append(stack.replace("tech_", ""))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_6(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("XXtech_XX") and pattern.search(body_lower):
                found.append(stack.replace("tech_", ""))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_7(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("TECH_") and pattern.search(body_lower):
                found.append(stack.replace("tech_", ""))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_8(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(None):
                found.append(stack.replace("tech_", ""))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_9(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(body_lower):
                found.append(None)
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_10(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(body_lower):
                found.append(stack.replace(None, ""))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_11(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(body_lower):
                found.append(stack.replace("tech_", None))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_12(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(body_lower):
                found.append(stack.replace(""))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_13(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(body_lower):
                found.append(
                    stack.replace(
                        "tech_",
                    )
                )
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_14(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(body_lower):
                found.append(stack.replace("XXtech_XX", ""))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_15(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(body_lower):
                found.append(stack.replace("TECH_", ""))
        return found

    def xǁIssueParserǁ_extract_tech_stack__mutmut_16(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(body_lower):
                found.append(stack.replace("tech_", "XXXX"))
        return found

    @_mutmut_mutated(mutants_xǁIssueParserǁ_extract_file_hints__mutmut)
    def _extract_file_hints(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(1) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_orig(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(1) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_1(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = None

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(1) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_2(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(None):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(1) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_3(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["XXcode_blocksXX"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(1) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_4(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["CODE_BLOCKS"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(1) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_5(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(None)

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(1) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_6(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(None))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(1) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_7(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(2))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(1) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_8(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(None):
            file_name = match.group(1) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_9(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["XXfile_mentionsXX"].finditer(body):
            file_name = match.group(1) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_10(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["FILE_MENTIONS"].finditer(body):
            file_name = match.group(1) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_11(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = None
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_12(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(1) and match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_13(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(None) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_14(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(2) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_15(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(1) or match.group(None)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_16(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(1) or match.group(3)
            if file_name:
                files.add(file_name)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_17(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(1) or match.group(2)
            if file_name:
                files.add(None)

        return sorted(files)

    def xǁIssueParserǁ_extract_file_hints__mutmut_18(self, body: str) -> list[str]:
        """파일/모듈 힌트 추출"""
        files = set()

        # 코드 블록 내 파일명
        for match in self._compiled_patterns["code_blocks"].finditer(body):
            files.add(match.group(1))

        # 본문 내 파일명 언급 (백틱 안 또는 일반 텍스트)
        for match in self._compiled_patterns["file_mentions"].finditer(body):
            file_name = match.group(1) or match.group(2)
            if file_name:
                files.add(file_name)

        return sorted(None)

    @_mutmut_mutated(mutants_xǁIssueParserǁ_extract_tasks__mutmut)
    def _extract_tasks(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_orig(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_1(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = None
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_2(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = None

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_3(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 1

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_4(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(None):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_5(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["XXtask_itemsXX"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_6(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["TASK_ITEMS"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_7(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = None
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_8(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(None).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_9(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(2).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_10(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) <= 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_11(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 11:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_12(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                break

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_13(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = None
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_14(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(None, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_15(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, None)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_16(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_17(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(
                task_text,
            )
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_18(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(None)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_19(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter = 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_20(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter -= 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_21(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 2

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_22(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_23(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = None
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_24(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(None, body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_25(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", None)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_26(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_27(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(
                r"[.!?]\s+",
            )
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_28(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.rsplit(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_29(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"XX[.!?]\s+XX", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_30(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = None
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_31(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) <= 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_32(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 16:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_33(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    break
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_34(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = None
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_35(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(None, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_36(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, None)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_37(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_38(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(
                    sent,
                )
                if task:
                    tasks.append(task)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_39(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(None)
                    task_id_counter += 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_40(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter = 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_41(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter -= 1

        return tasks

    def xǁIssueParserǁ_extract_tasks__mutmut_42(self, body: str) -> list[ParsedTask]:
        """작업 항목 추출"""
        tasks = []
        task_id_counter = 0

        # 1. 불릿 포인트/번호 목록에서 작업 추출
        for match in self._compiled_patterns["task_items"].finditer(body):
            task_text = match.group(1).strip()
            if len(task_text) < 10:  # 너무 짧은 건 제외
                continue

            task = self._parse_task_text(task_text, task_id_counter)
            if task:
                tasks.append(task)
                task_id_counter += 1

        # 2. 문장 단위로 작업 추출 (불릿 포인트가 없는 경우)
        if not tasks:
            sentences = re.split(r"[.!?]\s+", body)
            for sent in sentences:
                sent = sent.strip()
                if len(sent) < 15:
                    continue
                task = self._parse_task_text(sent, task_id_counter)
                if task:
                    tasks.append(task)
                    task_id_counter += 2

        return tasks

    @_mutmut_mutated(mutants_xǁIssueParserǁ_parse_task_text__mutmut)
    def _parse_task_text(self, text: str, task_id: int) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_orig(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_1(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = None  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_2(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = None

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_3(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.upper()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_4(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") or pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_5(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith(None) and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_6(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("XXtask_type_XX") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_7(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("TASK_TYPE_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_8(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(None):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_9(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = None
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_10(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(None)
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_11(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace(None, ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_12(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", None))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_13(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace(""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_14(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(
                    task_type_enum.replace(
                        "task_type_",
                    )
                )
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_15(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("XXtask_type_XX", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_16(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("TASK_TYPE_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_17(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", "XXXX"))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_18(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                return

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_19(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = None
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_20(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(None):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_21(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w not in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_22(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["XXcriticalXX", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_23(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["CRITICAL", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_24(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "XXurgentXX", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_25(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "URGENT", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_26(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "XX긴급XX", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_27(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "XX즉시XX"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_28(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = None
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_29(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(None):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_30(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w not in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_31(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["XXhighXX", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_32(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["HIGH", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_33(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "XX중요XX", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_34(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "XX높음XX"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_35(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = None
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_36(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(None):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_37(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w not in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_38(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["XXlowXX", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_39(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["LOW", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_40(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "XX낮음XX", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_41(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "XX나중에XX"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_42(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = None

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_43(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = None
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_44(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(None):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_45(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["XXfile_mentionsXX"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_46(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["FILE_MENTIONS"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_47(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = None
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_48(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) and match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_49(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(None) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_50(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(2) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_51(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(None)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_52(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(3)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_53(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(None)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_54(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(None):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_55(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["XXcode_blocksXX"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_56(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["CODE_BLOCKS"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_57(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(None) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_58(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(2) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_59(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_60(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(None)

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_61(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(None))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_62(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(2))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_63(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_64(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = None

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_65(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(None, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_66(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, None)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_67(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_68(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(
                text,
            )

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_69(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = None

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_70(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(None, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_71(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, None)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_72(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_73(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(
            text,
        )

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_74(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = None

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_75(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(None)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_76(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=None,
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_77(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=None,
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_78(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=None,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_79(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=None,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_80(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=None,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_81(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=None,
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_82(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=None,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_83(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=None,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_84(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_85(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_86(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_87(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_88(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_89(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_90(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_91(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_92(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:101],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(target_files)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_93(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(None),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    def xǁIssueParserǁ_parse_task_text__mutmut_94(
        self, text: str, task_id: int
    ) -> ParsedTask | None:
        """텍스트에서 작업 파싱"""
        # 작업 유형 판별
        task_type = TaskType.CREATE  # 기본값
        text_lower = text.lower()

        for task_type_enum, pattern in self._compiled_patterns.items():
            if task_type_enum.startswith("task_type_") and pattern.search(text_lower):
                task_type = TaskType(task_type_enum.replace("task_type_", ""))
                break

        # 우선순위 판별
        priority = TaskPriority.MEDIUM
        if any(w in text_lower for w in ["critical", "urgent", "긴급", "즉시"]):
            priority = TaskPriority.CRITICAL
        elif any(w in text_lower for w in ["high", "중요", "높음"]):
            priority = TaskPriority.HIGH
        elif any(w in text_lower for w in ["low", "낮음", "나중에"]):
            priority = TaskPriority.LOW

        # 대상 파일 추출
        target_files = []
        for match in self._compiled_patterns["file_mentions"].finditer(text):
            # group(1)은 백틱 안의 파일명, group(2)는 일반 파일명
            file_name = match.group(1) or match.group(2)
            if file_name:
                target_files.append(file_name)

        # 기술 스택 기반 파일 추론
        for match in self._compiled_patterns["code_blocks"].finditer(text):
            if match.group(1) not in target_files:
                target_files.append(match.group(1))

        # 작업 유형에 따른 기본 파일 추론
        if not target_files:
            target_files = self._infer_files_from_task_type(text, task_type)

        # 예상 시간 계산
        estimated_hours = self._estimate_hours(text, task_type)

        # 승인 기준 추출
        acceptance_criteria = self._extract_acceptance_criteria(text)

        return ParsedTask(
            id=f"task_{task_id}",
            title=text[:100],
            description=text,
            task_type=task_type,
            priority=priority,
            target_files=list(set(None)),
            estimated_hours=estimated_hours,
            acceptance_criteria=acceptance_criteria,
        )

    @_mutmut_mutated(mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut)
    def _infer_files_from_task_type(self, text: str, task_type: TaskType) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_orig(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_1(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = None
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_2(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = None

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_3(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.upper()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_4(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") or pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_5(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith(None) and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_6(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("XXfile_XX") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_7(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("FILE_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_8(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(None):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_9(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(None)

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_10(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace(None, ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_11(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", None))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_12(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace(""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_13(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(
                    file_type.replace(
                        "file_",
                    )
                )

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_14(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("XXfile_XX", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_15(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("FILE_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_16(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", "XXXX"))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_17(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST or "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_18(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type != TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_19(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "XXtestXX" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_20(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "TEST" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_21(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_22(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append(None)
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_23(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("XXtestXX")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_24(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("TEST")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_25(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG or "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_26(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type != TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_27(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "XXconfigXX" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_28(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "CONFIG" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_29(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_30(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append(None)
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_31(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("XXconfigXX")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_32(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("CONFIG")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_33(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS or "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_34(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type != TaskType.DOCS and "docs" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_35(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "XXdocsXX" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_36(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "DOCS" not in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_37(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" in files:
            files.append("docs")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_38(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append(None)

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_39(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("XXdocsXX")

        return files

    def xǁIssueParserǁ_infer_files_from_task_type__mutmut_40(
        self, text: str, task_type: TaskType
    ) -> list[str]:
        """작업 유형에서 파일 유형 추론"""
        files = []
        text_lower = text.lower()

        for file_type, pattern in self._compiled_patterns.items():
            if file_type.startswith("file_") and pattern.search(text_lower):
                files.append(file_type.replace("file_", ""))

        # 작업 유형별 기본 파일
        if task_type == TaskType.TEST and "test" not in files:
            files.append("test")
        elif task_type == TaskType.CONFIG and "config" not in files:
            files.append("config")
        elif task_type == TaskType.DOCS and "docs" not in files:
            files.append("DOCS")

        return files

    @_mutmut_mutated(mutants_xǁIssueParserǁ_estimate_hours__mutmut)
    def _estimate_hours(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_orig(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_1(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = None

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_2(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 4.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_3(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 3.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_4(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 5.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_5(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 3.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_6(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 2.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_7(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 2.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_8(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 1.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_9(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = None

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_10(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(None, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_11(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_12(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_13(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(
            task_type,
        )

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_14(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 3.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_15(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = None
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_16(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.upper()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_17(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(None):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_18(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w not in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_19(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["XXcomplexXX", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_20(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["COMPLEX", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_21(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "XX복잡XX", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_22(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "XXcomplexXX"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_23(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "COMPLEX"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_24(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base = 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_25(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base /= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_26(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 2.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_27(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(None):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_28(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w not in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_29(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["XXsimpleXX", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_30(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["SIMPLE", "간단", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_31(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "XX간단XX", "simple"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_32(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "XXsimpleXX"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_33(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "SIMPLE"]):
            base *= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_34(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base = 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_35(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base /= 0.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_36(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]) or any(
            w in text_lower for w in ["simple", "간단", "simple"]
        ):
            base *= 1.5

        return round(base, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_37(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(None, 1)

    def xǁIssueParserǁ_estimate_hours__mutmut_38(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, None)

    def xǁIssueParserǁ_estimate_hours__mutmut_39(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(1)

    def xǁIssueParserǁ_estimate_hours__mutmut_40(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(
            base,
        )

    def xǁIssueParserǁ_estimate_hours__mutmut_41(self, text: str, task_type: TaskType) -> float:
        """예상 소요 시간 계산"""
        base_hours = {
            TaskType.CREATE: 3.0,
            TaskType.MODIFY: 2.0,
            TaskType.REFACTOR: 4.0,
            TaskType.TEST: 2.0,
            TaskType.DOCS: 1.0,
            TaskType.CONFIG: 1.0,
            TaskType.DELETE: 0.5,
        }

        base = base_hours.get(task_type, 2.0)

        # 복잡도 키워드로 조정
        text_lower = text.lower()
        if any(w in text_lower for w in ["complex", "복잡", "complex"]):
            base *= 1.5
        elif any(w in text_lower for w in ["simple", "간단", "simple"]):
            base *= 0.5

        return round(base, 2)

    @_mutmut_mutated(mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut)
    def _extract_acceptance_criteria(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                criteria.append(match.group(1).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_orig(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                criteria.append(match.group(1).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_1(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = None

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                criteria.append(match.group(1).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_2(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = None

        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                criteria.append(match.group(1).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_3(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"XX(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)XX",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                criteria.append(match.group(1).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_4(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:ACCEPTANCE|승인|기준|CRITERIA)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                criteria.append(match.group(1).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_5(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"XX(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)XX",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                criteria.append(match.group(1).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_6(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|MUST|SHOULD|SHALL)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                criteria.append(match.group(1).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_7(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(None, text, re.IGNORECASE):
                criteria.append(match.group(1).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_8(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, None, re.IGNORECASE):
                criteria.append(match.group(1).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_9(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text, None):
                criteria.append(match.group(1).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_10(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(text, re.IGNORECASE):
                criteria.append(match.group(1).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_11(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, re.IGNORECASE):
                criteria.append(match.group(1).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_12(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(
                pattern,
                text,
            ):
                criteria.append(match.group(1).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_13(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                criteria.append(None)

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_14(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                criteria.append(match.group(None).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_15(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                criteria.append(match.group(2).strip())

        return criteria[:5]  # 최대 5개

    def xǁIssueParserǁ_extract_acceptance_criteria__mutmut_16(self, text: str) -> list[str]:
        """승인 기준 추출"""
        criteria = []

        # 명시적 기준 패턴
        patterns = [
            r"(?:acceptance|승인|기준|criteria)[\s:]+(.+?)(?:\n|$)",
            r"(?:해야|must|should|shall)[\s]+(.+?)(?:\n|$)",
        ]

        for pattern in patterns:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                criteria.append(match.group(1).strip())

        return criteria[:6]  # 최대 5개

    @_mutmut_mutated(mutants_xǁIssueParserǁ_infer_dependencies__mutmut)
    def _infer_dependencies(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_orig(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_1(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = None
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_2(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_3(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = None
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_4(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(None)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_5(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) >= 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_6(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 2:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_7(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = None
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_8(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 1,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_9(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 2,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_10(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 3,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_11(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 4,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_12(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 5,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_13(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 6,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_14(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 7,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_15(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=None)
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_16(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: None)
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_17(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(None, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_18(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_19(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_20(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(
                    key=lambda t: type_order.get(
                        t.task_type,
                    )
                )
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_21(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 100))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_22(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(None):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_23(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) + 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_24(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 2):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_25(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i - 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_26(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 2].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_27(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_28(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(None)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_29(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i - 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_30(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 2].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_31(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = None

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_32(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "XXmodelXX": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_33(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "MODEL": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_34(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 1,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_35(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "XXdtoXX": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_36(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "DTO": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_37(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 2,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_38(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "XXrepositoryXX": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_39(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "REPOSITORY": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_40(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 3,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_41(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "XXserviceXX": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_42(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "SERVICE": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_43(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 4,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_44(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "XXauthXX": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_45(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "AUTH": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_46(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 5,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_47(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "XXsecurityXX": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_48(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "SECURITY": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_49(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 5,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_50(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "XXutilXX": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_51(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "UTIL": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_52(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 5,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_53(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "XXmiddlewareXX": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_54(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "MIDDLEWARE": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_55(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 5,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_56(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "XXcontrollerXX": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_57(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "CONTROLLER": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_58(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 6,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_59(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "XXapiXX": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_60(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "API": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_61(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 6,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_62(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "XXconfigXX": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_63(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "CONFIG": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_64(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 7,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_65(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "XXtestXX": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_66(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "TEST": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_67(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 8,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_68(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "XXdocsXX": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_69(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "DOCS": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_70(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 9,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_71(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = None
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_72(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = None
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_73(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 100
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_74(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = None
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_75(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.upper()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_76(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key not in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_77(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = None
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_78(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(None, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_79(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, None)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_80(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_81(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(
                            layer,
                        )
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_82(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = None

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_83(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    or task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_84(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    or not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_85(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    or task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_86(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id == other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_87(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] <= task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_88(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_89(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) | set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_90(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(None) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_91(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(None)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_92(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id in other.dependencies
                ):
                    other.dependencies.append(task.id)

    def xǁIssueParserǁ_infer_dependencies__mutmut_93(self, tasks: list[ParsedTask]) -> None:
        """작업 간 의존성 추론"""
        # 파일별 작업 매핑
        file_to_tasks: dict[str, list[ParsedTask]] = {}
        for task in tasks:
            for f in task.target_files:
                if f not in file_to_tasks:
                    file_to_tasks[f] = []
                file_to_tasks[f].append(task)

        # 1. 같은 파일 내 순서: CREATE -> MODIFY -> TEST -> DOCS
        for file_tasks in file_to_tasks.values():
            if len(file_tasks) > 1:
                type_order = {
                    TaskType.CREATE: 0,
                    TaskType.MODIFY: 1,
                    TaskType.REFACTOR: 2,
                    TaskType.TEST: 3,
                    TaskType.DOCS: 4,
                    TaskType.CONFIG: 5,
                    TaskType.DELETE: 6,
                }
                file_tasks.sort(key=lambda t: type_order.get(t.task_type, 99))
                for i in range(len(file_tasks) - 1):
                    if file_tasks[i + 1].id not in file_tasks[i].dependencies:
                        file_tasks[i].dependencies.append(file_tasks[i + 1].id)

        # 2. 파일 간 의존성: 모델 -> 서비스 -> 컨트롤러 -> 테스트
        layer_order = {
            "model": 0,
            "dto": 1,
            "repository": 2,
            "service": 3,
            "auth": 4,
            "security": 4,
            "util": 4,
            "middleware": 4,
            "controller": 5,
            "api": 5,
            "config": 6,
            "test": 7,
            "docs": 8,
        }

        # 각 작업의 레이어 결정
        task_layers = {}
        for task in tasks:
            layer = 99
            for f in task.target_files:
                f_lower = f.lower()
                for key, val in layer_order.items():
                    if key in f_lower:
                        layer = min(layer, val)
            task_layers[task.id] = layer

        # 레이어 순서대로 의존성 추가 (낮은 레이어가 높은 레이어의 전제조건)
        for task in tasks:
            for other in tasks:
                if (
                    task.id != other.id
                    and task_layers[task.id] < task_layers[other.id]
                    and not set(task.target_files) & set(other.target_files)
                    and task.id not in other.dependencies
                ):
                    other.dependencies.append(None)

    @_mutmut_mutated(mutants_xǁIssueParserǁ_assess_complexity__mutmut)
    def _assess_complexity(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_orig(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_1(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = None
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_2(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(None)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_3(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = None

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_4(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 and num_files > 10:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_5(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours >= 20 or num_files > 10:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_6(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 21 or num_files > 10:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_7(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files >= 10:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_8(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 11:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_9(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "XXhighXX"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_10(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "HIGH"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_11(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours > 8 and num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_12(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours >= 8 or num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_13(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours > 9 or num_files > 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_14(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours > 8 or num_files >= 5:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_15(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours > 8 or num_files > 6:
            return "medium"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_16(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "XXmediumXX"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_17(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "MEDIUM"
        return "low"

    def xǁIssueParserǁ_assess_complexity__mutmut_18(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "XXlowXX"

    def xǁIssueParserǁ_assess_complexity__mutmut_19(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "LOW"


mutants_xǁIssueParserǁ__init____mutmut["_mutmut_orig"] = IssueParser.xǁIssueParserǁ__init____mutmut_orig  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ__init____mutmut["xǁIssueParserǁ__init____mutmut_1"] = IssueParser.xǁIssueParserǁ__init____mutmut_1  # type: ignore # mutmut generated

mutants_xǁIssueParserǁ_compile_patterns__mutmut["_mutmut_orig"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_1"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_1  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_2"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_2  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_3"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_3  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_4"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_4  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_5"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_5  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_6"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_6  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_7"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_7  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_8"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_8  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_9"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_9  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_10"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_10  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_11"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_11  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_12"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_12  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_13"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_13  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_14"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_14  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_15"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_15  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_16"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_16  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_17"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_17  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_18"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_18  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_19"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_19  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_20"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_20  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_21"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_21  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_22"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_22  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_23"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_23  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_24"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_24  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_25"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_25  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_26"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_26  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_27"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_27  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_28"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_28  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_29"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_29  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_30"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_30  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_31"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_31  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_32"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_32  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_33"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_33  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_34"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_34  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_35"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_35  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_36"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_36  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_37"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_37  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_38"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_38  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_39"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_39  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_40"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_40  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_41"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_41  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_42"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_42  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_43"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_43  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_44"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_44  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_45"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_45  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_46"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_46  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_47"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_47  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_48"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_48  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_49"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_49  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_50"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_50  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_51"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_51  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_52"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_52  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_53"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_53  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_54"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_54  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_55"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_55  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_56"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_56  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_57"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_57  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_58"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_58  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_59"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_59  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_60"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_60  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_61"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_61  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_compile_patterns__mutmut["xǁIssueParserǁ_compile_patterns__mutmut_62"] = IssueParser.xǁIssueParserǁ_compile_patterns__mutmut_62  # type: ignore # mutmut generated

mutants_xǁIssueParserǁparse_issue__mutmut["_mutmut_orig"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_1"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_1  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_2"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_2  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_3"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_3  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_4"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_4  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_5"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_5  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_6"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_6  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_7"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_7  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_8"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_8  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_9"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_9  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_10"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_10  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_11"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_11  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_12"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_12  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_13"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_13  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_14"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_14  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_15"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_15  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_16"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_16  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_17"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_17  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_18"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_18  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_19"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_19  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_20"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_20  # type: ignore # mutmut generated
mutants_xǁIssueParserǁparse_issue__mutmut["xǁIssueParserǁparse_issue__mutmut_21"] = IssueParser.xǁIssueParserǁparse_issue__mutmut_21  # type: ignore # mutmut generated

mutants_xǁIssueParserǁ_extract_summary__mutmut["_mutmut_orig"] = IssueParser.xǁIssueParserǁ_extract_summary__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_summary__mutmut["xǁIssueParserǁ_extract_summary__mutmut_1"] = IssueParser.xǁIssueParserǁ_extract_summary__mutmut_1  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_summary__mutmut["xǁIssueParserǁ_extract_summary__mutmut_2"] = IssueParser.xǁIssueParserǁ_extract_summary__mutmut_2  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_summary__mutmut["xǁIssueParserǁ_extract_summary__mutmut_3"] = IssueParser.xǁIssueParserǁ_extract_summary__mutmut_3  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_summary__mutmut["xǁIssueParserǁ_extract_summary__mutmut_4"] = IssueParser.xǁIssueParserǁ_extract_summary__mutmut_4  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_summary__mutmut["xǁIssueParserǁ_extract_summary__mutmut_5"] = IssueParser.xǁIssueParserǁ_extract_summary__mutmut_5  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_summary__mutmut["xǁIssueParserǁ_extract_summary__mutmut_6"] = IssueParser.xǁIssueParserǁ_extract_summary__mutmut_6  # type: ignore # mutmut generated

mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["_mutmut_orig"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_1"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_1  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_2"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_2  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_3"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_3  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_4"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_4  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_5"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_5  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_6"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_6  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_7"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_7  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_8"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_8  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_9"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_9  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_10"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_10  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_11"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_11  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_12"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_12  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_13"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_13  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_14"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_14  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_15"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_15  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tech_stack__mutmut["xǁIssueParserǁ_extract_tech_stack__mutmut_16"] = IssueParser.xǁIssueParserǁ_extract_tech_stack__mutmut_16  # type: ignore # mutmut generated

mutants_xǁIssueParserǁ_extract_file_hints__mutmut["_mutmut_orig"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_1"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_1  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_2"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_2  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_3"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_3  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_4"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_4  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_5"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_5  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_6"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_6  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_7"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_7  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_8"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_8  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_9"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_9  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_10"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_10  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_11"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_11  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_12"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_12  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_13"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_13  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_14"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_14  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_15"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_15  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_16"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_16  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_17"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_17  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_file_hints__mutmut["xǁIssueParserǁ_extract_file_hints__mutmut_18"] = IssueParser.xǁIssueParserǁ_extract_file_hints__mutmut_18  # type: ignore # mutmut generated

mutants_xǁIssueParserǁ_extract_tasks__mutmut["_mutmut_orig"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_1"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_1  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_2"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_2  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_3"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_3  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_4"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_4  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_5"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_5  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_6"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_6  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_7"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_7  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_8"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_8  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_9"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_9  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_10"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_10  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_11"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_11  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_12"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_12  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_13"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_13  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_14"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_14  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_15"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_15  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_16"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_16  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_17"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_17  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_18"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_18  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_19"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_19  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_20"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_20  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_21"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_21  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_22"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_22  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_23"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_23  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_24"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_24  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_25"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_25  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_26"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_26  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_27"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_27  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_28"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_28  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_29"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_29  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_30"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_30  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_31"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_31  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_32"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_32  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_33"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_33  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_34"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_34  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_35"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_35  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_36"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_36  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_37"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_37  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_38"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_38  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_39"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_39  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_40"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_40  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_41"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_41  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_tasks__mutmut["xǁIssueParserǁ_extract_tasks__mutmut_42"] = IssueParser.xǁIssueParserǁ_extract_tasks__mutmut_42  # type: ignore # mutmut generated

mutants_xǁIssueParserǁ_parse_task_text__mutmut["_mutmut_orig"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_1"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_1  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_2"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_2  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_3"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_3  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_4"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_4  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_5"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_5  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_6"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_6  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_7"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_7  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_8"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_8  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_9"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_9  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_10"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_10  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_11"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_11  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_12"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_12  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_13"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_13  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_14"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_14  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_15"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_15  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_16"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_16  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_17"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_17  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_18"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_18  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_19"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_19  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_20"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_20  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_21"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_21  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_22"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_22  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_23"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_23  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_24"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_24  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_25"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_25  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_26"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_26  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_27"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_27  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_28"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_28  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_29"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_29  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_30"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_30  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_31"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_31  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_32"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_32  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_33"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_33  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_34"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_34  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_35"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_35  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_36"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_36  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_37"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_37  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_38"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_38  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_39"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_39  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_40"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_40  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_41"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_41  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_42"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_42  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_43"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_43  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_44"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_44  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_45"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_45  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_46"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_46  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_47"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_47  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_48"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_48  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_49"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_49  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_50"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_50  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_51"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_51  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_52"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_52  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_53"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_53  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_54"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_54  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_55"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_55  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_56"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_56  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_57"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_57  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_58"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_58  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_59"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_59  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_60"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_60  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_61"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_61  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_62"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_62  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_63"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_63  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_64"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_64  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_65"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_65  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_66"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_66  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_67"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_67  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_68"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_68  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_69"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_69  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_70"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_70  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_71"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_71  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_72"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_72  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_73"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_73  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_74"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_74  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_75"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_75  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_76"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_76  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_77"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_77  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_78"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_78  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_79"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_79  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_80"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_80  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_81"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_81  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_82"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_82  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_83"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_83  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_84"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_84  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_85"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_85  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_86"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_86  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_87"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_87  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_88"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_88  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_89"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_89  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_90"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_90  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_91"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_91  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_92"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_92  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_93"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_93  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_parse_task_text__mutmut["xǁIssueParserǁ_parse_task_text__mutmut_94"] = IssueParser.xǁIssueParserǁ_parse_task_text__mutmut_94  # type: ignore # mutmut generated

mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["_mutmut_orig"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_1"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_1  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_2"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_2  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_3"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_3  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_4"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_4  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_5"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_5  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_6"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_6  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_7"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_7  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_8"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_8  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_9"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_9  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_10"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_10  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_11"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_11  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_12"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_12  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_13"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_13  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_14"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_14  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_15"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_15  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_16"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_16  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_17"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_17  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_18"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_18  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_19"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_19  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_20"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_20  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_21"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_21  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_22"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_22  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_23"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_23  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_24"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_24  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_25"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_25  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_26"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_26  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_27"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_27  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_28"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_28  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_29"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_29  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_30"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_30  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_31"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_31  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_32"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_32  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_33"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_33  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_34"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_34  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_35"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_35  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_36"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_36  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_37"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_37  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_38"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_38  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_39"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_39  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_files_from_task_type__mutmut["xǁIssueParserǁ_infer_files_from_task_type__mutmut_40"] = IssueParser.xǁIssueParserǁ_infer_files_from_task_type__mutmut_40  # type: ignore # mutmut generated

mutants_xǁIssueParserǁ_estimate_hours__mutmut["_mutmut_orig"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_1"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_1  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_2"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_2  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_3"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_3  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_4"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_4  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_5"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_5  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_6"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_6  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_7"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_7  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_8"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_8  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_9"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_9  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_10"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_10  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_11"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_11  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_12"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_12  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_13"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_13  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_14"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_14  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_15"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_15  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_16"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_16  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_17"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_17  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_18"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_18  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_19"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_19  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_20"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_20  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_21"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_21  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_22"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_22  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_23"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_23  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_24"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_24  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_25"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_25  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_26"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_26  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_27"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_27  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_28"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_28  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_29"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_29  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_30"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_30  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_31"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_31  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_32"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_32  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_33"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_33  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_34"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_34  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_35"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_35  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_36"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_36  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_37"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_37  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_38"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_38  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_39"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_39  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_40"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_40  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_estimate_hours__mutmut["xǁIssueParserǁ_estimate_hours__mutmut_41"] = IssueParser.xǁIssueParserǁ_estimate_hours__mutmut_41  # type: ignore # mutmut generated

mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["_mutmut_orig"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_1"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_1  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_2"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_2  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_3"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_3  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_4"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_4  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_5"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_5  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_6"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_6  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_7"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_7  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_8"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_8  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_9"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_9  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_10"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_10  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_11"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_11  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_12"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_12  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_13"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_13  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_14"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_14  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_15"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_15  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_extract_acceptance_criteria__mutmut["xǁIssueParserǁ_extract_acceptance_criteria__mutmut_16"] = IssueParser.xǁIssueParserǁ_extract_acceptance_criteria__mutmut_16  # type: ignore # mutmut generated

mutants_xǁIssueParserǁ_infer_dependencies__mutmut["_mutmut_orig"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_1"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_1  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_2"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_2  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_3"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_3  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_4"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_4  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_5"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_5  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_6"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_6  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_7"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_7  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_8"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_8  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_9"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_9  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_10"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_10  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_11"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_11  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_12"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_12  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_13"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_13  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_14"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_14  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_15"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_15  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_16"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_16  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_17"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_17  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_18"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_18  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_19"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_19  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_20"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_20  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_21"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_21  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_22"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_22  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_23"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_23  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_24"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_24  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_25"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_25  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_26"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_26  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_27"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_27  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_28"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_28  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_29"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_29  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_30"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_30  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_31"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_31  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_32"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_32  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_33"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_33  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_34"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_34  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_35"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_35  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_36"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_36  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_37"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_37  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_38"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_38  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_39"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_39  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_40"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_40  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_41"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_41  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_42"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_42  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_43"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_43  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_44"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_44  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_45"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_45  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_46"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_46  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_47"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_47  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_48"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_48  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_49"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_49  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_50"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_50  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_51"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_51  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_52"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_52  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_53"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_53  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_54"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_54  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_55"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_55  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_56"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_56  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_57"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_57  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_58"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_58  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_59"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_59  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_60"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_60  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_61"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_61  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_62"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_62  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_63"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_63  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_64"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_64  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_65"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_65  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_66"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_66  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_67"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_67  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_68"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_68  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_69"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_69  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_70"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_70  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_71"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_71  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_72"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_72  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_73"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_73  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_74"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_74  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_75"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_75  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_76"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_76  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_77"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_77  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_78"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_78  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_79"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_79  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_80"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_80  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_81"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_81  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_82"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_82  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_83"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_83  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_84"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_84  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_85"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_85  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_86"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_86  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_87"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_87  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_88"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_88  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_89"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_89  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_90"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_90  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_91"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_91  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_92"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_92  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_infer_dependencies__mutmut["xǁIssueParserǁ_infer_dependencies__mutmut_93"] = IssueParser.xǁIssueParserǁ_infer_dependencies__mutmut_93  # type: ignore # mutmut generated

mutants_xǁIssueParserǁ_assess_complexity__mutmut["_mutmut_orig"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_1"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_1  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_2"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_2  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_3"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_3  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_4"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_4  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_5"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_5  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_6"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_6  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_7"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_7  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_8"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_8  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_9"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_9  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_10"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_10  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_11"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_11  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_12"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_12  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_13"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_13  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_14"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_14  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_15"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_15  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_16"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_16  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_17"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_17  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_18"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_18  # type: ignore # mutmut generated
mutants_xǁIssueParserǁ_assess_complexity__mutmut["xǁIssueParserǁ_assess_complexity__mutmut_19"] = IssueParser.xǁIssueParserǁ_assess_complexity__mutmut_19  # type: ignore # mutmut generated
mutants_x_parse_issue__mutmut: MutantDict = {}  # type: ignore


# 편의 함수
@_mutmut_mutated(mutants_x_parse_issue__mutmut)
def parse_issue(issue_number: int, title: str, body: str) -> IssueAnalysis:
    """이슈 파싱 편의 함수"""
    parser = IssueParser()
    return parser.parse_issue(issue_number, title, body)


# 편의 함수
def x_parse_issue__mutmut_orig(issue_number: int, title: str, body: str) -> IssueAnalysis:
    """이슈 파싱 편의 함수"""
    parser = IssueParser()
    return parser.parse_issue(issue_number, title, body)


# 편의 함수
def x_parse_issue__mutmut_1(issue_number: int, title: str, body: str) -> IssueAnalysis:
    """이슈 파싱 편의 함수"""
    parser = None
    return parser.parse_issue(issue_number, title, body)


# 편의 함수
def x_parse_issue__mutmut_2(issue_number: int, title: str, body: str) -> IssueAnalysis:
    """이슈 파싱 편의 함수"""
    parser = IssueParser()
    return parser.parse_issue(None, title, body)


# 편의 함수
def x_parse_issue__mutmut_3(issue_number: int, title: str, body: str) -> IssueAnalysis:
    """이슈 파싱 편의 함수"""
    parser = IssueParser()
    return parser.parse_issue(issue_number, None, body)


# 편의 함수
def x_parse_issue__mutmut_4(issue_number: int, title: str, body: str) -> IssueAnalysis:
    """이슈 파싱 편의 함수"""
    parser = IssueParser()
    return parser.parse_issue(issue_number, title, None)


# 편의 함수
def x_parse_issue__mutmut_5(issue_number: int, title: str, body: str) -> IssueAnalysis:
    """이슈 파싱 편의 함수"""
    parser = IssueParser()
    return parser.parse_issue(title, body)


# 편의 함수
def x_parse_issue__mutmut_6(issue_number: int, title: str, body: str) -> IssueAnalysis:
    """이슈 파싱 편의 함수"""
    parser = IssueParser()
    return parser.parse_issue(issue_number, body)


# 편의 함수
def x_parse_issue__mutmut_7(issue_number: int, title: str, body: str) -> IssueAnalysis:
    """이슈 파싱 편의 함수"""
    parser = IssueParser()
    return parser.parse_issue(
        issue_number,
        title,
    )


mutants_x_parse_issue__mutmut["_mutmut_orig"] = x_parse_issue__mutmut_orig  # type: ignore # mutmut generated
mutants_x_parse_issue__mutmut["x_parse_issue__mutmut_1"] = x_parse_issue__mutmut_1  # type: ignore # mutmut generated
mutants_x_parse_issue__mutmut["x_parse_issue__mutmut_2"] = x_parse_issue__mutmut_2  # type: ignore # mutmut generated
mutants_x_parse_issue__mutmut["x_parse_issue__mutmut_3"] = x_parse_issue__mutmut_3  # type: ignore # mutmut generated
mutants_x_parse_issue__mutmut["x_parse_issue__mutmut_4"] = x_parse_issue__mutmut_4  # type: ignore # mutmut generated
mutants_x_parse_issue__mutmut["x_parse_issue__mutmut_5"] = x_parse_issue__mutmut_5  # type: ignore # mutmut generated
mutants_x_parse_issue__mutmut["x_parse_issue__mutmut_6"] = x_parse_issue__mutmut_6  # type: ignore # mutmut generated
mutants_x_parse_issue__mutmut["x_parse_issue__mutmut_7"] = x_parse_issue__mutmut_7  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_analyze_issue__mutmut)
def analyze_issue(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_orig(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_1(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = None
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_2(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(None, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_3(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, None, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_4(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, None)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_5(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_6(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_7(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(
        issue_number,
        title,
    )
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_8(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "XXissue_numberXX": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_9(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "ISSUE_NUMBER": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_10(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "XXtitleXX": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_11(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "TITLE": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_12(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "XXsummaryXX": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_13(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "SUMMARY": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_14(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "XXtech_stackXX": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_15(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "TECH_STACK": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_16(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "XXsuggested_filesXX": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_17(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "SUGGESTED_FILES": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_18(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "XXcomplexityXX": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_19(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "COMPLEXITY": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_20(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "XXestimated_hoursXX": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_21(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "ESTIMATED_HOURS": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_22(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "XXtasksXX": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_23(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "TASKS": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_24(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "XXidXX": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_25(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "ID": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_26(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "XXtitleXX": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_27(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "TITLE": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_28(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "XXtypeXX": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_29(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "TYPE": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_30(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "XXpriorityXX": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_31(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "PRIORITY": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_32(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "XXfilesXX": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_33(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "FILES": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_34(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "XXdependenciesXX": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_35(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "DEPENDENCIES": t.dependencies,
                "hours": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_36(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "XXhoursXX": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_37(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "HOURS": t.estimated_hours,
                "criteria": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_38(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "XXcriteriaXX": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


def x_analyze_issue__mutmut_39(issue_number: int, title: str, body: str) -> dict[str, Any]:
    """이슈 분석 결과 딕셔너리 반환"""
    analysis = parse_issue(issue_number, title, body)
    return {
        "issue_number": analysis.issue_number,
        "title": analysis.title,
        "summary": analysis.summary,
        "tech_stack": analysis.tech_stack_hints,
        "suggested_files": analysis.suggested_files,
        "complexity": analysis.complexity,
        "estimated_hours": analysis.estimated_total_hours,
        "tasks": [
            {
                "id": t.id,
                "title": t.title,
                "type": t.task_type.value,
                "priority": t.priority.name,
                "files": t.target_files,
                "dependencies": t.dependencies,
                "hours": t.estimated_hours,
                "CRITERIA": t.acceptance_criteria,
            }
            for t in analysis.parsed_tasks
        ],
    }


mutants_x_analyze_issue__mutmut["_mutmut_orig"] = x_analyze_issue__mutmut_orig  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_1"] = x_analyze_issue__mutmut_1  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_2"] = x_analyze_issue__mutmut_2  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_3"] = x_analyze_issue__mutmut_3  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_4"] = x_analyze_issue__mutmut_4  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_5"] = x_analyze_issue__mutmut_5  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_6"] = x_analyze_issue__mutmut_6  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_7"] = x_analyze_issue__mutmut_7  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_8"] = x_analyze_issue__mutmut_8  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_9"] = x_analyze_issue__mutmut_9  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_10"] = x_analyze_issue__mutmut_10  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_11"] = x_analyze_issue__mutmut_11  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_12"] = x_analyze_issue__mutmut_12  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_13"] = x_analyze_issue__mutmut_13  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_14"] = x_analyze_issue__mutmut_14  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_15"] = x_analyze_issue__mutmut_15  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_16"] = x_analyze_issue__mutmut_16  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_17"] = x_analyze_issue__mutmut_17  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_18"] = x_analyze_issue__mutmut_18  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_19"] = x_analyze_issue__mutmut_19  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_20"] = x_analyze_issue__mutmut_20  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_21"] = x_analyze_issue__mutmut_21  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_22"] = x_analyze_issue__mutmut_22  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_23"] = x_analyze_issue__mutmut_23  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_24"] = x_analyze_issue__mutmut_24  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_25"] = x_analyze_issue__mutmut_25  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_26"] = x_analyze_issue__mutmut_26  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_27"] = x_analyze_issue__mutmut_27  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_28"] = x_analyze_issue__mutmut_28  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_29"] = x_analyze_issue__mutmut_29  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_30"] = x_analyze_issue__mutmut_30  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_31"] = x_analyze_issue__mutmut_31  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_32"] = x_analyze_issue__mutmut_32  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_33"] = x_analyze_issue__mutmut_33  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_34"] = x_analyze_issue__mutmut_34  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_35"] = x_analyze_issue__mutmut_35  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_36"] = x_analyze_issue__mutmut_36  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_37"] = x_analyze_issue__mutmut_37  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_38"] = x_analyze_issue__mutmut_38  # type: ignore # mutmut generated
mutants_x_analyze_issue__mutmut["x_analyze_issue__mutmut_39"] = x_analyze_issue__mutmut_39  # type: ignore # mutmut generated


if __name__ == "__main__":
    # 테스트
    test_body = """
    사용자 인증 시스템을 구현해야 합니다.
    
    - 사용자 로그인/로그아웃 기능 구현
    - JWT 토큰 기반 인증 추가
    - 비밀번호 암호화 (bcrypt) 적용
    - 로그인/로그아웃 API 엔드포인트 생성
    - 단위 테스트 작성 필요
    
    기술 스택: Python, FastAPI, JWT, bcrypt
    """

    analysis = parse_issue(1, "사용자 인증 시스템 구현", test_body)

    print(f"이슈: {analysis.title}")
    print(f"요약: {analysis.summary}")
    print(f"기술 스택: {analysis.tech_stack_hints}")
    print(f"추천 파일: {analysis.suggested_files}")
    print(f"복잡도: {analysis.complexity}")
    print(f"예상 시간: {analysis.estimated_total_hours}시간")
    print(f"\n작업 항목 ({len(analysis.parsed_tasks)}개):")
    for task in analysis.parsed_tasks:
        print(
            f"  - [{task.id}] {task.task_type.value} | {task.priority.name} | {task.estimated_hours}h"
        )
        print(f"    제목: {task.title}")
        print(f"    파일: {task.target_files}")
        print(f"    의존성: {task.dependencies}")
        print(f"    기준: {task.acceptance_criteria}")
