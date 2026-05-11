---
name: tech-solution-design
description: Design the integrated technical solution that addresses Phase 1 audit findings while satisfying SRS requirements. Produces a TECH_SOLUTION_DESIGN.md with chosen architecture, alternatives considered, key decisions (ADRs), data model evolution, integration plan, and rollout strategy. Use when Phase 1 Discovery is done and the team needs to converge on HOW to build/refactor before committing to implementation, when comparing competing architecture proposals, or when generating Phase 2 Strategic solution output. Triggers include "design the solution", "architecture proposal", "how should we build this", "tech solution design", "generate TECH_SOLUTION", or "Phase 2 Strategic design".
---

# Tech Solution Design

Convert Phase 1 findings + SRS requirements into a coherent technical solution: chosen architecture, key decisions, data evolution, integration approach, rollout strategy. Distinct from `feasibility-assessment` (which compares scenarios) and `implementation-planning` (which decomposes work).

## When this skill applies

Use when:
- Phase 1 Discovery is complete; team needs to converge on a technical direction
- Multiple architectural approaches exist; need a structured comparison + chosen direction
- Solution must satisfy both functional (SRS) and non-functional (NFR) requirements
- Producing Phase 2 Strategic solution output for company doc standard

Do NOT use for:
- Business case / ROI (use `feasibility-assessment`)
- Decomposing chosen solution into work packages (use `implementation-planning`)
- Authoring requirements (use `srs-*-author`)

## Inputs (must read first)

1. `docs/00_REQUIREMENTS/SRS_VI/M1-M9` — what must be built and to what quality
2. `docs/01_DISCOVERY/CODEBASE_MAP.md` — current technical state
3. `docs/01_DISCOVERY/DATA_ARCHITECTURE.md` — current data state + governance
4. `docs/01_DISCOVERY/TECH_DEBT_AUDIT.md` — what to fix
5. `docs/01_DISCOVERY/BUSINESS_CONTEXT.md` — domain context
6. `docs/02_STRATEGIC/FEASIBILITY_ASSESSMENT.md` (if exists) — chosen scope
7. **External:** company technology standards, regulatory constraints, vendor SLAs

## Output

`docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md`, filled from [assets/SOLUTION_DESIGN_template.md](assets/SOLUTION_DESIGN_template.md).

Optionally: separate `docs/02_STRATEGIC/SERVER_ARCHITECTURE.md` (or similar) if the solution requires a deep architectural refactor warranting its own document.

## Workflow

### Step 1 — Frame the design problem

Write the design problem in 1 paragraph:

- **What we have:** current state from Discovery (1-2 sentences)
- **What we need:** key requirements from SRS (1-2 sentences)
- **The gap:** what's missing/wrong (1-2 sentences)
- **Constraints:** budget, timeline, team capacity, technology lock-ins (1 sentence)

This becomes Section 1 of the output.

### Step 2 — Choose architecture mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — Standard architecture pattern** *(default)* | No company-locked patterns; choose based on context | Layered / Hexagonal / Clean / Service-oriented |
| **B — Honor existing architecture decisions** | Project has ADRs / locked tech stack; design extends existing | Existing ADRs and architecture docs |
| **C — User-defined architecture** | User specifies pattern (e.g., "must be event-sourced") | User input |

Selection logic:
1. User explicit → use it
2. Existing ADRs OR strong existing architecture → ask user (extend Mode B or break Mode A?)
3. Default → Mode A; pick pattern based on requirements (see Step 3)

### Step 3 — Identify candidate architectures

Generate 2-3 candidate architectures. For each:
- **Name:** common pattern name (Hexagonal, Clean, Layered + Strategy, Event-Sourced, etc.)
- **Suitability:** why it might fit
- **Strengths:** what this pattern is good at
- **Weaknesses:** trade-offs
- **Rough cost:** effort to introduce vs. status quo

Don't write 5 architectures — that's analysis paralysis. 2-3 is the sweet spot.

### Step 4 — Compare against requirements

Build a comparison matrix:

| Requirement | Candidate A | Candidate B | Candidate C |
|-------------|------------|------------|------------|
| FR-AUTH-01 | ✅ Native | ✅ Native | ⚠️ Requires adapter |
| NFR-PERF-01 | ✅ Easy | ⚠️ Cache layer needed | ❌ Conflicts |
| NFR-SEC-02 | ✅ | ✅ | ✅ |
| Team familiarity | ✅ Known | ⚠️ Mid | ❌ New |
| Migration risk from current | ⚠️ Med | ✅ Low | ❌ High |

