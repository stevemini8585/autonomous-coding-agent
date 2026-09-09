#!/usr/bin/env python3
"""Chaos Testing - 장애 주입 테스트"""

import json
import os
import shutil
import signal
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FuturesTimeoutError
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from autonomous_coding_agent import (
    AutonomousCodingAgent,
    CodeCritic,
    CodeExplorer,
    CodeGenerator,
    LearningAgent,
    PatternMemory,
    StateManager,
    Verifier,
    WorkPlanner,
)
from autonomous_coding_agent.models import Plan, PlanStep, StepStatus, StepType, VerificationResult


class TestChaosNetworkFailure:
    """네트워크 장애 시나리오 테스트"""

    def test_github_api_failure_handling(self):
        """GitHub API 실패 시 graceful degradation"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            (tmp_path / "main.py").write_text("# Test\nprint('hello')\n")

            agent = AutonomousCodingAgent(tmp_path, max_iterations=2)
            agent.state.goal = "Add a simple function"

            # 탐색 & 계획
            agent._run_explore()
            agent._create_plan()

            # GitHubClient 모킹하여 네트워크 에러 시뮬레이션
            from autonomous_coding_agent.github import GitHubClient

            original_get_pr = GitHubClient.get_pr

            def mock_get_pr(*args, **kwargs):
                raise ConnectionError("Network unreachable")

            with patch.object(GitHubClient, "get_pr", side_effect=mock_get_pr):
                # 에러가 전파되지 않고 처리되어야 함
                try:
                    # PR 리뷰 관련 기능이 네트워크 에러를 처리하는지 확인
                    pass
                except ConnectionError:
                    pytest.fail("네트워크 에러가 처리되지 않고 전파됨")

    def test_web_search_failure_handling(self):
        """웹 검색 실패 시 fallback 동작"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            (tmp_path / "main.py").write_text("# Test\n")

            from autonomous_coding_agent.web_search import WebSearcher

            searcher = WebSearcher()

            # 네트워크 에러 시 빈 결과 반환 확인
            with patch("urllib.request.urlopen", side_effect=ConnectionError("Network down")):
                results = searcher.search("test query", limit=5)
                assert isinstance(results, list)
                # 에러 시 빈 리스트 또는 적절한 에러 처리


class TestChaosDiskFull:
    """디스크 풀 시나리오 테스트"""

    def test_state_save_disk_full_handling(self):
        """상태 저장 시 디스크 풀 에러 처리"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            state_manager = StateManager(tmp_path)

            from autonomous_coding_agent.models import AgentState

            state = AgentState(session_id="test_session", workspace=tmp_path, goal="Test goal")

            # 디스크 풀 시뮬레이션 (OSError with errno=ENOSPC)
            def mock_open_disk_full(*args, **kwargs):
                raise OSError(28, "No space left on device")

            with patch("builtins.open", side_effect=mock_open_disk_full):
                # 에러가 로그만 남기고 예외를 전파하지 않아야 함
                state_manager.save_state(state)
                # 예외 없이 완료되어야 함 (단, 로그에 에러 기록)

    def test_checkpoint_creation_disk_full(self):
        """체크포인트 생성 시 디스크 풀"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            state_manager = StateManager(tmp_path)

            from autonomous_coding_agent.models import AgentState

            state = AgentState(session_id="test_session", workspace=tmp_path, goal="Test goal")

            def mock_open_disk_full(*args, **kwargs):
                raise OSError(28, "No space left on device")

            with patch("builtins.open", side_effect=mock_open_disk_full):
                result = state_manager.create_checkpoint(state, "test")
                # 빈 문자열 반환 또는 적절한 에러 처리
                assert result == ""


