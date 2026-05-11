# AI Operator Protocol — Worked Example

Anonymized. Fictional project: **"Project Voyager"** — logistics tracking platform mid-migration. 1 senior operator, 4 backend devs, mix of Claude + Gemini AIs.

## Context

**Imagined input:** "Author the AI Operator Guide for Voyager. We use Claude (Opus + Sonnet + Haiku) and Gemini Flash. We're in the middle of a 14-week migration. Operator is the lead backend engineer."

**Mode chosen:** Mode A (no existing AI governance policy).

---

## Output excerpt

```markdown
# Project Voyager — AI Operator Guide

> Last updated: 2026-09-15
> Owner: Lead Backend Engineer

## 1. The Operator's Role

The operator is responsible for...

## 2. Hard Rules

[Standard 7 + project-specific:]

| ID | Rule | Why | Enforced by |
|----|------|-----|-------------|
| H-1 | No autonomous commits | Standard | Operator habit + signed commits |
| H-2 | No PR merge by AI | Standard | GitHub branch protection |
| H-3 | One WP per PR | Standard | PR template requires WP-X.Y reference |
| H-4 | No scope drift | Standard | Diff review checklist |
| H-5 | No skipping tests | Standard | CI required checks |
| H-6 | No .env modification | Standard | Pre-commit hook + CODEOWNERS |
| H-7 | No production deploys | Standard | Deploy gated on operator manual run |
| LR-01 | Database migration changes require DBA in reviewers | Schema risk | PR template + label |
| LR-02 | Multi-region changes require infra-team in reviewers | Cross-region risk | CODEOWNERS for tf/regions/ |
| LR-03 | Auth/crypto changes require Security Lead | Security risk | CODEOWNERS for src/server/auth/ + src/lib/crypto/ |
| LR-04 | EU customer data changes require Compliance Lead | GDPR | Label `data-privacy` triggers reviewer |

## 3. The 14-Step Workflow

(Standard 14 steps applied per WP. Excerpt of one:)

### Step 12 — Operator: Review final diff

Operator runs:

```bash
git diff main...HEAD
```

Checklist:
- [ ] Every acceptance criterion in WP doc has an observable change addressing it
- [ ] No file changed outside WP "Files affected" list
- [ ] No `console.log`, `// TODO`, `// FIXME` added
- [ ] No `any` type added (Voyager uses strict TypeScript)
- [ ] No secrets / API keys / tokens visible
- [ ] No .env* files changed
- [ ] Imports cleaned (no unused)

If any check fails: AI fixes (or operator does, depending on cause); re-review.

## 4. Stop Conditions

(Standard 6 stop conditions; specific Voyager additions:)

7. **Replication lag check fails on data-touching changes** — Voyager has multi-region; any data change must verify replication monitor remains healthy
8. **Cross-region routing test fails** — for changes affecting routing layer
9. **Postgres logical replication slot warning** — should be 0; if non-zero, halt and investigate

## 5. Escalation Paths

(Standard escalations + Voyager-specific:)

| Voyager-specific scenario | First action | If still failing |
|---------------------------|--------------|-------------------|
| Replication lag spikes during WP execution | Pause WP; observe 5 minutes | If sustained >2 min, abort WP; switch to incident mode |
| EU region health check failing | Pause WP | If 5min sustained, treat as incident |
| Stripe webhook signature verification breaks (auth WP) | STOP immediately | Roll back any auth changes; verify Stripe sandbox first |

## 6. System Prompts

### 6.1 Orchestrator AI — system prompt for Voyager

```
You are the Orchestrator AI for Project Voyager (logistics tracking SaaS, mid-migration to multi-region).

ROLE: Plan + supervise. Read WPs, decompose, coordinate Executor AI, report to operator.

REQUIRED READING (before any task):
1. docs/03_EXECUTION/AI_OPERATOR_GUIDE.md (this protocol — your rules)
2. docs/02_STRATEGIC/MASTER_PLAN.md (the migration plan)
3. The specific WP doc for current task

HARD RULES (NEVER violate — these are non-negotiable):
1. No autonomous commits or pushes
2. No PR merge
3. One WP per PR
4. No scope drift outside WP "Files affected"
5. No skipping tests
6. No .env modifications
7. No production deploys
8. (Voyager-specific) DB migration changes → DBA in reviewers
9. (Voyager-specific) Multi-region changes → infra-team in reviewers
10. (Voyager-specific) Auth changes → Security Lead in reviewers

WORKFLOW per WP:
1. Read WP fully — confirm understanding by summarizing in 3 bullets
2. Plan: list files to change, tests to add, anticipated risks. Wait for operator approval.
3. Decompose into tasks (use `work-package-decomposer` skill patterns; produce task table with TIER per task)
4. Execute one task at a time; after each, present output for operator verification
5. Stop on any failure or anomaly; do NOT retry without operator authorization
6. After all tasks pass, present final diff
7. After operator approval, commit (operator pushes); open draft PR (operator merges)

OUTPUT FORMAT:
- Plan reports: bulleted lists; reference WP-X.Y
- Task results: structured (task ID, output, verify result)
- Stop reports: clear summary of what failed and proposed next action

START: confirm you've read this protocol. Await WP assignment.
```

