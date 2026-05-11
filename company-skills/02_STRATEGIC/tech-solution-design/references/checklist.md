# Tech Solution Design — Quality Checklist

Run before delivering TECH_SOLUTION_DESIGN.md.

## Gate 1 — Problem framing

- [ ] Section 1 frames problem in 4 sentences max
- [ ] Current state cites Phase 1 outputs (not invented from memory)
- [ ] Constraints are concrete, not aspirational

## Gate 2 — Candidate alternatives

- [ ] Section 3 has 2-3 candidates (not 1; not 5+)
- [ ] Each candidate has Strengths + Weaknesses (not just upside)
- [ ] Candidates are genuinely different (not 3 flavors of "microservices")
- [ ] Section 4 comparison matrix scores against actual requirements (FRs, NFRs from SRS)

## Gate 3 — ADR rigor

- [ ] Section 5 ADR present with: Status, Context, Decision, Consequences (positive + negative), Alternatives rejected
- [ ] Negative consequences are non-trivial (every choice has costs; if listed costs are tiny, you didn't think hard enough)
- [ ] Rejected alternatives have reasons, not "we chose X instead"
- [ ] Revisit conditions explicit (when does this decision become wrong?)

## Gate 4 — Component design

- [ ] Section 6 has component diagram (visual or ASCII)
- [ ] Each component has Purpose + Public interface + Dependencies + Anti-scope
- [ ] Anti-scope is non-empty for each component (else component boundary is unclear)
- [ ] If folder structure changes, target structure shown

## Gate 5 — Data evolution

- [ ] Section 7 distinguishes additive (online) vs breaking (requires migration)
- [ ] Migration approach specified per change (not just "we'll migrate")
- [ ] Reconciliation strategy explicit
- [ ] Rollback per migration item

## Gate 6 — Integration plan

- [ ] Section 8: every external system has Protocol, Contract, Failure mode, Monitoring
- [ ] Internal integrations distinguished from external
- [ ] Cross-cutting concerns (auth, authz, observability, errors, config) addressed

## Gate 7 — Rollout strategy

- [ ] Section 9 has phased rollout, not "deploy and pray"
- [ ] Each phase has cutover criteria (measurable)
- [ ] Each phase has rollback approach
- [ ] Feature flags identified by name where used
- [ ] Rollout % stages specified for traffic-affecting changes

## Gate 8 — NFR verification

- [ ] Section 10 maps each major NFR class to verification approach
- [ ] Performance NFRs: load test plan stated
- [ ] Security NFRs: audit/test approach stated
- [ ] Compliance NFRs: control mapping noted

## Gate 9 — Risk discipline

- [ ] Section 11 has ≥3 solution-level risks (different from per-WP risks)
- [ ] Each risk has Likelihood + Impact + Mitigation
- [ ] Risks acknowledge solution's weak points, not just praise

## Gate 10 — Open Questions

- [ ] Section 13 has ≥2 OQs
- [ ] OQs have specific next steps, not "investigate"

## Gate 11 — Mode discipline

- [ ] Mode A: pattern chosen with rationale; doesn't impose pattern that doesn't fit
- [ ] Mode B: existing ADRs cited; design extends rather than breaks
- [ ] Mode C: user-defined approach respected

## Gate 12 — Format

- [ ] Output: `docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md`
- [ ] ADR uses standard structure (Status, Context, Decision, Consequences)
- [ ] Component names consistent (don't rename mid-document)
- [ ] References to SRS use IDs (FR-XXX, NFR-XXX)

## Self-review prompt

Read as the engineer who'll implement this. Ask: "Do I know enough to start? What's still ambiguous?" Sharpen ambiguous areas or move to OQ.

Read as a future architect 2 years out. Ask: "Could I understand WHY this was chosen?" If ADR is thin, sharpen.

Read as an auditor. Ask: "Does the design demonstrate compliance NFR achievement, or just hope?" If it's hope, add explicit verification approach.
