# Phase 2 Orchestrator — Runbook

## Worked example 1 — Standard run, single iteration

**Setup:** Project Pegasus rewrite. Phase 0 + 1 complete. CEO approved budget $1.4M / 14 months.

**Pipeline:**

| Day | Event | Duration |
|-----|-------|----------|
| 1 | Operator runs orchestrator pre-flight + Step 1 | 4 hr (3 hr AI + 1 hr operator) |
| 1 | FEASIBILITY_ASSESSMENT.md ready | — |
| 2 | Operator presents to CEO+CFO+CTO | 1 hr meeting |
| 2 | Discussion: Partial scenario chosen ($900K, 14 months) | — |
| 2 | Operator captures approval in email + saves to _decisions/G1_approval_2026-04-22.md | 15 min |
| 3 | Resume orchestrator, Step 2 tech-solution-design | 4 hr |
| 3 | TECH_SOLUTION_DESIGN.md ready with 7 ADRs | — |
| 4 | Tech Lead reviews ADRs, requests modification on ADR-005 (DB choice) | 30 min review + 1 hr update |
| 4 | Updated ADRs approved | G2 artifact saved |
| 5 | Resume orchestrator, Step 3 implementation-planning | 3 hr |
| 5 | MASTER_PLAN.md + 5 PHASE_*.md files generated | — |
| 5 | Operator final review, archive prior _phase_report | 30 min |

**Total:** 5 days elapsed (3 days work + 2 days waiting). 12 hr AI + 4 hr operator + 1.5 hr stakeholder + 1.5 hr tech lead.

**Outputs:**
- 4 scenarios analyzed, Partial chosen
- 7 ADRs (DB, hosting, queue, observability, auth, deployment, integration pattern)
- 18 WPs across 4 implementation phases
- Critical path: WP-1.B (data migration) → WP-2.A (driver mobile MVP)

## Worked example 2 — Stakeholder rejects all scenarios

**Setup:** Project Atrium feasibility — CEO finds all 3 scenarios over budget.

**Pipeline:**

| Day | Event |
|-----|-------|
| 1 | Run Step 1, FEASIBILITY ready |
| 2 | Stakeholder meeting: rejects all 3 ("too expensive across the board") |
| 2 | Operator captures: "New constraint = budget cap $250K instead of $480K" |
| 2 | Update CONTEXT_PACK Section 7.3 |
| 2 | RE-RUN Step 1 with new constraint |
| 3 | New FEASIBILITY ready: scenarios shifted (Full now $250K, Partial $180K, Minimum $100K) |
| 3 | CEO approves new Partial |
| 4-7 | Continue Step 2, G2, Step 3 normally |

**Lesson:** Stakeholder rejection = orchestrator loops Step 1 with new inputs. NOT skip-ahead.

## Worked example 3 — Tech Lead rejects ADR

**Setup:** Project Helix Step 2. Tech Lead says ADR-003 (event-driven vs. request-response) is wrong.

**Pipeline:**

| Step | Action |
|------|--------|
| Step 2 complete | TECH_SOLUTION_DESIGN with 6 ADRs |
| G2 review | Tech Lead approves 5/6 ADRs; rejects ADR-003 (architecture-altering) |
| Operator decision | Re-run Step 2 (because architecture-altering); not just ADR patch |
| Step 2 re-run | New ADR-003 + downstream ADRs adjusted (4-6 still valid) |
| G2 re-review | All approved |
| Continue | Step 3 |

**Cost:** Adds ~3-4 hr AI work + 1-2 days elapsed for re-loop.

---

## Troubleshooting

### T1 — Operator wants to skip G1 because "stakeholder is busy"

**Resolution:** REFUSE. Without stakeholder approval, Step 2 has no scope target. Better to wait 1 week than build wrong thing.

If genuinely urgent: operator escalates to alternative approver (e.g., CTO substitutes for unavailable CEO) — but that substitution itself is documented.

### T2 — Stakeholder gives verbal approval but won't put in writing

**Resolution:** Operator drafts approval note, sends to stakeholder for confirmation:
```
"Subject: Confirming Project [X] Phase 2 approval
Per our 2026-04-22 meeting, you approved scenario [Partial], $900K, 14 months.
Replying 'confirmed' to this email is sufficient.
This will be saved as G1 approval artifact."
```

If stakeholder still won't reply → escalate. Don't proceed.

### T3 — FEASIBILITY shows none of the scenarios meet budget

**Cause:** Scope too large for budget cap.

**Resolution options:**
1. Re-run feasibility with "Minimum-minus" scenario (cut more scope)
2. Re-run after stakeholder relaxes budget cap
3. Decline project (sometimes the right answer)

Don't fudge the numbers.

### T4 — TECH_SOLUTION_DESIGN gets too many "candidates" (e.g., 8 DB options)

**Cause:** AI didn't filter by constraints.

**Resolution:**
- Re-run Step 2 with explicit prompt: "Honor CONTEXT_PACK 7.2 (vendor lock = AWS) → only AWS-native DB options. Max 3 candidates per decision."

### T5 — MASTER_PLAN timeline exceeds approved scenario timeline

**Resolution:**
- Re-run Step 3 with explicit timeline ceiling
- If still impossible, acknowledge timeline gap → loop back to G1 (re-negotiate with stakeholder)
- Do NOT silently approve the longer timeline

### T6 — Multiple approvers contradict (e.g., CEO approves, CFO objects)

**Cause:** Stakeholder map unclear in CONTEXT_PACK.

**Resolution:**
- Operator escalates: "Approval requires both CEO and CFO. Please align."
- Pause orchestrator until conflict resolved
- Update CONTEXT_PACK Section 8 contradictions

### T7 — Re-running Phase 2 6 months later with new scope

**Resolution:**
- Treat as new Phase 2 run
- Archive prior _phase_report
- Pre-flight check: are Phase 0/1 still current? If stale, refresh first
- Run full pipeline again with new approvals (G1 + G2 from current decision-makers)

---

## Cost projections

Medium project:

| Pipeline | AI work | Human time | Elapsed |
|----------|---------|------------|---------|
| First run, 1 iteration | 10-12 hr | 4 hr operator + 2 hr stakeholder + 2 hr tech lead | 1 week |
| First run, with G1 re-loop | 14-18 hr | 6 hr operator + 4 hr stakeholder | 2 weeks |
| First run, with G2 re-loop | 14-16 hr | 5 hr operator + 4 hr tech lead | 1.5 weeks |
| Refresh (after Phase 0 changed) | 6-8 hr | 2-3 hr | 3-5 days |

Phase 2 is the slowest phase due to gates — that's a feature.

---

## Why this orchestrator has no Express mode

Other orchestrators have Mode B Express that chains through with minimal pauses. Phase 2 does NOT.

Reason: Phase 2 outputs commit budget + timeline + architecture. Wrong commitment = months of rework. The 1-week elapsed time for proper gates is cheap insurance vs. months of rework.

If operator pressure says "we need this faster" — push back. The right response to schedule pressure is descope, not skip approval gates.

---

## When orchestrator is NOT the right tool

- **Just-feasibility** (deciding whether to even start): run `feasibility-assessment` standalone, no commitment needed yet
- **Just-design** (architecture exploration without decision): run `tech-solution-design` standalone
- **Just-planning** (replanning approved work): run `implementation-planning` standalone
- **Multi-project portfolio planning:** different tool, not project-level
