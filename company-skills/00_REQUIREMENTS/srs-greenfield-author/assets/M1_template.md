# M1 — Introduction

> **SRS Module 1 of 10** | Project: {{PROJECT_NAME}} | Version: v0.1 (DRAFT) | Date: {{YYYY-MM-DD}}

---

## 1.1 Purpose

This Software Requirements Specification (SRS) describes the requirements for **{{PROJECT_NAME}}**.

**Audience:**
- {{AUDIENCE_1 — e.g., Product manager, engineering lead, stakeholders}}
- {{AUDIENCE_2 — e.g., External vendor for procurement}}
- {{AUDIENCE_3 — e.g., Regulatory reviewer (specify body if known)}}

**Purpose of this document:**
- {{PURPOSE_1 — e.g., Define scope and boundaries before development begins}}
- {{PURPOSE_2 — e.g., Provide testable acceptance criteria for QA}}
- {{PURPOSE_3 — e.g., Serve as contract appendix for vendor engagement}}

---

## 1.2 Scope

### Product name
{{PROJECT_NAME}} (working title: {{ALT_NAME_IF_ANY}})

### What it does (3-5 sentences)
{{PARAGRAPH — concrete description: who uses it, what they accomplish, what value it delivers, deployment model (web/mobile/etc.)}}

### What it does NOT do (out of scope)
- {{NOT_INCLUDED_1}}
- {{NOT_INCLUDED_2}}
- {{NOT_INCLUDED_3}}

This explicit boundary prevents scope creep. Items here can be revisited in future SRS versions.

### Goals & objectives
| Goal | Success measure |
|------|-----------------|
| {{BUSINESS_GOAL}} | {{MEASURE — e.g., 1000 active users in 90 days}} |
| {{BUSINESS_GOAL}} | {{MEASURE}} |

---

## 1.3 Definitions, Acronyms, Abbreviations

Domain terminology used in this SRS. Update as new terms appear.

| Term | Definition |
|------|------------|
| {{TERM}} | {{DEFINITION}} |
| {{ACRONYM}} | {{EXPANSION — and one-line explanation}} |
| **MoSCoW** | Priority rubric: Must / Should / Could / Won't (used in M3-M8 priorities) |
| **FR** | Functional Requirement (covered in M3-M8) |
| **NFR** | Non-Functional Requirement (covered in M9) |
| **RTM** | Requirements Traceability Matrix (covered in M10) |
| **Stakeholder** | {{ROLE_LIST_OR_DEFINITION}} |

---

## 1.4 References

External documents this SRS relies on:

| ID | Reference | Why it matters here |
|----|-----------|---------------------|
| REF-01 | {{e.g., IEEE 830-1998 Recommended Practice for SRS}} | Format basis |
| REF-02 | {{e.g., GDPR Regulation (EU) 2016/679}} | M2.5 constraints, M9 NFRs |
| REF-03 | {{e.g., Company API Style Guide v3}} | M3 functional domain "API" constraints |
| REF-04 | {{e.g., Stakeholder interview transcript, CEO, 2026-04-02}} | Source for many FRs |
| REF-05 | {{e.g., Competitor X feature comparison}} | Scope rationale |

---

## 1.5 Overview

This SRS is organized into 10 modules:

| Module | Content | Read this if you... |
|--------|---------|---------------------|
| M1 | Introduction (this document) | Want context for the SRS |
| M2 | Overall Description | Need product context, user classes, constraints |
| M3 | {{DOMAIN_1}} | Build/test {{DOMAIN_1}} features |
| M4 | {{DOMAIN_2}} | Build/test {{DOMAIN_2}} features |
| M5 | {{DOMAIN_3}} | ... |
| M6 | {{DOMAIN_4}} | ... |
| M7 | {{DOMAIN_5}} (if any) | ... |
| M8 | {{DOMAIN_6}} (if any) | ... |
| M9 | Non-Functional Requirements | Care about performance, security, compliance |
| M10 | RTM + Issues + Appendix | Track requirements ↔ tests; see open issues |

### Reading order

For maximum efficiency:
- **Stakeholders / Product:** M1, M2, then specific functional modules (M3-Mx) of interest, then M9
- **Engineering:** M2.5 (constraints), then all M3-Mx, then M9, refer back to M1 for definitions
- **QA:** All M3-Mx for FRs to test, M9 for NFR baselines, M10 for RTM
- **Compliance / Audit:** M1.4 (references), M2.5 (constraints), M9 (NFRs), M10 (Issues)
- **AI agents:** Read M1 + M2 + relevant Mx; reference M10 for known gaps

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{YYYY-MM-DD}} | {{NAME}} | Initial draft |

**Status:** DRAFT — pending stakeholder review.

**Review checklist before promoting to v1.0:**
- [ ] All sections in M1-M2 reviewed by {{STAKEHOLDER_LIST}}
- [ ] All FRs in M3-Mx have priority assigned (MoSCoW)
- [ ] All FRs have at least one source citation
- [ ] M9 NFRs populated (run `nfr-specification` skill)
- [ ] M10 Open Issues triaged with stakeholders
