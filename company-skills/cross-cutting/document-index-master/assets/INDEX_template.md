# {{PROJECT_NAME}} — Document Index (Master Navigation)

> **Purpose:** Hub navigation for all technical documentation. Start here.
> **Last updated:** {{YYYY-MM-DD}}
> **Total docs:** {{N}} files across {{N}} phase folders + cross-cutting

---

## 1. Bird's-Eye Map

```
                    ┌──────────────────────────────────────┐
                    │      {{PROJECT_NAME}} Doc Hub        │
                    └──────────────────────────────────────┘
                                       │
       ┌───────────┬────────────────┬──────────────┬───────────────┐
       ▼           ▼                ▼              ▼               ▼
   Phase 0     Phase 1          Phase 2         Phase 3        Phase 4
  Requirements Discovery        Strategic       Execution      Maintenance
   (WHAT)      (WHERE WE ARE)   (WHAT TO BUILD) (HOW TO BUILD) (OPERATE)
       │           │                │              │               │
       ▼           ▼                ▼              ▼               ▼
   SRS M1-M10   Audit docs       Solution +      WPs + ops      Runbooks +
   NFR + RTM    + Codebase map   roadmap         protocols      sync reports
```

---

## 2. Folder Structure

```
docs/
├── 00_REQUIREMENTS/        ← WHAT (system requirements)
├── 01_DISCOVERY/           ← WHERE WE ARE (technical audit)
├── 02_STRATEGIC/           ← WHAT TO BUILD (solution + plan)
├── 03_EXECUTION/           ← HOW TO BUILD (AI agents execute)
│   └── work-packages/
├── 04_MAINTENANCE/         ← OPERATE (post-launch)
│   └── runbooks/
│   └── feature-extensions/
├── INDEX.md                ← (this file)
└── QUICK_START.md          ← Day-1 cheatsheet
```

---

## 3. Documents by Phase

### 3.0 Phase 0 — Requirements (WHAT)

| File | Purpose | Status | Audience |
|------|---------|--------|----------|
| [00_REQUIREMENTS/SRS_VI/M1_*.md](00_REQUIREMENTS/SRS_VI/M1_Introduction.md) | SRS Introduction | {{Stable/Draft}} | All |
| [00_REQUIREMENTS/SRS_VI/M2_*.md](00_REQUIREMENTS/SRS_VI/M2_Overall_Description.md) | Overall description | {{...}} | Tech Lead, Architect |
| [00_REQUIREMENTS/SRS_VI/M3-Mx](00_REQUIREMENTS/SRS_VI/) | Functional requirements per domain | {{...}} | Dev + QA |
| [00_REQUIREMENTS/SRS_VI/M9_*.md](00_REQUIREMENTS/SRS_VI/M9_Non_Functional_Requirements.md) | NFRs | {{...}} | All |
| [00_REQUIREMENTS/SRS_VI/M10_*.md](00_REQUIREMENTS/SRS_VI/M10_RTM_Issues_Appendix.md) | RTM + Issues + Appendix | {{...}} | Dev + Auditor |

### 3.1 Phase 1 — Discovery (WHERE WE ARE)

| File | Purpose | Status | Audience |
|------|---------|--------|----------|
| [01_DISCOVERY/CODEBASE_MAP.md](01_DISCOVERY/CODEBASE_MAP.md) | Tech stack, structure, modules | {{...}} | All |
| [01_DISCOVERY/DATA_ARCHITECTURE.md](01_DISCOVERY/DATA_ARCHITECTURE.md) | Storage layers, data flow, governance | {{...}} | Tech Lead, Backend |
| [01_DISCOVERY/TECH_DEBT_AUDIT.md](01_DISCOVERY/TECH_DEBT_AUDIT.md) | Code quality, security, perf findings | {{...}} | Tech Lead, Backend |
| [01_DISCOVERY/BUSINESS_CONTEXT.md](01_DISCOVERY/BUSINESS_CONTEXT.md) | Domain logic, actors, use cases | {{...}} | Product, PM, AI Agent |
| (Optional security audit, etc.) | | | |

### 3.2 Phase 2 — Strategic (WHAT TO BUILD)

| File | Purpose | Status | Audience |
|------|---------|--------|----------|
| [02_STRATEGIC/FEASIBILITY_ASSESSMENT.md](02_STRATEGIC/FEASIBILITY_ASSESSMENT.md) | ROI, business case, scenarios | {{...}} | C-level, PM, Investor |
| [02_STRATEGIC/TECH_SOLUTION_DESIGN.md](02_STRATEGIC/TECH_SOLUTION_DESIGN.md) | Chosen solution + ADRs | {{...}} | Tech Lead, Architect |
| [02_STRATEGIC/MASTER_PLAN.md](02_STRATEGIC/MASTER_PLAN.md) | Multi-phase implementation plan | {{...}} | All roles |

