---
name: optimize
description: "Performance optimization with proof: profile a slow page, build, query, script, or endpoint, identify the real bottleneck with measured evidence, fix the biggest contributor first, and demonstrate the improvement with before/after numbers under identical conditions. Use this whenever the user says something is slow, laggy, or takes too long — 'my build takes forever', 'this page loads slowly', 'this query is killing us', 'speed this up', 'why is this so slow' — or asks to profile, benchmark, or optimize anything. Trigger even when they've already guessed a cause; the guess gets verified before anything is changed."
---

# Optimize

Fix slow things with evidence, in a strict loop: **measure → profile → fix the biggest contributor → re-measure → prove it.** The discipline that makes this work is refusing to touch code before profiling. "This is slow and I've never managed to fix it" almost always means previous attempts optimized a guess — often a correct-sounding one — while the real bottleneck sat untouched. The profile decides what gets fixed; intuition (the user's or yours) only decides where to point the profiler first.

## Step 1 — Baseline

Before reading a line of code, establish the number that defines "slow":

- **Pick one primary metric** appropriate to the thing: p50/p95 request latency, wall-clock build time, LCP for page load, query execution ms, script runtime. Improvement claims will be made against this metric only.
- **Measure it 3–5 times**, not once — record min/median/max. Run-to-run variance is the noise floor; an "improvement" smaller than the spread between runs is not an improvement.
- **Record conditions**: cold vs. warm cache, dataset size, hardware/environment, concurrency. After-numbers are only valid under the same conditions.
- If the slowness can't be reproduced in the working environment (production-only, user's machine), get the user's measurements and profiling output instead — never optimize a thing that was never measured. Getting the baseline is the step; skipping it is doing a different, worse task.

## Step 2 — Profile

Use the right instrument per domain, then **attribute time**: a ranked list of where it actually goes.

| Domain | Instruments | Usual suspects (verify, don't assume) |
|---|---|---|
| Web page | Lighthouse, DevTools Performance + Network waterfall, WebPageTest | Unoptimized images, render-blocking JS/CSS, oversized bundles, fonts, missing caching, request chains/waterfalls |
| Build | Tool timing flags — `webpack --profile`, `vite --debug`, `tsc --extendedDiagnostics`, `cargo build --timings`, Gradle `--profile`, `next build --profile` | No/broken cache, serial steps that could parallelize, type-checking in the hot path, barrel-file imports, monster dependencies |
| Database query | `EXPLAIN (ANALYZE, BUFFERS)`, slow-query log, ORM query logging | Missing index, N+1 from the app layer, `SELECT *` over wide tables, unbatched writes, lock contention, stale statistics |
| Script / backend code | Language profiler (`cProfile`/`py-spy`, Node `--prof`/clinic, `perf`), flame graphs | Hot loop doing repeated work, sync I/O in a loop, accidental O(n²), serialization overhead, chatty external calls |

Output of this step is a sentence of the form: **"X% of the total is [component], evidence: [profiler output]."** If no single contributor dominates (death by a thousand cuts), say so — the strategy changes from one big fix to batching the top handful.

Distinguish symptom from cause before moving on: "the query is slow" may be a missing index (query's fault), or an N+1 issue (the app calling a fine query 400 times). The profile of the layer above tells you which.

## Step 3 — Fix, one change at a time

- **Biggest contributor first.** Fixing something that's 4% of the total caps the win at 4% no matter how elegant the fix — spend effort where the time is. Don't polish the familiar small thing while the awkward big thing sits there; that's usually how the user got stuck for this long.
- **Smallest change that removes the bottleneck.** Prefer the cache flag, the index, the lazy import — not a rewrite. Rewrites are the last resort, proposed to the user before starting, never sprung on them.
- **One change → re-measure → then next.** Batched changes make it impossible to know what worked, and one of them usually didn't.
- **Show each change** briefly before or as it's applied: what it targets, expected effect, any behavior tradeoff (e.g., "this index speeds reads, adds ~small write cost").
- **Revert what doesn't move the number.** A change that adds complexity without measured improvement is negative value. Reverting is a finding, not a failure — record it so the user never re-tries it.
- Stop when the target is met or contributors flatten out — past that point every win costs more complexity than it returns. Say when that point is reached rather than grinding out 2% fixes.

## Step 4 — Prove it

Close with a proof table — same metric, same conditions, same number of runs as the baseline:

```
| Metric              | Before (median of 5) | After (median of 5) | Δ      |
|---------------------|----------------------|---------------------|--------|
| Build wall time     | 142s                 | 31s                 | −78%   |

Changes, in order applied:
1. Enabled persistent cache        142s → 96s
2. Moved type-check out of build   96s → 38s
3. Replaced barrel imports          38s → 31s
(Reverted: parallel plugin — no measurable change, added config complexity)
```

Report medians with the min–max spread, attribute the gain per change, and be honest about residuals: what's still slow, why it wasn't addressed (out of scope, needs infra, diminishing returns), and the single next thing to do if more speed is needed later.

## Conduct

- **Never present a projected improvement as a measured one.** If the after-number couldn't be measured (e.g., fix must deploy to prod first), label it an estimate, state the basis, and tell the user exactly how to measure it themselves.
- **Don't validate the user's guess by default.** "I've never managed to fix it" plus a stated suspicion means the suspicion is probably wrong — check it first, respectfully, with the profiler.
- **Watch the noise floor.** Warm caches, JIT warmup, and CDN state routinely fake 20% "improvements". When a result looks too good, re-run cold.
- **Performance work must not change behavior.** If tests exist, they pass after every change; if they don't, verify the output/response is identical before and after.
