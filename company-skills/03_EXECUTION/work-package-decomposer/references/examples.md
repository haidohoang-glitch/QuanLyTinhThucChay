# Work Package Decomposer — Worked Example

Anonymized. Decomposing **WP-0.E (Error Boundaries)** — a typical Phase 0 WP.

## Context

**Imagined input:** "Decompose WP-0.E (Error Boundaries) for execution. WP says: Add React Error Boundary components in `src/components/`, integrate with Sentry, add `componentDidCatch` to top-level routes. Effort: S (4h). Files affected: 5 component files + 1 new ErrorBoundary.tsx + 1 test."

**Mode chosen:** Mode A (3-tier).

---

## Output excerpt

```markdown
# WP-0.E — Task Decomposition

> Source WP: docs/03_EXECUTION/work-packages/PHASE_0_PRE_FLIGHT.md Section WP-0.E
> Decomposition mode: A — 3-tier
> Author: Operator
> Date: 2026-09-12

## Context (from WP)

- Goal: Add React Error Boundaries to top-level routes; integrate Sentry capture
- Effort estimate: S (4h)
- Files affected: src/components/ErrorBoundary.tsx (new), src/App.tsx, src/components/Routes.tsx, src/main.tsx, tests/unit/components/ErrorBoundary.test.tsx (new)
- Acceptance: ErrorBoundary catches render errors; falls back to friendly UI; Sentry captures exception; test verifies fallback UI renders on thrown error

## Tier Distribution Summary

| Tier | Count | Estimated time |
|------|-------|----------------|
| 🟢 Tier 1 (Simple AI) | 9 | ~50min |
| 🟡 Tier 2 (Mid AI) | 2 | ~40min |
| 🔴 Tier 3 (Strong AI) | 0 | 0min |
| 👤 Human | 4 | ~25min |
| **Total tasks** | **15** | **~115min** |

(80% Tier 1 + Human; 20% Tier 2; 0% Tier 3 — appropriate for boilerplate-heavy UI WP.)

## Task Sequence

```
T1 ──> T2 ──> T3 ──> T4 ──> T5 (gate) ──> T6 ──> T7 ──> T8 (gate) ──> T9 ──> T10 ──> T11 ──> T12 (gate) ──> T13 ──> T14 ──> T15 (gate)
```

(Mostly sequential; T1 and T2 could parallelize but each is ~5min so not worth.)

## Task Table

| ID | Tier | Description | Prompt | Verify command | Expected output | Effort |
|----|------|-------------|--------|----------------|-----------------|--------|
| WP-0.E-T1 | 🟢 | Verify Sentry installed | `Run command: npm ls @sentry/react. Output the result.` | `npm ls @sentry/react` | `@sentry/react@7.x` shown | 3min |
| WP-0.E-T2 | 🟢 | Create ErrorBoundary.tsx with content | (full prompt below — see Detailed Tier 1 Prompts) | `cat src/components/ErrorBoundary.tsx \| head -10` | First 10 lines match prompt | 5min |
| WP-0.E-T3 | 🟢 | Create test file | (full prompt below) | `cat tests/unit/components/ErrorBoundary.test.tsx` | File matches | 5min |
| WP-0.E-T4 | 🟡 | Wrap routes with ErrorBoundary in src/App.tsx | (Mid AI: detailed inference task — see specifications below) | `git diff src/App.tsx` | Diff shows ErrorBoundary import + wraps `<Routes>` | 20min |
| WP-0.E-T5 | 👤 | Operator reviews diff for src/App.tsx | (Human task) `git diff src/App.tsx` | n/a | Operator approves | 5min |
| WP-0.E-T6 | 🟢 | Run unit test | `Run: npm run test -- ErrorBoundary. Output last 30 lines.` | (operator reviews) | All tests pass | 5min |
| WP-0.E-T7 | 🟢 | Run lint | `Run: npm run lint. Output last 10 lines.` | (operator reviews) | 0 errors | 3min |
| WP-0.E-T8 | 👤 | Operator approves intermediate state | (Human: review) | `git status; git diff` | Approved | 5min |
| WP-0.E-T9 | 🟡 | Add componentDidCatch hook to top-level Routes.tsx | (Mid AI specification below) | `git diff src/components/Routes.tsx` | Diff shows componentDidCatch added | 20min |
| WP-0.E-T10 | 🟢 | Run integration test (manual smoke) | `Run: npm run dev. Then in browser, navigate to /test-error-route. Output what you see.` | (operator views browser) | Fallback UI renders; not blank page | 5min |
| WP-0.E-T11 | 🟢 | Verify Sentry captured | `Open Sentry dashboard URL: https://sentry.io/<project>. Check Issues for last 10 minutes.` | n/a (operator verifies) | New issue with stack trace appears | 3min |
| WP-0.E-T12 | 👤 | Operator approves Sentry integration | (Human) | (visual check) | Approved | 5min |
| WP-0.E-T13 | 🟢 | Run full test suite | `Run: npm test. Output last 30 lines.` | (operator reviews) | All tests pass | 5min |
| WP-0.E-T14 | 🟢 | Stage + commit | `Run: git add -A && git commit -m "[WP-0.E] Add error boundaries with Sentry capture"` | `git log -1 --oneline` | Commit shown | 3min |
| WP-0.E-T15 | 👤 | Operator approves PR | (Human) Push branch + open PR via gh CLI | `gh pr view` | PR opened | 10min |

