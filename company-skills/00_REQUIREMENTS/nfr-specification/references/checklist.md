# NFR Specification — Quality Checklist

Run before delivering M9.

## Gate 1 — Coverage

- [ ] All 8 ISO 25010 categories addressed (Mode A) OR equivalent in Mode B/C — no category silently skipped
- [ ] Performance Efficiency: ≥3 NFRs (latency, throughput, resource usage)
- [ ] Security: ≥5 NFRs (auth, encryption at rest, in transit, audit, incident response minimum)
- [ ] Usability: ≥2 NFRs (one accessibility-related)
- [ ] Reliability: ≥3 NFRs (uptime, RTO, RPO at minimum)
- [ ] Maintainability: ≥2 NFRs
- [ ] Compliance: every applicable regulation has at least 1 NFR per major requirement
- [ ] Section 9.9 (NFR-to-FR cross-reference) populated
- [ ] Section 9.10 (Constraint-to-NFR cross-reference) populated
- [ ] Section 9.11 Open Issues has ≥3 items (most NFRs have unmeasured current state)

## Gate 2 — Per-NFR rigor (CRITICAL)

For each NFR, verify ALL fields populated:

- [ ] Statement uses imperative form ("The system shall...")
- [ ] Metric is named (latency, error rate, percentage, count, etc.)
- [ ] Target is a specific value, not a range without bound
- [ ] Condition specifies under what circumstances target applies (load, data volume, time of day)
- [ ] Current state is either measured (with source) or "Unknown — not measured"
- [ ] Source cites SLA, regulation, stakeholder commitment, benchmark, or similar
- [ ] Verification method is specific (load test, audit, monitoring, drill — not "test it")
- [ ] Priority assigned (Must/Should/Could)
- [ ] Functional impact lists at least one FR (else why does this NFR exist?)

## Gate 3 — Measurability

The hardest gate. For each NFR, ask: "Could two engineers verify this and reach the same answer?"

- [ ] No NFR contains "fast", "easy", "intuitive", "robust", "scalable", "user-friendly" without concrete measure attached
- [ ] No NFR uses "should be" language without metric
- [ ] Latency NFRs specify percentile (p50, p95, p99) — not just "average" without context
- [ ] Uptime NFRs specify measurement method (external monitor, error budget, etc.) and measurement window (monthly, quarterly)
- [ ] Test coverage NFRs specify scope (which files/areas) — not "the codebase"

## Gate 4 — Honesty

- [ ] Current state is honest: most reverse-engineered systems FAIL several NFR targets — this is documented, not hidden
- [ ] If current state is unknown, it says so explicitly + adds to 9.11 Open Issues
- [ ] If a target is aspirational, says so; doesn't pretend it's currently met
- [ ] Confidence note in 9.0 Overview reflects how much was measured vs assumed

## Gate 5 — Compliance rigor

If the project is regulated:

- [ ] Every applicable regulation has at least one citation (clause-level, not just regulation-name)
- [ ] Regulation-mandated targets are not loosened (e.g., GDPR 30-day cannot become 60-day)
- [ ] Verification method for compliance NFRs satisfies the regulator (audit-grade, not just "we ran a test")
- [ ] Compliance gaps (current state vs. target) explicitly flagged in 9.11

## Gate 6 — Cross-references

- [ ] Section 9.9 lists every M3-Mx FR that has at least one NFR constraint (or notes if a FR genuinely has no NFR — rare)
- [ ] Section 9.10 maps each M2.5 constraint to its M9 NFR — many constraints become NFRs verbatim
- [ ] FRs that have many NFR impacts (e.g., login flow has perf, sec, usability, compliance NFRs) are cross-referenced from each

## Gate 7 — Mode discipline

- [ ] If Mode A: 8 ISO 25010 categories used as-is
- [ ] If Mode B: company taxonomy cited at 9.0 Overview; categories follow company structure
- [ ] If Mode C: user-defined categories cited; user confirmed structure before authoring

## Gate 8 — Format

- [ ] Output filename: `M9_Non_Functional_Requirements.md`
- [ ] Output location: `docs/00_REQUIREMENTS/SRS_VI/M9_*`
- [ ] NFR IDs follow `NFR-<CATEGORY>-NN` format
- [ ] Section numbering 9.0 → 9.12 (or as adjusted for chosen mode)
- [ ] Tables present for cross-references (9.9, 9.10, 9.12)

## Self-review prompt

For each NFR, ask:

> "If we ship the product today and a customer asks 'does it meet NFR-XXX-NN?', could I prove yes/no with a single test or report?"

If not, the NFR is too vague. Sharpen.

Then ask:

> "Does Section 9.11 reflect genuine gaps? Or am I over-claiming current state?"

Add unmeasured NFRs to Open Issues. Honesty here saves audit pain later.
