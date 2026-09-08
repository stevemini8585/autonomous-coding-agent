"""
PR 리뷰 자동화 모듈
GitHub PR 변경사항 분석, 보안/성능 이슈 탐지, 리뷰 코멘트 자동 생성
"""

from __future__ import annotations

import logging
import re
import subprocess
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import ClassVar

log = logging.getLogger("autonomous_coding_agent.pr_reviewer")


class ReviewSeverity(Enum):
    """리뷰 심각도"""

    CRITICAL = "critical"  # 보안 취약점, 치명적 버그
    ERROR = "error"  # 버그, 로직 오류
    WARNING = "warning"  # 성능 이슈, 베스트 프랙티스 위반
    INFO = "info"  # 스타일, 제안사항
    NIT = "nit"  # 사소한 스타일


class ReviewCategory(Enum):
    """리뷰 카테고리"""

    SECURITY = "security"  # 보안 (SQL 인젝션, XSS, 시크릿 노출 등)
    PERFORMANCE = "performance"  # 성능 (N+1, 비효율적 쿼리, 메모리 누수)
    CORRECTNESS = "correctness"  # 정확성 (버그, 로직 오류, 예외 처리)
    MAINTAINABILITY = "maintainability"  # 유지보수성 (복잡도, 중복, 네이밍)
    STYLE = "style"  # 스타일 (포맷팅, import 정렬, 타입 힌트)
    TESTING = "testing"  # 테스트 (커버리지, 엣지 케이스, 모킹)
    DOCUMENTATION = "documentation"  # 문서 (docstring, 주석, README)
    DEPENDENCY = "dependency"  # 의존성 (취약한 패키지, 미사용 import)


@dataclass
class ReviewComment:
    """리뷰 코멘트"""

    file_path: str
    line_start: int
    line_end: int
    severity: ReviewSeverity
    category: ReviewCategory
    title: str
    message: str
    suggestion: str | None = None
    rule_id: str | None = None


@dataclass
class PRReviewResult:
    """PR 리뷰 결과"""

    pr_number: int
    repo: str
    total_comments: int
    critical_count: int
    error_count: int
    warning_count: int
    info_count: int
    nit_count: int
    comments: list[ReviewComment] = field(default_factory=list)
    summary: str = ""
    reviewed_at: datetime = field(default_factory=datetime.now)
    files_reviewed: list[str] = field(default_factory=list)


