# Phase 4 Orchestrator — Runbook

## Worked example 1 — Mode A Setup at go-live

**Setup:** Project Pegasus, all 18 WPs done, deploy in 1 week.

**Run:**

```
Operator: "Run phase-4-maintenance-orchestrator Mode A Setup.
TECH_SOLUTION_DESIGN at docs/02_STRATEGIC/.
On-call: 4 engineers in rotation.
Go-live: 2026-09-15."
```

**Pipeline:**

| Step | Action | Duration |
|------|--------|----------|
| Pre-flight | Verified Phase 3 done, on-call defined, monitoring up | 30 min |
| Step 1 | Inventoried failure modes from architecture: 22 failure modes (DB, auth, payment, queue, deploy, ...) | 1 hr |
| Step 2 | Ran incident-response-playbook 22 times (mostly Tier 2 + 1 Tier 3 for complex deploy rollback) | 8 hr AI work + 4 hr operator review |
| Step 3 | Scheduled: monthly doc-sync 1st of month, quarterly consistency Q-start, yearly review on go-live anniversary | 30 min |
| Step 4 | Tabletop: 3 P0 scenarios with on-call team (1.5 hr meeting) | 1.5 hr |
| Step 5 | Setup report generated | 15 min |

**Total:** ~16 hr work spread over 1 week pre-launch.

**Outputs:**
- 22 runbooks in docs/04_MAINTENANCE/runbooks/
- Calendar entries for monthly/quarterly/yearly cycles
- Setup report in docs/04_MAINTENANCE/_setup_report_2026-09-08.md
- On-call team trained on top 3 P0 scenarios

## Worked example 2 — Mode B Incident response

**Setup:** Pegasus, 3 months post-launch. P0 alert: "Postgres primary unreachable" at 2:14 AM.

**Pipeline (real-time):**

| Time | Action |
|------|--------|
| T+0 | Alert fires; on-call paged |
| T+3min | On-call acks, opens runbook INCIDENT_postgres_primary_down.md |
| T+5min | Runbook Step 1 (Detection): confirmed via secondary check |
| T+8min | Runbook Step 2 (Containment): traffic cut to read replicas (per runbook command) |
| T+15min | Runbook Step 3 (Eradication): primary failover initiated |
| T+22min | Failover complete; primary restored from replica |
| T+25min | Runbook Step 4 (Recovery): traffic restored, verify normal ops |
| T+45min | Incident closed; SLA RTO 15min — missed by 30 min (tracked) |

**Post-incident (T+24 to T+48 hr):**

| Step | Action |
|------|--------|
| Run incident-response-playbook in post-incident mode | Generates timeline + lessons |
| Lesson: "Replica failover took 22 min vs runbook estimate 15 min" | Update runbook with realistic timing |
| Lesson: "Step 2 traffic cut command had typo, ran twice" | Fix runbook command |
| Lesson: "Alerting only fired 3 min after primary down" | Open monitoring ticket |

**Outputs:**
- Updated runbook (more accurate timing, fixed command)
- 1 new monitoring ticket
- Incident report to ops team channel

## Worked example 3 — Mode C Monthly cycle

**Setup:** Pegasus, 8 months post-launch. 1st of October.

**Run:**

```
Operator: "Run Mode C Monthly cycle."
```

**Pipeline:**

| Step | Action | Duration |
|------|--------|----------|
| Step 1 | documentation-sync full scope | 1.5 hr |
| Step 2 | Operator reviews report | 30 min |
| Step 3 | Findings: 3 Medium drifts (API endpoints in doc vs router) | 15 min triage |
| Step 4 | Created 3 tickets, assigned to dev team | 10 min |
| Step 5 | document-index-master refresh INDEX.md | 15 min |
| Step 6 | PROGRESS.md updated | 5 min |

**Total:** ~3 hr.

**Trend:** Down from 7 findings 3 months ago (October has fewer drifts because team incorporating doc updates per PR).

## Worked example 4 — Mode D Audit prep

**Setup:** SOC2 audit in 3 weeks. Pegasus, 11 months post-launch.

**Run:**

```
Operator: "Run Mode D Audit prep. SOC2. Auditor: Acme CPA. Scope: all Phase 0-4 docs + runbooks. Deadline: 2026-08-15."
```

**Pipeline:**

