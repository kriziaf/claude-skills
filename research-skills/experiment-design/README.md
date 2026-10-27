# A note on this skill

You'll notice there are almost no rules in this SKILL.md — nothing about quote fidelity, citation, or minimum evidence counts.

That's deliberate. I keep constant rules in a separate rules file rather than repeating them inside every skill, so my skills stay focused on method. Your setup and your standards are probably different from mine, so I'd rather leave that space for you to fill than impose my structure on you.

The skill runs fine as-is. If you want it to enforce your own evidence standards, add them — either to a rules file, or directly into SKILL.md.

If you want to go deeper on building skills, rules, and multi-step research workflows in Claude Code, that's what I teach: **https://maven.com/caitlin/claude-code-insights**

---

**Optional ensemble mode** is off by default. It sends your analysis to Gemini and GPT so you can see where three models independently agree on risk. It needs `GEMINI_API_KEY` (or `GOOGLE_API_KEY`) and `OPENAI_API_KEY` set in your environment. Nothing to install — `scripts/cross-model-risk.py` uses Python's built-in `urllib`.

Note that this sends your content to external APIs. The skill asks before dispatching. Don't run it on client or confidential material without thinking about that first.

The model IDs are pinned near the top of the script — currently `gpt-5.6-sol` and `gemini-3.7-flash`, both capable tiers rather than cheap ones, because the ensemble is only worth running if all three models can actually do the reasoning. Swap to `gpt-5.6-terra` or `gpt-5.6-luna` if you want to cut cost. They'll go stale eventually; update when you notice.
