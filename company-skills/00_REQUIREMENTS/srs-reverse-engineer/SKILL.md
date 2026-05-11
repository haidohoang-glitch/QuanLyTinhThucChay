---
name: srs-reverse-engineer
description: Reverse-engineer a Software Requirements Specification (SRS) from an existing codebase, UI, and Phase 1 Discovery outputs. Produces a 10-module SRS that captures what the system already does as formal requirements, suitable for compliance audits, handover documentation, regulatory submissions, or as input to a planned rewrite. Use when the codebase exists but no SRS does, when preparing audit/handover, before a major refactor, or when a regulator demands formal documentation. Triggers include "extract SRS from code", "reverse-engineer requirements", "document existing system as SRS", "create SRS for legacy", or "Phase 0 Requirements legacy".
---

# SRS Reverse Engineer

Extract a formal SRS from an existing system. Output mirrors `srs-greenfield-author` (10-module structure) but is derived from code, UI, and prior Discovery outputs rather than from stakeholder interviews about a future product.

## When this skill applies

Use when:
- Codebase exists; no SRS exists
- Compliance audit demands formal requirements documentation (SOC2, ISO 27001, FDA, GDPR DPA)
- Handover from departing team needs a stable SRS as canonical reference
- Pre-rewrite work: capture current state as "as-is SRS" before drafting "to-be SRS" with `srs-greenfield-author`
- Vendor/customer relationship requires SRS as contract artifact

