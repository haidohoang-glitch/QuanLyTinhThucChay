# Phase 1 Orchestrator — Runbook

## Worked example 1 — Mid-size legacy, Mode A Sequential

**Setup:** "Project Mosaic" learning platform. ~80K lines TS/React, 4 years old, no Discovery docs.

**Run:**

```
Operator: "Run phase-1-discovery-orchestrator Mode A.
Codebase at src/. Inputs/CONTEXT_PACK at docs/00_REQUIREMENTS/.
Output to docs/01_DISCOVERY/."
```

**Pipeline:**

| Step | Skill | Duration | Pause |
|------|-------|----------|-------|
| 0 | Pre-flight | 5 min | Operator confirmed mode + plan |
| 1 | codebase-discovery | 2 hr | Operator reviewed coverage 78%, accepted |
| 2 | data-architecture-audit | 1.5 hr | Operator flagged 1 PII gap (analytics warehouse not audited) — accepted as known limitation |
| 3 | business-context-capture | 2.5 hr | Operator + PM joint review found 3 code-vs-CONTEXT_PACK mismatches → opened Phase 0 issues |
| 4 | tech-debt-audit | 3 hr | Operator forced re-calibration: AI initially marked 18 Critical → re-ran with severity discipline → final 7 Critical |
| 5 | Phase report | 5 min | — |

**Total:** ~9 hr AI + 2.5 hr operator review across 2 days.

**Outcome:** Audit-grade Phase 1. Phase 0 reverse-engineer started day 3.

## Worked example 2 — Time-pressured, Mode B Parallel

**Setup:** Acquisition due-diligence, 3 days max, "Project Aurora" e-commerce.

**Run:**

```
Operator: "Run phase-1-discovery-orchestrator Mode B Parallel.
Tight timeline. Skip CONTEXT_PACK (no stakeholder access during DD).
Accept lower coverage if needed."
```

**Pipeline:**

| Step | Status |
|------|--------|
| 0 | Pre-flight (no CONTEXT_PACK warned) — 3 min |
| 1 | codebase-discovery — 2 hr (coverage 65%, accepted under time pressure) |
| 2+3 | Parallel: data-architecture-audit + business-context-capture — 2.5 hr (longest) |
| 4 | tech-debt-audit — 2 hr (express, top-N findings only) |
| 5 | Phase report (with explicit caveats about coverage) |

**Total:** ~7 hr AI + 1 hr operator review in 1 day.

**Caveats logged:** Coverage 65% vs target 70%. No stakeholder voice. Tech-debt findings top-N only. NOT audit-grade — internal DD only.

## Worked example 3 — Selective refresh

**Setup:** Project Helix added a new payment integration; need DATA_ARCHITECTURE refresh only.

**Run:**

```
Operator: "Mode D Selective. Run only data-architecture-audit.
Reason: new Stripe integration adds 3 tables, 1 webhook, PII for cards (tokenized).
Other Phase 1 docs unchanged."
```

**Pipeline:**

| Step | Action |
|------|--------|
| Pre-flight | Verify only data layer changed; confirm scope |
| Step 2 | Re-run data-architecture-audit, archive prior |
| Cross-check | Operator manually updates BUSINESS_CONTEXT references if needed (10 min) |

**Total:** ~1.5 hr.

---

## Troubleshooting

### T1 — "Coverage too low" after Step 1

**Cause:** Codebase very large or AI session limit hit.

**Resolution:**
- Split codebase: run codebase-discovery per top-level folder, then merge
- Or accept lower coverage with explicit caveat in CODEBASE_MAP

### T2 — Step 2 cannot access production DB

**Cause:** Common — DDB credentials not in dev environment.

**Resolution:**
- Use migration files + ORM models as proxy
- Mark report: "Schema based on migrations; runtime data not verified"
- Schedule follow-up data-architecture audit with prod read-only access

### T3 — Step 3 finds "no clear actors"

**Cause:** Codebase has authentication but no role/permission system.

**Resolution:**
- Document as "single-actor system" in BUSINESS_CONTEXT
- Flag as design observation (might be intentional, might be tech debt)

### T4 — Step 4 produces 30+ Critical findings

**Cause:** AI inflation.

**Resolution:**
- Re-run with explicit instruction: "Critical = causes outage OR blocks revenue OR fails audit. Max 10 for medium project."
- If still >10 after re-calibration, flag systemic issue (the project might genuinely be in bad shape)

### T5 — Code-vs-stakeholder mismatch surfaced — what to do?

**Cause:** Code does something CONTEXT_PACK doesn't mention (or vice versa).

**Resolution:**
- BUSINESS_CONTEXT Section 9 Open Questions — document the mismatch
- Phase 0 srs-reverse-engineer reads this and either:
  - Resolves with stakeholder
  - Documents as M10 Open Issue
- Don't pick a side in Phase 1

### T6 — Mode B parallel: Step 2 finishes 30 min before Step 3

**Cause:** data-architecture is faster than business-context.

**Resolution:**
- Operator reviews Step 2 output during Step 3 wait
- Don't auto-start Step 4 — Step 4 needs both done

### T7 — Step 4 cost-estimates wildly different from operator intuition

**Cause:** AI doesn't know team velocity / context.

**Resolution:**
- Operator overrides estimates with team-specific velocity data
- Update TECH_DEBT after operator review
- Note: cost estimates are baseline only — refine in Phase 2 feasibility

---

## Cost projections

Medium legacy (~80K LOC, 4 functional domains):

| Mode | AI work | Operator | Elapsed | Cost |
|------|---------|----------|---------|------|
| A Sequential | 9-10 hr | 2-3 hr | 2-3 days | ~$25-40 |
| B Parallel | 7-8 hr | 2-3 hr | 1-2 days | ~$22-35 |
| C Express | 5-7 hr | 1 hr | 1 day | ~$18-28 |
| D Selective | 1-3 hr | 30 min | <1 day | ~$5-10 |

---

## When orchestrator is NOT the right tool

- **Greenfield projects:** No code = nothing to discover
- **Microservice exploration:** If you only need 1 service mapped, run codebase-discovery alone
- **Post-incident root-cause analysis:** Out of scope; use incident-response-playbook
- **Architecture review (not Discovery):** That's Phase 2 tech-solution-design
