"""
테스트 생성 고도화 모듈
엣지 케이스, 파라미터 조합, 모킹 자동화
"""

from __future__ import annotations

import ast
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, ClassVar

log = logging.getLogger("autonomous_coding_agent.test_generator")


@dataclass
class TestCase:
    """단일 테스트 케이스"""
    name: str
    description: str
    inputs: dict[str, Any]
    expected: Any
    raises: type[Exception] | None = None
    marks: list[str] = field(default_factory=list)  # pytest.mark.xxx
    fixtures: list[str] = field(default_factory=list)


@dataclass
class ParameterizedTest:
    """파라미터화된 테스트"""
    function_name: str
    params: list[str]  # 파라미터 이름들
    test_cases: list[TestCase]
    fixture_deps: list[str] = field(default_factory=list)


@dataclass
class MockSpec:
    """목 사양"""
    target: str  # 모킹할 대상 (예: "httpx.AsyncClient.get")
    return_value: Any = None
    side_effect: Any = None
    spec: Any = None
    autospec: bool = False


@dataclass
class GeneratedTestModule:
    """생성된 테스트 모듈"""
    source_file: str
    test_file: str
    imports: list[str]
    fixtures: list[str]
    test_functions: list[str]
    parameterized_tests: list[ParameterizedTest]
    mocks: list[MockSpec]
    coverage_targets: list[str] = field(default_factory=list)


class EdgeCaseAnalyzer:
    """엣지 케이스 분석기"""

    # 타입별 기본 엣지 케이스
    EDGE_CASES: ClassVar[dict[str, list[Any]]] = {
        "str": [
            "",
            " ",
            "  leading/trailing  ",
            "unicode: 日本語",
            "special: <script>alert(1)</script>",
            "sql: ' OR '1'='1",
            "very_long: " + "a" * 10000,
            "newlines:\n\r\t",
            "null_byte: \x00",
        ],
        "int": [
            0,
            -1,
            1,
            -2**31,
            2**31 - 1,
            -2**63,
            2**63 - 1,
            999999999,
        ],
        "float": [
            0.0,
            -0.0,
            1.0,
            -1.0,
            float("inf"),
            float("-inf"),
            float("nan"),
            1e-10,
            1e10,
            3.14159265359,
        ],
        "bool": [True, False],
        "list": [
            [],
            [1],
            [1, 2, 3],
            [None, 1, None],
            ["a", "b", "c"],
            list(range(1000)),
        ],
        "dict": [
            {},
            {"key": "value"},
            {"a": 1, "b": 2},
            {"nested": {"deep": "value"}},
            {1: "int_key"},
            {None: "none_key"},
        ],
        "None": [None],
        "bytes": [
            b"",
            b"hello",
            b"\x00\xff",
            "hello".encode("utf-8"),
        ],
    }

    # 검증 관련 엣지 케이스
    VALIDATION_EDGE_CASES: ClassVar[dict[str, list[dict[str, Any]]]] = {
        "email": [
            {"input": "test@example.com", "valid": True},
            {"input": "invalid", "valid": False},
            {"input": "@example.com", "valid": False},
            {"input": "test@", "valid": False},
            {"input": "test..double@example.com", "valid": False},
            {"input": "test@example", "valid": False},
            {"input": "a" * 64 + "@example.com", "valid": True},
            {"input": "a" * 65 + "@example.com", "valid": False},
        ],
        "url": [
            {"input": "https://example.com", "valid": True},
            {"input": "http://localhost:8000", "valid": True},
            {"input": "ftp://example.com", "valid": True},
            {"input": "not-a-url", "valid": False},
            {"input": "http://", "valid": False},
        ],
        "uuid": [
            {"input": "550e8400-e29b-41d4-a716-446655440000", "valid": True},
            {"input": "invalid-uuid", "valid": False},
            {"input": "", "valid": False},
        ],
    }

    def __init__(self):
        pass

    def get_edge_cases_for_type(self, type_hint: str) -> list[Any]:
        """타입 힌트에서 엣지 케이스 추출"""
        type_hint = type_hint.lower()

        # Optional 처리
        if "optional" in type_hint or "|" in type_hint and "none" in type_hint:
            cases = [None]
        else:
            cases = []

        # 기본 타입 매칭
        for base_type, edge_cases in self.EDGE_CASES.items():
            if base_type in type_hint:
                cases.extend(edge_cases)

        return cases

    def get_validation_cases(self, field_name: str) -> list[dict[str, Any]]:
        """필드명으로 검증 케이스 추출"""
        field_lower = field_name.lower()

        for pattern, cases in self.VALIDATION_EDGE_CASES.items():
            if pattern in field_lower:
                return cases

        # 일반적인 필드 패턴
        if "password" in field_lower or "secret" in field_lower:
            return [
                {"input": "short", "valid": False, "reason": "too_short"},
                {"input": "a" * 8, "valid": True},
                {"input": "a" * 128, "valid": True},
                {"input": "a" * 129, "valid": False, "reason": "too_long"},
                {"input": "weakpassword", "valid": False, "reason": "no_uppercase"},
                {"input": "StrongPass123!", "valid": True},
            ]
        elif "name" in field_lower:
            return [
                {"input": "", "valid": False},
                {"input": "John", "valid": True},
                {"input": "J", "valid": True},
                {"input": "a" * 100, "valid": False},
                {"input": "John<script>", "valid": False},
            ]
        elif "age" in field_lower or "year" in field_lower:
            return [
                {"input": -1, "valid": False},
                {"input": 0, "valid": True},
                {"input": 18, "valid": True},
                {"input": 120, "valid": True},
                {"input": 150, "valid": False},
                {"input": "twenty", "valid": False},
            ]

        return []


