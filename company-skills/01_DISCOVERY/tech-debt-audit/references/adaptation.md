# Tech Debt Audit — Adaptation

Variations by project shape. Read only the section matching your project.

> **Applies to Mode A only.** Mode B/C adapt principles to your taxonomy.

## Frontend SPA

**Emphasize categories:**
- **PERFORMANCE**: bundle size, render performance, list virtualization, image optimization
- **MAINTAINABILITY**: prop drilling, state management consistency, component duplication
- **CODE_QUALITY**: type coverage, missing keys in lists, inline event handlers in render

**Specific checks:**
- Lighthouse audit (perf score, accessibility score)
- Largest dependencies in bundle (`webpack-bundle-analyzer`, `source-map-explorer`)
- Unused exports (`ts-prune`, `unimported`)
- Inline styles vs design system adherence

**De-emphasize:** SCALABILITY (mostly N/A for client-side); the "it scales by serving more browsers" pattern.

## Backend API

**Emphasize categories:**
- **SECURITY**: auth/authz on every route, input validation, rate limiting, CORS, helmet/equivalent headers
- **RELIABILITY**: timeouts, retries with backoff, idempotency keys, circuit breakers
- **SCALABILITY**: database connection pooling, query patterns, hot keys, in-memory state

**Specific checks:**
- Every route has auth middleware (or explicit `// public` annotation)
- Every external call has a timeout
- Every retry has a max retry count
- Logs do not contain PII / secrets

## Full-stack monolith

Combine Frontend SPA + Backend API. Add:

**Boundary debt:**
- Frontend ↔ Backend contract — is it typed? Does FE know what's required vs optional?
- Validation duplicated FE+BE (good) or only on FE (bad — server is the trust boundary)
- Auth flow correctness (cookies vs JWT vs session)

## Monorepo

**Specific debt patterns:**
- Inconsistent dep versions across packages (different React versions, lockstep failures)
- Circular package deps
- Shared package with no clear owner
- Build cache misconfiguration → slow CI

**Use:** `nx graph`, `pnpm why`, `turbo run --dry-run` to gather signal.

## CLI tool

**Emphasize:**
- **MAINTAINABILITY**: argument parsing consistency, help text completeness, error message quality
- **RELIABILITY**: graceful failure on edge inputs, exit code discipline, signal handling

**De-emphasize:** SCALABILITY (single-process), most SECURITY (unless CLI handles secrets).

## Library / SDK

**Emphasize:**
- **MAINTAINABILITY**: API stability, semver discipline, deprecation policy
- **CODE_QUALITY**: types, examples in docstrings, peer dep declarations
- **COMPLIANCE**: license consistency, third-party license compatibility (especially if vendoring)

**Specific checks:**
- Public API surface area (smaller is better)
- Breaking changes in patch/minor releases (semver violations)
- Bundle size impact on consumers

## Mobile app

**Emphasize:**
- **PERFORMANCE**: app launch time, JS thread blocking, memory leaks, large list scrolling
- **RELIABILITY**: offline behavior, retry/queue logic, background task lifecycle
- **SECURITY**: secure storage usage, certificate pinning, deep link validation

**Specific checks:**
- App size growth trend
- Memory leak indicators (long-running views holding refs)
- Permissions requested vs actually used

## ML pipeline / data science

**Emphasize:**
- **RELIABILITY**: notebook → production gap (code copied, not productionized?)
- **MAINTAINABILITY**: experiment tracking, dependency lock files, environment reproducibility
- **COMPLIANCE**: training data lineage, PII in training data, model bias evaluation

**Specific checks:**
- Notebooks committed without `.ipynb_checkpoints` discipline
- Hardcoded paths to data files (not parameterized)
- Models served from notebooks (production hazard)

**De-emphasize:** Frontend-style PERFORMANCE checks.

## Infrastructure-as-code

**Emphasize:**
- **SECURITY**: IAM least-privilege, public resources, hardcoded secrets in state
- **RELIABILITY**: drift between IaC and actual state, missing tags, region disasters
- **MAINTAINABILITY**: module reuse, version pinning, terragrunt/composition discipline

**Specific checks:**
- Public S3 buckets / public security groups
- IAM `*` policies
- Terraform state stored insecurely (local file vs remote with locking)

---

## Cross-cutting: regulated industries

If healthcare (HIPAA), financial (PCI-DSS), or EU (GDPR), add a COMPLIANCE-heavy review even if those categories normally take less time. Specifically:
- HIPAA: PHI inventory, BAA records, access logging, training records (not in code, but absence is debt to flag)
- PCI-DSS: cardholder data flow, tokenization, network segmentation, key rotation
- GDPR: data residency, consent records, DPA list, deletion cascade