Score each (✅ ⚠️ ❌) per requirement; tally results.

### Step 5 — Choose architecture + write ADR

Pick the winning candidate. Document the decision as an Architecture Decision Record (ADR):

- **Title:** "ADR-N: Adopt {{PATTERN}} architecture"
- **Status:** Proposed → Accepted (after review)
- **Context:** the problem (from Step 1)
- **Decision:** the chosen pattern
- **Consequences:** trade-offs accepted (positive and negative)
- **Alternatives considered:** brief paraphrase of rejected candidates + why not

ADR is the lasting artifact; future decisions reference it.

### Step 6 — Design key components

For the chosen architecture, design the major components:

- **Component name + purpose** (1 line each)
- **Interfaces:** what each component exposes (public surface)
- **Dependencies:** what each component depends on
- **Boundaries:** what each component does NOT do (anti-scope)

A component diagram (ASCII or Mermaid) helps. Don't over-detail — high-level structure, not class diagrams.

### Step 7 — Design data evolution

Most solutions touch data. Document:

- **Schema changes:** what new tables/collections, what migrations
- **Data migration plan:** how existing data moves (online migration, dual-write, etc.)
- **Compatibility:** old code reads new schema or vice versa during transition
- **Rollback:** how to undo schema if needed

Reference `DATA_ARCHITECTURE.md` for current state; this section shows target state + path.

### Step 8 — Design integration approach

How does the new solution integrate with:
- Existing systems (other services, monolith parts)
- External vendors (payment, auth, email, etc.)
- Data systems (cache, queue, warehouse)
- Monitoring / observability

For each integration: protocol, contract, failure mode, security, monitoring.

### Step 9 — Design rollout strategy

How does this go from "designed" to "in production":

- **Phasing:** which parts ship first, in what order
- **Feature flags:** what's gated behind flags during rollout
- **Gradual rollout %:** if applicable (5% → 25% → 100%)
- **Reconciliation:** for migrations, how to detect/fix divergence
- **Cutover criteria:** what conditions must hold before next phase
- **Rollback strategy:** per phase, how to revert

This is the bridge to `implementation-planning` — implementation plan converts this into WPs.

### Step 10 — Identify risks + mitigations

Solution-level risks (different from per-WP risks):

- **Architectural risks:** "Hexagonal adoption requires team training; 4 weeks productivity dip"
- **Migration risks:** "Dual-write phase exposes consistency bugs; need reconciliation cron"
- **Vendor risks:** "Reliance on single vendor; switching cost high"
- **Regulatory risks:** "GDPR right-to-export must be tested before launch in EU"

Document each with mitigation.

### Step 11 — Self-review

Run [references/checklist.md](references/checklist.md). Solution design is the most "creative" Phase 2 skill — discipline matters most here.

## Quality bar

A good solution design lets:
- An architect-level reviewer check the design is sound (not just "looks good")
- An engineer estimate effort to build (sufficient detail to scope)
- A QA lead identify what testing strategies apply (unit, integration, contract, perf)
- A stakeholder understand the trade-offs and chosen trade-offs (ADR)
- An auditor verify NFRs/compliance can be met by design (not just hoped for)

If the design has unresolved "we'll figure that out later", those are Open Questions to surface — not glossed over.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations: greenfield vs. modernization vs. migration; monolith vs. service-oriented; data-heavy vs. compute-heavy; regulated industries; open-source-first.

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: "Project Helix" (continued) — designing the migration from monolith to multi-region distributed system.

## Failure modes to avoid

- **Over-detailed.** The solution design isn't the final code. Stay at component-and-interface level; class details belong in implementation.
- **Under-detailed.** "Use microservices" is not a design. Specify which services, contracts, data ownership.
- **Single architecture.** One option is advocacy; design needs alternatives in Section 4.
- **No ADR.** The decision must be captured for future reference. Future readers need to know WHY.
- **Skipping rollout strategy.** "Then we deploy" is not a strategy. Phasing, flags, reconciliation, cutover criteria are mandatory for any non-trivial change.
- **Optimistic assumptions.** Same as feasibility — assumptions must be explicit.
- **Forcing a pattern that doesn't fit.** Hexagonal is not always right. Match pattern to context (Mode A is selection, not prescription).
- **Confusing solution with implementation.** Solution = architecture + decisions. Implementation = WPs + tests + rollout. Don't blur.
