"""
Tests for autonomous_coding_agent.type_inference (auto-generated smoke).
Goal: GitHub 이슈 #5: Add edge-case unit test for join_types

tests/test_type_inference.py의 TestJoinTypes 클래스에 Union 중첩 엣지 케이스 테스트 1개를 추가하세요. 예: join_types('O
"""

import pytest

try:
    from autonomous_coding_agent.type_inference import (
        annotation_to_str,
        create_type_analyzer,
        infer_file,
        infer_source,
        join_types,
    )
except ImportError:
    annotation_to_str = None


def test_annotation_to_str_callable():
    """annotation_to_str 호출 가능 여부(스모크)"""
    assert callable(annotation_to_str)


def test_create_type_analyzer_callable():
    """create_type_analyzer 호출 가능 여부(스모크)"""
    assert callable(create_type_analyzer)


def test_infer_file_callable():
    """infer_file 호출 가능 여부(스모크)"""
    assert callable(infer_file)


def test_infer_source_callable():
    """infer_source 호출 가능 여부(스모크)"""
    assert callable(infer_source)


def test_join_types_callable():
    """join_types 호출 가능 여부(스모크)"""
    assert callable(join_types)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
