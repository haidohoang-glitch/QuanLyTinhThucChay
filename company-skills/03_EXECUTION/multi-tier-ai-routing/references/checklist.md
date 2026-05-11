# Multi-Tier AI Routing — Quality Checklist

Run before delivering AI_AGENT_TASK_DISTRIBUTION.md.

## Gate 1 — Tool inventory

- [ ] Section 1 lists all AI tools the project may use
- [ ] Cost (input/output per 1M tokens) accurate as of writing date
- [ ] Privacy / DPA status noted per vendor
- [ ] Strengths and weaknesses honest (not just marketing)

## Gate 2 — Tier definitions

- [ ] Each tier has Capability statement
- [ ] Each tier lists 5+ use case examples
- [ ] Each tier has pinned models (specific, not "Claude")
- [ ] Token budget per task estimated per tier
- [ ] Verification approach per tier specified

## Gate 3 — Classification rubric

- [ ] Section 4 has decision flowchart or sequential checklist
- [ ] Rubric matches earliest condition (deterministic outcome)
- [ ] Edge cases addressed ("when in doubt" guidance)

## Gate 4 — Prompt templates

- [ ] Tier 1, 2, 3 prompt templates present
- [ ] Each template clear about DO and DO NOT
- [ ] Each template has output format guidance
- [ ] Stop conditions in each prompt
- [ ] Templates work across vendors (avoid vendor-specific syntax unless mandated)

## Gate 5 — Cost projection

- [ ] Per-phase cost estimate present
- [ ] Cost-saving vs. all-Tier-3 baseline calculated
- [ ] Token budget × task volume × model price → realistic
- [ ] If projected cost > 10% of project budget, flag for review

## Gate 6 — Escalation rules

- [ ] Section 7 covers Tier 1→2, Tier 2→3, Tier 3 retry → operator
- [ ] Each rule has clear trigger (not "if it doesn't work")
- [ ] Action is specific (not "escalate")

## Gate 7 — Vendor outage fallbacks

- [ ] Section 8 covers each major vendor's outage scenario
- [ ] Fallback model named (not "another model")
- [ ] Action steps when fallback engaged documented

## Gate 8 — Privacy / compliance

- [ ] DPA / BAA / SOC2 status of each vendor noted
- [ ] If project handles PII / PHI / financial data, only compliant vendors used at relevant tiers
- [ ] Free tiers (no DPA) restricted to non-PII data

## Gate 9 — Quotas (if applicable)

- [ ] Daily / monthly spending limits per tier (if team uses quotas)
- [ ] Action when exceeded (pause / escalate)

## Gate 10 — Update cadence

- [ ] Section 11 specifies when document updates (vendor add/remove, pricing change, retros)
- [ ] Quarterly review mandate documented

## Gate 11 — Mode discipline

- [ ] Mode A: 3-tier (Simple/Mid/Strong + Human)
- [ ] Mode B: company catalog mapped to capability tiers
- [ ] Mode C: user-defined; rationale documented

## Gate 12 — Format

- [ ] Output: `docs/03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md`
- [ ] Tier symbols (🟢 🟡 🔴 👤) used consistently
- [ ] Tables for: tools, tiers, classification rubric, cost projection, fallbacks, quotas

## Self-review prompt

Pick a real task from a real WP. Apply the rubric mentally. Does it route to the cheapest tier that can do it correctly? If not, the rubric is mis-calibrated.

Imagine Anthropic API outage Wednesday morning. Could the operator continue working using only the document? If steps are vague or fallbacks unspecified, sharpen.

Sum projected cost. Is it 20-40% of all-Tier-3 baseline? Good — you're routing well. If 70%+, you're not capturing value of multi-tier.
