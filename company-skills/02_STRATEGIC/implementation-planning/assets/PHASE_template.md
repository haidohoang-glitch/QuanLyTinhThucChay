# Phase {{N}} — {{PHASE_NAME}}

> **Purpose:** {{ONE_LINE_PURPOSE — what this phase achieves and why it's a phase boundary}}
> **Phase number:** {{N}}
> **WPs in this phase:** {{COUNT}}
> **Total effort:** {{HOURS}}
> **Calendar duration estimate:** {{DAYS_RANGE}}
> **Verification Gate:** Gate {{N}} (criteria in MASTER_PLAN.md Section 6)

---

## Context

**Why this phase exists (in 1 paragraph):**
{{REASONING — why these WPs cluster into a phase, what risk is being managed, why phase boundary here}}

**Inputs (must be true at start of phase):**
- {{PRECONDITION_1}}
- {{PRECONDITION_2}}

**Outputs (must be true at end of phase):**
- {{POSTCONDITION_1}}
- {{POSTCONDITION_2}}

**Out of scope for this phase:**
- {{NOT_INCLUDED_1}}

---

## WP Sequence

Recommended order (respecting dependencies; parallelism noted):

```
Day 1-2: WP-{{N}}.A, WP-{{N}}.B (parallel)
Day 3:   WP-{{N}}.C (depends on A)
Day 4-5: WP-{{N}}.D, WP-{{N}}.E (parallel)
...
```

| WP | Depends on | Parallelizable with | Effort |
|----|------------|---------------------|--------|
| WP-{{N}}.A | (none) | WP-{{N}}.B | {{XS/S/M/L}} |
| WP-{{N}}.B | (none) | WP-{{N}}.A | {{XS/S/M/L}} |
| WP-{{N}}.C | WP-{{N}}.A | — | {{XS/S/M/L}} |

---

## Work Packages

(Each WP follows the same structure. See `assets/WP_template.md` for the empty WP template.)

---

### WP-{{N}}.A — {{TITLE}}

**Goal:** {{ONE_SENTENCE}}
**Effort:** {{XS/S/M/L}}
**Owner:** {{ROLE_OR_PERSON}}
**Dependencies:** {{LIST_OR_NONE}}

**Files affected:**
- `{{PATH_1}}` — {{WHAT_CHANGES}}
- `{{PATH_2}}` — {{WHAT_CHANGES}}

**Acceptance criteria** (each must be observable):
- [ ] {{CRITERION_1}}
- [ ] {{CRITERION_2}}
- [ ] {{CRITERION_3}}

**Unit tests:**
- {{TEST_1}} — `{{PATH_TO_TEST_FILE}}`
- {{TEST_2}} — `{{PATH_TO_TEST_FILE}}`

**Manual test cases (TC IDs):**
- TC-{{N}}A-01: {{SCENARIO}} → expected: {{OUTCOME}}
- TC-{{N}}A-02: {{SCENARIO}} → expected: {{OUTCOME}}

**Risks:**
- {{RISK_1}}: {{MITIGATION}}

**Rollback plan:**
- {{HOW_TO_REVERT}} (e.g., `git revert <hash>`; or feature flag off; or DB migration down)

**PR title format:**
`[Phase {{N}}][WP-{{N}}.A] {{TITLE_SHORT}}`

---

### WP-{{N}}.B — {{TITLE}}

(repeat structure)

---

(continue for each WP in this phase)

---

## Phase Verification Gate

Cannot proceed to Phase {{N+1}} until ALL of:

- [ ] All WPs in this phase merged
- [ ] All acceptance criteria for each WP passed (verify by re-running tests)
- [ ] All manual test cases (TC-*) passed
- [ ] No production incidents introduced during phase
- [ ] {{PHASE_SPECIFIC_CRITERION_1}}
- [ ] {{PHASE_SPECIFIC_CRITERION_2}}

If gate fails: do NOT start next phase. Document blocker, fix, re-run gate.

---

## Notes

- **Bundling rule:** No WP combines unrelated changes. If you find yourself wanting to "also fix Y while in here", create a follow-up WP.
- **PR-per-WP rule:** One WP = one PR. Do not merge multiple WPs in a single PR.
- **AI agent execution:** WPs in this phase can be executed by AI agents under human supervision per `docs/03_EXECUTION/AI_OPERATOR_GUIDE.md`.
