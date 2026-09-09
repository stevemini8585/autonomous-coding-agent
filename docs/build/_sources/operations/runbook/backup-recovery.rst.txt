Backup & Recovery
=================

This document describes backup and recovery procedures for the Autonomous Coding Agent system.

What to Backup
--------------

**Critical Data:**

1. **Agent State** (``.autonomous_state/``)
   - Session JSON files
   - Checkpoint files
   - Lock files (excluded)

2. **Workspace Code** (``src/``, ``tests/``, project files)
   - Version controlled via Git

3. **Configuration** (``config.yaml``, ``pyproject.toml``, ``.env``)
   - Version controlled (except ``.env`` secrets)

4. **Logs** (``~/.hermes/logs/``)
   - Rotated automatically

Backup Strategy
---------------

**Git-Based (Primary)**
- All code and config in Git
- Push to remote on every commit
- Tags for releases

**State Snapshots (Automatic)**
- Checkpoints created every 2 iterations
- Manual checkpoints before risky operations
- Stored in ``.autonomous_state/``

**Manual Backup Commands**

.. code-block:: bash

   # Full state backup
   tar -czf backup-$(date +%Y%m%d-%H%M%S).tar.gz \
       --exclude='.git' \
       --exclude='__pycache__' \
       --exclude='*.pyc' \
       --exclude='mutants' \
       --exclude='.venv' \
       --exclude='dist' \
       --exclude='build' \
       /path/to/workspace

   # State only
   tar -czf state-backup-$(date +%Y%m%d).tar.gz \
       /path/to/workspace/.autonomous_state

   # Config only
   tar -czf config-backup-$(date +%Y%m%d).tar.gz \
       /path/to/workspace/config.yaml \
       /path/to/workspace/pyproject.toml \
       /path/to/workspace/.github

Automated Backup (Cron)
-----------------------

.. code-block:: bash

   # Add to crontab (crontab -e)
   # Daily at 2 AM: Full workspace backup
   0 2 * * * /path/to/backup.sh >> /var/log/autonomous-agent-backup.log 2>&1
   
   # Hourly: State snapshots
   0 * * * * /path/to/state-snapshot.sh >> /var/log/autonomous-agent-state.log 2>&1

Recovery Procedures
-------------------

**1. Full Workspace Recovery**

.. code-block:: bash

   # Stop any running agents
   pkill -f autonomous_coding_agent
   
   # Restore from backup
   tar -xzf backup-20240115-020000.tar.gz -C /path/to/restore
   
   # Verify
   cd /path/to/restore
   python -c "from autonomous_coding_agent import AutonomousCodingAgent; print('OK')"

**2. State Recovery**

.. code-block:: python

   from autonomous_coding_agent import StateManager, AutonomousCodingAgent
   from pathlib import Path

   workspace = Path("/path/to/workspace")
   sm = StateManager(workspace)

   # List sessions
   sessions = sm.list_sessions()
   print(f"Found {len(sessions)} sessions")

   # Restore specific session
   if sessions:
       session = sessions[0]
       state = sm.load_state(session['session_id'])
       
       # Or restore from checkpoint
       checkpoints = sm.list_checkpoints(session['session_id'])
       if checkpoints:
           restored = sm.restore_checkpoint(
               session['session_id'], 
               checkpoints[0]['checkpoint_id']
           )

**3. Configuration Recovery**

.. code-block:: bash

   # Restore config files
   tar -xzf config-backup-20240115.tar.gz -C /path/to/workspace
   
   # Restore secrets (manual)
   # Copy .env from secure location

**4. Log Recovery**

.. code-block:: bash

   # Logs are rotated, old logs in archive
   tar -xzf logs-backup-20240115.tar.gz -C ~/.hermes/logs

Disaster Recovery Plan
----------------------

**Scenario: Complete Data Loss**

1. Clone repository
   .. code-block:: bash
      git clone https://github.com/stevemini8585/autonomous-coding-agent.git
      cd autonomous-coding-agent

2. Install dependencies
   .. code-block:: bash
      pip install -e .[dev]

3. Restore state from latest backup
   .. code-block:: bash
      tar -xzf state-backup-latest.tar.gz

4. Verify system
   .. code-block:: bash
      pytest tests/ -v --cov=src --cov-fail-under=43

**RTO/RPO Targets**

| Recovery Tier | RTO (Recovery Time) | RPO (Recovery Point) |
|---------------|---------------------|----------------------|
| Code/Config | < 15 min | 0 (Git) |
| Agent State | < 5 min | < 2 iterations |
| Logs | < 1 hour | 24 hours |

Testing Backups
---------------

**Monthly Backup Test**

.. code-block:: bash

   #!/bin/bash
   # test_backup.sh
   
   BACKUP_FILE="backup-$(date +%Y%m%d).tar.gz"
   
   # 1. Create test workspace
   TEST_DIR="/tmp/autonomous-agent-backup-test-$$"
   mkdir -p "$TEST_DIR"
   
   # 2. Extract backup
   tar -xzf "$BACKUP_FILE" -C "$TEST_DIR"
   
   # 3. Verify structure
   if [ ! -d "$TEST_DIR/src/autonomous_coding_agent" ]; then
       echo "FAIL: Source code not found"
       exit 1
   fi
   
   # 4. Verify imports
   cd "$TEST_DIR"
   python -c "from autonomous_coding_agent import AutonomousCodingAgent" || exit 1
   
   # 5. Quick test
   pytest tests/integration/test_e2e_pipeline.py::TestE2EPipeline::test_01_explorer -v || exit 1
   
   echo "✅ Backup test passed"
   
   # 6. Cleanup
   rm -rf "$TEST_DIR"

Schedule: Run monthly, alert on failure

Offsite Backup
--------------

- **GitHub**: Primary remote (code + config)
- **GitHub Releases**: Tagged releases with artifacts
- **Local/External Drive**: Periodic full backups
- **Cloud Storage** (optional): Encrypted state snapshots

Verification Checklist
----------------------

After any recovery:

- [ ] Git history intact
- [ ] All tests pass (``pytest tests/``)
- [ ] Coverage gate passes (``pytest --cov=src --cov-fail-under=43``)
- [ ] Lint clean (``ruff check . && black --check .``)
- [ ] Security scan clean (``pip-audit --desc``)
- [ ] Agent can start new session
- [ ] Agent can resume from checkpoint
- [ ] Dashboard accessible
- [ ] Logs writing correctly