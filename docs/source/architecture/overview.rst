Architecture Overview
=====================

The Autonomous Coding Agent is a modular, stateful system designed to autonomously execute coding tasks from exploration to pull request creation.

High-Level Architecture
-----------------------

.. mermaid::

   graph TB
       subgraph "External Systems"
           GH[GitHub API]
           WS[Web Search]
       end

       subgraph "Agent Core"
           AGENT[AutonomousCodingAgent]
           STATE[StateManager]
           DASH[Dashboard]
       end

       subgraph "Pipeline Modules"
           EXP[CodeExplorer]
           PLAN[WorkPlanner]
           CODE[CodeGenerator]
           VER[Verifier]
           CRIT[CodeCritic]
       end

       subgraph "Support Modules"
           MEM[PatternMemory + LearningAgent]
           GIT[GitManager]
           GH_C[GitHubClient]
           IPS[IssueParser]
           PR[PRReviewer]
           WS_C[WebSearcher]
           VP[VersionChecker]
           CA[CodeExampleAdapter]
       end

       AGENT --> EXP
       AGENT --> PLAN
       AGENT --> CODE
       AGENT --> VER
       AGENT --> CRIT
       
       AGENT --> STATE
       AGENT --> DASH
       AGENT --> MEM
       
       CODE --> GIT
       AGENT --> GH_C
       AGENT --> IPS
       AGENT --> PR
       AGENT --> WS_C
       AGENT --> VP
       AGENT --> CA

       STATE -.->|checkpoints| AGENT
       DASH -.->|progress| AGENT

Data Flow
---------

1. **Goal Input** → Agent receives coding goal
2. **Explore** → CodeExplorer analyzes workspace, builds symbol graph
3. **Plan** → WorkPlanner creates dependency-ordered execution plan
4. **Execute Loop** (iterative):
   - CodeGenerator implements changes
   - Verifier validates (tests, lint, types, format)
   - CodeCritic reviews quality
   - Retry on failure (max 3x per step)
5. **Final Verification** → Full project validation
6. **PR Creation** → GitHubClient creates PR via GitWorkflow
7. **Learning** → PatternMemory stores successful patterns

State Management
----------------

The system uses a **checkpoint-based state machine**:

- **AgentState**: Complete session state (goal, plan, progress, iteration)
- **Checkpoints**: Immutable snapshots every 2 iterations + manual
- **Persistence**: JSON files in `.autonomous_state/`
- **Recovery**: `restore_checkpoint()` / `resume_from_checkpoint()`
- **Concurrency**: File-based locking (`fcntl`) prevents parallel runs

Key Design Principles
---------------------

1. **Modularity**: Each pipeline stage is a separate class
2. **Observability**: Dashboard streams real-time progress
3. **Resilience**: Auto-retry, checkpoint rollback, chaos-tested
4. **Learning**: PatternMemory enables cross-session improvement
5. **Security**: Sandboxed execution, secret scanning, dependency auditing
6. **Extensibility**: Clean interfaces for custom modules

Technology Stack
----------------

- **Language**: Python 3.11+
- **Async**: asyncio for I/O-bound operations
- **AST**: `ast` module for code analysis/generation
- **Git**: `GitPython` for repository operations
- **GitHub**: `ghapi` for API interactions
- **Testing**: pytest + hypothesis + mutmut
- **Monitoring**: Custom dashboard (FastAPI + WebSocket)
- **Documentation**: Sphinx + sphinx-autodoc2