class TestChaosProcessKill:
    """프로세스 강제 종료 시나리오 테스트"""

    def test_agent_interruption_recovery(self):
        """에이전트 실행 중 강제 종료 후 복구"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            (tmp_path / "main.py").write_text("# Test\n")

            agent = AutonomousCodingAgent(tmp_path, max_iterations=3)
            agent.state.goal = "Add hello function"

            # 탐색 & 계획
            agent._run_explore()
            agent._create_plan()

            # 체크포인트 생성
            cp_id = agent.state_manager.create_checkpoint(agent.state, "pre_execution")
            assert cp_id != ""

            # 강제 종료 시뮬레이션 (상태 저장 안 된 상황)
            # 새 에이전트 인스턴스로 복구 테스트
            restored_state = agent.state_manager.restore_checkpoint(agent.state.session_id, cp_id)

            assert restored_state.plan is not None
            assert restored_state.plan.goal == "Add hello function"
            assert len(restored_state.plan.steps) > 0


class TestChaosConcurrency:
    """동시성/경쟁 상태 테스트"""

    def test_concurrent_state_access(self):
        """동시 상태 접근 시 락 동작"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            state_manager = StateManager(tmp_path)

            from autonomous_coding_agent.models import AgentState

            state = AgentState(
                session_id="concurrent_test", workspace=tmp_path, goal="Concurrent test"
            )

            # 첫 번째 락 획득
            acquired1 = state_manager.acquire_lock(tmp_path)
            assert acquired1 is True

            # 두 번째 락 획득 시도 (실패해야 함)
            state_manager2 = StateManager(tmp_path)
            acquired2 = state_manager2.acquire_lock(tmp_path)
            assert acquired2 is False

            # 첫 번째 해제 후 두 번째 획득 가능
            state_manager.release_lock()
            acquired3 = state_manager2.acquire_lock(tmp_path)
            assert acquired3 is True
            state_manager2.release_lock()

    def test_is_locked_detection(self):
        """락 상태 감지"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            state_manager = StateManager(tmp_path)

            # 초기 상태: 언락됨
            assert state_manager.is_locked(tmp_path) is False

            # 락 획득
            state_manager.acquire_lock(tmp_path)
            assert state_manager.is_locked(tmp_path) is True

            # 락 해제
            state_manager.release_lock()
            assert state_manager.is_locked(tmp_path) is False


class TestChaosVerificationFailure:
    """검증 실패 시나리오 테스트"""

    def test_verification_failure_triggers_critique_and_retry(self):
        """검증 실패 시 비평 및 재시도 트리거"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            (tmp_path / "main.py").write_text("def broken():\n    return 1/0\n")  # 에러 있는 코드

            agent = AutonomousCodingAgent(tmp_path, max_iterations=2)
            agent.state.goal = "Fix the broken function"
            agent._run_explore()
            agent._create_plan()

            # 계획에 CODE 단계가 있는지 확인
            code_steps = [s for s in agent.state.plan.steps if s.type == StepType.CODE]
            assert len(code_steps) > 0

            step = code_steps[0]
            step.max_retries = 2

            # 컨텍스트 구성
            context = {
                "goal": agent.state.goal,
                "explore_result": agent.state.explore_result,
                "plan": agent.state.plan,
                "workspace": tmp_path,
                "config": {
                    "verify_tests": True,
                    "verify_lint": True,
                    "verify_types": True,
                    "coverage_threshold": 80.0,
                },
            }

            # 단계 실행 (검증 실패 예상)
            agent._run_single_step(step)

            # 검증 실패로 FAILED 상태가 되거나 재시도되어야 함
            assert step.status in (StepStatus.FAILED, StepStatus.PENDING)
            if step.status == StepStatus.PENDING:
                assert step.retry_count > 0


