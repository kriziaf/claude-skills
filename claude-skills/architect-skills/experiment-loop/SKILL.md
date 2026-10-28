---
name: experiment-loop
description: A hypothesis → prediction → review testing framework for content, products, features, or work output. Sets up and maintains experiment files in the current project so every piece shipped gets a falsifiable prediction before launch and a scored review after. Use this whenever the user wants to test whether their work is working — "did this post/feature/change perform?", "set up an experiment", "log a hypothesis", "review my experiments", "score this against what I predicted" — or mentions A/B thinking, validating content strategy, or measuring whether something they shipped had the effect they expected.
---

# Experiment Loop

A lightweight testing framework that forces three moves for every piece of work: state a **hypothesis** before shipping, commit to a **falsifiable prediction** with a confidence level, and **score the result against the prediction** at review time. The point is not bureaucracy — it is to stop retroactive storytelling ("that did well, I guess people liked the tone") and build a calibrated record of what actually works.

## File structure

All experiment state lives in the project as plain Markdown, so it survives across conversations and can be read, diffed, and edited by hand:

```
experiments/
├── LEDGER.md            # index of all experiments: id, title, status, score
├── RUBRIC.md            # the scoring scale (copied once at setup, then stable)
└── EXP-NNN-slug.md      # one file per experiment
```

Templates for all three files are in `assets/`. On first use, check whether `experiments/` exists in the project. If not, scaffold it from the templates and tell the user what was created. Never overwrite an existing LEDGER or experiment file — append and edit surgically.

## The three moves

### 1. Open an experiment (before or at ship time)

When the user has a new piece (a post, a feature, a workshop format, a pricing change — anything), create `experiments/EXP-NNN-slug.md` from `assets/experiment-template.md` with the next sequential ID. Fill it in *with* the user; push back until each field is sharp:

- **Hypothesis** — the causal belief being tested, with a "because". Weak: "this post will do well." Strong: "posts that lead with a failure story get more replies *because* the audience is tired of polished takes."
- **Prediction** — one falsifiable sentence with a number, a metric, a timeframe, and a stated confidence. Format: *"[Metric] will [reach/exceed/change by X] within [timeframe]. Confidence: NN%."* If the user can't name a metric, help them pick the closest observable proxy and record the proxy's weakness in the Notes field.
- **Measurement plan** — where the number will come from and when to check. A prediction that can't be checked in under five minutes at review time is a prediction that won't get checked.

Then add a row to LEDGER.md with status `open`. A hypothesis written after seeing results is not an experiment; if the user brings a piece that already shipped, mark the file `retrodiction: true` so the record stays honest.

### 2. Review and score (when the timeframe lapses)

When the user asks to review — or when you notice open experiments past their check date while working in the project — walk through each one:

1. Get the actual result (ask the user for the number, or compute it if data is in the project).
2. Score it 0–4 against the prediction using RUBRIC.md. Score against the *prediction as written*, not against how the user feels about the outcome.
3. Record a one-line **learning** — what this updates about the hypothesis — and a **next action** (double down / vary one element / kill).
4. Update the LEDGER row: status `scored`, plus the score.

The default scale (in `assets/rubric-template.md`):

| Score | Meaning |
|---|---|
| 4 | Prediction correct; effect met or beat the stated number |
| 3 | Directionally correct but under the number |
| 2 | Null / ambiguous — no clear effect either way |
| 1 | Directionally wrong |
| 0 | Opposite effect, or the result actively cost something |

The user can edit RUBRIC.md to their own scale; always read it rather than assuming the default.

### 3. Calibration retro (every ~10 scored experiments)

When the ledger accumulates roughly ten scored experiments, offer a retro. Read all scored files and report:

- **Hit rate by confidence band** — of predictions made at 80%+ confidence, what fraction scored 3–4? If far below the stated confidence, say so plainly: the user is overconfident, and by how much.
- **Patterns in what wins** — cluster hypotheses by theme and compare average scores.
- **Zombie hypotheses** — beliefs that keep scoring ≤2 but keep reappearing in new experiments. Name them for retirement.

Write the retro to `experiments/RETRO-YYYY-MM.md` so the record persists.

## Conduct rules

- **One variable per experiment where possible.** If the user changed the headline, the format, and the posting time at once, record all three and flag that the result won't isolate any of them.
- **No grade inflation.** A 2 is a 2. Null results are the framework working, not failing — say so, and log them with the same care as wins.
- **Predictions are frozen at open.** If the user wants to revise a prediction mid-flight, keep the original and add the revision with a date — never silently replace it.
- **Keep each session short.** Opening an experiment should take a few minutes of conversation, not a form-filling ceremony. If the user is on a roll shipping things, batch: open several thin experiments rather than one exhaustive one.

## Example

**User:** "I'm publishing the Trough of Disillusionment article Tuesday — set it up."

**Behavior:** Create `experiments/EXP-004-trough-article.md`. Hypothesis: "Civic tech readers engage more with hype-cycle skepticism than with tool coverage, because the audience is post-honeymoon on AI." Prediction: "The article will exceed my trailing-3-article average for shares by 25% within 14 days. Confidence: 65%." Measurement: platform analytics, check July 20. Ledger row added, status `open`. At review: actual = +8% over average → score 3 (directionally right, under the number). Learning: "Skepticism angle resonates but doesn't spike sharing; maybe it earns replies, not shares." Next action: "Repeat theme once, predict replies instead of shares."
