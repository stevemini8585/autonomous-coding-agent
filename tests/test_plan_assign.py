"""플래너 파일 지정 + coder 미지원 확장자 테스트"""

from pathlib import Path

from autonomous_coding_agent.coder import CodeGenerator
from autonomous_coding_agent.models import (
    CodeSymbol,
    ExploreResult,
    FileInfo,
    StepType,
)
from autonomous_coding_agent.planner import WorkPlanner


def _explore():
    return ExploreResult(
        symbols=[
            CodeSymbol(
                name="join_types",
                type="function",
                file_path="src/pkg/types.py",
                line_start=1,
                line_end=5,
            ),
            CodeSymbol(
                name="unrelated",
                type="function",
                file_path="src/pkg/other.py",
                line_start=1,
                line_end=5,
            ),
        ],
        files=[
            FileInfo(path="src/pkg/types.py", language="python", size=100, lines=50),
            FileInfo(path="src/pkg/other.py", language="python", size=100, lines=50),
            FileInfo(path="tests/test_types.py", language="python", size=50, lines=20),
            FileInfo(path="tests/integration/test_e2e.py", language="python", size=200, lines=100),
            FileInfo(path="docs/page.html", language="html", size=500, lines=400),
        ],
    )


def _code_files(goal):
    planner = WorkPlanner(Path())
    plan = planner.create_plan(goal, _explore())
    code_steps = [s for s in plan.steps if s.type == StepType.CODE]
    assert code_steps
    return code_steps[0].assigned_files


class TestAssign:
    def test_explicit_path_first(self):
        files = _code_files("tests/test_types.py에 엣지 테스트 추가")
        assert files[0] == "tests/test_types.py"

    def test_basename_match(self):
        # 파일명만 언급돼도 해당 파일이 1순위
        files2 = _code_files("other.py 관련 수정")
        assert files2[0] == "src/pkg/other.py"

    def test_symbol_match(self):
        files = _code_files("join_types 버그 수정")
        assert files[0] == "src/pkg/types.py"

    def test_cap_three(self):
        files = _code_files("전체 리팩토링")
        assert len(files) <= 3

    def test_html_never_for_python_task(self):
        files = _code_files("join_types 엣지 케이스 테스트 추가")
        assert "docs/page.html" not in files


class TestUnknownExt:
    def test_existing_unchanged(self, tmp_path):
        html = "<html>\n" * 100
        (tmp_path / "p.html").write_text(html)
        gen = CodeGenerator(tmp_path)
        from autonomous_coding_agent.models import PlanStep

        step = PlanStep(
            id="s", type=StepType.CODE, title="t", description="d", assigned_files=["p.html"]
        )
        impl = gen._generate_task_specific_implementation(step, "goal", {})
        assert impl["p.html"] == html  # 무변경
