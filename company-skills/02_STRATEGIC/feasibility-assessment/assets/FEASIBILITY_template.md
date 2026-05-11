# {{PROJECT_NAME}} — Feasibility Assessment

> **Purpose:** Business case for proposed technical work. Translates Phase 1 findings into stakeholder decision.
> **Audience:** Executive / budget owner / board / skeptic.
> **Last updated:** {{YYYY-MM-DD}}
> **Generated using:** `feasibility-assessment` skill v1
> **Author:** {{NAME}}

---

## 1. Executive Summary

**The question:** {{ONE_SENTENCE_QUESTION — e.g., "Should we invest in modernizing the data layer? At what scope?"}}

**Recommendation:** {{1-2 SENTENCES — which scenario the analysis supports, top reason}}

**At a glance:**

| Scenario | Cost | Year-1 benefit | Payback | Risk |
|----------|------|----------------|---------|------|
| **Full** | {{$X}} | {{$Y}} | {{months}} | {{Med/High}} |
| **Partial** *(recommended)* | {{$X}} | {{$Y}} | {{months}} | {{Low/Med}} |
| **Minimum** | {{$X}} | {{$Y}} | {{months}} | {{High — doesn't close compliance gap}} |
| **Do nothing** | $0 upfront | -{{$Y}} per year (debt cost) | n/a | {{Critical}} |

(The "Do nothing" row matters — it's the baseline.)

---

## 2. Background

**Current state (1 paragraph):** {{Where the system is today; what's broken or risky; based on `TECH_DEBT_AUDIT.md`}}

**Triggering events:**
- {{e.g., "Customer X requested SOC2 certification by Q4"}}
- {{e.g., "DB migration EOL announced; current Postgres 12 unsupported by 2026"}}
- {{e.g., "Sustained customer-facing incidents (4 in last 90 days)"}}

**Why now (vs. defer):**
- {{REASON}}
- {{REASON}}

---

## 3. Scenario Mode

See Section 9 for chosen mode (A / B / C). Default Mode A: 3 scenarios — Full / Partial / Minimum.

---

## 4. Cost of Inaction (Baseline)

If we do nothing, what does the next 12 months cost?

| Cost type | Amount/year | Notes |
|-----------|-------------|-------|
| Direct: customer churn from instability | {{$X}} | {{Based on N current at-risk accounts × ARR × churn probability}} |
| Direct: incident response time | {{$X}} | {{N incidents/yr × avg duration × engineering cost}} |
| Opportunity: feature delays from debt friction | {{$X}} | {{Estimated from velocity reduction}} |
| Risk: probability-weighted incidents | {{$X}} | {{e.g., 15% breach probability × $500K cost}} |
| Compliance: sales blocked at $X ARR until cert | {{$X}} | {{ARR not closeable without SOC2}} |
| Cost growth trajectory | {{+X%/year}} | {{e.g., infra cost grows 30%/year on current arch}} |
| **Estimated total cost of inaction (Year 1)** | **{{$X}}** | |

This is what "no" costs.

---

## 5. Scenarios

### 5.1 Scenario: FULL

**Scope:**
- {{All Phase 0 WPs}} — {{description}}
- {{Phase 1 WPs}} — {{description}}
- {{Phase 2 WPs}} — {{description}}
- {{Phase 3 WPs}} — {{description}}
- {{Phase 4 WPs}} — {{description}}

**Out of scope:** {{LIST}}

**Cost:**

| Cost type | Amount | Notes |
|-----------|--------|-------|
| Engineering | {{N hours × $X/hr = $Y}} | {{N senior devs × T weeks × $X loaded}} |
| Infrastructure delta | {{$X/mo × T mo}} | {{New services / upgrades}} |
| External (audit/consult) | {{$X}} | {{e.g., SOC2 audit fee, vendor consult}} |
| Opportunity (deferred features) | {{$X}} | {{Roughly Y feature-weeks delayed × revenue per feature}} |
| **Total** | **{{$X}}** | |

**Benefit:**

| Benefit type | Year 1 | Year 3 | Notes |
|--------------|--------|--------|-------|
| Direct savings (infra cost reduction) | {{$X}} | {{$X}} | {{New arch is N% more efficient}} |
| Risk reduction (incidents avoided) | {{$X}} | {{$X}} | {{Probability × cost reduced}} |
| Revenue unlocked (features, sales) | {{$X}} | {{$X}} | {{Compliance unlocks $Y ARR; new features unlock $Z}} |
| Productivity (faster velocity post-fix) | {{$X}} | {{$X}} | {{Faster feature delivery}} |
| **Total** | **{{$Y1}}** | **{{$Y3}}** | |

**Time-to-value:** First measurable benefit at {{N weeks}}; full benefit at {{N months}}.

**Payback period:** {{N months}}.

**ROI:**
- Year 1: {{(Benefit_Y1 - Cost) / Cost × 100%}}
- Year 3: {{((Benefit_Y3 sum) - Cost) / Cost × 100%}}

**Top risks:**
- {{RISK}}: {{MITIGATION}}
- {{RISK}}: {{MITIGATION}}

---

### 5.2 Scenario: PARTIAL

(Same structure as Full)

**Scope:** {{Subset — typically Phase 0+1, or P0+P1 findings only}}

**What you're NOT getting (vs. Full):**
- {{IMPACT_OF_OMISSION}}
- {{IMPACT_OF_OMISSION}}

(Repeat cost / benefit / payback / risks subsections)

---

### 5.3 Scenario: MINIMUM

(Same structure as Full)

**Scope:** {{Smallest viable — typically Phase 0 only / P0 findings only}}

**What you're NOT getting (vs. Partial or Full):**
- {{IMPACT_OF_OMISSION}}
- {{Compliance gap remains}}
- {{Cost-growth trajectory mostly unchanged}}

(Repeat cost / benefit / payback / risks subsections)

---

## 6. Side-by-side Comparison

| Dimension | Full | Partial | Minimum | Do nothing |
|-----------|------|---------|---------|------------|
| One-time cost | {{$X}} | {{$Y}} | {{$Z}} | $0 |
| Year-1 benefit | {{$X}} | {{$Y}} | {{$Z}} | -{{$baseline}} |
| Year-3 benefit (cumulative) | {{$X}} | {{$Y}} | {{$Z}} | -{{$Y3 baseline}} |
| Payback | {{months}} | {{months}} | {{months}} | n/a |
| Year-1 ROI | {{%}} | {{%}} | {{%}} | n/a |
| Year-3 ROI | {{%}} | {{%}} | {{%}} | n/a |
| Risk closed | {{N P0/P1 findings}} | {{N}} | {{N}} | 0 |
| Time-to-completion | {{weeks}} | {{weeks}} | {{weeks}} | n/a |
| Stakeholder impact | {{Engineering, Sales, Legal}} | {{...}} | {{...}} | {{Sales blocked, customer churn}} |
| Reversibility if wrong | {{Hard}} | {{Medium}} | {{Easy}} | n/a |

---

## 7. Assumptions

Each scenario depends on these holding true. If any falsify, re-evaluate.

| ID | Assumption | Confidence | What changes if violated |
|----|-----------|------------|---------------------------|
| ASM-01 | {{e.g., 2x user growth in Year 1}} | {{H/M/L}} | {{Cost projections shift; benefits proportional}} |
| ASM-02 | {{e.g., Vendor pricing stable through 2027}} | {{H/M/L}} | {{If vendor raises price 30%, partial scenario underestimates by $X}} |
| ASM-03 | {{e.g., Current team capacity (N senior, M junior) maintained}} | {{H/M/L}} | {{Each lost senior adds N weeks to timeline}} |
| ASM-04 | {{e.g., No major regulatory change}} | {{H/M/L}} | {{New regulation could force minimum → partial}} |

---

## 8. Stakeholder Impact (per scenario)

| Stakeholder | Full | Partial | Minimum | Do nothing |
|-------------|------|---------|---------|------------|
| Engineering | Major work; capability building | Significant work | Targeted work | Compounding debt |
| Sales | Unblocks $X ARR | Unblocks partial $X ARR | No unblock | Customers churn |
| Customers | Improved reliability | Improved partial | Status quo | Sustained pain |
| Legal/Compliance | Full compliance | Partial — gaps remain | Critical only | Compliance risk |
| Finance | $X investment, $Y return | $X investment, $Y return | $X investment, $Y return | -$X cost trajectory |
| Customer Success | Reduced ticket volume | Some reduction | Status quo | Volume grows |

---

## 9. Recommendation

**Recommended scenario:** {{Full / Partial / Minimum}}

**Top reasons:**
1. {{REASON_GROUNDED_IN_ANALYSIS}}
2. {{REASON}}
3. {{REASON}}

**What would change the recommendation:**
- If {{ASSUMPTION_X}} fails → switch to {{ALTERNATIVE_SCENARIO}}
- If budget < {{$X}} → only Minimum is feasible; document deferred risks
- If compliance deadline shifts → may force Partial or Full earlier

**Decisions needed from {{STAKEHOLDER}} by {{DATE}}:**
- [ ] Choose scenario (or modified blend)
- [ ] Approve budget
- [ ] Approve timeline
- [ ] Approve out-of-scope items

---

## 10. Notes & Caveats

- **Scenario mode:** {{A — Standard 3-scenario / B — Honor company template / C — User-defined}}
- **Mode rationale:** {{WHY}}
- **Inputs read:** TECH_DEBT_AUDIT ✅/❌, DATA_ARCHITECTURE ✅/❌, CODEBASE_MAP ✅/❌, BUSINESS_CONTEXT ✅/❌
- **Cost basis:** Loaded engineering cost = {{$X}}/hr (industry-typical $150-250/hr); infrastructure cost = current cloud spend × projected delta
- **Confidence:** {{HIGH/MEDIUM/LOW}}
- **Time spent on assessment:** {{HOURS}}

---

## 11. Open Questions

| ID | Question | Suggested next step |
|----|----------|---------------------|
| OQ-1 | {{e.g., What's the actual incident cost? Need 12-month review}} | {{Pull Sentry + on-call data}} |
| OQ-2 | {{e.g., Sales pipeline impact — how much ARR is gated on compliance?}} | {{Sales conversation}} |

---

*Numbers in this assessment are estimates with explicit confidence levels. Refine before any irreversible commitment.*
