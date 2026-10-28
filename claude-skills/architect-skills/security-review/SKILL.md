---
name: security-review
description: "Two-phase defensive security review of the user's own code: first a severity-ranked audit of vulnerabilities (injection, auth, secrets, crypto, input validation, dependencies), then a gated fix loop that presents each change for approval before applying it — highest severity first, one change at a time. Use this whenever the user asks for a security review, audit, or vulnerability check of their code or project, asks 'is this code secure', 'find security holes', 'harden this', or asks to fix security issues that were found. Also use before-launch checks like 'review this before I deploy'."
---

# Security Review

A two-phase workflow: **audit** the user's code for real vulnerabilities, then **fix them one at a time behind an approval gate** — highest severity first, every change shown before it is applied. The gate is the point: security fixes change behavior, and an unapproved "fix" that breaks auth is worse than the finding it patched.

This skill is for reviewing and hardening code the user owns or is authorized to assess. It reports flaws and remediations; it does not produce weaponized exploit code — a finding is demonstrated by pointing at the flawed line and explaining the attack mechanism, not by shipping a working payload.

## Phase 1 — Audit

### Scope first

Establish what's being reviewed: which files/directories, what the code does, and what it trusts (user input? network? file uploads? other services?). For a repo, map entry points before reading everything — routes, handlers, CLI args, file parsers, anything that touches external input. Trust boundaries are where the findings live.

### Scan by category

Work through each category systematically against the code — not from memory of what "usually" goes wrong, but by reading the actual code paths:

| Category | What to look for |
|---|---|
| Injection | SQL/NoSQL built by string concat, shell commands from user input, template injection, path traversal in file ops |
| AuthN / AuthZ | Missing auth checks on routes, IDOR (object access by ID without ownership check), privilege checks done client-side, session handling |
| Secrets | Hardcoded keys/tokens/passwords, secrets in logs, secrets committed in config or history |
| Input validation | Unvalidated input reaching sinks, mass assignment, unsafe deserialization, file upload without type/size limits |
| Crypto | Home-rolled crypto, weak algorithms (MD5/SHA1 for passwords, ECB), hardcoded IVs/salts, non-constant-time comparisons |
| Web-specific | XSS (unescaped output), CSRF, open redirects, CORS misconfig, missing security headers, SSRF |
| Dependencies | Known-vulnerable versions (check manifest against advisories if network access allows), unpinned deps, install scripts |
| Config & ops | Debug mode in prod paths, verbose error leakage, permissive file permissions, disabled TLS verification |

### Report findings

Present the audit as a findings table, then a short paragraph per finding. Severity definitions — apply them honestly, no inflation to seem thorough and no deflation to be polite:

- **Critical** — remotely exploitable now, leads to code execution, auth bypass, or bulk data exposure
- **High** — exploitable with modest preconditions; serious data or account impact
- **Medium** — real weakness needing specific circumstances, or defense-in-depth gap with plausible attack path
- **Low** — hygiene: hardening, headers, verbose errors, minor info leaks

Each finding: **ID, severity, file:line, the flaw, the attack mechanism (one or two sentences, conceptual), the fix in brief.** Only report what's actually there — if something is suspicious but unconfirmed (e.g., can't see the deployment config), list it separately as "needs verification" rather than padding the findings. A short review with three real findings beats a long one with ten speculative ones.

If the audit finds nothing significant, say so plainly and list what was checked — a clean result is a result, not a failure to try hard enough.

## Phase 2 — Gated fixes

**Never batch-apply.** The loop, per finding, in severity order (Critical → High → Medium → Low):

1. **Propose** — show the exact change as a before/after diff (or old/new code blocks), with one or two sentences: what it fixes, and any behavior change or side effect the user should know about (e.g., "requests without a valid token will now 401 — check that your cron job sends one").
2. **Wait** — get explicit approval before touching the file. "Show me each change before you make it" means the user's yes gates every write. If they say skip, mark it skipped in the tracker and move on; skipping is their call to make.
3. **Apply** — make exactly the approved change. No opportunistic refactoring, formatting sweeps, or bonus fixes riding along in the same edit.
4. **Verify** — re-read the changed code; run tests or the relevant code path if the environment allows. Confirm the fix and confirm nothing obvious broke.

If the user pre-authorizes ("just fix all of it, don't ask"), honor it for Medium/Low, but still pause to show Critical and High fixes before applying — those are the ones most likely to change behavior in ways the user needs to see. Say you're doing this and why.

### Track state

Maintain a running fix tracker in the conversation (or as `SECURITY-REVIEW.md` in the project if working in one):

```
| ID | Severity | Finding | Status |
|----|----------|---------|--------|
| F1 | Critical | SQL injection in /search | fixed |
| F2 | High     | JWT secret hardcoded    | approved, applying |
| F3 | Medium   | Missing CSRF token      | awaiting approval |
| F4 | Low      | Verbose stack traces    | skipped by user |
```

### Close out

When the queue is done: summarize what was fixed, what was skipped and the residual risk of each skip, anything marked "needs verification," and 2–3 prioritized next steps beyond code (rotate the exposed key, add dependency scanning to CI, pen test before launch). If a secret was found hardcoded, rotating it is always in the next steps — removing it from code does not un-leak it.

## Conduct

- **Severity order is not negotiable by default.** Don't fix the easy Lows first to build momentum while a Critical sits open. If the user reorders, follow their order and note the open Criticals at each step.
- **Explain attacks at the mechanism level.** "An attacker can pass `' OR 1=1 --` here because the query concatenates raw input" is right. A full working exploit chain against the user's production system is not the deliverable.
- **Findings must be tied to code the reviewer actually read.** Never report a category as clean if it wasn't checked — say what was and wasn't covered.
