#!/usr/bin/env python3
"""Property-based tests for autonomous coding agent models and utilities."""

import pytest
from hypothesis import given, strategies as st, settings, assume
from pathlib import Path
import tempfile

from autonomous_coding_agent.models import (
    StepStatus, StepType, CodeSymbol, FileInfo, ExploreResult,
    PlanStep, Plan, VerificationResult, CritiqueResult, AgentState, AgentResult
)
from autonomous_coding_agent.explorer import CodeExplorer
from autonomous_coding_agent.planner import WorkPlanner
from autonomous_coding_agent.coder import CodeGenerator
from autonomous_coding_agent.verifier import Verifier


# ============================================================
# Hypothesis Strategies
# ============================================================

# Valid identifier characters (letters, digits, underscore)
IDENTIFIER_CHARS = st.characters(
    whitelist_categories=('Ll', 'Lu', 'Nd'),
    blacklist_characters=''
) | st.just('_')

@st.composite
def valid_identifier(draw):
    """유효한 식별자 생성 (시작은 문자나 _)"""
    first = draw(st.characters(whitelist_categories=('Ll', 'Lu')) | st.just('_'))
    rest = draw(st.text(alphabet=IDENTIFIER_CHARS, min_size=0, max_size=49))
    return first + rest


@st.composite
def valid_file_path(draw):
    """유효한 파일 경로 생성"""
    parts = draw(st.lists(valid_identifier(), min_size=1, max_size=4))
    name = draw(valid_identifier())
    ext = draw(st.sampled_from(['.py', '.js', '.ts', '.json', '.yaml', '.md']))
    return '/'.join(parts) + '/' + name + ext


@st.composite
def code_symbol(draw):
    """CodeSymbol 전략"""
    line_start = draw(st.integers(min_value=1, max_value=1000))
    line_end = draw(st.integers(min_value=line_start, max_value=1000))
    return CodeSymbol(
        name=draw(valid_identifier()),
        type=draw(st.sampled_from(['function', 'class', 'method', 'variable', 'import'])),
        file_path=draw(valid_file_path()),
        line_start=line_start,
        line_end=line_end,
        signature=draw(st.text(max_size=200)),
        docstring=draw(st.text(max_size=500)),
        references=draw(st.lists(valid_file_path(), max_size=5))
    )


@st.composite
def file_info(draw):
    """FileInfo 전략"""
    return FileInfo(
        path=draw(valid_file_path()),
        language=draw(st.sampled_from(['python', 'javascript', 'typescript', 'json', 'yaml', 'markdown'])),
        size=draw(st.integers(min_value=0, max_value=1000000)),
        lines=draw(st.integers(min_value=0, max_value=50000)),
        imports=draw(st.lists(st.text(max_size=100), max_size=20)),
        exports=draw(st.lists(st.text(max_size=100), max_size=20)),
    )


@st.composite
def explore_result(draw):
    """ExploreResult 전략"""
    symbols = draw(st.lists(code_symbol(), max_size=20))
    files = draw(st.lists(file_info(), max_size=20))
    return ExploreResult(
        symbols=symbols,
        files=files,
        import_graph=draw(st.dictionaries(valid_file_path(), st.lists(valid_file_path(), max_size=10), max_size=20)),
        call_graph=draw(st.dictionaries(st.text(max_size=50), st.lists(st.text(max_size=50), max_size=10), max_size=20)),
        entry_points=draw(st.lists(st.text(max_size=50), max_size=10)),
        config_files=draw(st.lists(valid_file_path(), max_size=10)),
        test_files=draw(st.lists(valid_file_path(), max_size=10)),
    )


@st.composite
def plan_step(draw):
    """PlanStep 전략"""
    step_id = draw(valid_identifier())
    return PlanStep(
        id=step_id,
        type=draw(st.sampled_from(list(StepType))),
        title=draw(st.text(max_size=100)),
        description=draw(st.text(max_size=500)),
        dependencies=draw(st.lists(valid_identifier(), max_size=5)),
        status=draw(st.sampled_from(list(StepStatus))),
        assigned_files=draw(st.lists(valid_file_path(), max_size=10)),
        expected_outputs=draw(st.lists(st.text(max_size=100), max_size=10)),
        verification_criteria=draw(st.lists(st.text(max_size=200), max_size=10)),
        max_retries=draw(st.integers(min_value=0, max_value=10)),
        retry_count=draw(st.integers(min_value=0, max_value=10)),
    )


@st.composite
def plan(draw):
    """Plan 전략"""
    steps = draw(st.lists(plan_step(), max_size=15))
    # Ensure unique IDs
    seen = set()
    unique_steps = []
    for step in steps:
        if step.id not in seen:
            seen.add(step.id)
            unique_steps.append(step)
    return Plan(
        goal=draw(st.text(max_size=500)),
        steps=unique_steps,
    )