class ParameterCombinationGenerator:
    """파라미터 조합 생성기"""

    def __init__(self, max_combinations: int = 50):
        self.max_combinations = max_combinations

    def generate_combinations(
        self,
        func_signature: dict[str, Any],
        edge_cases: dict[str, list[Any]],
    ) -> list[dict[str, Any]]:
        """함수 시그니처와 엣지 케이스로 조합 생성"""
        import itertools

        params = func_signature.get("params", [])
        param_names = [p["name"] for p in params]

        # 각 파라미터별 테스트 값 수집
        param_values = {}
        for name in param_names:
            if name in edge_cases:
                param_values[name] = edge_cases[name]
            else:
                # 타입 힌트에서 추출
                param_type = next((p.get("type", "") for p in params if p["name"] == name), "")
                analyzer = EdgeCaseAnalyzer()
                param_values[name] = analyzer.get_edge_cases_for_type(param_type)

            # 기본값이 있으면 추가
            default = next((p.get("default") for p in params if p["name"] == name), None)
            if default is not None and default not in param_values[name]:
                param_values[name].insert(0, default)

        # 카르테시안 곱 생성 (최대 제한)
        combinations = []
        keys = list(param_values.keys())
        values_lists = [param_values[k] for k in keys]

        for combo in itertools.product(*values_lists):
            combinations.append(dict(zip(keys, combo)))
            if len(combinations) >= self.max_combinations:
                break

        return combinations

    def generate_boundary_combinations(
        self,
        func_signature: dict[str, Any],
    ) -> list[dict[str, Any]]:
        """경계값 분석 기반 조합 생성"""
        params = func_signature.get("params", [])
        combinations = []

        for param in params:
            name = param["name"]
            param_type = param.get("type", "").lower()

            boundary_values = self._get_boundary_values(param_type)
            if boundary_values:
                for val in boundary_values:
                    combo = {p["name"]: p.get("default") for p in params}
                    combo[name] = val
                    combinations.append(combo)

        return combinations[:20]

    def _get_boundary_values(self, param_type: str) -> list[Any]:
        """타입별 경계값"""
        if "int" in param_type:
            return [0, 1, -1, 2**31 - 1, -2**31, 2**63 - 1, -2**63]
        elif "float" in param_type:
            return [0.0, -0.0, 1.0, -1.0, float("inf"), float("-inf"), 1e-10, 1e10]
        elif "str" in param_type:
            return ["", "a", "a" * 255, "a" * 256, "unicode: 日本語"]
        elif "list" in param_type or "array" in param_type:
            return [[], [1], [1] * 1000]
        return []


