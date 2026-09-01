---
type: Agent Training
status: active
tags: [02-organization]
---

# Appointment Setter Agent — Method Playbook

> Companion note: [[Appointment Setter Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I turn interested replies into booked meetings. I respond to interested leads, answer common questions (services, pricing range, fit, process), suggest meeting times (2–3 concrete options), handle scheduling, and prepare a meeting agenda framed to our services.

**Never:** book a meeting without confirming a concrete time; send a confirmation the CRM Manager hasn't been told about.

---

## 2. Core Workflow

### Phase A — Respond
1. Take interested replies from the Campaign Manager / inbox.
2. Reply with a helpful answer + 2–3 concrete meeting-time options.

### Phase B — Book
3. On agreement, book the slot, send confirmation, alert the CRM Manager (Meeting Booked).

### Phase C — Prepare
4. Draft a short agenda framed to our services (Google Workspace, M365, migrations, DNS, SPF/DKIM/DMARC, deliverability) for the Proposal Agent / Client Success.

---


## Web Access (Mandatory Standard)

Web access is required for live research/verification. Use this uniform chain (enforced company-wide):
- **Primary: the CRW crawler** (`crw_scrape` / `crw_map`) — independent of the Firecrawl/Nous paid-credit wall.
- **Fallback (CRW error/timeout/403/'Target unreachable'): the Jina Reader proxy** via shell redirection (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06).
- If both fail, mark the source **unverified** — never fabricate.


## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

Sources fetched live this pass:

1. https://calendly.com/blog/find-a-meeting-time — verified live via Jina on 2026-08-03
2. https://calendly.com/blog/meeting-polls — verified live via Jina on 2026-08-03
3. https://calendly.com/blog/is-calendly-rude — verified live via Jina on 2026-08-03

### Skill Improvements

**1. Kill the 7.3-email scheduling tax — lead with a link, not a question.**
Calendly's own study finds it takes an average of **7.3 emails to schedule a single meeting**. Every extra round trip is a chance for an interested reply to go cold. On the *first* reply to an interested lead, include a concrete booking path (2–3 specific times **plus** a scheduling link) so the lead can close the loop in one action instead of negotiating. Speed + single-step booking beats polite back-and-forth.

**2. "Open the door first" framing — offer their times before offering mine.**
Sending a bare scheduling link reads as making the prospect do the work ("here ya go"). The etiquette pattern that preserves rapport is reciprocity-first: invite their availability, *then* offer the link as the convenience option. Template:
> "Happy to work around you — send over a couple of times that suit, or grab whatever's easiest here: [link]."
This keeps the booking friction low without signalling that my calendar outranks theirs. Use it especially with senior/decision-maker replies.

**3. Poll, don't ping, for multi-stakeholder bookings; always render times in the lead's time zone.**
When a reply pulls in extra attendees (tech lead, finance, ops), stop proposing fixed slots — switch to a meeting poll so invitees vote on preferred times. Two attendance levers from the source material: (a) **show times in each invitee's local time zone** to boost attendance and prevent zone-math no-shows, and (b) keep the vote and the actual booking in the same tool so the poll ends in a confirmed calendar event, not another email thread.

**Applies to workflow:** Phase A (respond with times + link), Phase B (poll for multi-stakeholder; confirm in-tool), Phase C (attach agenda to the confirmed invite so the meeting has a stated purpose before it starts).

---

## 6. Sources

- https://calendly.com/blog/find-a-meeting-time — verified live via Jina on 2026-08-03
- https://calendly.com/blog/meeting-polls — verified live via Jina on 2026-08-03
- https://calendly.com/blog/is-calendly-rude — verified live via Jina on 2026-08-03


## Live Web Refresh (2026-08-05)

Live CRW crawl attempted on 2026-08-05. Result: no usable primary source bodies were retrieved. All six candidate URLs resolved to 404 or nav-only shells. Recording this honestly rather than inventing tactics.

- Gong - Discovery Call Tips - https://www.gong.io/blog/discovery-call-tips/ - returns OOPS PAGE NOT FOUND. Dead URL, do not cite (verified live via CRW on 2026-08-05)
- Close - Discovery Calls - https://blog.close.com/discovery-calls/ - body is literally Not Found; site chrome still renders, which is a false-positive trap (verified live via CRW on 2026-08-05)
- Cognism - Appointment Setting - https://www.cognism.com/blog/appointment-setting - nav rendered with 2026 branding so it looked live, but body says Whoops, we could not find the page. Confirms the site is live in 2026 while this article path is dead (verified live via CRW on 2026-08-05)
- HubSpot - Sales Discovery Call - https://blog.hubspot.com/sales/sales-discovery-call - returned only global nav and footer, zero article text. Current product lineup visible (Agent Hub, AEO Beta) confirms a 2026-era live fetch (verified live via CRW on 2026-08-05)
- Belkins - Appointment Setting - https://belkins.io/blog/appointment-setting - Sorry, this page is not available (verified live via CRW on 2026-08-05)
- Martal Group - Appointment Setting Statistics - https://martal.ca/appointment-setting-statistics/ - explicit 404 page not found; footer copyright 2009-2026 confirms live fetch (verified live via CRW on 2026-08-05)

### Skill improvements adopted

1. Never trust a scrape because the page renders. Six of six guessed URLs returned full site chrome (logos, nav, footers, even current 2026 branding) while the article body was a 404. Verification rule going forward: a source counts as real only when the crawl returns article body text - headline plus at least one substantive paragraph. Presence of a title, logo, or nav proves the domain is alive, not the page.
2. Stop guessing URL slugs. Guessing blog paths from memory had a zero percent hit rate this session and burned the entire fetch budget. Going forward: resolve URLs first via search or site map discovery, then scrape only confirmed links. Under a tight call budget, spend the first call on discovery, not on a hopeful direct fetch.
3. Report empty-handed rather than fill the gap. A refresh note that fabricates booking-rate tactics is worse than one that says the sources were dead, because downstream agents would treat invented numbers as researched fact.

Status: research objective NOT met this pass. Re-run with search-first URL discovery before scraping.

---

## Live Web Refresh (2026-08-31)

Live CRW crawl performed on 2026-08-31. Successfully retrieved and verified content from Cognism blog (2025/2026 articles) and HubSpot blog (2025/2026). All sources returned full article bodies with substantive content.

### Sources Verified Live (2026-08-31)

1. **Cognism - Best Time to Cold Call** (https://www.cognism.com/blog/best-time-to-cold-call) — Published 22 July 2025, updated 16 April 2026. Verified via CRW.
2. **Cognism - Cold Calling Scripts** (https://www.cognism.com/blog/cold-calling-scripts) — Published 24 June 2025, updated 9 April 2026. Verified via CRW.
3. **Cognism - Get Past the Gatekeeper** (https://www.cognism.com/blog/get-past-the-gatekeeper) — Published 29 September 2025, updated 16 April 2026. Verified via CRW.
4. **Cognism - Voicemail Scripts** (https://www.cognism.com/blog/voicemail-scripts) — Published 9 July 2025, updated 24 April 2026. Verified via CRW.
5. **Cognism - Objection Handling** (https://www.cognism.com/blog/objection-handling) — Published 30 September 2025, updated 16 April 2026. Verified via CRW.
6. **Cognism - How to Build Sales Cadence** (https://www.cognism.com/blog/how-to-build-cadences-that-convert) — Published 9 July 2025, updated 15 April 2026. Verified via CRW.
7. **HubSpot - BANT Lead Qualification** (https://blog.hubspot.com/sales/bant) — Published 31 July 2025, updated 2026. Verified via CRW.

### Skill Improvements Adopted (2026-08-31)

**1. Cold Calling Timing Precision**
- Best window confirmed: 10:00-11:00 AM local prospect time (highest average talk time). Secondary: 2:00-3:00 PM.
- Best day: Tuesday (highest meetings booked). Friday = best conversations, worst bookings. Monday = worst overall.
- Action: Schedule outbound blocks accordingly; respect time zones religiously.

**2. Structured 17-21 Day Multi-Channel Cadence (Cognism/Morgan J Ingram/Florin Tatulea)**
- 8-12 touchpoints across phone, email, LinkedIn, video.
- Day 1: Blank LinkedIn connection (no note = higher acceptance).
- Day 2: Email (75-100 words, ask for interest not meeting).
- Day 3: Call → VM (email in 5 min) → email (4 touches in 3 days).
- Days 5, 7: Calls only (no VM — gave response time).
- Days 7-10: Video only after engagement signal (open/click).
- Day 10: Persona-based personalized email.
- Day 13: Call.
- Day 15: Case study/social proof email.
- Day 18: Final call/VM (mention stopping outreach).
- Day 21: Breakup email asking for feedback (can reopen).
- Regional: US = more calls; APAC/EMEA = fewer touches; DACH = avoid triple-touch Day 1.

**3. Five Cold Calling Script Archetypes (Cognism 2026)**
- General (gatekeeper → "following up on email" → 30-sec value → 15-min demo ask)
- SaaS (casual open → relevance → discovery → demo)
- SaaS Demo (direct "3 minutes for [benefit]" → challenge → demo → case study if team buy-in needed)
- CEO (humble ask → specific time → pain resonance → demo → reframe "not interested")
- Enterprise (transparent "well-researched call" → peer proof → stakeholder mapping → calendar invite with CCs)

**4. Gatekeeper Mastery: 11 Strategies + 10 Scripts**
- Strategies: Mobile numbers (3x connect rate), research both parties, politeness, respect, don't pitch to GK, calm persistence, confidence (steady voice/warm tone), honesty/humor, first-name basis, empathy, off-hours calling.
- Scripts: Opinion ask, fake familiarity, honest helper, book time, polite direct, casual repeat, minimal info, pain alignment, email follow-up reference.

**5. Voicemail Optimization: 10 Types + iOS 26 Adaptation (2026)**
- Types: Pain-point, peer proof, name-drop, content feedback, confidence/familiarity, ultra-short (<20s), vague purpose, professional+peer, referral, urgency/deadline.
- Critical don'ts: No pitch, use name, <20 seconds, no "call when you can", warm tone, slow callback number, leave 3+ VMs (callback rate compounds).
- iOS 26 (2026) impact: Live voicemail transcription, silence unknown callers, caller ID emphasis, message filtering.
- Adaptation: Nail first 5 seconds with relevance (not name/company), multi-channel warm-up (LI/email before call), STIR/SHAKEN compliance + branded caller ID, signal-based prospecting (job changes, funding, stack changes), coach on messaging quality over quantity.

**6. Objection Handling: 5-Step Framework + Top 4 Objections**
- Framework: Listen (70/30) → Open-ended Qs → Solve urgent first → Confirm ("Happy with solution?") → Move on (never revisit).
- "No time": "30 seconds to explain. If relevant, calendar when ready. Fair?" → pause.
- "Not interested": "Typically Sales Directors struggle with X,Y,Z — on radar?" → pivot value prop.
- "Sales call?": "Not a sales call — seeing if interested in one. 30 sec, fair?" → reframe.
- "Using competitor": Don't badmouth. "Rate 1-10?" → if 8-9: "What makes it 10?" → "Married to it? What would you improve?" → dig for pains.

**7. Lead Qualification: BANT Modernized (HubSpot 2025/2026)**
- Budget: Spending patterns > dollar amount. "Invested in similar before? Process?" → Crunchbase funding signals.
- Authority: Buying committee early (champion, gatekeepers, influencers, end-users). "Anyone from [dept] weigh in?" → LinkedIn Sales Navigator.
- Need: Vitamins (nice) vs Aspirin (must). Cost of inaction: "What if unresolved 3-6 months? Impact on goals?" → Glassdoor/RepVue for pain intel.
- Timeline: Evaluation stages (exploring → comparing → ready). Timeframe: "Similar teams complete in 2-3 weeks. Realistic?" → Google Alerts for triggers.
- Application: Not every call. Earn right via insight/pain discovery first. ~10-15 of 50-60 daily calls warrant BANT.
- CRM tracking: Dropdown scorecard — Qualified / Partially known / Unknown-Unqualified.

**8. No-Show Reduction & Scheduling Optimization**
- Reciprocity-first booking: "Happy to work around you — send times or grab easiest here: [link]" (eliminates 7.3-email scheduling tax).
- Multi-stakeholder: Meeting polls (not fixed slots), show times in each invitee's local TZ, vote + booking in same tool.
- Attach agenda to confirmed invite (stated purpose before start).
- Reminder sequence: Email + SMS + calendar at 24h, 2h, 15min.
- Day-of confirmation with value reminder: "Looking forward to showing how [specific benefit] applies to [their context]."

**9. CRM Logging Standards**
- Log every activity: call (outcome, duration, recording), email (sent/opened/replied), LinkedIn (connection sent/accepted/message), voicemail left.
- Immediate stage updates: Connected, Qualified, Meeting Booked, Not Interested, Bad Timing.
- BANT fields in CRM with dropdown statuses.
- Tag: competitor mentions, objection types, trigger events.
- Auto-sync calendar events → CRM (meeting booked = stage update + attendee capture).

---

## Related

- [[02 - ORGANIZATION/Agents/Identity/Appointment Setter Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Appointment Setter Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/Interviews/Appointment Setter Agent - Interview 2026-08-10.md|02 - ORGANIZATION/Agents/Interviews/Appointment Setter Agent - Interview 2026-08-10.md]]
- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
- [[02 - ORGANIZATION/Agents/Training/Appointment Setter Agent - Training.md|02 - ORGANIZATION/Agents/Training/Appointment Setter Agent - Training.md]]
- [[02 - ORGANIZATION/Agents/Verification Logs/Appointment Setter Agent - Verification Log 2026-08-05.md|02 - ORGANIZATION/Agents/Verification Logs/Appointment Setter Agent - Verification Log 2026-08-05.md]]
- [[02 - ORGANIZATION/Memory Ledgers/appointment-setter-agent.md|02 - ORGANIZATION/Memory Ledgers/appointment-setter-agent.md]]
- [[09 - RESEARCH/B2B Appointment Setting Methodology - Appointment Setter Agent.md|09 - RESEARCH/B2B Appointment Setting Methodology - Appointment Setter Agent.md]]
- [[10 - TRAINING/Agent Training/appointment-setter-agent/Cycle 1 Plan.md|10 - TRAINING/Agent Training/appointment-setter-agent/Cycle 1 Plan.md]]
