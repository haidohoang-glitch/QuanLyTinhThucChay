# Feasibility Assessment — Adaptation

Variations by project context.

> **Applies to Mode A (3-scenario) only.** Mode B/C follow their conventions.

## Regulated industries (compliance-driven)

When compliance is a hard deadline driver:

**Adjust:**
- Add "regulatory exposure" line in Cost of Inaction (probability × fine × revenue impact of non-compliance)
- Compliance NFR achievement is a binary benefit, not ROI-based
- Include certification cost (auditor, gap analysis) explicitly

**Add:**
- "Compliance milestone" timeline (when does each scenario achieve which compliance gate?)
- "If audit triggered before completion" risk per scenario
- Sign-off requires Legal/Compliance lead in addition to Eng/Finance

## Early-stage startups

When budget is tight and uncertainty high:

**Adjust:**
- Use "lean" cost models (fewer scenarios; usually just "Do" vs "Don't")
- Time-to-value matters more than absolute ROI (cash runway constraint)
- Opportunity cost is huge (every week not building features = competitive risk)

**Add:**
- Runway impact (does this consume runway?)
- "Survival case" scenario: what's the absolute minimum to survive next milestone?

## Enterprise procurement

When the audience is procurement/finance with formal NPV/IRR requirements:

**Adjust:**
- Add NPV calculation: discount Year-N benefits at company's discount rate
- Add IRR (Internal Rate of Return) per scenario
- Multi-year cash flow projection (5+ years typical)

**Add:**
- Depreciation schedule for capex items
- Tax implications (capex vs opex treatment)
- Total Cost of Ownership (TCO) over 5 years

## Build vs Buy decision

Specific structure:

- "Build" scenario: full cost of building + maintaining
- "Buy" scenarios: vendor A, B, C (each becomes a scenario)
- "Hybrid" scenario: build core, buy commodity

**Add:**
- Switching cost (if buy and later need to switch)
- Vendor lock-in risk
- Strategic capability (does building this become a moat?)

## Rewrite vs Refactor decision

Specific structure:

- Scenarios: full rewrite / phased refactor / status quo + targeted fixes
- Time-to-value matters: rewrite often slow

**Add:**
- "Bridge" period cost (running both during cutover)
- Knowledge loss risk (rewrite team may not preserve domain knowledge)
- "Big bang" vs "strangler fig" approaches per scenario

## Nonprofit / mission-driven

When primary value isn't financial:

**Adjust:**
- Replace "ROI" with "Mission Impact ratio"
- Quantify in mission units: "people served per $", "tons CO2 avoided per $"
- Financial ROI may be neutral or negative; mission impact carries weight

**Add:**
- Theory of change link: which mission outcome does each scenario advance?
- Impact measurement plan: how will you know it worked?

## Internal tool / B2B back-office

When users are internal employees:

**Adjust:**
- Benefits are productivity-based ("save 200 hours/month for support team = $X at loaded cost")
- Customer impact often indirect (faster support → customer satisfaction)
- Can be harder to quantify; use ranges with rationale

## Vendor consolidation

Special case: replacing N tools with 1:

**Scenarios:** consolidate full / consolidate partial / status quo
**Add:**
- Per-tool license savings
- Integration cost (often higher than expected)
- Workflow disruption during migration

## Rapidly changing market

When the market shifts under analysis:

**Add:**
- Time-decay assumption: "If this analysis is X months old, re-validate before deciding"
- Competitor move sensitivity: "If Competitor Y launches feature Z, scenario re-evaluation"
- Optionality value: scenarios that preserve future flexibility worth more

---

## Cross-cutting: confidence calibration

Match confidence to data:

| Confidence | Data basis |
|------------|-----------|
| **High** | Real production data, 12+ months history, validated externally |
| **Medium** | Limited production data + reasonable industry benchmarks |
| **Low** | Mostly estimates and benchmarks; few measured points |

Avoid HIGH confidence on early-stage projects. Pattern of "all High" suggests over-claim.

---

## When NOT to use this skill

- Trivial decisions (1-2 day work) — too much overhead
- Research / discovery questions where the answer is "we don't know yet" — do the discovery first
- Strategic / brand questions (e.g., "should we expand to EU?") — broader business analysis, not technical feasibility

If the audience needs a 1-pager, write a 1-pager (executive summary + recommendation). Use this template only when full analysis is genuinely required.
