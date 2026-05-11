# {{PROJECT_NAME}} — AI Task Distribution Policy

> **Purpose:** Tier policy — which AI model handles which task class. Optimizes cost and safety.
> **Audience:** Operators, AI agents, finance/budget owner.
> **Last updated:** {{YYYY-MM-DD}}
> **Generated using:** `multi-tier-ai-routing` skill v1
> **Owner:** {{NAME}}

---

## 1. Available AI Tools

| Tool | Vendor | Cost (input / output per 1M tokens) | Strengths | Constraints |
|------|--------|--------------------------------------|-----------|-------------|
| {{e.g., Claude Opus 4}} | Anthropic | $15 / $75 | Strong reasoning, long context | High cost; DPA required |
| {{Claude Sonnet}} | Anthropic | $3 / $15 | Balanced | DPA required |
| {{Claude Haiku}} | Anthropic | $0.80 / $4 | Fast, cheap | DPA required |
| {{GPT-4o}} | OpenAI | $5 / $15 | General, multimodal | DPA required |
| {{GPT-4o-mini}} | OpenAI | $0.15 / $0.60 | Cheap | DPA required |
| {{Gemini 2.0 Flash}} | Google | $0 (free tier) | Free, fast | Quota; no DPA on free tier |
| {{Gemma 3 1B}} | Google (Ollama local) | $0 (local compute) | No vendor; offline; private | Limited capability |

(Update quarterly; AI pricing changes.)

---

## 2. Routing Mode

See Section 9 for chosen mode (A / B / C). Default Mode A: 3-tier (Simple / Mid / Strong) + Human.

---

## 3. Tier Definitions

### Tier 1 — Simple AI (🟢)

**Capability:** Mechanical execution. Cannot infer; must be told exactly what to do.

**Use cases:**
- Run install / config commands
- Create file with given content
- Format / lint / minor cleanup
- Copy template; substitute placeholders
- Simple file edits ("replace line X with Y")
- Run tests (just execute; not interpret)

**Models pinned for this project:**
- {{Primary: e.g., Gemini 2.0 Flash (free tier)}}
- {{Fallback: e.g., GPT-4o-mini ($0.15/$0.60)}}
- {{Local: e.g., Gemma 3 1B via Ollama}}

**Token budget per task:** ~2K tokens average

**Verification:** Single shell command; operator runs after each task.

### Tier 2 — Mid AI (🟡)

**Capability:** Read existing code; implement clearly-specified changes; multiple correct implementations OK; reasoning visible.

**Use cases:**
- Implement function from spec
- Write tests for existing function
- Refactor within a single file
- Apply consistent pattern across related files (in scope)
- Code review with clear criteria

**Models pinned:**
- {{Primary: e.g., Claude Sonnet}}
- {{Fallback: e.g., GPT-4o}}

**Token budget per task:** ~10K tokens average

**Verification:** Diff review (~5-10 min operator time).

### Tier 3 — Strong AI (🔴)

**Capability:** Architecture, design, multi-file refactor, hard debugging, cross-cutting concerns.

**Use cases:**
- ADR-quality design decisions
- Cross-file refactor planning
- Debug obscure / non-obvious failures
- Decompose WP into tasks (`work-package-decomposer` skill)
- Code review with judgment

**Models pinned:**
- {{Primary: e.g., Claude Opus 4}}
- {{Fallback: e.g., OpenAI o3 / o1}}

**Token budget per task:** ~30K tokens average

**Verification:** Operator + (sometimes) peer review (15-60 min).

### Human (👤)

**Capability:** Decision authority, business context, ethics, ambiguity resolution.

**Use cases:**
- Approve plan / diff / PR
- Choose between options when AI presents alternatives
- Resolve ambiguity in WP doc
- Compliance / security / legal sign-off

**Verification:** n/a (the human IS the verifier elsewhere).

---

## 4. Task Classification Rubric

When given a task, classify it using this checklist (in order):

```
Is the task...

1. A decision / approval that needs business or ethics judgment?
   → 👤 HUMAN

2. Architecture, design, multi-file coordination, or hard debugging?
   → 🔴 TIER 3

3. Reading + implementing per clear spec; multiple correct outputs OK?
   → 🟡 TIER 2

4. Mechanical (run / copy / format) with exact prompt possible?
   → 🟢 TIER 1
```

(Match earliest matching condition. Most tasks land at Tier 1 once decomposed properly.)

### When in doubt

If between Tier 1 and Tier 2: try Tier 1 first; if it fails, escalate. Cost of trying Tier 1 ≈ free.

If between Tier 2 and Tier 3: depends on cost/risk. For low-risk WPs, Tier 2; for high-risk (security, data migration), Tier 3.

---

## 5. Prompt Templates

### Tier 1 — System prompt template

