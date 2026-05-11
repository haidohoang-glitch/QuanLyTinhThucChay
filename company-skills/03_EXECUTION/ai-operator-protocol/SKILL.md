---
name: ai-operator-protocol
description: Author the AI Operator Guide — the supervision protocol that defines how a human operator coordinates AI agents executing work packages. Includes hard rules (no autonomous merges, no scope creep), the 14-step per-WP workflow, system prompt templates, escalation paths, and stop conditions. Produces AI_OPERATOR_GUIDE.md customized to a specific project. Use when starting AI-assisted execution of a project, when standardizing operator practices across projects, or when generating Phase 3 Execution operator output. Triggers include "create operator guide", "AI supervision protocol", "how do humans supervise AI agents", "author AI_OPERATOR_GUIDE", or "Phase 3 Execution protocol".
---

# AI Operator Protocol

Author `AI_OPERATOR_GUIDE.md` — the protocol document that defines how a human operator supervises AI agents executing work packages safely. This skill produces the operator manual; the actual supervision uses the manual at runtime.

## When this skill applies

Use when:
- Starting AI-assisted execution on a project
- Standardizing operator practices across multiple projects
- Onboarding a new operator to AI-supervised workflows
- Producing Phase 3 Execution operator output for the company doc standard

Do NOT use for:
- Defining tier policy (use `multi-tier-ai-routing`)
- Decomposing a specific WP (use `work-package-decomposer`)
- Authoring SRS or requirements (use Phase 0 skills)

## Inputs

1. `docs/02_STRATEGIC/MASTER_PLAN.md` — phases + WPs the operator supervises
2. `docs/03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md` (or equivalent) — tier policy
3. **Team context:** who is the operator? Senior engineer? Tech lead? Skill level?
4. **AI tools available:** which models/services in scope (informs prompt templates)
5. **Risk profile:** regulated industry? Production access? Customer impact?

## Output

`docs/03_EXECUTION/AI_OPERATOR_GUIDE.md`, filled from [assets/AI_OPERATOR_GUIDE_template.md](assets/AI_OPERATOR_GUIDE_template.md).

The output is read by:
- Human operator: protocol manual at runtime
- AI agents: system prompt context (sections relevant to AI behavior)
- New team members: onboarding to AI-supervised workflows

## Workflow

### Step 1 — Establish hard rules

Hard rules are non-negotiable boundaries. Without them, AI agents creep beyond intent. The standard 7 rules:

1. **No autonomous commits or pushes** — operator approves every commit
2. **No PR merge by AI** — operator merges; AI may open PR draft
3. **One WP per PR** — never combine work packages
4. **No scope drift** — AI modifies only files listed in WP "Files affected"
5. **No skipping tests** — every WP runs unit + manual TCs before commit
6. **No secrets / .env modifications** — `.env*` files are operator-managed
7. **No production deploys** — even with green CI, operator deploys manually

These are STARTING rules. Add project-specific rules in Step 4.

### Step 2 — Choose protocol mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — Standard 14-step workflow** *(default)* | No existing protocol | This skill's standard workflow |
| **B — Honor company AI governance policy** | Company has formal AI usage policy / playbook | Company policy doc |
| **C — User-defined protocol** | Specific operator style preferred | User input |

Selection logic:
1. User explicit → use it
2. Company has AI governance → ask user (Mode A or B?)
3. Default → Mode A

#### Mode A — Standard 14-step per-WP workflow

```
1. Operator: select WP from MASTER_PLAN
2. Operator: provide AI agent the WP doc path
3. AI: read WP fully (do NOT skim)
4. AI: report plan (files, tests, estimated effort) BEFORE coding
5. Operator: review plan; approve or revise
6. AI: decompose WP into tasks (run `work-package-decomposer` skill)
7. Operator: review task list; approve
8. AI: execute task 1 (Tier per decomposition)
9. Operator: run verify command for task 1; approve or retry
10. AI: execute next task (loop steps 8-9 until all tasks done)
11. AI: run full test suite + lint
12. Operator: review final diff; approve
13. AI: commit (single commit with WP-X.Y prefix); operator pushes
14. Operator: open PR; assign reviewers; track to merge
```

Each step has stop conditions if expected outcome doesn't occur.

#### Mode B / C — adapt as appropriate

### Step 3 — Define escalation paths

