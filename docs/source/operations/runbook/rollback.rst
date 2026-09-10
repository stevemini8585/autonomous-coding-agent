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

Autopilot 오머지 롤백 (자동화)
-------------------------------

Autopilot이 잘못 머지한 PR은 ``rollback`` 모듈로 revert PR + 연결 이슈 재오픈을
한 번에 처리한다. main 직접 푸시는 하지 않으며, 항상 revert PR 경유이다.

.. code-block:: bash

   # 1) 계획만 확인 (읽기 전용: gh pr view + git status만 실행, 변경 없음)
   PYTHONPATH=src python -m autonomous_coding_agent.rollback 34 --dry-run --workspace /path/to/repo

   # 2) 실행 (revert 브랜치 → revert PR → 이슈 재오픈 → 텔레그램 알림)
   PYTHONPATH=src python -m autonomous_coding_agent.rollback 34 --workspace /path/to/repo

   # 옵션:
   #   --base main        기준 브랜치 (기본값: PR의 baseRef)
   #   --no-reopen        이슈 재오픈 생략
   #   --quiet            텔레그램 알림 생략

동작 순서:

1. ``gh pr view`` 로 머지 상태·머지 커밋·연결 이슈 확인 (미머지면 즉시 중단)
2. 작업 트리가 깨끗한지 확인 (더러우면 중단 — 커밋/스태시 후 재시도)
3. ``revert/pr-<N>`` 브랜치에서 ``git revert -m 1 <merge-sha>`` 후 푸시
4. revert PR 생성 (제목: ``Revert #<N>``)
5. 연결 이슈 ``reopen`` + 원인 코멘트
6. 텔레그램 알림 (성공/실패)

충돌(``CONFLICT``) 시 자동 중단되며, 작업자는 로컬에서 수동 해결 후
revert PR을 완성한다. 관련 테스트: ``tests/test_rollback.py``.