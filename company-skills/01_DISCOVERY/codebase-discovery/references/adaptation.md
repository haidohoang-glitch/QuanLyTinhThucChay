# Codebase Discovery — Adaptation by Project Shape

The base workflow in `SKILL.md` covers the common case. This file describes shape-specific adjustments — sections to expand, skip, or add. Read only the section matching your project's primary shape (from Step 2).

> **Applies to Mode A (standard taxonomy) only.**
> If you chose **Mode B** (honor codebase's existing classification) or **Mode C** (user-defined), use this file as inspiration but adapt principles to your chosen taxonomy. Do NOT force a Mode B/C project into Mode A shapes — that defeats the purpose of mode flexibility.

## Web Frontend (SPA)

**Expand:**
- Section 2 Tech Stack: include UI library (React/Vue/Svelte), state management (Redux/Zustand/Pinia), routing, styling approach (CSS-in-JS, Tailwind, modules)
- Section 3 Folder Structure: distinguish `components/`, `pages/`, `hooks/`, `services/`, `assets/`, `styles/`
- Section 7 Entry Points: include the bootstrap chain (`index.html` → `main.tsx` → `App.tsx`)

**Add:**
- Routing manifest (which routes exist, where they map)
- Browser support matrix (from `browserslist` or polyfill setup)
- Build output structure (what gets shipped to CDN)

**Skip:** Server-side sections (controllers, middleware) unless full-stack.

## Backend API

**Expand:**
- Section 4 Module Boundaries: organize by domain (users, payments, etc.) AND by layer (controllers, services, repositories)
- Section 5 External Dependencies: emphasize databases, queues, caches, third-party APIs
- Section 7 Entry Points: list HTTP routes with method+path table; for gRPC, list services

**Add:**
- Authentication/authorization model (JWT, sessions, API keys, OAuth)
- Background workers / cron jobs (separate from HTTP entry points)
- Rate limiting / throttling configuration

**Skip:** Frontend bootstrap. UI considerations.

## Full-Stack Monolith

Use **both** Web Frontend AND Backend API guidance, but:

**Add a new section between Section 4 and Section 5:**
- Frontend ↔ Backend boundary: how they communicate (REST? GraphQL? tRPC? Server actions?), where the contract is defined, whether types are shared

**Watch for:** Confusion about which entry point is "primary". Document both clearly in Section 7.

## Monorepo

**Expand:**
- Section 1 Executive Summary: list each package/app and its purpose
- Section 3 Folder Structure: show 3 levels (root → packages → package internals)

**Replace Section 4 (Module Boundaries) with:**
- Package map: name, path, purpose, what depends on what
- Workspace tool (Nx, Turborepo, pnpm workspaces, Lerna) and how tasks compose
- Shared dependencies vs package-specific

**Add:**
- Build orchestration: which packages build first, caching strategy
- Versioning model (independent vs fixed, changesets vs lerna publish)

## CLI Tool

**Expand:**
- Section 7 Entry Points: list every command/subcommand, what each does
- Section 6 Build & Deploy: focus on packaging (npm publish, brew tap, binary release)

**Add:**
- Argument parsing library and command structure
- Distribution channels (npm, homebrew, GitHub releases, PyPI)
- Plugin/extension system if present

**Skip:** Most of Section 5 unless the CLI calls external services.

## Library / SDK

**Expand:**
- Section 4 Module Boundaries: focus on public API surface (what's exported)
- Section 6 Build & Deploy: include packaging output (CJS/ESM/types), publish flow

**Add:**
- API versioning strategy (semver discipline, deprecation policy)
- Tree-shakeability and bundle size
- Peer dependencies and target environments (Node version, browser support)

**Skip:** Section 5 (External Dependencies) — libraries usually don't make network calls. If they do, that's notable.

## Mobile App (React Native, Flutter, native)

**Expand:**
- Section 2 Tech Stack: native bridge layer, platform-specific deps
- Section 3 Folder Structure: distinguish shared vs platform-specific code (`ios/`, `android/`)

**Add:**
- Permissions and capabilities (camera, location, push)
- Build variants (dev, staging, prod) and signing configuration
- App store deployment pipeline
- Offline / sync model if applicable

**Skip:** Server-side sections.

## ML / Data Science

**Expand:**
- Section 2 Tech Stack: include data libs (pandas, polars), ML libs (torch, sklearn), experiment trackers (MLflow, W&B)
- Section 5 External Dependencies: data sources (S3, BigQuery, feature stores), model registries

**Add:**
- Notebook structure: which notebooks are exploratory vs production
- Data pipeline: source → transform → model → serve
- Model artifacts: where trained models live, versioning
- Reproducibility: environment lock files, data snapshots

**Skip:** UI sections.

## Infrastructure-as-Code

**Replace Section 4 with:**
- Resource inventory: every cloud resource declared, grouped by environment
- Module decomposition: which IaC modules wrap what

**Replace Section 7 with:**
- Apply order: which environments deploy first, dependencies between stacks
- State management: where state files live, locking mechanism

**Add:**
- Drift detection process
- Secrets handling (Vault, SSM, Doppler)
- Cost annotations if present

**Skip:** Application code sections.

---

## Mixed shapes

If the project genuinely is multi-shape (e.g., monorepo containing frontend + backend + infra), use the **monorepo** template as the outer structure, and apply each child package's shape guidance within its package section.

Do NOT try to merge all shape guidance into one big document — it will become unreadable. Choose the dominant shape for the outer structure.
