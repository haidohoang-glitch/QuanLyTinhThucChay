---
name: requirements-traceability
description: Build and maintain a Requirements Traceability Matrix (RTM) that links each requirement (FR + NFR) to design artifacts, code, and tests. Identifies orphan requirements (no test), orphan code (no requirement), and coverage gaps. Produces M10 of the company SRS standard. Use when populating M10 of an SRS, preparing for compliance audit (SOC2/ISO/FDA require RTM), tracking implementation completeness, or generating Phase 0 Requirements traceability output. Triggers include "build RTM", "requirements traceability matrix", "trace requirements to tests", "populate M10", "audit traceability", or "Phase 0 Requirements RTM".
---

# Requirements Traceability

Build the Requirements Traceability Matrix (RTM) — the audit-grade table linking each FR/NFR to its implementation and tests. RTM exposes orphans (requirements without tests, code without requirements), measures coverage, and provides the evidence trail auditors demand.

## When this skill applies

Use when:
- Populating M10 RTM section of an SRS
- Preparing for compliance audit (SOC2 Type II, ISO 27001, FDA, GDPR — all require RTM-style evidence)
- Tracking implementation completeness mid-development ("how many FRs are actually built?")
- Identifying test gaps before release
- Generating Phase 0 Requirements traceability output for company doc standard

Do NOT use for:
- Authoring requirements (use `srs-greenfield-author` or `srs-reverse-engineer`)
- Authoring NFRs (use `nfr-specification`)
- Test case design (RTM tracks test coverage; test design is QA work upstream)
- Implementation planning (use `implementation-planning`)

## Inputs (must read first)

The RTM is downstream of everything. Read in order:

1. **`docs/00_REQUIREMENTS/SRS_VI/M1-M2`** — context, scope
2. **`docs/00_REQUIREMENTS/SRS_VI/M3-Mx` — Functional Requirements** (every FR-XXX-NN gets an RTM row)
3. **`docs/00_REQUIREMENTS/SRS_VI/M9` — NFRs** (every NFR-XXX-NN gets an RTM row)
4. **`docs/01_DISCOVERY/CODEBASE_MAP.md`** — to find code paths corresponding to FRs
5. **Codebase itself** — actual file paths for "Code" column
6. **Test suite + test results** — actual test names + last run status

If an SRS doesn't exist yet, the RTM is empty — author the SRS first via the appropriate skill.

## Output

A single file: `docs/00_REQUIREMENTS/SRS_VI/M10_RTM_Issues_Appendix.md` (or update existing M10 placeholder), filled from [assets/M10_template.md](assets/M10_template.md).

