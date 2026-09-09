#!/usr/bin/env python3
"""벡터 메모리 테스트"""

import tempfile
from pathlib import Path

import pytest

from autonomous_coding_agent import (
    VectorLearningAgent,
    VectorPattern,
    VectorPatternMemory,
)


class TestVectorPatternMemory:
    """VectorPatternMemory 테스트"""

    @pytest.fixture
    def memory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            yield VectorPatternMemory(Path(tmpdir))

    def test_store_and_find_pattern(self, memory):
        """패턴 저장 및 벡터 검색"""
        pid = memory.store_pattern(
            pattern_type="test",
            context={"language": "python", "framework": "fastapi"},
            solution={"method": "ast_based", "edge_cases": True},
            success_metrics={"success_rate": 0.95, "tests_generated": 10},
            tags=["test_generation", "fastapi"],
        )

        assert pid.startswith("test_")
        assert pid in memory.vector_patterns

        # 벡터 검색
        results = memory.find_patterns_vector(
            query_context={"language": "python", "framework": "fastapi"},
            pattern_type="test",
            limit=3,
        )

        assert len(results) >= 1
        assert results[0].pattern_id == pid
        assert hasattr(results[0], "_similarity")

    def test_vector_search_cross_framework(self, memory):
        """다른 프레임워크 간 유사도 검색"""
        # FastAPI 패턴
        memory.store_pattern(
            pattern_type="test",
            context={"language": "python", "framework": "fastapi"},
            solution={"method": "ast_based"},
            success_metrics={"success_rate": 0.9},
            tags=["fastapi"],
        )

        # Flask 패턴
        memory.store_pattern(
            pattern_type="test",
            context={"language": "python", "framework": "flask"},
            solution={"method": "ast_based"},
            success_metrics={"success_rate": 0.85},
            tags=["flask"],
        )

        # Django 패턴
        memory.store_pattern(
            pattern_type="test",
            context={"language": "python", "framework": "django"},
            solution={"method": "ast_based"},
            success_metrics={"success_rate": 0.88},
            tags=["django"],
        )

        # FastAPI 쿼리로 검색 - FastAPI 패턴이 가장 유사해야 함
        results = memory.find_patterns_vector(
            query_context={"language": "python", "framework": "fastapi"},
            pattern_type="test",
            limit=3,
        )

        assert len(results) >= 1
        # FastAPI 패턴이 상위에 있어야 함
        assert results[0].context.get("framework") == "fastapi"

    def test_weight_learning_success(self, memory):
        """성공 시 가중치 증가"""
        pid = memory.store_pattern(
            pattern_type="test",
            context={"language": "python"},
            solution={"method": "ast"},
            success_metrics={"success_rate": 0.9},
        )

        initial_weight = memory.vector_patterns[pid].weight

        # 성공 2회
        memory.update_pattern_weight(pid, True, {"success_rate": 1.0})
        memory.update_pattern_weight(pid, True, {"success_rate": 1.0})

        assert memory.vector_patterns[pid].weight > initial_weight
        assert memory.vector_patterns[pid].weight <= 2.0

    def test_weight_learning_failure(self, memory):
        """실패 시 가중치 감소"""
        pid = memory.store_pattern(
            pattern_type="test",
            context={"language": "python"},
            solution={"method": "regex"},
            success_metrics={"success_rate": 0.7},
        )

        initial_weight = memory.vector_patterns[pid].weight

        # 실패 2회
        memory.update_pattern_weight(pid, False)
        memory.update_pattern_weight(pid, False)

        assert memory.vector_patterns[pid].weight < initial_weight
        assert memory.vector_patterns[pid].weight >= 0.1
        assert memory.vector_patterns[pid].failure_count == 2

    def test_recommendations_ranking(self, memory):
        """추천 순위가 가중치와 유사도를 반영하는지"""
        # 높은 가중치 패턴
        pid1 = memory.store_pattern(
            pattern_type="test",
            context={"language": "python", "task": "api"},
            solution={"method": "ast"},
            success_metrics={"success_rate": 0.95},
        )
        memory.update_pattern_weight(pid1, True)
        memory.update_pattern_weight(pid1, True)

        # 낮은 가중치 패턴
        pid2 = memory.store_pattern(
            pattern_type="test",
            context={"language": "python", "task": "cli"},
            solution={"method": "regex"},
            success_metrics={"success_rate": 0.6},
        )
        memory.update_pattern_weight(pid2, False)
        memory.update_pattern_weight(pid2, False)

        # 중간 패턴
        pid3 = memory.store_pattern(
            pattern_type="fix",
            context={"language": "python", "task": "bug"},
            solution={"method": "patch"},
            success_metrics={"success_rate": 0.8},
        )

        # API 작업 컨텍스트로 추천 요청
        recs = memory.get_pattern_recommendations({"language": "python", "task": "api"})

        assert len(recs) >= 1
        # api 작업과 유사한 pid1이 상위에 있어야 함
        assert recs[0]["pattern_id"] == pid1
        assert recs[0]["confidence"] > recs[-1]["confidence"] if len(recs) > 1 else True

    def test_vector_pattern_persistence(self, memory):
        """벡터 패턴 영구 저장/복원"""
        pid = memory.store_pattern(
            pattern_type="test",
            context={"language": "python"},
            solution={"method": "ast"},
            success_metrics={"success_rate": 0.9},
            tags=["persistence"],
        )

        # 새 메모리 인스턴스로 복원 (같은 디렉토리 사용)
        memory2 = VectorPatternMemory(memory.memory_dir)

        assert pid in memory2.vector_patterns
        assert memory2.vector_patterns[pid].weight == 1.0

    def test_learning_agent_integration(self, memory):
        """VectorLearningAgent 연동"""
        agent = VectorLearningAgent(memory)

        # 세션 시작
        session = agent.start_session("Add API endpoint", "/workspace")
        assert session.session_id.startswith("session_")

        # 세션 종료 (성공) - 패턴 생성 조건 만족
        agent.end_session(
            True,
            {
                "tests_generated": 5,
                "language": "python",
                "framework": "fastapi",
                "pr_reviewed": True,
                "files_modified": 2,
                "issues_found": 3,
            },
        )

        # 생성된 패턴 확인
        assert len(session.patterns_created) >= 1

        # 가중치 업데이트 확인
        for pid in session.patterns_created:
            pattern = memory.vector_patterns[pid]
            assert pattern.weight >= 1.0  # 성공으로 가중치 유지/증가

    def test_find_patterns_fallback(self, memory):
        """인코더 없을 때 폴백 동작"""
        # encoder 없이도 기본 검색 동작 확인
        pid = memory.store_pattern(
            pattern_type="test",
            context={"language": "python", "framework": "fastapi"},
            solution={"method": "ast"},
            success_metrics={"success_rate": 0.9},
        )

        # encoder 비활성화 시뮬레이션
        memory.encoder = None

        results = memory.find_patterns_vector(
            query_context={"language": "python"},
            limit=5,
        )

        # 폴백: 기존 키워드 기반 검색 동작
        assert len(results) >= 1


class TestVectorPattern:
    """VectorPattern 데이터클래스 테스트"""

    def test_vector_pattern_creation(self):
        pattern = VectorPattern(
            pattern_id="test_123",
            pattern_type="test",
            context={"language": "python"},
            solution={"method": "ast"},
            success_metrics={"success_rate": 0.9},
            weight=1.5,
            failure_count=2,
        )

        assert pattern.pattern_id == "test_123"
        assert pattern.weight == 1.5
        assert pattern.failure_count == 2

    def test_vector_pattern_defaults(self):
        pattern = VectorPattern(
            pattern_id="test_456",
            pattern_type="fix",
            context={},
            solution={},
            success_metrics={},
        )

        assert pattern.weight == 1.0
        assert pattern.failure_count == 0
        assert pattern.context_embedding is None
        assert pattern.solution_embedding is None
        assert pattern.combined_embedding is None


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