### 3.3 Phase 3 — Execution (HOW TO BUILD)

| File | Purpose | Status | Audience |
|------|---------|--------|----------|
| [03_EXECUTION/AI_OPERATOR_GUIDE.md](03_EXECUTION/AI_OPERATOR_GUIDE.md) | Operator manual, hard rules, 14-step workflow | {{...}} | Operator, AI Agents |
| [03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md](03_EXECUTION/AI_AGENT_TASK_DISTRIBUTION.md) | Multi-tier AI routing policy | {{...}} | Operator, Finance |
| [03_EXECUTION/00_TESTING_INFRASTRUCTURE.md](03_EXECUTION/00_TESTING_INFRASTRUCTURE.md) | Test framework setup | {{...}} | All Devs, QA |
| [03_EXECUTION/work-packages/PHASE_0_*.md](03_EXECUTION/work-packages/PHASE_0_PRE_FLIGHT.md) | Phase 0 work packages | {{...}} | Devs |
| [03_EXECUTION/work-packages/PHASE_1_*.md](03_EXECUTION/work-packages/PHASE_1_QUICK_WINS.md) | Phase 1 work packages | {{...}} | Devs |
| (more phases) | | | |
| [03_EXECUTION/A_CODE_SNIPPETS.md](03_EXECUTION/A_CODE_SNIPPETS.md) | Reusable code patterns | {{...}} | All Devs |
| [03_EXECUTION/B_QA_CHECKLIST_MASTER.md](03_EXECUTION/B_QA_CHECKLIST_MASTER.md) | Master QA checklist | {{...}} | QA |

### 3.4 Phase 4 — Maintenance (OPERATE)

| File | Purpose | Status | Audience |
|------|---------|--------|----------|
| [04_MAINTENANCE/runbooks/INCIDENT_*.md](04_MAINTENANCE/runbooks/) | Per-incident playbooks | {{...}} | On-call, DevOps |
| [04_MAINTENANCE/feature-extensions/FEAT_*.md](04_MAINTENANCE/feature-extensions/) | Feature spec docs | {{...}} | Product, Eng |
| [04_MAINTENANCE/DOC_SYNC_REPORT.md](04_MAINTENANCE/DOC_SYNC_REPORT.md) | Latest doc drift report | {{...}} | All |

### 3.5 Cross-cutting

| File | Purpose | Audience |
|------|---------|----------|
| [INDEX.md](INDEX.md) | This file — navigation hub | All |
| [QUICK_START.md](QUICK_START.md) | Day-1 cheatsheet | New onboardees |

---

## 4. Document Relationships

```
┌────────────────────────────────────────────────────────────────┐
│ Phase 0 Requirements                                           │
│   SRS M1-M10 — what the system must do                         │
└────────────────┬───────────────────────────────────────────────┘
                 │ (input to)
                 ▼
┌────────────────────────────────────────────────────────────────┐
│ Phase 1 Discovery                                              │
│   Codebase / Data / Tech Debt / Business Context audits        │
└────────────────┬───────────────────────────────────────────────┘
                 │ (input to)
                 ▼
┌────────────────────────────────────────────────────────────────┐
│ Phase 2 Strategic                                              │
│   Feasibility (business case)                                  │
│   Tech Solution Design (chosen architecture)                   │
│   Master Plan (multi-phase roadmap)                            │
└────────────────┬───────────────────────────────────────────────┘
                 │ (input to)
                 ▼
┌────────────────────────────────────────────────────────────────┐
│ Phase 3 Execution                                              │
│   AI Operator Guide (supervision protocol)                     │
│   AI Task Distribution (tier policy)                           │
│   Work Packages per phase + tests                              │
└────────────────┬───────────────────────────────────────────────┘
                 │ (after go-live)
                 ▼
┌────────────────────────────────────────────────────────────────┐
│ Phase 4 Maintenance                                            │
│   Incident playbooks                                           │
│   Feature extensions                                           │
│   Doc sync reports                                             │
└────────────────────────────────────────────────────────────────┘
```

---

## 5. Reading Order per Role

### Tech Lead / Architect
```
1. INDEX.md (this file)
2. 02_STRATEGIC/TECH_SOLUTION_DESIGN.md (especially ADRs)
3. 01_DISCOVERY/DATA_ARCHITECTURE.md
4. 02_STRATEGIC/MASTER_PLAN.md
5. 03_EXECUTION/work-packages/PHASE_*.md (lookup as needed)
```

