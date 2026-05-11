# M10 — RTM, Open Issues, Appendix

> **SRS Module 10 of 10** | Project: {{PROJECT_NAME}} | RTM Version: v0.1 | Last validated: {{YYYY-MM-DD}}

---

## 10.1 Requirements Traceability Matrix (RTM)

**Mode used:** {{A — Standard 4-tier (Req → Design → Code → Test) / B — Honor company template / C — User-defined}}
**Mode rationale:** {{WHY}}
**RTM scope:** All FRs (M3-M{{X}}) + all NFRs (M9). Total rows: {{N}}.
**Source SRS commit:** `{{HASH}}` (date: {{YYYY-MM-DD}})
**Source codebase commit:** `{{HASH}}` (date: {{YYYY-MM-DD}})
**Last test run:** {{YYYY-MM-DD}} (CI run {{ID}}, branch `{{BRANCH}}`)

### How to read this RTM

- **Req ID:** Reference to FR or NFR in SRS
- **Design:** Where the design decision is documented (ADR, architecture doc section)
- **Code:** Implementing file(s) and key functions
- **Test:** Manual test case IDs + automated test names
- **Status:** PASS / FAIL / SKIP / NOT RUN / NOT IMPLEMENTED
- **Last verified:** Date the trace was last confirmed accurate (not just last test run)
- **Notes:** Anything notable

### 10.1.0 Functional Requirements

| Req ID | Title (short) | Design | Code | Test | Status | Last verified | Notes |
|--------|---------------|--------|------|------|--------|---------------|-------|
| FR-AUTH-01 | User Login | ADR-007 + M2.1 | `src/server/services/auth/login.ts` | TC-AUTH-01..06; `auth.spec.ts → 'login'` | PASS | {{YYYY-MM-DD}} | |
| FR-AUTH-02 | Logout | ADR-007 | `src/server/services/auth/logout.ts` | TC-AUTH-07; `auth.spec.ts → 'logout'` | PASS | {{YYYY-MM-DD}} | |
| FR-AUTH-03 | Password Reset | ADR-007 | `src/server/services/auth/reset.ts` | TC-AUTH-08..12 | FAIL | {{YYYY-MM-DD}} | TC-AUTH-09 fails — see ISS-XX |
| FR-CUST-01 | Create Customer | M2.1 | `src/server/services/customers/create.ts` | `customers.spec.ts → 'create'` | PASS | {{YYYY-MM-DD}} | |
| ... | ... | ... | ... | ... | ... | ... | ... |
| **Total FRs:** {{N}} | | | | | | | |

### 10.1.1 Non-Functional Requirements

NFRs traced to verification artifacts (often differ from FR test types — load tests, audits, monitoring queries).

| NFR ID | Title (short) | Verification method | Verification artifact | Status (target met?) | Last verified |
|--------|---------------|----------------------|------------------------|----------------------|---------------|
| NFR-PERF-01 | API GET p95 ≤ 500ms | k6 load test | `tests/perf/api_get.js` | PASS (p95 = 320ms at 50 req/s) | {{YYYY-MM-DD}} |
| NFR-SEC-02 | Encryption at rest | KMS configuration audit | `audit/2026-Q2-encryption-review.pdf` | PASS | {{YYYY-MM-DD}} |
| NFR-REL-01 | Uptime ≥ 99.9% | External monitor (Pingdom) | Monthly Pingdom report | PASS (99.94% YTD) | {{YYYY-MM-DD}} |
| NFR-REL-02 | RTO ≤ 4h | DR drill | `runbooks/dr-drill-2026-Q2.md` | NOT VERIFIED — drill scheduled Q3 | {{YYYY-MM-DD}} |
| NFR-COMP-01 | SOC2 Type I | External audit | (pending) | NOT VERIFIED — audit Year 1 | {{YYYY-MM-DD}} |
| ... | ... | ... | ... | ... | ... |

### 10.1.2 Coverage Statistics

| Metric | Count | % of total |
|--------|-------|------------|
| **Functional Requirements** | | |
| Total FRs | {{N}} | 100% |
| FRs with design linked | {{N}} | {{%}} |
| FRs with code linked | {{N}} | {{%}} |
| FRs with test linked | {{N}} | {{%}} |
| FRs with passing test | {{N}} | {{%}} |
| FRs with failing test | {{N}} | {{%}} |
| FRs not implemented (greenfield gap) | {{N}} | {{%}} |
| **Non-Functional Requirements** | | |
| Total NFRs | {{N}} | 100% |
| NFRs with verification artifact | {{N}} | {{%}} |
| NFRs currently meeting target | {{N}} | {{%}} |
| NFRs not yet verified | {{N}} | {{%}} |
| **Orphans** | | |
| Orphan code paths (no Req linked) | {{N}} | (info only) |
| Orphan tests (no Req linked) | {{N}} | (info only) |

### 10.1.3 Findings

#### Orphan requirements (no test or no code)

