Deployment Procedures
=====================

Standard Deployment
-------------------

1. **Pre-deployment Checks**
   
   .. code-block:: bash
   
      # Run full test suite
      pytest tests/ -v --cov=src --cov-fail-under=43
      
      # Lint check
      ruff check src/ tests/
      black --check src/ tests/
      
      # Security scan
      pip-audit --desc
      bandit -r src/

2. **Build Package**
   
   .. code-block:: bash
   
      python -m build
      twine check dist/*

3. **Deploy to Staging**
   
   .. code-block:: bash
   
      # Tag release
      git tag -a v0.1.0 -m "Release v0.1.0"
      git push origin v0.1.0
      
      # CI/CD will run automatically

4. **Post-deployment Verification**
   
   .. code-block:: bash
   
      # Verify agent imports
      python -c "from autonomous_coding_agent import AutonomousCodingAgent; print('OK')"
      
      # Run self-test
      python -c "
      import tempfile
      from pathlib import Path
      from autonomous_coding_agent import TestGenerator
      
      with tempfile.TemporaryDirectory() as tmpdir:
          tmp_path = Path(tmpdir)
          (tmp_path / 'sample.py').write_text('def hello(): pass')
          generator = TestGenerator(tmp_path)
          module = generator.generate_tests_for_file('sample.py')
          print('Self-test passed')
      "

Rollback Procedures
-------------------

If deployment fails or issues detected:

1. **Automatic Rollback (CI Failure)**
   
   The CI pipeline will block merge on failure. No manual rollback needed.

2. **Manual Rollback (Post-deployment Issue)**
   
   .. code-block:: bash
   
      # Revert to previous tag
      git revert HEAD
      git push origin main
      
      # Or reset to previous tag
      git reset --hard v0.0.9
      git push --force origin main

3. **State Recovery**
   
   If agent was running during deployment:
   
   .. code-block:: python
   
      from autonomous_coding_agent import AutonomousCodingAgent
      
      agent = AutonomousCodingAgent(workspace="/path/to/workspace")
      agent.state_manager.list_sessions()
      
      # Resume from latest checkpoint
      checkpoints = agent.state_manager.list_checkpoints(session_id)
      if checkpoints:
          agent.resume_from_checkpoint(checkpoints[0]['checkpoint_id'])

Emergency Procedures
--------------------

**Agent Stuck in Loop**

.. code-block:: bash

   # Find and kill agent process
   pkill -f "autonomous_coding_agent"
   
   # Check for orphaned locks
   find /path/to/workspace -name ".lock" -delete

**Disk Space Critical**

.. code-block:: bash

   # Clean old checkpoints
   find /path/to/workspace/.autonomous_state -name "*.json" -mtime +7 -delete
   
   # Clean mutants directory
   rm -rf mutants/

**Memory Leak**

.. code-block:: bash

   # Restart agent with fresh state
   # No state recovery - start new session
   python -m autonomous_coding_agent /path/to/workspace "Goal"