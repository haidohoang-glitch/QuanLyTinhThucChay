---
name: codebase-discovery
description: Reverse-engineer a codebase to produce a standardized CODEBASE_MAP.md document covering tech stack, folder structure, module boundaries, dependencies, build/deploy pipeline, and entry points. Use when onboarding to an unfamiliar project, performing technical due diligence, preparing handover documentation, or generating Phase 1 Discovery output for the company documentation standard. Triggers include phrases like "map this codebase", "do a discovery audit", "I need to understand this project", "generate CODEBASE_MAP", or "Phase 1 Discovery".
---

# Codebase Discovery

Produce a standardized `CODEBASE_MAP.md` describing what a codebase IS — tech stack, structure, modules, dependencies, build pipeline, entry points. This is a *technical view*, distinct from business requirements (SRS) or solution design.

## When this skill applies

Use when:
- First-time onboarding to a legacy or unfamiliar codebase
- Audit/due diligence for M&A or external review
- Producing Phase 1 Discovery output in the company documentation standard
- Quarterly/annual codebase health check

Do NOT use for:
- Greenfield projects with no code yet (use `srs-greenfield-author` instead)
- Business requirements capture (use `business-context-capture` instead)
- Solution design / refactoring proposals (use `tech-solution-design` instead)

## Output

A single file: `docs/01_DISCOVERY/CODEBASE_MAP.md`, filled from the template at [assets/CODEBASE_MAP_template.md](assets/CODEBASE_MAP_template.md).

## Workflow

Follow these steps in order. Do NOT skip steps even if some sections feel "obvious".

### Step 1 — Inventory the workspace

Run these commands and record raw output mentally (do not paste raw output into the final doc):

```bash
ls -la                                    # root layout
cat package.json | head -50               # JS/TS projects
cat requirements*.txt pyproject.toml      # Python projects
cat go.mod Cargo.toml pom.xml             # other ecosystems
cat README.md                             # if exists
git log --oneline -20                     # recent activity
git ls-files | head -50                   # tracked files overview
git ls-files | wc -l                      # total file count
```

Goal: form a hypothesis about what this project IS before reading any source.

### Step 2 — Classify the project shape

There are **3 modes** for classification. Pick ONE before continuing:

| Mode | When to use | Source of taxonomy |
|------|-------------|--------------------|
| **A — Standard taxonomy** *(default)* | No special instruction; codebase has no documented architecture style | The 9-shape table below |
| **B — Honor codebase's existing classification** | Codebase already has `ARCHITECTURE.md`, `HLD.md`, or README clearly labeling its own project type / layering | Whatever the codebase declares |
| **C — User-defined classification** | User provides their own taxonomy in the request (e.g., "classify by service tier" or "use our 5-domain map") | User input |

#### Choosing the mode

1. **If the user explicitly named a mode** (e.g., "use Mode C with these categories"), use it.
2. **Else if the user provided a custom taxonomy** in the request, use Mode C.
3. **Else if the codebase contains an architectural doc** (e.g., `ARCHITECTURE.md`, `HLD.md`, README section explicitly stating "This is a hexagonal/clean/onion architecture"), surface this to the user and ask whether to use Mode B (honor it) or Mode A (override with standard taxonomy). Do not silently pick.
4. **Otherwise, default to Mode A.**

Document the chosen mode and the reason in Section 9 Notes of the output.

#### Mode A — Standard taxonomy (9 shapes)

| Shape | Indicators |
|-------|-----------|
| **Web frontend (SPA)** | `index.html`, `vite.config`/`webpack`, React/Vue/Svelte deps |
| **Backend API** | `server.{ts,py,go}`, framework deps (Express, FastAPI, Gin) |
| **Full-stack monolith** | Both frontend deps + server file in same repo |
| **Monorepo** | `pnpm-workspace.yaml`, `lerna.json`, `nx.json`, multiple `package.json` |
| **CLI tool** | `bin/`, `cli.{ts,py}`, single executable entry |
| **Library / SDK** | `main`/`exports` field in `package.json`, no app entry, has tests |
| **Mobile app** | `ios/`, `android/`, `App.{tsx,swift,kt}`, RN/Flutter deps |
| **ML / Data** | `notebooks/`, `requirements.txt` with `numpy`/`torch`/`pandas` |
| **Infra-as-code** | `*.tf`, `Pulumi.yaml`, `cdk.json`, `helm/` |

If multi-classification (e.g., full-stack monolith with infra), record secondary in Section 9 Notes. Refer to [references/adaptation.md](references/adaptation.md) for shape-specific guidance.

#### Mode B — Honor codebase's existing classification

When the codebase already documents its architecture, follow that taxonomy verbatim. Common cases:

- "Hexagonal / Ports-and-Adapters" → use the project's own port/adapter naming for Section 4 module boundaries
- "Clean Architecture (Entities / Use Cases / Interface Adapters / Frameworks)" → organize Section 4 by these four rings
- "DDD with bounded contexts" → list each bounded context as a module
- "Microservices, X services" → each service is a module; add a service inventory table

In Section 9 Notes, cite the source: "Classification per `ARCHITECTURE.md` (commit abc123)".

`references/adaptation.md` may not apply directly in Mode B — use it only as inspiration. Do not force the project into a shape it has explicitly rejected.

