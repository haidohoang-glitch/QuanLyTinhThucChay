# SRS Greenfield Author — Quality Checklist

Run before delivering the SRS module set.

## Gate 1 — Coverage

- [ ] M1.1 Purpose: audience and use cases documented
- [ ] M1.2 Scope: 3-5 sentence description AND explicit out-of-scope list
- [ ] M1.3 Glossary: every domain term used in SRS is defined here
- [ ] M1.4 References: every external doc/standard cited has an ID
- [ ] M1.5 Overview: reading order per role provided
- [ ] M2.1 Product perspective: includes a context diagram
- [ ] M2.3 User classes: ≥2 classes (most products have at least end-user + admin)
- [ ] M2.4 Operating environment: platforms, runtime, regions explicit
- [ ] M2.5 Constraints: regulatory + technology + operational + business sections all populated (or marked N/A with reason)
- [ ] M2.7 Assumptions and dependencies both have entries
- [ ] M3-Mx: 4-8 functional domain modules (one per major capability)
- [ ] Each functional module has ≥5 FRs
- [ ] M9: placeholder present (will be populated by `nfr-specification`)
- [ ] M10: placeholder present, Open Issues populated

## Gate 2 — Per-FR rigor

For each FR in M3-Mx:

- [ ] ID follows `FR-{{DOMAIN_PREFIX}}-NN` format, sequential within domain
- [ ] Statement is single imperative sentence ("The system shall...")
- [ ] Details bulleted (no run-on paragraphs)
- [ ] Acceptance criteria are testable (no "should be intuitive")
- [ ] Priority (MoSCoW) assigned
- [ ] Source cited (stakeholder, document, or "Inferred" + flag)
- [ ] Verification method specified (test / demo / inspection / analysis)

## Gate 3 — Honesty discipline

- [ ] FRs marked "Inferred" if not from explicit stakeholder/document source
- [ ] Open Issues (M10.2) capture every unresolved question — do NOT pretend they don't exist
- [ ] If stakeholder review hasn't happened, document is marked **DRAFT** (not v1.0)
- [ ] Glossary terms not assumed — every domain-specific term defined explicitly

## Gate 4 — Priority sanity

- [ ] No domain has >70% of FRs as "Must" (over-prioritization)
- [ ] No domain has 0 "Must" FRs (under-prioritization)
- [ ] Priority distribution per domain noted in M.7

## Gate 5 — Scope discipline

- [ ] M3-Mx FRs are *functional* — describe what the system does. Quality/performance/security goes to M9 (NFRs)
- [ ] No FR is actually a design decision ("FR-XX shall use REST API" — design choice; remove or move to constraints)
- [ ] No FR mixes multiple requirements ("system shall X and Y" → split into 2 FRs)

## Gate 6 — Ambiguity check

For each FR, ask: "Could two engineers implement this differently and both claim compliance?"

- [ ] No FR uses vague verbs: "support", "handle", "manage", "process" without specifying how
- [ ] No FR uses subjective adjectives: "fast", "easy", "intuitive", "robust" (move to M9 NFRs with measure)
- [ ] No FR uses "and/or" — pick one
- [ ] No FR has "etc." — list exhaustively

## Gate 7 — Traceability prep

- [ ] Each FR has a unique ID — IDs do not repeat across modules
- [ ] FRs cross-reference each other when dependencies exist (FR-A "requires FR-B")
- [ ] FRs link to M2.5 constraints they implement (CON-REG-01 → FR-AUTH-04)
- [ ] M10 RTM placeholder ready to be populated by `requirements-traceability` skill

## Gate 8 — Format

- [ ] Output files at `docs/00_REQUIREMENTS/SRS_VI/M{{N}}_{{NAME}}.md`
- [ ] M1, M2, M3-Mx, M9 (placeholder), M10 (placeholder) all created
- [ ] Section numbering matches templates
- [ ] Tables have headers
- [ ] All `{{PLACEHOLDER}}` markers replaced or marked "TBD" with reason

## Self-review prompt

Re-read M2.2 (Product Functions summary) and check: does every functional capability mentioned have a corresponding FR in M3-Mx? If yes, coverage is complete. If not, add missing FRs.

Then re-read each "Must" priority FR and ask: "If we don't ship this, is the product literally unusable?" If "kind of usable", downgrade to "Should". Be honest — nobody ships 100% Musts on time.