## Detailed Tier 1 Prompts

### T2 (🟢) — Create ErrorBoundary.tsx

```
Create file at path src/components/ErrorBoundary.tsx with EXACTLY this content:

```tsx
import { Component, ErrorInfo, ReactNode } from 'react';
import * as Sentry from '@sentry/react';

interface Props {
  children: ReactNode;
}

interface State {
  hasError: boolean;
}

export class ErrorBoundary extends Component<Props, State> {
  state: State = { hasError: false };

  static getDerivedStateFromError(): State {
    return { hasError: true };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo): void {
    Sentry.captureException(error, { extra: errorInfo as Record<string, unknown> });
  }

  render() {
    if (this.state.hasError) {
      return (
        <div role="alert" style={{ padding: 20 }}>
          <h2>Something went wrong</h2>
          <p>Please refresh the page or contact support if the problem persists.</p>
        </div>
      );
    }
    return this.props.children;
  }
}
```

Output the file path after creation.
```

**Verify after AI responds:** `cat src/components/ErrorBoundary.tsx | head -10`
**If verify fails:** Re-run prompt; if fails twice, escalate to Tier 2.

---

### T3 (🟢) — Create test file

```
Create file at path tests/unit/components/ErrorBoundary.test.tsx with EXACTLY this content:

```tsx
import { describe, it, expect, vi } from 'vitest';
import { render, screen } from '@testing-library/react';
import { ErrorBoundary } from '../../../src/components/ErrorBoundary';

const Throws = (): never => {
  throw new Error('test boundary error');
};

describe('ErrorBoundary', () => {
  it('renders fallback UI when child throws', () => {
    // Suppress console.error noise from React
    vi.spyOn(console, 'error').mockImplementation(() => {});
    render(
      <ErrorBoundary>
        <Throws />
      </ErrorBoundary>,
    );
    expect(screen.getByRole('alert')).toBeInTheDocument();
    expect(screen.getByText(/Something went wrong/i)).toBeInTheDocument();
  });

  it('renders children when no error thrown', () => {
    render(
      <ErrorBoundary>
        <div>Healthy</div>
      </ErrorBoundary>,
    );
    expect(screen.getByText('Healthy')).toBeInTheDocument();
  });
});
```

Output the file path after creation.
```

**Verify:** `cat tests/unit/components/ErrorBoundary.test.tsx | wc -l` → should be ~30 lines

---

## Tier 2/3 Task Specifications

### T4 (🟡) — Wrap routes with ErrorBoundary in src/App.tsx

