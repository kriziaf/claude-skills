---
name: experiment-design
description: Turns a completed analysis into a validation plan — reads the findings, extracts the assumptions the analysis treated as true without proving them, rates the evidence behind each, ranks them by risk, and designs three targeted studies with falsifiable success and kill criteria. Use when an analysis is finished and someone is about to act on it, when asked what to test next or how to validate a finding, when a recommendation rests on thinner evidence than it appears, or as the validation-planning step after a research synthesis.
---

# Experiment design

## Purpose

Read a completed analysis, extract the assumptions embedded in its findings, assess which are under-evidenced, prioritise by risk, and generate a targeted validation plan for the riskiest ones.

**Not the same as assumption extraction.** That skill starts from a *decision* — a PRD, a strategy doc, a plan — and asks what the team is taking on faith. This one starts from a *finished analysis* and asks what the analysis itself is taking on faith, then designs the studies to close those gaps. If the input is a plan, use assumption extraction. If the input is research output, use this.

## Evidence standards

This skill does not restate general analysis rules — quote fidelity, citation, minimum evidence counts. Those are expected to come from a rules file or project configuration. See `README.md`.

## Inputs

The path to a completed analysis. If it was not supplied, ask:

> **Which analysis should I evaluate?** Drag the file in or type the path.

If you are running non-interactively and no path was given, list the analysis files you can see and stop rather than picking one.

## Workflow

```
- [ ] Step 1: Read the analysis
- [ ] Step 2: Extract embedded assumptions
- [ ] Step 3: Map evidence gaps
- [ ] Step 4: Prioritise risk
- [ ] Step 5: Optional ensemble pass
- [ ] Step 6: Design three studies
- [ ] Step 7: Save and present
```

### Step 1: Read the analysis

Read it in full. For every finding, claim, and conclusion, note the evidence cited (participant counts, quote sources, confidence ratings), the evidence type (behavioral or stated, spontaneous or prompted), and the confidence level the analysis assigned itself.

### Step 2: Extract embedded assumptions

For each finding, extract what is *not* directly evidenced — the beliefs the analysis treated as true without proving them. Look for:

- **Generalisation** — the analysis studied N people; does it claim the finding holds more broadly? What has to be true for that leap?
- **Causal** — it says X causes Y; is that demonstrated, or inferred from co-occurrence?
- **Segment** — it says a pattern holds for a segment; does it assume the segment boundary is the right cut?
- **Interpretation** — it reads a quote or behaviour a particular way; would another reading fit the same evidence?
- **Absence** — it concludes something is not a factor because it did not come up. Was it asked about? Could this sample have detected it?

Record each assumption as a testable claim, the finding it belongs to, and what changes about the recommendation if it turns out false.

### Step 3: Map evidence gaps

For each assumption: the direct evidence available (cite specifics), its quality (behavioral or stated, spontaneous or prompted, how many independent sources), and what data would be needed to test it that does not currently exist.

Count a data point as one participant, one survey row, or one distinct behavioral metric — not one mention.

| Rating | Criteria |
|---|---|
| 🟢 **Strong** | 3+ data points, 2+ source types, majority behavioral |
| 🟡 **Moderate** | 1–2 data points, OR 3+ from a single source type, OR mostly stated |
| 🔴 **Weak** | 1 data point, or evidence is indirect and inferential |
| ⚪ **Untested** | No evidence bears on this assumption either way |

Absence of contradicting evidence never counts as support — that is ⚪, not 🟢.

*Note: `⚫` is not used here. Across this toolkit it means "contradicted by evidence," which is a different state from "untested" and belongs to the assumption-extraction skill.*

### Step 4: Prioritise risk

For every assumption rated 🟡, 🔴, or ⚪, rate three dimensions **High / Medium / Low**:

- **Impact if wrong** — does the recommendation change fundamentally, partially, or not at all?
- **Reversibility** — High risk means hard to course-correct after acting. Low risk means easily undone.
- **Likelihood of being wrong** — given evidence quality and sample characteristics. **Label this as model inference, not evidence.**

