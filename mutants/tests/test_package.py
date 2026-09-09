"""Tests for autonomous coding agent package"""

import pytest

from autonomous_coding_agent import (
    AutonomousCodingAgent,
    CodeCritic,
    CodeExampleAdapter,
    CodeExampleApplier,
    CodeExplorer,
    CodeGenerator,
    DocumentationParser,
    EdgeCaseAnalyzer,
    GitHubClient,
    GitManager,
    GitWorkflow,
    IssueParser,
    MockGenerator,
    ParameterCombinationGenerator,
    PatchManager,
    ProjectAnalyzer,
    PRReviewer,
    StateManager,
    TestGenerator,
    Verifier,
    VersionChecker,
    WebSearcher,
    WorkPlanner,
)


def test_imports():
    """Test all main classes can be imported"""
    assert AutonomousCodingAgent is not None
    assert CodeExplorer is not None
    assert WorkPlanner is not None
    assert CodeGenerator is not None
    assert Verifier is not None
    assert CodeCritic is not None
    assert StateManager is not None
    assert GitManager is not None
    assert GitHubClient is not None
    assert GitWorkflow is not None
    assert PatchManager is not None
    assert IssueParser is not None
    assert PRReviewer is not None
    assert WebSearcher is not None
    assert DocumentationParser is not None
    assert VersionChecker is not None
    assert ProjectAnalyzer is not None
    assert CodeExampleAdapter is not None
    assert CodeExampleApplier is not None
    assert TestGenerator is not None
    assert EdgeCaseAnalyzer is not None
    assert ParameterCombinationGenerator is not None
    assert MockGenerator is not None


def test_version():
    """Test version is accessible"""
    import autonomous_coding_agent

    assert autonomous_coding_agent.__version__ == "0.1.0"


def test_edge_case_analyzer():
    """Test edge case analyzer"""
    analyzer = EdgeCaseAnalyzer()

    # String edge cases
    str_cases = analyzer.get_edge_cases_for_type("str")
    assert "" in str_cases
    assert " " in str_cases
    assert "unicode: 日本語" in str_cases

    # Int edge cases
    int_cases = analyzer.get_edge_cases_for_type("int")
    assert 0 in int_cases
    assert -1 in int_cases
    assert 1 in int_cases
    assert 2**31 - 1 in int_cases
    assert -(2**31) in int_cases


def test_parameter_combination_generator():
    """Test parameter combination generator"""
    gen = ParameterCombinationGenerator(max_combinations=10)

    func_sig = {
        "params": [
            {"name": "x", "type": "int", "default": 0},
            {"name": "y", "type": "str", "default": "test"},
        ]
    }

    edge_cases = {
        "x": [0, 1, -1, 100],
        "y": ["", "a", "test"],
    }

    combos = gen.generate_combinations(func_sig, edge_cases)
    assert len(combos) > 0
    assert len(combos) <= 10
    for combo in combos:
        assert "x" in combo
        assert "y" in combo


def test_mock_generator():
    """Test mock generator"""
    gen = MockGenerator()

    # Test import analysis
    imports = gen.analyze_imports("import httpx\nfrom sqlalchemy import AsyncSession")
    assert "httpx" in imports
    assert "sqlalchemy.AsyncSession" in imports

    # Test mock generation
    mocks = gen.generate_mocks_for_imports(["httpx.AsyncClient", "redis.asyncio.Redis"])
    assert len(mocks) >= 1
    for mock in mocks:
        assert hasattr(mock, "target")
        assert hasattr(mock, "return_value")


def test_test_generator():
    """Test test generator basic functionality"""
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        sample_code = '''def add(a: int, b: int) -> int:
    """add 함수."""
    return a + b

async def fetch_data(url: str) -> dict:
    return {"data": url}
'''
        (tmp_path / "sample.py").write_text(sample_code)

        generator = TestGenerator(tmp_path)
        module = generator.generate_tests_for_file("sample.py")

        assert module.source_file == "sample.py"
        assert len(module.test_functions) > 0
        assert "add" in str(module.test_functions)
        assert "fetch_data" in str(module.test_functions)


def test_project_analyzer():
    """Test project analyzer"""
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        (tmp_path / "pyproject.toml").write_text("""
[project]
name = "test"
dependencies = ["httpx", "pydantic"]
""")

        analyzer = ProjectAnalyzer(tmp_path)
        context = analyzer.analyze()

        assert context.language == "python"
        assert context.package_manager in ["pip", "poetry"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
