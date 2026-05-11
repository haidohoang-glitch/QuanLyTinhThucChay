# M{{N}} — {{DOMAIN_NAME}}

> **SRS Module {{N}} of 10** — Functional Requirements for {{DOMAIN_NAME}} | Project: {{PROJECT_NAME}}

---

## {{N}}.1 Domain Overview

{{ONE_PARAGRAPH — what this domain covers, its boundary against other modules, key external systems involved}}

### Related modules
- **Depends on:** {{e.g., M3 Authentication — users must be logged in for these FRs}}
- **Provides to:** {{e.g., M5 Reporting — exposes data this module owns}}

### User classes involved
{{LIST_FROM_M2.3}}

### External systems involved
{{LIST_FROM_M2.1}}

---

## {{N}}.2 Functional Requirements

> Format conventions:
> - ID: `FR-{{DOMAIN_PREFIX}}-NN` (sequential within domain)
> - Each FR is atomic, testable, unambiguous, traceable
> - Priority follows MoSCoW: **Must** / **Should** / **Could** / **Won't (this release)**
> - Source field cites stakeholder or document; "Inferred" if not from explicit source (flag for review)

---

### FR-{{PREFIX}}-01 — {{REQUIREMENT_TITLE}}

**Statement:** {{The system shall ... — single sentence imperative}}

**Details:**
- {{DETAIL_1 — observable condition or rule}}
- {{DETAIL_2}}
- {{DETAIL_3}}

**Acceptance criteria:**
- [ ] {{CRITERION_1 — testable}}
- [ ] {{CRITERION_2 — testable}}
- [ ] {{CRITERION_3 — testable}}

**Priority:** {{Must / Should / Could / Won't}}

**Source:** {{e.g., Stakeholder interview (CEO, 2026-04-02) | REF-02 GDPR Article 17 | Inferred from competitor Y}}

**Verification method:** {{Acceptance test / Demo / Inspection / Analysis}}

**Test cases (anticipated):** TC-{{PREFIX}}-01..XX (populated by QA in M10 RTM)

**Notes / Open questions:**
- {{ANY_AMBIGUITY_OR_UNRESOLVED_DETAIL}}

---

### FR-{{PREFIX}}-02 — {{REQUIREMENT_TITLE}}

(repeat structure)

---

(continue for each FR in domain — typically 5-15 FRs per domain)

---

## {{N}}.3 Workflows in this Domain

Multi-step user/system journeys that span multiple FRs.

### Workflow: {{WORKFLOW_NAME}}

**Trigger:** {{WHAT_INITIATES}}

**Actors:** {{USER_CLASSES_INVOLVED}}

**FRs involved:** FR-{{PREFIX}}-01, FR-{{PREFIX}}-04, FR-{{PREFIX}}-07

**Happy path:**
```
1. {{STEP — references which FR enables it}}
2. {{STEP}}
3. {{STEP}}
```

**Alternative paths:**
- {{CONDITION}} → {{OUTCOME}}
- {{CONDITION}} → {{OUTCOME}}

**Failure paths:**
- {{ERROR_CONDITION}} → {{HANDLING}}

---

## {{N}}.4 Data Entities Owned by This Domain

| Entity | Description | Key attributes (business level) | Created by | Modified by |
|--------|-------------|----------------------------------|------------|-------------|
| {{ENTITY}} | {{ONE_LINE}} | {{ATTR_LIST}} | {{ACTOR}} | {{ACTOR_LIST}} |

(Detailed schemas belong in technical design, not SRS. SRS stays at business-entity level.)

---

## {{N}}.5 Out of Scope (for clarity)

Explicitly out of scope for this domain (to prevent scope creep):

- {{NOT_INCLUDED_1}}
- {{NOT_INCLUDED_2}}

If these become in scope later, add new FRs and update this section.

---

## {{N}}.6 Open Questions

| ID | Question | Why unresolved | Action needed |
|----|----------|----------------|---------------|
| OQ-{{NN}} | {{QUESTION}} | {{e.g., Stakeholder unavailable; pending interview}} | {{NEXT_STEP}} |

These also propagate to M10 (Open Issues consolidated).

---

## {{N}}.7 Priority Summary

| Priority | Count |
|----------|-------|
| Must | {{N}} |
| Should | {{N}} |
| Could | {{N}} |
| Won't (this release) | {{N}} |

If "Must" >70% of total, you may be over-prioritizing. Force ranking conversations with stakeholders to refine.
