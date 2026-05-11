# Phase 2 Orchestrator — Quality Checklist

## Gate 1 — Pre-flight integrity

- [ ] Phase 0 complete (M1-M10 verified)
- [ ] Phase 1 complete if legacy (4 docs verified)
- [ ] Stakeholder approver named + role identified
- [ ] Tech lead approver named + role identified
- [ ] Operator confirmed timeline expectations (1-2 weeks elapsed)

## Gate 2 — Step 1 feasibility integrity

- [ ] FEASIBILITY_ASSESSMENT.md generated
- [ ] All 3 scenarios + Do nothing baseline present
- [ ] Each scenario has cost, benefit, risk, timeline, ROI
- [ ] All numbers cite source (no fabricated estimates)
- [ ] Operator recommendation present + justified
- [ ] AI did NOT claim "scenario X is the best" — only operator recommendation

## Gate 3 — G1 stakeholder approval (HARD GATE)

- [ ] Approval artifact saved to docs/02_STRATEGIC/_decisions/
- [ ] Approval explicitly names approved scenario
- [ ] Approver name + role + date documented
- [ ] If verbal approval, written record (email/minutes/Slack quote) attached
- [ ] If approval is conditional, conditions documented
- [ ] Orchestrator REFUSED to start Step 2 without artifact

## Gate 4 — Step 2 tech-solution-design integrity

- [ ] TECH_SOLUTION_DESIGN.md generated for approved scenario only
- [ ] ≥3 candidates considered per major architectural decision
- [ ] Each ADR has all 4 sections (Context/Decision/Alternatives Considered/Consequences)
- [ ] Constraints from CONTEXT_PACK Section 7.2 honored (not contradicted)
- [ ] M9 NFRs respected in design

## Gate 5 — G2 architecture approval (HARD GATE)

- [ ] Approval artifact saved to docs/02_STRATEGIC/_decisions/
- [ ] Tech lead name + date documented
- [ ] If conditional approval, modifications listed + applied
- [ ] Orchestrator REFUSED to start Step 3 without artifact

## Gate 6 — Step 3 implementation-planning integrity

- [ ] MASTER_PLAN.md generated
- [ ] PHASE_*.md files in 03_EXECUTION/work-packages/
- [ ] Timeline fits approved scenario budget + deadline
- [ ] Per-WP: scope + FR coverage + dependencies + effort + owner
- [ ] Critical path identified
- [ ] WP count reasonable (10-30 typical)
- [ ] No WP >2 weeks effort (decompose further if so)
- [ ] No WP <1 day effort (merge if so)

## Gate 7 — Inter-step coherence

- [ ] FEASIBILITY scenario → TECH_SOLUTION_DESIGN scope match
- [ ] TECH_SOLUTION_DESIGN ADRs → MASTER_PLAN architecture decisions reflected
- [ ] MASTER_PLAN WPs → SRS FR coverage complete (all Must FRs in some WP)

## Gate 8 — Phase report

- [ ] `_phase_report_<DATE>.md` generated
- [ ] G1, G2 artifact paths referenced
- [ ] Approved scenario + ADRs summarized
- [ ] Phase 3 hand-off recommendations present

## Self-check

Pick approved scenario from G1. Open MASTER_PLAN. Verify:
- Total budget in plan ≤ approved budget
- Total timeline in plan ≤ approved timeline
- Critical FRs (Must) all covered in WPs
- ADRs from Step 2 reflected in WP architecture descriptions

If any fails → Phase 2 has internal inconsistency. Re-loop affected step.

Pick 2 random ADRs. For each:
- Verify Alternatives Considered section is non-trivial (not "we picked X because")
- Verify Consequences section names downside (not just upside)
- Verify constraints honored (vendor lock, NFR, budget)

If 1+ fails → re-run Step 2 with stronger guidance.
