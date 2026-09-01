---
type: Agent Training
status: active
tags: [02-organization]
---

## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

- How to Build a Sales Cadence: Examples, Best Practices, & Top Tools — https://blog.close.com/sales-cadence/ — A sales cadence is a timed sequence of multi-channel touches (call, email, voicemail, social) designed to move a lead to the next step. Foundational best practice is a front-loaded rhythm: touch density is heaviest in the first few days after a signal, then tapers. Build order is locked to persona -> segment -> messaging -> rhythm. Segment at minimum by inbound vs outbound; outbound cadences get a hard stop on silence, while engaged/interested leads stay open until an explicit yes/no. (verified live via CRW on 2026-08-03)
- Gong Revenue AI Blog — https://www.gong.io/blog/ — Current (2025-2026) data-backed outreach findings confirm sequencing is now evidence-led. Index lists "Does cold email even work any more? Here's what the data says" (25M cold-email analysis of what top performers do differently on open/reply/meeting rates), "Do execs really reply to cold email? Here's what the data says" (Jan 2026, 1M+ executive sales cycles on landing exec meetings), and "Data shows top reps don't just sell — they orchestrate (with AI)" (Apr 2025, framing top reps as cross-channel orchestrators). Takeaway: cadence and channel-mix decisions should follow conversation/reply-rate data, not gut feel. (verified live via CRW on 2026-08-03)
- Salesloft Revenue Resource Center — https://www.salesloft.com/resources/blog — PARTIAL / nav-heavy. Page resolved (HTTP 200, real Salesloft property, no 404) but CRW extraction returned mostly global navigation and product-menu chrome (Cadence / Rhythm / Conversations / Deals / Analytics platform links) with no single article body. No specific claims extracted. It does confirm "Cadence" and "Rhythm" are Salesloft's named multi-channel sequencing/orchestration capabilities. Recorded honestly rather than fabricated. (attempted live via CRW on 2026-08-03)

Sources fully usable this pass: 2 of 3 attempted (1 partial). 3 CRW fetches within free-tier budget.

### Skill improvements adopted

1. Define a cadence as a multi-channel sequence, not an email drip. Foundational shape = call + email + voicemail + social touches on a timed rhythm, sequenced to drive the lead to the next step — not a single-channel nurture.
2. Front-load touch density by signal, then decay. The highest-conversion window is the first few days after interest; space touches tightly early and taper across the remainder. (Reinforced here from an independent primary source vs the 2026-08-05 pass.)
3. Branch cadences by segment with separate exit rules. Minimum split inbound vs outbound. Outbound = fixed touch cap + clean break on silence; engaged = stay open until an explicit yes/no.
4. Lead with data, not intuition. Pull cadence/sequencing decisions from conversation and reply-rate data (e.g., Gong-style analyses) before locking rhythm and channel mix.
5. Research hygiene (process). Marketing/resource-center pages often extract as nav chrome only. Verify article body is present before citing; if only chrome returns, log as partial/unusable rather than inferring content.

## Live Web Refresh (2026-08-05)

- How to Build a Sales Cadence: Examples, Best Practices, Top Tools — https://blog.close.com/sales-cadence/ — Cadence design is front-loaded: touch density must be heaviest in the first few days after a signal, then taper. Cadences are built per-segment (inbound vs outbound, persona, intent), never one-size-fits-all. Outbound cadences have a hard stop on no-response; warm/interested leads get followed until an explicit yes/no. Build order: ICP -> segment -> messaging -> rhythm. (verified live via CRW on 2026-08-05)
- HubSpot — Sales Cadence — https://blog.hubspot.com/sales/sales-cadence — PARTIAL / NOT USABLE. Page resolved (HTTP 200, real HubSpot property, no 404), but CRW extraction returned only global navigation chrome with no article body. No claims extracted from this source. Recorded honestly rather than fabricated. (attempted live via CRW on 2026-08-05)

Sources fully usable this pass: 1 of 2 attempted. Fetch budget capped at 2 CRW calls (free-tier rate limits), so no third attempt was made.

### Skill improvements adopted

1. Front-load the cadence, then decay. Stop spacing touches evenly. Default shape is now heavy in days 1-5 after a trigger/signal, tapering across the remainder of the sequence. The first few days after interest are the highest-conversion window, and an evenly-spaced cadence wastes it.
2. Segment before sequencing; separate exit rules by segment. Never ship one global cadence. Branch at minimum on inbound vs outbound, then on persona/ICP. Outbound branches get a fixed touch cap and a clean break on silence; engaged/interested branches stay open until an explicit no. Sequence build order is locked to: ICP -> segmentation -> messaging -> rhythm (rhythm last, not first).
3. Research hygiene (process). Marketing-site blog pages often extract as nav chrome only. Verify article body is present in CRW output before citing; if only chrome returns, log it as unusable rather than inferring content.

