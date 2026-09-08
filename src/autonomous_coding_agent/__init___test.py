"""
Tests for __init__
Auto-generated test for: GitHub Issue #1: Test: Add hello world endpoint

Add a simple GET /hello endpoint that returns {'message': 'Hello World'}
"""

from __init__ import main
import pytest


def test_main():
    """Test main function"""
    result = main()
    assert result is not None
    # TODO: 구체적 테스트 케이스 추가

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
