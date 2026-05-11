# SRS Greenfield Author — Adaptation

Variations by project context.

> **Applies to Mode A only.** Mode B (company template) and Mode C (user-defined) follow their own conventions.

## Regulated industries

### Healthcare (FDA, HIPAA)

**Must-have additions:**
- M1.4: cite 21 CFR Part 11 (electronic records), HIPAA Privacy Rule, applicable FDA guidance docs
- M2.5 Constraints: explicit BAA requirement; PHI inventory mandatory; audit trail constraints
- M3-Mx: every FR touching PHI flagged with privacy class
- M9 (when populated): include validation requirements per ALCOA+ principles
- M10: sign-off includes Quality Assurance Lead and Regulatory Affairs

**Don't:**
- Skip device classification if applicable (Class I/II/III drives requirement rigor)
- Forget to cite predicate device or 510(k) basis if applicable

### Financial services (PCI-DSS, SOX)

**Must-have additions:**
- M2.5: cardholder data scope (CDE) explicit; tokenization vs storage decision
- M2.5: SOX-specific audit trail and segregation-of-duties constraints
- M3-Mx: separate domain for "Audit & Reporting" (often required even if not feature-rich)
- M9: encryption requirements aligned to PCI-DSS § 3, 4

### EU-resident user data (GDPR)

**Must-have additions:**
- M2.5: data residency explicit; sub-processor list referenced
- M3-Mx: dedicated FRs for right-to-export, right-to-delete, right-to-rectification, consent
- M9: lawful basis for processing per category

## Government / Public sector

- Use the funding agency's required SRS format (often based on IEEE 29148 with extensions). Mode B applies.
- Section 508 / WCAG accessibility as constraints (M2.5) and as NFRs (M9)
- Public records / FOIA implications must be documented in M2.5

## Agile teams

When the team will execute via user stories, but a formal SRS is still required (e.g., for procurement or regulatory):

- M3-Mx FRs may be **derived from user stories** rather than written first
- Include an appendix in M10 mapping FR → User Story / Epic
- Maintain SRS as living document; update at end of each release vs. lock at v1.0
- Acceptance criteria in FRs match user story acceptance criteria

If team is fully agile and SRS is just bureaucratic overhead, push back — sometimes the right answer is "we don't need an SRS, we need a Product Brief". Use this skill only when an SRS is genuinely required.

## B2B procurement / contract appendix

When SRS will be attached to a vendor contract:

- M2.5 Constraints become especially load-bearing — they're contractual obligations
- Every FR's "Verification method" becomes acceptance test for payment milestone
- M10 includes "Acceptance Criteria for Project Completion" section
- Reduce ambiguity ruthlessly — vendor disputes always cite SRS gaps

## Internal tools / Lower-stakes products

When the product is for internal use only and lower-risk:

- Light formal weight is OK
- Can collapse M3-Mx into 2-3 modules if domain is small
- M9 may be lighter (NFRs less critical for non-customer-facing)
- But: still document scope clearly to prevent indefinite scope creep

If you find yourself authoring a full IEEE-style SRS for a 2-week internal tool, you're probably over-engineering. Use a simpler "Product Brief" instead.

## Mobile-first products

- M2.4: include OS version matrix (iOS, Android), device class (phone/tablet/wearable)
- M3-Mx: offline behavior FRs are mandatory (most consumer SRSs forget these)
- M9: app size, battery impact, App Store guideline compliance as NFRs

## ML / AI products

- M3-Mx: separate domain for "Model Inputs" (data lineage, consent, quality requirements)
- M3-Mx: separate domain for "Model Outputs" (confidence handling, fallback behavior)
- M2.5: training data constraints (PII, fairness, bias evaluation)
- M9: model performance NFRs (accuracy, latency, drift detection)
- Address: explainability, contestability (regulated decisions)

## API / Platform products

When the product IS an API (no UI):

- M2.3 User classes are "Developer integrators" (different characteristics from end-users)
- M3-Mx organized by API resource (Users, Orders, Webhooks, etc.) rather than user-facing feature
- Include OpenAPI spec as appendix in M10
- Versioning policy explicit in M2.5 (e.g., "API versioned; breaking changes require new major version")
- Rate limiting, authentication, idempotency as cross-cutting NFRs in M9

## Multi-tenant SaaS

- M2.3 User classes: distinguish tenant types (free / pro / enterprise) and roles within tenant (owner / admin / member)
- M2.5: tenant isolation as constraint
- M3-Mx: tenant-context aware FRs (e.g., "Admin can manage members within own tenant only")
- M9: per-tenant quotas and rate limits

---

## Cross-cutting: project age

- **Pre-funding / pre-team:** Lighter SRS, focus on M1 and M2; M3-Mx may be sketches. Use this skill but tag everything as "DRAFT".
- **Post-funding, pre-build:** Full formal SRS; this is the canonical use case.
- **Mid-build (rare for greenfield):** If you're authoring SRS while building, you're probably reverse-engineering — switch to `srs-reverse-engineer`.
- **Post-launch (refactor):** Use `srs-reverse-engineer` to capture current state, then this skill to author target-state SRS for the rewrite.
