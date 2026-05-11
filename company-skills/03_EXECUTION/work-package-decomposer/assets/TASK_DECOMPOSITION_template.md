# WP-{{X.Y}} — Task Decomposition

> **Purpose:** Micro-task plan for executing WP-{{X.Y}} via multi-tier AI workflow.
> **Source WP:** `docs/03_EXECUTION/work-packages/PHASE_<N>_*.md` Section WP-{{X.Y}}
> **Decomposition mode:** {{A — 3-tier / B — Honor company policy / C — User-defined}}
> **Generated using:** `work-package-decomposer` skill v1
> **Author (operator):** {{NAME}}
> **Date:** {{YYYY-MM-DD}}

---

## Context (from WP)

- **Goal:** {{COPY_FROM_WP}}
- **Effort estimate:** {{COPY_FROM_WP}}
- **Files affected:** {{COPY_FROM_WP}}
- **Acceptance criteria:** {{SUMMARIZE — full list in WP doc}}

---

## Tier Distribution Summary

| Tier | Count | Estimated time |
|------|-------|----------------|
| 🟢 Tier 1 (Simple AI) | {{N}} | {{N × 5-10min}} |
| 🟡 Tier 2 (Mid AI) | {{N}} | {{N × 15-30min}} |
| 🔴 Tier 3 (Strong AI) | {{N}} | {{N × 30-60min}} |
| 👤 Human | {{N}} | variable |
| **Total tasks** | **{{N}}** | **{{TOTAL}}** |

(Healthy distribution for a typical Phase 0/1 WP: 50-70% Tier 1, 20-30% Tier 2, 5-15% Tier 3 + human gates.)

---

## Task Sequence

### Sequential (each depends on previous)

```
T1 ──> T2 ──> T3 ──> T4 ──> T5 ──> ...
```

### Parallel

Tasks marked **[P]** can run in parallel with others marked **[P]** at the same level.

---

## Task Table

| ID | Tier | Description | Prompt (full text for Tier 1, summary for higher) | Verify command | Expected output | Effort |
|----|------|-------------|---------------------------------------------------|----------------|-----------------|--------|
| WP-{{X.Y}}-T1 | 🟢 | {{e.g., Install dependency}} | `Run command: npm install bcrypt@5.1.1 --save-prod. Output the resulting package.json line for "bcrypt".` | `npm ls bcrypt` | `bcrypt@5.1.1` | 5min |
| WP-{{X.Y}}-T2 | 🟢 | {{e.g., Create new file with fixed content}} | `Create file at path src/server/services/auth/passwordHash.ts with EXACTLY this content:\n\n\`\`\`ts\nimport bcrypt from 'bcrypt';\n\nexport async function hashPassword(plain: string): Promise<string> {\n  return bcrypt.hash(plain, 12);\n}\n\nexport async function verifyPassword(plain: string, hash: string): Promise<boolean> {\n  return bcrypt.compare(plain, hash);\n}\n\`\`\`\n\nOutput the file path after creation.` | `cat src/server/services/auth/passwordHash.ts` | File matches exactly | 5min |
| WP-{{X.Y}}-T3 | 🟡 | {{e.g., Update existing function to use new helper}} | (Mid AI: detailed inference task) "In src/server/services/auth/login.ts, replace the inline `bcrypt.compare(...)` call (around line 28) with a call to `verifyPassword` imported from `./passwordHash`. Add the import statement at the top of the file." | `git diff src/server/services/auth/login.ts` | Diff shows: import added; bcrypt.compare replaced with verifyPassword call | 20min |
| WP-{{X.Y}}-T4 | 🟢 | {{e.g., Run tests}} | `Run: npm run test -- auth.spec.ts. Output last 30 lines of output.` | (operator reviews output) | All tests pass | 5min |
| WP-{{X.Y}}-T5 | 🟢 | {{e.g., Run linter}} | `Run: npm run lint. Output last 20 lines.` | (operator reviews) | 0 errors | 3min |
| WP-{{X.Y}}-T6 | 👤 | {{e.g., Operator reviews diff}} | (Human task) Review full diff: `git diff` | n/a | Operator approves diff | 10min |
| WP-{{X.Y}}-T7 | 🟢 | {{e.g., Commit}} | `Run: git add -A && git commit -m "WP-{{X.Y}}: <description>"` | `git log -1 --oneline` | Commit shown | 3min |
| ... | ... | ... | ... | ... | ... | ... |

