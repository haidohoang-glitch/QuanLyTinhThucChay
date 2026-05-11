# Business Context Capture — Quality Checklist

Run before delivering `BUSINESS_CONTEXT.md`.

## Gate 1 — Coverage

- [ ] Section 1 product description is in business language, not technical (no "REST API", "endpoint", "middleware")
- [ ] Section 3 lists all primary actors AND non-human actors (webhooks, cron, system jobs)
- [ ] Section 4 has 15+ use cases (small product) or grouped use cases for larger products
- [ ] Section 5 entities are named in product terminology, not DB column names
- [ ] Section 6 has rules in all three subsections (Validation, Calculation, Eligibility)
- [ ] Section 7 documents at least 3 multi-step workflows
- [ ] Section 8 has ≥5 invariants
- [ ] Section 9 Tensions has ≥2 items (every codebase has terminology drift)
- [ ] Section 10 Open Questions has ≥3 items
- [ ] Section 11 documents the chosen decomposition mode

## Gate 2 — Honesty

- [ ] Items I inferred (vs. directly observed) are explicitly labeled as "Inferred"
- [ ] Counts in Section 11 (rules vs invariants observed vs inferred) are honest
- [ ] If a workflow has unclear branches, those gaps are in Section 9 or 10, not glossed over
- [ ] Confidence rating reflects reality

## Gate 3 — Domain language discipline

- [ ] No code identifiers in the business view (no `userController`, `expenseSchema`, etc.)
- [ ] Use the product's vocabulary (if the product calls them "Members", do not call them "Users")
- [ ] If the codebase uses inconsistent terminology, document the inconsistency in Section 5 → Terminology notes
- [ ] Every business rule (Section 6) has an evidence pointer (file:line); the rule itself is in business language

## Gate 4 — Scope discipline

- [ ] No code structure description (those go to `codebase-discovery`)
- [ ] No data architecture description (those go to `data-architecture-audit`)
- [ ] No fix proposals or product change recommendations (descriptive only)
- [ ] No implementation plans
- [ ] If you found a tension, the recommendation is "interview X" / "clarify with PM", NOT "do Y"

## Gate 5 — Invariant rigor

- [ ] Each invariant has a "Why it matters" — the business cost if broken
- [ ] Each invariant has "Where enforced" — and if not enforced, that's flagged as risk
- [ ] Invariants are not just "nice to have" — each is something the product would consider broken without

## Gate 6 — Format

- [ ] Output filename: `BUSINESS_CONTEXT.md`
- [ ] Output location: `docs/01_DISCOVERY/BUSINESS_CONTEXT.md`
- [ ] Use Case IDs `UC-01`, `UC-02`, ...
- [ ] Business Rule IDs `BR-V-01` (validation), `BR-C-01` (calculation), `BR-A-01` (authorization)
- [ ] Invariant IDs `INV-01`, `INV-02`, ...
- [ ] Tension IDs `T-01`, `T-02`, ...
- [ ] Section headings match template

## Self-review prompt

Re-read your output as the product manager who'll inherit this product. For each section, ask: "Is this written in language I'd use in a roadmap meeting?" If not, rewrite. Code-flavored language is a sign you slipped back into `codebase-discovery` mode.
