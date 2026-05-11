# Feature Extension Planning — Adaptation

Variations by feature size and context.

> **Applies to Mode A only.** Mode B/C follow conventions.

## Small features (XS / S effort)

When the feature is < 1 day work:

**Adjust:**
- Sections 1-2 brief (1-2 sentences each)
- Section 4 design may be 1 paragraph (no detailed flow)
- Sections 5-7 minimal but present (don't skip even if small)
- Section 8 may have only 1 risk

**Don't:**
- Skip risk + rollback even if "obviously safe" — it's the recurring "obviously safe" features that surprise

## Medium features (M effort, 1-3 days)

The default case. Follow template fully. Each section ~1 paragraph.

## Large features (L+ effort)

When feature is >3 days:

**Decision point:** is this still a feature, or is it a small project?

If it's a project:
- Use `tech-solution-design` for architecture (Phase 2)
- Use `implementation-planning` for WPs (Phase 2)
- Feature spec becomes a "feature epic" doc that links to design + plan

If it's still a feature (just complex):
- Spec is longer; expand each section
- Decompose Section 10 into clear WPs
- Multiple compliance reviewers may be needed

## Regulated features

When feature touches PII / PHI / financial data / accessibility:

**Mandatory additions:**
- Section 11 Compliance review fully populated
- Specific reviewers (Compliance Lead, Security Lead, Legal)
- DPIA if GDPR Article 35 (high-risk processing)
- Audit log entries explicit

**Watch for:** Compliance reviews can slip; build buffer into timeline

## Experimental / A/B test features

When feature is a controlled experiment:

**Add:**
- Section: A/B Test Hypothesis (what we're testing)
- Section: Success metrics (what counts as "won")
- Section: Test duration + sample size (statistical power)
- Section: What happens if test wins (rollout) vs loses (cleanup)

**Watch for:** Failed experiments leaving dead code; commit to cleanup whether win or lose

## Feature flag heavy features

When feature is gated by complex flag logic:

**Add:**
- Flag conditions table (user tier, country, plan, etc.)
- Cleanup plan (when does flag retire?)
- Flag interaction with other flags

**Watch for:** Long-lived flags becoming permanent infrastructure; aim for <90 day flag lifespan

## Cross-team features

When feature requires multiple teams:

**Add:**
- Team RACI (Responsible, Accountable, Consulted, Informed)
- Cross-team sync cadence
- Contract between teams (e.g., service A provides X by date Y)

**Watch for:** Coordination overhead; consider whether one team should own more

## Customer-specific features

When feature is for one or few large customers:

**Adjust:**
- Section 1 names customer + commitment
- Sales / Account Management as stakeholder
- Rollout may be 1-customer-at-a-time

**Watch for:** Custom features rotting into product debt; prefer features that benefit multiple customers

## API / contract changes

When feature changes public API:

**Add:**
- Versioning approach (v1 stable? new v2? deprecation timeline?)
- Migration guide for API consumers
- Breaking change communication plan

**Watch for:** SLA implications (API stability commitments); consult API governance

## UI redesign features

When feature changes UI:

**Add:**
- Design mockups attached
- Accessibility (WCAG) review
- Browser/device matrix tested
- Visual regression test plan

**Watch for:** Accessibility regressions; test with screen readers, keyboard-only, zoom

## ML model features

When feature involves model training/serving:

**Add:**
- Training data lineage
- Model evaluation metrics (precision, recall, F1, latency)
- Drift detection plan
- Fallback if model fails (rule-based default?)

**Watch for:** Model degradation over time; commitment to monitoring

## Performance-critical features

When feature is on hot path:

**Add:**
- Performance budget (specific targets)
- Load test plan with realistic load
- Profile before/after
- Capacity planning impact

---

## When to upgrade to `tech-solution-design`

Some features need full architectural treatment. Signs:

- Feature requires new architectural pattern
- Affects >3 services / modules
- Introduces new external dependency
- Changes core data model (not just adding column)
- Requires new infrastructure (queue, worker pool, region)

In these cases, do `tech-solution-design` first; this skill produces feature spec that REFERENCES the solution design.

## When to downgrade to a Jira ticket

If the feature is genuinely tiny:

- Single config change
- Copy/text edit
- Bug fix (use bug tracker, not feature spec)
- Internal tool tweak (no customer impact)

Jira ticket suffices. Don't ceremony-overhead small work.

---

## Lifecycle

| Stage | Status | Trigger |
|-------|--------|---------|
| Initial idea | Draft | Author starts spec |
| Reviewed | Reviewed | Eng + Product reviewed |
| Approved | Approved | Sign-offs collected; ready to build |
| In Implementation | In Implementation | Engineering picked up |
| Shipped | Shipped | Feature live in production at 100% |
| Deferred | Deferred | Decision to not build (yet); preserve spec |

Update Status field as feature progresses.
