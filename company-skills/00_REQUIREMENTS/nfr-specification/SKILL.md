---
name: nfr-specification
description: Author the Non-Functional Requirements (NFR) section of an SRS — covering performance, security, usability, reliability, maintainability, portability, compliance, and scalability. Each NFR has measurable target, current state, source, and verification method. Produces M9 of the company SRS standard. Use when populating M9 of a new or reverse-engineered SRS, when establishing measurable quality targets, when preparing for compliance/SLA review, or when generating Phase 0 Requirements NFR output. Triggers include "write NFRs", "specify quality requirements", "performance targets", "security requirements", "compliance NFRs", "populate M9", or "Phase 0 Requirements NFR".
---

# NFR Specification

Author measurable Non-Functional Requirements: how well the system performs, not what it does. Output is M9 of the company SRS standard (or standalone if SRS not yet structured).

## When this skill applies

Use when:
- Authoring or completing an SRS (M9 placeholder needs population)
- Establishing quality targets for a new product (e.g., "what performance must we meet?")
- Preparing for compliance review (regulatory NFRs must be enumerated)
- Negotiating SLAs (NFRs become contractual targets)
- Setting baselines for performance/reliability monitoring

Do NOT use for:
- Functional requirements (those go to M3-Mx via `srs-greenfield-author` or `srs-reverse-engineer`)
- Design decisions (NFRs constrain design; they are not designs)
- Implementation tasks (NFRs become acceptance criteria for tasks elsewhere)

## What is an NFR (vs FR)

| Functional Requirement (FR) | Non-Functional Requirement (NFR) |
|----------------------------|----------------------------------|
| What system DOES | How WELL it does it |
| "User can transfer funds" | "Funds transfer completes in ≤2s p95 under 1K req/s load" |
| Tested by acceptance test | Tested by load test, security audit, etc. |
| Counted in feature scope | Constrains design space across features |
| In modules M3-Mx | In module M9 |

NFRs are measurable. "System should be fast" is NOT an NFR — it's a wish. "API p95 latency ≤ 200ms at 100 req/s" IS an NFR.

## Inputs (must read first)

Read in order:

1. **`docs/00_REQUIREMENTS/SRS_VI/M1_*` and `M2_*`** — context, scope, user classes, constraints
2. **`docs/00_REQUIREMENTS/SRS_VI/M2_Overall_Description.md` Section 2.5 (Constraints)** — many constraints translate directly to NFRs
3. **All M3-Mx modules** — to understand what functions need quality envelopes
4. **`docs/01_DISCOVERY/DATA_ARCHITECTURE.md` Section 6 (Governance)** — security, privacy, retention NFRs (especially for reverse-engineered SRS)
5. **`docs/01_DISCOVERY/TECH_DEBT_AUDIT.md` if exists** — Performance/Reliability/Security findings inform current-state NFRs
6. **External:** SLAs, contracts, regulations applicable, competitor benchmarks (if available)

## Output

A single file: `docs/00_REQUIREMENTS/SRS_VI/M9_Non_Functional_Requirements.md`, filled from [assets/M9_template.md](assets/M9_template.md).

## Workflow

### Step 1 — Identify NFR sources

Where do NFRs come from? List what applies to your project:

- **Stakeholder commitments / contracts** (uptime SLA, response time promises)
- **Regulations** (HIPAA, PCI-DSS, GDPR, SOX, FDA, sector-specific)
- **Competitive benchmarks** ("our app must launch in <2s like X")
- **User class characteristics** (M2.3 — power users tolerate longer load than casual)
- **Technology constraints** (M2.5 — locked-in stack has performance ceilings)
- **Operational requirements** (RTO, RPO from M2.5 or DR plan)
- **Industry baselines** (e.g., web vitals, OWASP Top 10 for security)
- **Current performance** (for reverse-engineered SRS — captures status quo)

For each source, note what NFR category it informs.

### Step 2 — Choose categorization mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — ISO/IEC 25010 standard categories** *(default)* | No special instruction | The 8 categories below |
| **B — Honor company's NFR taxonomy** | Company has formal QA framework with its own categorization | Company taxonomy |
| **C — User-defined categories** | User specifies (e.g., "by SLA tier", "by trust criteria") | User input |