### Backend Developer
```
1. INDEX.md
2. 02_STRATEGIC/MASTER_PLAN.md (Section 1-3)
3. 02_STRATEGIC/TECH_SOLUTION_DESIGN.md (component design)
4. 03_EXECUTION/00_TESTING_INFRASTRUCTURE.md
5. 03_EXECUTION/work-packages/PHASE_0_*.md
6. ... per WP being executed
7. 03_EXECUTION/A_CODE_SNIPPETS.md (reference)
```

### Frontend Developer
```
1. INDEX.md
2. 02_STRATEGIC/MASTER_PLAN.md
3. 03_EXECUTION/00_TESTING_INFRASTRUCTURE.md
4. 03_EXECUTION/work-packages/PHASE_0_*.md (UI-related WPs)
5. 03_EXECUTION/work-packages/PHASE_1_*.md
6. 03_EXECUTION/A_CODE_SNIPPETS.md
```

### QA Engineer
```
1. INDEX.md
2. 00_REQUIREMENTS/SRS_VI/M3-Mx (FRs to test)
3. 00_REQUIREMENTS/SRS_VI/M9 (NFRs)
4. 00_REQUIREMENTS/SRS_VI/M10 (RTM)
5. 03_EXECUTION/00_TESTING_INFRASTRUCTURE.md
6. 03_EXECUTION/B_QA_CHECKLIST_MASTER.md
7. Each PHASE_*.md (manual TC sections)
```

### DevOps / SRE
```
1. INDEX.md
2. 03_EXECUTION/00_TESTING_INFRASTRUCTURE.md (CI/CD)
3. 03_EXECUTION/work-packages/PHASE_0_*.md (infra setup WPs)
4. 04_MAINTENANCE/runbooks/INCIDENT_*.md (on-call playbooks)
5. 03_EXECUTION/work-packages/PHASE_4_*.md (DR drill, compliance)
```

### Product / Compliance
```
1. INDEX.md
2. 02_STRATEGIC/FEASIBILITY_ASSESSMENT.md (business case)
3. 00_REQUIREMENTS/SRS_VI/M1, M2, M9 (overview + NFRs)
4. 03_EXECUTION/work-packages/PHASE_4_*.md (compliance items)
```

### AI Agent (autonomous execution under supervision)
```
System prompt:
"You are an AI agent for {{PROJECT}}. Read these docs in order:
1. docs/INDEX.md
2. docs/03_EXECUTION/AI_OPERATOR_GUIDE.md (your protocol)
3. docs/02_STRATEGIC/MASTER_PLAN.md
4. docs/02_STRATEGIC/TECH_SOLUTION_DESIGN.md
5. docs/03_EXECUTION/00_TESTING_INFRASTRUCTURE.md
6. Specific WP doc for current task
Follow operator guide hard rules. Report plan before coding."
```

---

## 6. Glossary

| Term | Definition |
|------|------------|
| **WP** | Work Package — single-PR-scoped unit of execution |
| **FR** | Functional Requirement (M3-Mx of SRS) |
| **NFR** | Non-Functional Requirement (M9 of SRS) |
| **RTM** | Requirements Traceability Matrix (M10 of SRS) |
| **ADR** | Architecture Decision Record |
| **MoSCoW** | Priority rubric: Must / Should / Could / Won't |
| **Verification Gate** | Mandatory checklist between phases (must PASS before next phase) |
| **Tier 1 / 2 / 3 AI** | Multi-tier routing classification (Simple / Mid / Strong) |
| {{PROJECT_GLOSSARY_TERMS}} | {{...}} |

---

## 7. Cross-Document Corrections / Audit Log

Significant changes affecting multiple docs:

| Date | Change | Files affected | Reason |
|------|--------|----------------|--------|
| {{YYYY-MM-DD}} | {{e.g., Reorganized to phase-based structure}} | (all docs) | {{Better navigation}} |
| {{YYYY-MM-DD}} | {{e.g., Auth approach corrected}} | TECH_SOLUTION_DESIGN.md, PHASE_0_*.md | {{Discovered API constraint}} |

---

## 8. Maintenance & Contact

| Role | Owner |
|------|-------|
| INDEX maintainer | {{NAME or role}} |
| Doc sync auditor | {{NAME or role}} |
| Cross-doc consistency | {{NAME or role}} |

### Update cadence

- **INDEX:** updated when docs added/removed; verify quarterly
- **Doc Sync Report:** monthly (latest at `04_MAINTENANCE/DOC_SYNC_REPORT.md`)
- **Consistency Review:** quarterly (latest at `04_MAINTENANCE/CONSISTENCY_REVIEW_REPORT.md`)

### Reporting issues

If you find a broken link, missing doc, or outdated info: open issue with label `docs-drift` (auto-tracked in next sync run).

---

*This index is the single source of truth for doc navigation. If a doc isn't here, it's not part of the official doc system.*
