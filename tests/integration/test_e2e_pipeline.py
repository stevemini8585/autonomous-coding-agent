#!/usr/bin/env python3
"""통합 테스트: GitHub Issue → Agent 실행 → PR 생성 전체 파이프라인"""

import asyncio
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from autonomous_coding_agent import (
    AutonomousCodingAgent,
    CodeCritic,
    CodeExplorer,
    CodeGenerator,
    GitHubClient,
    GitManager,
    GitWorkflow,
    IssueParser,
    LearningAgent,
    PatchManager,
    PatternMemory,
    PRReviewer,
    StateManager,
    Verifier,
    WorkPlanner,
)


class TestE2EPipeline:
    """E2E 파이프라인 통합 테스트"""

    @classmethod
    def setup_class(cls):
        """테스트용 임시 워크스페이스 생성"""
        cls.temp_dir = Path(tempfile.mkdtemp(prefix="e2e_test_"))
        cls.workspace = cls.temp_dir / "test_project"
        cls.workspace.mkdir(parents=True)

        # 기본 FastAPI 프로젝트 생성
        (cls.workspace / "main.py").write_text("""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Test API")

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
def read_root():
    return {"message": "Welcome to Test API"}

@app.post("/items/")
def create_item(item: Item):
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
""")

        (cls.workspace / "requirements.txt").write_text("fastapi\nuvicorn\npydantic\n")

        # Git 초기화
        subprocess.run(["git", "init"], cwd=cls.workspace, capture_output=True)
        subprocess.run(
            ["git", "config", "user.email", "test@test.com"], cwd=cls.workspace, capture_output=True
        )
        subprocess.run(
            ["git", "config", "user.name", "Test"], cwd=cls.workspace, capture_output=True
        )
        subprocess.run(["git", "add", "."], cwd=cls.workspace, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", "Initial commit"], cwd=cls.workspace, capture_output=True
        )

    @classmethod
    def teardown_class(cls):
        """임시 디렉토리 정리"""
        shutil.rmtree(cls.temp_dir, ignore_errors=True)

    def test_01_explorer(self):
        """1. 코드베이스 탐색 테스트"""
        explorer = CodeExplorer(self.workspace)
        result = explorer.explore()

        assert len(result.files) >= 1
        assert len(result.symbols) >= 1
        assert any(f.path == "main.py" for f in result.files)
        assert any(s.name == "read_root" for s in result.symbols)
        assert any(s.name == "Item" for s in result.symbols)

        print(f"✅ Explorer: {len(result.files)} files, {len(result.symbols)} symbols")

    def test_02_planner(self):
        """2. 계획 수립 테스트"""
        explorer = CodeExplorer(self.workspace)
        explore_result = explorer.explore()

        planner = WorkPlanner(self.workspace)
        goal = "Add a GET /hello endpoint that returns {'message': 'Hello World'}"
        plan = planner.create_plan(goal=goal, explore_result=explore_result, task_type="feature")

        assert len(plan.steps) >= 3  # explore, plan, code 최소
        step_ids = [s.id for s in plan.steps]
        assert "step_1_explore" in step_ids
        assert "step_2_plan" in step_ids
        assert any("code" in s.id for s in plan.steps)

        print(f"✅ Planner: {len(plan.steps)} steps created")

    def test_03_coder(self):
        """3. 코드 생성 테스트"""
        explorer = CodeExplorer(self.workspace)
        explore_result = explorer.explore()

        planner = WorkPlanner(self.workspace)
        goal = "Add a GET /hello endpoint that returns {'message': 'Hello World'}"
        plan = planner.create_plan(goal=goal, explore_result=explore_result, task_type="feature")

        coder = CodeGenerator(self.workspace)
        step_3 = plan.get_step("step_3_code")
        assert step_3 is not None, "step_3_code not found in plan"

        context = {
            "goal": goal,
            "explore_result": explore_result,
            "plan": plan,
            "workspace": self.workspace,
            "config": {
                "verify_tests": True,
                "verify_lint": True,
                "verify_types": True,
                "coverage_threshold": 80.0,
            },
        }

        result = coder.execute_step(step_3, context)

        assert "files_modified" in result
        assert "main.py" in result["files_modified"]

        # 생성된 코드 확인
        content = (self.workspace / "main.py").read_text()
        assert "/hello" in content
        assert "Hello World" in content

        print(f"✅ Coder: {result}")

    def test_04_verifier(self):
        """4. 검증 테스트"""
        explorer = CodeExplorer(self.workspace)
        explore_result = explorer.explore()

        planner = WorkPlanner(self.workspace)
        goal = "Add a GET /hello endpoint that returns {'message': 'Hello World'}"
        plan = planner.create_plan(goal=goal, explore_result=explore_result, task_type="feature")

        # 코드 생성
        coder = CodeGenerator(self.workspace)
        step_3 = plan.get_step("step_3_code")
        context = {
            "goal": goal,
            "explore_result": explore_result,
            "plan": plan,
            "workspace": self.workspace,
            "config": {
                "verify_tests": True,
                "verify_lint": True,
                "verify_types": True,
                "coverage_threshold": 80.0,
            },
        }
        coder.execute_step(step_3, context)

        # 검증
        verifier = Verifier(self.workspace)
        verification = verifier.verify_step(step_3, ["main.py"])

        assert verification.passed
        assert verification.lint_results.get("passed")
        assert verification.format_results.get("passed")
        assert verification.type_results.get("passed")

        print(f"✅ Verifier: passed={verification.passed}")

    def test_05_critic(self):
        """5. 비평 테스트"""
        from autonomous_coding_agent.models import StepStatus, VerificationResult

        explorer = CodeExplorer(self.workspace)
        explore_result = explorer.explore()

        planner = WorkPlanner(self.workspace)
        goal = "Add a GET /hello endpoint that returns {'message': 'Hello World'}"
        plan = planner.create_plan(goal=goal, explore_result=explore_result, task_type="feature")

        coder = CodeGenerator(self.workspace)
        step_3 = plan.get_step("step_3_code")
        context = {
            "goal": goal,
            "explore_result": explore_result,
            "plan": plan,
            "workspace": self.workspace,
            "config": {
                "verify_tests": True,
                "verify_lint": True,
                "verify_types": True,
                "coverage_threshold": 80.0,
            },
        }
        coder.execute_step(step_3, context)

        verifier = Verifier(self.workspace)
        verification = verifier.verify_step(step_3, ["main.py"])

        critic = CodeCritic(self.workspace)
        critique = critic.critique(step_3, verification, context)

        assert critique.score >= 0.0
        assert critique.score <= 1.0
        assert isinstance(critique.issues, list)
        assert isinstance(critique.improvements, list)

        print(f"✅ Critic: score={critique.score:.2f}, issues={len(critique.issues)}")

    def test_06_state_manager(self):
        """6. 상태 관리 테스트"""
        state_manager = StateManager(self.workspace)

        import uuid
        from datetime import datetime

        from autonomous_coding_agent.models import AgentState

        state = AgentState(
            session_id=f"test_{uuid.uuid4().hex[:8]}",
            workspace=self.workspace,
            goal="Test goal",
            max_iterations=5,
        )

        # 저장
        state_manager.save_state(state)

        # 로드
        loaded = state_manager.load_state(state.session_id)
        assert loaded is not None
        assert loaded.session_id == state.session_id
        assert loaded.goal == state.goal

        # 체크포인트
        state_manager.create_checkpoint(state, "test_checkpoint")

        print("✅ StateManager: save/load/checkpoint OK")

    def test_07_git_integration(self):
        """7. Git 연동 테스트"""
        git_manager = GitManager(self.workspace)

        # 브랜치 생성
        branch = git_manager.create_branch("test/feature-hello")
        assert branch == "test/feature-hello"

        # 커밋
        commit = git_manager.commit("feat: add hello endpoint")
        assert commit is not None

        # 로그
        log = git_manager.get_log(5)
        assert len(log) >= 2  # Initial + feat commit

        print("✅ GitManager: branch/commit/log OK")

    def test_08_git_workflow(self):
        """8. Git 워크플로우 테스트"""
        git_workflow = GitWorkflow(self.workspace)

        # 기능 브랜치 생성 (이슈 번호와 제목으로)
        branch = git_workflow.create_feature_branch(1, "Add hello endpoint")
        assert branch.startswith("issue-1-")
        assert "hello" in branch or "endpoint" in branch

        print("✅ GitWorkflow: feature branch OK")

    def test_09_pattern_memory(self):
        """9. 패턴 메모리 테스트"""
        with tempfile.TemporaryDirectory() as tmpdir:
            memory = PatternMemory(Path(tmpdir) / "memory")

            # 패턴 저장
            pattern_id = memory.store_pattern(
                pattern_type="test",
                context={"language": "python", "framework": "fastapi"},
                solution={"method": "ast_based", "edge_cases": True},
                success_metrics={"success_rate": 0.95, "tests_generated": 10},
                tags=["test_generation", "fastapi"],
            )

            assert pattern_id.startswith("test_")
            assert pattern_id in memory.patterns

            # 패턴 검색
            patterns = memory.find_patterns(
                pattern_type="test",
                context={"language": "python"},
                limit=5,
            )

            assert len(patterns) >= 1
            assert patterns[0].pattern_id == pattern_id

            # 패턴 사용
            used = memory.use_pattern(pattern_id)
            assert used is not None
            assert used.use_count == 1

            print("✅ PatternMemory: store/find/use OK")

    def test_10_learning_agent(self):
        """10. 학습 에이전트 테스트"""
        memory = PatternMemory()
        agent = LearningAgent(memory)

        # 세션 시작
        session = agent.start_session(goal="Add hello endpoint", workspace=str(self.workspace))

        assert session.session_id.startswith("session_")
        assert session.goal == "Add hello endpoint"

        # 세션 종료 (성공)
        agent.end_session(
            success=True,
            metrics={
                "language": "python",
                "framework": "fastapi",
                "tests_generated": 5,
                "files_modified": 1,
                "files_created": 0,
            },
        )

        # 패턴이 추출되었는지 확인
        patterns = memory.find_patterns(pattern_type="fix", limit=5)
        assert len(patterns) >= 1

        print("✅ LearningAgent: session/pattern extraction OK")


if __name__ == "__main__":
    # 수동 실행 시
    test = TestE2EPipeline()
    test.setup_class()

    try:
        test.test_01_explorer()
        test.test_02_planner()
        test.test_03_coder()
        test.test_04_verifier()
        test.test_05_critic()
        test.test_06_state_manager()
        test.test_07_git_integration()
        test.test_08_git_workflow()
        test.test_09_pattern_memory()
        test.test_10_learning_agent()
        print("\n✅ 모든 통합 테스트 통과!")
    finally:
        test.teardown_class()
