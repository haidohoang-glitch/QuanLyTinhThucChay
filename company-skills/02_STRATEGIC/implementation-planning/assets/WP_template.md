# WP-{{X.Y}} — {{TITLE}}

> Empty WP template. Copy into PHASE_<N>_<NAME>.md as a section. Fill every placeholder.

**Goal:** {{ONE_SENTENCE — what this WP changes in the system}}

**Effort:** {{XS (<2h) / S (2-8h) / M (1-3 days) / L (>3 days, consider splitting)}}

**Owner:** {{Backend dev / Frontend dev / DevOps / specific person — defaults to role if unassigned}}

**Dependencies:**
- WP-{{X.Y}} (hard — must merge before this starts)
- WP-{{X.Y}} (soft — easier after, not blocking)
- (none) (if this WP can start anytime)

**Background / Why:**
{{1-2 SENTENCES — what problem this WP addresses, link to TECH_DEBT_AUDIT finding ID or similar}}

---

## Files affected

| File | Action | Why |
|------|--------|-----|
| `{{PATH}}` | {{Create / Modify / Delete / Rename}} | {{WHAT_CHANGES}} |

If files affected exceed ~10, the WP is probably too big. Split.

---

## Acceptance criteria

Each must be observable (testable or smoke-testable). Vague criteria are forbidden.

- [ ] {{CRITERION_1 — e.g., "All `fetch` calls in src/api/ have an explicit timeout via AbortController"}}
- [ ] {{CRITERION_2 — e.g., "Test `users.spec.ts` passes including new test 'rejects expired token'"}}
- [ ] {{CRITERION_3 — e.g., "TypeScript compile passes with strict mode in src/server/auth/"}}

---

## Unit tests

New tests added by this WP:

| Test name | Test file | What it verifies |
|-----------|-----------|------------------|
| {{TEST_NAME}} | `tests/unit/{{PATH}}.test.ts` | {{ASSERTION}} |
| {{TEST_NAME}} | `tests/unit/{{PATH}}.test.ts` | {{ASSERTION}} |

Existing tests that must still pass: `npm run test` (full suite).

---

## Manual test cases

Reproducible scenarios for human reviewer / QA:

| TC ID | Scenario | Expected outcome |
|-------|----------|------------------|
| TC-{{X}}{{Y}}-01 | {{SETUP_AND_ACTION}} | {{OBSERVABLE_OUTCOME}} |
| TC-{{X}}{{Y}}-02 | {{...}} | {{...}} |

---

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| {{RISK}} | {{L/M/H}} | {{MITIGATION}} |

If a risk has high likelihood AND high impact, consider splitting WP or adding precursor WP to de-risk.

---

## Rollback plan

If this WP causes production issues after merge:

1. {{STEP_1 — e.g., "Disable feature flag `enable_new_auth`"}}
2. {{STEP_2 — e.g., "Verify old path resumes via Sentry monitoring"}}
3. {{STEP_3 — e.g., "If flag insufficient, `git revert <commit>` and re-deploy"}}

If rollback requires data migration reverse:
- Forward migration: `migrations/{{ID}}_up.sql`
- Reverse migration: `migrations/{{ID}}_down.sql`
- Data preservation: {{HOW_DATA_IS_PRESERVED_OR_LOST_DURING_REVERSE}}

---

## PR conventions

**Title:** `[Phase {{X}}][WP-{{X}}.{{Y}}] {{SHORT_DESCRIPTION}}`

**Branch:** `feature/phase-{{X}}-wp-{{Y}}-{{kebab-slug}}`

**PR description should include:**
- Reference to WP-{{X}}.{{Y}} in this doc
- Acceptance criteria checklist (copy from above)
- Manual test results (TC IDs and pass/fail)
- Screenshot or output sample if user-visible

---

## AI agent execution notes

When an AI agent executes this WP:

- Read the WP fully before starting (do NOT skim)
- Plan changes before coding; report plan to operator for approval
- Make changes only in files listed under "Files affected"
- Run unit tests after each file edit; do not let tests stay broken between commits
- Stop if: scope drifts, dependency conflict, ambiguous acceptance criterion, or failed test you cannot diagnose in <30 minutes
- Commit per file group; final commit message: `WP-{{X}}.{{Y}}: <action>`
- Do NOT push or open PR without operator approval

---

## Verification (operator self-check before approving merge)

- [ ] All acceptance criteria observable as PASS
- [ ] All unit tests pass
- [ ] All manual TCs executed and passed
- [ ] No unrelated changes in PR diff
- [ ] No `// TODO` or `// FIXME` comments added
- [ ] No console.log / print statements added
- [ ] No hardcoded secrets or test credentials in diff
- [ ] Rollback plan tested (at minimum, dry-run mentally)
