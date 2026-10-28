---
name: page-builder
description: Build full-page website templates from pre-assembled frames of stacked component sections. Inspects each frame's component instances, applies content architecture best practices for section ordering, and populates all text slots with brief-driven copy. Use when frames already contain stacked component instances that need content.
---

# Page Builder

Build full-page website templates from frames that already contain stacked component section instances. This skill handles inspecting each frame's component structure, validating content architecture, and populating all text slots with brief-driven copy.

## When to Use

Use this skill when the user has pre-assembled frames on the canvas — each frame is a vertical stack of component section instances (hero, cards, banners, CTAs) — and wants to populate them with real content from a brief.

This is different from `build-template` which creates frames and instances from scratch. Page-builder works with **existing frame compositions**.

## Inputs to Gather

Before building, clarify or infer:
1. **Brief** — Brand name, services, value proposition, target audience, and key messaging. If a brief was used previously in the conversation, reuse it.
2. **Page themes** — Infer a theme for each frame based on its section composition (e.g., a frame heavy on mental health components → "Mental Health & Therapy" page).
3. **Content architecture validation** — Check section ordering against best practices (below) and note any deviations.

## Content Architecture Best Practices

These rules govern which component types belong where in a page flow:

### Opening (Top of Page)
- **Hero** (`.hero-secondary` variants: `hero-inset`, `hero-float`) — Always first. Sets the page identity.

### Wayfinding (Immediately After Hero)
- **External-link-card** (`small-card`, `medium-card`) — Navigation/wayfinding sits directly under the hero. Helps users self-select their path.
- May also follow an intro/extended text section or overview cards used for intro text.

### Supporting Content (After Wayfinding)
- **Expanded text** (`with-intro` variant) — Value proposition with intro paragraph + 3 detail cards. Use after wayfinding to explain the service.
- **Bullet-image** (`plus-bullet` variant) — Feature lists with `+` prefix bullets. Always comes after intro text.
- **Overview-card** (`stacked`, `2-col`, `6up` variants) — Service/feature cards with eyebrow + heading + cards. Good for detailed breakdowns.

### Credibility Break (Mid-Page)
- **Highlight** (`brand` variant) — Benefits messaging, breaks up white space. "Why choose us" content.
- **Highlight** (`metric` variant) — Credibility numbers/stats (e.g., "2M+ visits", "4.8★ rating", "<10 min wait"). Use for "why we are credible" messaging.

### Midway Conversion (Mid-to-Lower Page)
- **Promo-banner-card** (`brand` variant) — Call-to-action for account creation, login, or service promo. Drives conversion mid-page.

### Resources / Articles (Lower Page)
- **Heading Text** (`Center` variant) — Section header, typically introduces a resources/articles section below.
- **External-link-card** (`large-cards` variant) — Article cards, blog posts, news & insights. For B2B customers or health education content.

### Closing (Bottom of Page)
- **CTA-banner** — Bold closing call-to-action. Always last. Reinforces the value proposition with primary + secondary button.

## Component Text Slot Reference

### `.hero-secondary` (hero-inset variant) — 2 text slots
| Index | Role |
|-------|------|
| 0 | Heading |
| 1 | Subtext/description |

### `.hero-secondary` (hero-float variant) — 4 text slots
| Index | Role |
|-------|------|
| 0 | Heading |
| 1 | Subtext/description |
| 2 | Primary button label |
| 3 | Secondary button label |

### `external-link-card` (small-card) — 3 text slots
| Index | Role |
|-------|------|
| 0 | Card 1 link label |
| 1 | Card 2 link label |
| 2 | Card 3 link label |

### `external-link-card` (medium-card) — 9 text slots
| Index | Role |
|-------|------|
| 0 | Card 1 title |
| 1 | Card 1 description |
| 2 | Card 1 link label |
| 3 | Card 2 title |
| 4 | Card 2 description |
| 5 | Card 2 link label |
| 6 | Card 3 title |
| 7 | Card 3 description |
| 8 | Card 3 link label |

### `external-link-card` (large-cards) — 9 text slots
| Index | Role |
|-------|------|
| 0 | Card 1 title |
| 1 | Card 1 description |
| 2 | Card 1 link label |
| 3 | Card 2 title |
| 4 | Card 2 description |
| 5 | Card 2 link label |
| 6 | Card 3 title |
| 7 | Card 3 description |
| 8 | Card 3 link label |

