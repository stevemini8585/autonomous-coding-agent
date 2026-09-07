---
name: autonomous-coding-agent
description: Use when need Codex/Claude Code level autonomous coding. Self-contained agent that explores codebase, plans work, writes code, runs tests, and iterates until verified.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [autonomous, coding, agent, codex, claude-code, self-improving]
    related_skills: [codex, claude-code, hermes-agent, test-driven-development, systematic-debugging]
---

# 자율 코딩 에이전트 (Autonomous Coding Agent)

Codex/Claude Code 수준의 완전 자율 코딩 파이프라인. Hermes 내부에서 동작하며 기존 도구들(terminal, search_files, patch, read_file, write_file)을 조합해 엔드투엔드 자율 개발을 수행.

## 핵심 아키텍처

```\n┌─────────────────────────────────────────────────────────────┐\n│  AutonomousCodingAgent                                        │\n├─────────────────────────────────────────────────────────────┤\n│  1. Explorer    → 코드베이스 인덱싱, 심볼 검색, 의존성 분석   │\n│  2. Planner     → 작업 분해, 단계별 계획 수립, 의존성 순서   │\n│  3. Coder       → 코드 생성/수정 (patch/write_file)          │\n│  4. Verifier    → 테스트 실행, 린트, 타입체크, 빌드 검증     │\n│  5. Critic      → 결과 평가, 이슈 발견, 개선점 도출          │\n│  6. Git         → Git/GitHub 연동 (이슈→브랜치→PR 자동화)     │\n│  7. IssueParser → 이슈 본문 파싱, 작업 분해, 의존성 추론     │\n│  8. PRReviewer  → PR 자동 리뷰 (보안/성능/스타일 탐지)       │\n│  9. Controller  → 루프 제어, 상태 관리, 재시도/롤백 결정     │\n│  10. TestGen    → 테스트 자동 생성 (엣지케이스/파라미터조합/모킹) │\n└─────────────────────────────────────────────────────────────┘\n```

## 워크플로우

```
사용자 요청
    ↓
[Explorer] 코드베이스 스캔 → 컨텍스트 수집
    ↓
[Planner] 작업 분해 → 단계별 Todo 생성
    ↓
[IssueParser] GitHub 이슈 파싱 → 작업 분해/의존성 추론 (이슈 기반 시)
    ↓
[Controller] 각 단계 실행 (병렬/순차 선택 가능)
    ├─→ [Coder] 코드 작성/수정 (PatchManager로 원자적 멀티파일 편집)
    ├─→ [Git] 브랜치 생성/커밋/푸시
    ├─→ [Verifier] 테스트/린트/빌드 실행 (ruff/black/mypy/pytest)
    ├─→ [Critic] 결과 분석 → PASS 시 다음 단계
    │              └─→ FAIL 시 피드백 생성 → [Coder] 재시도 (최대 N회)
    └─→ [PRReviewer] PR 자동 리뷰 (보안/성능/스타일 탐지)
    ↓
[Git] PR 생성 (GitHub 이슈 연결)
    ↓
[Controller] 전체 완료 검증 → 사용자 보고
```

## 주요 기능

### 1. 코드베이스 탐색 (Explorer)
- `search_files` + `read_file`로 심볼/파일/의존성 매핑
- 언어별 파서 트리 (Python AST, TS/JS, Go, Rust 등)
- 임포트 그래프, 호출 그래프 구성
- 관련 파일 자동 추천

### 2. 작업 계획 (Planner)
- 자연어 요청 → 구조화된 단계 리스트
- 의존성 순서 토폴로지 정렬
- 병렬 가능 단계 식별
- 리스크 평가 및 롤백 포인트 설정

### 3. 코드 생성 (Coder)
- `patch` 도구로 정밀 수정 (fuzzy matching)
- `write_file`로 신규 파일 생성
- **PatchManager**: 퍼지 매칭, 원자적 멀티파일 편집, 백업/롤백
- 템플릿/패턴 기반 보일러플레이트
- 컨벤션 준수 (프로젝트 기존 스타일 따름)

### 4. 검증 루프 (Verifier)
- 단위/통합 테스트 실행 (`pytest`, `go test`, `cargo test` 등)
- 린터/포맷터 (`ruff`, `black`, `eslint`, `prettier`)
- 타입 체커 (`mypy`, `pyright`, `tsc`)
- 빌드/컴파일 검증
- 커버리지 리포트

### 5. 비평/개선 (Critic)
- 테스트 실패 로그 분석 → 근본 원인 추출
- 코드 품질 메트릭 (복잡도, 중복, 커플링)
- 보안/성능 안티패턴 탐지
- 개선 제안 우선순위화

### 6. Git/GitHub 연동 (Git + GitHub)
- **GitManager**: 로컬 Git 작업 (status, branch, commit, log, diff, push)
- **GitHubClient**: `gh` CLI 래퍼 (Issue/PR/Repo CRUD)
- **GitWorkflow**: 이슈→브랜치→커밋→푸시→PR 자동화 파이프라인
- 이슈 번호 기반 안전한 브랜치명 생성 (`issue-{num}-{slug}`)
- PR 자동 생성 및 베이스 브랜치 관리