Selection logic:
1. User explicit → use it
2. Company has QA standard (e.g., "we organize NFRs per SOC2 Trust Services Criteria") → ask user
3. Default → Mode A

#### Mode A — ISO/IEC 25010 categories

| Category | What it covers | Example NFR |
|----------|----------------|-------------|
| **Performance Efficiency** | Response time, throughput, resource use | API p95 latency ≤ 200ms at 100 req/s |
| **Security** | Auth, encryption, audit, threat protection | All API responses signed; PII encrypted at rest with KMS |
| **Usability** | Learnability, accessibility, UX quality | New user can complete signup in ≤3 minutes; WCAG 2.1 Level AA |
| **Reliability** | Availability, fault tolerance, recoverability | 99.9% uptime measured monthly; RTO ≤ 4h, RPO ≤ 1h |
| **Maintainability** | Modularity, testability, modifiability | Test coverage ≥ 80% for critical paths; CI build < 10 min |
| **Portability** | Adaptability to different environments | Runs on AWS + Azure; supports Postgres 14+ and MySQL 8+ |
| **Compatibility** | Co-existence with other systems | API v3 backward-compatible with v2 for 12 months post-release |
| **Compliance** | Adherence to laws, standards, contracts | SOC2 Type II compliant; GDPR right-to-export within 30 days |

Some teams add **Scalability** as 9th category (often subsumed into Performance Efficiency).

#### Mode B — Company's NFR taxonomy

Common company structures:
- SOC2-aligned: Security / Availability / Confidentiality / Processing Integrity / Privacy
- Web Vitals-aligned: LCP / FID / CLS / TTFB / TBT (perf-heavy)
- Custom: e.g., "P0 NFRs" (must), "P1 NFRs" (should), "P2 NFRs" (could)

Cite company source in M9.0 introduction.

#### Mode C — User-defined

Common user-supplied:
- "By tier": Free tier NFRs vs Pro tier NFRs (different SLAs per plan)
- "By environment": dev / staging / prod (different targets)
- "By trust principle": SOC2's 5 TSPs

Confirm structure with user.

### Step 3 — For each category, enumerate NFRs

Use [assets/M9_template.md](assets/M9_template.md). Each NFR has:

- **ID:** `NFR-<CATEGORY_PREFIX>-NN` (e.g., NFR-PERF-01, NFR-SEC-04)
- **Title:** ≤8 words
- **Statement:** "The system shall {{measurable property}} under {{condition}}"
- **Metric:** what is measured (e.g., latency, error rate, MTTR)
- **Target:** specific value (e.g., "p95 ≤ 200ms")
- **Condition:** under what load / state (e.g., "at 100 req/s", "during normal operation")
- **Current state:** measured value if known; "Unknown — not measured" otherwise
- **Source:** what motivates this NFR (SLA contract, regulation, stakeholder, benchmark)
- **Verification method:** how to verify (load test, audit, monitoring, drill, code review)
- **Priority:** Must / Should / Could (for prioritization within category)
- **Functional impact:** which M3-Mx FRs this NFR affects (cross-reference)

Example of a good NFR:

> **NFR-PERF-03** — API List Endpoint Latency
> **Statement:** The system shall respond to `GET /api/v1/transactions?limit=50` within 200ms p95.
> **Metric:** Response time (server-side, excluding network)
> **Target:** p95 ≤ 200ms; p99 ≤ 500ms
> **Condition:** Under nominal load (≤100 req/s); cache warm; ≤10K transactions in user's account
> **Current state:** p95 ≈ 240ms (Datadog APM, 7-day average) — currently fails target
> **Source:** Customer SLA tier "Pro" promises sub-300ms p95 for list endpoints (Contract §4.2)
> **Verification method:** k6 load test in staging at 100 req/s; production monitoring with alert at 250ms p95 sustained 5 min
> **Priority:** Must (contractual obligation)
> **Functional impact:** FR-TRX-04 (View Transaction History), FR-TRX-07 (Search Transactions)

Bad NFR (do not write):

> **NFR-PERF-XX** — System should be fast.

### Step 4 — Pay special attention to Security NFRs

Security NFRs are often most contractually significant. Cover at minimum:

- **Authentication:** what identifies users? MFA required for what classes?
- **Authorization:** how is access enforced? Defense in depth?
- **Encryption at rest:** what data, what algorithm, key management?
- **Encryption in transit:** TLS version minimum?
- **Audit trail:** what events logged, what retention, tamper resistance?
- **Vulnerability management:** patch SLA, dep scanning frequency
- **Incident response:** detection target time, response target time
- **Compliance:** specific regulation (SOC2, ISO 27001, PCI-DSS) and which controls

For each, derive a measurable NFR — not "system shall be secure" but "All data classified PII (per data classification policy) encrypted at rest using AES-256-GCM with KMS-managed keys".

### Step 5 — Pay special attention to Compliance NFRs

If the system is regulated, Compliance NFRs are often the most enforceable. For each applicable regulation:

- Cite specific regulation clause (e.g., "GDPR Article 17")
- Translate clause into measurable NFR
- Specify verification method that satisfies regulator (audit, assessment, certification)
- Map to M3-Mx FRs that implement it

### Step 6 — Document current state honestly

For each NFR, "Current state" field:

- If measured: cite source (Datadog, New Relic, prod logs, audit report)
- If not measured: write "Unknown — not measured" and add to Open Issues
- If aspirational (target not yet met): say so explicitly; do NOT pretend

This separates **target NFRs** from **current performance**. Plans (later phase) close the gap.

### Step 7 — Group by category in M9 structure

Final M9 has subsections per category:

- 9.1 Performance Efficiency
- 9.2 Security
- 9.3 Usability
- 9.4 Reliability
- 9.5 Maintainability
- 9.6 Portability
- 9.7 Compatibility
- 9.8 Compliance

(Adjust per chosen mode.)

Each subsection has 3-15 NFRs typically. <3 likely under-specifies; >15 may indicate over-decomposition (consolidate similar).

### Step 8 — Cross-link to FRs and constraints

Final pass:

- For each FR in M3-Mx, identify which NFRs constrain it (use the "Functional impact" field of NFRs)
- For each constraint in M2.5, identify which NFR it became (most M2.5 constraints become NFRs verbatim)
- Add traceability table at end of M9

### Step 9 — Self-review

Run [references/checklist.md](references/checklist.md). NFR rigor is the most common failure mode of SRS — review carefully.

## Quality bar

A good M9 lets:
- An auditor verify each compliance NFR has a corresponding control + evidence
- A QA engineer write load tests / security tests directly from NFR statements
- An SRE define monitors and alerts (current state vs. target gap drives alerts)
- A product manager understand which NFRs may be violated and the business impact
- A vendor read the SRS and bid on meeting NFRs

If reading M9 leaves anyone wondering "how would I verify this is met?", the NFR is too vague.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations: regulated industries (HIPAA, PCI), high-availability systems, latency-critical systems, accessibility-critical products, multi-tenant SaaS, and consumer mobile.

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: "Project Atrium" (continued from `srs-greenfield-author`) — invoicing SaaS NFRs across all 8 categories.

## Failure modes to avoid

- **Vague metrics.** "Fast" — by what measure? "Reliable" — uptime %? Error rate? MTBF? Always pick a metric.
- **Targets without conditions.** "p95 latency ≤ 200ms" — at what load? With what cache state? Conditions are mandatory.
- **Pretending current matches target.** Be honest: most reverse-engineered systems do not currently meet their NFR targets. Document the gap.
- **One-size-fits-all targets.** Different endpoints have different latency expectations. Different user classes tolerate different perf. Specify.
- **Skipping Compliance section because "not regulated".** Even non-regulated products often have implicit compliance (privacy, accessibility) — at minimum say "no formal compliance requirements; follows industry best practice X".
- **NFRs that aren't NFRs.** "System shall use Postgres" — not an NFR, that's a constraint or design choice. NFR is "Storage layer shall support the latency NFR-PERF-* targets".
- **No verification method.** If you can't say HOW to verify the NFR, the NFR is meaningless. Strike it or sharpen it.
- **Unmeasurable usability NFRs.** "Easy to use" → unmeasurable. "New user completes signup task in ≤3 min in usability test (5/5 succeed)" → measurable.
