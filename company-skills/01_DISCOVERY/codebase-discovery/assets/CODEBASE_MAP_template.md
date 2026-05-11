# {{PROJECT_NAME}} — Codebase Map

> **Purpose:** Technical reference describing what this codebase IS — structure, stack, modules, dependencies, build pipeline. Distinct from business requirements (see SRS) and solution design (see Phase 2 docs).
> **Audience:** Engineers onboarding, architects auditing, AI agents needing project context.
> **Last updated:** {{YYYY-MM-DD}}
> **Generated using:** `codebase-discovery` skill v1
> **Reviewer:** {{REVIEWER_NAME_OR_TBD}}

---

## 1. Executive Summary

**What is this project?**
{{ONE_PARAGRAPH_DESCRIPTION — what it does, who uses it, deployment model}}

**Project shape:** {{PRIMARY_SHAPE — see Section 9 for classification mode used}}

**Primary stack:** {{TOP_3_TECHNOLOGIES — e.g., React 19 + Express + Postgres}}

**Maturity signals:**
- Lines of code (approx.): {{NUMBER}}
- Tracked files: {{NUMBER}}
- Last commit: {{DATE}}
- Active branches: {{NUMBER}}
- Test coverage: {{PERCENTAGE_OR_UNKNOWN}}

---

## 2. Tech Stack Inventory

### Runtime / Language

| Component | Version | Notes |
|-----------|---------|-------|
| {{LANGUAGE}} | {{VERSION}} | {{NOTES}} |
| {{RUNTIME}} | {{VERSION}} | {{NOTES}} |

### Framework / Application Layer

| Library | Version | Purpose |
|---------|---------|---------|
| {{FRAMEWORK}} | {{VERSION}} | {{ONE_LINE_PURPOSE}} |

### Data Layer

| Component | Version | Purpose |
|-----------|---------|---------|
| {{DATABASE}} | {{VERSION}} | {{PRIMARY_DB / CACHE / QUEUE}} |

### Build & Tooling

| Tool | Version | Purpose |
|------|---------|---------|
| {{BUILD_TOOL}} | {{VERSION}} | {{e.g., bundler, transpiler, type checker}} |

### Other Notable Dependencies

| Group | Libraries | Purpose |
|-------|-----------|---------|
| Auth | {{LIBRARIES}} | {{PURPOSE}} |
| Observability | {{LIBRARIES}} | {{PURPOSE}} |
| AI / ML | {{LIBRARIES}} | {{PURPOSE}} |
| Utilities | {{COUNT}} libraries (top: {{NAMES}}) | misc |

---

## 3. Folder Structure

```
{{REPO_ROOT}}/
├── {{TOP_LEVEL_FOLDER}}/    {{ONE_LINE_DESCRIPTION}}
├── {{TOP_LEVEL_FOLDER}}/    {{ONE_LINE_DESCRIPTION}}
├── ...
└── {{TOP_LEVEL_FILE}}       {{ONE_LINE_DESCRIPTION}}
```

### Notable folders

**`{{FOLDER_NAME}}/`** — {{PURPOSE}}
- Contains: {{KEY_FILES_OR_SUBFOLDERS}}
- Imported by: {{WHO_USES_IT}}
- Notes: {{ANYTHING_SURPRISING}}

{{REPEAT_FOR_EACH_NOTABLE_FOLDER}}

### Excluded from analysis

- `node_modules/` / `vendor/` / `.venv/` — dependency caches
- `dist/` / `build/` / `out/` — build output
- {{OTHER_EXCLUSIONS}}

---

## 4. Module Boundaries

Logical modules within the application code. Each module has a clear purpose and public surface.

| Module | Path | Purpose | Public surface | Depends on |
|--------|------|---------|---------------|-----------|
| {{MODULE_NAME}} | `{{PATH}}` | {{ONE_LINE}} | {{EXPORTS}} | {{OTHER_MODULES}} |

### Dependency graph

```
{{MODULE_A}} ──depends on──> {{MODULE_B}}
{{MODULE_B}} ──depends on──> {{MODULE_C}}
                             ↑
{{MODULE_D}} ────────────────┘
```