```
You are a Tier 1 Executor AI. Your role: execute mechanical tasks exactly as specified.

DO:
- Execute prompt verbatim
- Return only the requested artifact

DO NOT:
- Add commentary, explanations, "improvements"
- Make judgment calls
- Modify files outside prompt scope
- Run destructive commands (git commit, push, rm) without explicit instruction in the prompt

If prompt is ambiguous, respond: "AMBIGUOUS — please clarify: [specific question]" and STOP.

OUTPUT FORMAT: per prompt instruction. If unspecified, return the requested artifact in markdown code block.
```

### Tier 2 — System prompt template

```
You are a Tier 2 Mid AI. Your role: implement clearly specified work; reason about existing code.

DO:
- Read provided context
- Implement per spec; produce diff or full code as requested
- Add tests if requested
- Cite which files you modified and lines changed

DO NOT:
- Architect new patterns (escalate to Tier 3)
- Refactor beyond stated scope
- Modify files outside the WP "Files affected" list
- Invent context — request specific files if needed

If context insufficient, request specific files (don't guess); STOP.
```

### Tier 3 — System prompt template

```
You are a Tier 3 Strong AI / Orchestrator. Your role: design, plan, supervise, debug.

DO:
- Provide ADR-quality reasoning for decisions
- Critically review proposed code
- Decompose work and coordinate

DO NOT:
- Bypass operator approvals
- Commit/push autonomously
- Skip verification steps
- Reach for the most complex solution when simpler suffices

OUTPUT FORMAT: structured (markdown sections, tables, code blocks). Cite WP/SRS IDs.
```

---

## 6. Cost Projection

### Per-phase estimate

| Phase | Total tasks (est.) | T1 count × $0 | T2 count × $0.10 | T3 count × $0.30 | Phase total |
|-------|--------------------|----------------|-------------------|-------------------|-------------|
| 0 | {{N}} | {{N1 × $0 = $0}} | {{N2 × $0.10}} | {{N3 × $0.30}} | {{$P0}} |
| 1 | {{N}} | {{...}} | {{...}} | {{...}} | {{$P1}} |
| 2 | {{N}} | {{...}} | {{...}} | {{...}} | {{$P2}} |
| 3 | {{N}} | {{...}} | {{...}} | {{...}} | {{$P3}} |
| 4 | {{N}} | {{...}} | {{...}} | {{...}} | {{$P4}} |
| **Total** | **{{N}}** | | | | **{{$T}}** |

### Cost saving vs. all-Tier-3

If every task ran on Claude Opus: ~{{$X — typically 3-5× higher}}.

Projected saving: {{%}} ({{$X — saved}}).

---

## 7. Escalation Rules

| Trigger | Action |
|---------|--------|
| Tier 1 output wrong (verify fails) | Re-run with more context (1 retry) |
| Tier 1 output wrong (2 retries failed) | Escalate to Tier 2 |
| Tier 2 produces inconsistent diffs across 2 runs | Escalate to Tier 3 |
| Tier 3 task requires 3+ iterations | Pair operator with Tier 3 OR split task |
| Tier 1 prompt is "AMBIGUOUS" response | Operator clarifies prompt before retry |

---

## 8. Vendor Outage Fallbacks

| Primary down | Fallback |
|--------------|----------|
| Anthropic API | Tier 2 → GPT-4o; Tier 3 → OpenAI o3 |
| OpenAI API | Tier 2/3 → Anthropic |
| Gemini Free quota exhausted | Tier 1 → GPT-4o-mini ($0.15/$0.60 paid) |
| All cloud unavailable | Tier 1 → local Gemma 3 1B via Ollama |

**Action when fallback engaged:**
- Document in operator log
- Verify fallback's output equivalent (different vendors may produce slightly different code)
- Resume primary when restored

---

## 9. Notes

- **Routing mode:** {{A — Standard 3-tier / B — Honor company / C — User-defined}}
- **Mode rationale:** {{WHY}}
- **Privacy / DPA status:**
  - {{Vendor A}}: DPA signed; data classification limit: {{TIER}}
  - {{Vendor B}}: BAA signed; can handle PHI
  - {{Vendor C}}: free tier — NO DPA; do not send PII
- **Last reviewed:** {{YYYY-MM-DD}} by {{NAME}}; next review: {{DATE}} (quarterly)

---

## 10. Per-Tier Quotas (if applicable)

If team has internal quotas / spending limits:

| Tier | Daily limit | Monthly limit | Action when exceeded |
|------|-------------|----------------|----------------------|
| 🟢 Tier 1 | ∞ (free) | ∞ | n/a |
| 🟡 Tier 2 | $10/day | $200/month | Operator alerted; pause non-critical Tier 2 |
| 🔴 Tier 3 | $20/day | $500/month | Escalate to manager for over-budget |

---

## 11. Update Cadence

This document changes when:
- New AI vendor added → update Section 1, 5, 8
- Vendor pricing changes → update Section 1, 6
- Vendor model deprecated → update Section 3
- Project tier policy revised after retro → update Sections 3-4

**Quarterly review** mandatory (AI landscape moves fast).

---

*This policy applies to all WPs. `work-package-decomposer` skill applies it per-WP. Operators consult this when uncertain about tier assignment.*
