---
name: ultracode
description: "Full-codebase sweep for dead code, inconsistencies, bugs, and out-of-date docs. Autonomously fixes what is provably safe (behavior-preserving, verified as it goes), and produces an escalation list of everything that needs the user's judgment. Use this whenever the user asks to sweep, clean up, audit, tidy, or 'go through' a whole codebase or project — 'find dead code', 'clean up this repo', 'what's broken or stale in here', 'fix the safe stuff and tell me about the rest' — or before a handoff, open-sourcing, or onboarding new contributors."
---

# Ultracode: Full-Codebase Sweep

Sweep an entire codebase in four passes — dead code, inconsistencies, bugs, doc drift — then split every finding across one boundary: **safe to fix autonomously** vs. **needs the user's call**. The boundary is the skill. Drawn too tight, the sweep is just a report the user has to execute themselves; drawn too loose, "cleanup" silently changes behavior — the worst outcome, because sweeps touch many files and a behavior change hidden in commit #40 of a cleanup is nearly undiscoverable.

**Safe means: behavior-preserving, low blast radius, and verifiable right now.** All three. Anything failing any one goes on the escalation list, however obvious the fix looks.

## Step 0 — Baseline before touching anything

- Map the repo: language(s), entry points, test command, build/typecheck command, linter/formatter config.
- **Run the tests and build first.** Record the result. A green baseline is the verification instrument for the whole sweep; a red baseline means (a) pre-existing failures get logged so they're never attributed to sweep changes, and (b) the safety boundary tightens — with no working tests, "verifiable" mostly means typecheck/build plus reference-proofs, so fewer things qualify as safe.
- If git is available, confirm the working tree is clean, and commit in small labeled batches as the sweep proceeds so everything is individually revertable.
- On large codebases, sweep module by module rather than shotgunning the whole tree; state the order.

## The four passes

### 1. Dead code

Unreferenced functions/classes/files, unused imports and variables, unreachable branches, commented-out code blocks, orphaned assets and config.

Deletion requires **proof of no references, including dynamic ones**. Grep for the bare name across the whole repo — not just import statements — because code is referenced through strings: route tables, DI containers, reflection, `getattr`/`globals()`, serializer field names, template files, CLI entry points in package manifests, config keys. Also check exports: anything re-exported from a package boundary or `__init__`/index file may be public API — dead *internally* is not dead. No proof, no deletion; escalate with the evidence gathered.

### 2. Inconsistencies

Mixed naming conventions, divergent patterns for the same job (three different HTTP-call styles), duplicated logic drifting out of sync, mixed formatting, inconsistent error handling.

Safe subset: formatting per the project's own config, and internal-only renames the IDE/compiler can verify. Everything structural — consolidating duplicated logic, standardizing on one of the three patterns — is a design decision: escalate with a recommendation. Convention questions get decided by the codebase's dominant existing pattern, never by external preference.

### 3. Bugs

Read for logic errors: off-by-ones, inverted conditions, unhandled error paths, resource leaks, `==`/`is` confusions, race-prone patterns, swallowed exceptions.

**Bug fixes change behavior by definition, so the default is escalate**, with the bug, the evidence, and the proposed fix written out. The narrow exception — fix-with-flag — requires all of: intent is unambiguous from the surrounding code, the fix is local, and a test (existing or newly written) proves the corrected behavior. Fixed bugs are still listed prominently in the report, never buried among typo fixes. Security-relevant findings go straight to the escalation list marked as such — and if a `security-review` skill is available, recommend running it rather than treating a sweep as a security audit. Likewise, performance findings note the `optimize` skill rather than turning the sweep into tuning.

### 4. Doc drift

READMEs describing commands that no longer exist, install steps that fail, docstrings contradicting signatures or behavior, comments that lie about the code below them, stale TODO/FIXMEs referencing closed work, changelogs and examples that no longer run.

Safe subset: corrections verifiable against the code right now — a flag rename, a moved file path, a parameter list. Where the *code* looks wrong rather than the doc (the docstring may describe intended behavior the code fails to deliver), that's a bug finding, not a doc fix: escalate. When it's genuinely ambiguous which side is right, escalate with both readings.

## Fix loop — verify as you go

Work in small same-category batches:

1. Apply the batch.
2. **Verify immediately**: tests + build/typecheck after every batch, not once at the end. For deletions, re-run the reference search post-deletion. A sweep that verifies only at the end can't tell which of 60 changes broke things.
3. Anything that fails verification gets reverted on the spot and moved to the escalation list with what happened.
4. Commit the batch (if git) with a message naming the category and files.

Momentum discipline: fixes must not ride together across the boundary — never slip a "while I'm here" behavior change into a safe batch.

## The report

End with a report (as `SWEEP-REPORT.md` in the repo, or inline for small sweeps):

```
# Sweep report — [repo], [date]

## Baseline
Tests: 142 passing (3 pre-existing failures, listed below — not from this sweep)

## Fixed (safe, verified)
| # | Category | Change | Verification |
|---|----------|--------|--------------|
| 1 | Dead code | Removed utils/legacy_export.py (0 refs incl. strings/templates) | grep proof + tests green |
| 2 | Docs | README install cmd updated to match package.json | ran the command |

## Fixed with flag (behavior-affecting — review these)
| # | What | Evidence | Test added |

## Needs your call
| # | Category | Finding | Why it needs judgment | Options / recommendation |
|---|----------|---------|----------------------|--------------------------|
| 1 | Inconsistency | 3 HTTP-client patterns across services/ | Consolidation is a design choice | Recommend axios wrapper in services/http.ts; ~14 call sites |

## Pre-existing issues (found, untouched)
```

Every escalation item must be decidable from the table alone — what, where, why it needs a human, and a concrete recommendation. An escalation list that just says "look at this" exports the sweep back to the user.

## Conduct

- **When in doubt, it's not safe.** The escalation list is a feature; a long one on a messy codebase is the correct output, not a failure to be helpful.
- **Never let the count of trivial fixes stand in for value.** Fixing 200 typos while stepping past a likely bug is a failed sweep — the report leads with what matters.
- **Respect suppressions and history.** A lint-ignore comment, a strange-looking workaround with a comment explaining it, or code guarded by "do not remove" gets escalated, not cleaned.
- **Scale honestly.** If the codebase is too large to sweep completely, say which modules were covered and which weren't — a partial sweep labeled as such beats a full sweep that skimmed.
