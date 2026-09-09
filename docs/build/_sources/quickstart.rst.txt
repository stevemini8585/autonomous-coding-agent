Quickstart Guide
=================

Installation
------------

.. code-block:: bash

   git clone https://github.com/stevemini8585/autonomous-coding-agent.git
   cd autonomous-coding-agent
   pip install -e .[dev]

Basic Usage
-----------

Run the autonomous agent on a workspace:

.. code-block:: python

   from autonomous_coding_agent import run_autonomous

   result = run_autonomous(
       goal="Add a REST API endpoint for user management",
       workspace="/path/to/your/project",
       task_type="feature",
       max_iterations=5,
       verify_tests=True,
       verify_lint=True,
       verify_types=True,
   )

   print(f"Success: {result.success}")
   print(f"Summary: {result.summary}")
   print(f"Files changed: {len(result.files_changed)}")

Command Line Interface
----------------------

.. code-block:: bash

   # Run autonomous agent
   python -m autonomous_coding_agent /path/to/workspace "Add a new feature"

   # With options
   python -m autonomous_coding_agent /path/to/workspace "Fix bug in login" \
       --task-type bugfix \
       --max-iterations 3 \
       --no-verify-tests

Configuration
-------------

Create a ``config.yaml`` in your project root or ``~/.config/autonomous-coding-agent/config.yaml``:

.. code-block:: yaml

   agent:
     max_iterations: 5
     timeout_per_step: 300
     parallel_steps: true
     verify_tests: true
     verify_lint: true
     verify_types: true
     coverage_threshold: 80.0

   dashboard:
     enabled: true
     port: 8899

   git:
     auto_commit: false
     auto_push: false

   github:
     token: "${GITHUB_TOKEN}"  # Set via environment variable

Environment Variables
---------------------

.. code-block:: bash

   export GITHUB_TOKEN="your_github_token"
   export AUTONOMOUS_AGENT_CONFIG="/path/to/config.yaml"

Running Tests
-------------

.. code-block:: bash

   # Run all tests
   pytest tests/ -v

   # With coverage
   pytest tests/ --cov=src --cov-report=html

   # Property-based tests
   pytest tests/property/ -v

   # Chaos tests
   pytest tests/integration/test_chaos.py -v

Next Steps
----------

* Read the :doc:`architecture/overview` to understand the system design
* Check :doc:`modules/agent` for the main controller
* See :doc:`operations/runbook` for operational procedures