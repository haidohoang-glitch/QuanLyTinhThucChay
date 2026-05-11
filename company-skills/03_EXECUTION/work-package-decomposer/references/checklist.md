# Work Package Decomposer — Quality Checklist

Run before delivering task decomposition.

## Gate 1 — WP comprehension

- [ ] WP doc read in full (not skimmed)
- [ ] Acceptance criteria copied into decomposition output
- [ ] Files affected list confirmed against actual codebase (paths exist)
- [ ] Any ambiguity in WP flagged BEFORE decomposing (don't decompose ambiguity into tasks)

## Gate 2 — Task granularity

- [ ] 8-20 tasks total (less = under-decomposed; more = WP probably too big)
- [ ] Each task touches ≤2 files (else split)
- [ ] Each task is a single unit of execution (not "do X then Y then Z")
- [ ] Task IDs sequential and follow `WP-X.Y-T<N>` format

## Gate 3 — Tier classification

- [ ] Tier 1 tasks are mechanical (install, copy file, run command, format)
- [ ] Tier 2 tasks have clear spec; verification by diff review
- [ ] Tier 3 tasks involve architecture, multi-file coordination, debugging
- [ ] Human tasks reserved for approvals, decisions, ambiguity
- [ ] Tier distribution looks reasonable: ~50-70% Tier 1, ~20-30% Tier 2, ~5-15% Tier 3 + human

If 100% Tier 3: probably misclassified; review.
If 100% Tier 1: probably WP is too small or skill misjudged inference needs.

## Gate 4 — Tier 1 prompt rigor (CRITICAL)

For each Tier 1 task, the prompt must:

- [ ] Specify exact file path
- [ ] Specify exact change (new content, exact lines, exact commands)
- [ ] Be copy-pasteable into Simple AI without modification
- [ ] Include expected output format
- [ ] NOT require reading other files unless those file contents are inlined in prompt
- [ ] NOT require inference ("decide between A or B" — that's Tier 2+)

If a Tier 1 prompt has any of:
- "Improve X"
- "Refactor for clarity"
- "Decide whether to..."
- "Use best judgment"

→ It's not Tier 1. Reclassify or rewrite.

## Gate 5 — Verify commands

- [ ] Every task has a verify command (or human verify step explicitly defined)
- [ ] Verify commands are deterministic (run same command twice, get same result)
- [ ] Verify commands are runnable by operator without specialized setup
- [ ] Failure-mode of verify is observable (operator can tell pass vs fail in <30 seconds)

## Gate 6 — Sequencing

- [ ] Task dependencies explicit (T2 depends on T1 documented)
- [ ] Parallelizable tasks marked
- [ ] No task depends on later task (no cycles)
- [ ] Operator approval gates inserted before destructive or irreversible operations

## Gate 7 — Stop conditions

- [ ] Section "Failure / Stop Conditions" present
- [ ] At least 4 specific stop conditions defined
- [ ] Each stop condition has clear handling instruction (retry / escalate / abort)
- [ ] Scope drift detection: if diff includes files outside WP's "Files affected" list, AI stops

## Gate 8 — Cost estimate

- [ ] Per-tier task counts × estimated tokens × current rates → realistic cost estimate
- [ ] Compare to all-Tier-3 baseline; cost saving documented
- [ ] If Tier 1 tasks dominate, cost should be near-free (Gemini Flash free tier or local Gemma)

## Gate 9 — Tier 2/3 task specifications

For each Tier 2/3 task:

- [ ] Goal clear (what to accomplish)
- [ ] Context to provide explicit (which docs, which files)
- [ ] Constraints stated (modifiable files, forbidden files)
- [ ] Verification approach defined

## Gate 10 — Format

- [ ] Output filename: `WP-{{X.Y}}_tasks.md` OR section appended to WP in PHASE doc
- [ ] Task table columns consistent
- [ ] Tier symbols (🟢 🟡 🔴 👤) used consistently
- [ ] Effort estimates in minutes, summed at end

## Self-review prompt

Pick a random Tier 1 prompt. Mentally paste it into a Simple AI. Could the AI succeed without seeing the WP doc? If not, fix the prompt.

Pick a random Tier 2/3 task. Could the operator verify it produced correct output without running it through more tools? If not, sharpen the verification approach.

Re-read the cost estimate. If higher than 30% of all-Tier-3 baseline, decomposition isn't taking advantage of tier routing. Look for tasks misclassified as Tier 2/3 that could be Tier 1.
