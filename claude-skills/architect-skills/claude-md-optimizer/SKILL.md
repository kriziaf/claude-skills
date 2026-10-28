---
name: claude-md-optimizer
description: Audit and rewrite CLAUDE.md files at any tier — Computer (~/.claude/CLAUDE.md), Project (repo root), or Folder (subdirectory). Use this skill whenever the user asks to review, clean up, tighten, audit, fix, or rewrite a CLAUDE.md file, asks why Claude keeps ignoring or misreading their instructions, wants to set up a new CLAUDE.md, or mentions their Claude config/memory/standing orders feeling bloated, stale, or contradictory. Also trigger when the user shares a CLAUDE.md and asks "is this any good?"
---

# CLAUDE.md Optimizer

CLAUDE.md files are standing orders: Claude reads them before every prompt. Good ones quietly sharpen everything; bloated or contradictory ones quietly degrade everything. This skill audits a CLAUDE.md, then rewrites it — preserving intent, cutting noise, and relocating content to the tier where it belongs.

## The three tiers

Every CLAUDE.md belongs to exactly one tier, and each tier has a distinct job. Misplaced content is one of the most common and most damaging failures, because it either loads irrelevant context into every session (too high) or hides universal rules where they're rarely seen (too low).

| Tier | Location | Job | Belongs here |
|---|---|---|---|
| **Computer** | `~/.claude/CLAUDE.md` | How the user and Claude work together, everywhere | Communication style, verification habits, error-handling philosophy, universal tooling defaults |
| **Project** | repo root `CLAUDE.md` | How this codebase works | Build/test/run commands, architecture map, project conventions, deployment gotchas |
| **Folder** | subdirectory `CLAUDE.md` | What's true only inside this path | Module-specific patterns, local gotchas, "in this directory, always X" |

Tier templates live in `references/`: `computer-template.md`, `project-template.md`, `folder-template.md`. Read the template for the tier you're working on before auditing or rewriting — it defines the target shape and voice.

## Workflow

### 1. Identify the tier

Determine which tier the file belongs to from its path. If the user pasted content without a path, infer from content and confirm: "This reads like a Project-level file — is it your repo root CLAUDE.md?"

### 2. Audit

Read the file and, where you have filesystem access, cross-check it against reality: do referenced commands, paths, packages, and scripts actually exist? A confidently stated instruction pointing at a renamed script is worse than no instruction.

Classify every line into exactly one bucket:

- **KEEP** — specific, actionable, correct, at the right tier
- **TIGHTEN** — right idea, wrong form (vague, wordy, hedged, or narrative where it should be imperative)
- **RELOCATE** — good instruction, wrong tier (note the destination)
- **CUT** — one of the failure modes below
- **VERIFY** — can't confirm it's still true; never silently cut these — surface them for the human

Failure modes that earn a CUT:

- **Generic advice.** "Write clean code," "follow best practices" — Claude already does this; the line costs context and buys nothing.
- **Restating the obvious.** Anything Claude would do anyway, or that duplicates the README, package.json scripts, or lint config.
- **Stale instructions.** References to removed files, old workflows, deprecated tooling.
- **Contradictions.** Two lines that can't both be followed. Flag both; let the human pick the survivor.
- **Aspiration dressed as instruction.** "We value accessibility" tells Claude nothing to *do*. Convert to a concrete rule or cut.
- **One-off remnants.** Instructions from a single past incident that no longer generalize ("don't touch auth.js today").
- **Cross-tier duplication.** The same rule stated at two tiers. The tiers add together — they don't override each other — so a repeated rule buys nothing, and if the two copies drift apart, the contradiction gets resolved arbitrarily. Keep it at the highest tier where it's fully true; cut the other copy.

### 3. Report findings

Before rewriting, present a short findings summary: line counts per bucket, the top problems, and every VERIFY item as an explicit question. Keep it scannable — this is a code review, not an essay.

### 4. Rewrite

Produce the new version following the tier template's structure and these rules:

- **Imperative voice, one instruction per line.** "Run `pnpm test` before committing," not "It would be good to remember that tests should generally be run."
- **Every line must change Claude's behavior.** If deleting the line wouldn't change what Claude does, the line doesn't belong.
- **Explain the why when it's load-bearing.** "Never edit files in `generated/` — they're overwritten on build" survives context better than a bare prohibition.
- **Group by concern with short headers**, matching the tier template's sections.
- **Never repeat a rule across tiers.** The files stack; state each rule once, at the highest tier where it's fully true.
- **Preserve every genuinely load-bearing instruction.** When in doubt between cutting and keeping, keep it and flag it — the human is the editor of record.
- **Target size:** Computer ≤ 30 lines, Project ≤ 60 lines, Folder ≤ 20 lines. These are pressure, not law — but exceeding them requires a reason.

### 5. Review gate — never overwrite

The original file is never modified directly. Write the proposed version alongside it (e.g., `CLAUDE.proposed.md`) or present it in full, together with a changelog: what was kept, tightened, relocated, cut, and why — plus the open VERIFY questions. The human approves the swap; the skill's authority ends at the proposal.

## Generating from scratch

If no CLAUDE.md exists yet, skip the audit and run this sequence:

1. **Interview the repo first.** Commands from package.json/Makefile, structure from the tree, conventions from existing code and configs. Everything inferable gets inferred — the user's time is only for what the code can't tell you.
2. **Then interview the user: up to 8 questions, one at a time.** Ask about how they like to work, what Claude keeps getting wrong, how technical they are, and gaps the repo left open (preferences, gotchas, history). One at a time matters — batched questions get half-answers. Stop early when the remaining questions wouldn't change what you write.
3. **Write the proposed file(s)** through the same review gate as a rewrite. Leave `[bracketed placeholders]` only for choices the interview didn't settle; never invent the user's preferences. Only write a Folder file if a subdirectory genuinely has rules of its own — most projects need none.
4. **Report the negative space.** Alongside each proposed file, say what you deliberately left out and why ("didn't include a formatting section — Prettier already enforces it"). Omissions are decisions too, and the user can only veto the ones they can see.

## Example

**Input line (Project tier):** "We try to keep our code well tested and would appreciate it if tests could be run when it makes sense to do so."

**Audit:** TIGHTEN — right intent, hedged into uselessness.

**Rewrite:** "Run `pnpm test` before saying any task is done."