### 6.2 Executor AI (Tier 1: Gemini Flash)

```
You are the Executor AI (Tier 1) for Project Voyager.

ROLE: Execute mechanical tasks the Orchestrator AI gives you. Produce exact outputs.

PER TASK YOU RECEIVE:
- A prompt (instructions)
- A verify command (operator runs to confirm correctness)
- Expected output (what you should produce)

DO:
- Execute the prompt EXACTLY
- Return the requested artifact (file content / command output / etc.)
- If the prompt says "create file at path X with EXACTLY this content", do that — do not modify

DO NOT:
- Add comments, explanations, or "improvements" the prompt didn't request
- Decide between options ("the user might want X or Y" — flag back to Orchestrator)
- Modify files not specified in prompt
- Run git commit, git push, or any destructive command

STOP if:
- Prompt is ambiguous
- File path doesn't exist (when prompt requires existing file)
- You'd need to make a creative judgment

Output the requested artifact in markdown if not specified otherwise. Be terse.
```

## 7. Progress Tracker (current state at example time)

| WP | Phase | Status | Operator | AI tier(s) | Started | Completed | Cost | Notes |
|----|-------|--------|----------|------------|---------|-----------|------|-------|
| WP-0.0 | 0 | Done | Lead BE | Tier3 | 2026-09-01 | 2026-09-03 | $4.50 | Server restructure (1.5d) |
| WP-0.A | 0 | Done | Lead BE | Tier1+Tier2 | 2026-09-04 | 2026-09-04 | $0.85 | Migrate auth tokens to httpOnly |
| WP-0.B | 0 | In progress | Lead BE | Tier1 | 2026-09-05 | — | $0.05 | Axios upgrade — at T7 awaiting test run |
| WP-0.C | 0 | Pending | — | — | — | — | — | Awaiting WP-0.A merge confirmation in staging |
| WP-0.D | 0 | Blocked | — | — | — | — | — | OQ-1 — DBA confirming Postgres logical replication compat |

Phase 0 cost-to-date: $5.40 (vs $40 estimated all-Tier-3 baseline; ~85% saving).

## 8. Cost Monitoring

Voyager Phase 0 budget: ~$60 total (estimated). Halfway through, $5.40 spent. **Trending under budget by ~80%.**

If individual WP exceeds 2x estimate (e.g., WP-0.B was estimated $0.50 but at $2 → investigate).

## 9. Failure Scenarios (Voyager-specific examples)

| Scenario | Detection | Recovery |
|----------|-----------|----------|
| AI changes Postgres replication config without DBA approval | Diff shows `tf/regions/` changes; CODEOWNERS flag in PR | Revert; reassign WP with explicit DBA pair |
| AI commits with secret in `.env.example` | Pre-commit hook catches; OR diff review | Revert; rotate secret if any chance leaked |
| Tier 1 AI outputs wrong file path (hallucinates path that doesn't exist) | Verify command `cat <path>` fails | Retry with explicit context; if fails twice, escalate to Tier 2 |
| Tests fail after AI's change to `auth/` (security-sensitive) | CI red | STOP; full WP rollback; investigate before retry |
| AI proposes a fix for failing test that hides bug rather than fixes | Operator notices test no longer asserts what it should | Reject; require AI to revert + re-attempt |

## 10. Onboarding (Voyager)

For a new operator:

1. Read this guide (45 min)
2. Read docs/02_STRATEGIC/MASTER_PLAN.md (15 min)
3. Pair on 1 WP with Lead BE (2 hours)
4. Execute WP solo: pick a Phase 1 WP (Quick Wins are well-bounded; ~3 hours)
5. After 3 solo WPs, ready for Phase 2-3 work

## 11. Retrospectives

Phase 0 retro held 2026-09-08 (mid-phase):
- ✅ Cost tracking working; well under budget
- ✅ Tier 1 (Gemini Flash) handled 60%+ of tasks reliably
- ⚠️ Tier 1 occasionally outputs invalid TS syntax → Always verify with `tsc --noEmit` after Tier 1 task
- ⚠️ Operator gate frequency (every task) feels heavy → Trial: gate every 2-3 tasks for routine sequences
- 📋 Action: Update Section 4 Stop Conditions to include "Tier 1 produces TS that doesn't compile"
```

---

## Calibration notes

- **Project-specific rules tied to actual reviewers.** LR-01 (DBA on migrations) requires actual DBA + working CODEOWNERS. Don't write rules that can't be enforced.
- **Cost tracking shows ~85% saving.** This is realistic for projects routing well.
- **Retrospective findings update the guide.** "Tier 1 occasional bad TS" became a new stop condition. The guide is living.
- **System prompts are real (no placeholders).** Operator can copy them as-is into their AI tool.
- **Onboarding has time estimates.** "45 min to read" sets expectations; doesn't pretend a 200-line guide is 5 minutes.
- **Failure scenarios are Voyager-specific.** Generic guide says "AI commits without approval"; Voyager guide adds "AI changes tf/regions/" and "AI hides bug in test".
- **Phase 0 cost transparency.** $5.40 to date out of $60 budget — operator can defend the project's AI spend with this data.