Do NOT use for:
- Greenfield projects (use `srs-greenfield-author` instead)
- Code mapping (use `codebase-discovery`)
- Domain extraction (use `business-context-capture` — that's an input to this skill)
- Lightweight feature documentation (overkill)

## Inputs (must read first)

This skill is downstream of Phase 1 Discovery. Read in order:

1. **`docs/00_REQUIREMENTS/CONTEXT_PACK.md`** *(strongly recommended, from `project-context-ingestion`)* — stakeholder voice, business constraints, regulatory citations, contradictions. Layers business INTENT on top of code findings. Without it, the reverse-engineered SRS describes only what the code does, never why — and silently encodes obsolete assumptions.
2. **`docs/01_DISCOVERY/BUSINESS_CONTEXT.md`** — actors, use cases, business rules, workflows, invariants. Most important code-derived input — provides the business view that becomes M2-M8.
3. **`docs/01_DISCOVERY/CODEBASE_MAP.md`** — technical structure, entry points, dependencies. Provides M2.1 product perspective and M2.4 operating environment.
4. **`docs/01_DISCOVERY/DATA_ARCHITECTURE.md`** — data layers, governance constraints. Provides M2.5 constraints (regulatory, technology) and seeds M9 NFRs.
5. **`docs/01_DISCOVERY/TECH_DEBT_AUDIT.md`** *(optional)* — issues that may inform M2.7 assumptions and M10 open issues.
6. **Live UI** — actual screens to confirm workflows captured in business-context match reality.

If `BUSINESS_CONTEXT.md` does not exist, run `business-context-capture` first. Without it, this skill is guessing. If `CONTEXT_PACK.md` is also missing, expect M10 Open Issues to be heavy — the SRS will need stakeholder verification on intent before it's audit-grade.

## Outputs

Same files as `srs-greenfield-author`:
- `docs/00_REQUIREMENTS/SRS_VI/M1_Introduction.md`
- `docs/00_REQUIREMENTS/SRS_VI/M2_Overall_Description.md`
- `docs/00_REQUIREMENTS/SRS_VI/M3_<Domain>.md` ... `Mx_<Domain>.md`
- `docs/00_REQUIREMENTS/SRS_VI/M9_Non_Functional_Requirements.md` (placeholder for `nfr-specification`)
- `docs/00_REQUIREMENTS/SRS_VI/M10_RTM_Issues_Appendix.md` (placeholder for `requirements-traceability`)

Templates: shared with `srs-greenfield-author` — see [assets/](assets/).

## Workflow

### Step 1 — Verify inputs are recent

Before extracting:
- Check git timestamps on `BUSINESS_CONTEXT.md` and `CODEBASE_MAP.md`. If older than 60 days, refresh first — code may have drifted.
- Sample 3-5 files in code to confirm they still match descriptions in Discovery outputs.
- If discrepancies found, **stop and refresh Discovery outputs**. SRS based on stale Discovery is worse than no SRS.

### Step 2 — Choose mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — Standard reverse-engineering** *(default)* | No existing SRS; prior team didn't formalize | Code + UI + Discovery outputs |
| **B — Honor partial existing SRS** | Older SRS exists; need to refresh/extend, not replace | Existing SRS as base, augment |
| **C — User-defined extraction scope** | User specifies what to document (e.g., "only API endpoints", "only billing module") | User input scope |

Selection logic:
1. User explicit → use it
2. Partial SRS exists in repo (`docs/`, `requirements/`) → ask user (Mode A or B?)
3. Default → Mode A

### Step 3 — Write M1: Introduction (mostly inferred)

Use [assets/M1_template.md](assets/M1_template.md). For reverse-engineering:

- **1.1 Purpose:** "This SRS documents the *current state* of {{PROJECT}} as of {{DATE}}". State explicitly that this is a reverse-engineered "as-is" SRS, not a "to-be" specification.
- **1.2 Scope:** Extract from `CODEBASE_MAP.md` Section 1 + `BUSINESS_CONTEXT.md` Section 1. Include explicit out-of-scope from what code does NOT do.
- **1.3 Glossary:** From `BUSINESS_CONTEXT.md` Section 5 (Domain Entities) and Terminology Notes. Use product's terminology consistently.
- **1.4 References:** Cite git commit hash for traceability ("This SRS reflects code state at commit `abc123`"). Cite regulations from `DATA_ARCHITECTURE.md` Section 6 (governance).
- **1.5 Overview:** Same reading order guidance as greenfield.

### Step 4 — Write M2: Overall Description (mostly inferred)

- **2.1 Product perspective:** Synthesize from `CODEBASE_MAP.md` Section 1 (project shape) and Section 5 (external services).
- **2.2 Product functions:** From `BUSINESS_CONTEXT.md` Section 4 — high-level groupings of use cases.
- **2.3 User classes:** From `BUSINESS_CONTEXT.md` Section 3 (Actors) verbatim.
- **2.4 Operating environment:** From `CODEBASE_MAP.md` Section 2 (Tech stack), Section 6 (Build & Deploy).
- **2.5 Design constraints:** This is the trickiest section. Constraints in reverse-engineered SRS are often **implicit**:
  - Technology constraints: tech stack listed in `CODEBASE_MAP.md` (e.g., "stuck with Postgres" — not a constraint, but listed because changing breaks things)
  - Regulatory constraints: from `DATA_ARCHITECTURE.md` Section 6 (governance audit) and from regulations user states apply (HIPAA, PCI, GDPR)
  - Operational constraints: deployment model, regions, vendors locked-in
  - Distinguish "intentional constraint" (deliberate decision) from "accidental constraint" (legacy lock-in). Mark accidental ones for review.
- **2.6 User documentation:** What docs already exist (README, user manual, API docs).
- **2.7 Assumptions:** From `BUSINESS_CONTEXT.md` Section 9 (Tensions) and from inferred behaviors. Include explicitly: "This SRS assumes the system continues operating as observed at {{DATE}}".

### Step 5 — Map functional domains (from BUSINESS_CONTEXT)

Use the domain decomposition already done in `BUSINESS_CONTEXT.md`:

- If `BUSINESS_CONTEXT.md` used Mode A (DDD-lite), each major domain area becomes M3-Mx
- If Mode B (codebase's bounded contexts), follow that decomposition
- If Mode C (user-defined), follow that

Typical: 4-8 domains. Naming should match `BUSINESS_CONTEXT.md` for consistency.

### Step 6 — Convert use cases to functional requirements

For each use case in `BUSINESS_CONTEXT.md` Section 4, write a corresponding FR:

| Source (use case) | Becomes (FR) |
|-------------------|--------------|
| "User can transfer funds between own wallets" | FR-WAL-01: The system shall allow users to transfer funds between their own wallets. |

Add details from code:
- Validation rules from `BUSINESS_CONTEXT.md` Section 6 → FR details
- Acceptance criteria derived from existing code paths and tests (if any)
- Priority: usually all "Must" for reverse-engineered (the system already does it)

**Important:** mark each FR's source as **"Reverse-engineered from code"** with the file path. Do NOT pretend stakeholder interviews happened.

Use [assets/Mx_FunctionalDomain_template.md](assets/Mx_FunctionalDomain_template.md) — same template, different sourcing approach.

### Step 7 — Capture business rules and invariants

From `BUSINESS_CONTEXT.md`:
- Section 6 Business Rules → FR details
- Section 8 Invariants → cross-cutting requirements (often appear in multiple FRs); document in M2.5 constraints OR as a dedicated cross-cutting subsection in relevant Mx modules

If an invariant is **not currently enforced** (per business-context audit), flag this in M10 Open Issues. The SRS captures intent; if reality diverges, that's a known issue.

### Step 8 — Identify reverse-engineering gaps

Things you cannot determine from code/UI alone:

- **Why** a behavior is the way it is (intent vs accidental)
- Whether undocumented behavior is **intentional** or a **bug**
- **Future direction**: what was planned but not built?
- **Stakeholder-required-but-not-implemented** behaviors (rare — but possible)
- Behaviors gated by feature flags (you may see only one path)

Document these in M10 Open Issues. The reverse-engineered SRS does not pretend to know intent it cannot derive.

### Step 9 — Generate M9 and M10 placeholders

Same as `srs-greenfield-author` — placeholders for downstream skills (`nfr-specification`, `requirements-traceability`).

For reverse-engineered SRS, M9 has a head start: `DATA_ARCHITECTURE.md` Section 6 (governance) and `TECH_DEBT_AUDIT.md` Section 6 (NFR-related findings) provide raw NFR material. Note this in the placeholder.

### Step 10 — Self-review

Run [references/checklist.md](references/checklist.md). Particular focus:
- Confidence levels (more inference = lower confidence; mark explicitly)
- Source citations (every FR cites code path, not invented stakeholder)
- Open Issues populated (every reverse-engineering has gaps)

## Quality bar

A good reverse-engineered SRS lets:
- An auditor verify what the system currently does (with code citations as evidence)
- A new engineer understand the product's behavior without reading every file
- A planner draft a "to-be" SRS for rewrite based on knowing the "as-is"
- A regulator accept the system as documented (with appropriate sign-offs)

If the SRS describes behavior the code does not exhibit, it's wrong (and dangerous — auditors will catch it).

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations by reverse-engineering context: legacy with no docs, codebase with partial docs, post-acquisition handover, regulatory after-the-fact, pre-rewrite "as-is" capture.

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: "Project Anchor", a 7-year-old internal CRM being formalized for SOC2 compliance.

## Failure modes to avoid

- **Inventing intent.** "FR-XXX-04 is intended to..." — you don't know intent. Stick to what the system does. Move "should it do this?" to M10 Open Issues.
- **Sourcing FRs to "stakeholders" who never confirmed them.** Source field must be "Reverse-engineered from `path/to/file.ts:42`", not "CEO interview".
- **Overstating priority.** Default to "Currently Implemented" rather than MoSCoW; or, mark all as Must but add a separate field "Was this intentional?" to flag candidates for removal.
- **Missing the implicit constraints.** Code locks you into many things you didn't choose. Document these honestly in M2.5 — auditors and rewrite teams need this.
- **Dressing up debt as requirement.** If something is buggy or accidental, document it as an Open Issue, not as a requirement to be preserved. Otherwise the SRS becomes a contract to keep the bug.
- **Skipping live UI verification.** Code may not run; configs may differ from prod. If you can't verify a behavior actually executes in the live system, mark FR as "Inferred — not verified live".
- **Pretending no gaps exist.** Reverse-engineering ALWAYS has gaps. M10 Open Issues should be substantial (10+ items typical) — small list = under-thoroughness.
