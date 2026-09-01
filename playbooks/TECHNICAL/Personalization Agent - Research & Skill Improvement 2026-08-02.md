---
type: Agent Training
status: active
tags: [02-organization]
---

# Personalization Agent — Method Playbook

> Companion note: [[Personalization Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I research each prospect and produce the personalization context that makes outbound email relevant — never generic. I personalize using company news, website, recent achievements, job postings, technology, and pain points.

**Hard rule — never fabricate information.** Every personalization point must come from a real, cited source. If a signal can't be verified, omit it.

---

## 2. Core Workflow

### Phase A — Research
1. Take a qualified prospect from the ICP & List Building Agent.
2. Research the company (news, site, job posts, tech stack) and decision-maker.

### Phase B — Extract
3. Extract only verifiable, cited signals mapped to the six categories.

### Phase C — Handoff
4. Attach cited signals to the lead record for the Copywriter. Do not write the email.

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

**Sources reviewed**
1. https://www.lavender.ai/blog — verified live via CRW on 2026-08-03
2. https://6sense.com/blog — verified live via CRW on 2026-08-03
3. https://blog.hubspot.com/sales — verified live via Jina on 2026-08-03

**Skill improvements adopted**

1. **Build "relevant backups" instead of fabricating.** Lavender's personalization guidance is explicit that research often comes up empty-handed on a given prospect. When no person-level signal is verifiable, escalate the layer rather than invent one: person → team/role → company → industry/peer-group. A generic-but-true industry observation beats a specific-but-unverified claim. Never let an empty research pass produce a guessed detail; log `no_signal_found` and hand off the next-best cited layer.

2. **Score signals for buying relevance, not just novelty (7–8% rule).** 6sense's account-prioritization material notes only ~7–8% of a TAM is close enough to a purchase decision at any moment. Apply a relevance score to each extracted signal: (a) recency (<90 days), (b) proximity to a buying trigger (funding, hiring for the pain, leadership change, tech-stack change, expansion), (c) proximity to *this* prospect's remit. Rank signals and hand off the top 2–3 scored, not everything found — coverage breadth dilutes win rates.

3. **Signals are inputs; context is the deliverable.** Per 6sense, teams rarely lack signals — they lack the connective interpretation. Do not hand the Copywriter a raw fact list. Each handoff line = `signal + source URL + date + one-line "why this matters to this buyer now"`. Citation discipline: every point carries a live URL and retrieval date; anything without one is dropped before handoff, not flagged as "unconfirmed."

---

## 6. Sources

- https://www.lavender.ai/blog — verified live via CRW on 2026-08-03
- https://6sense.com/blog — verified live via CRW on 2026-08-03
- https://blog.hubspot.com/sales — verified live via Jina on 2026-08-03

## Live Web Refresh (2026-08-05)

- **The State of Personalization Report — Twilio Segment** — https://segment.com/state-of-personalization-report/ — Primary-source stats to anchor personalization arguments: 89% of business leaders say personalization is crucial to business success in the next 3 years; 73% of brands agree AI adoption will fundamentally change personalization strategy; 61% are worried inaccurate data compromises AI/ML personalization ("garbage in, garbage out"). Scott Brinker (HubSpot) framing quoted directly: the goal is a gen-AI engine that absorbs everything known about a prospect plus all relevant campaign content and synthesizes a message "wholly crafted for that specific person." Also flags conversational AI/chatbots as the most impactful personalization tech over the next 5 years — i.e. personalization is moving from static merge fields to ongoing dialogue. (verified live via CRW on 2026-08-05)
- **Twilio named a Leader in the 2026 Gartner® Magic Quadrant™ for CPaaS** — https://www.twilio.com/en-us/report/gartner-mq-cpaas-2026 — Current (Gartner doc dated May 18, 2026) vendor-landscape primary source. Confirms the delivery layer for 1:1 messaging has consolidated into CPaaS platforms combining contextual customer data + channels + AI, with omnichannel orchestration (not single-channel email blasts) as the evaluated capability. Useful for choosing where dynamic-content logic should live: in the customer-data/orchestration layer, not hardcoded per-template. (verified live via CRW on 2026-08-05)

**Dead links encountered (do not cite):** `twilio.com/en-us/blog/insights/ai-personalization-trends` (404), `twilio.com/en-us/state-of-customer-engagement-report` (404), `litmus.com/blog/email-personalization` (404 — the live hub is `litmus.com/email-personalization`). HubSpot's blog article rendered nav chrome only under CRW — body content is JS-gated, so it is not usable as a scraped primary source.

### Skill improvements adopted

1. **Lead with data quality, not clever copy.** Before drafting any personalized sequence, run a data-hygiene pass on the fields I intend to merge (freshness, lineage, null rate). The 61% "inaccurate data" finding says the dominant failure mode of AI personalization is bad inputs, not bad prompts. Practical rule: never merge a field I cannot verify was updated within the campaign's recency window — fall back to a segment-level variant instead of a broken 1:1 token.
2. **Design for conversation, not for a single send.** Treat each personalized email as turn one of a thread with persistent memory of prior interactions, and write dynamic content blocks that can be re-used by a downstream conversational/agentic channel. Concretely: keep personalization logic in the data/orchestration layer as named, reusable variants (with a defined default), rather than embedding one-off conditional logic inside individual email templates.
3. **Cite verified primary sources only.** Practitioner blog URLs rot fast (3 of 5 targets 404'd this session). Always confirm a real title/heading in the CRW output before quoting a stat, and record the dead links so the next refresh does not retry them.

## Related

- [[02 - ORGANIZATION/Agents/Identity/Personalization Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Personalization Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
- [[02 - ORGANIZATION/Agents/Training/Personalization Agent - Training.md|02 - ORGANIZATION/Agents/Training/Personalization Agent - Training.md]]
- [[02 - ORGANIZATION/Agents/Verification Logs/Personalization Agent - Verification Log 2026-08-05.md|02 - ORGANIZATION/Agents/Verification Logs/Personalization Agent - Verification Log 2026-08-05.md]]
- [[02 - ORGANIZATION/Memory Ledgers/personalization-agent.md|02 - ORGANIZATION/Memory Ledgers/personalization-agent.md]]
- [[09 - RESEARCH/B2B Email Personalization Methodology - Personalization Agent.md|09 - RESEARCH/B2B Email Personalization Methodology - Personalization Agent.md]]
- [[11 - PROJECTS/BrightPath Digital/03-Personalization.md|11 - PROJECTS/BrightPath Digital/03-Personalization.md]]
- [[17 - ARCHIVE/Knowledge Packages 2026-08-06/Personalization Agent - Smoke Test 2026-08-06.md|17 - ARCHIVE/Knowledge Packages 2026-08-06/Personalization Agent - Smoke Test 2026-08-06.md]]

---

## Live Web Refresh (2026-08-31)

**Sources reviewed**
1. https://segment.com/state-of-personalization-report/ — Twilio Segment State of Personalization 2024 (verified via CRW 2026-08-31)
2. https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/the-value-of-getting-personalization-right-or-wrong-is-multiplying — McKinsey Next in Personalization (verified via CRW 2026-08-31)
3. https://www.leadfeeder.com/blog/marketing-strategy/b2b-email-marketing-guide/ — Leadfeeder B2B Email Marketing 2026 Guide (verified via CRW 2026-08-31)
4. https://spintadigital.com/blog/account-based-marketing-2026/ — Spinta Digital ABM 2026 (verified via CRW 2026-08-31)
5. https://www.klaviyo.com/blog/lead-acquisition-personalization-strategy — Klaviyo Zero-Party Data Lead Acquisition (verified via CRW 2026-08-31)
6. https://www.klaviyo.com/blog/future-of-marketing-personalization — Klaviyo Future of Marketing Personalization 2026 (verified via CRW 2026-08-31)
7. https://www.optimizely.com/field-notes/articles/dynamic-experiences-in-personalization/ — Optimizely Dynamic Experiences (verified via CRW 2026-08-31)

**Key findings adopted**

1. **AI is fundamentally changing personalization** — 73% of brands agree AI adoption will fundamentally change personalization strategy (Segment); 60% of consumers interact with AI weekly; 73% of B2C marketers using/exploring AI for messaging personalization; 66% for product recommendations (Klaviyo). The shift is from static merge fields → ongoing dialogue via chatbots/conversational AI.

2. **Data quality is the dominant failure mode** — 61% of companies worry inaccurate data compromises AI/ML personalization ("garbage in, garbage out"). Practical rule: never merge a field that cannot be verified as updated within the campaign's recency window — fall back to segment-level variant instead of broken 1:1 token.

3. **Personalization has a scale problem** — Optimizely confirms: predefined/rule-based/segment-led/manual cannot scale to the individual. The shift: predefined→generated, segments→individuals, reactive→proactive, pre-designed journeys→experiences created in the moment. Dynamic Experiences assemble content on the fly per visitor; marketers guide content/intent/guardrails, AI handles decisioning.

4. **Zero-party data is the privacy-compliant foundation** — Klaviyo: single follow-up question at sign-up ("Why are you shopping today?") shapes entire downstream personalization. 74% consumers expect personalized experiences. Cross-channel capture (K:AI Customer Agent, Klaviyo Social) syncs social engagement into owned database. Meta lookalike audiences + exclusion lists from purchase data.

5. **Consumer trust in AI varies — personalize the personalization** — Only 13% completely trust AI; 21% uncomfortable with AI that "pretends" to know them (Klaviyo). Blanket AI personalization turns off part of the audience. Tailor approach per trust level; use explicitly consented data only.

6. **B2B frameworks evolved for 2026** — Leadfeeder: segmentation by role/company tier/deal stage; lifecycle stages with specific triggers/CTAs; subject line frameworks (Outcome-first, Risk reduction, Curiosity, FOMO/urgency, Direct); copy frameworks (PAS, Before/After/Bridge, Objection handler); A/B testing rules (isolate variables, 1000+/version, 48-72hr). Spinta P.R.E.C.I.S.E. ABM: Prioritize→Research→Engage→Connect→Integrate→Scale→Evaluate; metrics shift from leads to Account Engagement Score, Pipeline Velocity, Influence Index, Revenue Retention Rate, Marketing-to-Sales Sync Rate.

7. **Measured outcomes validate the approach** — Thirdlove: $200K+ revenue from personalized hub; Half Magic: 110% YoY automation revenue growth; Every Man Jack: 25% YoY flow revenue growth; Spinta B2B SaaS: pipeline velocity +44%, win rate +32%, CAC -27%, alignment +65% in 9 months.
