# Phase 1 Orchestrator — Quality Checklist

## Gate 1 — Pre-flight

- [ ] Project type confirmed legacy (non-empty src/)
- [ ] Codebase access verified
- [ ] Mode (A/B/C/D) selected with rationale
- [ ] Existing Phase 1 docs archived if refresh

## Gate 2 — Step completion

- [ ] Step 1 codebase-discovery → CODEBASE_MAP.md
- [ ] Step 2 data-architecture-audit → DATA_ARCHITECTURE.md
- [ ] Step 3 business-context-capture → BUSINESS_CONTEXT.md
- [ ] Step 4 tech-debt-audit → TECH_DEBT_AUDIT.md
- [ ] Each component skill's checklist passed

## Gate 3 — Inter-skill consistency

- [ ] CODEBASE_MAP entries referenced consistently in DATA_ARCH + BUSINESS_CONTEXT + TECH_DEBT
- [ ] DATA_ARCH PII findings cross-referenced with CONTEXT_PACK Section 7.1 (if exists)
- [ ] BUSINESS_CONTEXT cross-referenced with CONTEXT_PACK Section 3 (if exists)
- [ ] TECH_DEBT findings cite specific files from CODEBASE_MAP

## Gate 4 — Honesty markers

- [ ] CODEBASE_MAP coverage % stated (read vs sample)
- [ ] DATA_ARCH limitations stated (e.g., "production DB not accessible")
- [ ] BUSINESS_CONTEXT ambiguities flagged in Section 9 Open Questions
- [ ] TECH_DEBT severity calibrated (Critical ≤ 10 for medium project)

## Gate 5 — Code-stakeholder reconciliation

- [ ] If CONTEXT_PACK exists: BUSINESS_CONTEXT notes any code-vs-stakeholder mismatches
- [ ] Mismatches in Section 9 Open Questions for Phase 0 SRS to resolve
- [ ] Not silently picked one side over the other

## Gate 6 — Phase report

- [ ] `_phase_report_<DATE>.md` generated
- [ ] Run summary with timing per skill
- [ ] Top 3 Critical tech debt findings highlighted
- [ ] Next-phase recommendation

## Self-check

Pick 3 random business rules from BUSINESS_CONTEXT. For each:
- Open cited file:line
- Verify rule actually present in code
- Verify business interpretation is reasonable

Pick 3 tech-debt findings (1 each Critical/High/Medium). For each:
- Verify finding is real (not noise from auto-detect)
- Verify severity matches actual impact
- Verify cost estimates are honest (range, not single number)

If 1+ fails → re-run problematic component skill.
