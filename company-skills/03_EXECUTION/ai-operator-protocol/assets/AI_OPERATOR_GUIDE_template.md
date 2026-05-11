# {{PROJECT_NAME}} — AI Operator Guide

> **Purpose:** Manual for human operators supervising AI agents during work-package execution.
> **Audience:** Operator (human), AI agents (read system prompt section), team members onboarding to AI workflows.
> **Last updated:** {{YYYY-MM-DD}}
> **Generated using:** `ai-operator-protocol` skill v1
> **Owner:** {{NAME — operator lead}}

---

## 1. The Operator's Role

The **operator** is the human in charge of:
- Selecting which WP runs next
- Approving AI plans before execution
- Verifying each task output before next task starts
- Approving final diff before commit
- Approving PR for merge
- Tracking cost and progress
- Escalating to higher AI tiers or humans when needed

The operator is NOT a coder during execution — they review and approve. If they need to code mid-WP, that's a sign the WP failed or AI got stuck; reset and re-plan.

---

## 2. Hard Rules (NEVER violate)

These rules apply to every WP. Violations are CRITICAL incidents.

1. **No autonomous commits or pushes.** AI never runs `git commit` or `git push` without explicit operator approval.
2. **No PR merge by AI.** Operator merges; AI may open draft PR.
3. **One WP per PR.** Never combine multiple WPs into a single PR.
4. **No scope drift.** AI modifies ONLY files listed in WP "Files affected". Any other file change = scope drift = STOP.
5. **No skipping tests.** Every WP runs unit + manual TCs before commit.
6. **No secrets / .env modifications.** `.env*` files are operator-managed only.
7. **No production deploys.** Even with green CI, operator deploys.

### Project-specific rules

| ID | Rule | Why | Enforced by |
|----|------|-----|-------------|
| LR-01 | {{e.g., "PHI-handling code requires Compliance Lead in PR reviewers"}} | {{HIPAA/SOC2}} | PR template + reviewer assignment |
| LR-02 | {{e.g., "Auth/crypto changes require Security Lead sign-off"}} | {{Security risk}} | PR labels + branch protection |
| LR-03 | {{...}} | {{...}} | {{...}} |

---

## 3. The 14-Step Workflow (per WP)

### Step 1 — Operator: Select WP

From `docs/02_STRATEGIC/MASTER_PLAN.md`, identify the next WP to execute. Verify dependencies satisfied.

### Step 2 — Operator: Provide WP doc to AI

Tell the AI agent: "Execute WP-{{X.Y}}. The WP doc is at `docs/03_EXECUTION/work-packages/PHASE_<N>_*.md` Section WP-{{X.Y}}."

### Step 3 — AI: Read WP fully

AI must read the full WP doc. **No skim mode.** If WP is unclear, AI must ask operator before continuing.

### Step 4 — AI: Report plan

AI summarizes:
- Files to modify
- Test changes needed
- Estimated effort
- Anticipated risks

This is BEFORE coding. Operator reviews this plan.

### Step 5 — Operator: Review plan

Operator confirms plan matches WP intent. If wrong, revise prompt or ask AI to re-read WP.

### Step 6 — AI: Decompose into tasks

AI applies `work-package-decomposer` skill. Output is a task table with tiers, prompts, verify commands.

### Step 7 — Operator: Review tasks

Operator approves task list. Particularly check Tier 1 prompts are concrete (not "improve X").

### Step 8 — AI: Execute task N

Per the decomposition, AI executes one task. Output produced.

### Step 9 — Operator: Verify task N

Operator runs the verify command from the task. Pass → continue. Fail → halt; retry or escalate.

### Step 10 — Loop steps 8-9

Continue until all tasks complete OR a stop condition triggers.

### Step 11 — AI: Run full test + lint

After all tasks done, AI runs `npm test`, `npm run lint`, `npm run typecheck` (or equivalents). Output for operator review.

### Step 12 — Operator: Review final diff

Operator runs `git diff` and reviews. Checks:
- Acceptance criteria all met (cross-check vs WP doc)
- No scope drift (only files in "Files affected" changed)
- No `console.log` / `// TODO` left
- No secrets in diff

