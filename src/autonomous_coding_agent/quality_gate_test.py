"""
Tests for autonomous_coding_agent.quality_gate (auto-generated smoke).
Goal: GitHub 이슈 #5: Add edge-case unit test for join_types

tests/test_type_inference.py의 TestJoinTypes 클래스에 Union 중첩 엣지 케이스 테스트 1개를 추가하세요. 예: join_types('O
"""

import pytest

try:
    from autonomous_coding_agent.quality_gate import (
        check_file,
        check_paths,
        check_source,
        create_quality_gate,
        gate_summary,
    )
except ImportError:
    check_file = None


def test_check_file_callable():
    """check_file 호출 가능 여부(스모크)"""
    assert callable(check_file)


def test_check_paths_callable():
    """check_paths 호출 가능 여부(스모크)"""
    assert callable(check_paths)


def test_check_source_callable():
    """check_source 호출 가능 여부(스모크)"""
    assert callable(check_source)


def test_create_quality_gate_callable():
    """create_quality_gate 호출 가능 여부(스모크)"""
    assert callable(create_quality_gate)


def test_gate_summary_callable():
    """gate_summary 호출 가능 여부(스모크)"""
    assert callable(gate_summary)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
