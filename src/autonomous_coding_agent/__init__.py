"""
Autonomous Coding Agent - Codex/Claude Code 수준의 자율 코딩 에이전트 파이프라인
"""

from .agent import AutonomousCodingAgent
from .autopilot import (
    Autopilot,
    AutopilotConfig,
    AutopilotResult,
    IssueRunResult,
    create_autopilot,
)
from .code_adapter import (
    CodeExampleAdapter,
    CodeExampleApplier,
    ProjectAnalyzer,
)
from .codebase_indexer import (
    CodebaseIndexer,
    ContextBuilder,
    IndexedFile,
    SearchResult,
    create_codebase_indexer,
    create_context_builder,
)
from .coder import CodeGenerator
from .critic import Critic as CodeCritic
from .dashboard import (
    AutopilotRun,
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
from .llm_client import chat as llm_chat
from .llm_client import ollama_chat, openrouter_chat
from .llm_coder import LLMCoder, create_llm_coder
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
from .metrics import (
    ClassMetrics,
    FunctionMetrics,
    MetricsResult,
    risk_rank,
)
from .metrics import (
    analyze_file as analyze_metrics_file,
)
from .metrics import (
    analyze_source as analyze_metrics_source,
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
from .notify import send_telegram
from .patch_utils import PatchManager
from .planner import WorkPlanner
from .pr_reviewer import (
    PRReviewer,
    PRReviewResult,
    ReviewCategory,
    ReviewComment,
    ReviewSeverity,
)
from .quality_gate import (
    Finding,
    GateConfig,
    GateResult,
    create_quality_gate,
    gate_summary,
)
from .quality_gate import (
    check_against_baseline as check_quality_against_baseline,
)
from .quality_gate import (
    check_file as check_quality_file,
)
from .quality_gate import (
    check_paths as check_quality_paths,
)
from .quality_gate import (
    check_source as check_quality_source,
)
from .quality_gate import (
    new_findings as quality_new_findings,
)
from .rollback import (
    RollbackConfig,
    RollbackError,
    RollbackPlan,
    RollbackResult,
    execute_rollback,
    plan_rollback,
    rollback_pr,
)
from .rollback import (
    main as rollback_main,
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
from .week3_3 import (
    DecompositionResult,
    IssueDecomposer,
    LLMReviewer,
    LLMReviewResult,
    ReviewComment,
    SubTask,
    TDDCycle,
    TDDResult,
    create_issue_decomposer,
    create_llm_reviewer,
    create_tdd_cycle,
)
from .week3_4 import (
    ContextManager,
    EscalationManager,
    EscalationRequest,
    LLMCallRecord,
    Telemetry,
    TelemetrySummary,
    create_context_manager,
    create_escalation_manager,
    create_telemetry,
    get_global_telemetry,
    get_telemetry,
    record_llm_call,
)

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
    "llm_chat",
    "ollama_chat",
    "openrouter_chat",
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
    "FunctionMetrics",
    "ClassMetrics",
    "MetricsResult",
    "analyze_metrics_source",
    "analyze_metrics_file",
    "risk_rank",
    "GateConfig",
    "GateResult",
    "Finding",
    "check_quality_source",
    "check_quality_file",
    "check_quality_paths",
    "gate_summary",
    "create_quality_gate",
    "check_quality_against_baseline",
    "quality_new_findings",
    "send_telegram",
    "RollbackConfig",
    "RollbackError",
    "RollbackPlan",
    "RollbackResult",
    "plan_rollback",
    "execute_rollback",
    "rollback_pr",
    "rollback_main",
    "Autopilot",
    "AutopilotConfig",
    "AutopilotResult",
    "IssueRunResult",
    "create_autopilot",
    "LLMCoder",
    "create_llm_coder",
    "IssueDecomposer",
    "SubTask",
    "DecompositionResult",
    "create_issue_decomposer",
    "TDDCycle",
    "TDDResult",
    "create_tdd_cycle",
    "LLMReviewer",
    "LLMReviewResult",
    "ReviewComment",
    "create_llm_reviewer",
    "CodebaseIndexer",
    "ContextBuilder",
    "IndexedFile",
    "SearchResult",
    "create_codebase_indexer",
    "create_context_builder",
    "ContextManager",
    "Telemetry",
    "TelemetrySummary",
    "LLMCallRecord",
    "get_telemetry",
    "record_llm_call",
    "EscalationManager",
    "EscalationRequest",
    "create_context_manager",
    "create_telemetry",
    "get_global_telemetry",
    "create_escalation_manager",
    "DashboardServer",
    "SessionProgress",
    "StepProgress",
    "AutopilotRun",
    "get_dashboard",
    "start_dashboard",
]

__version__ = "0.1.0"
