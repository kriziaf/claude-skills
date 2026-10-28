---
name: deep-research
description: Structured decision research for "Should I do X?" questions — launching a product, entering a market, pricing a service, choosing a tool or platform, starting a project or business. Produces a cited report covering market reality, competitive landscape, realistic pricing, and a mandatory steelmanned case AGAINST the decision. Use this whenever the user asks "should I...", "is it worth...", "does it make sense to...", weighs a launch/build/buy/pivot decision, or asks for market/competitor/pricing research to support a decision — even if they don't say "research" or "report."
---

# Deep Research: Decision Reports

Turn a "Should I [do the thing]?" question into an evidence-based decision report. The report is not a pep talk and not a hit piece — it is the research a skeptical, well-informed advisor would hand over before the user commits money or time.

## Core rules

1. **Every factual claim gets a citation.** Market sizes, competitor pricing, adoption stats, failure rates — all cited to a source. If a number can't be sourced, label it as an estimate and show the reasoning.
2. **The case AGAINST is mandatory and steelmanned.** Not a token "risks" bullet list. Write the strongest argument a smart critic would make for NOT doing it, using the same evidence quality as the rest of the report. If the research genuinely supports going ahead, the AGAINST section still gets full effort — the user needs to know what they're betting against.
3. **Pricing must be realistic, not aspirational.** Anchor to what comparable offerings actually charge today, not what the user hopes to charge. Include the low end.
4. **No verdict inflation.** End with a conditional read ("worth doing IF..."), not cheerleading. Name the conditions that would flip the answer.

## Workflow

### Step 1 — Pin down the decision

Before searching, restate the decision in one sentence: who is deciding, what the action is, and what success would look like. If any of these is genuinely ambiguous (e.g., "should I build a chatbot" — for whom? paid or free? side project or company?), ask ONE clarifying question. Otherwise state your assumptions inline and proceed.

### Step 2 — Research (5–10 searches, tiered sources)

Run searches across four tracks. Scale effort to stakes: a tool choice might need 5 searches; a business launch needs 8–10. Use web_fetch to read full articles when snippets are thin.

| Track | What to find | Example queries |
|---|---|---|
| Market | Size, growth/decline, demand signals, saturation | "[category] market size 2026", "[category] demand trends" |
| Competition | Who exists, positioning, what's failed | "[category] competitors", "[competitor] shut down / postmortem" |
| Pricing | Actual price points across the range, willingness to pay | "[category] pricing", "[competitor] plans cost" |
| Counter-evidence | Failure rates, critiques, churned users, structural headwinds | "why [category] fails", "[category] criticism", "[category] churn" |

**Source tiers** — prefer higher tiers; flag when a claim rests only on Tier 3:

- **Tier 1**: primary sources — company pricing pages, SEC filings, government/industry statistics, peer-reviewed work
- **Tier 2**: reputable trade press, analyst reports, established journalism
- **Tier 3**: blogs, forums, community posts — useful for sentiment and failure anecdotes, weak for numbers

Deliberately search for disconfirming evidence. If every result is positive, the search terms are the problem — add "problems", "failed", "overrated", "alternatives to".

### Step 3 — Write the report

Use this exact structure:

```
# Should you [decision]?

## Bottom line
2–4 sentences. Conditional verdict: "Worth doing if [conditions]; skip it if [conditions]."

## The market
Size, direction, demand evidence. Cited.

## The competition
Who's there, how they're positioned, gaps and graveyards. Cited.

## Realistic pricing
The actual range comparable offerings charge, where the user could
plausibly sit, and why. Include the low end. Cited.

## The strongest case AGAINST
Steelmanned. The best argument a smart skeptic would make, with evidence.
This section must be able to stand on its own.

## What would change the answer
2–4 concrete conditions or signals that would flip the verdict either way.

## Sources
Only if the client doesn't render citations inline; otherwise omit.
```

Write in prose, not bullet walls. Keep the whole report tight — roughly 600–1,000 words. Density over length; every sentence should carry a sourced fact or a judgment derived from one.

### Step 4 — Calibrate the close

Do not soften the AGAINST section to be nice, and do not manufacture doom to seem rigorous. If the evidence is mixed, say it's mixed and identify what research or small experiment would resolve it (e.g., "run a $200 ad test before building").

## What this skill is NOT for

- Pure factual lookups ("what does X cost?") — just answer.
- Emotional/personal decisions with no researchable market component ("should I text my ex") — respond conversationally.
- Legal or medical decisions — provide researched context but flag that this isn't professional advice.

## Example

**Input:** "Should I launch a paid newsletter about civic tech?"

**Behavior:** Restate (individual creator, paid subscription, civic tech niche). Search: newsletter market size/platform stats; comparable civic tech / policy newsletters and their pricing; paid newsletter conversion benchmarks; "paid newsletter failed" postmortems. Report: bottom line ("viable side income if you already have an engaged audience of 1k+; poor bet as a primary income from zero"); market (creator economy stats, niche saturation); competition (named newsletters, their prices, free substitutes); realistic pricing ($5–10/mo typical, cite comparable examples, note free-to-paid conversion rates of 5–10%); strongest case against (tiny addressable niche × low conversion = ceiling math, plus the free-content substitution problem, cited); what changes the answer (existing list size, institutional subscribers, sponsorship instead of subscriptions).
