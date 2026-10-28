---
name: page-write-brief
description: Generate a structured content brief for a brand or service — voice and tone guidelines, audience-specific messaging, card content pools (paragraph and bullet-list variants), and hero/CTA copy. Use before running page-builder to define what content goes into templates.
---

# Page Create Brief

Generate a structured content brief for a brand, service, or topic. The brief defines the voice, tone, messaging, and content pools that `page-builder` uses to populate template pages. Use this skill when starting a new project or switching brands/topics.

## When to Use

- Before running `page-builder` on a new brand or topic
- When the user wants to define or refine the copy direction for their templates
- When switching from one service vertical to another (e.g., pharmacy → virtual care)

## Inputs to Gather

Prompt the user with these questions (use `ask_user_question` for each, one at a time):

1. **Service / Brand** — "What brand or service is this content for?"
   - Options: "Online Pharmacy", "Virtual Care", "Other (I'll describe it)"

2. **Audience** — "Who is the target audience?"
   - Options: "Patients / Members", "Care Providers / Prescribers", "Other (I'll describe it)"

3. **Content length** — "How detailed should the copy be?"
   - Options: "Concise (short headlines + 1-sentence descriptions)", "Standard (headlines + 1–2 sentence descriptions)", "Detailed (headlines + full paragraph descriptions or bullet lists)"

4. **Key messaging** — Ask the user for their value proposition, tagline, or key messages. Example: "health care. board-certified doctors. licensed therapists. now. that's better."

5. **Services / features to highlight** — Ask what specific services, features, or differentiators to weave into the content. Example: "Find Providers using Marketplace, Virtual Care set up in minutes, Walk-ins welcome, fast hassle-free."

6. **Number of page themes** — How many distinct page themes to create content for (default: 5). Each theme gets its own hero, cards, metrics, and CTA variations.

## Voice & Tone Guidelines

All content generated must follow these rules:

- **Warm and professional** — empathetic but not clinical. Write like a trusted healthcare partner, not a medical textbook.
- **Action-oriented** — lead with what the user can do, not what the system does. "Transfer your prescriptions in minutes" not "Our system enables prescription transfers."
- **Specific over generic** — use concrete details (time estimates, step counts, feature names) instead of vague promises. "Under 60 seconds" not "quickly."
- **Parallel structure** — all cards in a set should follow the same grammatical pattern. If one heading starts with a verb, all should.
- **No jargon for patients** — plain language for patient-facing copy. Industry terms (NPI, DEA, EPCS, PDMP) are fine for prescriber/provider audiences.
- **Link labels are specific verbs** — "Start Delivery", "Transfer Now", "Track Orders" — never generic "Learn More" or "Click Here."

## Brief Structure

Generate the brief in this structure, organized by page theme:

### Per-Theme Brief

For each page theme (e.g., "Virtual Care Overview", "Urgent Care & Walk-ins", "Mental Health & Therapy"):

**Hero Content** (2 variants — one for `hero-inset` with 2 slots, one for `hero-float` with 4 slots):
- Heading: 4–8 words, bold and benefit-driven
- Subtext: 1–2 sentences reinforcing the value prop
- Primary button label: 2–4 words, main action
- Secondary button label: 2–4 words, alternative path

**Wayfinding Cards** (pool of 3–6 cards for `external-link-card`):
- Title: 2–5 words, specific service or feature name
- Description: 1–2 sentences, what the user gets
- Link label: specific action verb, 2–4 words

**Value Proposition Content** (for `expanded text` with-intro):
- Section heading: 3–6 words
- Intro paragraph: 1–2 sentences
- 3 detail cards: title + description each

**Supporting Features** (for `bullet-image` plus-bullet):
- Section heading: 3–6 words
- 3 bullet items: short phrases, 6–12 words each

**Service/Feature Cards** (pool of 4–6 cards for `overview-card` variants):
- Eyebrow: 1–3 words, category label
- Heading: 4–8 words
- Per card: title + description + link label

