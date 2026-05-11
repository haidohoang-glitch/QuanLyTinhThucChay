# Document Index Master — Worked Example

Anonymized. Generating INDEX for a fully-stocked project (Phase 0-4 docs all present).

## Context

**Imagined input:** "Generate INDEX.md for Project Voyager. We have docs in all 5 phase folders. Roles: Tech Lead, Backend Dev, Frontend Dev, QA, DevOps, Product, AI Agent."

**Mode:** A.

---

## Output excerpt

```markdown
# Project Voyager — Document Index (Master Navigation)

> Purpose: Hub navigation for all technical documentation. Start here.
> Last updated: 2026-10-22
> Total docs: 31 files across 5 phase folders + cross-cutting

## 1. Bird's-Eye Map

```
                    ┌──────────────────────────────────────┐
                    │      Voyager Doc Hub                 │
                    └──────────────────────────────────────┘
                                       │
       ┌───────────┬────────────────┬──────────────┬───────────────┐
       ▼           ▼                ▼              ▼               ▼
   Phase 0     Phase 1          Phase 2         Phase 3        Phase 4
  Requirements Discovery        Strategic       Execution      Maintenance
       │           │                │              │               │
   SRS M1-M10   Codebase +       Feasibility +  AI Operator +   Runbooks +
   NFR + RTM    Data audit +     Solution +     Task Dist +     Feature
                Tech debt +      Master Plan    Work Pkgs       extensions
                Business ctx