**Goal:** Modify src/App.tsx so that the top-level `<Routes>` component (or whatever the routing entry is) is wrapped by `<ErrorBoundary>`.

**Context to provide AI:**
- Current src/App.tsx contents (paste in prompt)
- Note: ErrorBoundary is at src/components/ErrorBoundary.tsx (just created in T2)

**Constraints:**
- Files MAY be modified: src/App.tsx (only)
- Files MUST NOT be modified: any other file
- Acceptance: ErrorBoundary import added; <Routes> wrapped; no other changes

**Verification approach:**
- `git diff src/App.tsx` — diff should show: 1 import line added, 1 wrapping element added
- No deleted lines except those replaced by wrapped version

---

### T9 (🟡) — Add componentDidCatch in Routes.tsx (per-route level)

**Goal:** Add ErrorBoundary wrappers around each route in src/components/Routes.tsx so that error in one route doesn't break siblings.

**Context to provide AI:**
- Current src/components/Routes.tsx contents
- Pattern: wrap each <Route> child element with <ErrorBoundary> inline

**Constraints:**
- Files MAY be modified: src/components/Routes.tsx
- Acceptance: Each route's element wrapped; render still works

**Verification approach:**
- `git diff src/components/Routes.tsx` — diff shows wrappers added; routes still render
- `npm run dev` and visit a few routes; all render correctly

---

## Operator Approval Gates

- [x] Gate 1 (T5): After src/App.tsx modified — verify diff before continuing
- [x] Gate 2 (T8): After tests + lint pass — confirm intermediate state OK
- [x] Gate 3 (T12): After Sentry integration verified live — confirm before committing
- [x] Gate 4 (T15): Final approval before pushing PR

## Failure / Stop Conditions

1. T2 or T3 verify fails twice → escalate to Tier 2 with full WP context
2. T4 or T9 diff includes changes to files NOT listed in WP "Files affected" → STOP, scope drift
3. T6 or T13 tests fail → STOP, debug before proceeding
4. T11 Sentry doesn't capture event → may indicate Sentry config issue; investigate before commit
5. T15 PR creation fails (gh CLI error) → operator handles manually

## Cost Estimate

| Tier | Tasks | Avg tokens | Cost/1M | Total |
|------|-------|------------|---------|-------|
| 🟢 Tier 1 (Gemini Flash free) | 9 | ~1.5K each | $0 (free) | $0 |
| 🟡 Tier 2 (Claude Sonnet) | 2 | ~12K each | $3 in / $15 out | ~$0.10 |
| 🔴 Tier 3 | 0 | n/a | n/a | $0 |
| **Total** | | | | **~$0.10** |

Compare: All-Tier-3 baseline (Claude Opus, 15 tasks × 15K tokens): ~$3-5.

**Cost saving: ~97%.**

## Notes

- Mode A — 3-tier
- WP is well-bounded (5 files, clear acceptance); decomposition straightforward
- High Tier 1 percentage normal for UI scaffolding work
- Operator gate frequency higher than typical because Sentry integration touches production observability — extra caution warranted
```

---

## Calibration notes

- **80%+ Tier 1 + Human** is correct for this WP type (UI boilerplate). Don't push more to Tier 2 just because "real engineering should be Tier 2".
- **Tier 1 prompts include FULL file content.** Simple AI doesn't infer well from "create an ErrorBoundary component" — give exact code.
- **Tier 2 prompts give context, not exact code.** "Wrap top-level Routes" requires reading App.tsx; give it the file content + the goal.
- **Operator gates more frequent than per-task.** 4 gates for 15 tasks (~27%) — not after every task, but at meaningful checkpoints.
- **Cost: $0.10 vs ~$3-5 all-Tier-3.** This is the value of this skill.
- **Stop conditions specific.** "Diff includes changes outside WP files" catches scope drift early.
- **Verification for live integration (Sentry) is "operator checks dashboard".** Some verifications cannot be commands; document them clearly.
