---
name: work-package-decomposer
description: Decompose a single Work Package (WP) into micro-tasks suitable for AI agents to execute under human supervision. Each micro-task has a Tier (Simple/Mid/Strong AI), exact prompt, verification command, and expected output. Used by an Orchestrator AI to prepare an execution plan for an Executor AI. Use when a WP is approved for execution and operator wants to route tasks across AI tiers for cost optimization, when an AI agent needs to subdivide work for safety, or when generating Phase 3 Execution decomposition output. Triggers include "decompose this WP", "break WP into micro-tasks", "split work for AI execution", "prepare task list for Simple AI", or "Phase 3 Execution decompose".
---

# Work Package Decomposer

Take a single approved WP (from `implementation-planning` output) and break it into micro-tasks small enough that:
- Tier 1 (Simple AI) can execute mechanical tasks with prompt-only guidance
- Tier 2 (Mid AI) handles tasks requiring small inference
- Tier 3 (Strong AI) reserved for architecture/judgment tasks
- Operator (human) verifies each micro-task before continuing

## When this skill applies

Use when:
- A WP from `docs/03_EXECUTION/work-packages/PHASE_*.md` is approved for execution
- Operator wants to route tasks across AI tiers for cost optimization (~75% cost saving typical)
- An AI agent (Orchestrator) is preparing the task plan for an Executor AI
- Generating Phase 3 Execution decomposition output

Do NOT use for:
- Authoring WPs (use `implementation-planning`)
- Defining the protocol AI agents follow (use `ai-operator-protocol`)
- Defining which tier handles which task class (use `multi-tier-ai-routing` — that defines the policy; this skill applies it per WP)

## Inputs (must read first)

