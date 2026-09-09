Rollback Procedures
===================

This document describes rollback procedures for the Autonomous Coding Agent system.

When to Rollback
----------------

- CI pipeline failure on main branch
- Post-deployment regression detected
- Security vulnerability in production
- Agent producing incorrect/unsafe code

Rollback Types
--------------

**1. Git Revert (Preferred)**

.. code-block:: bash

   # Revert specific commit
   git revert <commit-hash>
   git push origin main

   # Revert merge commit
   git revert -m 1 <merge-commit-hash>
   git push origin main

**2. Hard Reset (Emergency Only)**

.. code-block:: bash

   # Reset to previous tag
   git fetch --tags
   git reset --hard v0.1.0
   git push --force-with-lease origin main

   # Reset to specific commit
   git reset --hard <commit-hash>
   git push --force-with-lease origin main

**3. Agent State Rollback**

If agent was mid-execution:

.. code-block:: python

   from autonomous_coding_agent import AutonomousCodingAgent, StateManager
   from pathlib import Path

   workspace = Path("/path/to/workspace")
   agent = AutonomousCodingAgent(workspace)

   # List available checkpoints
   checkpoints = agent.state_manager.list_checkpoints(agent.state.session_id)
   print(f"Available checkpoints: {len(checkpoints)}")

   # Rollback to specific checkpoint
   if checkpoints:
       # Option A: Automatic rollback (modifies current state)
       agent.state_manager.rollback_to_checkpoint(
           agent.state, 
           checkpoints[0]['checkpoint_id']
       )
       
       # Option B: Restore to new state object
       restored_state = agent.state_manager.restore_checkpoint(
           agent.state.session_id,
           checkpoints[0]['checkpoint_id']
       )
       
       # Resume from checkpoint
       result = agent.resume_from_checkpoint(checkpoints[0]['checkpoint_id'])

Post-Rollback Verification
--------------------------

1. **Verify CI passes**

   .. code-block:: bash
   
      # Trigger CI
      git push origin main
      gh run watch --repo stevemini8585/autonomous-coding-agent

2. **Run smoke tests**

   .. code-block:: bash
   
      pytest tests/integration/test_e2e_pipeline.py -v

3. **Verify agent functionality**

   .. code-block:: python
   
      result = agent.run("Simple test goal")
      assert result.success

Rollback Checklist
------------------

- [ ] Identify rollback reason and document
- [ ] Choose appropriate rollback method
- [ ] Execute rollback
- [ ] Verify CI passes
- [ ] Run smoke tests
- [ ] Verify agent state consistency
- [ ] Notify team
- [ ] Create incident record
- [ ] Schedule postmortem if SEV-1/2