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

    def __init__(self):
        self._compiled_patterns = self._compile_patterns()

    def _compile_patterns(self) -> dict:
        """정규식 패턴 사전 컴파일"""
        patterns = {}

        # 작업 유형 패턴
        for task_type, keywords in self.TASK_TYPE_KEYWORDS.items():
            pattern = r"\b(" + "|".join(re.escape(k) for k in keywords) + r")\b"
            patterns[f"task_type_{task_type.value}"] = re.compile(
                pattern, re.IGNORECASE
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
        analysis.estimated_total_hours = sum(
            t.estimated_hours for t in analysis.parsed_tasks
        )

        log.info(f"이슈 #{issue_number} 파싱 완료: {len(analysis.parsed_tasks)}개 작업")

        return analysis

    def _extract_summary(self, body: str) -> str:
        """본문에서 요약 추출 (첫 문단 또는 첫 200자)"""
        paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
        if paragraphs:
            return paragraphs[0][:200]
        return body[:200]

    def _extract_tech_stack(self, body: str) -> list[str]:
        """기술 스택 힌트 추출"""
        found = []
        body_lower = body.lower()
        for stack, pattern in self._compiled_patterns.items():
            if stack.startswith("tech_") and pattern.search(body_lower):
                found.append(stack.replace("tech_", ""))
        return found

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

    def _assess_complexity(self, tasks: list[ParsedTask]) -> str:
        """복잡도 평가"""
        total_hours = sum(t.estimated_hours for t in tasks)
        num_files = len({f for t in tasks for f in t.target_files})

        if total_hours > 20 or num_files > 10:
            return "high"
        elif total_hours > 8 or num_files > 5:
            return "medium"
        return "low"


# 편의 함수
def parse_issue(issue_number: int, title: str, body: str) -> IssueAnalysis:
    """이슈 파싱 편의 함수"""
    parser = IssueParser()
    return parser.parse_issue(issue_number, title, body)


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
