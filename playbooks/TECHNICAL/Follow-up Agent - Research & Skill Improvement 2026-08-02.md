---
type: Agent Training
status: active
tags: [02-organization]
---

# Follow-up Agent — Method Playbook

> Companion note: [[Follow-up Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I generate intelligent follow-up emails at the right intervals (Day 3, Day 7, Day 14, Day 30) so no lead goes cold. I never repeat previous messages — each follow-up adds new value or a new angle — and I reference prior thread context.

**Never:** repeat a prior message; send a follow-up after a reply/meeting booked/unsubscribe without checking the CRM stage.

---

## 2. Core Workflow

### Phase A — Trigger
1. Take the campaign sequence + prior messages from the Campaign Manager / Copywriter.

### Phase B — Generate
2. For each due follow-up, generate a fresh message referencing the thread and adding value.
3. Check against all prior messages; if it would repeat, rewrite with a distinct hook.

### Phase C — Handoff
4. Hand follow-up copy to the Campaign Manager for scheduling.
5. Signal the CRM Manager to stop the cadence on reply/meeting/unsubscribe.

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

**Sources fetched this pass**
- https://www.yesware.com/blog/sales-follow-up-email/ — verified live via CRW on 2026-08-03
- https://www.yesware.com/blog/sales-email-frequency-guide-pays-follow/ — verified live via Jina on 2026-08-03
- https://www.lemlist.com/blog/follow-up-email — verified live via Jina on 2026-08-03 (multichannel sequence guidance; page rendered nav-heavy, used for channel-mix context only)

**Skill improvements adopted**

1. **Tighten cadence to the open-decay curve, not the calendar.** Yesware's dataset (500k+ sales emails) shows 91% of emails that ever open are opened within one day, 90% of replies arrive within a day of the open, and over half within three hours. Practical change: when tracking shows *opened, no reply within 24-48h*, fire the next touch then — do not idle to Day 7. Keep Day 3 / 7 / 14 / 30 as the default no-signal spine, but let engagement signals compress it.

2. **Never stop at touch #1 — persistence is where the reply volume is.** 70% of unanswered sales email chains stop after the first email, yet the second email earns roughly a 21% reply rate when the first is ignored, with another ~25% cumulative chance across later touches. Practical change: enforce a minimum 4-touch sequence before any lead is marked cold, and log a reason code whenever a cadence is stopped early.

3. **Rotate a distinct *angle* per touch instead of re-sending the ask (thread-aware variation).** The highest-performing templates each used a different mechanism: referencing observed behavior (opens/clicks) hit ~50% reply; a post-call recap that adds a new resource hit ~51%; a "point me to the right person" referral pivot works via the Ben Franklin effect when the contact isn't the decision-maker. Practical change: maintain an angle ledger per thread — behavior-reference → new-value/insight → referral pivot → short breakup — and block generation if the drafted angle or opening line matches any prior message in the thread. Keep messages short (brevity correlates with faster response) and always restate the exact next step.

---

## 6. Sources

- https://www.yesware.com/blog/sales-follow-up-email/ — verified live via CRW on 2026-08-03
- https://www.yesware.com/blog/sales-email-frequency-guide-pays-follow/ — verified live via Jina on 2026-08-03
- https://www.lemlist.com/blog/follow-up-email — verified live via Jina on 2026-08-03

## Live Web Refresh (2026-08-05)

- Does cold email even work any more? Here's what the data says — https://www.gong.io/blog/does-cold-email-even-work-any-more-heres-what-the-data-says — Gong Labs analysis of 28M+ cold emails (Jason Bay / Outbound Squad; published 2025-07-24, last modified 2026-05-27). Key numbers for follow-up work: top performers book **8.1x more meetings** than average performers and get **4.2x more replies** — the skill gap, not the channel, is the constraint. **10%+ reply rate is the gold standard.** Copy rules that drive it: use the customer's language about *problems*, not your solution; **100 words or fewer**, with the highest reply rates at **3-4 sentences** (cognitive-load theory — the easier the ask is to process, the more likely the action). (verified live via CRW on 2026-08-05)
- Do execs really reply to cold email? Here's what the data says — https://www.gong.io/blog/do-execs-really-reply-to-cold-email-here-s-what-the-data-says — Gong executive-insights research (Dan Morgese; published 2026-01-29, last modified 2026-05-27). Executives spend **<3 seconds** deciding whether to open and **no more than 9 seconds** reading. Highest-performing exec emails land **between 50 and 100 words**. Buzzwords and vague ROI claims measurably *reduce* reply rates; short subject lines anchored to the exec's own world (e.g. "Student dropout risk") outperform. Structural guidance: **make an offer, not a meeting request**, and use the Problem Prompter framework. (verified live via CRW on 2026-08-05)
- Gong blog index — https://www.gong.io/blog/ — used as the landing page to resolve real article slugs via link extraction rather than guessing URLs. Index confirmed live and current. (verified live via CRW on 2026-08-05)

**Honesty note:** https://blog.hubspot.com/sales/sales-follow-up resolved (HTTP 200, real HubSpot shell) but CRW returned only navigation chrome — no article body was extractable, so **no claims are recorded from it**. Nothing from that page has been paraphrased or invented.

### Skill improvements adopted

1. **Hard length ceiling on every follow-up.** 100 words max for standard contacts; **50-100 words for C-level**. Target 3-4 sentences. Any draft over that gets cut before send.
2. **Nine-second test for exec follow-ups.** If the ask isn't legible inside ~9 seconds of reading, rewrite. Subject line short and anchored to the recipient's world — not to my product.
3. **Ban buzzwords and unquantified ROI claims** in follow-up copy — Gong data shows these actively depress reply rates. Replace with the prospect's own problem language.
4. **Offer, don't request.** Convert "do you have 15 minutes?" follow-ups into a concrete offer (a teardown, a benchmark, a relevant datapoint) that has standalone value if they never book.
5. **Reply rate is the follow-up KPI, benchmarked at 10%+.** Track per-sequence reply rate rather than send volume; an 8.1x meeting delta between top and average performers means persistence without craft is wasted cadence.
6. **Problem-first, not solution-first, on every touch** — including later-stage bump and re-engagement emails, which are the ones most likely to drift into product talk.
7. **Resolve URLs from a live index, never guess slugs** — link extraction off a landing page avoided 404s entirely on this pass; adopt as standing research practice.

## Related

- [[02 - ORGANIZATION/Agents/Identity/Follow-up Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Follow-up Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/Interviews/Follow-up Agent - Interview 2026-08-10.md|02 - ORGANIZATION/Agents/Interviews/Follow-up Agent - Interview 2026-08-10.md]]
- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
- [[02 - ORGANIZATION/Agents/Training/Follow-Up Agent - Training.md|02 - ORGANIZATION/Agents/Training/Follow-Up Agent - Training.md]]
- [[02 - ORGANIZATION/Agents/Verification Logs/Follow-up Agent - Verification Log 2026-08-05.md|02 - ORGANIZATION/Agents/Verification Logs/Follow-up Agent - Verification Log 2026-08-05.md]]
- [[02 - ORGANIZATION/Memory Ledgers/follow-up-agent.md|02 - ORGANIZATION/Memory Ledgers/follow-up-agent.md]]
- [[04 - REVENUE/Follow Up/README.md|04 - REVENUE/Follow Up/README.md]]
- [[09 - RESEARCH/B2B Sales Follow-Up Sequence Methodology - Follow-up Agent.md|09 - RESEARCH/B2B Sales Follow-Up Sequence Methodology - Follow-up Agent.md]]

---

## Live Web Refresh (2026-08-31)

**Sources fetched this pass**
- https://www.yesware.com/blog/sales-follow-up-email/ — re-verified via CRW on 2026-08-31
- https://www.yesware.com/blog/sales-email-frequency-guide-pays-follow/ — re-verified via CRW on 2026-08-31
- https://www.gong.io/blog/does-cold-email-even-work-any-more-heres-what-the-data-says — re-verified via CRW on 2026-08-31
- https://www.gong.io/blog/do-execs-really-reply-to-cold-email-here-s-what-the-data-says — re-verified via CRW on 2026-08-31
- https://www.woodpecker.co/blog/how-to-send-a-follow-up-email-after-no-response/ — verified live via CRW on 2026-08-31 (13 follow-up templates, 2026 edition)
- https://www.salesforce.com/blog/sales/sales-follow-up-email-templates/ — verified live via CRW on 2026-08-31

**Skill improvements adopted**

1. **Open-decay curve-driven cadence compression (reinforced).** 91% of opens within 24h (Yesware 500k+); 90% replies within 1 day of open; >50% within 3h. **Practical change:** Fire next touch on "opened, no reply 24-48h" signal — don't wait for Day 7. Keep Day 3/7/14/30 as default no-signal spine.

2. **Sequence length: minimum 4 touches.** 70% stop after #1 (Yesware); 2nd email = 21% reply rate; cumulative ~25% across later touches. Woodpecker 2026: 3–5 follow-ups total, spaced 3–7 days apart, increasing intervals for later messages. Log reason code if cadence stopped early.

3. **Angle rotation ledger (expanded).** Four distinct mechanisms per thread:
   - Touch 1-2: Behavior reference (opens/clicks) → ~50% reply (Yesware)
   - Touch 2-3: New value/insight (case study, benchmark, resource) → ~51% reply (Yesware post-call recap)
   - Touch 3-4: Referral pivot ("point me to the right person") — Ben Franklin effect
   - Final: Short breakup — "Closing the loop" (Woodpecker #13)
   Block generation if drafted angle/opening matches any prior message in thread.

4. **Content rules hardened (Gong + Woodpecker):**
   - 100 words max standard; 50–100 for C-level; target 3–4 sentences
   - Problem-first, not solution-first — applies to re-engagement too
   - Ban: buzzwords, unquantified ROI, "AI," "platform," feature-led positioning (Gong: these *actively depress* reply rates)
   - Subject lines: 1–4 words best for execs; priority-based; avoid numbers/questions/buzzwords/social proof in subject

5. **Objection handling in follow-ups (Woodpecker templates):**
   - Firm follow-up (touch 3-4): "Should I speak with someone else, revisit later, or close the conversation?"
   - Meeting-request follow-up: Reduce commitment — offer summary/benchmark instead of call
   - Proposal/quote follow-up: Ask about specific obstacles (scope, timing, pricing) — opens conversation without discounting

6. **Breakup email = compliance touch.** "Closing the loop" — assume timing not right, no guilt/fake urgency/disguised meeting request. End: "If [problem] becomes relevant later, you know where to find me." Immediate stop on reply/meeting/unsubscribe.

7. **Re-engagement / win-back framework (Gong Problem Prompter):**
   1. "Saw this…" — reference strategic objective
   2. "ACME was up against X" — name the problem
   3. "We've seen companies handle this by…" — acknowledge status quo
   4. "Open to hearing how they did Y?" — offer new perspective
   5. "Either way" / P.S. — low-pressure close
   - Nth no-response: Simple multiple-choice (Woodpecker #12): 1) Relevant but not now, 2) Someone else handles it, 3) Not a priority. "A number is enough."

8. **CRM automation & personalization at scale:**
   - Behavior-triggered automation: fire follow-ups on open/click signals (Yesware tracking), not just calendar days
   - Angle ledger per thread: track angle used; block generation if matches prior
   - Personalization: prospect's problem language + specific social proof (logos/industries); avoid templated "I thought about what you said"
   - AI-assisted (2026): Klenty "Agentic Cadences" (custom cadences/account), "AI Account Research" (hyper-personalized at scale) — **but human review required**; Gong shows skill gap (top vs avg = 8.1x meetings) is the constraint, not the channel

9. **Sequence optimization & conversion tracking:**
   - KPI: Reply rate ≥ 10% (Gong gold standard); track per-sequence, not send volume
   - A/B test levers: subject length (1–4 words exec), word count (50–100 exec / ≤100 standard), CTA type (offer > meeting request), angle sequence
   - Top-performer delta: Top 10% = 8.1x meetings vs avg; Top 25% = 4.3x. Persistence without craft = wasted cadence
   - Open rate: Top reps get 2.1x opens; short priority-based subjects

10. **Compliance (GDPR / CAN-SPAM):**
    - Immediate stop on unsubscribe; honor "do not contact" in CRM
    - Breakup email documents good-faith loop closure
    - No manufactured urgency, no deceptive subject lines, clear sender identity
    - Data minimization: only store engagement data needed for cadence logic
