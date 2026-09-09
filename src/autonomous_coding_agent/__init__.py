"""
Autonomous Coding Agent - Codex/Claude Code 수준의 자율 코딩 에이전트 파이프라인
"""

from .agent import AutonomousCodingAgent
from .code_adapter import (
    CodeExampleAdapter,
    CodeExampleApplier,
    ProjectAnalyzer,
)
from .coder import CodeGenerator
from .critic import Critic as CodeCritic
from .dashboard import (
    DashboardServer,
    SessionProgress,
    StepProgress,
    get_dashboard,
    start_dashboard,
)
from .dataflow import (
    AnalysisResult,
    Definition,
    DefUseChain,
    DependencyEdge,
    Use,
    create_dataflow_analyzer,
)
from .dataflow import (
    analyze_file as analyze_dataflow_file,
)
from .dataflow import (
    analyze_source as analyze_dataflow_source,
)
from .explorer import CodeExplorer
from .git import GitManager
from .git_integration import GitWorkflow
from .github import GitHubClient
from .issue_parser import IssueParser
from .llm_critic import (
    LLMCritic,
    LLMCriticWithMemory,
    create_llm_critic,
)
from .llm_planner import (
    LLMPlanner,
    LLMPlannerWithMemory,
    create_llm_planner,
)
from .memory import (
    LearningAgent,
    PatternMemory,
    SessionRecord,
    SuccessPattern,
)
from .models import (
    AgentState,
    CodeSymbol,
    ExploreResult,
    FileInfo,
    Plan,
    PlanStep,
    StepStatus,
    StepType,
    VerificationResult,
)
from .patch_utils import PatchManager
from .planner import WorkPlanner
from .pr_reviewer import (
    PRReviewer,
    PRReviewResult,
    ReviewCategory,
    ReviewComment,
    ReviewSeverity,
)
from .state import StateManager
from .test_generator import (
    EdgeCaseAnalyzer,
    MockGenerator,
    ParameterCombinationGenerator,
    TestGenerator,
)
from .type_inference import (
    InferenceResult,
    TypeInferenceVisitor,
    TypeInfo,
    create_type_analyzer,
    infer_file,
    infer_source,
    join_types,
)
from .vector_memory import (
    VectorLearningAgent,
    VectorPattern,
    VectorPatternMemory,
    create_vector_learning_agent,
    create_vector_memory,
)
from .verifier import Verifier
from .web_search import DocumentationParser, VersionChecker, WebSearcher

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
    "PatternMemory",
    "LearningAgent",
    "SuccessPattern",
    "SessionRecord",
    "VectorPatternMemory",
    "VectorLearningAgent",
    "VectorPattern",
    "create_vector_memory",
    "create_vector_learning_agent",
    "LLMPlanner",
    "LLMPlannerWithMemory",
    "create_llm_planner",
    "LLMCritic",
    "LLMCriticWithMemory",
    "create_llm_critic",
    "TypeInfo",
    "InferenceResult",
    "TypeInferenceVisitor",
    "infer_source",
    "infer_file",
    "join_types",
    "create_type_analyzer",
    "AnalysisResult",
    "Definition",
    "Use",
    "DefUseChain",
    "DependencyEdge",
    "analyze_dataflow_source",
    "analyze_dataflow_file",
    "create_dataflow_analyzer",
    "DashboardServer",
    "SessionProgress",
    "StepProgress",
    "get_dashboard",
    "start_dashboard",
]

__version__ = "0.1.0"