| Step | Action | Duration |
|------|--------|----------|
| Pre-flight | Confirmed scope + deadline + framework | 30 min |
| Step 1 | documentation-sync full | 1.5 hr |
| Step 2 | document-consistency-review full | 2 hr |
| Step 3 | Critical: 0 (good); High: 4 → 3 fixed in 1 week, 1 accepted with rationale | 1 week elapsed |
| Step 4 | Spot-check 3 random runbooks: 2 OK, 1 needed tweaking (auth changed) | 1 hr |
| Step 5 | Generated audit binder (table of contents + Phase 0-4 docs + reports + samples) | 2 hr |
| Step 6 | Git tag `audit-soc2-2026-08-13` | 5 min |
| Step 7 | Delivered binder to auditor 2 days before deadline | — |

**Total:** ~7 hr work + 1 week elapsed.

**Audit outcome:** Pass with 0 findings. Cited "exemplary documentation discipline" — direct credit to Phase 4 maintenance.

---

## Troubleshooting

### T1 — Mode A: Operator overwhelmed by 30+ failure modes

**Cause:** Inventory thorough but team capacity to write 30 runbooks low.

**Resolution:**
- Prioritize: P0 + P1 only at go-live (typically 8-12 runbooks)
- P2/P3 within first 30 days post-launch
- Document the gap in setup report

### T2 — Mode B Incident: runbook missing for this failure mode

**Cause:** Either gap in setup OR new failure mode (not anticipated).

**Resolution:**
- During incident: improvise based on similar runbook + escalate
- Post-incident: create new runbook (highest priority)
- Update inventory: failure mode count grew from N to N+1

### T3 — Mode C Monthly cycle skipped (operator forgot)

**Cause:** Calendar missed; operator overloaded.

**Resolution:**
- Skip 1 month → catch up next month (no big deal)
- Skip 2+ months → alarm: discipline broken; escalate to tech lead
- Long-term: automate via CI/cron; remove operator memory dependency

### T4 — Mode B Feature: PM wants to skip feature-extension-planning

**Cause:** "Just code it" mentality.

**Resolution:**
- Push back: even 30-min mini-spec saves rework
- For trivial features (<1 day, no schema/API change): allow doc-after with operator log entry
- For non-trivial: require feature-extension-planning before code

### T5 — Mode D Audit prep finds Critical findings 1 day before deadline

**Cause:** Mode C discipline weak; cramming pattern.

**Resolution:**
- Prioritize Critical fixes by audit framework requirement
- Document remaining as "planned remediation post-audit"
- Negotiate with auditor for 1-2 week extension if feasible
- Long-term: stop Mode D cramming; run Mode C reliably

### T6 — Runbook execution failed during real incident

**Cause:** Runbook outdated (env changed since written).

**Resolution:**
- During incident: improvise, log every deviation
- Post-incident: update runbook completely (not patch)
- Schedule quarterly runbook review (not just yearly)

### T7 — Multiple incidents in quick succession

**Cause:** Underlying systemic issue, not isolated incidents.

**Resolution:**
- Don't run individual post-incident reviews — run pattern analysis
- Identify root systemic issue
- May trigger Phase 2 partial re-loop (architecture change)

---

## Cost projections

| Mode | Cost (one-time / per-event) | Time |
|------|------------------------------|------|
| Mode A Setup | $30-100 (depends on # runbooks) | 16-30 hr work, 1-2 weeks elapsed |
| Mode B per feature | $5-20 | 1-3 hr |
| Mode B per incident | $0-5 (mostly during incident; AI used in post-review) | Variable |
| Mode C monthly | $5-15 | 2-4 hr |
| Mode C quarterly | $10-30 | 4-8 hr |
| Mode C yearly | $30-100 | 8-20 hr |
| Mode D audit prep | $15-50 + remediation cost | 4-8 hr direct + remediation |

Per year for medium project: ~$300-800 AI spend on Phase 4 (cheap relative to value of catching drift early).

---

## When orchestrator is NOT the right tool

- **Active P0 incident:** No time to invoke orchestrator; on-call follows runbook directly
- **Trivial typo fix:** Just edit doc + commit
- **Single skill ad-hoc run:** Just run the skill directly
- **Pre-production work:** Wrong phase; use Phase 0/1/2/3