### 7. 이슈 파싱 & 작업 분해 (IssueParser)
- GitHub 이슈 본문에서 작업 항목 자동 추출 (불릿/번호/문장)
- 기술 스택 힌트 감지 (12개 카테고리: python, auth, api, database 등)
- 파일 힌트 추출 (백틱/일반 텍스트 내 파일명)
- 작업 유형 분류 (CREATE/MODIFY/DELETE/REFACTOR/TEST/DOCS/CONFIG)
- 우선순위 판별 (CRITICAL/HIGH/MEDIUM/LOW)
- **의존성 자동 추론**: 레이어 기반 (model→service→controller→test)
- 예상 소요 시간 계산, 승인 기준 추출
- 실행 순서 위상 정렬 제공

### 8. PR 자동 리뷰 (PRReviewer)
- PR Diff 파싱 (`gh pr diff`) → 파일별 변경사항 추출
- 추가된 라인만 분석 (라인 번호 추적)
- **보안 패턴 10개**: SQL 인젝션, 하드코딩 시크릿, XSS, 경로 순회, 약한 암호화, 디버그 코드, 명령어 인젝션, 코드 인젝션, 시크릿 유출
- **성능 패턴 5개**: N+1 쿼리, 비효율 리스트 연산, 중복 계산, 깊은 복사
- **정확성 패턴 5개**: 빈 except, 가변 기본 인자, 리소스 누수, 불필요한 비교, 수정 전 데이터
- **유지보수성 패턴 4개**: 긴 함수, 깊은 중첩, 매직 넘버, TODO/FIXME
- **스타일 패턴 3개**: 타입 힌트/도큐스트링/import 순서
- **자동 수정 제안 (Suggestion)**: 모든 패턴에 구체적 코드 수정 예시 제공
- 정적 분석 도구 연동: `ruff` (린트), `mypy` (타입) JSON 출력 파싱
- GitHub 리뷰 코멘트 자동 생성 (`gh api`로 PR 리뷰 게시)
- Critical/Error/Warning/Info/Nit 5단계 심각도 분류

### 9. 상태 관리 & 병렬 실행 (Controller)
- 세션별 상태 영구 저장 (skills/memory)
- 체크포인트/롤백 지원
- **ThreadPoolExecutor 병렬 실행** (최대 4 workers, 스레드 격리 컨텍스트)
- 진행률 추적, 타임아웃 처리
- 사람 개입 지점 (HITL) 알림

### 10. 테스트 자동 생성 (TestGenerator)
- **엣지 케이스 분석**: 타입별 경계값/무효값/특수문자 자동 추출 (str 9종, int 8종, float 8종, bool/list/dict 등)
- **검증 케이스 생성**: 필드별 의미적 검증 (email, password, name, age, URL, UUID 등)
- **파라미터 조합**: 카르테시안 곱 + 경계값 분석 + Equivalence Partitioning + Pairwise (최대 50개)
- **자동 모킹**: httpx.AsyncClient, SQLAlchemy AsyncSession, Redis, FastAPI Depends 등 6종 라이브러리 지원
- **pytest-asyncio 지원**: 비동기 함수 자동 감지 → `async def` + `await` + `--asyncio-mode=auto`
- **파라미터화 테스트**: `pytest.mark.parametrize` 자동 생성 (입력값 + fixture 파라미터 분리)
- **픽스처 생성**: `pytest-mock` 기반 모킹 픽스처 자동 생성 (async context manager 체인 포함)
- **소스 import 자동화**: AST로 함수/클래스 추출 → 테스트 파일 import 자동 구성
- **마크/픽스처 적용**: `xfail`, `fixture`, `parametrize` 자동 적용

## 사용법

```python
from skills.autonomous_coding_agent import AutonomousCodingAgent

agent = AutonomousCodingAgent(
    workspace="/path/to/project",
    model="auto",  # Hermes 현재 모델 사용
    max_iterations=5,
    timeout_per_step=300,
)

# 자연어 요청으로 자율 실행
result = agent.run("""
기능 추가: 사용자 알림 시스템
- 이메일/슬랙/텔레그램 멀티채널 지원
- 템플릿 엔진 (Jinja2)
- 재시도/큐잉/레이트리밋
- 테스트 커버리지 80% 이상
""")

print(result.summary)
print(result.files_changed)
print(result.test_results)
```

## 설정 옵션

