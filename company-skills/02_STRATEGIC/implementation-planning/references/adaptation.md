# Implementation Planning — Adaptation

Variations by execution context. Read the section matching your situation.

> **Applies to Mode A only.** Mode B/C adapt principles to your taxonomy.

## Solo-developer plan

When one engineer executes the plan:

**Adjust:**
- Drop "parallelism factor" from Step 7; everything is sequential
- Reduce coordination overhead in WPs (no need for handoff docs)
- Increase buffer from 15-25% to 25-40% (no peer to catch mistakes)
- Smaller WPs; M and L are dangerous for solo (one bug derails a week)

**Add:**
- Self-review pause between phases (no peer review otherwise)
- Decision log: capture WHY decisions were made (no team memory to fall back on)

**Watch for:** Hero mode (skipping tests because "I know the code"). Tests are even more important when there's no peer reviewer.

## AI-agent-executed plan

When an AI agent executes WPs under human supervision:

**Adjust:**
- WP size: ALL WPs should be S or M (XS for trivial; L is too much for an AI session)
- Acceptance criteria: must be programmatically verifiable (run tests, check file contents)
- Files affected: must be explicit list, not "wherever needed"
- Reduce ambiguity to zero — AI agents don't ask clarifying questions well

**Add:**
- Per-WP system prompt template in `docs/03_EXECUTION/AI_OPERATOR_GUIDE.md`
- Validation steps the AI must perform after each file edit
- Stop conditions: when the AI must halt and request human input

**Watch for:**
- AI "improving" beyond scope — explicit guard rails in WP
- AI inventing test cases that pass trivially — TCs must be specified, not generated
- AI skipping rollback verification — checklist must include rollback dry-run

## Multi-team / multi-repo plan

When the plan spans repos or teams:

**Adjust:**
- WP IDs include team prefix or repo: `WP-2.A-payments` vs `WP-2.A-platform`
- Cross-repo dependencies become hard dependencies — track as such
- Verification gates may include "PR merged in repo X" not just internal CI

**Add:**
- Repo manifest section: which repos are touched per phase
- Coordination meetings or async checkins between teams
- Contract change tracking (API, schema, event format) — these often slip across team boundaries

## Regulated industry plan (HIPAA, PCI, GDPR-heavy)

**Adjust:**
- Phase 4 (Compliance) is non-skippable; do not collapse with cleanup
- Verification gates include compliance-specific criteria (audit log present, retention enforced)
- Add risk: regulator audit during plan execution; mitigation = plan in production-safe order

**Add:**
- Compliance review checkpoint between Phase 2 and Phase 3 (before traffic moves to new system)
- Documentation requirement per WP — regulators audit docs as well as code
- Sign-off list per phase: tech lead + security lead + legal/compliance

## Accelerated / MVP plan

When deadline is harder than scope:

**Adjust:**
- Drop Phase 1 (Quick Wins) if they don't ship value to launch
- Drop Phase 4 (Compliance) ONLY if regulator/contractual exposure is acceptable; document risk
- Increase WP sizing tolerance (more S, fewer XS) — don't over-decompose

**Add:**
- Explicit "tech debt to revisit" list: what's deferred and which phase will address it
- Launch criteria distinct from completion criteria: what's the MINIMUM to ship safely
- Day-after-launch plan: which Phase 4 work happens in the week post-launch

**Watch for:** Accidentally cut corners that should be P0 — re-validate `tech-debt-audit` findings against deferred list.

## Migration plan (replacing technology X with Y)

Special structure variant of Mode A:

**Phase 0:** Parallel infrastructure (Y deployed but unused)
**Phase 1:** Read-side parity (queries can answer from either X or Y)
**Phase 2:** Write-side dual-write (writes go to both X and Y)
**Phase 3:** Read flip (Y becomes primary read source)
**Phase 4:** Decommission X

This is the FinanceOS-style template that inspired Mode A. If your migration is similar, follow this exactly.

**Watch for:**
- Reconciliation strategy in Phase 2 — how do you know X and Y agree?
- Rollback after Phase 3 read flip — is X still warm enough to take traffic back?
- Cost optimization: dual-running both during Phase 2 is expensive; budget it explicitly

## Refactor plan (no behavior change)

When the plan is "improve internals, no user-visible change":

**Adjust:**
- Phase 1 may dominate (most refactors are accumulated quick wins)
- Acceptance criteria emphasize "behavior unchanged" via integration tests
- Drop Phase 2-3 if there's no migration; collapse to "before / after" structure

**Add:**
- Behavior-equivalence test suite — runs against old + new, must produce identical output
- Performance benchmark before / after each phase to catch regressions

## Rewrite plan (Greenfield replacement)

When the plan is "build a new system, retire old":

**Adjust:**
- Treat as TWO plans: "build new" (forward-leaning phases) + "retire old" (Phase 4 cleanup)
- Verification gate for cutover is far more important than for refactor
- Old system stays as primary until new system passes parity for N weeks

**Watch for:**
- Scope creep ("while rewriting, we should also add feature X") — rewrite already has high risk; resist
- "It's just like the old one but better" — verify with feature inventory; missing features become open issues

## Plans with significant unknowns

When inputs (TECH_SOLUTION_DESIGN, etc.) are partial or missing:

**Adjust:**
- Phase 0 includes "spike" WPs: time-boxed investigation that produces inputs
- Don't pretend to plan past what's known; include an explicit "Re-plan after Phase 0" step
- Confidence rating: LOW for any phase past first one

**Add:**
- Open Questions section is large; expect 5-10 OQs
- Plan revision schedule: "After Phase 0 complete, re-run `implementation-planning` skill to refine Phases 2-4"

This is honest planning — the alternative (pretending to plan when you can't) wastes time.

---

## Cross-cutting: AI operator guide alignment

If your plan is AI-executed, ensure WP structure aligns with `docs/03_EXECUTION/AI_OPERATOR_GUIDE.md` (if it exists in the project) or the company AI execution standard. WP fields may need to map directly to the operator's prompt template.
