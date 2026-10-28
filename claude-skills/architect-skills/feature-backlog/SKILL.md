---
name: feature-backlog
description: "Deliver a feature that has stalled before: autopsy why past attempts died, produce a plan sliced to avoid those exact stall points, get the plan approved, then build end to end — flagging every uncertainty in an assumptions ledger instead of guessing. Use this whenever the user describes a feature they've never managed to ship or finish — 'I keep starting this and abandoning it', 'past attempts stalled', 'plan it first then build it', 'help me finally deliver X' — or asks to plan-then-build any non-trivial feature, especially with history attached."
---

# Feature Backlog: Deliver the Stalled Feature

Ship a feature with a history of failed attempts, in three phases: **autopsy the stalls → plan around them (gated on approval) → build end to end with a visible assumptions ledger.** A feature that has stalled repeatedly is not just an unbuilt feature — the stall history is data, and a plan that ignores it will die in the same place the last attempt did.

## Phase 1 — Intake and stall autopsy

Get three things (from the message, the project, or one round of questions):

1. **What the feature does** — as user-visible behavior with acceptance criteria ("done means: a user can ___ and sees ___"), not as an implementation sketch.
2. **Where past attempts stalled** — this is the load-bearing input. For each attempt: how far it got, and what was true when work stopped. If the user says "I don't know, I just stopped," probe once — the last thing they remember working on is usually the stall point.
3. **Constraints** — stack, existing code the feature must live inside, hard requirements.

Classify each stall into a cause, because the mitigation differs:

| Stall cause | Signature | Mitigation in the plan |
|---|---|---|
| Hidden unknown | "I got stuck on how to do X and drifted off" | Spike X first, before anything else is built |
| Scope spiral | "It kept growing / I kept redesigning" | Ruthless v1 cut list, protected by the plan |
| Horizontal trap | "I built the models/setup but never got to the actual thing" | Vertical slices — every milestone runs |
| Integration cliff | "It worked alone but wiring it in broke everything" | Integrate in milestone 1, thin, not at the end |
| Ambiguity swamp | "I was never sure what it should actually do" | Acceptance criteria pinned before code |

## Phase 2 — The plan (the gate)

Present the plan and **wait for approval before building.** Not a spec novel — one screen:

- **Acceptance criteria** — 3–6 checkable statements defining done.
- **v1 cut list** — what's explicitly out, by name. This list is protected: new ideas mid-build go to a backlog section at the bottom of the plan, not into the build. Scope spiral is the most common stall, and the cut list is its containment.
- **Milestones, vertically sliced** — each milestone ends with something that *runs and can be shown*, however thin. "M1: hardcoded happy path works end to end; M2: real data; M3: edge cases and errors" beats "M1: database layer" every time, because a horizontal plan can stall with 80% of the code written and 0% of the feature working.
- **The scary part goes first.** Whatever the autopsy identified as the killer — the unknown API, the tricky algorithm, the integration point — is milestone 1 or a pre-milestone spike. If the plan's riskiest item is scheduled last, the plan is wrong; that's how the previous attempts were sequenced.
- **Named risks** — each past stall point, restated, with the specific plan feature that neutralizes it.

Revise on feedback; build only on an explicit go.

## Phase 3 — Build end to end

Work milestone by milestone. At each boundary: run it, verify against the relevant acceptance criteria, and show a brief checkpoint (what works now, what's next). End-to-end means the acceptance criteria pass in the real context — integrated, runnable, with errors handled — not a scaffold plus a TODO list.

### The assumptions ledger — flag, don't guess

Silent guessing is how "built it wrong" happens; stopping for every trifle is how momentum dies. The protocol:

- **Blocking uncertainties — stop and ask.** Anything where a wrong guess poisons work built on top of it: data formats and schemas, API contracts, business rules ("what happens when the balance is negative?"), auth/permission behavior, anything irreversible (migrations, deletions, external side effects). Ask as a batched, concretely-optioned question — "A or B, I'd default to A because..." — not an open "what do you think?"
- **Non-blocking uncertainties — proceed on a stated assumption and log it.** Naming, copy, layout details, sensible defaults, internal structure. Each entry: the assumption, the choice made, and how to change it. The ledger is surfaced at every milestone checkpoint, not saved for a surprise ending.
- **Never launder a guess as a fact.** If the code embodies an assumption, the ledger says so. An empty ledger on a feature with a stall history is a red flag, not a clean bill.

### Delivery

Close with: what was built against each acceptance criterion (pass/fail, honestly — a criterion that isn't met is reported, not reworded), how to run it, the full assumptions ledger, the untouched v1 cut list as the natural v2 backlog, and — if anything in the build revealed a new risk for v2 — name it while it's fresh.

## Conduct

- **The plan gate is not skippable.** If the user says "skip the plan, just build," compress Phase 2 to five lines and get a one-word go — the gate shrinks, it doesn't vanish. They asked for the plan for a reason: this feature has died before.
- **Respect the cut list you wrote.** Mid-build "while I'm here" additions are the scope spiral wearing a helpful face.
- **A stalled milestone gets said out loud.** If milestone 2 hits an unexpected wall, that's a checkpoint conversation with options — not three hours of silent thrashing followed by a partial delivery. The user has watched this feature die quietly before; don't reenact it.
