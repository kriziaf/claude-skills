---
name: chat-kb-conditions
description: Workflow for parsing health-related blog articles (MD Live/Evernorth) into structured data tables in Figma, organized by condition/topic. Each table includes a Chat KB Snippet column for chatbot knowledgebase use in the "ask conditions" intent flow.
---

## Chat Conditions KB — Content Parsing Workflow

### Purpose
Parse health-related blog articles from MD Live / Evernorth into structured data tables in Figma. Dual purpose:
- **A)** Design blog templates with article metadata and content structure
- **B)** Build a Knowledgebase for a chat "ask conditions" intent flow (via Chat KB Snippet column)

### Source Material
- PDF exports of MD Live by Evernorth blog articles
- Topics include: symptoms, conditions, wellness, prevention

### Output Format
All tables go inside the **"Blog Content — Conditions & Topics"** section (ID: `8158:25495`) on page `7690:93257` in file `2zlkFqlIO0LjVl4JnQL4oM`.

### Table Structure
Each condition/topic gets:
1. **Topic heading** (orange, Inter Bold 26, color `{r:0.85, g:0.45, b:0.1}`)
2. **Source subtitle** (gray, Inter Regular 13, color `{r:0.5, g:0.5, b:0.55}`)
3. **Data table** with 4 columns:
   - **Section** (300px) — content section name
   - **Content** (650px) — detailed content from the article
   - **Key Details** (550px) — summary of important points
   - **Chat KB Snippet** (1150px) — condensed, chatbot-ready response for the knowledgebase

### Table Styling
- Header row: light blue fill `{r:0.76, g:0.90, b:1.0}`, Inter Semi Bold 13
- Data rows: alternating white / light gray `{r:0.97, g:0.97, b:0.98}`
- Row borders: `{r:0.88, g:0.88, b:0.88}`
- Table border: `{r:0.85, g:0.85, b:0.85}`, corner radius 8
- Font: Inter family (Regular, Bold, Semi Bold, Medium)

### Per-Batch Overview Table
Each batch includes an Article Overview table with columns:
- Article Title (420px), Topic/Category (300px), Source (350px), Summary (700px), Key Sections (880px)

### Chat KB Snippet Guidelines
- Write as if answering a patient's question directly
- Keep concise but informative (2-4 sentences)
- Include actionable advice (when to seek care, home remedies)
- Avoid medical jargon where possible
- Include key differentiators (e.g., viral vs bacterial)

### Processing Steps
1. Read all PDFs in the batch
2. Inspect current section to find bottom edge (last child y + height)
3. Parse each article into structured rows by topic/section
4. Create tables using auto-layout frames (HORIZONTAL rows in VERTICAL container)
5. Add Article Overview table for the batch
6. Resize section to fit all new content

### Completed Batches
- **Batch 1** (5 articles): Back Pain, Sleep Disorders, Joint Pain/Nutrition, Fatigue, Cough/Respiratory
- **Batch 2** (5 articles): Allergies, Headache, Cold Sore, COVID-19, Cold & Flu
- **Batch 3** (5 articles): Sore Throat, Pink Eye, UTI, Rash, Gut Health

### Technical Notes
- `figma.createTable()` is NOT available — use auto-layout frames
- Load fonts before text operations: Inter Regular, Bold, Semi Bold, Medium
- Break large batches into multiple evaluate_script calls to stay within script size limits
- Section node ID may change between sessions — always verify by inspecting both known IDs
