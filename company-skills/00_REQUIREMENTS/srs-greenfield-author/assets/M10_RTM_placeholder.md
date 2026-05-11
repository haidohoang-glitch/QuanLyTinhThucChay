# M10 — RTM, Open Issues, Appendix

> **SRS Module 10 of 10** | Project: {{PROJECT_NAME}}

---

## 10.1 Requirements Traceability Matrix (RTM)

> **PLACEHOLDER** — Populated by the `requirements-traceability` skill once code and tests exist.

The RTM links:

```
FR/NFR ──> Design artifact ──> Code module ──> Test case ──> Status (Pass/Fail/Pending)
```

### When to populate

- After Phase 1 (Quick Wins) when first features land in code
- Continuously updated as new FRs are implemented
- Required for compliance audit (SOC2, ISO 27001, FDA, etc.)

### Inputs the RTM skill will need

- M3-Mx FRs (already authored in this SRS)
- M9 NFRs (after `nfr-specification` skill runs)
- Implemented code (file paths, function names)
- Test cases (TC IDs from manual testing or automated test names)
- Pass/fail status from latest test run

---

## 10.2 Open Issues

Unresolved scope or design questions captured during SRS authoring. Each must be resolved before SRS is "approved" status (or explicitly deferred).

| ID | Issue | Originated in | Status | Owner | Target resolution date |
|----|-------|---------------|--------|-------|------------------------|
| ISS-01 | {{e.g., Should `User` and `Account` be one entity or separate? — affects FR-AUTH-* and FR-ACCT-*}} | M2.3 + M3 | OPEN | Product Owner | {{YYYY-MM-DD}} |
| ISS-02 | {{e.g., Email verification is required for "Must" FRs but legal hasn't confirmed wording}} | M3 | BLOCKED on legal | Legal | {{YYYY-MM-DD}} |
| ISS-03 | {{e.g., GDPR right-to-export scope unclear — full data dump or filtered?}} | M2.5 | OPEN | Compliance | {{YYYY-MM-DD}} |

### Issue lifecycle

- **OPEN** — Captured, not yet investigated
- **IN PROGRESS** — Owner is actively resolving
- **BLOCKED** — Waiting on external (legal, vendor, executive decision)
- **RESOLVED** — Decision made; SRS updated to reflect; issue closed
- **DEFERRED** — Acknowledged, postponed to future SRS version (must include rationale)

---

## 10.3 Appendix

### A. Data Dictionary (Domain Entities)

Consolidated from M3-Mx domain modules. Each entity defined once here; referenced by ID in FRs.

| Entity | Definition | First mentioned |
|--------|------------|-----------------|
| {{ENTITY}} | {{DEFINITION}} | M{{N}}.4 |

### B. User Class Privilege Matrix

| User class | Resource | Read | Create | Update | Delete | Special |
|------------|----------|------|--------|--------|--------|---------|
| {{CLASS}} | {{RESOURCE}} | ✓ / ✗ | ✓ / ✗ | own / all / ✗ | own / all / ✗ | {{SPECIAL}} |

### C. State Diagrams

For entities with non-trivial lifecycles, document state machines:

```
{{ASCII_OR_MERMAID — e.g., Order: pending → paid → shipped → delivered ; with branches for refund, cancel}}
```

### D. Glossary (Extended)

For project-specific terminology requiring more context than M1.3 inline definitions.

| Term | Detailed definition | Example | Synonyms in code |
|------|---------------------|---------|-------------------|
| {{TERM}} | {{LONG_DEFINITION}} | {{EXAMPLE}} | {{CODE_NAMES}} |

### E. Document Revision History

| Version | Date | Author | Section(s) changed | Reason |
|---------|------|--------|---------------------|--------|
| 0.1 | {{YYYY-MM-DD}} | {{NAME}} | All | Initial draft |

---

## 10.4 Sign-off

| Role | Name | Signature/Approval | Date |
|------|------|---------------------|------|
| Product Owner | | | |
| Engineering Lead | | | |
| QA Lead | | | |
| Compliance / Legal (if applicable) | | | |

SRS is **approved** when all Open Issues (10.2) are resolved or formally deferred AND all sign-offs collected.
