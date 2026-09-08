"""Tests for memory/learning module"""

import tempfile
from pathlib import Path

import pytest

from autonomous_coding_agent import (
    LearningAgent,
    PatternMemory,
)


def test_pattern_memory_basic():
    """Test basic pattern memory operations"""
    with tempfile.TemporaryDirectory() as tmpdir:
        memory = PatternMemory(Path(tmpdir) / "memory")

        # Store a pattern
        pattern_id = memory.store_pattern(
            pattern_type="test",
            context={"language": "python", "framework": "fastapi"},
            solution={"method": "ast_based", "edge_cases": True},
            success_metrics={"success_rate": 0.95, "tests_generated": 10},
            tags=["test_generation", "fastapi"],
        )

        assert pattern_id.startswith("test_")
        assert pattern_id in memory.patterns

        # Find patterns
        patterns = memory.find_patterns(
            pattern_type="test",
            context={"language": "python"},
            limit=5,
        )
        assert len(patterns) == 1
        assert patterns[0].pattern_id == pattern_id
        assert patterns[0].context["language"] == "python"

        # Use pattern
        used = memory.use_pattern(pattern_id)
        assert used is not None
        assert used.use_count == 1
        assert used.last_used is not None


def test_pattern_memory_similarity():
    """Test pattern similarity matching"""
    with tempfile.TemporaryDirectory() as tmpdir:
        memory = PatternMemory(Path(tmpdir) / "memory")

        # Store multiple patterns
        memory.store_pattern(
            pattern_type="test",
            context={"language": "python", "framework": "fastapi"},
            solution={"method": "ast_based"},
            success_metrics={"success_rate": 0.9},
        )

        memory.store_pattern(
            pattern_type="test",
            context={"language": "python", "framework": "django"},
            solution={"method": "ast_based"},
            success_metrics={"success_rate": 0.85},
        )

        memory.store_pattern(
            pattern_type="fix",
            context={"language": "python", "framework": "fastapi"},
            solution={"method": "patch_based"},
            success_metrics={"success_rate": 0.95},
        )

        # Search for fastapi patterns
        patterns = memory.find_patterns(
            context={"language": "python", "framework": "fastapi"},
            limit=10,
        )

        # Should find both fastapi patterns (test and fix)
        assert len(patterns) >= 2
        # Fastapi patterns should have higher similarity
        for p in patterns:
            assert p.context.get("framework") == "fastapi" or p.context.get("framework") == "django"


def test_session_record():
    """Test session recording"""
    with tempfile.TemporaryDirectory() as tmpdir:
        memory = PatternMemory(Path(tmpdir) / "memory")
        agent = LearningAgent(memory)

        # Start session
        session = agent.start_session(
            goal="Add user authentication",
            workspace="/tmp/test",
        )

        assert session.session_id.startswith("session_")
        assert session.goal == "Add user authentication"
        assert session.workspace == "/tmp/test"
        assert session.start_time is not None

        # End session with success
        agent.end_session(
            success=True,
            metrics={
                "tests_generated": 15,
                "coverage": 85.5,
                "language": "python",
                "framework": "fastapi",
                "test_framework": "pytest",
            }
        )

        # Check session recorded
        assert len(memory.sessions) == 1
        recorded = memory.sessions[0]
        assert recorded.success is True
        assert recorded.metrics["tests_generated"] == 15

        # Should have created patterns
        assert len(memory.patterns) > 0


def test_learning_agent_pattern_application():
    """Test learning agent pattern application"""
    with tempfile.TemporaryDirectory() as tmpdir:
        memory = PatternMemory(Path(tmpdir) / "memory")
        agent = LearningAgent(memory)

        # Store a pattern
        memory.store_pattern(
            pattern_type="test",
            context={"language": "python", "framework": "fastapi"},
            solution={"method": "ast_based", "edge_cases": True, "mocking": True},
            success_metrics={"success_rate": 0.95},
            tags=["test_generation"],
        )

        # Get relevant patterns
        patterns = agent.get_relevant_patterns(
            {"language": "python", "framework": "fastapi"}
        )
        assert len(patterns) > 0

        # Apply pattern
        pattern_id = patterns[0].pattern_id
        result = agent.apply_pattern(pattern_id, {"language": "python", "framework": "django"})

        assert result is not None
        assert result["pattern_id"] == pattern_id
        assert "adapted_solution" in result
        assert result["adapted_solution"]["framework_adapted"] is True
        assert result["adapted_solution"]["target_framework"] == "django"
        assert result["confidence"] == 0.95


def test_statistics():
    """Test statistics"""
    with tempfile.TemporaryDirectory() as tmpdir:
        memory = PatternMemory(Path(tmpdir) / "memory")

        memory.store_pattern(
            pattern_type="test",
            context={"language": "python"},
            solution={},
            success_metrics={"success_rate": 0.9},
        )
        memory.store_pattern(
            pattern_type="fix",
            context={"language": "python"},
            solution={},
            success_metrics={"success_rate": 0.85},
        )

        stats = memory.get_statistics()
        assert stats["total_patterns"] == 2
        assert stats["pattern_types"]["test"] == 1
        assert stats["pattern_types"]["fix"] == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