Note: M10 has 3 sections — RTM (10.1, this skill's primary output), Open Issues (10.2, often pre-populated by SRS author skill), and Appendix (10.3). This skill primarily populates 10.1 and may add to 10.2.

## Workflow

### Step 1 — Inventory all requirements

From SRS, list:
- Every FR-XXX-NN from M3-Mx
- Every NFR-XXX-NN from M9

Aggregate into a master list. This becomes RTM rows. Typical: 30-150 rows total.

### Step 2 — Choose RTM trace dimensions mode

Three modes:

| Mode | When to use | Source |
|------|-------------|--------|
| **A — Standard 4-tier RTM** *(default)* | No special instruction | Req → Design → Code → Test |
| **B — Honor company's RTM format** | Company has formal RTM template (often required for regulated industries) | Company template |
| **C — User-defined dimensions** | Project needs additional columns (Risk, Owner, Operations, etc.) | User input |

Selection logic:
1. User explicit → use it
2. Company has formal RTM template → ask user (Mode A or B?)
3. Default → Mode A

#### Mode A — Standard 4-tier RTM

Each requirement traces forward through 4 columns:

| Req | Design | Code | Test |
|-----|--------|------|------|
| FR-AUTH-01 | M2.1 perspective + ADR-007 | `src/server/services/auth/login.ts` | TC-AUTH-01 (manual), `auth.spec.ts → 'login with valid credentials'` (auto) |

**Plus status columns:**

| Req | Design | Code | Test | Test status | Coverage |
|-----|--------|------|------|-------------|----------|
| FR-AUTH-01 | ... | ... | ... | PASS (last run 2026-05-01) | 87% |

#### Mode B — Honor company RTM format

Common variations:
- **5-column with Verification Method** (FDA-style): Req → Design → Code → Verification Method → Verification Status
- **Risk-weighted** (HIPAA-style): adds Severity, Mitigation columns
- **Bidirectional** (ISO 13485): explicit forward and backward trace tables

Cite source template in 10.1 introduction.

#### Mode C — User-defined dimensions

Common user additions:
- **Owner** — who is responsible for each Req's implementation/maintenance
- **Risk** — severity of failing this requirement
- **Operations** — runbook for handling failures of this Req
- **Last verified date** — when was the trace last confirmed accurate
- **Story points** / **PR refs** — link to project management tools

Confirm columns with user.

### Step 3 — For each requirement, trace forward

For each Req row, fill the trace columns:

#### Design column

Where is the design decision documented?

- ADR (Architecture Decision Record) ID if exists
- M2.1 (Product Perspective) for cross-cutting Reqs
- `docs/02_STRATEGIC/SERVER_ARCHITECTURE.md` or equivalent design doc
- "Implicit (not formally designed)" — flag as Open Issue

If a Req has no documented design, that's a finding. Add to 10.2.

#### Code column

Where is the implementing code?

- File path (relative from repo root)
- Optionally: function/class name
- Multiple paths if Req spans files (e.g., FR-AUTH-01 is auth/login.ts AND auth/middleware.ts AND db/users.ts)

If a Req has no implementing code: 
- For greenfield SRS: code doesn't exist yet — mark "Not implemented (target: Phase X)"
- For reverse-engineered SRS: this is a major finding — Req is documented but unimplemented

#### Test column

Where are the verification tests?

- Manual test case IDs (TC-XXX-NN from FR or NFR)
- Automated test names + file path: `auth.spec.ts → 'login with valid credentials'`
- Audit/inspection: "SOC2 audit 2026-Q3" for compliance NFRs
- Performance test: "k6 load test in `tests/perf/api.js`"

Multiple tests OK. Zero tests = orphan; flag as finding.

### Step 4 — Trace backward (test → req)

For each test in the suite, identify which Req it verifies:

```bash
# List automated test files
find tests/ -name "*.test.*" -o -name "*.spec.*"
```

For each test, ask: "Which FR or NFR does this verify?"

- If 1:1 mapping: simple
- If 1:many (one test verifies multiple Reqs): note all
- If 0:1 (test exists but no Req): orphan code/test — flag

This is the most overlooked step. It surfaces tests written without requirements (often technical fixture tests; often acceptable, but document).

### Step 5 — Capture test status

For each row's Test column, record:
- **PASS / FAIL / SKIP / NOT RUN**
- Last run date (use most recent CI run or manual test record)
- Coverage % if applicable (line coverage from `nyc`/`vitest --coverage`)

Use most recent CI run output. If a test has not run in >30 days, flag.

### Step 6 — Identify orphans

After steps 3-5, three orphan categories emerge:

1. **Orphan requirements** — Req has no Code OR no Test → flag in 10.1 Findings
2. **Orphan code** — Code path with no linked Req → may be incidental (utility code) or a missing requirement
3. **Orphan tests** — Test exists with no Req → may be appropriate (fixture, integration scaffolding) or indicate a missing Req

Document all three categories in 10.1.4 Findings.

### Step 7 — Calculate coverage statistics

Aggregate metrics for SRS-level health:

| Metric | Count |
|--------|-------|
| Total FRs | {{N}} |
| FRs with code linked | {{N}} ({{%}}) |
| FRs with test linked | {{N}} ({{%}}) |
| FRs with passing test | {{N}} ({{%}}) |
| Total NFRs | {{N}} |
| NFRs with verification method run | {{N}} ({{%}}) |
| NFRs currently meeting target | {{N}} ({{%}}) |
| Orphan code paths | {{N}} |
| Orphan tests | {{N}} |

Healthy mature project: ≥95% Reqs have code+test, ≥90% have passing test.
Healthy early-stage: ≥70% can be acceptable if explicit roadmap covers gaps.

### Step 8 — Generate output

Use [assets/M10_template.md](assets/M10_template.md). Sections:

- **10.1 Requirements Traceability Matrix** — the main RTM table
- **10.1.1 Coverage statistics** — aggregate metrics
- **10.1.2 Findings** — orphans + gaps
- **10.1.3 Verification log** — when was RTM last validated; signed-off by whom
- **10.2 Open Issues** — preserve any items SRS author left here; add new ones from RTM findings
- **10.3 Appendix** — preserve existing; add per-tool exports if needed

### Step 9 — Self-review

Run [references/checklist.md](references/checklist.md). RTM accuracy is critical — auditors trust RTM as evidence.

## Quality bar

A good RTM lets:
- An auditor verify each requirement has implementation evidence + test evidence
- A QA engineer find untested requirements quickly
- An engineering manager forecast release readiness ("87 of 92 Must FRs have passing tests")
- A new engineer find the code for a feature given the FR ID
- A compliance officer demonstrate audit trail for a regulator

If the RTM is "mostly accurate but I'm not sure about some rows", it fails its primary purpose. Auditors detect imprecision quickly.

## Maintenance burden

RTMs are living documents. They drift fast. Standard maintenance practices:

- **Per-PR update:** PR template asks "Which Req does this implement/test? Update RTM row."
- **Quarterly RTM audit:** verify ≥10% sample for accuracy
- **CI check:** when a test file changes, verify its RTM row still references it
- **Auto-generation tools:** some teams generate RTM from code annotations (e.g., `// @implements FR-AUTH-01`); requires upfront discipline but reduces drift

This skill produces v1; ongoing maintenance is operator/engineering team's responsibility. Document the maintenance approach in 10.1.3.

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations: regulated industries (FDA, HIPAA, PCI demands), greenfield vs. reverse-engineered, monorepo (multiple sub-RTMs), agile teams (RTM as live dashboard), and tools that can generate parts of RTM automatically.

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: "Project Atrium" RTM (continuing from `srs-greenfield-author` and `nfr-specification`) — 47 FRs + 31 NFRs traced to code + tests, with explicit orphan analysis.

## Failure modes to avoid

- **Pretending coverage is high.** "All FRs have tests" — verify by sampling 10 random rows; if any are wrong, claim is invalid.
- **Stale test status.** Auditor sees "PASS" + last run date 6 months ago = automatic skepticism. Re-run tests before claiming PASS.
- **Vague code links.** "src/auth/" — too vague. "src/server/services/auth/login.ts:42-78" — auditable.
- **Skipping NFR verification.** NFRs are harder to trace (no unit test for "p95 ≤ 200ms") but must still have evidence (load test result, audit report, monitoring screenshot).
- **Letting RTM rot.** RTM done once, never updated → useless within months. Build maintenance into engineering workflow.
- **Ignoring orphan code.** Orphan code paths are NOT all bad (utility code is fine), but uninvestigated orphans hide missing requirements.
- **Mode A in regulated industries when company template exists.** If FDA submission requires specific RTM format, Mode A is wrong. Use Mode B.
