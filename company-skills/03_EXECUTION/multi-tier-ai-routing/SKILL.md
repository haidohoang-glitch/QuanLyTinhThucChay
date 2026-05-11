---
name: multi-tier-ai-routing
description: Define the project's AI tier policy — which AI model handles which class of task to optimize cost and safety. Produces AI_AGENT_TASK_DISTRIBUTION.md with classification rubric, model-to-tier mapping, prompt templates per tier, and cost projections. Distinct from `work-package-decomposer` which APPLIES the policy to a specific WP. Use when starting an AI-assisted project to set the tier policy, when adding new AI vendors and need to route them, or when generating Phase 3 Execution routing output. Triggers include "set up AI tier policy", "which AI for which task", "task routing", "author AI_AGENT_TASK_DISTRIBUTION", or "Phase 3 Execution routing".
---

# Multi-Tier AI Routing

Define **the policy** for routing tasks across AI tiers — not the per-WP application. This skill produces `AI_AGENT_TASK_DISTRIBUTION.md`, which `work-package-decomposer` references when classifying individual tasks.

## When this skill applies

Use when:
- Starting an AI-assisted project; need to choose tier policy upfront
- Adding new AI vendors / models; need to slot them into tiers
- Reviewing cost; need to revise tier mappings
- Producing Phase 3 Execution routing output

Do NOT use for:
- Per-WP task decomposition (use `work-package-decomposer` — it APPLIES this policy)
- Operator workflow (use `ai-operator-protocol`)
- Authoring requirements / plans (Phase 0/2 skills)

## Inputs

1. **Available AI tools** — which models/services the team has access to (Claude tier, OpenAI tier, Gemini tier, local models)
2. **Budget constraint** — monthly AI spend cap
3. **Project risk profile** — regulated? customer-facing? prototype?
4. **Team's AI literacy** — junior/mid/senior; affects how much policy needed
5. `docs/02_STRATEGIC/MASTER_PLAN.md` — to estimate task volume

## Output

`docs/03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md`, filled from [assets/AI_TASK_DISTRIBUTION_template.md](assets/AI_TASK_DISTRIBUTION_template.md).

## Workflow

### Step 1 — Inventory available AI tools

List every AI service/model the project may use:

| Tool | Vendor | Cost (input/output per 1M tokens) | Strengths | Weaknesses |
|------|--------|------------------------------------|-----------|------------|
| Claude Opus 4 | Anthropic | $15 / $75 | Strong reasoning, long context, code review | Highest cost |
| Claude Sonnet | Anthropic | $3 / $15 | Balanced; good for most coding | Mid cost |
| Claude Haiku | Anthropic | $0.80 / $4 | Fast, cheap, mechanical | Less reasoning |
| GPT-4o | OpenAI | $5 / $15 | General, multimodal | Privacy considerations |
| GPT-4o-mini | OpenAI | $0.15 / $0.60 | Very cheap | Limited reasoning |
| Gemini 2.0 Flash | Google | $0 (free tier) | Free, fast, decent | Free quota limits |
| Gemma 3 1B | Google (local via Ollama) | $0 (compute) | No vendor lock-in; offline | Limited capability |
| {{...}} | {{...}} | {{...}} | {{...}} | {{...}} |

Update for current pricing (these change quarterly).

### Step 2 — Choose routing mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — Standard 3-tier policy** *(default)* | No company policy; cost-optimization + safety baseline | This skill's standard tiers |
| **B — Honor company AI catalog / governance** | Company has approved-vendors list and tier policy | Company doc |
| **C — User-defined routing** | Specific routing logic (e.g., per language, per repo, per environment) | User input |

Selection logic:
1. User explicit → use it
2. Company has AI catalog → ask user
3. Default → Mode A

#### Mode A — Standard 3-tier policy

| Tier | Symbol | Capability | Use cases | Suggested models |
|------|--------|-----------|-----------|------------------|
| **1 — Simple** | 🟢 | Mechanical execution; no inference | Run commands, copy templates, format files, paste-and-go boilerplate | Gemma 3 1B (local), Gemini Flash, GPT-4o-mini, Haiku |
| **2 — Mid** | 🟡 | Moderate inference; clear spec; multiple valid implementations | Implement function from spec, write tests, refactor within file, interpret unambiguous code | Claude Sonnet, GPT-4o |
| **3 — Strong** | 🔴 | Architecture, multi-file coordination, hard debugging | Design ADRs, cross-file refactors, debug obscure issues, complex code review | Claude Opus, GPT-o1/o3 |
| **Human** | 👤 | Decisions, approvals, ambiguity, ethics | Approve PR, choose between options, review for compliance | n/a |

#### Mode B — Company catalog

If company has an approved-vendor list, map company tiers to capability tiers:

| Company tier | Capability tier | Models |
|--------------|-----------------|--------|
| Self-service (no DPA needed) | Tier 1 (mostly) | {{LIST}} |
| DPA-signed vendors | Tier 1-2 | {{LIST}} |
| BAA / regulated vendors | All tiers | {{LIST}} |

#### Mode C — User-defined routing

Examples:
- "Per language": Claude for backend, Gemini for frontend
- "Per repo": Tier 3 only on customer-facing code; Tier 1 for internal tools
- "Per environment": Tier 1 freely in dev; Tier 3 review for prod-bound changes

### Step 3 — Write task classification rubric

For Mode A or extension, define **what makes a task each tier**. The rubric guides `work-package-decomposer` skill.

**Tier 1 (🟢) checklist:**
- Task is mechanical (run, copy, format, install)
- Prompt can specify exact output (no inference required)
- Verification is one shell command
- Failure obvious and recoverable
- Risk of harm: minimal