class PRReviewer:
    """PR 자동 리뷰어"""

    # 보안 패턴 (정규식)
    SECURITY_PATTERNS: ClassVar[list[tuple[str, ReviewCategory, str, str, str]]] = [
        # SQL 인젝션 가능성
        (
            r"(?i)(execute|query|raw)\s*\(\s*[\"'].*%.*[\"']",
            ReviewCategory.SECURITY,
            "SQL_INJECTION",
            "SQL 인젝션 취약점 가능성: 파라미터 바인딩 사용 필요",
            'cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))',
        ),
        (
            r"(?i)f[\"'].*SELECT.*\{.*\}.*[\"']",
            ReviewCategory.SECURITY,
            "SQL_INJECTION",
            "f-string으로 SQL 쿼리 구성: 파라미터 바인딩 사용 필요",
            'cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))',
        ),
        # 시크릿/키 하드코딩
        (
            r"(?i)(api[_-]?key|secret[_-]?key|password|token|private[_-]?key)\s*[=:]\s*[\"'][^\"']{8,}[\"']",
            ReviewCategory.SECURITY,
            "HARDCODED_SECRET",
            "하드코딩된 시크릿/키 발견: 환경 변수 사용 필요",
            "API_KEY = os.environ.get('API_KEY')",
        ),
        (
            r"(?i)(aws[_-]?access[_-]?key|aws[_-]?secret|github[_-]?token|slack[_-]?token)\s*[=:]\s*[\"'][^\"']+[\"']",
            ReviewCategory.SECURITY,
            "HARDCODED_SECRET",
            "클라우드 자격 증명 하드코딩: 시크릿 매니저 사용 필요",
            "AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')",
        ),
        # XSS 가능성
        (
            r"(?i)(render_template_string|mark_safe|safe\s*=\s*True)\s*\(",
            ReviewCategory.SECURITY,
            "XSS_RISK",
            "XSS 위험: 사용자 입력 이스케이프 필요",
            "escape(user_input) 또는 템플릿 엔진의 autoescape 사용",
        ),
        (
            r"(?i)dangerouslySetInnerHTML",
            ReviewCategory.SECURITY,
            "XSS_RISK",
            "React dangerouslySetInnerHTML 사용: XSS 위험",
            "DOMPurify.sanitize(html) 또는 안전한 컴포넌트 사용",
        ),
        # 경로 순회
        (
            r"(?i)open\s*\(\s*[\"']\.\./",
            ReviewCategory.SECURITY,
            "PATH_TRAVERSAL",
            "경로 순회 가능성: 경로 검증 필요",
            "os.path.normpath(path) 후 허용된 디렉토리 내인지 확인",
        ),
        (
            r"(?i)path\.join\s*\([^)]*\.\.",
            ReviewCategory.SECURITY,
            "PATH_TRAVERSAL",
            "경로 순회 가능성: 안전한 경로 결합 필요",
            "os.path.join(base, path) 후 os.path.commonprefix로 검증",
        ),
        # 명령어 인젝션
        (
            r"(?i)(subprocess|os\.system|os\.popen)\s*\([^)]*[\"'].*%.*[\"']",
            ReviewCategory.SECURITY,
            "COMMAND_INJECTION",
            "명령어 인젝션 가능성: shell=False 및 인자 리스트 사용",
            "subprocess.run(['cmd', arg1, arg2], shell=False)",
        ),
        (
            r"(?i)eval\s*\(|exec\s*\(",
            ReviewCategory.SECURITY,
            "CODE_INJECTION",
            "코드 인젝션 위험: eval/exec 사용 금지",
            "ast.literal_eval() 또는 안전한 파싱 라이브러리 사용",
        ),
        # 약한 암호화
        (
            r"(?i)(md5|sha1)\s*\(",
            ReviewCategory.SECURITY,
            "WEAK_CRYPTO",
            "약한 해시 함수 사용: SHA-256 이상 권장",
            "hashlib.sha256(data).hexdigest()",
        ),
        (
            r"(?i)ECB\s*mode",
            ReviewCategory.SECURITY,
            "WEAK_CRYPTO",
            "ECB 모드 사용: CBC/GCM 모드 권장",
            "AES.new(key, AES.MODE_GCM)",
        ),
        # 디버그 코드
        (
            r"(?i)(print|console\.log|debugger|pdb\.set_trace)\s*\(",
            ReviewCategory.SECURITY,
            "DEBUG_CODE",
            "프로덕션 코드에 디버그 코드 존재",
            "logging 모듈 사용 또는 디버그 코드 제거",
        ),
        # 시크릿 패턴 (일반적인 패턴)
        (
            r"(?i)(secret|password|token|api_key)\s*=\s*[\"'][a-zA-Z0-9_\-]{20,}[\"']",
            ReviewCategory.SECURITY,
            "HARDCODED_SECRET",
            "긴 랜덤 문자열 하드코딩: 환경 변수 또는 시크릿 매니저 사용",
            "SECRET = os.environ.get('SECRET_KEY')",
        ),
    ]

    # 성능 패턴
    PERFORMANCE_PATTERNS: ClassVar[list[tuple[str, ReviewCategory, str, str, str]]] = [
        # N+1 쿼리
        (
            r"(?i)for\s+\w+\s+in\s+\w+:\s*\n\s*\w+\.(query|filter|get)\s*\(",
            ReviewCategory.PERFORMANCE,
            "N_PLUS_ONE",
            "N+1 쿼리 가능성: eager loading 사용 필요",
            "select_related() 또는 prefetch_related() 사용 (Django), joinedload() (SQLAlchemy)",
        ),
        (
            r"(?i)\.all\(\)\s*\n\s*for\s+\w+\s+in",
            ReviewCategory.PERFORMANCE,
            "N_PLUS_ONE",
            "전체 조회 후 루프: 배치 처리 고려",
            "IN 절로 한 번에 조회하거나 bulk 연산 사용",
        ),
        # 비효율적 리스트 연산
        (
            r"(?i)\.append\s*\([^)]*\)\s*for\s+\w+\s+in",
            ReviewCategory.PERFORMANCE,
            "LIST_COMPREHENSION",
            "리스트 컴프리헨션 사용 권장",
            "[x for x in items if condition] 또는 [func(x) for x in items]",
        ),
        # 중복 계산
        (
            r"(?i)len\s*\(\s*\w+\s*\)\s*[><=!]=",
            ReviewCategory.PERFORMANCE,
            "REPEATED_LEN",
            "반복문에서 len() 호출: 변수에 저장 권장",
            "length = len(items); for i in range(length): ...",
        ),
        # 큰 객체 복사
        (
            r"(?i)copy\.deepcopy\s*\(",
            ReviewCategory.PERFORMANCE,
            "DEEP_COPY",
            "깊은 복사 사용: 얕은 복사 또는 불변 객체 고려",
            "copy.copy() 또는 dataclass(frozen=True) 사용",
        ),
    ]

    # 정확성 패턴
    CORRECTNESS_PATTERNS: ClassVar[list[tuple[str, ReviewCategory, str, str, str]]] = [
        # 빈 except
        (
            r"(?i)except\s*:\s*\n\s*(pass|continue|break)",
            ReviewCategory.CORRECTNESS,
            "BARE_EXCEPT",
            "빈 except 절: 구체적 예외 타입 지정 필요",
            "except ValueError: 또는 except (ValueError, TypeError):",
        ),
        (
            r"(?i)except\s+Exception\s*:\s*\n\s*(pass|continue|break)",
            ReviewCategory.CORRECTNESS,
            "BROAD_EXCEPT",
            "광범위한 예외 캐치: 구체적 예외 타입 지정 필요",
            "except (ValueError, TypeError) as e: logging.error(e); raise",
        ),
        # 미사용 변수
        (
            r"(?i)^\s*_\s*=\s*.+",
            ReviewCategory.CORRECTNESS,
            "UNUSED_VARIABLE",
            "미사용 변수 가능성: 의도적이면 _ 접두사 유지",
            "사용하지 않는 변수는 _prefix 또는 del로 명시적 처리",
        ),
        # 변경 가능한 기본 인자
        (
            r"def\s+\w+\s*\([^)]*=\s*\[[^\]]*\]",
            ReviewCategory.CORRECTNESS,
            "MUTABLE_DEFAULT",
            "가변 기본 인자 리스트: None 기본값 후 내부에서 초기화",
            "def func(items=None): items = items or []",
        ),
        (
            r"def\s+\w+\s*\([^)]*=\s*\{[^}]*\}",
            ReviewCategory.CORRECTNESS,
            "MUTABLE_DEFAULT",
            "가변 기본 인자 딕셔너리: None 기본값 후 내부에서 초기화",
            "def func(config=None): config = config or {}",
        ),
        # 리소스 누수
        (
            r"(?i)(open|connect|acquire)\s*\([^)]*\)\s*[^;]*(?!\s*with\s)",
            ReviewCategory.CORRECTNESS,
            "RESOURCE_LEAK",
            "리소스 해제 누락 가능성: with 문 또는 try-finally 사용",
            "with open(path) as f: 또는 try: ... finally: resource.close()",
        ),
    ]

    # 유지보수성 패턴
    MAINTAINABILITY_PATTERNS: ClassVar[
        list[tuple[str, ReviewCategory, str, str, str]]
    ] = [
        # 긴 함수
        (
            r"(?m)^def\s+\w+\([^)]*\):",
            ReviewCategory.MAINTAINABILITY,
            "LONG_FUNCTION",
            "함수 길이 확인 필요 (50줄 초과 시 분리 권장)",
            "함수를 단일 책임 원칙에 따라 분리: helper function 추출",
        ),
        # 깊은 중첩
        (
            r"(?m)^\s{16,}\w",
            ReviewCategory.MAINTAINABILITY,
            "DEEP_NESTING",
            "깊은 중첩 (4단계 이상): 함수 분리 권장",
            "early return으로 중첩 감소, guard clause 패턴 적용",
        ),
        # 매직 넘버
        (
            r"(?i)(?<![\w.])(\d{3,})(?![\w.])",
            ReviewCategory.MAINTAINABILITY,
            "MAGIC_NUMBER",
            "매직 넘버: 상수 정의 권장",
            "MAX_RETRY_COUNT = 3; TIMEOUT_SECONDS = 30",
        ),
        # TODO/FIXME
        (
            r"(?i)(TODO|FIXME|HACK|XXX)\s*[::-]",
            ReviewCategory.MAINTAINABILITY,
            "TECH_DEBT",
            "기술 부채 마커: 이슈 트래커 연동 권장",
            "관련 이슈 번호와 함께 작성: #123",
        ),
    ]

    # 스타일 패턴 (ruff/mypy가 커버하지만 보완)
    STYLE_PATTERNS: ClassVar[list[tuple[str, ReviewCategory, str, str, str]]] = [
        # 타입 힌트 누락
        (
            r"def\s+\w+\s*\([^)]*\)\s*:",
            ReviewCategory.STYLE,
            "MISSING_TYPE_HINT",
            "타입 힌트 누락: 반환 타입 및 인자 타입 추가 권장",
            "def func(arg: int) -> str: ...",
        ),
        # docstring 누락
        (
            r"(?m)^def\s+\w+\s*\([^)]*\)\s*:\s*\n\s*(?!\"\"\")",
            ReviewCategory.STYLE,
            "MISSING_DOCSTRING",
            "docstring 누락: 함수 설명 추가 권장",
            '"""함수 설명.\n\nArgs:\n    arg: 설명\n\nReturns:\n    설명\n"""',
        ),
        # import 순서
        (
            r"(?m)^import\s+\w+",
            ReviewCategory.STYLE,
            "IMPORT_ORDER",
            "import 순서 확인: 표준/서드파티/로컬 순서 권장",
            "1. 표준 라이브러리\n2. 서드파티\n3. 로컬 import",
        ),
    ]

    def __init__(self, workspace: str | Path):
        self.workspace = Path(workspace)
        self._compile_patterns()

    def _compile_patterns(self) -> None:
        """모든 패턴 컴파일"""
        self.all_patterns = []

        for pattern_str, category, rule_id, message, suggestion in (
            self.SECURITY_PATTERNS
            + self.PERFORMANCE_PATTERNS
            + self.CORRECTNESS_PATTERNS
            + self.MAINTAINABILITY_PATTERNS
            + self.STYLE_PATTERNS
        ):
            severity = self._get_severity_for_category(category)
            compiled = re.compile(pattern_str, re.MULTILINE)
            self.all_patterns.append(
                (compiled, category, rule_id, message, severity, suggestion)
            )

    def _get_severity_for_category(self, category: ReviewCategory) -> ReviewSeverity:
        """카테고리별 기본 심각도"""
        severity_map = {
            ReviewCategory.SECURITY: ReviewSeverity.CRITICAL,
            ReviewCategory.PERFORMANCE: ReviewSeverity.WARNING,
            ReviewCategory.CORRECTNESS: ReviewSeverity.ERROR,
            ReviewCategory.MAINTAINABILITY: ReviewSeverity.WARNING,
            ReviewCategory.STYLE: ReviewSeverity.INFO,
            ReviewCategory.TESTING: ReviewSeverity.INFO,
            ReviewCategory.DOCUMENTATION: ReviewSeverity.NIT,
            ReviewCategory.DEPENDENCY: ReviewSeverity.WARNING,
        }
        return severity_map.get(category, ReviewSeverity.INFO)

    def review_pr(
        self, pr_number: int, repo: str, base_branch: str = "main"
    ) -> PRReviewResult:
        """PR 리뷰 수행"""
        log.info(f"PR #{pr_number} 리뷰 시작: {repo}")

        # 1. PR 변경사항 가져오기
        diff = self._get_pr_diff(pr_number, repo)
        if not diff:
            return PRReviewResult(
                pr_number=pr_number,
                repo=repo,
                total_comments=0,
                critical_count=0,
                error_count=0,
                warning_count=0,
                info_count=0,
                nit_count=0,
                summary="PR diff를 가져올 수 없습니다.",
            )

        # 2. 변경된 파일 파싱
        changed_files = self._parse_diff(diff)

        # 3. 각 파일 분석
        all_comments = []
        for file_path, file_diff in changed_files.items():
            comments = self._analyze_file(file_path, file_diff)
            all_comments.extend(comments)

        # 4. 정적 분석 도구 실행 (ruff, mypy)
        tool_comments = self._run_static_analysis(list(changed_files.keys()))
        all_comments.extend(tool_comments)

        # 5. 결과 집계
        result = self._aggregate_results(
            pr_number, repo, all_comments, list(changed_files.keys())
        )

        log.info(
            f"PR #{pr_number} 리뷰 완료: {result.total_comments}개 코멘트 (Critical: {result.critical_count}, Error: {result.error_count}, Warning: {result.warning_count})"
        )

        return result

    def _get_pr_diff(self, pr_number: int, repo: str) -> str | None:
        """PR diff 가져오기"""
        try:
            result = subprocess.run(
                ["gh", "pr", "diff", str(pr_number), "-R", repo],
                capture_output=True,
                text=True,
                timeout=60,
                cwd=self.workspace,
                check=False,
            )
            if result.returncode == 0:
                return result.stdout
            log.error(f"PR diff 가져오기 실패: {result.stderr}")
            return None
        except subprocess.TimeoutExpired:
            log.error("PR diff 타임아웃")
            return None
        except (OSError, subprocess.SubprocessError) as e:
            log.error(f"PR diff 가져오기 오류: {e}")
            return None

    def _parse_diff(self, diff: str) -> dict[str, str]:
        """diff 파싱하여 파일별 변경사항 추출"""
        files = {}
        current_file = None
        current_content = []

        for line in diff.split("\n"):
            if line.startswith("diff --git"):
                if current_file and current_content:
                    files[current_file] = "\n".join(current_content)
                # 파일명 추출: diff --git a/path b/path
                parts = line.split()
                if len(parts) >= 4:
                    current_file = parts[3][2:]  # b/ 제거
                current_content = [line]
            elif current_file:
                current_content.append(line)

        if current_file and current_content:
            files[current_file] = "\n".join(current_content)

        return files

    def _analyze_file(self, file_path: str, diff: str) -> list[ReviewComment]:
        """단일 파일 분석"""
        comments = []

        # diff에서 추가된 라인만 추출
        added_lines = self._extract_added_lines(diff)

        # 패턴 매칭
        for line_num, line_content in added_lines:
            for (
                pattern,
                category,
                rule_id,
                message,
                severity,
                suggestion,
            ) in self.all_patterns:
                matches = pattern.finditer(line_content)
                for match in matches:
                    comments.append(
                        ReviewComment(
                            file_path=file_path,
                            line_start=line_num,
                            line_end=line_num,
                            severity=severity,
                            category=category,
                            title=f"[{category.value.upper()}] {rule_id}",
                            message=message,
                            suggestion=suggestion,
                            rule_id=rule_id,
                        )
                    )

        return comments

    def _extract_added_lines(self, diff: str) -> list[tuple[int, str]]:
        """diff에서 추가된 라인 추출 (라인 번호 포함)"""
        added = []
        current_line = 0

        for line in diff.split("\n"):
            if line.startswith("@@"):
                # @@ -old_start,old_count +new_start,new_count @@
                match = re.search(r"\+(\d+)", line)
                if match:
                    current_line = int(match.group(1)) - 1
            elif line.startswith("+"):
                current_line += 1
                # diff 헤더 라인 제외 (+++ b/file.py)
                if not line.startswith("+++"):
                    added.append((current_line, line[1:]))
            elif line.startswith("-"):
                # 삭제된 라인은 라인 번호만 증가
                pass
            else:
                current_line += 1

        return added

    def _run_static_analysis(self, file_paths: list[str]) -> list[ReviewComment]:
        """정적 분석 도구 실행 (ruff, mypy)"""
        comments = []

        # ruff 실행
        try:
            result = subprocess.run(
                ["ruff", "check", "--output-format=json"] + file_paths,
                capture_output=True,
                text=True,
                timeout=120,
                cwd=self.workspace,
                check=False,
            )
            if result.stdout:
                import json

                issues = json.loads(result.stdout)
                for issue in issues:
                    loc = issue.get("location", {})
                    end_loc = issue.get("end_location", {})
                    line_start = loc.get("row", 1)
                    line_end = end_loc.get("row", line_start)
                    comments.append(
                        ReviewComment(
                            file_path=issue["filename"],
                            line_start=line_start,
                            line_end=line_end,
                            severity=self._map_ruff_severity(
                                issue.get("level", "warning")
                            ),
                            category=ReviewCategory.STYLE,
                            title=f"[RUFF] {issue['code']}",
                            message=issue["message"],
                            rule_id=issue["code"],
                        )
                    )
        except (OSError, subprocess.SubprocessError, json.JSONDecodeError) as e:
            log.warning(f"ruff 실행 실패: {e}")

        # mypy 실행
        try:
            result = subprocess.run(
                ["mypy", "--explicit-package-bases", "--json"] + file_paths,
                capture_output=True,
                text=True,
                timeout=120,
                cwd=self.workspace,
                check=False,
            )
            if result.stdout:
                import json

                issues = json.loads(result.stdout)
                for issue in issues:
                    comments.append(
                        ReviewComment(
                            file_path=issue["file"],
                            line_start=issue["line"],
                            line_end=issue.get("end_line", issue["line"]),
                            severity=ReviewSeverity.WARNING,
                            category=ReviewCategory.STYLE,
                            title=f"[MYPY] {issue.get('code', 'type-error')}",
                            message=issue["message"],
                            rule_id=issue.get("code", "type-error"),
                        )
                    )
        except (OSError, subprocess.SubprocessError, json.JSONDecodeError) as e:
            log.warning(f"mypy 실행 실패: {e}")

        return comments

    def _map_ruff_severity(self, level: str) -> ReviewSeverity:
        """ruff 레벨을 ReviewSeverity로 매핑"""
        mapping = {
            "error": ReviewSeverity.ERROR,
            "warning": ReviewSeverity.WARNING,
            "info": ReviewSeverity.INFO,
        }
        return mapping.get(level.lower(), ReviewSeverity.WARNING)

    def _aggregate_results(
        self,
        pr_number: int,
        repo: str,
        comments: list[ReviewComment],
        files_reviewed: list[str],
    ) -> PRReviewResult:
        """결과 집계"""
        severity_counts = dict.fromkeys(ReviewSeverity, 0)
        for comment in comments:
            severity_counts[comment.severity] += 1

        # 심각도 순 정렬
        comments.sort(key=lambda c: (c.severity.value, c.file_path, c.line_start))

        # 요약 생성
        summary_lines = [
            f"## PR #{pr_number} 자동 리뷰 결과",
            "",
            f"**총 {len(comments)}개 이슈 발견**",
            f"- 🔴 Critical: {severity_counts[ReviewSeverity.CRITICAL]}",
            f"- 🟠 Error: {severity_counts[ReviewSeverity.ERROR]}",
            f"- 🟡 Warning: {severity_counts[ReviewSeverity.WARNING]}",
            f"- 🔵 Info: {severity_counts[ReviewSeverity.INFO]}",
            f"- ⚪ Nit: {severity_counts[ReviewSeverity.NIT]}",
            "",
            f"**검토된 파일**: {len(files_reviewed)}개",
        ]

        return PRReviewResult(
            pr_number=pr_number,
            repo=repo,
            total_comments=len(comments),
            critical_count=severity_counts[ReviewSeverity.CRITICAL],
            error_count=severity_counts[ReviewSeverity.ERROR],
            warning_count=severity_counts[ReviewSeverity.WARNING],
            info_count=severity_counts[ReviewSeverity.INFO],
            nit_count=severity_counts[ReviewSeverity.NIT],
            comments=comments,
            summary="\n".join(summary_lines),
            files_reviewed=files_reviewed,
        )

    def post_review_to_github(
        self, result: PRReviewResult, event: str = "COMMENT"
    ) -> bool:
        """GitHub에 리뷰 게시"""
        if not result.comments:
            log.info("게시할 코멘트가 없습니다.")
            return True

        # 리뷰 본문 생성
        body = result.summary + "\n\n---\n\n"

        # 파일별로 그룹화
        from collections import defaultdict

        by_file = defaultdict(list)
        for comment in result.comments:
            by_file[comment.file_path].append(comment)

        for file_path, file_comments in by_file.items():
            body += f"### `{file_path}`\n\n"
            for comment in file_comments:
                severity_emoji = {
                    ReviewSeverity.CRITICAL: "🔴",
                    ReviewSeverity.ERROR: "🟠",
                    ReviewSeverity.WARNING: "🟡",
                    ReviewSeverity.INFO: "🔵",
                    ReviewSeverity.NIT: "⚪",
                }
                emoji = severity_emoji.get(comment.severity, "")
                body += f"{emoji} **Line {comment.line_start}** [{comment.category.value.upper()}] {comment.title}\n"
                body += f"> {comment.message}\n"
                if comment.suggestion:
                    body += f"> 💡 제안: {comment.suggestion}\n"
                body += "\n"

        # gh api로 리뷰 생성
        try:
            import json

            review_data = {
                "event": event,  # COMMENT, APPROVE, REQUEST_CHANGES
                "body": body,
                "comments": [
                    {
                        "path": c.file_path,
                        "line": c.line_start,
                        "body": f"{emoji} **[{c.category.value.upper()}] {c.title}**\n{c.message}"
                        + (f"\n💡 제안: {c.suggestion}" if c.suggestion else ""),
                    }
                    for c in result.comments
                    for emoji in [severity_emoji.get(c.severity, "")]
                ],
            }

            # gh api 호출
            import tempfile

            with tempfile.NamedTemporaryFile(
                mode="w", suffix=".json", delete=False
            ) as f:
                json.dump(review_data, f)
                temp_path = f.name

            try:
                subprocess.run(
                    [
                        "gh",
                        "api",
                        f"repos/{result.repo}/pulls/{result.pr_number}/reviews",
                        "--method",
                        "POST",
                        "--input",
                        temp_path,
                    ],
                    capture_output=True,
                    text=True,
                    timeout=60,
                    cwd=self.workspace,
                    check=False,
                )
                log.info(f"PR #{result.pr_number} 리뷰 게시 완료")
                return True
            finally:
                Path(temp_path).unlink(missing_ok=True)

        except (OSError, subprocess.SubprocessError) as e:
            log.error(f"GitHub 리뷰 게시 실패: {e}")
            return False