**Credibility Metrics** (for `highlight` metric):
- Section heading: 4–8 words
- 3 metrics: number (e.g., "2M+", "4.8★", "<10 min") + label (3–8 words)

**Benefits Highlight** (for `highlight` brand):
- Section heading: 4–8 words
- 3 items: title + description

**Promo Banner** (for `promo-banner-card`):
- Heading: 4–8 words, conversion-focused
- Description: 1–2 sentences
- Primary button label + secondary button label

**CTA Banner** (for `CTA-banner`):
- Heading: bold tagline or value statement (can use brand's key messaging)
- Subtext: 1 sentence calling user to action
- Primary + secondary button labels

**Article/Resource Cards** (pool of 3–6 for `external-link-card` large):
- Title: article headline, 6–10 words
- Description: 1–2 sentences teasing the article content
- Link label: "Read Article", "View Guide", etc.

### Card Content — Paragraph vs. Bullet-List Variants

For each card pool, generate both variants:

**Paragraph variant** — Title + 1–2 sentence body + link label
**Bullet-list variant** — Title + 4 short bullet items (6–10 words each)

Detect which variant to use by inspecting text node content: bullet lists have `\n`-separated items, often with `•` or `+` prefixes.

## Built-In Content Briefs

### Online Pharmacy

**For Patients / Members:**

Headline: "Your Prescriptions, Delivered"
Subtitle: "Getting your medications has never been easier. We deliver your prescriptions right to your door — safely, quickly, and on your schedule."

Card set (use as many as variant requires, pick from this pool):
1. Title: "Free Home Delivery" | Body: "Skip the pharmacy line. We deliver your prescriptions directly to your doorstep at no extra cost — with temperature-controlled packaging when needed." | Link: "Start Delivery"
2. Title: "Easy Prescription Transfers" | Body: "Transfer your existing prescriptions in minutes. Just share your pharmacy details and we'll handle the rest — no paperwork required." | Link: "Transfer Now"
3. Title: "Automatic Refill Reminders" | Body: "Never miss a dose. Set up auto-refills and we'll prepare your medications before you run out, so they arrive right on time." | Link: "Set Up Refills"
4. Title: "24/7 Pharmacist Support" | Body: "Have questions about your medication? Our licensed pharmacists are available around the clock to answer your questions and provide guidance." | Link: "Talk to a Pharmacist"
5. Title: "Real-Time Order Tracking" | Body: "Track your prescription from pharmacy to front door. Get notifications at every step so you always know when your medications will arrive." | Link: "Track Orders"
6. Title: "Insurance & Savings" | Body: "We work with your insurance to keep costs low. Plus, our savings program helps you find the best price on every prescription." | Link: "Check Savings"

Bullet-list variant (for cards with list items instead of body paragraphs):
1. "Free Home Delivery" — Delivered to your door at no cost / Temperature-controlled packaging / Discreet, secure packaging / Flexible delivery scheduling
2. "Easy Prescription Transfers" — Transfer from any pharmacy / No paperwork needed / Ready in as few as 24 hours / We contact your doctor for you
3. "Automatic Refill Reminders" — Set your refill schedule / Get reminders before you run out / Auto-ship on your timeline / Pause or skip anytime
4. "24/7 Pharmacist Support" — Licensed pharmacists on call / Chat, phone, or video options / Medication interaction checks / Personalized dosage guidance
5. "Real-Time Order Tracking" — Live order status updates / Delivery window notifications / Signature or no-signature options / Track multiple prescriptions
6. "Insurance & Savings" — Works with most insurance plans / Automatic copay calculation / Generic alternatives suggested / Savings card integration

**For Care Providers / Prescribers:**

Headline: "Get Started with E‑Prescribing"
Subtitle: "Start sending prescriptions electronically in just a few steps. Our platform connects you directly to the pharmacy — faster, safer, and fully compliant."

Card set:
1. Title: "Register Your Practice" | Body: "Create your prescriber account in minutes. Verify your NPI, DEA credentials, and state license to unlock full e‑prescribing capabilities." | Link: "Create Account"
2. Title: "Connect to Pharmacies" | Body: "Link to your patients' preferred pharmacies through our nationwide network. Search by name, location, or pharmacy ID — all EPCS‑certified." | Link: "Find Pharmacies"
3. Title: "Send Your First Script" | Body: "Prescribe from your EHR or our web portal. Select the medication, confirm the patient, and transmit — your first e‑prescription takes under 60 seconds." | Link: "Start Prescribing"
4. Title: "Manage Controlled Substances" | Body: "Complete EPCS identity proofing and set up two-factor authentication to prescribe Schedule II–V medications compliantly." | Link: "Set Up EPCS"
5. Title: "Monitor Prescription Activity" | Body: "Track prescription volume, fill rates, and turnaround times. Export audit-ready reports and view integrated PDMP results." | Link: "View Reports"
6. Title: "Get Onboarding Support" | Body: "Access video tutorials, schedule live training, or reach our clinical support team around the clock for help with any workflow." | Link: "Get Help"

Bullet-list variant:
1. "Account Setup" — Complete your prescriber profile / Verify NPI and DEA numbers / Set up two-factor authentication / Choose your default pharmacy
2. "Patient Enrollment" — Add patients individually or in bulk / Verify insurance and eligibility / Set medication history preferences / Enable refill authorization rules
3. "Prescribing Workflow" — Search the full drug formulary / Check real-time drug interactions / Select dosage, quantity, and refills / Transmit directly to pharmacy
4. "Controlled Substances" — Complete EPCS identity proofing / Set up biometric or token auth / Sign with two-factor credentials / Meet DEA EPCS compliance rules
5. "Reporting & Analytics" — Track prescription volume by month / Monitor fill rates and turnaround / Export data for audits and reviews / View PDMP integration results
6. "Support & Training" — Access on-demand video tutorials / Schedule a live onboarding session / Reach our clinical support team 24/7 / Download quick-reference guides

---

### Virtual Care

**For Patients / Members:**

Headline: "See a Doctor from Anywhere"
Subtitle: "Connect with board-certified providers from the comfort of home. No waiting rooms, no commute — just quality care when you need it."

Card set:
1. Title: "Book in Minutes" | Body: "Schedule a virtual visit in under two minutes. Choose your provider, pick a time that works, and get a confirmation instantly — no phone calls needed." | Link: "Book a Visit"
2. Title: "Talk to a Provider Now" | Body: "Skip the wait. Connect with an available provider for an on-demand video visit, typically within 15 minutes, day or night." | Link: "Start a Visit"
3. Title: "Prescriptions Sent Directly" | Body: "If your provider determines you need medication, your prescription is sent electronically to your preferred pharmacy — ready when you are." | Link: "Learn About Rx"
4. Title: "Secure Messaging" | Body: "Follow up with your care team between visits. Send messages, share photos, and get answers without scheduling another appointment." | Link: "Message Your Team"
5. Title: "Specialist Referrals" | Body: "Need to see a specialist? Your virtual provider can refer you directly and share your visit notes, so you don't have to repeat your story." | Link: "Find a Specialist"
6. Title: "Your Records in One Place" | Body: "Access visit summaries, lab results, and care plans from every virtual visit — all in one secure, easy-to-navigate dashboard." | Link: "View My Records"

Bullet-list variant:
1. "Book in Minutes" — Choose your preferred provider / Pick from available time slots / Get instant confirmation / Add your visit to calendar
2. "Talk to a Provider Now" — Average wait under 15 minutes / Available 24/7 including holidays / Video, phone, or chat options / No referral required
3. "Prescriptions Sent Directly" — E-prescribed to your pharmacy / Refills managed online / Generic options when available / Insurance applied automatically
4. "Secure Messaging" — Message your provider anytime / Share photos and documents / Get responses within 24 hours / Full conversation history saved
5. "Specialist Referrals" — In-network specialists prioritized / Visit notes shared automatically / Pre-authorization handled for you / Follow-up scheduling included
6. "Your Records in One Place" — Visit summaries after every call / Lab and test results integrated / Download or share with other providers / HIPAA-compliant and encrypted

**For Care Providers / Prescribers:**

Headline: "Launch Your Virtual Practice"
Subtitle: "Expand your reach and see patients remotely with a fully integrated telehealth platform — built for clinical workflows, not workarounds."

Card set:
1. Title: "Set Up Your Profile" | Body: "Build your virtual practice profile with your specialties, availability, and accepted insurance. Patients find you through our provider directory." | Link: "Create Profile"
2. Title: "Configure Your Schedule" | Body: "Set your virtual office hours, visit duration, and buffer times. Sync with your existing calendar so in-person and virtual visits never overlap." | Link: "Set Availability"
3. Title: "Conduct Video Visits" | Body: "Launch HIPAA-compliant video consultations directly from your dashboard. Built-in charting, e-prescribing, and order entry — no tab switching." | Link: "Start a Visit"
4. Title: "E-Prescribe from the Visit" | Body: "Prescribe during or after a virtual visit with integrated e-prescribing. Formulary checks, interaction alerts, and EPCS for controlled substances." | Link: "Prescribe Now"
5. Title: "Review Patient Intake" | Body: "Patients complete intake forms, consent, and symptom questionnaires before the visit — so you start each consultation with context, not paperwork." | Link: "View Intake"
6. Title: "Track Outcomes & Billing" | Body: "Access visit analytics, patient satisfaction scores, and auto-generated billing codes. Export reports for credentialing or quality reviews." | Link: "View Dashboard"

Bullet-list variant:
1. "Profile Setup" — Add specialties and credentials / Set accepted insurance plans / Upload photo and bio / Configure patient-facing profile
2. "Schedule Configuration" — Set recurring availability blocks / Sync with EHR or Google Calendar / Define visit types and durations / Enable on-demand visit queue
3. "Video Consultations" — HIPAA-compliant HD video / Built-in screen sharing / Record visits with consent / Waiting room with patient queue
4. "E-Prescribing" — Integrated drug formulary / Real-time interaction alerts / EPCS for Schedule II–V / Pharmacy network search
5. "Patient Intake" — Pre-visit questionnaires / Digital consent collection / Insurance verification / Symptom and history capture
6. "Outcomes & Billing" — Auto-generated CPT codes / Visit analytics dashboard / Patient satisfaction tracking / Export for credentialing

---

## How to Generate a New Brief

When the user picks "Other" or describes a new service:

1. Ask the user to describe the service in 1–2 sentences.
2. Generate a full brief following the exact structure above — hero, wayfinding cards, value prop, features, metrics, benefits, promo, CTA, and articles.
3. Create both paragraph and bullet-list variants for all card pools.
4. Generate content for each page theme, varying the focus (e.g., one page per specialty, one for onboarding, one for provider marketplace).
5. Follow the voice & tone guidelines strictly.
6. Present the brief to the user for review before handing off to `page-builder`.

## Output

Present the completed brief in a structured format the user can review. Once approved, the brief feeds directly into `page-builder` for text population.

## Rules

- Each card in a pool must have unique content — never duplicate copy
- All cards in a set follow the same grammatical pattern (parallel structure)
- Metric numbers should feel real and credible (e.g., "2M+", "4.8★", "<10 min", "95%")
- CTA headings can use the brand's key messaging verbatim
- If the user provides a tagline, weave it into at least one CTA-banner heading
- Generate enough card content to fill any component variant (pools of 6+ cards)
- Bullet-list items are 6–10 words each, 4 bullets per card
- Article titles are 6–10 words, teasers are 1–2 sentences