When something doesn't go as planned, operator needs clear escalation:

| Scenario | Action |
|----------|--------|
| Tier 1 task fails twice | Escalate to Tier 2 |
| Tier 2 task produces wrong output | Escalate to Tier 3 OR human |
| AI cannot resolve ambiguity in WP | Operator clarifies or pauses WP |
| Test fails unexpectedly | STOP; debug before next task |
| AI requests permission to modify file outside scope | DENY; investigate scope correctness |
| Production incident during WP execution | Pause WP; switch to incident-response mode |

Document each scenario explicitly.

### Step 4 — Add project-specific rules

Beyond the standard 7, projects may need:

- **Regulated industries:** "All changes affecting PHI must include compliance reviewer in PR"
- **Multi-team:** "Cross-team changes require team-X approver"
- **Security-critical:** "Auth/crypto changes require Security Lead sign-off"
- **Customer-facing:** "UI changes require visual regression test before merge"

Add these to the hard rules list. Document why each project-specific rule exists (so future operators understand).

### Step 5 — Provide system prompt templates

AI agents need consistent system prompts. Provide templates:

- **Orchestrator AI (Tier 3) system prompt** — defines its role: read WP, plan, decompose, supervise Executor
- **Executor AI (Tier 1-2) system prompt** — defines its role: execute mechanical tasks, follow operator gates, never modify outside WP scope
- **Reviewer AI (optional, Tier 2-3) system prompt** — code review role

Each template includes:
- Role definition
- Required reading (which docs to read first)
- Hard rules (verbatim)
- Stop conditions
- Output format expected

### Step 6 — Define progress tracking

Operator needs to track WP status. Provide template for `PROGRESS_TRACKER.md`:

| WP | Phase | Status | Operator | AI agent(s) | Started | Completed | Cost | Notes |
|----|-------|--------|----------|-------------|---------|-----------|------|-------|
| WP-0.A | 0 | Done | Op1 | Tier3+Tier1 | 2026-09-01 | 2026-09-02 | $1.20 | |
| WP-0.B | 0 | In progress | Op1 | Tier1 | 2026-09-02 | — | — | Awaiting human review of T6 |

### Step 7 — Document failure scenarios + recovery

Common scenarios + recovery:

- **AI hallucinates a file change** → operator notices in diff review → reject; re-run with corrective context
- **AI gets stuck in loop** → operator stops; switches tier or revises prompt
- **Test fails, AI proposes fix → fix breaks something else** → operator stops; manual intervention or escalates to Tier 3
- **AI skips a step** → operator detects via missing artifact; reverts; re-run
- **AI commits without approval** → CRITICAL violation; revert commit; review what enabled the violation; tighten rules

### Step 8 — Cost monitoring

How operator tracks cost per WP:

- Per-task cost (from decomposition output)
- Aggregate per WP
- Aggregate per phase
- Anomaly thresholds (>2x estimate → investigate)

Document cost-monitoring approach in operator guide.

### Step 9 — Self-review

Run [references/checklist.md](references/checklist.md). Operator guide affects every WP execution; rigor matters.

## Quality bar

A good operator guide lets:
- A new operator execute their first WP within 1 hour of reading
- An existing operator know what to do in any escalation scenario without re-thinking from scratch
- An AI agent given the system prompt template behave consistently
- A retrospective trace what went right or wrong using PROGRESS_TRACKER

If the guide leaves room for "I'll figure that out as I go", it's incomplete.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations: solo operator vs. team, single AI vendor vs. multi, regulated industry, high-security projects, junior vs. senior operator.

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: operator guide for a typical migration project with 4 backend devs and 1 senior operator.

## Failure modes to avoid

- **Permissive rules.** "AI may merge if tests pass" — no. Always operator-merges. Hard rules must be hard.
- **Vague escalation.** "If something goes wrong, escalate" — to whom? What process? Be specific.
- **No cost monitoring.** AI cost can blow up unnoticed; track per-WP.
- **Assuming senior operator.** Junior operators need more scaffolding; document accordingly.
- **Single-AI-vendor lock-in.** Most projects use multiple AI tools; system prompts should work across them where possible.
- **Stale system prompts.** AI capabilities change; review prompts quarterly.
- **No retrospective process.** After each phase, operator should review what worked + what didn't; document in operator guide for next phase.