class MockGenerator:
    """자동 모킹 생성기"""

    # 일반적인 모킹 패턴
    COMMON_MOCKS: ClassVar[dict[str, MockSpec]] = {
        "httpx.AsyncClient": MockSpec(
            target="httpx.AsyncClient",
            return_value=None,  # 특수 처리로 AsyncClient 모킹
        ),
        "sqlalchemy.ext.asyncio.AsyncSession.execute": MockSpec(
            target="sqlalchemy.ext.asyncio.AsyncSession.execute",
            return_value={"scalars": {"all": [], "first": None, "one": None}, "fetchone": None, "fetchall": []},
        ),
        "redis.asyncio.Redis.get": MockSpec(
            target="redis.asyncio.Redis.get",
            return_value=None,
        ),
        "redis.asyncio.Redis.set": MockSpec(
            target="redis.asyncio.Redis.set",
            return_value=True,
        ),
        "fastapi.Depends": MockSpec(
            target="fastapi.Depends",
            return_value="mocked_dependency",
        ),
    }

    def __init__(self):
        self.mocks: list[MockSpec] = []

    def analyze_imports(self, source_code: str) -> list[str]:
        """소스 코드에서 import 분석하여 모킹 대상 추출"""
        imports = []
        tree = ast.parse(source_code)

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                for alias in node.names:
                    imports.append(f"{module}.{alias.name}")

        return imports

    def generate_mocks_for_imports(self, imports: list[str]) -> list[MockSpec]:
        """import 목록에서 필요한 모킹 생성"""
        mocks = []

        for imp in imports:
            # 직접 매칭
            if imp in self.COMMON_MOCKS:
                mocks.append(self.COMMON_MOCKS[imp])
                continue

            # 패턴 매칭
            for pattern, mock_spec in self.COMMON_MOCKS.items():
                if self._match_import(imp, pattern):
                    mocks.append(mock_spec)

        return mocks

    def _match_import(self, import_name: str, pattern: str) -> bool:
        """import와 패턴 매칭"""
        # 정확한 매칭
        if import_name == pattern:
            return True

        # 패턴이 import로 시작하는 경우 (예: import httpx, pattern httpx.AsyncClient.get)
        if pattern.startswith(import_name + "."):
            return True

        # 모듈 경로 매칭 (예: httpx.AsyncClient.get 매칭)
        pattern_parts = pattern.split(".")
        import_parts = import_name.split(".")

        if len(pattern_parts) <= len(import_parts):
            for i in range(len(pattern_parts)):
                if pattern_parts[i] != import_parts[i] and pattern_parts[i] != "*":
                    return False
            return True

        return False

    def generate_pytest_mock_fixtures(self, mocks: list[MockSpec]) -> list[str]:
        """pytest fixture 형태의 모킹 코드 생성"""
        fixtures = []

        for mock in mocks:
            fixture_name = mock.target.replace(".", "_").replace("(", "").replace(")", "").replace("[", "").replace("]", "")
            fixture_name = "mock_" + fixture_name[-50:]  # 길이 제한

            # return_value를 문자열로 직렬화 가능한 형태로 변환
            return_value_repr = "None"
            if mock.return_value is not None:
                try:
                    return_value_repr = repr(mock.return_value)
                except Exception:
                    return_value_repr = "{}"

            # lambda 등 호출 불가 객체 처리
            if "lambda" in return_value_repr or "<function" in return_value_repr:
                return_value_repr = '{"json": {"data": "mocked"}, "text": "mocked", "status_code": 200, "raise_for_status": None}'

            # AsyncClient.get/post 등의 메서드를 위한 async context manager 모킹
            fixture_code = f'''@pytest.fixture
def {fixture_name}(mocker):
    """Mock for {mock.target}"""
    from unittest.mock import AsyncMock
    mock_obj = mocker.patch("{mock.target}")'''

            # AsyncClient.get/post인 경우 async context manager 체인 모킹
            if "AsyncClient" in mock.target:
                fixture_code += '''
    # AsyncClient의 async context manager 체인 모킹
    async_client = AsyncMock()
    async_client.__aenter__ = AsyncMock(return_value=async_client)
    async_client.__aexit__ = AsyncMock(return_value=None)
    
    # get, post, put, delete 메서드 모킹
    from unittest.mock import Mock
    mock_response = AsyncMock()
    mock_response.json = Mock(return_value={"name": "Test User", "email": "test@example.com", "age": 30, "id": 1})
    mock_response.text = "mocked"
    mock_response.status_code = 200
    mock_response.raise_for_status = AsyncMock()
    
    async_client.get = AsyncMock(return_value=mock_response)
    async_client.post = AsyncMock(return_value=mock_response)
    async_client.put = AsyncMock(return_value=mock_response)
    async_client.delete = AsyncMock(return_value=mock_response)
    
    mock_obj.return_value = async_client'''
            elif mock.return_value is not None:
                fixture_code += f'\n    mock_obj.return_value = {return_value_repr}'
            if mock.side_effect is not None:
                fixture_code += f'\n    mock_obj.side_effect = {repr(mock.side_effect)}'
            if mock.autospec:
                fixture_code += '\n    mock_obj.autospec = True'

            fixture_code += '\n    return mock_obj'

            fixtures.append(fixture_code)

        return fixtures


