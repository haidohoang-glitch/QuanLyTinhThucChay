# Requirements Traceability — Adaptation

Variations by project context.

> **Applies to Mode A (4-tier RTM) only.** Mode B/C follow their own structures.

## Regulated industries

### FDA-regulated software (medical devices, clinical decision support)

**Required additions:**
- Verification & Validation (V&V) columns: Verification (does it match design?), Validation (does it satisfy intended use?)
- Risk class column (Class I/II/III) per device classification
- Traceability to Risk Management File (per ISO 14971)
- Sign-off columns per regulator-required role (Quality Lead, Regulatory Affairs)

**Use Mode B** if your company has an FDA-aligned RTM template — never pure Mode A for Class II+ devices.

**Watch for:** RTMs are heavily audited; Class III devices may require external SQA review.

### HIPAA-regulated (healthcare data)

**Required additions:**
- "PHI handling" column for Reqs that touch PHI
- "BAA scope" column noting which subprocessors are involved
- Cross-reference to access controls (HIPAA Security Rule §164.312)

**Verification artifacts:**
- Access logs sampled (not just "logging enabled")
- Encryption verified in actual configuration, not just policy
- Subprocessor agreements current and signed

### PCI-DSS (cardholder data)

**Required additions:**
- "PCI scope" column: in-scope (CDE) vs out-of-scope (SAQ-A reduced)
- Reference to specific PCI requirement number (e.g., PCI 3.4 for encryption)
- Verification artifact for each PCI requirement (often QSA assessment)

### SOX (public companies, financial reporting)

**Required additions:**
- "ICFR control" column: which Internal Control over Financial Reporting this Req supports
- Segregation of duties trace (who can do what)
- Change control evidence

### GDPR (EU user data)

**Required additions:**
- Data classification per Req (PII / pseudonymized / anonymous)
- Lawful basis per Req (consent / contract / legitimate interest / etc.)
- Data subject rights coverage (export, delete, rectify)

---

## Greenfield SRS RTM (pre-launch)

When the SRS is for a product not yet built:

**Mode A still applies, but:**
- "Code" column = "Not implemented (planned: Phase X, WP-X.Y)"
- "Test" column = "Test plan TC-XXX-NN drafted; will execute in Phase X"
- "Status" = "NOT IMPLEMENTED"
- Coverage stats reflect roadmap completeness, not current implementation

**As implementation progresses:**
- Update rows as PRs merge (per-PR maintenance)
- Refresh coverage stats weekly
- v1.0 RTM (post-launch) replaces v0.x with full implementation evidence

## Reverse-engineered RTM (existing product)

When SRS was reverse-engineered AND RTM is being built for the existing system:

**Mode A applies, but:**
- Some FRs/NFRs may have unclear test coverage; spend most RTM effort here
- Many tests may be orphans (no clear Req); investigate and add Reqs OR document tests as acceptable infra
- "Last verified" dates legitimately old for stable code; but auditors expect ≤90 days for compliance-sensitive Reqs

**Watch for:** Reverse-engineered RTMs often surface that "we thought we had test coverage but actually..." gaps. This is the value — don't hide it.

## Monorepo / multi-component RTM

When the project has multiple sub-systems:

- Decide: ONE master RTM, or per-component RTMs?
- Master RTM: Reqs span components; complex but unified
- Per-component RTMs: cleaner but cross-component Reqs (e.g., "user can place order" spans frontend + cart + payment) need cross-RTM links

**Recommendation:** master RTM at platform level + per-component "implementation detail" RTMs that don't repeat Req text but link to master. Use Mode C with a "Component" column.

## Microservices RTM

When system is N services:

- Each service may have its own SRS subset; each Req traces to one or more services
- "Code" column may list multiple service:path entries
- Add column "Service(s)" to make ownership explicit
- Cross-service Reqs (e.g., end-to-end transactions) often have orphan-like patterns that aren't actually orphans — they trace to orchestration layer; document explicitly

## Agile teams (RTM as live dashboard)

When team uses agile/iterative delivery:

- RTM is a **live dashboard**, not a doc artifact
- Generate from Jira/Linear/etc. + code annotations
- Auto-update on PR merge
- Quarterly snapshot becomes the audit-friendly version

**Tools:**
- Jira: Use "Issue Links" to connect Reqs (issues) to Code (commits) and Tests (test cases)
- Linear: Similar — issues + relations
- Custom: code annotations like `// @implements FR-AUTH-01` scanned by CI and exported

If using auto-generation: document tooling in 10.3.E and cite tool versions.

## API-only products RTM

When product is an API:

- Reqs typically organized per endpoint
- "Code" trace usually goes to endpoint handler + service layer
- "Test" includes contract tests (OpenAPI conformance) in addition to unit/integration
- API versioning Reqs are NFRs but often have unique RTM rows tracking version compatibility tests

## ML/AI product RTM

When system includes ML models:

- Reqs include model accuracy, fairness, drift detection
- "Test" for ML Reqs = evaluation report (not unit test)
- "Code" includes training pipeline, inference service, monitoring
- Add column "Model version" for Reqs tied to specific trained model

**Watch for:** Performance NFRs for ML are model-specific; refreshed every model retraining.

## Multi-tenant SaaS RTM

When system supports many tenants:

- Tenant isolation Reqs are critical RTM rows
- "Test" for isolation includes synthetic multi-tenant test scenarios
- Per-tenant compliance variations (some tenants HIPAA-bound, some not) may require sub-RTMs

## When RTM lives outside Markdown

For some compliance contexts, the official RTM lives in:
- A spreadsheet (Excel, Google Sheets) reviewed by auditors
- A GRC tool (Vanta, Drata, Secureframe)
- An ALM tool (Polarion, IBM DOORS)

In those cases, this skill produces the **markdown summary RTM** that complements the system-of-record. Cite the system-of-record in 10.1 introduction and document the sync method.

---

## RTM update frequency by project type

| Project type | Update frequency | Refresh trigger |
|--------------|------------------|-----------------|
| FDA-regulated | Per change; full re-validation per release | Document control sign-off |
| SOC2-prepping | Weekly (RTM-aligned testing); quarterly full audit | CI green + manual review |
| Greenfield post-MVP | Per PR (RTM updated by PR author) | PR template question |
| Reverse-engineered (audit) | Once for audit; refresh per major change | Compliance calendar |
| Mature, stable product | Quarterly | Compliance calendar |
| Agile fast-moving | Continuous (auto-generated) | CI |

Document the chosen frequency in 10.1.5.