1. **The specific WP doc:** `docs/03_EXECUTION/work-packages/PHASE_<N>_*.md` Section for WP-X.Y
2. `docs/03_EXECUTION/AI_OPERATOR_GUIDE.md` — supervision protocol (or equivalent)
3. `docs/03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md` — tier policy (or equivalent)
4. `docs/03_EXECUTION/A_CODE_SNIPPETS.md` (if exists) — reusable patterns
5. **Source code** — for the files the WP affects (read but don't edit yet)

## Output

A task table appended to the WP section in PHASE_*.md OR a separate file `docs/03_EXECUTION/work-packages/decomposition/WP-<X.Y>_tasks.md`. Format follows [assets/TASK_DECOMPOSITION_template.md](assets/TASK_DECOMPOSITION_template.md).

The output is consumed by an Executor AI (Tier 1) for mechanical tasks; Mid AI (Tier 2) for moderate tasks; verified by operator at every step.

## Workflow

### Step 1 — Read the WP fully

Do NOT skim. Read:
- Goal
- Effort estimate
- Files affected
- Acceptance criteria
- Unit tests required
- Manual test cases
- Risks
- Rollback plan

If anything is unclear, STOP and request clarification — do not decompose ambiguous WPs.

### Step 2 — Choose decomposition mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — 3-tier AI routing** *(default)* | Standard multi-AI workflow | Tier 1 (Simple), Tier 2 (Mid), Tier 3 (Strong) |
| **B — Honor company AI tier policy** | Company has defined AI catalog (specific models per tier) | Company policy doc |
| **C — User-defined tier model** | User specifies (e.g., 2-tier "low/high"; or by model: "Gemini for X, Claude for Y") | User input |

Selection logic:
1. User explicit → use it
2. Company has AI catalog or governance doc → ask user
3. Default → Mode A

#### Mode A — 3-tier AI routing

| Tier | Symbol | Examples | Cost | Use cases |
|------|--------|----------|------|-----------|
| **Tier 1 — Simple AI** | 🟢 | Gemini Flash (free), Gemma 3 1B (local), GPT-4o-mini, Claude Haiku | Free or near-free | Mechanical: install commands, small file edits, boilerplate, format conversions |
| **Tier 2 — Mid AI** | 🟡 | Claude Sonnet, GPT-4o | Medium | Moderate inference: implementing a function from clear spec, writing tests, refactoring within a file |
| **Tier 3 — Strong AI** | 🔴 | Claude Opus, GPT-4 (or O1/O3) | Highest | Architecture, multi-file refactor, debugging hard issues, design decisions |
| **Human (operator)** | 👤 | n/a | $0 | Approval, push, decisions, ambiguity resolution |

Goal: route task to the cheapest tier that can do it correctly. Wrong tier = wasted money OR broken work.

### Step 3 — Identify task boundaries

Within a WP, look for natural task boundaries:

- **One file = one task** (when possible). If a WP touches 5 files, that's likely 5+ tasks.
- **One concept = one task.** Adding tests for a function = separate from implementing the function.
- **Mechanical vs. inferential.** "Install package X" (mechanical, Tier 1) vs. "Refactor function Y" (inferential, Tier 2-3).
- **Dependencies between tasks.** Some tasks must run before others (T2 depends on T1 output).

Aim for: 8-20 micro-tasks per WP. Less = under-decomposed; more = WP probably too big (split WP).

### Step 4 — Classify each task by tier

For each candidate task, ask:

**Tier 1 (Simple AI) if:**
- Task is mechanical (run command, copy template, format file)
- No design judgment required
- Verification is one shell command or `cat` of a file
- Risk of error is low; failure is obvious and recoverable

**Tier 2 (Mid AI) if:**
- Task requires reading existing code and modifying consistently
- Spec is clear; multiple correct implementations possible (but all equivalent)
- Risk of subtle error exists; verification requires reviewing diff

**Tier 3 (Strong AI) if:**
- Task involves architecture decision, multi-file coordination, hard debugging
- "How" is non-obvious or needs context beyond the WP
- Failure is hard to detect without thorough review

**Human (operator) if:**
- Approval gate (review code, sign off PR)
- Requires decision authority (security review, choice between options)
- Requires context AI can't see (ops state, customer feedback, business priority)

### Step 5 — Write a prompt per task (Tier 1 especially)

Tier 1 prompts must be **complete and self-contained**:

- Specify exact file path
- Specify exact change (don't say "improve"; say "add line X after line Y")
- Specify expected output format
- Provide context if needed (don't assume Simple AI has read the WP)

Bad Tier 1 prompt:
> "Add error handling to login.ts"

Good Tier 1 prompt:
> "In file `src/server/services/auth/login.ts`, after the line `const user = await db.users.findOne({email});`, add the following 3 lines:
> ```ts
> if (!user) {
>   throw new AppError('INVALID_CREDENTIALS', 401);
> }
> ```
> Output the full updated file content."

### Step 6 — Define verify command per task

Each task has a verify step the **operator runs** to confirm the AI did it right:

- File edit: `cat path/to/file.ts | grep "expected line"` or `git diff path/to/file.ts`
- Install: `npm ls <package>` or `npx <package> --version`
- Test: `npm run test -- <test-name>` and check output
- Code change: `npm run lint && npm run typecheck`

Verify commands must be deterministic — same input, same output. No "looks good?".

### Step 7 — Sequence tasks (dependency order)

Tasks have dependencies:

- T1 (install deps) → T2 (configure)
- T3 (write tests) ← depends on T2 (config exists)
- T4 (implement function) → T5 (verify tests pass with new function)
- T6 (run full test suite) ← depends on all previous

Document order. Parallelizable tasks marked.

### Step 8 — Estimate per-task effort

Per task, estimate AI execution time + operator verification time:

- Tier 1 task: ~5-10 min total (3-5 min AI + 2-5 min operator verify)
- Tier 2 task: ~15-30 min total
- Tier 3 task: ~30-60 min total
- Human task: variable

Sum per WP. If sum > original WP effort estimate, decomposition has overhead — review.

### Step 9 — Produce output table

Use [assets/TASK_DECOMPOSITION_template.md](assets/TASK_DECOMPOSITION_template.md). Output is a table:

| ID | Tier | Description | Prompt (full text) | Verify command | Expected output | Effort |
|----|------|-------------|--------------------|-----------------| ----------------|--------|
| WP-0A-T1 | 🟢 | Install package | "Run: npm install bcrypt@5.1.1" | `npm ls bcrypt` | `bcrypt@5.1.1` | 5min |

The table is consumed by the Orchestrator AI to coordinate execution; or printed by operator to drive Executor AI manually.

### Step 10 — Self-review

Run [references/checklist.md](references/checklist.md). Decomposition quality directly affects cost and safety.

## Quality bar

A good decomposition lets:
- An operator paste each Tier 1 prompt into a Simple AI without modification and get correct output
- Cost run in the operator's expected band (~75% saving vs. all-Tier-3)
- Each task's correctness be verified in <5 minutes by the operator
- No silent failures — if a task goes wrong, the verify command catches it before next task

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations: simple WPs (mostly Tier 1), complex WPs (heavy Tier 3), risky WPs (more verification gates), legacy code WPs (more Tier 2-3 reading).

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: decomposing WP-0.E (Error Boundaries) — typical Phase 0 WP with mostly Tier 1 work.

## Failure modes to avoid

- **Over-tiering.** "All Tier 3 because we want quality" — wastes money. Most WPs are 50-80% Tier 1 if decomposed honestly.
- **Under-tiering.** "All Tier 1 to save money" — Simple AI hallucinates on inference tasks; failures cascade.
- **Vague prompts.** Tier 1 prompts must be exact. "Refactor for clarity" is Tier 3 territory; Tier 1 needs "replace line X with Y".
- **Missing verify step.** Without verify, you don't know if the AI did the right thing. Always include verify command.
- **Wrong granularity.** WP intended for 1 PR shouldn't decompose into 50 micro-tasks; usually 8-20 is right.
- **Skipping operator approval gates.** Even within a WP, intermediate gates matter (e.g., after destructive task like file delete, operator must confirm before proceeding).
