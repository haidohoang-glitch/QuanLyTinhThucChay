# Phase 3 Orchestrator — Runbook

## Worked example 1 — Sub-pipeline A setup

**Setup:** Project Pegasus, Phase 2 done. 18 WPs across 4 implementation phases. Budget $1.4M includes ~$30K AI spend.

**Run:**

```
Operator: "Run phase-3-execution-orchestrator Sub-pipeline A.
Project complexity: medium (~80K LOC target by end).
AI budget: $30K total Phase 3.
Mode A Supervised."
```

**Pipeline:**

| Step | Skill | Duration | Operator action |
|------|-------|----------|------------------|
| 0 | Pre-flight | 5 min | Confirmed Phase 2 done, budget OK |
| 1 | ai-operator-protocol | 1 hr | Reviewed + customized 7 rules (added rule about Stripe API keys) |
| 2 | multi-tier-ai-routing | 1.5 hr | Reviewed tier policy; adjusted: more T2 less T3 (project not super-complex) |
| 3 | Phase report | 5 min | Sub-A complete |

**Total:** ~3 hr.

**Outputs:**
- AI_OPERATOR_GUIDE.md (project-specific)
- AI_AGENT_TASK_DISTRIBUTION.md (with $30K cost projection)
- Phase 3 ready for WP loop

## Worked example 2 — Sub-pipeline B for WP-0.E

**Setup:** First WP of Project Pegasus: "Error Boundaries setup". Operator running first time, supervised tightly.

**Run:**

```
Operator: "Run phase-3-execution-orchestrator Sub-pipeline B for WP-0.E.
Mode A Supervised."
```

**Pipeline:**

| Step | Action | Duration |
|------|--------|----------|
| B1 | Pre-flight: dependencies (WP-0.A scaffolding) done? Yes | 2 min |
| B2 | work-package-decomposer → WP-0.E_tasks.md (15 tasks) | 30 min |
| Operator review | Reviewed task list; approved (no tier changes) | 10 min |
| B4 | Dispatch tasks per dependency order: T1×9 (boilerplate), T2×5 (logic), T3×1 (architectural choice) | 2 hr executor work |
| B5 | Independent reviewer session; ran all verify commands; flagged 1 issue (test missing for edge case) | 30 min |
| Operator decision | Operator approved with addendum task to add test (ran T2 task ~15 min) | 15 min + 15 min |
| B5 (re-run) | Reviewer re-verified; approved | 10 min |
| B6 | Operator committed with convention message | 10 min |
| B7 | Updated PROGRESS.md WP-0.E row | 2 min |

**Total:** ~4 hr (mostly executor work).

**Cost:**
- Decomposer (T3): ~$0.50
- Executor T1 tasks ×9: ~$0.45
- Executor T2 tasks ×6 (incl addendum): ~$0.90
- Executor T3 task ×1: ~$0.30
- Reviewer (T2): ~$0.50
- **Total: ~$2.65** (well within $30K budget)

vs all-Tier-3 baseline estimate: ~$22 → ~88% saving as projected.

## Worked example 3 — Mode C Auto-WP after confidence built

**Setup:** Project Pegasus completed 6 WPs supervised. Operator confident in policy. Switching to Auto-WP for low-risk Tier 1 WPs.

**Run:**

```
Operator: "Run Sub-pipeline B Mode C Auto-WP for WP-1.A through WP-1.D.
These are scaffolding WPs (mostly Tier 1).
Auto-dispatch authorized; reviewer must still pass.
Operator hard-stop: review every commit before push."
```

**Pipeline (per WP, abbreviated):**

| WP | Decomposer | Executor | Reviewer | Operator commit | Total |
|----|-------------|----------|----------|------------------|-------|
| WP-1.A | 15 min auto | 1 hr auto | 20 min auto | 10 min review/commit | 1.75 hr |
| WP-1.B | 15 min auto | 1.5 hr auto | 25 min auto | 10 min review/commit | 2.25 hr |
| WP-1.C | 15 min auto | 1 hr auto | 20 min auto | (BLOCKED — reviewer flagged regression) | — |
| WP-1.C remediation | manual | manual | — | 1 hr operator + AI fix | 1 hr |
| WP-1.C re-run reviewer | 20 min | — | — | 10 min commit | 30 min |
| WP-1.D | 15 min auto | 45 min auto | 20 min auto | 10 min review/commit | 1.5 hr |

