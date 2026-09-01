---
type: Agent Training
status: active
tags: [02-organization]
---

# Email Copywriter Agent — Method Playbook

> Companion note: [[Email Copywriter Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I write the email copy that moves prospects through the pipeline: cold emails, follow-ups, welcome emails, meeting confirmations, re-engagement campaigns, and referral requests. Every message must be personalized, short, professional, value-first, and carry a clear CTA.

**Never:** send generic blast copy; write a CTA that isn't a single obvious next step; lead with features instead of the prospect's problem.

---

## 2. Core Workflow

### Phase A — Context
1. Take the personalized prospect context from the Personalization Agent (or raw lead + ICP).

### Phase B — Draft
2. Draft the right email type for the pipeline stage.
3. Apply the rules: personalized, short, professional, value-first, clear CTA.

### Phase C — Library & Handoff
4. Hand copy to the Campaign Manager (sequencing) and Deliverability Agent (send readiness).
5. Keep a copy library in the vault tagged by segment + variant for A/B testing.

---


## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

**Sources fetched this pass**
- https://www.saleshandy.com/blog/cold-email-statistics/ — verified live via CRW on 2026-08-03 (53M cold emails analyzed, Jan–Jun 2026)
- https://www.lemlist.com/blog/cold-email-templates — verified live via CRW on 2026-08-03
- https://blog.hubspot.com/sales/sales-email-templates-guaranteed-to-get-a-response — verified live via CRW on 2026-08-03

### Improvement 1 — Micro-segment instead of blasting (personalization at scale)
Campaigns under 200 prospects hit **15–20% reply rates vs 8%** for 500–1,000-prospect campaigns — roughly **2x**. The winners did not send less; they split the same volume into persona-specific sequences (VP Sales vs Sales Manager vs SDR Leader vs "recently funded"), each with its own pain framing. **New rule:** never write one email for a 1,000-name list. Request segment-level context from the Personalization Agent and produce one variant per persona/trigger, capped at ~200 prospects per sequence.

### Improvement 2 — One soft CTA, always (CTA design)
Emails with a **single soft CTA generated 78% more positive replies** than hard CTAs; multiple CTAs performed worst. Hard asks ("here's my calendar link", "book a two-minute test drive") are declining in 2026 because they demand commitment before trust. **New rule:** close with a reply-ask, not a commitment-ask — "Worth a quick chat?", "Does this resonate?", "Want me to send it over?" Reserve calendar links for after a positive reply. Never ship copy with two asks in it.

### Improvement 3 — Brevity + value-first structure, and treat follow-ups as the main event
First-touch emails should be **under 100 words**: one problem, one value prop, one CTA. Subject lines land best at **4–5 words (36–50 chars)**; avoid colons, quotes, ALL CAPS, and Re:/Fwd: prefixes (spam-flagged across major providers in 2026). Lead with the prospect's problem, not the product. Critically, **44% of all positive replies come from follow-ups** (first follow-up alone = 26%), so follow-ups get equal copy craft, not "just bumping this." Best sequences ran 4–6 follow-ups over ~20 days. Value-first framing (offer a list, cheat sheet, or benchmark before asking for time) and observation-based openers ("Noticed you [trigger]…") are the reply triggers, per lemlist's and HubSpot's template teardowns — HubSpot notes sub-150-word emails with specific company/role references outperform generic templates by ~35%.

---


## Web Access Standard

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall.
- **JINA FALLBACK IS MANDATORY, NOT OPTIONAL.** If CRW returns an error, times out, or is blocked (404 / 403 / "Target unreachable"), you MUST immediately retry the same URL via the **Jina Reader proxy** before recording the source as dead. Use **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06, re-verified 2026-08-08). Only mark a source "dead" after BOTH CRW and Jina return 404/blocked.
- **Process correction (2026-08-08):** During the email-writing deep research, 3 CRW 404s (Backlinko, GMass, Mailmodo) were logged as dead WITHOUT trying Jina first. This violated the fallback rule. Jina was later tested and confirmed those 3 are genuinely 404 on both CRW and Jina — but the *step* was wrong. Always: try CRW, then Jina, then conclude.

## 6. Sources

- https://www.saleshandy.com/blog/cold-email-statistics/ — verified live via CRW on 2026-08-03
- https://www.lemlist.com/blog/cold-email-templates — verified live via CRW on 2026-08-03
- https://blog.hubspot.com/sales/sales-email-templates-guaranteed-to-get-a-response — verified live via CRW on 2026-08-03

## Live Web Refresh (2026-08-08) — Deep Email-Writing Research

**Sources fetched this pass (live, via CRW):**
- HubSpot — *Sales Prospecting Email Templates* (2025): conversation-first framing, warm up socially before pitching, respect the relationship timeline, "feels like it came from a person, not a playbook."
- lemlist — *21+ Cold Email Templates* (2025): observation-based openers ("Noticed you [trigger]"), AIDA/PAS frameworks, real-result proof (named brands + numbers), single dead-easy CTA. Explicit warning: don't copy-paste, that's a fast track to spam.
- (Dead this pass, excluded: Backlinko /cold-email-study 404, GMass /blog/cold-email-statistics 404, Mailmodo /guides/personalized-email 404.)

**Synthesis → 3 added rules (now in [[Email Writing Standard]]):**
1. **Real personalization only.** Merge fields are a floor. Reference a specific, verifiable detail (observed trigger, role pain). Never fabricate a reference ("saw your post about X") — if none, use a honestly general but relevant line. Faked specifics destroy trust when wrong.
2. **No overstatement.** Cut superlatives ("leading", "best-in-class", "guaranteed"). Describe plainly; quantify only with a real basis. Calm confidence, not loud claims.
3. **Professional realism via restraint.** Sub-100-word first touch, one soft autonomy-preserving CTA, subject 6–10 words / <45 chars, no banned punctuation, human sign-off. Confidence reads as competence, not hype.

**Templates updated (2026-08-08):** all 4 in `company/Templates/Emails/` rewritten to the standard — observation/problem-led openers, no resume-leading, single soft CTA, no superlatives, tighter subjects.

## Live Web Refresh (2026-08-08, pass 2) — Reach / Write / Improve

**Sources fetched live (CRW; Hunter deep pages via Jina fallback per the mandatory rule):**
- Woodpecker — Cold Email Benchmarks: personalization nearly doubles reply rate vs none; advanced personalization lifts further; keep ICP updated; A/B test relentlessly, don't settle on one version.
- Close — 15 Cold Email Templates (2026): referral / introduction / authority-building / recent-event frames; "the best templates continue to evolve."
- CXL — Cold Emails (8-step process): ICP + relevance ("sell water not sand"); CAN-SPAM vs perceived-spam; research is the foundation.
- Hunter — Cold Email Guide + *State of Email Outreach 2026* (via Jina): value-prop canvas, WARM goals, tight segments (+158% reply at 21–50 vs 500+), custom-domain sender (+108% vs freemail), 3-message sequence (+106% vs 1), 2 custom attributes (+56% reply vs none), NO open tracking (+68% reply), manually edited (+18%), 69% of decision-makers resist synthetic-feeling copy, 1–2 contacts/company (+46% vs 3+), 20–49 sends/account/day (+27%).

**Synthesis → Email Writing Standard expanded to 3 parts (2026-08-08 pass 2):**
- **Part A — Reach:** real ICP first; tight segments (≤50) over blasts; 1–2 contacts/company; observation-based trigger openers; irresistible specific offer; send from company domain, paced volume.
- **Part B — Write:** (rules 1–8 unchanged) + new data points (2 attributes +56% reply, manual edit +18%, synthetic copy resisted).
- **Part C — Improve:** reply rate (not opens) as north star; no open-tracking (+68%); benchmark ~4.5% avg, 6–7%+ for tight/personalized/3-touch; A/B one variable; follow-up = new angle over 3 touches; close loop into vault library.

**Added to [[Email Writing Standard]] sources list**; Jina fallback discipline re-affirmed (Hunter deep pages fetched via Jina after CRW returned thin/JS content).


## Live Web Refresh (2026-08-05)

- 13 Powerful Cold Email Statistics You Should Know in 2025 (updated 2026-01-19) — https://instantly.ai/blog/cold-email-statistics/ — Current primary benchmark data: subject lines of 6-10 words hit ~21% open rate (double that of 21-25 word lines); ~45 characters is the mobile-safe ceiling; personalized subject lines get ~50% higher opens; questions +21%; specific numbers up to +113%. Cadence data: 4-7 touch sequences roughly triple response rates, one follow-up alone lifts reply odds ~25%, yet ~70% of reps stop after the first email. Timing: 1 PM weekdays best, Fridays/weekends worst, 8 PM-7 AM dead. A/B testing lifts opens ~49%. (verified live via CRW on 2026-08-05)
- 10 Examples for Cold Emailing & Why They Work — https://www.yesware.com/blog/cold-email/ — Verified live, but content is dated 2020/2022, so treated as structural reference only, not current benchmark. Useful for the persuasion-frame inventory: Before-After-Bridge, Problem-Agitate-Solve, But-You-Are-Free (autonomy-preserving close), Star-Chain-Hook, AIDA, Star-Story-Solution, 3-B Plan, Praise-Picture-Push, ACCA. Core principle restated well: the only job of each line is to earn the next line; the first sentence exists solely to get the second sentence read. (verified live via CRW on 2026-08-05)

Attempted and dead (404, recorded so I do not re-try them): https://www.lavender.ai/blog/cold-email-statistics and https://belkins.io/blog/cold-email-statistics.

### Skill improvements adopted

1. Subject-line hard constraints, not preferences. Every subject line I ship is now 6-10 words AND under ~45 characters, and must carry at least one of: a personalization token that is actually specific, a question, or a concrete odd number. No more generic value-prop subject lines. This is now a checklist gate before any draft leaves my hands.
2. Never deliver a single email again. Default deliverable becomes a 4-7 touch sequence with the follow-ups written up front, because that is where the tripling of reply rate lives and because most senders quit after one. Each follow-up must add a new angle rather than "just bumping this" — and I will pair the sequence with an explicit A/B variant of the opener, since split testing is the single cheapest documented lift available.
3. Close with autonomy. Adopting the "But You Are Free" frame from the formula inventory as my default CTA posture — explicitly granting the prospect the option to decline lowers resistance and reads as less desperate than an assumptive-close ask.

---

## 2026-08-08 — Humanizer training (anti-AI email voice)

**Instruction received:** CEO + Orchestrator directed me to make every client email sound like a real person at SevenMails wrote it, not an AI. The humanizer skill (`creative/humanizer`, blader/humanizer port, 34 patterns) is adopted as a MANDATORY pass on every draft.

**Adopted rule (now hard rule #4 in SOUL.md Operating Method):** every draft goes through the humanizer skill before handoff — load it, scan for the email-relevant patterns, rewrite, then run the skill's self-audit ("What makes the below so obviously AI generated?") and revise once more. Existing Email Writing Standard rules (personalized, short, value-first, one CTA) are unchanged; humanizer is an extra pass on voice only.

**Email anti-AI checklist (patterns to strip):**
- P20 Chatbot artifacts: "I hope this helps", "let me know if", "Certainly!" → cut
- P22 Sycophantic/servile tone → cut
- P14 Em-dash overuse (—) → commas/periods
- P7 AI vocab: crucial, key, highlight, underscore, valuable, vibrant, landscape → cut
- P8 Copula avoidance: "serves as", "boasts", "features" → is/are/has
- P23/24 Filler + hedging: "In order to", "It is important to note" → cut
- P33 Sentence-opener tics: "So...", "Look,", "Importantly," → cut
- P34 Reassurance kickers: "And that's okay" → cut
- P26 Hyphenated word pairs with perfect consistency (client-facing, end-to-end, data-driven) → use sparingly, vary
- P31/32 Dramatic fragmentation + rhetorical questions answered immediately → avoid in email
- P25 Generic positive conclusions → avoid

**Voice bar:** conversational but professional; varied sentence length; occasional first-person "I"; NO chatbot sign-offs; NO em-dash-as-style. Grounded, no hype.

**See also:** [[Email Copywriter - Humanizer Training 2026-08-08]] (training note with before/after).

## 2026-08-31 — Live Web Refresh (2025-2026 Full Research Refresh)

**Sources fetched live (via CRW + Jina fallback):**
- Saleshandy — *I Analyzed 53 Million Cold Emails* (2026-06-07): 53.1M emails Jan–Jun 2026, 67.4M connected accounts, Google Workspace 97% deliverability, micro-segment <200 = 15–20% reply rate (2x vs 500+), single soft CTA = 78% more positive replies, 44% positive replies from follow-ups, Tuesday 9–10 AM best window, SaaS highest reply rate
- lemlist — *21 Cold Email Templates* (2025): Observation-based openers, AIDA/PAS frameworks, real-result proof, single dead-easy CTA, warning against copy-paste, 30/30/50 rule (subject/deliverability/follow-ups)
- HubSpot — *Sales Prospecting Email Templates* (2025-10-27): Social-first, meaningful engagement, respect relationship timeline, quality over scale, warm up cold outreach, 82% buyers want journey-tailored outreach, Gong: sub-150 words + specific refs = 35% outperformance
- Close — *15 Best Cold Email Templates* (2024, updated 2026-07-14): Authentic referral, authority-building, recent-event, PAS competitor mention, no-ask outreach, 4 components (subject, CTA, follow-up plan, measurement), multi-channel = 37% better
- Hunter — *How to Write a Cold Email* + *Email Deliverability* + *Cold Email Subject Lines* (2026-03-04): 2+ custom attributes = +56% reply, manual edit = +18%, NO open tracking = +68% reply, custom domain +108% vs freemail, verified lists bounce 40% less, subject line personalization +7% opens, short subjects outperform
- Woodpecker — *Cold Email Benchmarks* (2020, structural reference): Personalization nearly doubles reply rate, advanced personalization lifts further, 2-3 follow-ups optimal, keep ICP updated, A/B test relentlessly
- Instantly — *13 Powerful Cold Email Statistics* (2026-01-19): 6-10 word subjects = 21% open rate, personalized subjects +50%, questions +21%, numbers +113%, 45 char mobile ceiling, 1 PM weekdays best, 4-7 follow-ups triple response, 70% stop after one email

**Synthesis → Key Rules Confirmed/Refined:**
1. **Micro-segment hard cap** — ≤200 prospects/sequence is now non-negotiable (2x reply rate proven at 53M scale)
2. **Single soft CTA** — 78% more positive replies; hard CTAs declining; autonomy-preserving frame mandatory
3. **Follow-ups = main event** — 44% of positive replies from follow-ups; 4-6 touches over 20 days; each = new angle
4. **No open tracking** — +68% reply rate (Hunter confirmed); reply rate is north star metric
5. **Real personalization only** — Merge fields floor; 2+ custom attributes +56%; manual edit +18%; NEVER fabricate references
6. **Custom domain + warm-up** — +108% reply vs freemail; ESP matching; 20-49 sends/day/account
7. **Humanizer pass** — Mandatory on every draft (34 AI-tell patterns); conversational professional voice
8. **A/B test one variable** — Sample size for significance; close loop into vault library tagged by segment+variant
9. **Multichannel default** — Email+Call 2.5x, Email+LinkedIn 1.9x; 99% still email-only = opportunity
10. **Compliance baked in** — Unsubscribe link mandatory (GDPR €20M/4% fines); CAN-SPAM/CASL/state laws

**Vault Updates:**
- All templates in `company/Templates/Emails/` already reflect observation/problem-led openers, no resume-leading, single soft CTA, no superlatives, tighter subjects (2026-08-08 pass)
- Added compliance reminders to template headers
- Humanizer checklist integrated into draft review step

---
