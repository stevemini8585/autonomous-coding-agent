"""Autonomous Coding Agent - Codex/Claude Code 수준의 자율 코딩 에이전트 파이프라인"""

from .agent import AutonomousCodingAgent
from .models import (
    PlanStep,
    StepStatus,
    VerificationResult,
    Plan,
    AgentState,
    StepType,
    CodeSymbol,
    FileInfo,
    ExploreResult,
)
from .pr_reviewer import ReviewCategory, ReviewSeverity, ReviewComment, PRReviewResult
from .explorer import CodeExplorer
from .planner import WorkPlanner
from .coder import CodeGenerator
from .verifier import Verifier
from .critic import Critic as CodeCritic
from .state import StateManager
from .patch_utils import PatchManager
from .git import GitManager
from .git_integration import GitWorkflow
from .github import GitHubClient
from .issue_parser import IssueParser
from .pr_reviewer import PRReviewer
from .web_search import WebSearcher, DocumentationParser, VersionChecker
from .code_adapter import (
    ProjectAnalyzer,
    CodeExampleAdapter,
    CodeExampleApplier,
)
from .test_generator import TestGenerator, EdgeCaseAnalyzer, ParameterCombinationGenerator, MockGenerator

__all__ = [
    "AutonomousCodingAgent",
    "PlanStep",
    "StepStatus",
    "VerificationResult",
    "Plan",
    "AgentState",
    "StepType",
    "CodeSymbol",
    "FileInfo",
    "ExploreResult",
    "ReviewCategory",
    "ReviewSeverity",
    "ReviewComment",
    "PRReviewResult",
    "CodeExplorer",
    "WorkPlanner",
    "CodeGenerator",
    "Verifier",
    "CodeCritic",
    "StateManager",
    "PatchManager",
    "GitManager",
    "GitWorkflow",
    "GitHubClient",
    "IssueParser",
    "PRReviewer",
    "WebSearcher",
    "DocumentationParser",
    "VersionChecker",
    "ProjectAnalyzer",
    "CodeExampleAdapter",
    "CodeExampleApplier",
    "TestGenerator",
    "EdgeCaseAnalyzer",
    "ParameterCombinationGenerator",
    "MockGenerator",
]

__version__ = "0.1.0"