```yaml
# ~/.hermes/skills/autonomous-coding-agent/config.yaml
autonomous_coding_agent:
  max_iterations: 5              # 단계당 최대 재시도
  timeout_per_step: 300          # 단계당 타임아웃(초)
  parallel_steps: true           # 독립 단계 병렬 실행
  verify_tests: true             # 테스트 강제 검증
  verify_lint: true              # 린트 강제 검증
  verify_types: true             # 타입 체크 강제 검증
  coverage_threshold: 80         # 최소 커버리지 %
  auto_commit: false             # 완료 시 자동 커밋
  hitl_on_failure: true          # 반복 실패 시 사람 개입 요청
  language_configs:
    python:
      test_cmd: "pytest -xvs"
      lint_cmd: "ruff check ."
      type_cmd: "mypy ."
      format_cmd: "black ."
    typescript:
      test_cmd: "vitest run"
      lint_cmd: "eslint ."
      type_cmd: "tsc --noEmit"
      format_cmd: "prettier --write ."
```

## 스킬 내부 구조

```\nskills/autonomous-coding-agent/\n├── SKILL.md                    # 이 파일\n├── config.yaml                 # 설정\n├── src/\n│   ├── __init__.py             # 통합 export\n│   ├── agent.py                # 메인 컨트롤러 (병렬 실행 지원)\n│   ├── explorer.py             # 코드베이스 탐색\n│   ├── planner.py              # 작업 계획\n│   ├── coder.py                # 코드 생성/수정\n│   ├── verifier.py             # 검증 실행\n│   ├── critic.py               # 결과 비평\n│   ├── state.py                # 상태 관리\n│   ├── models.py               # 데이터 모델\n│   ├── git.py                  # GitManager\n│   ├── github.py               # GitHubClient\n│   ├── git_integration.py      # GitWorkflow\n│   ├── patch_utils.py          # PatchManager\n│   ├── issue_parser.py         # IssueParser\n│   ├── pr_reviewer.py          # PRReviewer\n│   ├── web_search.py           # WebSearcher + DocumentationParser + VersionChecker\n│   ├── code_adapter.py         # CodeExampleAdapter/Applier\n│   └── test_generator.py       # TestGenerator (엣지케이스/모킹/파라미터조합)\n├── templates/\n│   ├── python/\n│   ├── typescript/\n│   └── common/\n└── tests/\n    ├── test_agent.py\n    └── fixtures/\n```

## 확장 포인트

- **언어 플러그인**: 새 언어 지원 추가 (explorer/verifier 템플릿)
- **도구 플러그인**: 커스텀 검증 도구 등록
- **모델 선택**: 작업 유형별 최적 모델 라우팅
- **후처리 훅**: 완료 시 알림, PR 생성, 배포 트리거 등

## 안전장치

- 샌드박스 실행 환경 (Docker/가상환경 격리)
- 파괴적 명령 차단 (`rm -rf`, `git push --force` 등)
- 변경 사항 미리보기 (diff) 후 적용
- 중요 파일 보호 패턴 설정
- 롤백 가능한 체크포인트 자동 생성

## 의존성 설치

```bash
# Hermes venv 필수 (시스템 Python 3.9 pip 깨짐)
/Users/steve-mini/.hermes/hermes-agent/venv/bin/pip install pytest pytest-asyncio pytest-mock httpx pydantic ruff black mypy
```

## 알려진 문제 & 해결

### pytest-asyncio 비동기 테스트 실행
- `pytest-asyncio` 설치 필수: `pip install pytest-asyncio`
- 실행 시 `--asyncio-mode=auto` 옵션 사용
- 비동기 함수: `async def test_xxx()` + `await func()`

### httpx.AsyncClient 모킹
- `pytest-mock` 설치 필수: `pip install pytest-mock`
- `mocker.patch("httpx.AsyncClient")`로 클래스 패치
- `AsyncMock` + `__aenter__`/`__aexit__`로 async context manager 체인 모킹
- `response.json`은 **동기 메서드** → `Mock(return_value=...)` 사용 (AsyncMock 아님)
- `response.raise_for_status`는 비동기 → `AsyncMock()` 사용

### 패키지 매니저 감지 (ProjectAnalyzer)
- Poetry: `pyproject.toml` `[tool.poetry]` 또는 `poetry.lock`
- PDM: `pyproject.toml` `[tool.pdm]` 또는 `pdm.lock`
- Hatch: `pyproject.toml` `[tool.hatch]` 또는 `hatch.toml`
- Rye: `rye.toml` 또는 `rye.lock`
- uv: `uv.lock` 또는 `[tool.uv]`
- Pipenv: `Pipfile`
- Conda: `environment.yml` / `conda-lock.yml`
- pip: `requirements*.txt`, `setup.py`, `setup.cfg`, `[build-system]`
- Node.js: `pnpm-lock.yaml` > `yarn.lock` > `package-lock.json`
- Rust: `Cargo.toml`
- Go: `go.mod`

## Hermes 통합

- `hermes send "자율 에이전트로 이슈 #123 해결해줘"`로 호출
- 진행 상황 실시간 스트리밍 (Telegram/데스크톱)
- 스킬 메모리에 학습 내용 축적 (패턴, 안티패턴, 프로젝트 컨벤션)
- 다른 스킬들과 조합 가능 (github-issue-to-pr, code-review 등)