class TestGenerator:
    """메인 테스트 생성기"""

    def __init__(self, workspace: str | Path):
        self.workspace = Path(workspace).resolve()
        self.edge_analyzer = EdgeCaseAnalyzer()
        self.param_generator = ParameterCombinationGenerator()
        self.mock_generator = MockGenerator()

    def generate_tests_for_file(
        self,
        source_file: str,
        test_framework: str = "pytest",
    ) -> GeneratedTestModule:
        """소스 파일에 대한 종합 테스트 생성"""
        source_path = self.workspace / source_file
        if not source_path.exists():
            raise FileNotFoundError(f"Source file not found: {source_file}")

        source_code = source_path.read_text(encoding="utf-8")

        # 1. AST 분석으로 함수/클래스 추출
        functions = self._extract_functions(source_code)
        classes = self._extract_classes(source_code)

        # 2. 모킹 생성
        imports = self.mock_generator.analyze_imports(source_code)
        mocks = self.mock_generator.generate_mocks_for_imports(imports)

        # 3. 각 함수에 대한 테스트 생성
        test_functions = []
        parameterized_tests = []
        coverage_targets = []

        for func in functions:
            if func["name"].startswith("_"):
                continue  # private 함수 스킵

            # 엣지 케이스 분석
            edge_cases = {}
            for param in func.get("params", []):
                edge_cases[param["name"]] = self.edge_analyzer.get_edge_cases_for_type(
                    param.get("type", "")
                )

            # 검증 필드 체크
            validation_cases = {}
            for param in func.get("params", []):
                validation_cases[param["name"]] = self.edge_analyzer.get_validation_cases(
                    param["name"]
                )

            # 파라미터 조합 생성
            combinations = self.param_generator.generate_combinations(
                func, edge_cases
            )
            boundary_combos = self.param_generator.generate_boundary_combinations(func)
            all_combos = combinations + boundary_combos

            # 테스트 케이스 생성
            test_cases = self._create_test_cases(
                func, all_combos, validation_cases
            )

            # 파라미터화된 테스트 생성
            if test_cases:
                param_test = ParameterizedTest(
                    function_name=func["name"],
                    params=list(func.get("params", [{}])[0].keys()) if func.get("params") else [],
                    test_cases=test_cases,
                    fixture_deps=[m.target for m in mocks if self._is_relevant_mock(m, func)],
                )
                parameterized_tests.append(param_test)

            # 일반 테스트 함수 생성
            test_func = self._generate_test_function(func, test_cases, mocks)
            test_functions.append(test_func)
            coverage_targets.append(func["name"])

        # 4. 테스트 파일 경로 결정
        test_file = self._get_test_file_path(source_file)

        # 5. import 문 생성
        imports = self._generate_imports(source_code, mocks, test_framework)

        # 6. fixture 생성
        fixtures = self.mock_generator.generate_pytest_mock_fixtures(mocks)

        return GeneratedTestModule(
            source_file=source_file,
            test_file=test_file,
            imports=imports,
            fixtures=fixtures,
            test_functions=test_functions,
            parameterized_tests=parameterized_tests,
            mocks=mocks,
            coverage_targets=coverage_targets,
        )

    def _extract_functions(self, source_code: str) -> list[dict[str, Any]]:
        """AST로 함수 추출"""
        functions = []
        tree = ast.parse(source_code)

        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                params = []
                args = node.args.args
                defaults = node.args.defaults
                # defaults는 뒤쪽 파라미터부터 매핑됨
                num_defaults = len(defaults)
                num_args = len(args)

                for i, arg in enumerate(args):
                    param_type = ""
                    if arg.annotation:
                        param_type = ast.unparse(arg.annotation) if hasattr(ast, "unparse") else ""

                    # 기본값 확인 (뒤쪽부터 매핑)
                    default = None
                    default_index = i - (num_args - num_defaults)
                    if default_index >= 0:
                        default = ast.unparse(defaults[default_index]) if hasattr(ast, "unparse") else ""

                    params.append({
                        "name": arg.arg,
                        "type": param_type,
                        "default": default,
                    })

                # 반환 타입
                return_type = ""
                if node.returns:
                    return_type = ast.unparse(node.returns) if hasattr(ast, "unparse") else ""

                # docstring
                docstring = ast.get_docstring(node)

                # 데코레이터
                decorators = []
                for dec in node.decorator_list:
                    if hasattr(ast, "unparse"):
                        decorators.append(ast.unparse(dec))

                functions.append({
                    "name": node.name,
                    "params": params,
                    "return_type": return_type,
                    "docstring": docstring,
                    "decorators": decorators,
                    "is_async": isinstance(node, ast.AsyncFunctionDef),
                    "lineno": node.lineno,
                    "source": ast.get_source_segment(source_code, node) if hasattr(ast, "get_source_segment") else "",
                })

        return functions

    def _extract_classes(self, source_code: str) -> list[dict[str, Any]]:
        """AST로 클래스 추출"""
        classes = []
        tree = ast.parse(source_code)

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                methods = []
                for item in node.body:
                    if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        methods.append(item.name)

                classes.append({
                    "name": node.name,
                    "methods": methods,
                    "bases": [ast.unparse(b) if hasattr(ast, "unparse") else "" for b in node.bases],
                    "lineno": node.lineno,
                })

        return classes

    def _create_test_cases(
        self,
        func: dict[str, Any],
        combinations: list[dict[str, Any]],
        validation_cases: dict[str, list[dict]],
    ) -> list[TestCase]:
        """조합에서 테스트 케이스 생성"""
        test_cases = []

        for i, combo in enumerate(combinations):
            # 검증 케이스 확인
            expected = None
            raises = None
            marks_set = set()

            for param_name, val_cases in validation_cases.items():
                if param_name in combo:
                    val = combo[param_name]
                    for vc in val_cases:
                        if vc["input"] == val:
                            if not vc["valid"]:
                                raises = Exception  # 구체적 예외는 추후 개선
                                marks_set.add("pytest.mark.xfail")
                            break

            test_cases.append(TestCase(
                name=f"test_{func['name']}_case_{i}",
                description=f"Test {func['name']} with {combo}",
                inputs=combo,
                expected=expected,
                raises=raises,
                marks=list(marks_set),
            ))

        return test_cases[:30]  # 최대 30개

    def _generate_test_function(
        self,
        func: dict[str, Any],
        test_cases: list[TestCase],
        mocks: list[MockSpec],
    ) -> str:
        """단일 테스트 함수 코드 생성"""
        func_name = func["name"]
        is_async = func.get("is_async", False)

        # 파라미터화된 테스트가 있으면 pytest.mark.parametrize 사용
        if test_cases:
            # 파라미터 이름 추출
            if test_cases[0].inputs:
                param_names = list(test_cases[0].inputs.keys())
                params_str = ", ".join(param_names)
            else:
                param_names = []
                params_str = ""

            # fixture 파라미터 추가 (mock fixture들)
            fixture_params = []
            for mock in mocks:
                if self._is_relevant_mock(mock, func):
                    fixture_name = "mock_" + mock.target.replace(".", "_")[-30:]
                    fixture_params.append(fixture_name)

            # parametrize에는 실제 함수 파라미터만 포함
            params_str = ", ".join(param_names)

            # 테스트 데이터 구성
            test_data = []
            for tc in test_cases:
                if tc.inputs:
                    test_data.append(tuple(tc.inputs.values()))
                else:
                    test_data.append(())

            # 마크 결정
            marks = set()
            for tc in test_cases:
                marks.update(tc.marks)

            # mock에서 async context manager 필요 여부 미리 확인 (더 이상 사용하지 않음)
            # has_async_with = False
            # if mocks:
            #     for mock in mocks:
            #         if self._is_relevant_mock(mock, func) and "AsyncClient" in mock.target:
            #             has_async_with = True
            #             break

            # 비동기 함수 처리 - 함수가 실제로 비동기일 때만 async/await 사용
            async_prefix = "async " if is_async else ""
            await_prefix = "await " if is_async else ""

            # 마크 문자열 생성
            marks_lines = [f"@{m}" for m in sorted(marks)]
            marks_str = "\n".join(marks_lines) + "\n" if marks_lines else ""

            # fixture 파라미터를 함수 시그니처에만 추가
            all_params = param_names + fixture_params
            all_params_str = ", ".join(all_params)

            test_code = f'''{marks_str}@pytest.mark.parametrize("{params_str}", {test_data})
{async_prefix}def test_{func_name}({all_params_str}):'''

            # 함수 바디
            body_lines = []
            has_async_with = False
            if mocks:
                # 관련 모킹 fixture 사용 - async context manager 체인 모킹
                for mock in mocks:
                    if self._is_relevant_mock(mock, func):
                        fixture_name = "mock_" + mock.target.replace(".", "_")[-30:]
                        if "AsyncClient" in mock.target:
                            # AsyncClient 모킹: 클래스를 패치하므로 async with 필요 없음
                            # mock fixture는 자동으로 적용됨 (pytest-mock)
                            body_lines.append(f"    # {mock.target} is mocked via {fixture_name} fixture")
                            continue
                        body_lines.append(f"    # {mock.target} is mocked via {fixture_name} fixture")

            if not any("async with" in line for line in body_lines):
                body_lines.append(f"    result = {await_prefix}{func_name}({', '.join(param_names)})")
            body_lines.append("    assert result is not None  # TODO: 구체적 검증 추가")

            test_code += "\n" + "\n".join(f"    {line}" for line in body_lines)

            return test_code

        # 파라미터화되지 않은 기본 테스트
        async_prefix = "async " if is_async else ""
        await_prefix = "await " if is_async else ""

        test_code = f'''{async_prefix}def test_{func_name}():
    """Test {func_name} basic functionality."""
    # TODO: 테스트 케이스 추가
    result = {await_prefix}{func_name}()
    assert result is not None'''

        return test_code

    def _is_relevant_mock(self, mock: MockSpec, func: dict[str, Any]) -> bool:
        """함수에 관련된 모킹인지 확인"""
        # 함수 본문에서 모킹 대상 사용 여부 확인
        func_source = func.get("source", "")
        target = mock.target
        
        # httpx.AsyncClient가 함수에서 사용되는지 확인
        if "AsyncClient" in target:
            # async with httpx.AsyncClient() as client: 패턴 확인
            if "AsyncClient" in func_source:
                return True
            # 또는 httpx.AsyncClient() 호출 확인
            if "httpx.AsyncClient" in func_source or "httpx.AsyncClient(" in func_source:
                return True
            return False
            
        # 다른 모킹도 대상 사용 여부 확인
        # 모듈/클래스 이름이 함수 소스에 있는지 확인
        parts = target.split(".")
        if len(parts) >= 2:
            # 클래스나 모듈 이름이 함수에 있는지 확인
            class_name = parts[-1] if not parts[-1].startswith("__") else parts[-2]
            if class_name in func_source:
                return True
                
        return False

    def _get_test_file_path(self, source_file: str) -> str:
        """테스트 파일 경로 생성"""
        path = Path(source_file)
        if path.name.startswith("test_"):
            return str(path)

        # tests/ 디렉토리 또는 같은 디렉토리
        tests_dir = self.workspace / "tests"
        if tests_dir.exists():
            return f"tests/test_{path.stem}.py"
        return f"test_{path.stem}.py"

    def _generate_imports(
        self,
        source_code: str,
        mocks: list[MockSpec],
        test_framework: str,
    ) -> list[str]:
        """테스트 파일에 필요한 import 생성"""
        imports = [
            "import pytest",
            "import pytest_asyncio",
            "from unittest.mock import AsyncMock, MagicMock, patch",
        ]

        # 소스 모듈 import (함수/클래스 가져오기)
        source_imports = self._extract_source_imports(source_code)
        imports.extend(source_imports)

        # httpx 등 외부 라이브러리
        if any("httpx" in str(m.target) for m in mocks):
            imports.append("import httpx")

        return imports

    def _extract_source_imports(self, source_code: str) -> list[str]:
        """소스 코드에서 함수/클래스 추출하여 import 문 생성"""
        imports = []
        try:
            tree = ast.parse(source_code)
            module_name = "service"  # 기본값, 실제로는 파일명에서 추출

            # 함수/클래스 이름 수집
            names = []
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if not node.name.startswith("_"):
                        names.append(node.name)
                elif isinstance(node, ast.ClassDef):
                    names.append(node.name)

            if names:
                imports.append(f"from {module_name} import {', '.join(sorted(set(names)))}")
        except Exception:
            pass

        return imports

    def write_test_file(self, module: GeneratedTestModule) -> Path:
        """테스트 파일 작성"""
        test_path = self.workspace / module.test_file
        test_path.parent.mkdir(parents=True, exist_ok=True)

        content = self._render_test_module(module)
        test_path.write_text(content, encoding="utf-8")
        log.info(f"테스트 파일 생성: {test_path}")
        return test_path

    def _render_test_module(self, module: GeneratedTestModule) -> str:
        """테스트 모듈 코드 렌더링"""
        lines = [
            '"""',
            f'Auto-generated tests for {module.source_file}',
            '"""',
            "",
        ]

        # Imports
        for imp in module.imports:
            lines.append(imp)
        lines.append("")

        # Fixtures
        for fixture in module.fixtures:
            lines.append(fixture)
            lines.append("")

        # Test functions
        for test_func in module.test_functions:
            lines.append(test_func)
            lines.append("")

        return "\n".join(lines)


