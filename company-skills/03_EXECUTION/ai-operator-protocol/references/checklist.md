# AI Operator Protocol — Quality Checklist

Run before delivering AI_OPERATOR_GUIDE.md.

## Gate 1 — Hard rules

- [ ] At least 7 hard rules listed (the standard set)
- [ ] Each hard rule is binary (no "should" / "try to")
- [ ] Project-specific rules added per Section 4 (regulated industries; security-critical; multi-team)
- [ ] Each rule has rationale (why) and enforcement mechanism (how)

## Gate 2 — Workflow rigor

- [ ] 14 steps documented (or per Mode B/C)
- [ ] Each step assigns explicit actor (Operator / AI)
- [ ] Operator approval gates explicit (steps 5, 7, 9, 12, 13, 14)
- [ ] Loop step (8-9) bounded (not infinite)

## Gate 3 — Stop conditions

- [ ] Section 4 lists ≥6 specific stop conditions
- [ ] Each has clear handling instruction
- [ ] "AI commits without approval" listed as CRITICAL stop condition

## Gate 4 — Escalation paths

- [ ] Section 5 covers tier escalation, ambiguity, prod incident, scope drift, cost overrun
- [ ] Each escalation has First action + If still failing
- [ ] No "escalate to manager" without specifying manager

## Gate 5 — System prompts

- [ ] Section 6 includes prompts for Orchestrator + Executor minimum
- [ ] Each prompt includes: Role, Required reading, Hard rules, Stop conditions, Output format
- [ ] Prompts copy-pasteable (no `{{PLACEHOLDER}}` left except where operator fills)
- [ ] Prompts work with at least 2 AI vendors (avoid vendor-specific syntax unless mandated)

## Gate 6 — Progress tracking

- [ ] Section 7 PROGRESS_TRACKER template present
- [ ] Status values defined (Pending / Planning / In progress / etc.)
- [ ] Cost column included

## Gate 7 — Cost monitoring

- [ ] Section 8 has anomaly thresholds (>2x, >5x)
- [ ] Cost reduction signals listed (Tier 1 %, gate frequency)
- [ ] Aggregate per-phase tracking documented

## Gate 8 — Failure scenarios

- [ ] Section 9 has ≥5 failure scenarios with Detection + Recovery
- [ ] CRITICAL violations (commit without approval) include investigation step
- [ ] Recovery doesn't assume operator omniscience (gives concrete next steps)

## Gate 9 — Onboarding section

- [ ] Section 10 lets a new operator know how to start
- [ ] Estimated time to first solo WP given (~3-5 hours typical)

## Gate 10 — Retrospective

- [ ] Section 11 specifies post-phase retro process
- [ ] Updates to this guide tracked (quarterly + per-phase)

## Gate 11 — Mode discipline

- [ ] Mode A: standard 14-step + 7 hard rules
- [ ] Mode B: company AI governance cited; protocol aligns
- [ ] Mode C: user-defined; rationale documented

## Gate 12 — Format

- [ ] Output: `docs/03_EXECUTION/AI_OPERATOR_GUIDE.md`
- [ ] Sections numbered 1-12 (or per chosen mode)
- [ ] Tables for: hard rules, escalation paths, progress tracker, failure scenarios
- [ ] System prompts in code blocks (not narrative paragraphs)

## Self-review prompt

Imagine a new operator with 1 hour to read. Could they execute a WP confidently after reading? If they'd still need to ask 5 questions, sharpen.

Imagine a Tier 1 AI given the Executor system prompt. Would it know what NOT to do? If hard rules are in narrative not bullet points, sharpen.

Imagine a CRITICAL incident: AI committed without approval. Does the guide tell operator what to do, in what order? If it just says "investigate", sharpen.
