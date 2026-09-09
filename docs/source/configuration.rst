Configuration
=============

The Autonomous Coding Agent can be configured via:

1. **Project config** (``config.yaml`` in workspace root)
2. **User config** (``~/.config/autonomous-coding-agent/config.yaml``)
3. **Environment variables** (highest priority for secrets)

Configuration File (config.yaml)
--------------------------------

.. code-block:: yaml

   # Agent behavior
   agent:
     max_iterations: 5
     timeout_per_step: 300
     parallel_steps: true
     verify_tests: true
     verify_lint: true
     verify_types: true
     coverage_threshold: 80.0
     auto_commit: false
     hitl_on_failure: true

   # Dashboard
   dashboard:
     enabled: true
     host: "0.0.0.0"
     port: 8899

   # Git operations
   git:
     auto_commit: false
     auto_push: false
     commit_message_template: "feat: {goal_summary}"

   # GitHub integration
   github:
     token: "${GITHUB_TOKEN}"
     base_branch: "main"
     draft_pr: true

   # Web search
   web_search:
     enabled: true
     max_results: 10
     timeout: 30

   # Learning/memory
   memory:
     enabled: true
     max_patterns: 1000
     similarity_threshold: 0.7

   # Security
   security:
     scan_dependencies: true
     block_on_critical: true
     allowed_hosts: []

Environment Variables
---------------------

.. code-block:: bash

   # Required for GitHub operations
   export GITHUB_TOKEN="ghp_xxxxxxxxxxxx"
   
   # Optional overrides
   export AUTONOMOUS_AGENT_MAX_ITERATIONS=10
   export AUTONOMOUS_AGENT_DASHBOARD_PORT=8899
   export AUTONOMOUS_AGENT_VERIFY_TESTS=false

   # Config file location
   export AUTONOMOUS_AGENT_CONFIG="/path/to/config.yaml"

Configuration Priority
----------------------

1. Environment variables (highest)
2. Project config.yaml
3. User config.yaml
4. Defaults (lowest)

Example: Complete config.yaml
-----------------------------

.. code-block:: yaml

   agent:
     max_iterations: 5
     timeout_per_step: 300
     parallel_steps: true
     verify_tests: true
     verify_lint: true
     verify_types: true
     coverage_threshold: 80.0
     auto_commit: false
     hitl_on_failure: true
   
   dashboard:
     enabled: true
     host: "0.0.0.0"
     port: 8899
   
   git:
     auto_commit: false
     auto_push: false
     commit_message_template: "feat: {goal_summary}"
   
   github:
     token: "${GITHUB_TOKEN}"
     base_branch: "main"
     draft_pr: true
   
   web_search:
     enabled: true
     max_results: 10
     timeout: 30
   
   memory:
     enabled: true
     max_patterns: 1000
     similarity_threshold: 0.7
   
   security:
     scan_dependencies: true
     block_on_critical: true
     allowed_hosts: []

Validation
----------

.. code-block:: bash

   # Validate config
   python -c "
   import yaml
   with open('config.yaml') as f:
       config = yaml.safe_load(f)
   print('Config valid:', config)
   "