def generate_tests(
    workspace: str | Path,
    source_file: str,
    test_framework: str = "pytest",
) -> GeneratedTestModule:
    """테스트 생성 편의 함수"""
    generator = TestGenerator(workspace)
    return generator.generate_tests_for_file(source_file, test_framework)


if __name__ == "__main__":
    # 테스트
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)

        # 샘플 소스 파일
        (tmp_path / "service.py").write_text('''
import httpx
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int

async def fetch_user(user_id: int) -> User:
    """Fetch user by ID."""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.example.com/users/{user_id}")
        response.raise_for_status()
        return User(**response.json())

def create_user(name: str, email: str, age: int) -> User:
    """Create new user."""
    if age < 0 or age > 150:
        raise ValueError("Invalid age")
    if "@" not in email:
        raise ValueError("Invalid email")
    return User(name=name, email=email, age=age)

def process_items(items: list[str]) -> dict[str, int]:
    """Process list of items."""
    return {item: len(item) for item in items}
''')

        # 테스트 생성
        module = generate_tests(tmp_path, "service.py")

        print(f"Source: {module.source_file}")
        print(f"Test file: {module.test_file}")
        print(f"Imports: {module.imports}")
        print(f"Fixtures: {len(module.fixtures)}개")
        print(f"Test functions: {len(module.test_functions)}개")
        print(f"Parameterized tests: {len(module.parameterized_tests)}개")
        print(f"Mocks: {len(module.mocks)}개")
        print(f"Coverage targets: {module.coverage_targets}")

        # 생성된 테스트 파일 출력
        print("\n=== Generated Test Module ===")
        test_path = Path(tmpdir) / module.test_file
        test_path.parent.mkdir(parents=True, exist_ok=True)
        test_path.write_text(module._render_test_module(module), encoding="utf-8")
        print(module._render_test_module(module)[:2000])