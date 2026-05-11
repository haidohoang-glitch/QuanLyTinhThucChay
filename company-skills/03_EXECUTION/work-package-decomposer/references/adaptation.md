# Work Package Decomposer — Adaptation

Variations by WP type and risk profile.

> **Applies to Mode A (3-tier) only.** Mode B/C follow company/user policy.

## Simple WPs (mostly mechanical)

WPs like "Install dependency", "Add config flag", "Fix typo":

- Likely 80-95% Tier 1
- Few or no Tier 2/3 tasks
- Total tasks: 5-10
- Operator gate count: 1-2 (mostly final approval)

If your decomposition exceeds 15 tasks for a "simple" WP, the WP itself may not be simple. Re-read.

## Implementation-heavy WPs

WPs like "Implement new auth flow", "Add new service":

- Mix tier-1 (boilerplate, install) + tier-2 (function implementation) + tier-3 (architecture)
- Likely 50-60% Tier 1, 30-40% Tier 2, ~10% Tier 3
- Total tasks: 12-20

## Risky WPs (data migration, security-sensitive)

WPs touching production data, auth, security primitives:

- More Tier 3 tasks (architectural review)
- More operator gates (every destructive operation)
- More verification rigor (each task verifies in 2+ ways: command + diff + test)
- Consider explicit "rollback rehearsal" task in staging

## Legacy code WPs

WPs in code with no tests / unclear architecture:

- More Tier 2/3 reading tasks ("understand X before changing")
- More upfront analysis tasks before any change task
- Operator gate after each non-trivial change
- May produce intermediate doc updates (BUSINESS_CONTEXT, CODEBASE_MAP) in addition to code change

## Test-only WPs

WPs that add tests to existing code:

- Tier 1 for boilerplate test setup
- Tier 2 for test case logic (deciding what to test)
- Verify is "run test, confirm it actually tests what it claims" (not just "test passes")

## Data migration WPs

WPs that modify schema or migrate data:

- Tier 3 for migration design (rollback safety, online vs offline)
- Tier 2 for migration script writing
- Tier 1 for executing migration command (only after approval gate)
- Mandatory: dry-run task on staging clone BEFORE production
- Mandatory: rollback rehearsal task

## UI / frontend WPs

WPs touching React/Vue/etc.:

- Tier 1 for component scaffolding (boilerplate from template)
- Tier 2 for component logic (state, props handling)
- Tier 3 for cross-component refactor or hook patterns
- Verification: visual check (operator runs locally, eye-tests)
- Consider: snapshot tests in CI as automated verify

## API / backend WPs

WPs adding/modifying endpoints:

- Tier 1 for boilerplate (route registration, middleware wiring)
- Tier 2 for handler logic
- Tier 3 for cross-cutting changes (auth, rate limiting affecting many routes)
- Verify: contract test against OpenAPI spec or curl scripts
- Mandatory: integration test task

## DevOps / infrastructure WPs

WPs touching IaC, CI/CD, deployment:

- Tier 1 for config file edits (when exact text known)
- Tier 2 for non-trivial IaC changes
- Tier 3 for architecture-affecting changes (network topology, IAM)
- Verify: `terraform plan` output review; `gh workflow` validation
- Mandatory: dry-run; never apply directly to prod from AI without operator review

## ML / data pipeline WPs

WPs touching ML code or data pipelines:

- Tier 2 dominates (most tasks require understanding data/model context)
- Tier 1 for boilerplate setup, data loading scaffolding
- Tier 3 for model architecture changes, fairness considerations
- Verify: model evaluation metrics; data quality checks; pipeline run on sample

---

## When to abort decomposition

Abort and re-scope if:

- WP requires >25 tasks → WP is too big; ask `implementation-planning` to split
- WP has unclear acceptance criteria → ambiguity will cascade into wrong tasks
- WP requires reading >10 files just to understand → likely needs `business-context-capture` first
- Operator can't articulate "definition of done" → spec the WP first

## When to escalate to higher tier

Mid-execution, if:

- Tier 1 task fails twice → escalate to Tier 2 (re-run with more context)
- Tier 2 task produces inconsistent diffs → escalate to Tier 3 OR human review
- Verification fails for unknown reason → STOP, operator decides

Don't keep retrying on same tier — that's how cost blows up without progress.

---

## Cost optimization rules of thumb

| Goal | Approach |
|------|----------|
| Maximum cost saving | 70%+ Tier 1; minimize Tier 3; batch operator gates |
| Maximum quality | More Tier 2/3; more verification; more operator gates |
| Balance | Per-task tier matches genuine complexity; don't reach for higher tier just for safety |

If a project consistently runs above $20/WP for ordinary WPs, decomposition isn't routing well. Audit a sample to find misclassified tasks.
