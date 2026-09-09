Example Postmortem: CI Pipeline Failure Due to Dependency Conflict
===================================================================

**Date:** 2024-01-15  
**Author:** Steve  
**Status:** Published  
**Severity:** SEV-2 (High)  
**Duration:** 2 hours 15 minutes  
**Impact:** Internal only - blocked all merges to main for 2 hours

---

## Executive Summary

On 2024-01-15, the Autonomous Coding Agent CI pipeline failed for 2 hours 15 minutes due to a transitive dependency conflict introduced by an automated Dependabot PR. The conflict caused `pytest` collection errors that blocked all merges to main. Resolution: reverted the Dependabot PR and added a version constraint to prevent future conflicts.

---

## Timeline (UTC)

| Time (UTC) | Event |
|------------|-------|
| 10:00 | Dependabot PR #42 opened (update `pytest` 7.4 → 8.0) |
| 10:05 | CI pipeline triggered, tests started failing |
| 10:10 | First alert: CI failure on main branch |
| 10:15 | Triage started - identified pytest version conflict |
| 10:30 | Root cause: `pytest-asyncio` incompatible with `pytest` 8.0 |
| 10:45 | Fix: Reverted Dependabot PR, added `pytest<8.0` constraint |
| 11:00 | Verification: CI passing on revert commit |
| 11:15 | Incident resolved - merges unblocked |

---

## Root Cause Analysis

### What Happened

Automated Dependabot PR updated `pytest` from 7.4.4 to 8.0.0. This major version upgrade introduced breaking changes in the plugin API that `pytest-asyncio` 0.23 depended on. The test suite failed at collection phase with `AttributeError: module 'pytest' has no attribute 'yield_fixture'`.

### Why It Happened (5 Whys)

1. **Why?** Tests failed with `AttributeError: 'pytest' has no attribute 'yield_fixture'`
2. **Why?** `pytest-asyncio` 0.23 used deprecated `pytest.yield_fixture` removed in pytest 8.0
3. **Why?** Dependabot auto-merged patch/minor updates but this was a major version
4. **Why?** Dependabot config allowed major updates for `pytest` (no version constraint)
5. **Why?** No upper bound on `pytest` in `pyproject.toml` or Dependabot ignore rules

**Root Cause:** Missing version upper bound on `pytest` allowed Dependabot to introduce a breaking major version upgrade that was incompatible with existing test plugins.

### Contributing Factors

- No upper bound constraints on critical test dependencies
- Dependabot config didn't ignore major version updates for `pytest`
- CI didn't have a pre-merge compatibility check for test infrastructure
- No automated testing of Dependabot PRs before merge

---

## Impact Assessment

| Metric | Value |
|--------|-------|
| Users Affected | 0 (internal tool) |
| Merges Blocked | 3 PRs waiting |
| Developer Time Lost | ~2 hours × 2 developers |
| Data Loss | None |

**Affected Components:**
- [x] CI/CD Pipeline
- [ ] Agent Runtime
- [ ] GitHub Integration
- [ ] Dashboard
- [ ] State Management

---

## Resolution

### Immediate Fix

1. Reverted Dependabot PR #42 via GitHub UI
2. Added `pytest>=7.4,<8.0` constraint to `pyproject.toml`
3. Pushed fix to main branch

### Permanent Fix

1. Added version constraints for all test infrastructure dependencies
2. Updated Dependabot config to ignore major versions for `pytest`, `pytest-asyncio`, `pytest-cov`
3. Added pre-merge CI check for dependency compatibility

### Verification Steps

1. Ran full test suite locally: `pytest tests/ -v` ✅
2. Verified CI passes on fix branch ✅
3. Merged fix to main ✅
4. Verified Dependabot PRs now respect constraints ✅

---

## Action Items

| # | Action | Owner | Due Date | Status | Tracking |
|---|--------|-------|----------|--------|----------|
| 1 | Add upper bounds to all test deps in pyproject.toml | Steve | 2024-01-16 | Done | #43 |
| 2 | Update Dependabot config to ignore major versions for pytest ecosystem | Steve | 2024-01-16 | Done | #44 |
| 3 | Add CI job to validate Dependabot PRs before auto-merge | Steve | 2024-01-20 | In Progress | #45 |
| 4 | Document dependency management policy in runbook | Steve | 2024-01-18 | Open | #46 |

---

## Lessons Learned

### What Went Well

- Automated CI failure detection worked (alert within 5 minutes)
- Revert procedure was fast and safe (GitHub UI revert)
- Team communication via Slack was immediate

### What Could Be Improved

- No pre-merge validation for Dependabot PRs
- Missing version constraints on critical dependencies
- Runbook didn't cover "automated PR breaks CI" scenario
- No automated rollback for failed Dependabot merges

### Surprising Discoveries

- `pytest-asyncio` 0.23.3 (latest at the time) was already incompatible with pytest 8.0
- Dependabot's "automerge" for patch/minor doesn't protect against major if not explicitly configured

---

## Preventive Measures

### Technical Changes

- [x] Add `pytest>=7.4,<8.0` to `pyproject.toml`
- [x] Add `pytest-asyncio>=0.23,<1.0` constraint
- [x] Add `pytest-cov>=4.1,<5.0` constraint
- [x] Update `.github/dependabot.yml` with `ignore` rules for major versions
- [ ] Add CI job: `dependabot-validation` that runs full test suite on PRs

### Process Changes

- [x] Document dependency management policy in runbook
- [ ] Add "Dependency Update" section to PR review checklist
- [ ] Quarterly review of all version constraints

### Cultural/Organizational

- [ ] Team sync: "How we manage test dependencies" (15 min)
- [ ] Postmortem review meeting scheduled for 2024-01-22

---

## Appendix

### Related Links

- GitHub Issue: #42
- CI Run (failure): https://github.com/stevemini8585/autonomous-coding-agent/actions/runs/12345
- Dependabot PR: #42
- Fix PR: #43
- Relevant logs: `pytest` collection error with `yield_fixture`

### Supporting Data

```
============================= test session starts ==============================
AttributeError: module 'pytest' has no attribute 'yield_fixture'
  File "/workspace/tests/integration/test_e2e_pipeline.py", line 1
    import pytest
```

---

*Template version: 1.0*