#### Mode C — User-defined classification

When the user provides a custom taxonomy (examples: "by service tier: gateway / orchestration / domain / data", "by team ownership: payments-team / growth-team / platform-team", "by deployment unit: edge / api / batch"), apply it as-is.

Steps:
1. Confirm with the user the categories before proceeding (don't infer if ambiguous).
2. Use those categories to organize Section 4 module boundaries and Section 7 entry points.
3. In Section 9 Notes, record the categories and the user's stated rationale.

Mode C overrides Mode A's shape table — do not mix them.

### Step 3 — Map folder structure

Walk the top 2 levels. For each top-level folder, classify it:

- **App code** (e.g., `src/`, `app/`, `lib/`) — what runtime
- **Config** (e.g., `.config/`, root dotfiles) — what tools
- **Build output** (`dist/`, `build/`, `out/`) — exclude from analysis
- **Dependencies** (`node_modules/`, `vendor/`, `.venv/`) — exclude
- **Tests** (`tests/`, `__tests__/`, `*.test.*`) — what framework
- **Docs** (`docs/`, `*.md` files) — what coverage exists
- **Scripts** (`scripts/`, `bin/`) — what orchestration

For folders with unclear purpose, read 1-2 representative files to deduce. Do NOT read every file.

### Step 4 — Identify module boundaries

Within app code, find logical modules. Heuristics:
- Subfolders named after domain concepts (`payments/`, `users/`, `notifications/`)
- Index/barrel files (`index.ts`, `__init__.py`) exporting a coherent API
- Co-located files (component + style + test in same folder)
- Routing manifests, plugin registrations

For each module, capture: **purpose** (1 line), **public surface** (what other modules import from it), **dependencies** (what it imports). 5-15 modules is typical for a medium project. If you find >25, group them.

### Step 5 — Extract dependencies

Three layers:
1. **Runtime deps** — production libraries (from `dependencies` in `package.json`, `[project.dependencies]` in `pyproject.toml`, etc.). Group: framework, data, auth, AI, observability, utilities.
2. **Dev deps** — testing, linting, build (from `devDependencies`).
3. **External services** — what the app calls out to: databases, APIs, queues, third-party SaaS. Find these by grepping for env var names (`process.env.*`, `os.getenv`), connection string patterns, SDK imports.

If a dependency is non-obvious, add a one-line note explaining what it does. Do not list every utility library; group "and 12 others (utility/polyfill)".

### Step 6 — Trace entry points & data flow

For each entry point, document the first 5-10 lines of execution:

| Entry type | Where to look |
|-----------|---------------|
| HTTP server | `server.ts`, `app.py`, route registrations |
| Frontend bootstrap | `main.tsx`, `index.tsx`, `App.tsx` |
| CLI | `bin/`, shebang scripts |
| Background workers | cron files, queue consumers, `worker.{ts,py}` |
| Build hooks | `prebuild`/`postbuild` scripts in package.json |

Record: what triggers it, what it initializes, what it routes to.

### Step 7 — Find unknowns and risks

Things you could NOT determine from a quick read — flag them as "Open Questions". Examples:
- Folder with cryptic name and no README
- Dependency listed but never imported (or vice versa)
- Multiple servers (`server.ts` + `svr.ts`) with no doc explaining which is canonical
- Hardcoded secrets, hardcoded URLs, hardcoded user IDs
- Test files that look stale (last commit > 1 year ago)
- Build configs that contradict each other

These become input for the next phase (Phase 1 `tech-debt-audit`).

### Step 8 — Fill the template

Open [assets/CODEBASE_MAP_template.md](assets/CODEBASE_MAP_template.md), fill every `{{PLACEHOLDER}}`. Write to `docs/01_DISCOVERY/CODEBASE_MAP.md`.

### Step 9 — Self-review

Run the checklist in [references/checklist.md](references/checklist.md). Do not deliver until all gates pass.

## Quality bar

A good `CODEBASE_MAP.md` lets a new engineer answer these in <5 minutes by reading it:
1. What does this project DO?
2. What stack is it built on?
3. Where do I find the code for feature X?
4. What does it depend on externally?
5. How do I run/build/test it?
6. What's confusing or risky?

If the answer to any of these requires opening source code, the map is incomplete.

## Adaptation for different project shapes

See [references/adaptation.md](references/adaptation.md) for shape-specific sections to add or skip (web frontend vs backend API vs monorepo vs ML vs infra).

## Worked example

See [references/examples.md](references/examples.md) for an anonymized worked example showing the workflow applied to a fictional "Project Atlas" e-commerce monolith.

## Failure modes to avoid

- **Don't paste raw `ls` output as the folder structure section.** Curate. Group similar folders. Annotate.
- **Don't list every npm dependency.** Group by purpose. 50 utility libraries become "13 utility libraries (lodash, dayjs, etc.)".
- **Don't speculate where you don't know.** Mark as "Open Question" with the specific thing that's unclear.
- **Don't include business logic explanations** — that's `business-context-capture`. Stick to technical structure.
- **Don't propose fixes** — that's `tech-debt-audit` and `tech-solution-design`. The map is descriptive, not prescriptive.
- **Don't skip the Open Questions section** — even on a project you understand well, you missed something. Force yourself to find 3+ items.