**Total:** ~7 hr across 4 WPs (2 days operator part-time supervision).

**Lesson:** Mode C Auto-WP works for routine WPs but reviewer-flag = stop everything for that WP. Don't override.

---

## Troubleshooting

### T1 — Decomposer produces too few tasks (e.g., 3 for a WP that should be 15)

**Cause:** WP under-specified or AI didn't decompose enough.

**Resolution:**
- Re-run decomposer with explicit guidance: "Target 10-20 atomic tasks per WP"
- If WP genuinely small, merge with adjacent WP (operator decision)
- If still underdecomposed, manually split

### T2 — Decomposer assigns mostly Tier 3

**Cause:** WP perceived as complex; or tier policy not loaded.

**Resolution:**
- Verify decomposer loaded AI_AGENT_TASK_DISTRIBUTION.md
- Re-run with constraint: "Per routing policy, Tier 1 should be 60-70% of tasks"
- If WP is genuinely complex, may justify higher T3 — but flag in operator review

### T3 — AI executor gets stuck on a Tier 1 task

**Cause:** Task description ambiguous OR tier mismatched (should be Tier 2).

**Resolution:**
- Per AI_OPERATOR_GUIDE escalation rules: retry once, then escalate
- Operator inspects: re-decompose with better task description, or bump tier
- Update decomposer prompt history for future runs (skill examples.md)

### T4 — Reviewer flags issue but operator disagrees

**Cause:** Reviewer over-cautious or operator under-cautious.

**Resolution:**
- Operator decision is final BUT must document reasoning in commit message
- If pattern (operator always overrides reviewer same flag), update reviewer system prompt
- Don't silently ignore reviewer — always document

### T5 — Phase 3 cost overrun (actual >120% projection)

**Cause:** Tier mix shifted up (more T3) due to actual complexity higher than estimated.

**Resolution:**
- Stop, don't continue WPs
- Re-calibrate tier policy with actual data
- Update AI_AGENT_TASK_DISTRIBUTION.md
- Re-decompose remaining WPs with new policy
- Update Phase 2 cost projection (may require feasibility refresh if material)

### T6 — Vendor outage (e.g., Anthropic API down)

**Cause:** Single-vendor dependency.

**Resolution:**
- Per AI_AGENT_TASK_DISTRIBUTION fallback policy: switch to alternate vendor (e.g., OpenAI)
- Some quality drop expected; flag affected commits
- When primary back: optionally re-run reviewer on flagged commits

### T7 — WP took 2x estimated effort

**Cause:** WP underdecomposed OR estimation poor OR scope crept.

**Resolution:**
- Don't continue without diagnosis
- Operator + AI review what happened
- Update MASTER_PLAN if pattern (estimation systematically off)
- Update decomposer's effort estimation logic

---

## Cost projections

For 18 WPs medium project:

| Mode | Total cost | Operator hr | AI work hr | Elapsed weeks |
|------|------------|-------------|------------|---------------|
| Sub-A only | $0 (skills only) | 3 hr | 2.5 hr | 1 day |
| Sub-B all-supervised | ~$25-40 | ~30 hr | ~50 hr | 6-8 weeks |
| Sub-B mixed (3 supervised then auto-WP) | ~$25-35 | ~20 hr | ~40 hr | 4-6 weeks |

The biggest variable: how often reviewer flags issues + how often operator must rework.

---

## When orchestrator is NOT the right tool

- **Single bug fix:** No need for decomposer; just edit + commit
- **Spike/PoC code:** Skills assume production-quality; spike may not need rigor
- **Pure refactor (no functional change):** Decomposer overhead may exceed value; manual + reviewer is fine
- **Emergency hotfix:** Skip orchestrator entirely; fix + post-incident review