### `expanded text` (with-intro) — 8 text slots
| Index | Role |
|-------|------|
| 0 | Section heading |
| 1 | Intro paragraph |
| 2 | Detail 1 title |
| 3 | Detail 1 description |
| 4 | Detail 2 title |
| 5 | Detail 2 description |
| 6 | Detail 3 title |
| 7 | Detail 3 description |

### `bullet-image` (plus-bullet) — 7 text slots
| Index | Role |
|-------|------|
| 0 | Section heading |
| 1 | `+` prefix (DO NOT MODIFY) |
| 2 | Bullet 1 text |
| 3 | `+` prefix (DO NOT MODIFY) |
| 4 | Bullet 2 text |
| 5 | `+` prefix (DO NOT MODIFY) |
| 6 | Bullet 3 text |

**IMPORTANT:** Indices 1, 3, 5 are the `+` prefix characters — never overwrite them. Only set content on indices 0, 2, 4, 6.

### `overview-card` (stacked) — 14 text slots
| Index | Role |
|-------|------|
| 0 | Eyebrow |
| 1 | Heading |
| 2 | Card 1 title |
| 3 | Card 1 description |
| 4 | Card 1 link label |
| 5 | Card 2 title |
| 6 | Card 2 description |
| 7 | Card 2 link label |
| 8 | Card 3 title |
| 9 | Card 3 description |
| 10 | Card 3 link label |
| 11 | Card 4 title |
| 12 | Card 4 description |
| 13 | Card 4 link label |

### `overview-card` (2-col) — 14 text slots
Same structure as stacked variant above.

### `overview-card` (6up) — 14 text slots
| Index | Role |
|-------|------|
| 0 | Eyebrow |
| 1 | Heading |
| 2 | Card 1 title |
| 3 | Card 1 description |
| 4 | Card 2 title |
| 5 | Card 2 description |
| 6 | Card 3 title |
| 7 | Card 3 description |
| 8 | Card 4 title |
| 9 | Card 4 description |
| 10 | Card 5 title |
| 11 | Card 5 description |
| 12 | Card 6 title |
| 13 | Card 6 description |

**Note:** 6up cards have NO link labels — only title + description per card.

### `highlight` (brand) — 7 text slots
| Index | Role |
|-------|------|
| 0 | Section heading |
| 1 | Item 1 title |
| 2 | Item 1 description |
| 3 | Item 2 title |
| 4 | Item 2 description |
| 5 | Item 3 title |
| 6 | Item 3 description |

### `highlight` (metric) — 7 text slots
| Index | Role |
|-------|------|
| 0 | Section heading |
| 1 | Metric 1 number (e.g., "2M+", "95%", "30 min") |
| 2 | Metric 1 label |
| 3 | Metric 2 number |
| 4 | Metric 2 label |
| 5 | Metric 3 number |
| 6 | Metric 3 label |

### `promo-banner-card` (brand) — 4 text slots
| Index | Role |
|-------|------|
| 0 | Heading |
| 1 | Description |
| 2 | Primary button label |
| 3 | Secondary button label |

### `Heading Text` (Center) — 2 text slots
| Index | Role |
|-------|------|
| 0 | Eyebrow |
| 1 | Heading |

### `CTA-banner` — 4 text slots
| Index | Role |
|-------|------|
| 0 | Heading (bold statement or tagline) |
| 1 | Subtext |
| 2 | Primary button label |
| 3 | Secondary button label |

### Composite sections (Heading Text + external-link-card large)
When a frame wraps a `Heading Text` instance and an `external-link-card` (large-cards) instance together, treat the combined frame as 11 text slots:
| Index | Role |
|-------|------|
| 0 | Eyebrow |
| 1 | Heading |
| 2–10 | Same as external-link-card large-cards (3 cards × title/desc/link) |

## Execution Steps

### Step 1 — Inspect all target frames

Use `evaluate_script` to inspect every target frame on the page. For each frame, collect:
- Frame ID, name, child count
- For each child: name, type, component name (if INSTANCE), variant properties, text node count
- Map each section to its component type from the reference above