**Tier 2 (🟡) checklist:**
- Task requires reading existing code + modifying consistently
- Spec is clear; multiple correct implementations OK
- Verification: diff review (~5 min)
- Risk: moderate (subtle bugs possible)

**Tier 3 (🔴) checklist:**
- Architecture or design decisions involved
- Multi-file coordination
- Hard debugging (not obvious from error message)
- Verification: hours of review
- Risk: high (wrong direction may propagate)

**Human (👤) checklist:**
- Decision authority required
- Context AI can't see (business priority, customer history)
- Approval gate
- Ethics / compliance / legal judgment

### Step 4 — Pick models per tier

For each capability tier, pick 1-2 specific models the project will use. Avoid more than 2 per tier (overhead).

Considerations:
- **Cost:** match budget to expected task volume
- **Latency:** if tasks are interactive, faster models matter
- **Privacy:** regulated industries may require BAA / DPA / on-prem
- **Quality variance:** newer models may break prompts; pin versions

Document choice rationale.

### Step 5 — Provide prompt templates per tier

Each tier needs a **system prompt template** for the typical task.

#### Tier 1 prompt template

```
You are a Tier 1 Executor AI. Your role: execute mechanical tasks exactly as specified.

DO:
- Execute prompt verbatim
- Return requested artifact

DO NOT:
- Add commentary, explanations, "improvements"
- Make judgment calls
- Modify files outside prompt scope
- Run destructive commands (git commit, push, rm) without explicit instruction

If prompt is ambiguous, respond: "AMBIGUOUS — please clarify: [specific question]" and STOP.
```

#### Tier 2 prompt template

```
You are a Tier 2 Mid AI. Your role: implement clearly specified work, requiring reading existing code.

DO:
- Read context provided
- Implement per spec
- Return diff or code with explanation if asked
- Add tests if WP requires

DO NOT:
- Architect new patterns (escalate to Tier 3)
- Refactor beyond scope
- Modify files outside WP "Files affected"

If context insufficient, request specific files; do NOT invent.
```

#### Tier 3 prompt template

```
You are a Tier 3 Strong AI / Orchestrator. Your role: design, plan, supervise, debug hard issues.

DO:
- Design architecture, decompose work, coordinate
- Provide ADR-quality reasoning for decisions
- Critically review proposed code

DO NOT:
- Bypass operator approvals
- Commit/push autonomously
- Skip verification steps

Output: structured (markdown sections, tables, code blocks).
```

### Step 6 — Estimate task volume + cost

From `MASTER_PLAN.md` (or implementation plan), estimate:

- **Total tasks per phase:** Sum WPs × estimated tasks per WP (use `work-package-decomposer` rule of thumb)
- **Tier distribution:** Apply policy (typical: 60% Tier 1, 25% Tier 2, 10% Tier 3, 5% Human)
- **Tokens per task:** Tier 1 ~2K tokens; Tier 2 ~10K; Tier 3 ~30K
- **Cost per phase:** Tasks × tokens × $/M

| Phase | Total tasks | T1 cost | T2 cost | T3 cost | Total |
|-------|-------------|---------|---------|---------|-------|
| 0 | {{N}} | {{$X}} | {{$Y}} | {{$Z}} | {{$T}} |

Compare to all-Tier-3 baseline (typical 3-5x higher) — document cost saving.

### Step 7 — Define escalation rules

When does a task get escalated to higher tier?

| Trigger | Action |
|---------|--------|
| Tier 1 task fails twice (output wrong) | Escalate to Tier 2 |
| Tier 2 task produces multiple inconsistent diffs | Escalate to Tier 3 |
| Tier 3 task requires multiple iterations | Operator pair OR break into sub-tasks |
| Verification consistently fails | Investigate prompt / context, not just retry |

Document so operators handle escalation consistently.

### Step 8 — Define vendor failure handling

When a vendor is unavailable:

| Vendor down | Fallback |
|-------------|----------|
| Anthropic API | Switch Tier 2 to GPT-4o; Tier 3 to GPT-o1 (different prompt format) |
| OpenAI API | Switch to Anthropic |
| Gemini Free | Switch Tier 1 to GPT-4o-mini ($0.15/$0.60) — paid but cheap |
| All cloud unavailable | Local Ollama fallback for Tier 1 |

This isn't theoretical — vendor outages happen.

### Step 9 — Self-review

Run [references/checklist.md](references/checklist.md). Routing policy affects every WP execution; rigor matters.

## Quality bar

A good routing policy lets:
- An operator know which model to use for any given task without consulting upstream
- Cost stay within projected budget
- Vendor outages not stall work indefinitely
- Tier-1-eligible tasks consistently routed to free/cheap tier (cost saving)

If projects run with all-Tier-3 by default, this skill's value isn't being captured.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations: solo dev, regulated industries, on-prem-only, multi-vendor, cost-pressured projects.

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: routing policy for a typical mid-size SaaS migration project.

## Failure modes to avoid

- **All-Tier-3 default.** Wastes 3-5x cost. Force routing rubric on every task.
- **All-Tier-1 default.** Simple AI hallucinates on inference; costs more in operator review and rework.
- **Stale model list.** AI vendors release/deprecate models monthly. Review quarterly.
- **No fallback plan.** Vendor outages stall the team.
- **Single-vendor lock-in.** Easy until pricing changes or quality regresses.
- **No cost monitoring.** Without tracking, cost optimization is theoretical.
- **Ignoring data privacy.** Some tiers (free / cheap) may not have DPAs; can't be used for regulated data.
