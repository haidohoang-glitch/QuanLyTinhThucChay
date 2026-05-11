# SRS Reverse Engineer — Adaptation

Variations by reverse-engineering context.

> **Applies to Mode A only.** Mode B (existing SRS to extend) and Mode C (user-defined scope) follow their own conventions.

## Legacy with no documentation

The pure case. Inputs are entirely Discovery outputs + code reading + UI exploration.

**Specific approaches:**
- Run all of Phase 1 Discovery first (CODEBASE_MAP, DATA_ARCHITECTURE, TECH_DEBT_AUDIT, BUSINESS_CONTEXT)
- Spend ~40% time on `BUSINESS_CONTEXT` quality — it's the foundation for M3-Mx
- M10 Open Issues will be very large (often 20+ items); this is correct, not a defect
- Partial coverage is OK for v0.1; iterate to v1.0 with stakeholder review

**Risks:**
- Tribal knowledge holders may quit before SRS is reviewed; capture interview notes as supporting docs
- "Why does the code do X?" rarely answerable without interviews; flag heavily

## Codebase with partial docs (README, ADRs, but no SRS)

Easier — partial source material exists.

**Specific approaches:**
- Use existing READMEs to inform M1.5 overview and M2.1 product perspective
- ADRs (Architecture Decision Records) feed M2.5 constraints (these are intentional)
- Inline code comments referenced as evidence — but don't trust them (often outdated)
- Partial product specs (e.g., a 2-page founder doc) can inform M1 and M2

**Risks:**
- Existing docs may be wrong; trust code over docs when they conflict
- ADRs may describe decisions that were later reversed; verify against code

## Post-acquisition handover

You acquired a company; their team is leaving; you need an SRS for the system.

**Specific approaches:**
- Schedule **interview** sessions with departing team (don't rely solely on code)
- Use `business-context-capture` outputs as interview prep (questions to ask)
- Capture interview output in M10 Appendix as supporting transcripts
- Mark FRs based on departing-team confirmation as **higher confidence**; FRs derived from code only as **medium confidence**

**Risks:**
- Departing team may have selective memory; verify their claims against code
- Time pressure (handover deadline) may force compromises; document what got skipped

## Regulatory after-the-fact

Regulator demands an SRS for an existing product. Audit deadline is the constraint.

**Specific approaches:**
- Use Mode A but **prioritize compliance-relevant domains** (PII handling, audit trail, security) over feature-rich domains
- M2.5 constraints section becomes the most important — must align with the regulation cited
- M9 (NFRs) populated with regulatory requirements verbatim, then verified against current implementation
- M10 Open Issues becomes a remediation list (gaps between regulation and current state)

**Risks:**
- "Currently doesn't comply" findings expose the company to regulator pressure; coordinate with legal
- Documenting non-compliance creates a paper trail; consider phased disclosure with remediation plan

## Pre-rewrite "as-is" capture

Before drafting a rewrite spec, document the current system to prevent feature loss.

**Specific approaches:**
- Use this skill for "as-is" SRS
- Use `srs-greenfield-author` to author "to-be" SRS for the rewrite target
- Diff between as-is and to-be SRSs becomes the migration scope
- M10 Open Issues from as-is feed into rewrite design decisions ("this bug exists; do we preserve, fix, or remove?")

**Risks:**
- Rewrite teams skip "as-is" capture and miss features only used by 5% of users; do not skip
- "As-is" SRS may capture bugs as features; use M10 to flag candidates for removal

## Multi-component / monolith breakup

Reverse-engineering an SRS for a monolith that will be split into services.

**Specific approaches:**
- Generate ONE SRS at first (the monolith level), with M3-Mx as functional domains
- Each functional domain may eventually become its own service with its own SRS
- M2.5 constraints emphasize current coupling that will need to be untangled
- M10 includes "Decomposition candidates" appendix — domains that look service-shaped

## API-only product

When the product is an API (no UI):

- M2.3 user classes are "Developer integrators"
- M3-Mx organized by API resource, with FRs derived from endpoint behavior
- Live verification means **calling the API**, not browsing UI
- Include OpenAPI spec as M10 Appendix
- Endpoint deprecations / version skew documented in M10 Open Issues

## ML / AI product reverse-engineering

When extracting requirements from an ML system:

- M3-Mx separates into "Model Inputs" (data acquired from where, transformed how) and "Model Outputs" (predictions used by what)
- Training data lineage is M2.5 constraint material (often regulatorily significant)
- Model performance NFRs (accuracy, latency) read from prod metrics for M9 placeholder
- M10 documents: model versioning policy, retraining cadence, drift detection — these are often unwritten

## Microservices reverse-engineering

When the system is many services:

- One SRS per service is too many; one for the whole system is too aggregated
- **Compromise:** one SRS at the platform level, with M3-Mx organized by user-facing capability (which may span services)
- Each Mx module's "External systems" subsection lists which services participate
- M2.5 includes service contract stability constraints (versioning policies)

---

## Cross-cutting: confidence calibration

Reverse-engineered SRSs almost never reach High confidence. Calibrate:

| Confidence | When to claim | Caveats |
|------------|---------------|---------|
| **High** | All inputs fresh; live UI verified for every workflow; ex-team interviewed; ≤5 Open Issues | Rare; usually requires 3+ weeks |
| **Medium-High** | All Discovery inputs fresh; live UI sampled; ≤15 Open Issues | Achievable with 1-2 weeks dedicated work |
| **Medium** | Discovery inputs OK but partial; some inferences without live verification; 15-30 Open Issues | Typical for first reverse-engineered draft |
| **Low** | Discovery stale or partial; no live verification; many gaps | Document as DRAFT; iterate before reliance |

Mark per-module if confidence varies (e.g., M3 Authentication HIGH because well-documented; M5 Reporting LOW because no live data observed).