---

## Detailed Tier 1 Prompts

For Tier 1 tasks (🟢), prompts must be self-contained and copy-pasteable into Simple AI without modification. If a Tier 1 task's prompt requires reference to other files or context, escalate to Tier 2.

### T{{N}} (🟢) — Full prompt

```
{{COPY_PASTE_READY_PROMPT_FOR_SIMPLE_AI}}
```

**Verify after AI responds:** {{COMMAND}}
**If verify fails:** {{e.g., "Re-run task with prompt; if fails twice, escalate to Tier 2"}}

(Repeat for each Tier 1 task)

---

## Tier 2/3 Task Specifications

Tier 2/3 tasks are inference-heavy; provide context, not exact commands.

### T{{N}} (🟡 / 🔴) — Specification

**Goal:** {{WHAT_TO_ACCOMPLISH}}
**Context to provide AI:**
- WP-{{X.Y}} section from PHASE doc
- Relevant existing code: {{LIST_FILES}}
- Relevant patterns: `docs/03_EXECUTION/A_CODE_SNIPPETS.md` Section {{}}

**Constraints:**
- Files MAY be modified: {{LIST}}
- Files MUST NOT be modified: {{LIST}}
- Acceptance criteria: {{LIST_FROM_WP}}

**Verification approach:** {{HOW_OPERATOR_CONFIRMS_QUALITY}}

(Repeat for each Tier 2/3 task)

---

## Operator Approval Gates

Operator must approve before proceeding past:

- [ ] **Gate 1:** After T{{N}} (typically after destructive operations — file delete, schema change, config change)
- [ ] **Gate 2:** Before T{{N}} (typically before commit/push)
- [ ] **Gate 3 (final):** Before opening PR

Gates are mandatory; AI must not skip them.

---

## Failure / Stop Conditions

The Executor AI must STOP and request operator input if:

1. A verify command fails twice for the same task
2. A Tier 1 task's prompt produces unexpected output (e.g., AI invents content not in prompt)
3. A test fails that wasn't expected to fail
4. AI encounters file/path that doesn't exist (likely scope drift)
5. Diff includes changes outside the WP's "Files affected" list (scope creep)

Operator decides: retry / escalate tier / abort WP.

---

## Cost Estimate

Estimated cost per execution:

| Tier | Tasks | Avg prompt+output tokens | Cost/1M tokens | Total cost |
|------|-------|---------------------------|-----------------|------------|
| 🟢 Tier 1 (e.g., Gemini Flash free) | {{N}} | ~2K | $0 (free tier) | $0 |
| 🟡 Tier 2 (e.g., Claude Sonnet) | {{N}} | ~10K | $3 input / $15 output | {{$X}} |
| 🔴 Tier 3 (e.g., Claude Opus) | {{N}} | ~30K | $15 input / $75 output | {{$X}} |
| **Total** | | | | **{{$X}}** |

(Compare to all-Tier-3 cost — typically ~3-5x higher.)

---

## Notes

- **Decomposition mode:** {{A / B / C}}
- **Confidence:** {{HIGH/MEDIUM/LOW — based on WP clarity}}
- **WP dependencies satisfied?:** {{Yes / No — if WP-X depends on WP-Y still pending, note}}
- **Ready for execution:** {{Yes after operator review / No because…}}

---

*This decomposition is consumed by the Orchestrator AI (or operator manually). Executor AI follows the task table sequentially. After each task, operator runs verify command before authorizing next task.*