```

## 2. Folder Structure

```
docs/
├── 00_REQUIREMENTS/
│   └── SRS_VI/
│       ├── M1_Introduction.md
│       ├── M2_Overall_Description.md
│       ├── M3_Authentication.md
│       ├── M4_Customers.md
│       ├── M5_Tracking.md
│       ├── M6_Billing.md
│       ├── M7_Reporting.md
│       ├── M8_Admin.md
│       ├── M9_Non_Functional_Requirements.md
│       └── M10_RTM_Issues_Appendix.md
├── 01_DISCOVERY/
│   ├── CODEBASE_MAP.md
│   ├── DATA_ARCHITECTURE.md
│   ├── TECH_DEBT_AUDIT.md
│   └── BUSINESS_CONTEXT.md
├── 02_STRATEGIC/
│   ├── FEASIBILITY_ASSESSMENT.md
│   ├── TECH_SOLUTION_DESIGN.md
│   └── MASTER_PLAN.md
├── 03_EXECUTION/
│   ├── AI_OPERATOR_GUIDE.md
│   ├── AI_AGENT_TASK_DISTRIBUTION.md
│   ├── 00_TESTING_INFRASTRUCTURE.md
│   ├── A_CODE_SNIPPETS.md
│   ├── B_QA_CHECKLIST_MASTER.md
│   └── work-packages/
│       ├── PHASE_0_PRE_FLIGHT.md
│       ├── PHASE_1_QUICK_WINS.md
│       ├── PHASE_2_DUAL_WRITE.md
│       ├── PHASE_3_SWITCH_READS.md
│       └── PHASE_4_COMPLIANCE.md
├── 04_MAINTENANCE/
│   ├── runbooks/
│   │   ├── INCIDENT_POSTGRES_PRIMARY.md
│   │   ├── INCIDENT_POSTGRES_REPLICA.md
│   │   ├── INCIDENT_PAYMENTS.md
│   │   └── INCIDENT_AUTH_BYPASS.md
│   ├── feature-extensions/
│   │   ├── FEAT_BULK_EXPORT.md
│   │   └── FEAT_2FA_OPTIONAL.md
│   └── DOC_SYNC_REPORT.md
├── INDEX.md
└── QUICK_START.md
```

## 3. Documents by Phase

### 3.0 Phase 0 — Requirements

| File | Purpose | Status | Audience |
|------|---------|--------|----------|
| [M1_Introduction.md](00_REQUIREMENTS/SRS_VI/M1_Introduction.md) | SRS Introduction (purpose, scope, glossary) | Stable v1.0 | All |
| [M2_Overall_Description.md](00_REQUIREMENTS/SRS_VI/M2_Overall_Description.md) | Product perspective, user classes, constraints | Stable v1.0 | Tech Lead, Architect |
| [M3_Authentication.md](00_REQUIREMENTS/SRS_VI/M3_Authentication.md) | Auth FRs (5 FRs: signup, login, reset, logout, verify) | Stable | Dev + QA |
| [M4_Customers.md](00_REQUIREMENTS/SRS_VI/M4_Customers.md) | Customer mgmt FRs (8 FRs) | Stable | Dev + QA |
| [M5_Tracking.md](00_REQUIREMENTS/SRS_VI/M5_Tracking.md) | Logistics tracking FRs (12 FRs) | Stable | Dev + QA |
| [M6_Billing.md](00_REQUIREMENTS/SRS_VI/M6_Billing.md) | Billing + Stripe FRs (7 FRs) | Stable | Dev + QA |
| [M7_Reporting.md](00_REQUIREMENTS/SRS_VI/M7_Reporting.md) | Reporting FRs (6 FRs) | Stable | Dev + QA |
| [M8_Admin.md](00_REQUIREMENTS/SRS_VI/M8_Admin.md) | Admin tools FRs (5 FRs) | Stable | Dev + QA |
| [M9_Non_Functional_Requirements.md](00_REQUIREMENTS/SRS_VI/M9_Non_Functional_Requirements.md) | NFRs (31 NFRs across 8 categories) | Stable v1.0 | All |
| [M10_RTM_Issues_Appendix.md](00_REQUIREMENTS/SRS_VI/M10_RTM_Issues_Appendix.md) | Requirements Traceability Matrix + Open Issues | v0.4 (47 FRs traced; ongoing) | Dev + Auditor |

### 3.1 Phase 1 — Discovery

| File | Purpose | Status | Audience |
|------|---------|--------|----------|
| [CODEBASE_MAP.md](01_DISCOVERY/CODEBASE_MAP.md) | Tech stack, structure, modules, entry points | Stable (audited 2026-09-15) | All |
| [DATA_ARCHITECTURE.md](01_DISCOVERY/DATA_ARCHITECTURE.md) | Storage layers (5 layers), schemas, governance audit | Stable (with R-04 + R-05 follow-ups) | Tech Lead, Backend |
| [TECH_DEBT_AUDIT.md](01_DISCOVERY/TECH_DEBT_AUDIT.md) | 47 findings (P0:3, P1:11, P2:24, P3:9) | Stable | Tech Lead, Backend |
| [BUSINESS_CONTEXT.md](01_DISCOVERY/BUSINESS_CONTEXT.md) | Actors, use cases (40+ UCs), entities, rules, invariants | Stable | Product, PM, AI Agent |

### 3.2 Phase 2 — Strategic

| File | Purpose | Status | Audience |
|------|---------|--------|----------|
| [FEASIBILITY_ASSESSMENT.md](02_STRATEGIC/FEASIBILITY_ASSESSMENT.md) | 3-scenario analysis; recommended Partial $480K / 14 weeks | Approved 2026-08-30 | C-level, PM, Investor |
| [TECH_SOLUTION_DESIGN.md](02_STRATEGIC/TECH_SOLUTION_DESIGN.md) | Active-Passive multi-region (ADR-001) | Approved 2026-09-05 | Tech Lead, Architect |
| [MASTER_PLAN.md](02_STRATEGIC/MASTER_PLAN.md) | 5-phase, 31 WPs, 14 weeks | In progress (Phase 1 done; Phase 2 active) | All roles |

### 3.3 Phase 3 — Execution

| File | Purpose | Status | Audience |
|------|---------|--------|----------|
| [AI_OPERATOR_GUIDE.md](03_EXECUTION/AI_OPERATOR_GUIDE.md) | 14-step workflow + 11 hard rules + system prompts | Active v1.2 | Operator, AI Agents |
| [AI_AGENT_TASK_DISTRIBUTION.md](03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md) | Tier policy (3-tier + Human; ~88% cost saving) | Active v1.0 | Operator, Finance |
| [00_TESTING_INFRASTRUCTURE.md](03_EXECUTION/00_TESTING_INFRASTRUCTURE.md) | Vitest + Playwright + CI setup | Stable | All Devs, QA |
| [A_CODE_SNIPPETS.md](03_EXECUTION/A_CODE_SNIPPETS.md) | Reusable patterns (mocks, hooks, error handlers) | Active | All Devs |
| [B_QA_CHECKLIST_MASTER.md](03_EXECUTION/B_QA_CHECKLIST_MASTER.md) | Master test cases (200+ TCs) | Active | QA |
| [PHASE_0_PRE_FLIGHT.md](03_EXECUTION/work-packages/PHASE_0_PRE_FLIGHT.md) | 8 WPs (auth, deps, observability, security) | DONE 2026-09-12 | Devs |
| [PHASE_1_QUICK_WINS.md](03_EXECUTION/work-packages/PHASE_1_QUICK_WINS.md) | 5 WPs (caching, pagination, rate limiting) | DONE 2026-09-25 | Devs |
| [PHASE_2_DUAL_WRITE.md](03_EXECUTION/work-packages/PHASE_2_DUAL_WRITE.md) | 8 WPs (multi-region setup, CDC, dual-write) | IN PROGRESS | Devs |
| [PHASE_3_SWITCH_READS.md](03_EXECUTION/work-packages/PHASE_3_SWITCH_READS.md) | 5 WPs (gradual rollout, perf tuning) | Pending Phase 2 | Devs |
| [PHASE_4_COMPLIANCE.md](03_EXECUTION/work-packages/PHASE_4_COMPLIANCE.md) | 6 WPs (MFA, GDPR, DR drill, decom legacy) | Pending | Devs |

### 3.4 Phase 4 — Maintenance

| File | Purpose | Status | Audience |
|------|---------|--------|----------|
| [INCIDENT_POSTGRES_PRIMARY.md](04_MAINTENANCE/runbooks/INCIDENT_POSTGRES_PRIMARY.md) | DB primary unreachable playbook | Active (last drilled 2026-09-15) | On-call, DevOps |
| [INCIDENT_POSTGRES_REPLICA.md](04_MAINTENANCE/runbooks/INCIDENT_POSTGRES_REPLICA.md) | DB replica unreachable playbook | Active | On-call, DevOps |
| [INCIDENT_PAYMENTS.md](04_MAINTENANCE/runbooks/INCIDENT_PAYMENTS.md) | Stripe webhook / payment failure playbook | Active | On-call, BE |
| [INCIDENT_AUTH_BYPASS.md](04_MAINTENANCE/runbooks/INCIDENT_AUTH_BYPASS.md) | Suspected breach / auth bypass playbook | Active | On-call, Security |
| [FEAT_BULK_EXPORT.md](04_MAINTENANCE/feature-extensions/FEAT_BULK_EXPORT.md) | Customer bulk export feature | Approved 2026-10-18; In implementation | Product, Eng |
| [FEAT_2FA_OPTIONAL.md](04_MAINTENANCE/feature-extensions/FEAT_2FA_OPTIONAL.md) | Optional 2FA for free tier | Draft | Product, Security |
| [DOC_SYNC_REPORT.md](04_MAINTENANCE/DOC_SYNC_REPORT.md) | Latest doc sync report (2026-10-20) | Latest | All |

### 3.5 Cross-cutting

| File | Purpose |
|------|---------|
| [INDEX.md](INDEX.md) | This file — navigation hub |
| [QUICK_START.md](QUICK_START.md) | Day-1 cheatsheet |

## 4. Document Relationships

(See template — phased flow diagram from Requirements → Discovery → Strategic → Execution → Maintenance)

## 5. Reading Orders per Role

### Tech Lead / Architect
1. INDEX.md (this file)
2. 02_STRATEGIC/TECH_SOLUTION_DESIGN.md (especially ADR-001)
3. 01_DISCOVERY/DATA_ARCHITECTURE.md (Section 6 governance audit + R-04)
4. 02_STRATEGIC/MASTER_PLAN.md
5. PHASE 2 / PHASE 3 work packages (currently active phases)

### Backend Developer
1. INDEX.md
2. 02_STRATEGIC/MASTER_PLAN.md (Section 1-3)
3. 03_EXECUTION/AI_OPERATOR_GUIDE.md (workflow protocol)
4. 03_EXECUTION/00_TESTING_INFRASTRUCTURE.md
5. PHASE 2 work packages (current focus)
6. 03_EXECUTION/A_CODE_SNIPPETS.md (reference)

### QA Engineer
1. INDEX.md
2. 00_REQUIREMENTS/SRS_VI/M3-M8 (FRs)
3. 00_REQUIREMENTS/SRS_VI/M9 (NFRs)
4. 00_REQUIREMENTS/SRS_VI/M10 (RTM)
5. 03_EXECUTION/B_QA_CHECKLIST_MASTER.md
6. Per-phase manual TCs in PHASE_*.md

### DevOps / SRE
1. INDEX.md
2. 03_EXECUTION/00_TESTING_INFRASTRUCTURE.md (CI/CD)
3. PHASE 0 (infra setup) + PHASE 4 (DR drill)
4. 04_MAINTENANCE/runbooks/INCIDENT_*.md (on-call)
5. 01_DISCOVERY/DATA_ARCHITECTURE.md Section 6 (Backup & DR)

### Product / Compliance
1. INDEX.md
2. 02_STRATEGIC/FEASIBILITY_ASSESSMENT.md
3. 00_REQUIREMENTS/SRS_VI/M1, M2, M9
4. PHASE 4 work packages (compliance items)
5. 04_MAINTENANCE/feature-extensions/ (current feature pipeline)

### AI Agent
```
System prompt (Voyager-specific):
"You are an AI agent for Voyager (logistics tracking SaaS).
READ IN ORDER:
1. docs/INDEX.md
2. docs/03_EXECUTION/AI_OPERATOR_GUIDE.md (your protocol — VERY IMPORTANT)
3. docs/02_STRATEGIC/MASTER_PLAN.md
4. docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md (ADR-001 multi-region)
5. docs/03_EXECUTION/00_TESTING_INFRASTRUCTURE.md
6. The specific PHASE_X_*.md for current task