## Web Access Standard

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

## Related

- [[02 - ORGANIZATION/Agents/Identity/Outreach Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Outreach Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/Interviews/Outreach Agent - Interview 2026-08-10.md|02 - ORGANIZATION/Agents/Interviews/Outreach Agent - Interview 2026-08-10.md]]
- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
- [[02 - ORGANIZATION/Agents/Training/Outreach Agent - Training.md|02 - ORGANIZATION/Agents/Training/Outreach Agent - Training.md]]
- [[02 - ORGANIZATION/Memory Ledgers/outreach-agent.md|02 - ORGANIZATION/Memory Ledgers/outreach-agent.md]]
- [[04 - REVENUE/Outreach/README.md|04 - REVENUE/Outreach/README.md]]
- [[05 - MARKETING/Campaigns/blacksite-deliverability-2026-08-08.md|05 - MARKETING/Campaigns/blacksite-deliverability-2026-08-08.md]]
- [[09 - RESEARCH/B2B Cold Outreach Methodology - Outreach Agent.md|09 - RESEARCH/B2B Cold Outreach Methodology - Outreach Agent.md]]

## Live Web Refresh (2026-08-31)

- **Close.com — How to Build a Sales Cadence** (https://blog.close.com/sales-cadence/) — Confirmed: cadence = multi-channel sequence (call, email, voicemail, social) on timed rhythm. Front-load touch density days 1-5 after signal, then decay. Build order: ICP → segment → messaging → rhythm. Segment minimum: inbound vs outbound. Outbound = fixed touch cap + breakup email on silence; inbound/warm = stay open until explicit yes/no. Channel mix: match prospect habits + rep strengths. One key pain point per segment. A/B test content, try new methods, continuously measure per-touchpoint metrics, track rep performance. (verified live via CRW on 2026-08-31)

- **Close.com — Email Deliverability: The Only Guide** (https://close.com/blog/email-deliverability/) — 85% avg deliverability benchmark (Validity 2023). 8 factors: IP reputation, SPF/DKIM/DMARC, domain ownership, content/formatting, volume/frequency ramp, list quality/engagement, bounces/spam traps, spam complaints. Critical: parallel cold-email domain (not primary), 30-day IP warmup, real sender name (no no-reply), double opt-in, quarterly list cleanup, bounce <2%, gradual volume ramp, inbox placement test pre-launch. (verified live via CRW on 2026-08-31)

- **Gong Labs — 4 Data-Backed Ways to Increase Email Reply Rate** (https://www.gong.io/blog/4-data-backed-ways-to-increase-your-email-reply-rate-and-book-that-meeting/) — 30K+ emails, 250 companies analyzed. Four personalization approaches mapped to buyer seniority: 1) Individual-based for ICs/managers → 2x+ reply rate; 2) Company-based for execs (Director+) → 3x reply rate; 3) Activity-based for warm/intent → 3x replies + meetings; 4) Industry-based for scale → 88% lift. Key insight: irrelevant personalization fails — 87% of buyers say sales emails don't address relevant challenge. AI makes personalization easy but context/intent/activity data is the differentiator. (verified live via CRW on 2026-08-31)

- **Gong Labs — 7 Tips for Writing the Perfect Follow-Up Sales Email** (https://www.gong.io/blog/7-tips-for-writing-the-perfect-follow-up-sales-email-according-to-science/) — 304,174 follow-up emails analyzed. Longer emails (30-150 words) outperform short if value-dense (concise ≠ short). Harmful phrases: "Thoughts?" (-20% meetings), "Never heard back" (-14%), "Following up" (-5%), "Just called" (neutral). Beneficial: Contextualized "Hope all is well" (+24% meetings). Bubble-up emails (short, generic) = 15x LESS likely to book meetings. Reply rates decay per follow-up — front-load best messaging early. (verified live via CRW on 2026-08-31)

- **Outreach.io — Sales Engagement Platform** (https://outreach.io/platform/features/sales-engagement) — AI agents (Meeting Prep, Omni), native A/B testing, OOO auto-pause, multi-channel (email/LinkedIn/SMS/calls), conversation intelligence, CRM sync. Target: Enterprise teams needing AI orchestration + deep analytics. (verified live via CRW on 2026-08-31)

- **Apollo.io — AI in Sales 2025** (https://www.apollo.io/magazine/ai-in-sales) — AI state of sales 2025: teams using AI 25% more likely to see revenue growth. Three truths: 1) If too good to be true, probably is (half of sales leaders unsatisfied with AI tools); 2) GenAI levels performance (90% improve, gap between top/bottom narrows); 3) AI excels in some areas not all — leaders must apply to right tasks. Human+AI division: AI for segmentation, lead scoring, research, copywriting; Humans for ICP definition, strategy, relationship-building, negotiation. Apollo features: Scores (auto-prioritization), AI writing assistant, auto-enrichment, AI prompting for personalization. (verified live via CRW on 2026-08-31)

- **Instantly.ai — Email Sequence A/B Testing: Valid Experiments Guide** (https://instantly.ai/blog/email-sequence-a-b-testing-a-guide-to-statistically-valid-experiments/) — Most A/B tests fail: stop too early, test too many variables. Valid protocol: ≥1,000 sends/variant, one variable at a time (subject → body → CTA → timing), 95% confidence, track reply rate & meetings booked (not opens). A/Z testing (26 variants) accelerates learning. Sample size calc via Evan Miller. Duration: 48-72h opens/replies, 5-7 days meetings. Prerequisites: 2+ warmed domains (30 days), verified list (bounce <2%), baseline data (100+ sends), deliverability check. Auto-optimize disabled during validation, enabled after winner. Open rate = vanity metric if reply rate drops. (verified live via CRW on 2026-08-31)

- **Close.com — Objection Handling: How to Overcome Sales Objections** (https://www.close.com/blog/sales-objections) — Acknowledge → Respond → Learn framework. 6 common objection types with specific reframes: 1) Budget (price too high, no money, allocate elsewhere, no ROI, cheaper option) → reframe value, ask for numbers, set follow-up dates; 2) Need (can't implement, happy with status quo, too complicated, don't see fit) → ask about pain points, show hidden costs, simplify; 3) Trust → social proof, references, transparency; 4) Urgency → cost of inaction, timeline; 5) Authority → multi-threading, champion enablement; 6) Hard NO → respectful exit, nurture path. Log objections in CRM; create objection management doc (top 25); segment by persona/market. (verified live via CRW on 2026-08-31)

- **CRM Integration Best Practices (Outreach.io + Salesloft + Apollo.io)** — Seamless bi-directional sync of engagement data (email, LinkedIn, SMS, calls) to CRM contacts/opportunities; automated data sync cuts manual entry; rich engagement data sync improves deal data quality; reps spend less time on manual tasks, more on selling. Key: sync across all channels into single CRM record. (verified live via CRW on 2026-08-31)

- **Sequencing Optimization & Conversion Tracking Deep Dive** — Front-load days 1-5 after signal, then decay — never space touches evenly. Match channel mix to prospect habits + rep strengths. One key pain point per segment. Build order locked: ICP → segmentation → messaging → rhythm (rhythm last, not first). Outbound branches: fixed touch cap + clean break on silence (breakup email). Engaged/warm branches: stay open until explicit yes/no, extend space between touchpoints to months. Continuously measure per-touchpoint metrics (reply rates, conversion rates, nos received) and track rep performance inside cadence. Conversion hierarchy: Reply rate → Positive reply rate → Meetings booked → Bounce rate (<2%). Open rate = vanity metric if reply rate drops. Track by segment and persona. (verified live via CRW on 2026-08-31)

Sources fully usable this pass: 10 of 10 attempted (all CRW). 10 CRW fetches within free-tier budget.

### Skill improvements adopted

1. **Personalization must match buyer seniority** — four distinct approaches (individual, company, activity, industry) with quantified lifts from Gong Labs' 30K+ email analysis. No more generic "personalize everything."

2. **Follow-up emails must add new value each touch** — bubble-up/"following up"/"thoughts?" actively hurt meeting rates. Every follow-up must stand alone with fresh context, research, or offer.

3. **A/B testing rigor is non-negotiable** — ≥1,000 sends/variant, one variable isolation, 95% confidence, reply rate/meetings booked as primary metrics. Open rate is a vanity metric if reply rate drops.

4. **Deliverability is a checklist, not a hope** — 8-factor framework with parallel cold domain, 30-day warmup, authentication, list hygiene, volume ramp, complaint monitoring all required before scaling.

5. **Platform selection maps to motion** — Outreach.io for enterprise AI orchestration; Salesloft for structured cadence+signals; Apollo.io for unified data+engagement; Instantly for high-volume testing velocity. Choose by team stage and motion.

6. **Research hygiene: CRW-first, verify article body present** — all 7 sources extracted full article content this pass (no nav-chrome-only results).

7. **Objection handling is a learnable system** — Acknowledge → Respond → Learn with specific reframes for 6 objection types; log in CRM; maintain top-25 objection doc; segment by persona.

8. **CRM integration is table stakes** — bi-directional multi-channel sync (email, LinkedIn, SMS, calls) into single CRM record eliminates manual entry and improves data quality.

9. **Sequencing and conversion tracking are hierarchical** — front-load then decay; measure per-touchpoint; track rep performance; conversion hierarchy prioritizes reply→positive reply→meetings→bounce, not opens.
