# Multi-Tier AI Routing — Adaptation

Variations by project context.

> **Applies to Mode A (3-tier) only.** Mode B/C follow company/user policy.

## Solo developer / hobby project

When budget is near $0:

**Adjust:**
- Lean heavily on free tiers (Gemini Flash, Gemma local)
- Tier 3 used sparingly — usually only for design moments
- Skip vendor outage fallbacks (downtime acceptable)

**Watch for:** Free tier quota exhaustion mid-task.

## Cost-pressured projects

When budget capped tightly (e.g., <$50/month):

**Adjust:**
- Push more tasks to Tier 1 (rewrite if needed to make Tier-1-eligible)
- Defer Tier 3 tasks; batch them per phase milestone
- Use local models (Ollama Gemma) where privacy-acceptable

**Add:**
- Pre-task cost estimate; abort if would exceed remaining budget

## Regulated industries

**Adjust:**
- All tiers must use BAA / DPA-signed vendors only
- Free tiers (typically no DPA) banned
- On-prem / customer-managed-keys options preferred

**Add:**
- Vendor data classification list (which vendors can see PII / PHI / cardholder data)
- Per-task data sensitivity check before sending to AI
- Audit log of every AI prompt+response (some regulators require)

## On-premise only / air-gapped

When AI cloud services unavailable:

**Adjust:**
- All tiers use local models (Ollama, vLLM-hosted)
- Tier 3 may be challenging (local models still trail SaaS frontier)
- Cost is hardware (GPU) + electricity, not per-token

**Add:**
- Hardware capacity per tier (e.g., A100 for Tier 3 model; consumer GPU for Tier 1)
- Model update cadence (download new model versions periodically)

## Multi-vendor strategy

When deliberately using 2+ vendors per tier:

**Reasons:**
- Hedge against vendor failure
- Cross-vendor testing (run same task on Claude + GPT; compare)
- Different vendors strong at different things

**Adjust:**
- Document which vendor for which task type (e.g., "GPT for OCR / vision; Claude for code")
- Test prompts on both before committing
- Track cost per vendor

## Model versioning

When pinning model versions matters (regulated, reproducibility):

**Adjust:**
- Pin specific versions (e.g., `claude-opus-4-20250115`) not "latest"
- Update version with explicit retest of representative tasks
- Document in Section 3 of policy

**Watch for:**
- Some vendors deprecate older versions; have migration plan

## Consumer mobile / IoT projects

When AI inference happens on-device (not cloud):

**Adjust:**
- Tier 1 / 2 may be on-device models (much smaller capability)
- Tier 3 reserved for design (developer's machine, not deployed)
- Different cost model: model size affects app/firmware size

## Open-source projects

When the project is open and contributors use AI:

**Adjust:**
- Document policy in CONTRIBUTING.md
- AI-assisted PRs disclosed
- Free tiers acceptable for routine contributions

**Add:**
- Code-quality gate for AI-assisted PRs (extra review for hallucinations)

## High-throughput projects

When task volume is very high (1000+ tasks/day):

**Adjust:**
- Cost matters disproportionately; aggressive Tier 1 routing
- Latency matters; faster models per tier
- Caching: identical prompts → cached response

**Add:**
- Batching where possible
- Rate-limit handling per vendor

## Latency-critical projects

When operator interactivity is key:

**Adjust:**
- Use streaming-capable models
- Tier 1 uses faster models (Haiku, Flash) over cheaper-but-slower
- Avoid models with high TTFB (time to first token)

## When to use ALL Tier 3

Sometimes the routing optimization isn't worth it:

- **Very small projects (1-2 WPs)** — overhead of routing isn't worth it
- **Pure architectural exploration** — every task is design-quality
- **Brand-new domain** — until team learns, every task feels Tier 3

In these cases, default to Tier 3 with operator gating; revisit policy after first few WPs.

## When to use ALL Tier 1

- **Very mechanical work** (mass file rename, batch format updates)
- **Boilerplate generation** at scale
- **Test data creation**

In these cases, skip Tier 2/3 entirely; just operator gates.

---

## Privacy-first routing

If project is privacy-sensitive:

```
Public data + non-PII → Tier 1 free vendors OK
PII (lawful basis, DPA exists) → Tier 1-3 DPA-signed vendors
PHI → Tier 1-3 BAA-signed vendors only
Cardholder data → Tier 1-3 PCI-aligned vendors only; tokenize before AI sees
Trade secrets → On-prem models only
```

Document data flow per task type.

---

## When to revise the policy

Review policy quarterly OR when:

- New AI vendor added
- Vendor pricing changes >10%
- Cost overrun (actual >2x projected)
- Quality issues (Tier 1 missing inferences it should handle)
- Privacy posture changes (new regulation, vendor compliance shift)

Don't let policy rot — it's the foundation of cost discipline.
