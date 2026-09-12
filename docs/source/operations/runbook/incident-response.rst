Incident Response
=================

This document describes the incident response procedures for the Autonomous Coding Agent system.

Incident Classification
-----------------------

**Severity Levels:**

| Severity | Description | Response Time | Escalation |
|----------|-------------|---------------|------------|
| **SEV-1 (Critical)** | Agent completely non-functional, data loss risk | Immediate | Page on-call |
| **SEV-2 (High)** | Major functionality broken, workarounds exist | 1 hour | Notify team |
| **SEV-3 (Medium)** | Partial degradation, non-critical features | 4 hours | Next business day |
| **SEV-4 (Low)** | Cosmetic issues, documentation | Next sprint | Backlog |

Incident Response Process
-------------------------

1. **Detection**
   
   - Automated: CI failure alerts, monitoring alerts
   - Manual: User reports, logs analysis

2. **Triage**
   
   .. code-block:: bash
   
      # Quick health check
      python -c "from autonomous_coding_agent import AutonomousCodingAgent; print('Imports OK')"
      
      # Check recent CI runs
      gh run list --repo stevemini8585/autonomous-coding-agent --limit 5
      
      # Check agent logs
      tail -100 ~/.hermes/logs/agent.log

3. **Investigation**
   
   - Check error logs
   - Reproduce in isolation
   - Identify root cause

4. **Resolution**
   
   - Apply fix
   - Verify with tests
   - Deploy fix

5. **Post-Incident**
   
   - Create postmortem (see :doc:`/operations/postmortem-template`)
   - Update runbook
   - Implement preventive measures

Common Incidents & Responses
----------------------------

**CI Pipeline Failure**

.. code-block:: bash

   # Check which job failed
   gh run view <run-id> --repo stevemini8585/autonomous-coding-agent
   
   # Common causes:
   # - Lint failure: ruff check --fix && black .
   # - Test failure: Check test logs, fix code
   # - Coverage drop: Add tests for new code
   # - Security scan: pip-audit --fix

**Agent Hangs/Timeout**

.. code-block:: bash

   # Kill stuck processes
   pkill -f autonomous_coding_agent
   
   # Clean lock files
   find /workspace -name ".lock" -delete
   
   # Restart with fresh session
   python -m autonomous_coding_agent /workspace "Goal"

**GitHub API Rate Limit**

.. code-block:: bash

   # Check rate limit
   gh api rate_limit
   
   # Wait or use different token
   export GITHUB_TOKEN="alternative_token"

**State Corruption**

.. code-block:: python

   # List available sessions
   from autonomous_coding_agent import StateManager
   from pathlib import Path
   
   sm = StateManager(Path("/workspace"))
   sessions = sm.list_sessions()
   
   # Restore from latest good checkpoint
   checkpoints = sm.list_checkpoints(sessions[0]['session_id'])
   if checkpoints:
       state = sm.restore_checkpoint(sessions[0]['session_id'], checkpoints[0]['checkpoint_id'])

**Security Vulnerability Found**

.. code-block:: bash

   # Immediate: Block merge
   # Fix: pip-audit --fix
   # Verify: pip-audit --desc
   # Deploy hotfix if needed

Communication
-------------

- **Internal**: #autonomous-agent Slack channel
- **External**: GitHub Issues for tracking
- **Status Page**: Update if user-facing

Contacts
--------

- **Primary On-Call**: Steve (steve@mini.local)
- **Backup**: Check rotation schedule
- **Security**: security@mini.local

Runbook Maintenance
-------------------

- Review quarterly
- Update after each incident
- Version control all changes