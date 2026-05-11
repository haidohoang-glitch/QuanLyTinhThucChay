# Codebase Discovery — Worked Example

This is an **anonymized** example showing the workflow applied end-to-end. The fictional project is "Project Atlas", a small e-commerce monolith. Use this to calibrate your output style — not to copy content.

---

## Context

**Imagined input:** "Map this codebase. We're considering acquiring this company and need a tech audit."

**Project shape (from Step 2):** Full-stack monolith.

**Time budget:** 2 hours.

---

## Generated output (excerpt)

```markdown
# Project Atlas — Codebase Map

> Purpose: Technical reference describing what this codebase IS...
> Last updated: 2026-03-15
> Generated using: codebase-discovery skill v1
> Reviewer: TBD

---

## 1. Executive Summary

Project Atlas is a B2C e-commerce platform serving ~5K daily active users. It runs as a
single deployable: a Node.js Express server that renders SSR pages and exposes a
REST API consumed by a React admin panel. Data lives in Postgres with Redis for sessions.
The codebase has been actively maintained for ~3 years (first commit 2023-01-12, latest
2026-03-10).

**Project shape:** Full-stack web monolith
**Primary stack:** Express 4.x + React 18 + Postgres 15
**Maturity signals:**
- LOC (approx.): 47,000
- Tracked files: 612
- Last commit: 2026-03-10
- Active branches: 4
- Test coverage: ~38% (statement coverage from `nyc`)

## 2. Tech Stack Inventory

### Runtime / Language

| Component | Version | Notes |
|-----------|---------|-------|
| Node.js | 18.17 | Single version pinned via `.nvmrc` |
| TypeScript | 4.9 | Strict mode disabled in 14 files (see Open Questions) |

### Framework / Application Layer

| Library | Version | Purpose |
|---------|---------|---------|
| Express | 4.18 | HTTP server + routing |
| React | 18.2 | Admin UI |
| EJS | 3.1 | SSR templating for storefront |
| Sequelize | 6.32 | ORM for Postgres |

### Data Layer

| Component | Version | Purpose |
|-----------|---------|---------|
| Postgres | 15 | Primary store (orders, products, users) |
| Redis | 7 | Session store + rate-limit counters |
| S3 (AWS) | n/a | Product images, invoices |

### Build & Tooling

| Tool | Version | Purpose |
|------|---------|---------|
| esbuild | 0.19 | Frontend bundler |
| ts-node | 10.9 | Backend dev server |
| Jest | 29 | Unit + integration tests |
| ESLint | 8.x | Linting |

### Other Notable Dependencies

| Group | Libraries | Purpose |
|-------|-----------|---------|
| Auth | passport, passport-local, bcrypt | Username/password + sessions |
| Payments | stripe (SDK), stripe-event-types | Charges + webhooks |
| Email | nodemailer, sendgrid | Transactional |
| Observability | winston, sentry/node | Logs + error tracking |
| Utilities | 18 libraries (lodash, dayjs, zod, etc.) | misc |

## 3. Folder Structure

```
atlas/
├── src/
│   ├── server/         Express app, routes, middleware
│   ├── client/         React admin SPA
│   ├── shared/         Types + validators used by both
│   └── jobs/           Cron + queue workers
├── views/              EJS templates for storefront SSR
├── public/             Static assets
├── migrations/         Sequelize migration files
├── scripts/            Ops scripts (backfills, seeders)
├── tests/              Test fixtures + integration suites
├── .github/workflows/  CI/CD definitions
└── docker-compose.yml  Local dev stack
```

### Notable folders

**`src/server/`** — Express app entry and HTTP layer
- Contains: `index.ts` (entry), `routes/`, `middleware/`, `services/`, `models/`
- Imported by: `src/jobs/` reuses services for background processing
- Notes: `routes/legacy/` contains 6 endpoints marked `@deprecated` in JSDoc but still wired up.
  Not clear if any client still uses them. → Open Question.

**`src/client/`** — React admin SPA
- Contains: `App.tsx`, `pages/`, `components/`, `hooks/`, `api/`
- Imported by: standalone — bundled separately, served from `/admin/*`
- Notes: Two competing styling approaches (CSS Modules in 60% of files, styled-components in 40%).
  → Open Question.

**`src/shared/`** — Shared types and Zod validators
- Contains: type definitions for API request/response shapes, validation schemas
- Imported by: both `server/` and `client/`
- Notes: This is the source of truth for the API contract. Healthy pattern.

**`src/jobs/`** — Background workers
- Contains: 4 BullMQ consumers + 3 cron entries (registered via node-cron)
- Imported by: separate `worker.ts` entry point
- Notes: Workers reuse `src/server/services/` directly (no separate worker service layer).
  Tight coupling — if HTTP layer breaks, workers break too.

### Excluded from analysis

- `node_modules/`, `dist/`, `.cache/`, `coverage/`

## 4. Module Boundaries

| Module | Path | Purpose | Public surface | Depends on |
|--------|------|---------|---------------|-----------|
| auth | `src/server/services/auth/` | User login, password reset, session mgmt | `login`, `logout`, `requestReset` | users, email |
| users | `src/server/services/users/` | User CRUD + profile | `createUser`, `getUser`, `updateProfile` | (none) |
| products | `src/server/services/products/` | Product catalog | `listProducts`, `getProduct`, `searchProducts` | (none) |
| orders | `src/server/services/orders/` | Order lifecycle | `createOrder`, `cancelOrder`, `fulfillOrder` | products, payments, email, users |
| payments | `src/server/services/payments/` | Stripe integration | `chargeCard`, `handleWebhook` | (Stripe SDK) |
| email | `src/server/services/email/` | Templated transactional email | `sendOrderConfirmation`, `sendPasswordReset` | (SendGrid SDK) |
| analytics | `src/server/services/analytics/` | Event capture | `track` | (none — fire-and-forget) |
| jobs | `src/jobs/*` | Background workers | (no exports — entry-only) | orders, email, products |

### Dependency graph

```
       ┌──> users
auth ──┤
       └──> email

orders ──> products
       ──> payments
       ──> email
       ──> users

jobs ──> orders, email, products  (worker layer reuses services)
```

No circular dependencies detected.

## 5. External Dependencies (Runtime)

### Services this app calls

| Service | Purpose | Connection method | Required env vars |
|---------|---------|-------------------|-------------------|
| Postgres | Primary DB | Sequelize (TCP) | `DATABASE_URL` |
| Redis | Sessions, rate limit | ioredis (TCP) | `REDIS_URL` |
| Stripe | Payments | SDK (HTTPS) | `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET` |
| SendGrid | Transactional email | SDK (HTTPS) | `SENDGRID_API_KEY`, `SENDGRID_FROM_ADDRESS` |
| AWS S3 | Image storage | SDK (HTTPS) | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `S3_BUCKET` |
| Sentry | Error tracking | SDK (HTTPS) | `SENTRY_DSN` |

### Services that call this app

| Caller | How | Endpoint(s) |
|--------|-----|-------------|
| Storefront customer browsers | HTTPS (SSR pages) | `/`, `/products/*`, `/cart`, `/checkout` |
| Admin browsers | HTTPS (SPA) | `/admin/*`, `/api/admin/*` |
| Stripe webhooks | HTTPS POST | `/webhooks/stripe` |
| Cron (external scheduler) | HTTPS | `/internal/cron/run` (auth via shared secret header) |

## 6. Build & Deploy

### Local development

```bash
cp .env.example .env
docker compose up -d postgres redis
npm install
npm run db:migrate
npm run dev
```

Expected outcome: storefront at http://localhost:3000, admin at http://localhost:3000/admin (login admin@example.com / changeme).

### Tests

```bash
npm test              # unit tests (Jest)
npm run test:e2e      # integration tests against dockerized Postgres
```

Test framework: Jest 29
Test file pattern: `**/*.test.ts`, `**/*.spec.ts`
Coverage tool: nyc (current: ~38%)

### Build (production)

```bash
npm run build
```

Output: `dist/server/` (transpiled JS), `dist/client/` (bundled React)

### Deploy

| Environment | Method | Triggered by |
|-------------|--------|--------------|
| staging | GitHub Actions → ECS Fargate | push to `develop` |
| production | GitHub Actions → ECS Fargate (manual approval) | tagged release |

## 7. Entry Points

### Entry: HTTP server

- **File:** `src/server/index.ts`
- **Triggered by:** `npm run start` (production) or `npm run dev` (development)
- **First 5-10 lines of execution:**
  1. Load env vars via dotenv
  2. Initialize Sentry
  3. Connect to Postgres (Sequelize) and Redis
  4. Create Express app, register middleware (helmet, cors, body parser, session, passport)
  5. Mount route modules from `routes/`
  6. Listen on `process.env.PORT || 3000`
- **Routes to:** `routes/storefront/*`, `routes/admin/*`, `routes/api/*`, `routes/webhooks/*`

### Entry: Background worker

- **File:** `src/jobs/worker.ts`
- **Triggered by:** separate ECS task started from same Docker image (different command)
- **First 5-10 lines:**
  1. Load env vars
  2. Connect to Redis (BullMQ)
  3. Connect to Postgres (Sequelize, reused pool)
  4. Register BullMQ consumers (order-fulfillment, email-send, image-process, analytics-flush)
  5. Register node-cron entries (daily-cleanup, weekly-report, hourly-stripe-reconcile)
- **Routes to:** Service layer in `src/server/services/`

## 8. Open Questions

| ID | Question | Where seen | Suggested next step |
|----|----------|------------|---------------------|
| OQ-1 | Are `routes/legacy/*` endpoints still in use? | `src/server/routes/legacy/` | grep client code + check access logs for past 30 days |
| OQ-2 | Why two styling approaches (CSS Modules + styled-components)? Migration in progress or accidental? | `src/client/` | Interview frontend lead |
| OQ-3 | TypeScript strict mode disabled in 14 files via `// @ts-nocheck` | grep `// @ts-nocheck` | Triage each file — fix or document |
| OQ-4 | Cron auth uses shared secret via header `X-Cron-Secret`. Is the secret rotated? | `src/server/routes/internal/cron.ts` | Check ops runbook (separate system) |
| OQ-5 | Test coverage on `payments/` is 12% (vs 38% project avg). Risky given financial impact. | `coverage/` report | Flag for `tech-debt-audit` |

## 9. Notes & Caveats

- **Discovery scope:** Read top 2 folder levels, sampled 1-2 files per top-level folder, ran build successfully, ran tests (some failures unrelated to discovery).
- **Time spent:** 2 hours
- **Confidence:** Medium-High. Open Questions reflect genuine uncertainty, not laziness.
- **Known gaps:** Did not analyze GitHub Actions workflows in detail. Did not profile runtime performance. Did not audit security configuration of Sentry, Stripe webhook verification, or session cookie attributes — those belong to `tech-debt-audit`.
```

---

## What this example demonstrates

1. **Specificity over vagueness.** "auth lives in `src/server/services/auth/`" is more useful than "auth handling exists somewhere".
2. **Honest uncertainty.** OQ-1 (legacy routes) is not pretended to be answered — it's flagged.
3. **Cross-references downstream.** OQ-5 explicitly notes "flag for tech-debt-audit" — Discovery doesn't propose fixes.
4. **Curated, not raw.** The folder structure section doesn't paste `ls` output; it groups and annotates.
5. **Counts and dates.** Maturity signals use real numbers (47K LOC, 612 files, 38% coverage). If unknown, mark unknown — don't omit.

## What it deliberately does NOT do

- Does not say "the architecture is bad" or "this should be refactored" — descriptive only.
- Does not explain the BUSINESS (what an "order" represents in domain terms) — that's `business-context-capture`.
- Does not propose a remediation plan — that's `tech-solution-design` and `implementation-planning`.
