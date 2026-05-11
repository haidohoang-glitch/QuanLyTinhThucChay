# Feasibility Assessment — Worked Example

Anonymized. Fictional project: **"Project Pegasus"** — a 6-year-old logistics tracking platform deciding between rewrite, refactor, or stabilization. Mode A.

## Context

**Imagined input:** "Pegasus has accumulated significant tech debt (per audit, 47 P0/P1 findings). Customers complaining about reliability. Investor wants the system future-proofed. We have 4 senior engineers. What should we do?"

**Question:** "How much of the modernization should we invest in?"

**Time budget for feasibility:** 12 hours over 1 week.

---

## Output excerpt

```markdown
# Project Pegasus — Feasibility Assessment

## 1. Executive Summary

**The question:** How much should we invest in modernizing Pegasus' platform — full rewrite, partial refactor, or critical-only stabilization?

**Recommendation:** **Partial scenario** (Phase 0+1 = 14 weeks, $480K). Reasons:
- Closes all P0 findings (security + active outages)
- Returns measurable reliability gains (target: 99.9% uptime, currently 99.4%)
- Year-1 ROI 180% via reduced churn + sales unlocks
- Defers 22 P2 items to next budget cycle (acceptable per audit)

**At a glance:**

| Scenario | Cost | Year-1 benefit | Payback | Risk |
|----------|------|----------------|---------|------|
| Full | $1.4M | $890K | 19mo | Med (team burnout, 28-week scope) |
| **Partial** *(recommended)* | **$480K** | **$870K** | **7mo** | Low |
| Minimum | $180K | $290K | 7mo | High — compliance gap remains |
| Do nothing | $0 | -$1.1M (debt cost) | n/a | Critical — customer churn projection |

## 2. Background

**Current state:** Pegasus is on Postgres 11 (EOL Q1 2026), Node 14 (unsupported), monolith with no test coverage on critical paths (auth: 8%, billing: 12%). 4 production incidents in last 90 days; SOC2 readiness audit found 47 gaps.

**Triggering events:**
- Customer X (top-3 ARR) requested SOC2 by Q4 — deadline binding
- Postgres 11 EOL Q1 2026 — forced upgrade
- Sustained customer escalations: support ticket volume +40% YoY

**Why now:**
- SOC2 deadline + Postgres EOL converge — addressing now batches mandatory work
- Team has bandwidth (just shipped Q1 features); next major feature pipeline starts Q3
- Hiring market tight — preserving current team's morale matters

## 4. Cost of Inaction (Baseline)

| Cost type | Year-1 amount | Notes |
|-----------|---------------|-------|
| Customer churn from instability | $720K | 3 mid-tier accounts at $240K ARR each, 80% churn probability per industry |
| Incident response time | $90K | 16 incidents/yr × 24h × 4 engineers × $200/hr |
| Opportunity (delayed features) | $200K | ~12 weeks of feature work blocked by debt friction |
| Risk: probability-weighted security incident | $75K | 15% probability × $500K cost basis |
| Compliance: blocked sales pipeline | $0 in Year 1 (long sales cycle) | $1.5M ARR pipeline gated on SOC2 (impacts Year 2-3) |
| Postgres 11 forced migration cost increase | +25% | Crisis migration costs more than planned |
| **Total cost of inaction (Year 1)** | **$1.085M** | Baseline |

If we do nothing for 12 months, we spend ~$1.1M in absorbed cost.

## 5. Scenarios

### 5.1 Scenario: FULL

**Scope:**
- Phase 0 (Pre-flight): 8 WPs — auth modernization, observability, dep upgrades
- Phase 1 (Quick wins): 5 WPs — pagination, caching, rate limiting
- Phase 2 (Dual-write): 8 WPs — new architecture standup, migration
- Phase 3 (Switch reads): 5 WPs — gradual rollout, performance tuning
- Phase 4 (Compliance): 6 WPs — MFA, GDPR, DR drill, decom legacy

**Out of scope:**
- Frontend SPA migration (separate project, separate team)
- Mobile app (different repo)
- Data warehouse rebuild (Year 2 initiative)

**Cost:**

| Cost type | Amount | Notes |
|-----------|--------|-------|
| Engineering | $1.16M | 4 sr devs × 28 weeks × 40 hrs × $200/hr loaded |
| Infrastructure delta | $48K | New region $2K/mo × 24 mo ramp; new monitoring $500/mo |
| External (audit + consult) | $50K | SOC2 audit $35K + DBA consultant $15K |
| Opportunity (deferred features) | $140K | 28 weeks × 1 senior × $5K/wk = features worth ~$140K shifted to Year 2 |
| **Total** | **$1.4M** | |

**Benefit:**

| Benefit type | Year 1 | Year 3 cumulative | Notes |
|--------------|--------|--------------------|-------|
| Direct savings (infra cost) | $30K | $180K | New arch ~25% more efficient |
| Risk reduction (incidents) | $80K | $240K | 16/yr → 4/yr |
| Revenue unlocked (sales pipeline) | $300K | $2.1M | $1.5M pipeline closes (12-mo cycle) |
| Productivity (feature velocity) | $140K | $700K | ~25% faster post-modernization |
| Customer retention | $340K | $1.2M | Reduced churn (3 → <1 mid-tier accounts/yr) |
| **Total** | **$890K** | **$4.42M** | |

**Time-to-value:** First measurable benefit at week 6 (Phase 0 complete); compliance unlock at week 22; full benefit at week 32.

**Payback period:** 19 months
**Year-1 ROI:** -36% (high upfront, returns lag)
**Year-3 ROI:** 216%

**Top risks:**
- Team burnout: 28-week dedicated push; mitigation: rotate WPs, take 1-week reset between phases
- Production parity issues during dual-write: mitigation: feature flag + 5%→100% rollout with rollback plan
- Customer expectations during 28-week period: mitigation: monthly status updates, no major UI changes

---

### 5.2 Scenario: PARTIAL (recommended)

**Scope:**
- Phase 0 (Pre-flight): 8 WPs (full)
- Phase 1 (Quick wins): 5 WPs (full)
- Phase 2 (Dual-write): SKIP except WP-2.A (Postgres 11→16 upgrade — forced)
- Phase 3: SKIP
- Phase 4: 2 WPs (MFA, basic audit log) — minimum SOC2 coverage

**What you're NOT getting (vs. Full):**
- New service-oriented architecture (defers to Year 2)
- Gradual rollout infra (no need this scope)
- Full GDPR tooling (deferred until EU customers)
- DR drill (deferred to Year 2)

**Cost:**

| Cost type | Amount | Notes |
|-----------|--------|-------|
| Engineering | $400K | 4 sr × 14 wks × 40 × $200 (loaded) |
| Infrastructure | $12K | Postgres upgrade window only |
| External | $35K | SOC2 audit only |
| Opportunity | $33K | 14 weeks deferred |
| **Total** | **$480K** | |

**Benefit:**

| Benefit type | Year 1 | Year 3 cumulative |
|--------------|--------|--------------------|
| Direct savings | $18K | $90K |
| Risk reduction | $75K | $225K |
| Revenue unlocked | $300K | $1.6M (slower than Full) |
| Productivity | $90K | $400K |
| Customer retention | $340K | $1.0M |
| Critical security closure | $60K | $180K |
| **Total** | **$870K** | **$3.5M** |

**Time-to-value:** Week 6 first benefit; Week 14 SOC2 ready; full Year 1 benefit by week 16.

**Payback period:** 7 months
**Year-1 ROI:** 81%
**Year-3 ROI:** 629%

**Top risks:**
- Postgres 11 EOL forces upgrade in Phase 2; if upgrade reveals deeper issues, may slip 2-4 weeks
- "Defer to Year 2" items may keep being deferred (debt accumulation): mitigation: explicit Year 2 roadmap with these items
- SOC2 audit reveals additional gaps: budget $20K contingency for remediation

---

### 5.3 Scenario: MINIMUM

**Scope:**
- Phase 0: 4 WPs (P0 only — auth, dep upgrades, basic observability)
- Phase 1: SKIP
- Phase 2: WP-2.A (Postgres upgrade only)
- Phase 4: SKIP
- No SOC2 work

**What you're NOT getting:**
- Compliance posture (SOC2 cert deferred indefinitely → $1.5M sales pipeline blocked)
- Reliability improvements (incidents continue → churn continues)
- Velocity improvements
- Most of Year 2 cost-of-inaction also accumulates

**Cost:**

| Cost type | Amount | Notes |
|-----------|--------|-------|
| Engineering | $160K | 4 sr × 5 wks × 40 × $200 |
| Infrastructure | $4K | Postgres upgrade |
| External | $0 | (no audit) |
| Opportunity | $14K | 5 wks deferred |
| **Total** | **$180K** | |

**Benefit:**

| Benefit type | Year 1 | Year 3 cumulative |
|--------------|--------|--------------------|
| Direct savings | $5K | $20K |
| Risk reduction | $30K | $90K |
| Revenue unlocked | $0 (SOC2 blocked) | $0 (continues to block) |
| Productivity | $20K | $60K |
| Customer retention | $235K | $400K |
| **Total** | **$290K** | **$570K** |

**Time-to-value:** Week 4
**Payback period:** 7 months
**Year-1 ROI:** 61%
**Year-3 ROI:** 217%

**Top risks:**
- SOC2 deadline missed → Customer X cancels (-$240K ARR), other accounts at risk
- Compounding debt: at Year 2, costs higher than initial Full would have been
- Team morale: doing minimum often demotivating ("we know what to do but can't do it")

## 6. Side-by-side Comparison

| Dimension | Full | Partial | Minimum | Do nothing |
|-----------|------|---------|---------|------------|
| One-time cost | $1.4M | $480K | $180K | $0 |
| Year-1 benefit | $890K | $870K | $290K | -$1.085M |
| Year-3 cumulative benefit | $4.42M | $3.5M | $570K | -$3.4M |
| Payback | 19mo | 7mo | 7mo | n/a |
| Year-3 ROI | 216% | 629% | 217% | n/a |
| P0 findings closed | 47/47 | 22/47 (P0+top P1) | 8/47 (P0 only) | 0 |
| Time-to-completion | 28wk | 14wk | 5wk | n/a |
| SOC2 readiness | Yes | Yes (basic) | No | No |
| Stakeholder impact | Major (broad) | Significant (focused) | Limited | Negative |
| Reversibility if wrong | Hard | Medium | Easy | n/a |

## 7. Assumptions

| ID | Assumption | Confidence | Falsification |
|----|-----------|------------|---------------|
| ASM-01 | Customer X SOC2 deadline holds (Q4) | High | If extended → Partial → Minimum scenario possible |
| ASM-02 | 4 senior devs available for full scope | Medium | If 1 leaves: timeline +25%; if hire takes 3mo: cost +$60K |
| ASM-03 | Sales pipeline projection $1.5M ARR holds | Medium | If half closes → benefit projections halved |
| ASM-04 | Vendor pricing stable | High | Postgres managed price increase 10%/yr is built in |
| ASM-05 | Customer churn projection (3 accounts) holds | Medium | Might be 2 (saving $240K) or 5 (losing more) |

## 9. Recommendation

**Recommended scenario: Partial.**

**Top reasons:**
1. Best risk-adjusted ROI: 7-month payback vs. 19-month for Full; meets SOC2 deadline
2. Closes all P0 findings without committing to 28-week effort that may exhaust team
3. Preserves optionality for Year 2 — Phase 2-3-4 work can be sequenced separately

**What would change the recommendation:**
- **→ Full** if: customer expansion (e.g., enterprise tier) requires architectural changes inherent in Full scope; OR sales pipeline doubles (>$3M ARR gated on modernization)
- **→ Minimum** if: revenue contracts (>20% drop); OR team loses 2+ senior devs

**Decisions needed from leadership by 2026-06-15:**
- [ ] Approve $480K Partial budget (or modified)
- [ ] Confirm 14-week timeline aligns with Customer X SOC2 deadline (Q4)
- [ ] Approve out-of-scope items (Phase 2-4 deferred to Year 2)
```

---

## Calibration notes

- **Cost of Inaction is the anchor.** Without it, scenarios float. $1.085M baseline grounds every comparison.
- **Year-1 vs Year-3 distinction.** Partial has lower Y1 benefit ($870K vs $890K) but vastly better ROI (629% vs 216% Y3) because cost is 1/3.
- **Recommendation has explicit conditions to flip.** Stakeholders rarely accept blind recommendations — this empowers them to engage.
- **Team burnout listed as risk.** Honest about non-financial costs — leadership respects this.
- **Deferred items become Year 2 commitment.** Avoids "Partial just becomes Minimum that we never finish".
- **SOC2 timeline drives ASM-01.** If that assumption shifts, the entire frame changes — explicit confidence level and falsification path matters.
