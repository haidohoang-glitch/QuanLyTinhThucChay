# Incident Response Playbook — Quality Checklist

Run before publishing playbook (and before treating it as production-ready).

## Gate 1 — Specificity

- [ ] Section 1 defines exactly ONE incident class
- [ ] Distinguishes from related incidents (Section 1 "What this incident is NOT")
- [ ] Severity criteria are concrete (specific symptoms, not "really bad")
- [ ] Detection signals are specific monitor/query/alert names

## Gate 2 — Triage runbook (CRITICAL)

- [ ] First 5 minutes are step-by-step
- [ ] Each step has explicit command or action
- [ ] No "investigate" without specifying what tools, queries, or dashboards
- [ ] Wait/timing thresholds explicit (e.g., "wait 60s")

## Gate 3 — Containment vs eradication separation

- [ ] Section 5 (Containment) only addresses stopping bleeding
- [ ] Section 6 (Eradicate) addresses root cause
- [ ] Containment doesn't require root cause known
- [ ] Containment has explicit "do NOT do" warnings (avoid making things worse)

## Gate 4 — Diagnostic approach

- [ ] Section 6 has structured diagnostic steps
- [ ] Common root causes table lists ≥3 typical causes for this incident class
- [ ] Each cause has Verify-by command and Fix approach
- [ ] Peer review step before applying fix

## Gate 5 — Recovery + verification

- [ ] Section 7 has explicit recovery steps
- [ ] Verification checklist non-empty (signals normal? smoke test? customer flow?)
- [ ] Monitoring window specified (e.g., "30 minutes" not "until ok")

## Gate 6 — Communication templates

- [ ] Internal Slack initial + update + resolution templates
- [ ] Status page initial + resolution templates
- [ ] Stakeholder update template (P0)
- [ ] Templates concise; no jargon for customer-facing

## Gate 7 — Escalation tree

- [ ] Section 9 escalation table covers P0/P1/P2
- [ ] Contact table has names + Slack handles + phone for P0
- [ ] Auto-escalation timing explicit ("if not acked in 5 min → secondary")

## Gate 8 — Postmortem trigger

- [ ] Section 10 explicit about which incidents require postmortem
- [ ] Postmortem template referenced
- [ ] Output location for postmortem docs specified

## Gate 9 — Drill / freshness

- [ ] Last drill date recorded
- [ ] Drill outcome documented
- [ ] If drill >6 months ago, flagged for re-drill

## Gate 10 — Completeness sanity

- [ ] All `{{PLACEHOLDER}}` filled
- [ ] All commands tested (or explicitly marked "untested")
- [ ] All links work
- [ ] Contact info current (names match current rotation)

## Gate 11 — Mode discipline

- [ ] Mode A: NIST IR phases (Prepare/Detect/Contain/Eradicate/Recover/Lessons)
- [ ] Mode B: company IR framework cited
- [ ] Mode C: user-defined phases; rationale documented

## Gate 12 — Format

- [ ] Output: `docs/04_MAINTENANCE/runbooks/INCIDENT_<TYPE>.md`
- [ ] Filename describes incident type clearly
- [ ] Sections numbered consistently

## Self-review prompt

Imagine being paged at 2am. Read your playbook. Could you respond confidently? If you'd still need to ask "where do I find X?" or "how do I do Y?", sharpen.

Also: tabletop the playbook with a colleague who didn't write it. Have them simulate following step-by-step. Where they get stuck = where you must add detail.

After tabletop, address ALL friction points before saving as v1. Iterate.
