---
name: landing-page
description: "Redesign or build a landing page hero: a color scheme derived from the user's brand color, a modern performant animation, and buttons that feel expensive — always presenting three distinct design directions for approval BEFORE building anything. Use this whenever the user asks to design, redesign, refresh, or build a landing page, hero section, splash page, or marketing page, mentions making their site look modern/premium/expensive, or asks for design directions or concepts for a web page. Trigger even if they don't say 'hero' — 'make my homepage pop' counts."
---

# Landing Page Hero

Redesign a landing page hero in two gated phases: **three named design directions first**, then **build only the one the user picks**. The gate is not ceremony — heroes are taste-driven, and building before alignment wastes a full build on a coin flip. Never skip to code, even if the user's brief seems clear; the brief describes what they want, the directions show them what it could be, and those are different things.

If a `frontend-design` skill is available in the environment, read it before the build phase — it carries the craft and anti-template guidance this skill assumes.

## Phase 0 — Intake

Collect before designing (from the conversation, an existing page URL/screenshot, or one round of questions — not an interrogation):

- **Brand color** — the one anchor. If the user has no color, ask what the product should feel like and propose one with reasoning.
- **Product + audience in one sentence** — a hero for a dev tool and a hero for a wellness brand should not look related.
- **The current hero, if one exists** — what's being kept (logo, headline, copy) vs. replaced.
- **Hard constraints** — framework, CMS, fonts they've licensed, things legal/brand won't allow.

## Phase 1 — Three directions (the gate)

Present exactly three directions as compact concept cards. Each must be a genuinely different bet — different mood, different animation concept, different typographic attitude — not the same design at three intensities. Push one direction somewhere the user didn't ask, one conservative-but-sharp, one in between; safe × 3 teaches the user nothing.

Per direction card:

- **Name** — evocative, two or three words ("Midnight Terminal", "Soft Gradient Editorial")
- **Mood in one sentence** — what a visitor feels in the first second
- **Color scheme** — how the brand color is deployed (dominant field vs. accent-only vs. duotone), the derived supporting palette, light or dark base
- **Animation concept** — the one motion idea, named and specific ("slow aurora gradient drifting behind the headline", "staggered word-by-word headline reveal on load")
- **Button treatment** — how the primary CTA earns "expensive" in this direction
- **Type attitude** — display choice and scale contrast

Render the three cards visually if the environment supports inline visuals or artifacts; otherwise as tight prose. Then stop and ask which direction to build (or which elements to cross-breed). **Do not build until the user picks.**

## Phase 2 — Build

Build the chosen direction as a single self-contained HTML file (CSS + JS inline) unless the user's stack dictates otherwise. All colors as CSS custom properties so the palette stays swappable.

### Deriving the scheme from one brand color

- Build a tonal ramp from the brand color (roughly 9 steps, near-white to near-black), keeping the hue consistent and adjusting lightness/saturation — never just adding white/black, which deadens the color.
- Tint the neutrals with the brand hue (2–5% saturation) instead of using pure grays; this is a large fraction of what reads as "designed".
- One accent at most, chosen deliberately (analogous for calm, complementary for punch), used sparingly — the CTA and one or two highlights.
- Ratio discipline: ~60% base, ~30% supporting, ~10% accent. Verify text contrast at WCAG AA (4.5:1 body, 3:1 large text) — premium never excuses illegible.

### What makes buttons feel expensive

Expensive is restraint plus tactility, not decoration:

- **Layered depth** — a 1px lighter inner top edge (inset highlight), a subtle vertical gradient (3–6% lightness range), and two stacked soft shadows (one tight, one diffuse) instead of a single hard drop shadow.
- **Precise geometry** — generous horizontal padding (roughly 2.5× vertical), a border radius consistent with the direction (sharp, soft, or pill — commit), optical alignment of any icon.
- **Micro-interaction** — hover: 150–250ms ease-out, slight lift (`translateY(-1px)`) and shadow growth; active: press down and shadow compression; a visible focus ring that matches the palette. Transitions on transform/box-shadow/color only.
- **Never**: default-blue, bouncy/elastic easing on CTAs, color-rotating gradients on the button itself, or hover states that move the button enough to dodge the cursor.

### Animation rules

One hero, one motion idea, executed well. Candidate menu: aurora/gradient-mesh drift, staggered headline reveal, slow parallax depth layers, particle or grain field, magnetic CTA, scroll-triggered section entrance. Whatever is chosen:

- Animate **transform and opacity only** — nothing that triggers layout or paint storms; target 60fps.
- Respect `prefers-reduced-motion: reduce` with a designed static fallback (the resting frame should look intentional, not broken).
- Entrance animations run once, under ~1.2s total, and never delay the headline being readable past ~400ms.
- Ambient loops must be slow and low-contrast enough to sit behind text without fighting it.

### Delivery

Ship the file, then summarize in a few sentences: the direction built, the palette tokens and where to change them, and what to check on mobile. Offer one refinement round framed as specifics ("dial the animation speed", "try the accent on the secondary button") rather than an open "any changes?".

## Conduct

- Three directions means three; not two, not five, and never zero because the brief "seemed clear enough".
- If the user says "just build something, skip the directions", compress Phase 1 to three two-line options in a single message and get a one-word pick — the gate shrinks; it doesn't vanish.
- Judge output against the direction card the user approved. If the build drifts from the card, that's a bug, not evolution.