| Req ID | Issue | Severity | Recommended action |
|--------|-------|----------|---------------------|
| FR-{{ID}} | No automated test; only manual TC exists | Medium | Add unit/integration test by {{DATE}} |
| FR-{{ID}} | No code link found | High | Investigate: not implemented? Or code path not located? |
| NFR-{{ID}} | No verification artifact | High | Plan verification (load test / audit / monitor) by {{DATE}} |

#### Orphan code (code paths with no Req)

| Code path | Likely category | Action |
|-----------|-----------------|--------|
| `src/utils/dateFormat.ts` | Utility — no Req expected | None (acceptable) |
| `src/server/legacy/oldCheckoutFlow.ts` | Possibly stale; no Req | Investigate: dead code? Or missing Req? |

#### Orphan tests (tests with no Req)

| Test path | Description | Action |
|-----------|-------------|--------|
| `tests/integration/db.fixture.test.ts` | DB fixture validation | Acceptable (infrastructure test; no end-user Req) |
| `tests/unit/legacy.test.ts` | Tests `legacy/oldCheckoutFlow.ts` | If code is stale, test is too — remove |

#### Failing tests (current state)

| Req ID | Test | Failure | Owner | Target fix date |
|--------|------|---------|-------|------------------|
| FR-AUTH-03 | TC-AUTH-09 (password reset email arrival) | Email not arriving in test inbox | Backend lead | {{YYYY-MM-DD}} |

### 10.1.4 Verification log

This RTM was last validated on {{YYYY-MM-DD}} by {{REVIEWER_NAME}}.

Validation method:
- [ ] Random sample of 10 FRs verified — Code links open to correct files
- [ ] Random sample of 10 NFRs verified — Verification artifacts exist and are recent
- [ ] Test status verified by re-running CI (run ID: {{ID}})
- [ ] Coverage statistics computed from current data (not stale)

### 10.1.5 Maintenance approach

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Update RTM row when PR merges | Per PR | PR author (gated by template) |
| Quarterly accuracy audit | Quarterly | QA Lead |
| Coverage statistics refresh | Weekly (CI auto) | CI |
| External RTM audit | Annually (SOC2-aligned) | External auditor |

---

## 10.2 Open Issues

Items requiring stakeholder decision or follow-up.

| ID | Issue | Originated in | Status | Owner | Target resolution |
|----|-------|---------------|--------|-------|-------------------|
| ISS-{{NN}} | {{e.g., FR-AUTH-03 has failing test (TC-AUTH-09); root cause investigation in progress}} | M10.1.3 | OPEN | Backend lead | {{YYYY-MM-DD}} |
| ISS-{{NN}} | {{e.g., NFR-REL-02 RTO never tested via DR drill}} | M10.1 + M9.4 | OPEN | DevOps | {{YYYY-MM-DD}} |
| ISS-{{NN}} | (issues from earlier SRS authoring — preserved here) | {{ORIGIN}} | {{STATUS}} | {{OWNER}} | {{DATE}} |

(Preserve any Open Issues from `srs-greenfield-author` or `srs-reverse-engineer` outputs; add new ones from RTM findings.)

### Issue lifecycle (same as SRS author)

- OPEN / IN PROGRESS / BLOCKED / RESOLVED / DEFERRED

---

## 10.3 Appendix

### A. Data Dictionary
(Preserve from SRS author skill — consolidated entity definitions)

### B. User Class Privilege Matrix
(Preserve from SRS author skill)

### C. State Diagrams
(Preserve from SRS author skill)

### D. Glossary (extended)
(Preserve from SRS author skill)

### E. RTM Generation Tools

If RTM was generated/aided by tools:

- {{TOOL_NAME}} version {{V}}: used to {{e.g., extract test → file mapping from coverage report}}
- {{TOOL_NAME}}: used to {{e.g., scan code annotations for FR-XXX-NN markers}}

If RTM is partly auto-generated:
- Auto-generated columns: {{LIST}}
- Manual columns: {{LIST}}
- Conflict resolution: when auto and manual disagree, manual wins; investigate why

### F. RTM Export Formats

For external systems:
- CSV export: `docs/00_REQUIREMENTS/SRS_VI/rtm_export.csv` (auto-generated)
- JSON export: `docs/00_REQUIREMENTS/SRS_VI/rtm_export.json`
- Audit-friendly PDF: produced quarterly for compliance archive

### G. Document Revision History

(Preserve from earlier modules; add RTM updates)

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{YYYY-MM-DD}} | {{NAME}} | Initial RTM populated from SRS v0.1 |

---

## 10.4 Sign-off

| Role | Name | Approval | Date |
|------|------|----------|------|
| Engineering Lead | | | |
| QA Lead | | | |
| Compliance / Audit (if applicable) | | | |

RTM is **approved** when:
- All FRs in M3-Mx have at least Design + Code + Test links (or explicit "not implemented" with planned date)
- All NFRs in M9 have a verification method documented
- Coverage statistics meet quality bar for SRS version (v1.0 typically requires ≥80% FRs with passing test)
- All RTM findings (10.1.3) have owners and target dates