If circular dependencies exist, flag them here. They are red flags.

---

## 5. External Dependencies (Runtime)

### Services this app calls

| Service | Purpose | Connection method | Required env vars |
|---------|---------|-------------------|-------------------|
| {{SERVICE_NAME}} | {{e.g., primary DB, auth, payments}} | {{e.g., HTTP, gRPC, SDK}} | `{{ENV_VAR_1}}`, `{{ENV_VAR_2}}` |

### Services that call this app

| Caller | How | Endpoint(s) |
|--------|-----|-------------|
| {{CALLER}} | {{HTTP/Webhook/Queue}} | {{ENDPOINTS}} |

If unknown, write "Unknown — no inbound traffic documented" rather than omitting the section.

---

## 6. Build & Deploy

### Local development

```bash
{{COMMANDS_TO_GET_RUNNING_LOCALLY}}
```

Expected outcome: {{WHAT_USER_SEES_WHEN_IT_WORKS}}

### Tests

```bash
{{TEST_COMMAND}}
```

Test framework: {{NAME}}
Test file pattern: {{e.g., **/*.test.ts}}
Coverage tool: {{NAME_OR_NONE}}

### Build (production)

```bash
{{BUILD_COMMAND}}
```

Output location: {{PATH}}

### Deploy

| Environment | Method | Triggered by |
|-------------|--------|--------------|
| {{ENV}} | {{e.g., GitHub Actions → AWS, manual SSH, Vercel auto-deploy}} | {{e.g., push to main, manual}} |

If deploy is unknown or undocumented, mark as "Open Question" in Section 8.

---

## 7. Entry Points

For each way this codebase starts executing:

### Entry: {{NAME — e.g., HTTP server / Frontend bootstrap / CLI / Worker}}

- **File:** `{{PATH}}`
- **Triggered by:** {{e.g., npm run start, docker container start, lambda invocation}}
- **First 5-10 lines of execution:**
  1. {{STEP}}
  2. {{STEP}}
  3. {{STEP}}
- **Routes to:** {{WHERE_IT_GOES_NEXT}}

{{REPEAT_FOR_EACH_ENTRY_POINT}}

---

## 8. Open Questions

Things that could NOT be determined from quick reading. Flag for follow-up — these become input for `tech-debt-audit`.

| ID | Question | Where seen | Suggested next step |
|----|----------|------------|---------------------|
| OQ-1 | {{SPECIFIC_QUESTION}} | `{{FILE_OR_FOLDER}}` | {{e.g., interview owner, read full file, run tool}} |
| OQ-2 | {{SPECIFIC_QUESTION}} | `{{FILE_OR_FOLDER}}` | {{NEXT_STEP}} |

If you have <3 open questions, you stopped too early. Look harder — every codebase has surprises.

---

## 9. Notes & Caveats

- **Classification mode:** {{A — Standard taxonomy / B — Honor codebase's existing classification / C — User-defined}}
- **Mode rationale:** {{WHY_THIS_MODE_WAS_CHOSEN — e.g., "Codebase has ARCHITECTURE.md declaring hexagonal style — Mode B" or "User provided custom taxonomy: gateway/orchestration/domain — Mode C" or "Default — no special instruction"}}
- **If Mode B:** Source document = `{{PATH_TO_ARCHITECTURE_DOC}}` (commit `{{COMMIT_HASH}}`)
- **If Mode C:** User-provided categories = {{LIST}}; rationale = {{WHY}}
- **Discovery scope:** This map was generated from {{e.g., reading top 2 folder levels, sampling key files, running build}}. It does NOT include {{WHAT_WAS_NOT_DONE — e.g., runtime profiling, full security review}}.
- **Time spent:** {{HOURS}}
- **Confidence:** {{HIGH/MEDIUM/LOW — calibrate based on how much you had to guess}}
- **Known gaps:** {{WHAT_THIS_MAP_DOES_NOT_COVER}}

---

*This document is descriptive (what IS), not prescriptive (what SHOULD BE). For improvement proposals, see Phase 2 Strategic documents.*
