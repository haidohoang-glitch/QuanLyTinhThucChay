# Multi-Tier AI Routing — Worked Example

Anonymized. Fictional project: **mid-size SaaS migration** (similar to "Project Voyager"). Mode A.

## Context

**Imagined input:** "Set up tier policy for a 14-week migration project. Budget: $300/month for AI. We have access to Claude (all tiers), Gemini Flash free, GPT-4o-mini, local Ollama with Gemma. Project handles customer PII (DPA required for cloud vendors)."

---

## Output excerpt

```markdown
# Project Migration — AI Task Distribution Policy

## 1. Available AI Tools

| Tool | Vendor | Cost | Strengths | Constraints |
|------|--------|------|-----------|-------------|
| Claude Opus 4 | Anthropic | $15 / $75 | Strong reasoning | DPA signed (PII OK); High cost |
| Claude Sonnet | Anthropic | $3 / $15 | Balanced | DPA signed (PII OK) |
| Claude Haiku | Anthropic | $0.80 / $4 | Fast, cheap | DPA signed |
| GPT-4o | OpenAI | $5 / $15 | General | DPA signed |
| GPT-4o-mini | OpenAI | $0.15 / $0.60 | Cheap | DPA signed |
| Gemini 2.0 Flash | Google | $0 (free tier) | Free | **NO DPA on free tier — only synthetic / non-PII data** |
| Gemma 3 1B | Local Ollama | $0 (compute) | Offline | Limited capability |

## 3. Tier Definitions

### Tier 1 — Simple AI (🟢)

**Models:**
- Primary: Claude Haiku ($0.80/$4 — DPA covers PII)
- Free fallback: Gemma 3 1B local (NO PII concerns since on-prem)
- Cheap fallback: GPT-4o-mini ($0.15/$0.60 — DPA covers PII)

**Note:** Gemini Flash NOT used at Tier 1 because no DPA — would prevent us from sending any PII.
This is the cost trade-off: sacrifice the $0 tier for compliance simplicity.

**Token budget:** ~2K tokens per task → ~$0.005 per task on Haiku

### Tier 2 — Mid AI (🟡)

**Models:**
- Primary: Claude Sonnet ($3/$15 — DPA covers PII)
- Fallback: GPT-4o ($5/$15 — DPA covers PII)

**Token budget:** ~10K tokens per task → ~$0.10 per task on Sonnet

### Tier 3 — Strong AI (🔴)

**Models:**
- Primary: Claude Opus 4 ($15/$75 — DPA covers PII)
- Fallback: OpenAI o3 ($15/$60 — DPA covers PII)

**Token budget:** ~30K tokens per task → ~$1.20 per task on Opus

## 4. Task Classification Rubric

```
Is the task...

1. A decision / approval / business judgment?
   → 👤 HUMAN

2. Architecture, multi-file refactor, hard debugging?
   → 🔴 TIER 3

3. Read existing code + implement per clear spec?
   → 🟡 TIER 2

4. Mechanical (run / copy / format / install)?
   → 🟢 TIER 1
```

When in doubt: try Tier 1; if fails, escalate to Tier 2.

## 6. Cost Projection

Estimated 31 WPs across 5 phases × ~12 tasks per WP = ~370 tasks total.

Distribution per typical WP:
- 60% Tier 1 = 222 tasks × $0.005 = $1.11 total
- 25% Tier 2 = 92 tasks × $0.10 = $9.20 total
- 10% Tier 3 = 37 tasks × $1.20 = $44.40 total
- 5% Human = 19 tasks × $0 = $0

**Projected total cost across project: ~$55**

If all Tier 3: 370 × $1.20 = $444

**Cost saving: ~88%**

## 8. Vendor Outage Fallbacks

| Primary down | Action |
|--------------|--------|
| Anthropic API | Switch to OpenAI: Sonnet → GPT-4o; Opus → o3; Haiku → GPT-4o-mini |
| OpenAI API | Switch to Anthropic (already primary) |
| Both Anthropic + OpenAI | Tier 1 → local Gemma 3 1B; Tier 2/3 → pause until either restored |

## 9. Notes

- **Routing mode:** A — Standard 3-tier
- **Privacy:** Project handles PII; only DPA-signed vendors at all tiers
- **Free tier (Gemini) deliberately not used at Tier 1** — DPA gap; simplicity prioritized over $0 cost
- **Last reviewed:** 2026-09-15; next review: 2026-12-15

## 10. Quotas

| Tier | Daily | Monthly | Action when exceeded |
|------|-------|---------|----------------------|
| 🟢 Tier 1 | $5 | $50 | Soft alert; usually within budget |
| 🟡 Tier 2 | $20 | $200 | Pause non-critical; investigate routing |
| 🔴 Tier 3 | $30 | $200 | Escalate to manager |
| **Total** | $55 | **$300** (budget cap) | Hard limit |

## 11. Update Cadence

- Quarterly review (next: 2026-12-15)
- Triggered review: vendor pricing change >10%; new vendor onboarded; cost overrun >2x
```

---

## Calibration notes

- **Privacy decision drives routing.** Project handles PII; team chose DPA-signed vendors at all tiers, sacrificing the $0 Gemini free tier for compliance simplicity.
- **Realistic cost projection.** $55 total for 370 tasks; project budget of $300/mo provides headroom for retries, escalations, exploration.
- **88% cost saving documented.** Defensible to finance/board: "we save $389 by routing intelligently".
- **Fallback if both Anthropic + OpenAI down:** local Gemma for Tier 1; pause for Tier 2/3. Honest about limit.
- **Quotas align to budget.** Daily × 30 ≈ monthly; total ≤ budget.
- **No "all-Tier-3 default" anti-pattern.** Forces routing per-task.
- **Free tier excluded by privacy.** Documented WHY ("no DPA"), not just "we don't use Gemini" — future operator can re-evaluate if Google offers free DPA tier.