@st.composite
def verification_result(draw):
    """VerificationResult 전략"""
    return VerificationResult(
        step_id=draw(st.text(max_size=50)),
        passed=draw(st.booleans()),
        test_results=draw(st.dictionaries(st.text(max_size=50), st.text(max_size=100), max_size=10)),
        lint_results=draw(st.dictionaries(st.text(max_size=50), st.text(max_size=100), max_size=10)),
        type_results=draw(st.dictionaries(st.text(max_size=50), st.text(max_size=100), max_size=10)),
        format_results=draw(st.dictionaries(st.text(max_size=50), st.text(max_size=100), max_size=10)),
        build_results=draw(st.dictionaries(st.text(max_size=50), st.text(max_size=100), max_size=10)),
        coverage=draw(st.floats(min_value=0.0, max_value=100.0)),
        errors=draw(st.lists(st.text(max_size=200), max_size=10)),
        warnings=draw(st.lists(st.text(max_size=200), max_size=10)),
        duration_seconds=draw(st.floats(min_value=0.0, max_value=3600.0)),
    )


@st.composite
def critique_result(draw):
    """CritiqueResult 전략"""
    return CritiqueResult(
        step_id=draw(st.text(max_size=50)),
        score=draw(st.floats(min_value=0.0, max_value=1.0)),
        issues=draw(st.lists(
            st.fixed_dictionaries({
                'type': st.text(max_size=50),
                'severity': st.sampled_from(['critical', 'error', 'warning', 'info', 'nit']),
                'file': st.text(max_size=100),
                'line': st.integers(min_value=0, max_value=10000),
                'message': st.text(max_size=500),
                'suggestion': st.text(max_size=500),
            }), max_size=10
        )),
        improvements=draw(st.lists(st.text(max_size=200), max_size=10)),
        should_retry=draw(st.booleans()),
        retry_feedback=draw(st.text(max_size=1000)),
    )


@st.composite
def agent_result(draw):
    """AgentResult 전략"""
    return AgentResult(
        success=draw(st.booleans()),
        summary=draw(st.text(max_size=1000)),
        files_changed=draw(st.lists(valid_file_path(), max_size=20)),
        files_created=draw(st.lists(valid_file_path(), max_size=20)),
        files_modified=draw(st.lists(valid_file_path(), max_size=20)),
        test_results=draw(st.dictionaries(st.text(max_size=50), st.text(max_size=100), max_size=20)),
        verification_results=draw(st.lists(verification_result(), max_size=10)),
        critique_results=draw(st.lists(critique_result(), max_size=10)),
        duration_seconds=draw(st.floats(min_value=0.0, max_value=7200.0)),
        iterations_used=draw(st.integers(min_value=0, max_value=20)),
        error=draw(st.one_of(st.none(), st.text(max_size=500))),
    )


# ============================================================
# Property Tests for Models
# ============================================================

