---
name: srs-greenfield-author
description: Author a Software Requirements Specification (SRS) for a new project before any code exists. Produces a 10-module SRS following IEEE 830 conventions (introduction, overall description, functional requirements per domain, NFRs, RTM placeholder) from product vision, business goals, and stakeholder input. Use when starting a greenfield project, drafting a formal requirements document for stakeholder approval, before solution design begins, or generating Phase 0 Requirements output for the company doc standard. Triggers include "write SRS", "create requirements doc", "spec a new project", "author SRS for greenfield", or "Phase 0 Requirements greenfield".
---

# SRS Greenfield Author

Author a formal Software Requirements Specification for a new project where no code exists. Output is a multi-file 10-module SRS (M1-M10) following IEEE 830-style structure, suitable for stakeholder review, vendor RFPs, regulatory submissions, and as input to subsequent design.

## When this skill applies

Use when:
- Starting a new project with stakeholder input but no code
- Drafting requirements for procurement / vendor selection
- Producing a regulatory submission (SOC2 / ISO 27001 / FDA / similar requires formal SRS)
- Creating a contract appendix specifying what will be built
- Generating Phase 0 Requirements output for company doc standard

Do NOT use for:
- Existing codebase (use `srs-reverse-engineer` instead)
- Lightweight feature spec (overkill — write a one-pager)
- Solution design (use `tech-solution-design` after SRS exists)
- Non-functional requirements only (use `nfr-specification` standalone)

## Inputs (must gather before drafting)

**Strongly recommended:** run `project-context-ingestion` first to consolidate raw stakeholder voice + constraints into `docs/00_REQUIREMENTS/CONTEXT_PACK.md`. If a CONTEXT_PACK exists, read it FIRST — Sections 3 (stakeholder voice), 4 (business context), 7 (constraints), 8 (contradictions), and 12 (open questions) supply most of items 1-6 below with citations.

If no CONTEXT_PACK exists, gather these directly:

1. **Product vision** — what problem this solves, for whom
2. **Stakeholder list** — who decides scope, who pays, who uses
3. **Business goals** — what success looks like in business terms (revenue, users, compliance)
4. **Constraints** — budget, timeline, regulatory, technology choices already locked
5. **Glossary inputs** — domain terminology used by stakeholders
6. **Reference materials** — existing similar systems, competitor analysis, regulatory docs

If any of these are missing or hand-wavy, the SRS will be hand-wavy. Flag missing inputs as Open Questions in M10 rather than inventing. (CONTEXT_PACK Section 8 contradictions and Section 12 open questions feed M10 directly.)

## Outputs

Multiple files:
- `docs/00_REQUIREMENTS/SRS_VI/M1_Introduction.md` (or localized name)
- `docs/00_REQUIREMENTS/SRS_VI/M2_Overall_Description.md`
- `docs/00_REQUIREMENTS/SRS_VI/M3_<Domain>.md` through `Mx_<Domain>.md` (one per functional domain)
- `docs/00_REQUIREMENTS/SRS_VI/M9_Non_Functional_Requirements.md` (placeholder; use `nfr-specification` to populate)
- `docs/00_REQUIREMENTS/SRS_VI/M10_RTM_Issues_Appendix.md` (placeholder; use `requirements-traceability` to populate)

Templates: [assets/M1_template.md](assets/M1_template.md), [assets/M2_template.md](assets/M2_template.md), [assets/Mx_FunctionalDomain_template.md](assets/Mx_FunctionalDomain_template.md), [assets/M9_NFR_placeholder.md](assets/M9_NFR_placeholder.md), [assets/M10_RTM_placeholder.md](assets/M10_RTM_placeholder.md).

## Workflow

### Step 1 — Confirm scope before writing

Before drafting, write 3 sentences and confirm with user:
1. **Who** uses this product (primary actors)
2. **What** it does for them (core value)
3. **Boundary** — what it does NOT do (the most useful sentence)

