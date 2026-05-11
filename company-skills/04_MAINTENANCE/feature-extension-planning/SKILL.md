---
name: feature-extension-planning
description: Plan a new feature extension to an existing system without breaking architectural integrity. Produces a feature spec covering scope, design alignment with existing architecture, schema changes, rollout, test plan, and SRS update notes. Lighter weight than `tech-solution-design` (single feature vs. system-level), heavier than a Jira ticket. Use post-launch when adding meaningful features to an existing system, when ensuring new feature aligns with established architecture, or when generating Phase 4 Maintenance feature output. Triggers include "plan a new feature", "feature spec", "extension to existing system", "feature design doc", or "Phase 4 Maintenance feature".
---

# Feature Extension Planning

Author a feature spec for adding a meaningful feature to an existing system. The output is a per-feature plan that:
- Respects the existing architecture (doesn't accidentally break it)
- Aligns with SRS / business context
- Covers schema, rollout, testing
- Updates SRS / RTM as needed

This is **post-launch** work; greenfield features go to `srs-greenfield-author` instead.

## When this skill applies

Use when:
- Adding a meaningful new feature to a live product
- Feature involves >1 file or affects multiple users
- Feature has data/schema/API surface change
- Need to ensure feature aligns with existing architecture (not a bolt-on hack)
- Generating Phase 4 Maintenance feature output

Do NOT use for:
- Tiny tweaks (config change, copy edit) — just a Jira ticket
- System-level redesign (use `tech-solution-design`)
- New product / new project (use `srs-greenfield-author`)

## Inputs

1. **Feature request:** product brief, user request, ticket
2. `docs/00_REQUIREMENTS/SRS_VI/M3-Mx` — existing FRs (where does this fit?)
3. `docs/01_DISCOVERY/CODEBASE_MAP.md` — current structure
4. `docs/01_DISCOVERY/BUSINESS_CONTEXT.md` — domain context
5. `docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md` (if exists) — architectural context
6. `docs/03_EXECUTION/AI_OPERATOR_GUIDE.md` (if exists) — execution protocol

## Output

`docs/04_MAINTENANCE/feature-extensions/FEAT_<NAME>.md`, filled from [assets/FEATURE_template.md](assets/FEATURE_template.md).

## Workflow

### Step 1 — Understand the feature ask

Write a 1-paragraph answer to:
- **What** does this feature do?
- **Who** uses it?
- **Why** are we building it (business reason)?

Verify with feature requester before continuing. If "what/who/why" is fuzzy, the feature spec will be too.

### Step 2 — Choose feature template mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — Standard feature template** *(default)* | No company-specific format | This skill's template (Why, What, How, Test, Rollout) |
| **B — Honor company feature spec template** | Company has formal feature spec | Company template |
| **C — User-defined sections** | Specific format needed (e.g., security review section, GDPR DPIA) | User input |

Selection logic:
1. User explicit → use it
2. Company has feature spec template → ask user
3. Default → Mode A

### Step 3 — Map feature to existing FRs / domain

Where does this feature fit?

- **Extends existing FR?** Reference FR-XXX-NN; describe extension
- **New FR in existing domain?** Pick which Mx module gets the new FR
- **Crosses domains?** Document as multi-domain feature
- **Conflicts with existing FR?** Resolve before continuing (cannot have contradictory FRs)

If feature genuinely doesn't fit any domain, that's a smell — domain may need restructuring (or the feature shouldn't be in this product).

### Step 4 — Design the feature (lightweight)

For most features, design is lightweight. Cover:

- **User flow:** what does the user do, in what order
- **Data:** what data is created/read/updated/deleted
- **API surface:** new endpoints (if applicable); changes to existing
- **UI:** new pages/components/states (if applicable)
- **Integration:** which existing services/components touched

Don't write a 30-page design doc; aim for 1-2 pages of design content.

If feature is large enough to need significant architectural thought, escalate to `tech-solution-design`.

### Step 5 — Identify SRS / NFR impact

- **New FRs to add:** specify ID + statement; will be added to SRS M3-Mx
- **Existing FRs to update:** specify which + change
- **NFR impact:** does this feature introduce new performance/security/compliance considerations?
- **RTM impact:** new tests; existing tests need updates

This is what makes "feature extension" different from "ticket" — feature requires SRS update.

### Step 6 — Plan rollout

How does this feature ship safely:

- **Feature flag:** name + default state + audience targeting
- **Gradual rollout:** % stages if applicable
- **A/B test:** if applicable, hypothesis + success metric
- **Backward compatibility:** does this break existing API/UI/data?
- **Migration:** any data migration needed
- **Training/docs:** internal docs; customer-facing changelog

### Step 7 — Plan testing

- **Unit tests:** new tests for new code
- **Integration tests:** feature-level
- **Manual TCs:** scenarios that need human verification
- **Performance test:** if feature changes load profile
- **Security test:** if feature changes authn/z surface

Reference TC IDs to be added to RTM.

### Step 8 — Risk + rollback

- **Risks:** what could go wrong; likelihood + impact
- **Mitigations:** flag-based rollback, schema-down migration, etc.
- **Rollback approach:** specifics, not "git revert"

### Step 9 — Plan execution

If this feature requires implementation work:

- Decompose into work packages (use `implementation-planning` for non-trivial features)
- Or define as single-WP work
- Estimate effort
- Identify dependencies

### Step 10 — Self-review

Run [references/checklist.md](references/checklist.md). Feature spec quality affects implementation; investing here saves rework.

## Quality bar

A good feature spec lets:
- Engineering implement without re-asking "what does it do?"
- QA write test plan from spec
- Product communicate value to customers
- Compliance verify regulated implications addressed
- Architecture maintain consistency (existing patterns followed)

If the spec is "build it and we'll figure out details", it's a ticket, not a spec. Use this skill to elevate to spec quality.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations: small features (light spec), large features (boundary with `tech-solution-design`), regulated features (compliance review section), experimental features (A/B framing).

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: adding "bulk export" to an existing CRM product.

## Failure modes to avoid

- **Skipping SRS update.** New FR exists but never gets to SRS → traceability breaks.
- **Designing in isolation.** Feature seems clean but conflicts with existing pattern; architecture rots.
- **No rollback plan.** Features deploy expecting success; reality includes rollback.
- **Over-spec.** 30-page doc for a small feature wastes time; aim for proportional rigor.
- **Under-spec.** "Add export button" — what data exported? What format? Scoping ambiguity → wrong implementation.
- **No NFR impact considered.** Adds latency, fails p95 SLA — discovered post-deploy.
- **Skipping flag.** Feature ships to 100% on day one; if issue, full rollback required.
