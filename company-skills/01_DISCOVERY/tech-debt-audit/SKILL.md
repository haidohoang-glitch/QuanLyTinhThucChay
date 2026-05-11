---
name: tech-debt-audit
description: Audit a codebase for technical debt across code quality, security, performance, reliability, maintainability, scalability, and compliance. Produces a standardized TECH_DEBT_AUDIT.md with categorized, severity-rated findings, each with evidence and remediation effort estimates. Use when preparing for refactor, due diligence, security review, or generating Phase 1 Discovery output. Triggers include "find tech debt", "code quality audit", "security review", "what should we fix first", "generate TECH_DEBT_AUDIT", or "Phase 1 Discovery audit".
---

# Tech Debt Audit

Identify and rank technical debt across multiple categories. Output is descriptive (what's broken / risky), not prescriptive (the fixes belong in Phase 2).

## When this skill applies

Use when:
- Preparing for a refactor or rewrite
- M&A due diligence
- Periodic codebase health check (annual/quarterly)
- Triaging accumulated debt before a release freeze
- Producing Phase 1 Discovery debt output

Do NOT use for:
- Mapping codebase structure (use `codebase-discovery`)
- Data layer audit (use `data-architecture-audit`)
- Designing the fix (use `tech-solution-design`)
- Planning the work (use `implementation-planning`)

## Output

A single file: `docs/01_DISCOVERY/TECH_DEBT_AUDIT.md`, filled from [assets/TECH_DEBT_AUDIT_template.md](assets/TECH_DEBT_AUDIT_template.md).

## Workflow

### Step 1 — Inventory existing quality signals

Cheap signals to gather first:

```bash
# Test coverage
npm test -- --coverage 2>&1 | tail -20
# Lint errors
npm run lint 2>&1 | tail -50
# Type errors
npx tsc --noEmit 2>&1 | tail -50
# Outdated/vulnerable deps
npm audit 2>&1 | head -30
npm outdated 2>&1 | head -30
# Bundle size (if applicable)
npm run build 2>&1 | tail -20
# Git age signals (stale code)
git log --diff-filter=A --name-only --pretty=format: | sort -u | tail -50
```

For non-JS projects, use equivalents: `pytest --cov`, `pyright`, `cargo audit`, `go vet`, etc.

These provide raw data, not findings. Findings come from interpretation.

### Step 2 — Choose categorization mode

Three modes:

| Mode | When to use | Source of categories |
|------|-------------|----------------------|
| **A — Standard categories** *(default)* | No special instruction | The 7 categories below |
| **B — Honor codebase's existing categories** | Codebase has prior audit doc, ADRs, or `DEBT_BACKLOG.md` using its own categories | Codebase docs |
| **C — User-defined categories** | User provides own taxonomy ("must-fix / should-fix / nice-to-have", or per-team buckets) | User input |

Selection logic:
1. User explicitly named a mode → use it.
2. Codebase has prior audit using its own categories → ask user (Mode A or B?).
3. Default → Mode A.

Document mode and rationale in Section 9.

#### Mode A — Standard categories

| Category | Examples |
|----------|----------|
| **CODE_QUALITY** | Duplication, long functions, complex conditionals, dead code, missing types |
| **SECURITY** | Injection vectors, auth flaws, secret exposure, missing rate limits, deps with CVEs |
| **PERFORMANCE** | N+1 queries, blocking I/O, render thrash, unbounded memory growth |
| **RELIABILITY** | Missing error handling, silent failures, retry-without-idempotency, unbounded retries |
| **MAINTAINABILITY** | Outdated deps, untested code, missing docs, inconsistent patterns |
| **SCALABILITY** | Hardcoded limits, single-instance assumptions, hot keys, missing pagination |
| **COMPLIANCE** | Missing GDPR/CCPA paths, audit log gaps, retention violations, license issues |

#### Mode B — Honor codebase's categories

If the project already organizes debt by its own buckets (e.g., "MFA backlog", "billing rewrite", "platform stability"), use those. Cite source doc in Section 9.

#### Mode C — User-defined

Common user-supplied taxonomies:
- By urgency: must-fix / should-fix / nice-to-have
- By team: team-A / team-B / shared
- By release: blocks-v3 / post-v3 / vaporware

Confirm categories with user before proceeding.

### Step 3 — Hunt for findings, by category

For each category (Mode A) or bucket (Mode B/C), look explicitly:

#### CODE_QUALITY

```bash
# Files >500 LOC are usually a smell
find . -path ./node_modules -prune -o -name "*.{ts,tsx,js,py,go}" -print | xargs wc -l 2>/dev/null | sort -rn | head -10
# Functions with cyclomatic complexity (manual: scan files >500 LOC)
# Dead exports
grep -rE "^export" src/ | wc -l   # then sample, check if used
```

#### SECURITY

```bash
# Hardcoded secrets
grep -rE "(api[_-]?key|secret|password|token).{0,20}=.{0,5}['\"][A-Za-z0-9+/=]{20,}" --include="*.{ts,js,py,go,env*}" .
# Direct SQL string concatenation (injection risk)
grep -rE "(query|execute)\(\s*[\"'].*\$\{|.*\+\s*req\." --include="*.{ts,js,py}" .
# CORS wide open
grep -rE "Access-Control-Allow-Origin.*\*|cors\(\s*\)" --include="*.{ts,js}" .
# Auth missing on routes
# (manual: read route definitions, look for endpoints without auth middleware)
```

#### PERFORMANCE

```bash
# N+1 patterns: loop over array, await inside loop with DB call
grep -rB1 -A3 "for.*await.*find\|forEach.*await\|map.*await" --include="*.{ts,js}" .
# Synchronous file I/O on hot path
grep -rE "fs\.readFileSync|fs\.writeFileSync" --include="*.{ts,js}" .
# Missing pagination on list endpoints
# (manual: read endpoints returning arrays, check for limit/offset)
```

#### RELIABILITY

```bash
# Empty catch blocks
grep -rE "catch\s*\([^)]*\)\s*\{\s*\}" --include="*.{ts,js,py}" .
# Unawaited promises
# (run lint with no-floating-promises rule, or grep promise patterns)
# Hardcoded timeouts/retries
grep -rE "setTimeout.*1000.*\*|retries:\s*\d+" --include="*.{ts,js}" .
```

#### MAINTAINABILITY

- Run `npm outdated`; flag majors >1 version behind
- Test coverage <60% in critical paths is debt
- Missing CI/CD pipeline is debt

#### SCALABILITY

- Hardcoded user IDs, hardcoded admin emails (single-tenant assumption)
- In-memory rate limiting (won't survive horizontal scaling)
- File uploads to local disk (won't survive container restart)

#### COMPLIANCE

- Search for "GDPR", "CCPA", "audit_log" in codebase — absence is a finding
- Check if user deletion exists; check if it cascades
- Check license headers, license file, third-party license compatibility

### Step 4 — Score each finding

Severity rubric (apply consistently):

- **P0** — Security incident, data loss, or compliance violation already happening or imminent (<7 days). Stop work and fix.
- **P1** — High likelihood of incident in <90 days, OR active customer-facing degradation. Plan now, ship within sprint.
- **P2** — Latent risk, doesn't manifest under current conditions but will at growth/change. Address in next planning cycle.
- **P3** — Notable; tracked but not urgent. May be acceptable forever.

Calibration check: **most P0 audits inflate**. Be ruthless. A finding without an articulated <7-day failure mode is NOT P0.

### Step 5 — Estimate remediation effort

For each finding, estimate developer-hours to fix:

- **XS** (<2h): config change, single-file fix
- **S** (2-8h): localized refactor, add a missing piece
- **M** (1-3 days): cross-cutting change, multiple files, requires testing
- **L** (3-10 days): architectural change, requires migration or coordination
- **XL** (>2 weeks): rewrite, major refactor, needs project plan

Don't pretend precision. Effort estimates calibrate prioritization, not budgets.

### Step 6 — Cluster related findings

After Step 3-5, you have a flat list. Group findings that share a root cause:

- 5 findings about "no error handling" → cluster: "Error handling discipline missing"
- 7 findings about "PII in logs" → cluster: "Log sanitization missing"

Clusters surface in Section 5 of the output. Individual findings still listed in Section 4.

### Step 7 — Recommend priority order

Sort by: P0 first, then P1, then within each tier sort by *effort × impact*. Quick P1 wins (<1 day) come before slow P0s (>1 week) when there's a deadline.

In Section 6 of output, give a "Top 10 Punch List" — most impactful findings ordered for action.

### Step 8 — Fill the template

Open [assets/TECH_DEBT_AUDIT_template.md](assets/TECH_DEBT_AUDIT_template.md), fill every `{{PLACEHOLDER}}`. Write to `docs/01_DISCOVERY/TECH_DEBT_AUDIT.md`.

### Step 9 — Self-review

Run [references/checklist.md](references/checklist.md). Do not deliver until all gates pass.

## Quality bar

A good `TECH_DEBT_AUDIT.md` lets a tech lead answer in <15 minutes:
1. What's the worst thing in this codebase right now?
2. What 5 things should we fix this sprint?
3. What technical debt blocks the next major feature?
4. Are there any compliance violations we should disclose?
5. How big is the total debt (XS/S/M/L/XL counts)?

## Adaptation

See [references/adaptation.md](references/adaptation.md) for variations by project shape (frontend SPA debt vs backend API debt vs ML pipeline debt vs infra debt).

## Worked example

See [references/examples.md](references/examples.md) for an anonymized example: "Project Beacon", a B2B analytics dashboard with 38 findings.

## Failure modes to avoid

- **P0 inflation.** If everything is P0, nothing is. Reserve P0 for active or imminent failures.
- **Vague evidence.** "The codebase needs better error handling" — useless. "12 catch blocks in `src/api/` swallow errors silently (e.g., `src/api/users.ts:45`)" — actionable.
- **Mixing description with prescription.** This audit identifies what IS broken/risky. The fix design belongs to `tech-solution-design`.
- **Counting LOC as debt.** A 1000-line file is a SMELL, not automatically debt. Verify it's actually problematic.
- **Missing the boring categories.** MAINTAINABILITY (outdated deps) and COMPLIANCE (missing audit log) are easy to skip but often the highest ROI fixes.
- **Forcing all findings into Mode A.** If a project is genuinely organized differently (e.g., "platform" vs "product" engineering), respect that with Mode B/C — don't force fit.