Rank by the combination and surface the top 3–5. Report the three dimensions separately rather than collapsing them into one score.

### Step 5: Optional ensemble pass

Skip unless the user asks for it.

The ensemble runs Gemini and GPT over the same assumptions independently — not reviewing this analysis, but doing the task from scratch. Convergence across three models is the signal: an assumption all three rate critical is a stronger finding than one only Claude flagged.

**This sends the analysis content to external APIs. Confirm with the user before dispatching, every time.** Do not run it on confidential or client material without an explicit go.

Save the analysis content, extracted assumptions, and evidence gaps to a temporary markdown file, then:

```bash
python3 scripts/cross-model-risk.py [path-to-temp-file] --provider gemini
python3 scripts/cross-model-risk.py [path-to-temp-file] --provider openai
```

Requires `GEMINI_API_KEY` (or `GOOGLE_API_KEY`) and `OPENAI_API_KEY` in the environment. No packages to install — the script uses `urllib`.

Read both responses and build a convergence view: where all three agree on risk level, where they agree on study design, and where they diverge. Present divergent rationales in full and do not resolve them — that is the user's call.

### Step 6: Design three studies

One per assumption, for the top three.

- **Validates assumption** — which one
- **Why it's a priority** — one sentence on what changes if it's wrong
- **Method** — specific. Not "run a survey" but "5 unmoderated concept tests with [segment], asking [questions]"
- **Target participants** — who, how many, and why this sample closes the gap the current data leaves open
- **Key questions** — falsifiable. "Is it true that X?" not "What do users think about X?"
- **Success criteria** — what result supports the assumption and what result kills it, with thresholds set in advance
- **Effort** — time and resources
- **Decision gate** — if supported → action; if contradicted → action; if inconclusive → fallback

### Step 7: Save and present

Save to the analysis directory alongside the source, as `experiment-design-[YYYY-MM-DD].md`. Tell the user the path, then summarise: how many assumptions were extracted and how many are under-evidenced, the top risk and why, where the models converged if ensemble ran, and the three studies.

## Output format

```markdown
# Experiment design: [analysis name]

## Summary
[3-4 sentences: findings reviewed, assumptions extracted, under-evidenced count, top risk]

## Assumptions extracted

| # | Assumption | Source finding | Evidence available | Evidence quality | What's missing | Rating |
|---|---|---|---|---|---|---|

## Risk prioritisation

For each, ranked:
- **Assumption**: [statement]
- **Impact if wrong**: [what changes]
- **Reversibility**: [High / Medium / Low risk]
- **Likelihood of being wrong**: [assessment] *(model inference, not evidence)*

## Ensemble convergence [only if run]

| Assumption | Claude | Gemini | GPT | Convergence | Key differences |
|---|---|---|---|---|---|

## Validation plan

### Study 1: [name]
- **Validates assumption**: #[N] — [statement]
- **Why this is a priority**: [one sentence]
- **Method**: [specific]
- **Target**: [who, how many, why this sample]
- **Key questions**: [falsifiable]
- **Success criteria**: [supports if…] / [kills it if…]
- **Effort**: [time, resources]
- **Decision gate**: If supported → […]. If contradicted → […]. If inconclusive → […].

### Study 2 / Study 3
[same structure]

## What this plan does not cover
[Assumptions not prioritised, and why — deliberate prioritisation, not oversight]
```

## Quality check

- [ ] Every finding in the source analysis was reviewed for embedded assumptions
- [ ] Evidence gaps name specific missing data, never "more research needed"
- [ ] Risk used impact + reversibility + likelihood separately, not a single feel-based score
- [ ] Likelihood judgments are labelled as model inference
- [ ] No more than 3–5 studies — more means prioritisation has not happened
- [ ] Every study has falsifiable success *and* kill criteria with thresholds set in advance
- [ ] If ensemble ran: the user approved the external dispatch, convergence is highlighted, and divergences are presented unresolved
- [ ] A PM could hand this to their team and start executing within a day
- [ ] Whatever evidence standards apply in this project have been met