HARD RULES (per Operator Guide Section 2): no autonomous commits, no PR merge,
one WP per PR, no scope drift, no skipping tests, no .env modifications, no prod
deploys + Voyager-specific: DBA on migrations, infra-team on multi-region, Security
Lead on auth/crypto, Compliance Lead on PII data.

START: confirm read; await WP assignment from operator."
```

## 6. Glossary

| Term | Definition |
|------|------------|
| WP | Work Package (single PR scope) |
| FR | Functional Requirement |
| NFR | Non-Functional Requirement |
| RTM | Requirements Traceability Matrix |
| ADR | Architecture Decision Record |
| MoSCoW | Must / Should / Could / Won't priority |
| Verification Gate | Mandatory checklist between phases |
| Tier 1/2/3 | AI tier (Simple/Mid/Strong) |
| Active-Passive | Multi-region pattern: writes US, reads EU/US (per ADR-001) |
| RTO | Recovery Time Objective (≤ 8h per NFR-REL-02) |
| RPO | Recovery Point Objective (≤ 1h per NFR-REL-03) |
| Pro tier | Paid plan ($99/yr/user) — affects feature gating |

## 7. Cross-Document Audit Log

| Date | Change | Files | Reason |
|------|--------|-------|--------|
| 2026-05-05 | Reorganized to phase-based structure | (all docs) | Better navigation; mirrors company-skills/ structure |
| 2026-09-05 | ADR-001 approved (Active-Passive multi-region) | TECH_SOLUTION_DESIGN.md, MASTER_PLAN.md, PHASE_2_*.md | Solution chosen over candidates B and C |
| 2026-09-12 | Phase 0 complete; Verification Gate 0 passed | (DOC_SYNC_REPORT noted) | Milestone |
| 2026-09-25 | Phase 1 complete; Verification Gate 1 passed | (DOC_SYNC_REPORT noted) | Milestone |
| 2026-10-15 | FEAT-042 (Bulk Export) approved | FEAT_BULK_EXPORT.md, M5 SRS update | Customer commitment |

## 8. Maintenance & Contact

| Role | Owner |
|------|-------|
| INDEX maintainer | Doc maintainer (rotation: Sarah K. → Mike J. → Diana L.) |
| Doc sync auditor | Lead Backend Engineer |
| Cross-doc consistency | Tech Lead |

### Update cadence
- INDEX: per-doc add/remove
- Doc Sync Report: monthly
- Consistency Review: quarterly

### Reporting issues
- Slack #docs channel
- GitHub label `docs-drift`
```

---

## Calibration notes

- **31 docs across 5 phases:** realistic for mid-size project. Each phase has its proportionate share.
- **Status reflects reality:** "Phase 1 DONE" — not "Stable" if it's actually complete. Use lifecycle status.
- **Reading orders are role-specific.** Same project, 7 different paths. AI Agent has its own — system prompt fragment included.
- **Audit log preserves history.** Future reader sees milestones (Phase 0 done, ADR approved, FEAT approved) → understands evolution.
- **Maintenance owners specific.** "Doc maintainer (rotation)" beats "TBD".
- **Reading order priorities reflect current state.** Backend Dev order says "PHASE 2 (current focus)" — tells reader where to focus, not just abstract list.
