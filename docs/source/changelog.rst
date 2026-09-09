Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

[Unreleased]
------------

Added
~~~~~

- Complete documentation with Sphinx
- Runbook with deployment, rollback, incident response procedures
- Postmortem template and example
- Chaos testing suite (13 tests)
- Property-based testing with Hypothesis (21 tests)
- Mutation testing integration (Mutmut)
- CodeQL, Semgrep, Gitleaks security scanning
- Dependabot with auto-fix PR creation

Changed
~~~~~~~

- Improved StateManager with checkpoint restore and locking
- Enhanced AutonomousCodingAgent with auto-recovery
- Increased test coverage from 30% to 51%
- Fixed lint issues (ruff, black)

Fixed
~~~~~

- Lock file handling in StateManager
- JSON decode error in corrupted checkpoint test
- Various type hints and import issues

[0.1.0] - 2024-01-15
---------------------

Added
~~~~~

- Initial autonomous coding agent implementation
- CodeExplorer: AST-based codebase exploration
- WorkPlanner: Dependency-aware task planning
- CodeGenerator: AST-based code generation
- Verifier: Multi-layer validation (tests, lint, types, format)
- CodeCritic: Quality review with retry logic
- StateManager: Persistent state with checkpoints
- PatternMemory + LearningAgent: Cross-session learning
- GitManager: Git operations wrapper
- GitHubClient: GitHub API integration
- GitWorkflow: Feature branch + PR workflow
- PRReviewer: Automated PR review
- WebSearcher: Documentation/API search
- IssueParser: GitHub issue parsing with dependencies
- Dashboard: Real-time progress visualization
- CI Pipeline: Lint, test, security, build, deploy
- Integration tests: E2E pipeline (10 tests)
- Unit tests: Core modules (17 tests)

Security
~~~~~~~~

- pip-audit integration
- Safety check integration
- Bandit static analysis
- Gitleaks secret scanning

[0.0.1] - 2024-01-01
---------------------

Added
~~~~~

- Project initialization
- Basic project structure
- Development environment setup