"""llm_planner/llm_critic 테스트 — 키 없이 템플릿 경로 + 순수 로직"""

import pytest

from autonomous_coding_agent.llm_critic import LLMCritic, create_llm_critic
from autonomous_coding_agent.llm_planner import LLMPlanner, create_llm_planner
from autonomous_coding_agent.models import (
    CodeSymbol,
    ExploreResult,
    FileInfo,
    PlanStep,
    StepType,
    VerificationResult,
)


def _explore():
    return ExploreResult(
        symbols=[CodeSymbol(name="f", type="function", file_path="m.py", line_start=1, line_end=5)],
        files=[FileInfo(path="m.py", language="python", size=50, lines=10)],
    )


@pytest.fixture
def planner(tmp_path):
    return LLMPlanner(tmp_path)


@pytest.fixture
def critic(tmp_path):
    return LLMCritic(tmp_path)


class TestPlannerBasics:
    def test_no_keys_template(self, planner):
        assert planner.provider == "template"

    def test_task_types(self, planner):
        assert planner._detect_task_type("버그 수정해줘") != ""
        assert planner._detect_task_type("새 기능 추가") != ""
        assert planner._detect_task_type("리팩토링 필요") != ""
        assert planner._detect_task_type("zzz") != ""

    def test_similarity(self, planner):
        a = {"steps": [{"title": "a"}, {"title": "b"}]}
        assert planner._plan_similarity(a, a) == pytest.approx(1.0)
        b = {"steps": [{"title": "x"}]}
        assert 0 <= planner._plan_similarity(a, b) <= 1.0

    def test_select_consistent(self, planner):
        plans = [
            {"steps": [{"title": "a"}]},
            {"steps": [{"title": "a"}, {"title": "b"}]},
            {"steps": [{"title": "a"}]},
        ]
        best = planner._select_consistent_plan(plans)
        assert best["steps"][0]["title"] == "a"

    def test_select_empty(self, planner):
        assert planner._select_consistent_plan([]) == {}

    def test_build_prompt(self, planner):
        p = planner._build_prompt("goal", "bug", _explore(), [])
        assert "goal" in p

    def test_topological(self, planner):
        from autonomous_coding_agent.models import Plan

        plan = planner._build_plan_from_data(
            {"steps": [{"title": "s1", "type": "code"}]}, "g", "bug"
        )
        assert isinstance(plan, Plan) and len(plan.steps) >= 1

    def test_create_plan_template(self, planner):
        plan = planner.create_plan("버그 수정", _explore())
        assert len(plan.steps) >= 1

    def test_create_plan_explicit_type(self, planner):
        plan = planner.create_plan("xxx", _explore(), task_type="feature")
        assert len(plan.steps) >= 1

    def test_summarize(self, planner):
        assert isinstance(planner._summarize_solution({"a": 1}), str)

    def test_factory(self, tmp_path):
        assert create_llm_planner(tmp_path) is not None

    def test_openai_call_no_client(self, planner):
        assert planner._call_openai("p", 0) is None

    def test_anthropic_call_no_client(self, planner):
        assert planner._call_anthropic("p", 0) is None

    def test_openai_call_mock(self, planner):
        import json

        class Msg:
            content = json.dumps({"steps": [{"title": "m"}]})

        class Choice:
            message = Msg()

        class Resp:
            choices = [Choice()]

        class Client:
            class chat:  # noqa: N801 (외부 API 형상 모킹)
                class completions:  # noqa: N801
                    @staticmethod
                    def create(**k):
                        return Resp()

        planner.client = Client()
        planner.provider = "openai"
        out = planner._call_openai("p", 0)
        assert out and out["steps"][0]["title"] == "m"

    def test_openai_call_bad_json(self, planner):
        class Msg:
            content = "not json"

        class Choice:
            message = Msg()

        class Resp:
            choices = [Choice()]

        class Client:
            class chat:  # noqa: N801 (외부 API 형상 모킹)
                class completions:  # noqa: N801
                    @staticmethod
                    def create(**k):
                        return Resp()

        planner.client = Client()
        planner.provider = "openai"
        assert planner._call_openai("p", 0) is None

    def test_language_distribution(self, planner):
        s = planner._get_language_distribution(_explore())
        assert "python" in s


class TestCriticBasics:
    def test_no_keys_template(self, critic):
        assert critic.provider == "template"

    def test_quality_score(self, critic):
        q = critic._evaluate_critique_quality(
            {"issues": [{"severity": "high", "suggestion": "fix it well"}]}
        )
        assert q > 0
        assert critic._evaluate_critique_quality({}) == 0

    def test_build_result(self, critic):
        r = critic._build_critique_result(
            {"score": 0.8, "issues": [{"severity": "low", "message": "m"}]}, "s1"
        )
        assert r.step_id == "s1" and len(r.issues) == 1

    def test_detect_language(self, critic, tmp_path):
        assert critic._detect_language(tmp_path / "x.py") == "python"
        assert critic._detect_language(tmp_path / "x.js") == "javascript"
        assert critic._detect_language(tmp_path / "x.zzz") != ""

    def test_main_language(self, critic):
        assert critic._detect_main_language({"a.py": "x"}) == "python"
        assert critic._detect_main_language({}) != ""

    def test_collect_files(self, critic, tmp_path):
        (tmp_path / "m.py").write_text("x = 1\n")
        step = PlanStep(
            id="s", type=StepType.CODE, title="t", description="d", assigned_files=["m.py"]
        )
        critic.workspace = tmp_path
        out = critic._collect_code_files(step, {})
        assert out.get("m.py", "").strip() == "x = 1"

    def test_critique_template(self, critic, tmp_path):
        (tmp_path / "m.py").write_text("x = 1\n")
        critic.workspace = tmp_path
        step = PlanStep(
            id="s", type=StepType.CODE, title="t", description="d", assigned_files=["m.py"]
        )
        v = VerificationResult(step_id="s", passed=True)
        r = critic.critique(step, v, {"goal": "g"})
        assert r.step_id == "s"

    def test_critique_prompt(self, critic):
        p = critic._build_critique_prompt(
            PlanStep(id="s", type=StepType.CODE, title="t", description="d"),
            VerificationResult(step_id="s", passed=False, errors=["e"]),
            {},
            {},
            [],
        )
        assert isinstance(p, str) and len(p) > 0

    def test_openai_critique_no_client(self, critic):
        assert (
            critic._call_openai_critique(
                PlanStep(id="s", type=StepType.CODE, title="t", description="d"),
                VerificationResult(step_id="s", passed=True),
                {},
                {},
                [],
                0,
            )
            is None
        )

    def test_anthropic_critique_no_client(self, critic):
        assert (
            critic._call_anthropic_critique(
                PlanStep(id="s", type=StepType.CODE, title="t", description="d"),
                VerificationResult(step_id="s", passed=True),
                {},
                {},
                [],
                0,
            )
            is None
        )

    def test_factory(self, tmp_path):
        assert create_llm_critic(tmp_path) is not None