If you cannot write these 3 sentences after reading inputs, you do not know enough yet. Ask the user before continuing.

### Step 2 — Choose SRS structure mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — IEEE 830 standard** *(default)* | No special instruction | The 10-module structure below |
| **B — Honor company's SRS template** | Company has its own SRS template/standard (often required for regulated industries) | Company template |
| **C — User-defined structure** | User specifies own structure (e.g., agile user-story based, BDD scenarios) | User input |

Selection logic:
1. User explicit → use it
2. Company has formal SRS template → ask user (Mode A or B?)
3. Default → Mode A

#### Mode A — Standard 10 modules

| Module | Content |
|--------|---------|
| M1 | Introduction (purpose, scope, definitions, references, overview) |
| M2 | Overall Description (product perspective, user classes, operating environment, assumptions, constraints) |
| M3-M8 | Functional Requirements (one module per functional domain — vary by project) |
| M9 | Non-Functional Requirements |
| M10 | RTM + Issues + Appendix |

#### Mode B — Honor company template

If your company has a fixed SRS template (e.g., based on a regulator-required format), follow it. Common variations:
- ISO/IEC/IEEE 29148 format (more comprehensive than 830)
- Government-style (e.g., USDS, EU procurement) often has different sections
- ISO 13485 medical device format

Cite source template in M1 references section.

#### Mode C — User-defined

Examples:
- Agile: User stories grouped by epic, no formal IEEE structure
- BDD: Feature files (Given/When/Then) as primary requirements form
- Hybrid: M1/M2/M9/M10 formal, M3-M8 as user stories

Confirm structure with user.

### Step 3 — Write M1: Introduction

Use [assets/M1_template.md](assets/M1_template.md). Sections:

- **1.1 Purpose** — why this SRS exists, who reads it
- **1.2 Scope** — product name, what it does (3-5 sentences max)
- **1.3 Definitions, acronyms** — every domain term used in SRS, defined here
- **1.4 References** — laws, standards, contracts, prior docs
- **1.5 Overview** — how to read this SRS (which modules cover what)

The hardest part: scope. Write a one-paragraph answer to "what is this product?" then verify it with stakeholders before continuing.

### Step 4 — Write M2: Overall Description

Use [assets/M2_template.md](assets/M2_template.md). Sections:

- **2.1 Product perspective** — context: standalone? part of larger system? replacing existing? (include system context diagram)
- **2.2 Product functions** — high-level function summary (NOT detailed FRs yet — those are in M3-M8)
- **2.3 User classes & characteristics** — who uses it, their tech literacy, frequency of use, privileges
- **2.4 Operating environment** — platforms, browsers, devices, OS, integration with other systems
- **2.5 Design & implementation constraints** — what's fixed (regulatory, technology stack, third-party dependencies, hardware)
- **2.6 User documentation** — what user-facing docs will exist (manual, online help, training)
- **2.7 Assumptions and dependencies** — what's assumed true; what depends on external factors

The most overlooked section is **2.5 Constraints**. Get this right — these are non-negotiable boundaries that shape M3-M8 design space.

### Step 5 — Identify functional domains

From the product vision, decompose into 4-8 functional domains. Examples:

| Product type | Typical domains |
|-------------|-----------------|
| Banking app | Authentication, Account Management, Transactions, Investment, Reporting, Notifications |
| E-commerce | User Management, Catalog, Cart & Checkout, Order Management, Payment, Fulfillment |
| Learning platform | User Management, Content Library, Assignments, Progress Tracking, Reporting |
| Healthcare | Patient Records, Appointments, Clinical Notes, Billing, Compliance/Audit |

Each domain becomes one module (M3 through Mx).

If you have <4 domains, you're under-decomposing. If >8, you're over-decomposing — group related ones.

### Step 6 — Write each functional module (M3-Mx)

For each domain, use [assets/Mx_FunctionalDomain_template.md](assets/Mx_FunctionalDomain_template.md). Each module contains:

- **Domain overview** — what this module covers in 1 paragraph
- **Functional requirements (FR-XXX-NN format)** — each FR is:
  - **Atomic** — one requirement, one statement
  - **Testable** — observable success/failure criteria
  - **Unambiguous** — no "should be intuitive"; specify what
  - **Traceable** — has a unique ID (FR-AUTH-01, FR-CART-02, etc.)
  - **Source** — cite stakeholder, regulation, or business goal that motivates it
  - **Priority** — Must / Should / Could / Won't (MoSCoW)

Example of a good FR:
> **FR-AUTH-04** — User Login with Email + Password
> The system shall authenticate users via email + password combination.
> - Email format validated per RFC 5322
> - Password minimum 12 chars, must include 1 number and 1 special char
> - Failed login attempts logged with timestamp + IP
> - 5 consecutive failures lock account for 15 minutes
> - **Priority:** Must
> - **Source:** Stakeholder interview (CEO, 2026-04-02); regulatory NIST SP 800-63B
> - **Verification:** Acceptance tests TC-AUTH-01..05

Bad FR (do not write):
> The system should be user-friendly and easy to log in.

### Step 7 — Cross-reference between modules

After writing all functional modules, cross-link:
- FRs that depend on other FRs (e.g., FR-CART-03 requires FR-AUTH-04 for logged-in user check)
- FRs that share data entities (use M2's data dictionary as anchor)
- FRs that share NFR constraints (link forward to M9 placeholders)

### Step 8 — Generate M9 placeholder

Create [assets/M9_NFR_placeholder.md](assets/M9_NFR_placeholder.md) — a stub indicating M9 will be populated by `nfr-specification` skill. Do NOT fill out NFRs in this skill; that's a separate skill's scope.

### Step 9 — Generate M10 placeholder

Create [assets/M10_RTM_placeholder.md](assets/M10_RTM_placeholder.md) — a stub. M10 has 3 parts:
- RTM (populated by `requirements-traceability` skill once code+tests exist)
- Open Issues (you populate in this skill)
- Appendix (any supporting tables, diagrams, mock data)

Open Issues = unresolved scope questions for stakeholder follow-up. Capture them now — do not pretend the SRS is complete when it isn't.

### Step 10 — Self-review

Run [references/checklist.md](references/checklist.md). Do not deliver until all gates pass.

## Quality bar

A good SRS lets:
- A new engineer estimate effort to build (without code samples)
- A QA engineer write test plans (each FR is testable)
- A regulator/auditor verify scope (each FR cites source)
- A stakeholder identify what's in scope vs out (boundaries clear)
- A vendor bid on the work (atomic, complete enough to scope)

If the SRS produces ambiguity in any of these, it's incomplete.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations: regulated industries (FDA, financial, healthcare), agile teams (FRs as user stories), B2B procurement (contract appendix), and consumer products (lighter formal weight).

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: "Project Atrium", a small business invoicing SaaS — 4 functional domains, 47 FRs.

## Failure modes to avoid

- **"Should be user-friendly" syndrome.** Replace with measurable: "User can complete checkout in ≤3 clicks from cart page". If not measurable, it's not a requirement, it's a wish.
- **Inventing requirements not from stakeholder input.** Every FR should trace to source. "I think we need this" is not source.
- **Skipping M2.5 Constraints.** This section saves 100x its writing time later when design hits these constraints.
- **Mixing FRs and NFRs.** "FR-AUTH-04: System shall authenticate quickly" — "quickly" is NFR. Move the NFR to M9.
- **Vague priorities.** "All Must" is wishful thinking. Force ranking — usually 30-50% Must, 30-40% Should, rest Could.
- **No glossary.** Domain experts use jargon casually. Define every term in M1.3 — readers from outside the domain need it.
- **Pretending the SRS is "done".** If stakeholders haven't reviewed, FRs without source, ambiguous scope — say so in M10 Issues. SRS is iterative.