class TestModelProperties:
    """데이터 모델의 불변식 및 속성 검증"""

    @given(code_symbol())
    @settings(max_examples=100)
    def test_code_symbol_line_order(self, symbol: CodeSymbol):
        """line_start <= line_end 불변식"""
        assert symbol.line_start <= symbol.line_end, f"line_start({symbol.line_start}) > line_end({symbol.line_end})"

    @given(code_symbol())
    @settings(max_examples=100)
    def test_code_symbol_name_not_empty(self, symbol: CodeSymbol):
        """이름이 비어있지 않음"""
        assert len(symbol.name.strip()) > 0

    @given(file_info())
    @settings(max_examples=100)
    def test_file_info_size_lines_non_negative(self, info: FileInfo):
        """크기와 라인 수는 음수가 아님"""
        assert info.size >= 0
        assert info.lines >= 0

    @given(explore_result())
    @settings(max_examples=50)
    def test_explore_result_consistency(self, result: ExploreResult):
        """탐색 결과의 일관성"""
        for symbol in result.symbols:
            assert symbol.file_path is not None
            assert len(symbol.name) > 0
        
        for file_path in result.import_graph.keys():
            assert len(file_path) > 0

    @given(plan())
    @settings(max_examples=50)
    def test_plan_step_ids_unique(self, plan_obj: Plan):
        """계획 단계 ID는 유일함"""
        ids = [step.id for step in plan_obj.steps]
        assert len(ids) == len(set(ids)), "중복된 단계 ID 존재"

    @given(plan())
    @settings(max_examples=50)
    def test_plan_get_ready_steps_only_pending(self, plan_obj: Plan):
        """get_ready_steps는 PENDING 단계만 반환"""
        ready = plan_obj.get_ready_steps()
        for step in ready:
            assert step.status == StepStatus.PENDING

    @given(plan())
    @settings(max_examples=50)
    def test_plan_get_ready_steps_deps_satisfied(self, plan_obj: Plan):
        """준비된 단계의 의존성은 모두 완료됨"""
        ready = plan_obj.get_ready_steps()
        completed_ids = {s.id for s in plan_obj.steps if s.status == StepStatus.COMPLETED}
        
        for step in ready:
            for dep in step.dependencies:
                assert dep in completed_ids, f"의존성 {dep} 미완료"

    @given(plan())
    @settings(max_examples=50)
    def test_plan_is_complete_all_done(self, plan_obj: Plan):
        """모든 단계가 완료/스킵이면 is_complete=True"""
        for step in plan_obj.steps:
            step.status = StepStatus.COMPLETED
        assert plan_obj.is_complete()

    @given(plan())
    @settings(max_examples=50)
    def test_plan_has_failures_detects_failed(self, plan_obj: Plan):
        """실패한 단계가 있으면 has_failures=True"""
        if plan_obj.steps:
            plan_obj.steps[0].status = StepStatus.FAILED
            assert plan_obj.has_failures()
        
        for step in plan_obj.steps:
            step.status = StepStatus.COMPLETED
        assert not plan_obj.has_failures()

    @given(verification_result())
    @settings(max_examples=50)
    def test_verification_result_coverage_range(self, result: VerificationResult):
        """커버리지는 0-100 범위"""
        assert 0.0 <= result.coverage <= 100.0

    @given(critique_result())
    @settings(max_examples=50)
    def test_critique_result_score_range(self, result: CritiqueResult):
        """점수는 0.0-1.0 범위"""
        assert 0.0 <= result.score <= 1.0

    @given(critique_result())
    @settings(max_examples=50)
    def test_critique_issue_severity_valid(self, result: CritiqueResult):
        """이슈 심각도는 유효한 값"""
        valid_severities = {'critical', 'error', 'warning', 'info', 'nit'}
        for issue in result.issues:
            assert issue['severity'] in valid_severities

    @given(agent_result())
    @settings(max_examples=50)
    def test_agent_result_duration_non_negative(self, result: AgentResult):
        """소요 시간은 음수가 아님"""
        assert result.duration_seconds >= 0.0
        assert result.iterations_used >= 0


# ============================================================
# Property Tests for Explorer
# ============================================================

class TestExplorerProperties:
    """CodeExplorer 속성 테스트"""

    @given(st.text(min_size=10, max_size=5000))
    @settings(max_examples=20, deadline=5000)
    def test_explorer_handles_any_python_code(self, code: str):
        """임의의 Python 코드도 에러 없이 탐색 시도"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            test_file = tmp_path / "test.py"
            test_file.write_text(code)
            
            explorer = CodeExplorer(tmp_path)
            result = explorer.explore()
            assert isinstance(result, ExploreResult)

    @given(st.lists(st.text(min_size=1, max_size=100), min_size=1, max_size=10))
    @settings(max_examples=20, deadline=5000)
    def test_explorer_multiple_files(self, file_contents: list[str]):
        """다중 파일 탐색"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            for i, content in enumerate(file_contents):
                (tmp_path / f"file_{i}.py").write_text(content)
            
            explorer = CodeExplorer(tmp_path)
            result = explorer.explore()
            assert isinstance(result, ExploreResult)
            assert len(result.files) >= len(file_contents)


# ============================================================
# Property Tests for Planner
# ============================================================

class TestPlannerProperties:
    """WorkPlanner 속성 테스트"""

    @given(st.text(min_size=10, max_size=500))
    @settings(max_examples=20, deadline=10000)
    def test_planner_creates_plan_for_any_goal(self, goal: str):
        """임의 목표에 대해 계획 생성"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            (tmp_path / "main.py").write_text("# Sample\nprint('hello')")
            
            explorer = CodeExplorer(tmp_path)
            explore_result = explorer.explore()
            
            planner = WorkPlanner(tmp_path)
            plan = planner.create_plan(goal=goal, explore_result=explore_result, task_type='feature')
            
            assert isinstance(plan, Plan)
            assert plan.goal == goal
            assert len(plan.steps) > 0
            for step in plan.steps:
                assert step.type in StepType
                assert step.status == StepStatus.PENDING

    @given(st.text(min_size=10, max_size=500))
    @settings(max_examples=20, deadline=10000)
    def test_planner_task_types(self, goal: str):
        """다양한 작업 유형 처리"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            (tmp_path / "main.py").write_text("# Sample")
            
            explorer = CodeExplorer(tmp_path)
            explore_result = explorer.explore()
            
            planner = WorkPlanner(tmp_path)
            
            for task_type in ['feature', 'bugfix', 'refactor', 'test', 'docs']:
                plan = planner.create_plan(goal=goal, explore_result=explore_result, task_type=task_type)
                assert isinstance(plan, Plan)
                assert len(plan.steps) > 0


