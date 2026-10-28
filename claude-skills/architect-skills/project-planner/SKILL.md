---
name: project-planner
description: Interview the user about a project, then produce a complete PLAN.md covering architecture/approach, milestones, risks, and step-by-step tasks written so a less capable model (Haiku-class or a Claude Code subagent) can execute each one with zero extra context. Use this skill whenever the user asks to "plan" a project, wants a PLAN.md, a roadmap, a project breakdown, milestones, a work breakdown structure, or asks to "break this down into tasks" — for any project type: software, writing, research, workshops, design systems, events.
---

# Project Planner

Turn a fuzzy project idea into a PLAN.md that a low-context executor can follow task by task. The plan is the product; the interview exists only to make the plan correct.

## Workflow

1. **Interview** — adaptively, only about genuine unknowns
2. **Draft the plan** — architecture/approach, milestones, risks, tasks
3. **Write PLAN.md** — to the working directory (or a path the user names)

## Phase 1: Interview (adaptive)

Ask only what is genuinely unclear AND would change the plan. Before asking anything, extract answers already present in the conversation, uploaded files, or memory. Then ask the remaining questions in **one batch** (max ~5 questions) — do not drip-feed across many turns. If the user's answer opens one critical follow-up, one more round is fine; two rounds is the ceiling unless the user invites more.

Things that usually matter and are worth asking if unknown:
- Definition of done — what does "finished" look like, concretely?
- Hard constraints: deadline, budget, required tools/stack, people involved
- What already exists (repo, draft, prior research) vs. greenfield
- Who consumes the output and where it lives

Things NOT to ask about: preferences you can default sensibly (naming, formatting), details that only matter mid-execution (capture as an open question in the plan instead), anything the user already said.

If the user says "just plan it," skip the interview entirely, state your assumptions in the plan's header, and proceed.

## Phase 2: Structure the plan

Use this skeleton. Adapt section *names* to the project type but keep the roles:

| Role | Software project | Non-code project (book, workshop, research) |
|---|---|---|
| How it's built | Architecture | Approach & Structure |
| Sequence of outcomes | Milestones | Milestones |
| What could go wrong | Risks | Risks |
| Executable steps | Tasks | Tasks |

**Architecture / Approach & Structure**: components and how they connect, key decisions with a one-line rationale each, and explicitly rejected alternatives (so an executor doesn't relitigate them). For non-code projects this is the outline, format, and method.

**Milestones**: 3–7 outcome-based checkpoints, each independently verifiable ("M2: user can log in end-to-end", not "M2: backend work"). Every task belongs to exactly one milestone.

**Risks**: table of risk / likelihood (L-M-H) / impact (L-M-H) / mitigation / early-warning sign. Include at least one non-obvious risk specific to this project, not just generic ones like "scope creep."

## Phase 3: Write tasks for a low-context executor

This is the heart of the skill. Assume the executor is a Haiku-class model or a fresh Claude Code subagent that sees **only the text of its one task** — not the conversation, not the other tasks, not the user's head.

Every task must contain:

- **ID and title**: `T3.2 — Write the lead-capture form validation` (milestone number.task number)
- **Context**: 1–3 sentences of project background needed for *this task only*. Repeat information rather than referencing other tasks ("as described in T2.1" is forbidden).
- **Inputs**: exact file paths, URLs, or artifacts the executor starts from
- **Steps**: numbered, imperative, one action each
- **Output**: the exact artifact to produce, with path and format
- **Done when**: an objectively checkable acceptance criterion (a command that passes, a file that exists with specific properties, a word count reached)

Rules of thumb:
- A task should be completable in one sitting (~30–90 min of model work). Split anything bigger.
- No task depends on judgment calls the plan hasn't already made. If a decision is genuinely open, put it in an "Open questions" section for the *user*, never inside a task.
- Name things literally: "create `src/components/HeroBlock.jsx`", not "create the component."
- Order tasks so each one's inputs exist by the time it runs; note the few true dependencies explicitly (`Depends on: T1.3`).

**Example task:**

```markdown
### T2.1 — Draft Chapter 3 outline
Context: This book covers socio-technical design in 8 chapters. Chapter 3
introduces the "Systems" pillar: how institutional incentives shape tool
design. Audience is civic technologists; tone is critical but practical.
Inputs: chapters/ch01-outline.md, chapters/ch02-outline.md (for voice
consistency), notes/systems-pillar-research.md
Steps:
1. Read all three input files.
2. Write a heading outline with 4–6 sections, each with a 2-sentence summary.
3. List 2–3 concrete case studies per section, drawn from the research notes.
Output: chapters/ch03-outline.md, 400–700 words, Markdown headings.
Done when: file exists, every section has ≥2 named case studies, and no
section duplicates a topic from ch01/ch02 outlines.
```

## PLAN.md template

ALWAYS use this exact structure:

```markdown
# [Project name] — Plan
> Generated [date]. Assumptions: [list any, or "none — confirmed in interview"]

## 1. Goal & definition of done
## 2. Architecture / Approach & Structure
## 3. Milestones
## 4. Risks
## 5. Tasks
### Milestone 1: [name]
[tasks...]
### Milestone 2: [name]
[tasks...]
## 6. Open questions for the owner
```

Write the file, then give the user a two-sentence summary and ask if any section needs a pass — do not paste the whole plan into chat.
