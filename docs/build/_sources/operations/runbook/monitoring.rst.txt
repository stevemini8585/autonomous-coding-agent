Monitoring & Alerting
=====================

This document describes monitoring and alerting for the Autonomous Coding Agent system.

Metrics to Monitor
------------------

**CI/CD Metrics**

+------------------------+---------+------------------+
| Metric                 | Target  | Alert Threshold  |
+========================+=========+==================+
| Build Success Rate     | > 95%   | < 90%            |
+------------------------+---------+------------------+
| Test Pass Rate         | 100%    | < 100%           |
+------------------------+---------+------------------+
| Coverage               | > 50%   | < 43%            |
+------------------------+---------+------------------+
| Build Duration         | < 10 min| > 15 min         |
+------------------------+---------+------------------+

**Agent Runtime Metrics**

+---------------------------+----------+------------------+
| Metric                    | Target   | Alert Threshold  |
+===========================+==========+==================+
| Session Success Rate      | > 80%    | < 60%            |
+---------------------------+----------+------------------+
| Avg Iterations            | < 3      | > 5              |
+---------------------------+----------+------------------+
| Avg Duration              | < 5 min  | > 10 min         |
+---------------------------+----------+------------------+
| Checkpoint Creation       | Every 2  | Missing > 4      |
|                           | iterations| iterations      |
+---------------------------+----------+------------------+

**System Metrics**

+------------------+---------+------------------+
| Metric           | Target  | Alert Threshold  |
+==================+=========+==================+
| Disk Usage       | < 70%   | > 85%            |
+------------------+---------+------------------+
| Memory Usage     | < 80%   | > 90%            |
+------------------+---------+------------------+
| Lock Contention  | 0       | > 5/min          |
+------------------+---------+------------------+

Dashboard Access
----------------

**GitHub Actions Dashboard**

- URL: https://github.com/stevemini8585/autonomous-coding-agent/actions
- Shows: All workflow runs, success/failure, duration

**Agent Dashboard (Local)**

- URL: http://localhost:8899 (when running)
- Shows: Real-time session progress, step status, logs

**Custom Dashboard Queries**

.. code-block:: bash

   # CI success rate last 30 days
   gh run list --repo stevemini8585/autonomous-coding-agent --limit 100 --json conclusion,createdAt | jq 'map(select(.conclusion=="success")) | length'

   # Agent sessions today
   find ~/.hermes/skills/autonomous-ai-agents/autonomous-coding-agent -name "session_*.json" -mtime -1 | wc -l

Alerting Rules
--------------

**GitHub Actions Notifications**

- Configured in CI workflow: ``notify-failure`` job
- Sends error annotation on any job failure

**Custom Alerts (Future Enhancement)**

- Webhook to Slack/Discord on SEV-1/2
- Email on coverage drop
- PagerDuty integration for critical failures

Log Locations
-------------

.. code-block:: bash

   # Agent logs
   ~/.hermes/logs/agent.log
   
   # Error logs (WARNING+)
   ~/.hermes/logs/errors.log
   
   # Gateway logs
   ~/.hermes/logs/gateway.log

   # View recent errors
   grep -i error ~/.hermes/logs/agent.log | tail -20
   
   # Follow logs
   tail -f ~/.hermes/logs/agent.log

Health Checks
-------------

**Automated Health Checks**

.. code-block:: bash

   #!/bin/bash
   # health_check.sh
   
   # 1. Import check
   python -c "from autonomous_coding_agent import AutonomousCodingAgent; print('✅ Imports OK')" || exit 1
   
   # 2. Self-test
   python -c "
   import tempfile
   from pathlib import Path
   from autonomous_coding_agent import TestGenerator
   with tempfile.TemporaryDirectory() as tmpdir:
       tmp_path = Path(tmpdir)
       (tmp_path / 'sample.py').write_text('def hello(): pass')
       generator = TestGenerator(tmp_path)
       module = generator.generate_tests_for_file('sample.py')
       print('✅ Self-test OK')
   " || exit 1
   
   # 3. Disk space
   df -h /path/to/workspace | awk 'NR==2 {if ($5+0 > 85) exit 1}' || exit 1
   
   echo "✅ All health checks passed"

**Schedule**: Run via cron every 15 minutes

Troubleshooting Dashboard Issues
--------------------------------

**Dashboard Not Loading**

- Check port 8899 is free: ``lsof -i :8899``
- Check firewall rules
- Restart: ``pkill -f dashboard; python -m autonomous_coding_agent.dashboard``

**Stale Data**

- Clear browser cache
- Check WebSocket connection in browser dev tools
- Verify agent is sending updates

**Missing Sessions**

- Verify ``.autonomous_state`` directory permissions
- Check state_manager.save_state() is called
- Look for JSON parse errors in logs