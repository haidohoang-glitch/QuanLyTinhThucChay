# Data Architecture Audit — Quality Checklist

Run before delivering `DATA_ARCHITECTURE.md`. Do not deliver until all gates pass; document exceptions in Section 9.

## Gate 1 — Coverage

- [ ] Every store discovered in Step 1 appears in Section 2
- [ ] Every primary store (L4/L5 in Mode A, equivalent in B/C) has a schema entry in Section 3
- [ ] Every major data type (≥3) has a write path AND read path in Section 4
- [ ] Section 5 has cost data for every store, OR explicitly marks it "Unknown"
- [ ] Section 6 governance table has a row for every concern (no skipping)
- [ ] Section 7 has ≥3 risk findings (or explicit "no risks found, here's what was checked")
- [ ] Section 8 Open Questions has ≥3 items
- [ ] Section 9 documents the **classification mode** and rationale

## Gate 2 — Honesty

- [ ] No invented facts — every claim is verifiable from code, configs, or live measurements
- [ ] "Unknown — needs measurement" is used instead of guessing for usage/cost numbers
- [ ] If a governance check could not be performed, the row says "Could not verify" not "✅"
- [ ] Confidence rating reflects reality, not optimism

## Gate 3 — Severity calibration

- [ ] P0 findings represent ACTIVE incidents or immediate compliance breaches (not latent risks)
- [ ] P1 findings have an articulated 90-day failure mode
- [ ] No "P0 inflation" (calling everything P0 to get attention)
- [ ] Each finding has evidence: file path, line number, query result, or config snippet

## Gate 4 — Scope discipline

This skill produces a *data-layer* audit. It must NOT include:

- [ ] No code quality issues unrelated to data (those go to `tech-debt-audit`)
- [ ] No solution proposals (those go to `tech-solution-design`)
- [ ] No business logic explanation (that goes to `business-context-capture`)
- [ ] No implementation plans (those go to `implementation-planning`)

If you find yourself proposing "we should migrate to X" — stop, move that idea to a follow-up note for Phase 2.

## Gate 5 — PII rigor

- [ ] Every field that could be PII is listed in Section 6's PII field map
- [ ] PII checks include: name, email, phone, address, government IDs, financial accounts, health data, biometric data, IP addresses (if regulated jurisdiction)
- [ ] For each PII field, verified WHERE it is stored, not just whether it exists
- [ ] If user-deletion was tested, evidence (e.g., "manually verified delete cascades to backup tier") is recorded

## Gate 6 — Format

- [ ] Output filename: `DATA_ARCHITECTURE.md`
- [ ] Output location: `docs/01_DISCOVERY/DATA_ARCHITECTURE.md`
- [ ] All section headings match the template (do not rename or reorder)
- [ ] Risk IDs use format `R-01`, `R-02`, ... (not random labels)
- [ ] Open Question IDs use format `OQ-1`, `OQ-2`, ...

## Self-review prompt

Re-read your output as a compliance auditor. Ask: "If I had to swear under oath that this is accurate, what would I be uncomfortable signing?" Move those items to Open Questions or downgrade the confidence claim.