# 편의 함수
def review_pr(
    pr_number: int, repo: str, workspace: str | Path, post: bool = False
) -> PRReviewResult:
    """PR 리뷰 편의 함수"""
    reviewer = PRReviewer(workspace)
    result = reviewer.review_pr(pr_number, repo)

    if post:
        reviewer.post_review_to_github(result)

    return result


if __name__ == "__main__":
    # 테스트
    from enum import Enum

    # Enum 정의 (위에서 이미 정의됨)
    class ReviewSeverity(Enum):
        CRITICAL = "critical"
        ERROR = "error"
        WARNING = "warning"
        INFO = "info"
        NIT = "nit"

    class ReviewCategory(Enum):
        SECURITY = "security"
        PERFORMANCE = "performance"
        CORRECTNESS = "correctness"
        MAINTAINABILITY = "maintainability"
        STYLE = "style"
        TESTING = "testing"
        DOCUMENTATION = "documentation"
        DEPENDENCY = "dependency"

    reviewer = PRReviewer("/tmp/test_git_workflow")

    # 테스트 코드
    test_diff = """diff --git a/auth/models.py b/auth/models.py
@@ -1,3 +1,15 @@
+import os
+API_KEY = "sk-1234567890abcdef"  # 하드코딩된 시크릿
+
+def get_user(user_id):
+    query = f"SELECT * FROM users WHERE id = {user_id}"  # SQL 인젝션
+    return db.execute(query)
+
+    password = "plaintext"  # 평문 비밀번호
+    pass
"""

    files = reviewer._parse_diff(test_diff)
    for fp, fd in files.items():
        print(f"=== {fp} ===")
        print(fd)
        print()
        comments = reviewer._analyze_file(fp, fd)
        for c in comments:
            print(
                f"  Line {c.line_start}: [{c.severity.value}] {c.title} - {c.message}"
            )