```javascript
const frame = await figma.getNodeByIdAsync(frameId);
const children = frame.children;
for (let i = 0; i < children.length; i++) {
  const child = children[i];
  let componentName = null;
  let variantProps = null;
  if (child.type === 'INSTANCE') {
    const mainComp = await child.getMainComponentAsync();
    if (mainComp) {
      componentName = mainComp.parent?.type === 'COMPONENT_SET' 
        ? mainComp.parent.name : mainComp.name;
      try { variantProps = child.variantProperties; } catch(e) {}
    }
  }
  const textNodes = child.findAllWithCriteria({ types: ['TEXT'] });
  // Log: index, componentName, variantProps, textCount
}
```

### Step 2 — Theme each frame

Based on the section composition, assign a page theme:
- Heavy on therapy/counseling sections → "Mental Health & Therapy"
- Metrics + provider search + multiple overviews → "Find a Provider"
- Bullet-image + urgent care framing → "Urgent Care & Walk-ins"
- Expanded text + primary care focus → "Primary Care at Home"
- General overview with highlight + resources → "Virtual Care Overview"

Rename each frame: `"01 — [Theme Name]"`, `"02 — [Theme Name]"`, etc.

### Step 3 — Populate text slots

For each frame, use the text slot reference to populate content. Follow this pattern:

```javascript
const frame = await figma.getNodeByIdAsync(frameId);
frame.name = "01 — Theme Name";

// Load all fonts
const allTexts = frame.findAllWithCriteria({ types: ['TEXT'] });
const allFonts = allTexts.flatMap(t => 
  t.getStyledTextSegments(['fontName']).map(s => s.fontName)
);
const unique = []; const seen = new Set();
for (const f of allFonts) {
  const k = f.family + '|' + f.style;
  if (!seen.has(k)) { seen.add(k); unique.push(f); }
}
await Promise.all(unique.map(f => figma.loadFontAsync(f)));

const setText = (nodes, i, text) => { if (nodes[i]) nodes[i].characters = text; };
const children = frame.children;

// Per section: get text nodes, then set content by index
const s0 = children[0].findAllWithCriteria({ types: ['TEXT'] });
setText(s0, 0, "Heading text here");
setText(s0, 1, "Subtext here");
// ... continue for each section
```

### Step 4 — Verify

Screenshot each completed frame to visually verify text placement.

## Content Writing Rules

1. **Hero headings** — Bold, benefit-driven. 4–8 words. E.g., "Virtual Care, Reimagined" or "Urgent Care — Anytime, Anywhere"
2. **Hero subtexts** — 1–2 sentences reinforcing the value prop. Include key messaging from the brief.
3. **Card titles** — Specific service or feature names. 2–5 words. Action-oriented.
4. **Card descriptions** — 1–2 sentences. Lead with what the user gets, not what the system does.
5. **Link labels** — Specific action verbs. "Find a Provider", "Start a Visit" — never generic "Learn More".
6. **Metric numbers** — Use real-feeling stats: "2M+", "4.8★", "<10 min", "95%", "30 min", "500+". Always include a unit or symbol.
7. **Metric labels** — Short descriptor of what the number means. 3–8 words.
8. **CTA headings** — Bold tagline or value statement. Can use the brand's key messaging verbatim.
9. **CTA subtexts** — 1 sentence calling the user to action.
10. **Button labels** — 2–4 words. Primary = main action, Secondary = alternative/explore path.
11. **Bullet-image content** — Short phrases, not full sentences. 6–12 words each.

## Parallelization

Process 2 frames per `evaluate_script` call to stay within execution limits. For 5 frames, use 3 calls: frames 1+2, frames 3+4, frame 5 (with screenshots).

## Rules

- Always call `figma.setCurrentPageAsync(page)` before accessing nodes
- Always load fonts via `getStyledTextSegments(['fontName'])` before setting `.characters`
- Never modify styling — only replace text content
- Never overwrite `+` prefix characters in bullet-image components (indices 1, 3, 5)
- Each card in a set must have unique content — never duplicate copy
- Screenshot each frame after population to verify
- If a section has a composite frame (Heading Text + cards), use `findAllWithCriteria` on the composite frame, not individual children
- Content must be thematically consistent within each page — don't mix unrelated services
- Vary CTA messaging across pages — don't reuse the same CTA heading on every page
