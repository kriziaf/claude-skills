# Project tier template — repo root `CLAUDE.md`

The target shape for a repo-level file. Everything here is specific to *this* codebase — things Claude can't infer or would infer wrong. Behavioral preferences belong up in Computer; single-module details belong down in a Folder file.

---

# What this project is
[One or two sentences: what it does, who it's for.]

# Stack
- [Framework, language, database, hosting — e.g. Next.js, TypeScript, Supabase, Vercel]

# Commands
- Run locally: [npm run dev]
- Test: [npm test]
- Build: [npm run build]

# Rules for this repo
- [Where things live: "API routes in app/api/", "components in components/"]
- [Conventions: naming, the styling system, how errors are handled]
- [The don'ts: "never commit .env.local", "don't touch the generated/ folder"]
- Secrets stay in env vars — never write a real key into any file.

# Gotchas
- [Anything Claude keeps getting wrong, or genuinely can't guess from the code]