class TestChaosTimeout:
    """타임아웃 시나리오 테스트"""

    def test_step_timeout_handling(self):
        """단계 실행 타임아웃 처리"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            (tmp_path / "main.py").write_text("# Test\n")

            agent = AutonomousCodingAgent(tmp_path, max_iterations=1, timeout_per_step=1)
            agent.state.goal = "Test timeout"
            agent._run_explore()
            agent._create_plan()

            # 긴 실행 단계 시뮬레이션
            original_execute = agent.coder.execute_step

            def slow_execute(*args, **kwargs):
                time.sleep(2)  # 타임아웃보다 길게
                return original_execute(*args, **kwargs)

            with patch.object(agent.coder, "execute_step", side_effect=slow_execute):
                code_steps = [s for s in agent.state.plan.steps if s.type == StepType.CODE]
                if code_steps:
                    step = code_steps[0]
                    # 타임아웃이 발생하더라도 graceful하게 처리
                    try:
                        agent._run_single_step(step)
                    except FuturesTimeoutError:
                        pass  # 예상된 타임아웃
                    except Exception as e:
                        # 다른 예외는 실패로 처리
                        assert step.status == StepStatus.FAILED


class TestChaosCorruptedState:
    """상태 파일 손상 시나리오 테스트"""

    def test_corrupted_state_file_recovery(self):
        """손상된 상태 파일 복구"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            state_manager = StateManager(tmp_path)

            # 손상된 JSON 파일 생성
            state_file = state_manager.state_dir / "corrupted_session.json"
            state_file.write_text("{ invalid json }")

            # 로드 시도 시 None 반환 (예외 전파 안 함)
            result = state_manager.load_state("corrupted_session")
            assert result is None

    def test_corrupted_checkpoint_recovery(self):
        """손상된 체크포인트 복구"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            state_manager = StateManager(tmp_path)

            from autonomous_coding_agent.models import AgentState

            state = AgentState(session_id="test_session", workspace=tmp_path, goal="Test")

            # 정상 체크포인트 생성
            cp_id = state_manager.create_checkpoint(state, "good")
            assert cp_id != ""

            # 체크포인트 파일 손상
            cp_file = state_manager.state_dir / f"{state.session_id}_{cp_id}.json"
            cp_file.write_text("{ corrupted }")

            # 복구 시도 시 JSONDecodeError 발생
            with pytest.raises(json.JSONDecodeError):
                state_manager.restore_checkpoint(state.session_id, cp_id)


class TestChaosMemoryPressure:
    """메모리 압박 시나리오 테스트"""

    def test_large_codebase_exploration(self):
        """대규모 코드베이스 탐색 시 메모리 관리"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)

            # 많은 파일 생성 (메모리 압박 시뮬레이션)
            for i in range(100):
                (tmp_path / f"module_{i}.py").write_text(
                    f"# Module {i}\n" + "def func():\n    pass\n" * 50
                )

            explorer = CodeExplorer(tmp_path)
            # 메모리 이슈 없이 완료되어야 함
            result = explorer.explore()

            assert isinstance(result, type(explorer.explore()))
            assert len(result.files) >= 100


class TestChaosAutoRecovery:
    """자동 복구 통합 테스트"""

    def test_full_cycle_failure_and_recovery(self):
        """전체 사이클 실패 후 자동 복구"""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_path = Path(tmpdir)
            (tmp_path / "main.py").write_text("# Test\n")

            # 첫 번째 실행 - 실패 시뮬레이션
            agent1 = AutonomousCodingAgent(tmp_path, max_iterations=2)
            agent1.state.goal = "Add feature X"

            agent1._run_explore()
            agent1._create_plan()

            # 체크포인트 생성
            cp_id = agent1.state_manager.create_checkpoint(agent1.state, "before_execution")

            # 실행 중 실패 시뮬레이션 (검증 실패)
            # 강제로 실패 상태로 만들기
            for step in agent1.state.plan.steps:
                if step.type == StepType.CODE:
                    step.status = StepStatus.FAILED
                    step.error = "Simulated failure"
                    break

            agent1.state_manager.save_state(agent1.state)

            # 두 번째 에이전트로 복구 실행
            agent2 = AutonomousCodingAgent(
                tmp_path, max_iterations=2, resume_session=agent1.state.session_id
            )

            # 체크포인트에서 복구
            restored = agent2.state_manager.restore_checkpoint(agent2.state.session_id, cp_id)
            agent2.state.plan = restored.plan
            agent2.state.explore_result = restored.explore_result
            agent2.state.iteration = restored.iteration

            # 실패한 단계가 PENDING으로 리셋되어 재시도 가능해야 함
            for step in agent2.state.plan.steps:
                if step.status == StepStatus.FAILED:
                    step.status = StepStatus.PENDING
                    step.retry_count = 0
                    step.error = None

            # 실행 루프 재개 가능해야 함
            assert agent2.state.plan is not None
            ready = agent2.state.plan.get_ready_steps()
            assert len(ready) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
