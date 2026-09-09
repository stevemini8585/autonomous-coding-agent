Postmortem Template
====================

Use this template for all SEV-1 and SEV-2 incidents. For SEV-3/4, a simplified version is acceptable.

---

# Postmortem: [Incident Title]

**Date:** YYYY-MM-DD  
**Author:** [Name]  
**Status:** [Draft / Under Review / Published]  
**Severity:** [SEV-1 / SEV-2 / SEV-3 / SEV-4]  
**Duration:** [X hours Y minutes]  
**Impact:** [User-facing / Internal only / Data loss risk]

---

## Executive Summary

**One-paragraph summary of what happened, impact, and resolution.**

Example: *"On 2024-01-15, the Autonomous Coding Agent CI pipeline failed for 2 hours due to a dependency conflict introduced by an automated Dependabot PR. The conflict caused test failures that blocked all merges to main. Resolution: reverted the PR and pinned the conflicting dependency."*

---

## Timeline (UTC)

| Time (UTC) | Event |
|------------|-------|
| HH:MM | Incident detected (how) |
| HH:MM | Triage started |
| HH:MM | Root cause identified |
| HH:MM | Fix deployed |
| HH:MM | Verification complete |
| HH:MM | Incident resolved |

---

## Root Cause Analysis

### What Happened

[Detailed description of the failure]

### Why It Happened (5 Whys)

1. **Why?** [Symptom]
2. **Why?** [Deeper cause]
3. **Why?** [Even deeper]
4. **Why?** [Systemic issue]
5. **Why?** [Root cause]

**Root Cause:** [Single sentence summarizing the fundamental cause]

### Contributing Factors

- [Factor 1: e.g., insufficient test coverage for X]
- [Factor 2: e.g., missing validation in CI]
- [Factor 3: e.g., unclear documentation]

---

## Impact Assessment

| Metric | Value |
|--------|-------|
| Users Affected | [Number / N/A] |
| Sessions Interrupted | [Number] |
| Data Loss | [None / Partial / Full - details] |
| Revenue Impact | [N/A for internal tools] |
| Reputation Impact | [None / Minor / Major] |

**Affected Components:**
- [ ] CI/CD Pipeline
- [ ] Agent Runtime
- [ ] GitHub Integration
- [ ] Dashboard
- [ ] State Management
- [ ] Other: _______

---

## Resolution

### Immediate Fix

[What was done to restore service]

### Permanent Fix

[What was done to prevent recurrence]

### Verification Steps

1. [Step 1]
2. [Step 2]
3. [Step 3]

---

## Action Items

| # | Action | Owner | Due Date | Status | Tracking |
|---|--------|-------|----------|--------|----------|
| 1 | [Description] | [Name] | YYYY-MM-DD | [Open/In Progress/Done] | [GitHub Issue #] |
| 2 | [Description] | [Name] | YYYY-MM-DD | [Open/In Progress/Done] | [GitHub Issue #] |
| 3 | [Description] | [Name] | YYYY-MM-DD | [Open/In Progress/Done] | [GitHub Issue #] |

---

## Lessons Learned

### What Went Well

- [e.g., automated alerts caught it quickly]
- [e.g., rollback procedure worked smoothly]
- [e.g., team communication was clear]

### What Could Be Improved

- [e.g., missing test case for X scenario]
- [e.g., runbook didn't cover this scenario]
- [e.g., monitoring gap for Y metric]

### Surprising Discoveries

- [Any unexpected findings during investigation]

---

## Preventive Measures

### Technical Changes

- [ ] [Specific code/config change]
- [ ] [Test addition]
- [ ] [Monitoring alert addition]
- [ ] [CI gate enhancement]

### Process Changes

- [ ] [Runbook update]
- [ ] [Documentation update]
- [ ] [Training/knowledge sharing]
- [ ] [Code review checklist update]

### Cultural/Organizational

- [ ] [Team discussion topic]
- [ ] [Postmortem review meeting scheduled]

---

## Appendix

### Related Links

- GitHub Issue: #[number]
- CI Run: [link]
- PR that introduced bug: #[number]
- PR that fixed bug: #[number]
- Relevant logs: [link or paste]

### Supporting Data

[Charts, graphs, log excerpts, metric screenshots]

---

## Review Checklist

Before publishing:

- [ ] All facts verified
- [ ] No blame language (focus on systems, not people)
- [ ] Action items have owners and due dates
- [ ] Reviewed by at least one other team member
- [ ] Published to team knowledge base
- [ ] Linked from incident tracking system

---

*Template version: 1.0*  
*Last updated: 2024-01-XX*