### Step 13 — Operator-mediated: Commit

Operator approves; AI runs `git commit -m "[WP-{{X.Y}}] <description>"`. Operator runs `git push`.

### Step 14 — Operator: Open PR

Operator runs `gh pr create` with PR description per template. Assigns reviewers per project-specific rules.

---

## 4. Stop Conditions (AI MUST halt)

The Executor AI must stop and request operator input when:

1. **Verify command fails twice** for the same task
2. **Tier 1 prompt produces unexpected output** (AI invents content not in prompt)
3. **Test fails unexpectedly** (test that should pass, doesn't)
4. **File path doesn't exist** (likely scope drift)
5. **Diff includes changes outside "Files affected"** list
6. **Hard rule potentially violated** (e.g., AI is asked to commit without approval)

Stop condition triggers: AI summarizes situation, awaits operator decision (retry / escalate / abort).

---

## 5. Escalation Paths

| Scenario | First action | If still failing |
|----------|--------------|-------------------|
| Tier 1 task fails (output wrong) | Re-prompt with more context | Escalate to Tier 2 |
| Tier 2 task produces inconsistent diffs | Add more context to prompt | Escalate to Tier 3 OR human review |
| AI cannot resolve ambiguity | Operator clarifies; updates WP if needed | Pause WP; convene mini-meeting |
| Production incident during execution | Pause WP immediately | Switch to incident-response mode (see runbook) |
| AI requests modify outside scope | DENY | Investigate why scope is wrong; revise WP |
| Cost overrun (>2x estimate) | Pause; investigate where cost concentrated | Revise decomposition; possibly split WP |

---

## 6. System Prompts for AI Agents

### 6.1 Orchestrator AI (Tier 3) — system prompt template

```
You are the Orchestrator AI for {{PROJECT_NAME}} implementation.

ROLE: Plan + supervise. Read WPs, decompose into tasks, coordinate with the Executor AI,
report to the human operator.

REQUIRED READING (in order):
1. docs/03_EXECUTION/AI_OPERATOR_GUIDE.md (this protocol)
2. docs/02_STRATEGIC/MASTER_PLAN.md
3. The specific WP doc for the current task

HARD RULES (NEVER violate):
1. No autonomous commits or pushes
2. No PR merge
3. One WP per PR
4. No scope drift outside WP "Files affected"
5. No skipping tests
6. No .env modifications
7. No production deploys

WORKFLOW per WP:
1. Read WP fully
2. Report plan to operator BEFORE coding
3. Wait for operator approval
4. Decompose into tasks (TIER classified) per `work-package-decomposer` patterns
5. Wait for operator approval of task list
6. Direct Executor AI through tasks one at a time
7. After each task, present output for operator verification
8. Stop on any failure; do not retry without operator authorization
9. After all tasks pass, present final diff for operator approval
10. Open PR (operator approves merge)

OUTPUT FORMAT:
- Short, structured updates to operator
- Plan reports as bulleted lists
- Task results as table rows or per-task summaries
- Always cite WP-X.Y when referring to the current task

START: Confirm you've read this protocol; await WP assignment from operator.
```

### 6.2 Executor AI (Tier 1-2) — system prompt template

```
You are the Executor AI for {{PROJECT_NAME}}.

ROLE: Execute mechanical and inferential tasks given by the Orchestrator AI; produce
outputs the operator can verify; STOP and request operator input on any anomaly.

REQUIRED READING per task:
- The task spec (prompt + verify + expected output)
- The relevant code file (if task modifies code)

HARD RULES:
- Do EXACTLY what the prompt specifies — no creative additions
- If unsure, say so; do NOT improvise
- After completion, return output in format requested
- If you produce a diff, only modify the files specified

STOP CONDITIONS:
- Cannot find file specified in prompt
- Prompt is ambiguous or contradictory
- Verify command would fail (you can predict failure)

OUTPUT: respond with the requested artifact (file content, command output, diff).
Do not add commentary unless asked.
```

### 6.3 Reviewer AI (optional Tier 2-3) — system prompt template

```
You are a code reviewer for {{PROJECT_NAME}}.

ROLE: Review diffs against WP acceptance criteria.

REQUIRED READING:
- The WP doc (acceptance criteria)
- The diff under review

CHECKS:
1. Every acceptance criterion met (cross-reference each)
2. No scope drift (changes only in "Files affected")
3. No code smells: console.log left, TODOs added, hardcoded values
4. No secrets in diff
5. Tests added/updated per WP unit test plan

OUTPUT: bullet list of findings; severity per finding; recommended action.

DO NOT: approve PR or merge. Only report findings.
```

---

## 7. Progress Tracker (template)

Maintain `PROGRESS_TRACKER.md` updated daily:

| WP | Phase | Status | Operator | AI tier(s) | Started | Completed | Cost | Notes |
|----|-------|--------|----------|------------|---------|-----------|------|-------|
| WP-0.0 | 0 | Done | {{NAME}} | Tier3 | 2026-09-01 | 2026-09-02 | $4.50 | Server restructure |
| WP-0.A | 0 | In progress | {{NAME}} | Tier1 + Tier2 | 2026-09-02 | — | $0.30 | At T7; awaiting operator review |
| WP-0.B | 0 | Blocked | — | — | — | — | — | OQ-2 — needs Compliance review |

Status values: **Pending / Planning / In progress / Awaiting review / Done / Blocked / Aborted**.

---

## 8. Cost Monitoring

### Per-WP cost tracking

Operator records cost per WP in `PROGRESS_TRACKER.md`. Anomaly thresholds:

- **>2x estimate** → investigate; likely decomposition routed too many tasks to high tier
- **>5x estimate** → halt; review with team

### Aggregate cost

| Phase | Estimated total | Actual to date | Variance |
|-------|-----------------|----------------|----------|
| 0 | {{$X}} | {{$Y}} | {{%}} |
| 1 | {{$X}} | {{$Y}} | {{%}} |

### Cost reduction signals

- High Tier 1 percentage (≥60%) → good
- Tier 3 only for genuine architecture work → good
- Operator gates not too frequent (gates × time has overhead) → good

---

## 9. Failure Scenarios + Recovery

| Scenario | Detection | Recovery |
|----------|-----------|----------|
| AI hallucinates a file change | Operator notices in diff review (file not requested) | Reject; re-run with corrective prompt |
| AI gets stuck in loop (same wrong output) | Same task fails twice with same error | Stop; escalate tier OR rewrite prompt |
| Test fails after AI's "fix" of another failure | Test suite runs longer than baseline | Stop; manual intervention; possibly revert AI's changes |
| AI skips an approval gate | Operator notices missing artifact | Revert; tighten enforcement; root-cause analysis |
| AI commits without approval | git log shows unapproved commit | CRITICAL: revert commit, investigate prompt/system, possibly retire model from project |
| Operator misses a defect; PR merged with bug | Production monitoring catches OR customer reports | Standard incident response; retro: why review missed it |

---

## 10. Onboarding a New Operator

For someone new to AI-supervised execution:

1. Read this guide end-to-end (~30 min)
2. Read `docs/02_STRATEGIC/MASTER_PLAN.md` to understand scope (~15 min)
3. Shadow an experienced operator on 1 WP (1-2 hours)
4. Execute first WP under supervision: pick a small, well-bounded WP (2-4 hours)
5. Solo on subsequent WPs

If operator has no AI background, additional reading: how to write good prompts, how to spot hallucinations, how to verify AI output.

---

## 11. Retrospectives

After each phase:

- What worked? (capture in this guide for next phase)
- What didn't work? (capture; revise rules / escalation as needed)
- Cost: actual vs estimate; calibrate decomposition for future WPs
- AI behavior: any new failure modes? Add to Section 9.

Update this guide quarterly minimum.

---

## 12. Notes

- **Protocol mode:** {{A — Standard 14-step / B — Honor company / C — User-defined}}
- **Mode rationale:** {{WHY}}
- **Scope:** Used for WP execution; not for free-form AI exploration or research tasks
- **Last reviewed:** {{YYYY-MM-DD}} by {{NAME}}

---

*This protocol is the safety net for AI-assisted execution. Operators who skip it discover why it exists the hard way.*