# ============================================================
# Property Tests for Verifier
# ============================================================

class TestVerifierProperties:
    """Verifier 속성 테스트"""

    @given(st.text(min_size=1, max_size=200))
    @settings(max_examples=10, deadline=5000)
    def test_verifier_step_id_consistency(self, step_id: str):
        """검증 결과의 step_id 일치"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            (tmp_path / "main.py").write_text("def hello():\n    return 'world'\n")
            
            verifier = Verifier(tmp_path)
            
            from autonomous_coding_agent.models import PlanStep, StepType, StepStatus
            step = PlanStep(
                id=step_id,
                type=StepType.CODE,
                title="Test",
                description="Test step"
            )
            
            result = verifier.verify_step(step, ['main.py'])
            assert result.step_id == step_id


# ============================================================
# Property Tests for Coder (CodeGenerator)
# ============================================================

class TestCoderProperties:
    """CodeGenerator 속성 테스트"""

    @given(st.text(min_size=10, max_size=500))
    @settings(max_examples=10, deadline=30000)
    def test_coder_generates_syntax_valid_python(self, goal: str):
        """생성된 코드는 문법적으로 유효"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            (tmp_path / "main.py").write_text("# Existing code\n")
            
            explorer = CodeExplorer(tmp_path)
            explore_result = explorer.explore()
            
            planner = WorkPlanner(tmp_path)
            plan = planner.create_plan(goal=goal, explore_result=explore_result, task_type='feature')
            
            coder = CodeGenerator(tmp_path)
            code_step = plan.get_ready_steps()[0] if plan.get_ready_steps() else plan.steps[0]
            
            context = {
                'goal': goal,
                'explore_result': explore_result,
                'plan': plan,
                'workspace': tmp_path,
                'config': {'verify_tests': True, 'verify_lint': True, 'verify_types': True}
            }
            
            result = coder.execute_step(code_step, context)
            
            # 생성된 파일들 파싱 가능 확인
            artifacts = result.get('artifacts', {}) if isinstance(result, dict) else {}
            for file_path in artifacts.get('files_created', []):
                full_path = tmp_path / file_path
                if full_path.exists() and file_path.endswith('.py'):
                    import ast
                    try:
                        ast.parse(full_path.read_text())
                    except SyntaxError:
                        pytest.fail(f"생성된 파일이 문법 오류: {file_path}")


# ============================================================
# Round-trip Serialization Tests
# ============================================================

class TestSerializationProperties:
    """직렬화/역직렬화 라운드트립 테스트"""

    @given(code_symbol())
    @settings(max_examples=50)
    def test_code_symbol_json_roundtrip(self, symbol: CodeSymbol):
        """CodeSymbol JSON 직렬화 라운드트립"""
        import json
        data = {
            'name': symbol.name,
            'type': symbol.type,
            'file_path': symbol.file_path,
            'line_start': symbol.line_start,
            'line_end': symbol.line_end,
            'signature': symbol.signature,
            'docstring': symbol.docstring,
            'references': symbol.references,
        }
        json_str = json.dumps(data, ensure_ascii=False)
        restored = json.loads(json_str)
        
        assert restored['name'] == symbol.name
        assert restored['type'] == symbol.type
        assert restored['file_path'] == symbol.file_path
        assert restored['line_start'] == symbol.line_start
        assert restored['line_end'] == symbol.line_end

    @given(plan())
    @settings(max_examples=20)
    def test_plan_json_roundtrip(self, plan_obj: Plan):
        """Plan JSON 직렬화 라운드트립"""
        import json
        data = {
            'goal': plan_obj.goal,
            'steps': [
                {
                    'id': s.id,
                    'type': s.type.value,
                    'title': s.title,
                    'description': s.description,
                    'dependencies': s.dependencies,
                    'status': s.status.value,
                    'assigned_files': s.assigned_files,
                    'expected_outputs': s.expected_outputs,
                    'verification_criteria': s.verification_criteria,
                    'max_retries': s.max_retries,
                    'retry_count': s.retry_count,
                }
                for s in plan_obj.steps
            ],
        }
        json_str = json.dumps(data, ensure_ascii=False, default=str)
        restored = json.loads(json_str)
        
        assert restored['goal'] == plan_obj.goal
        assert len(restored['steps']) == len(plan_obj.steps)
        for orig, rest in zip(plan_obj.steps, restored['steps']):
            assert rest['id'] == orig.id
            assert rest['type'] == orig.type.value


if __name__ == '__main__':
    pytest.main([__file__, '-v', '--tb=short'])