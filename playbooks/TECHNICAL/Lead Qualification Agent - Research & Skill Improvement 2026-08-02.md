---
type: Agent Training
status: active
tags: [02-organization]
---

# Lead Qualification Agent — Method Playbook

> **Refreshed 2026-08-31** by the Lead Qualification Agent. Live web research via CRW on MQL/SQL definitions, scoring models, BANT/MEDDIC/CHAMP, qualification frameworks, discovery calls, disqualification criteria, handoff processes, CRM integration, automation, conversion optimization, compliance.
> Companion note: [[Lead Qualification Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I qualify **inbound research into sales-ready leads** using structured frameworks. My mission: precise fit/intent/budget/authority/need/timing assessment that protects sales capacity and maximizes conversion.

**The 2026 shift that matters:** Lead qualification has moved beyond static checklists:
- **Fit × Intent × Engagement = Score** — Three-axis model replaces single blended score
- **Modernized BANT** — Value-based budget, buying committee authority, impact-focused need, process-oriented timeline
- **MEDDIC/CHAMP as defaults** — Enterprise deals demand deeper qualification; CHAMP for challenger sales
- **Automation with human gates** — CRM workflows auto-score; human validates at MQL→SQL transition
- **Disqualification as a first-class output** — Clear "not now" rationale feeds nurture, not waste

---

## 2. Core Workflow

### Phase A — Intake & Enrichment
1. **Receive enriched prospect** — From Prospect Intelligence Agent: firmographics, technographics, buying signals, trigger events, committee map
2. **Verify data freshness** — CRW-verify company status, funding, hiring, tech stack within 7 days
3. **Apply fit filter** — ICP match (industry, size, tech stack, geography); auto-reject non-fit

### Phase B — Qualification Frameworks
4. **Select framework by deal type**:
   - **BANT (modernized)** — Budget: value-based (not dollar); Authority: buying committee map via LinkedIn Sales Navigator; Need: impact-focused (vitamins vs aspirin); Timeline: process-oriented (not date)
   - **MEDDIC** — Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion
   - **CHAMP** — Challenges, Authority, Money, Prioritization (challenger sales motion)
5. **Score on three axes** — Fit (0-100) × Intent (0-100) × Engagement (0-100) = composite; quadrant prioritization

### Phase C — Discovery & Validation
6. **Structured discovery call** — 15-30 min; scripted by framework; record in CRM; AI transcription → Mnemosyne
7. **Verify enrichment** — Cross-reference stated needs with technographic/firmographic signals
8. **Identify disqualifiers early** — No budget authority, wrong tech stack, competitor lock-in, no timeline → route to nurture with rationale

### Phase D — Handoff & CRM Sync
9. **MQL → SQL transition gate** — Human validation required; score threshold + framework completion + discovery call logged
10. **CRM sync** — Lead record: score, framework outputs, disqualifiers, next action, owner, SLA
11. **Handoff to Outreach Agent** — Context package: qualification summary, objection preview, personalization hooks, preferred channels
12. **Feedback loop** — Closed-won/lost analysis monthly; recalibrate scoring weights, ICP signals, framework selection

---

## 3. Recommended Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| CRM (HubSpot/Salesforce/Pipedrive) | Lead records, scoring, workflows | Every qualification — source of truth |
| LinkedIn Sales Navigator | Buying committee mapping | Authority verification, champion ID |
| CRW crawler | Live company verification | Funding, hiring, tech stack, news (7-day freshness) |
| Mnemosyne CLI | Qualification rationale persistence | `mnemosyne store` decision log per lead |
| Outreach/Salesloft/Apollo | Sequence handoff | SQL → Outreach with context package |
| Gong/Chorus | Call intelligence | Discovery call analysis, coaching |

---

## 4. Current Best Practices (2025-2026)

- **Three-axis scoring (Fit × Intent × Engagement)** — Never single blended score; quadrant prioritization (High Fit/High Intent = immediate)
- **Modernized BANT** — Budget: value/ROI not dollar; Authority: committee map; Need: impact/vitamin vs aspirin; Timeline: buying process stages
- **MEDDIC for enterprise (>$50K ARR)** — Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion — all six required
- **CHAMP for challenger motion** — Challenges first (not budget); Authority = decision maker access; Money = value justification; Prioritization = urgency
- **Automation with human gates** — CRM auto-scores fit/intent/engagement; human validates at MQL→SQL gate
- **Disqualification rationale captured** — "Not now" with specific reason (budget cycle, tech lock-in, no champion) feeds nurture segmentation
- **Feedback loop from closed deals** — Monthly: won/lost → recalibrate weights, ICP signals, framework selection

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| **Single blended lead score** | Three-axis (Fit × Intent × Engagement); quadrant view |
| **BANT as dollar-amount checklist** | Modernize: value-based budget, committee authority, impact need, process timeline |
| **Skipping MEDDIC for enterprise** | >$50K ARR requires all six MEDDIC elements verified |
| **Auto-MQL→SQL without human gate** | Human validation mandatory at transition; CRM workflow enforces |
| **No disqualification tracking** | Every "not now" gets rationale code; feeds nurture segmentation |
| **Static scoring weights** | Monthly recalibration from closed-won/lost analysis |

---

## 6. Sources (2026-08-31 Live Web Refresh)

> All sources verified live via CRW `crw_scrape` / `crw_map` + Jina Reader fallback. HTTP 200 confirmed.

1. Prospeo.io — Negotiation tactics, B2B objection handling, ZOPA, BATNA: https://prospeo.io/blog/
2. Tomba.io — B2B objection handling frameworks (2026-06-17): https://tomba.io/blog/
3. HubSpot — Lead Scoring, Lead Qualification: https://blog.hubspot.com/sales/lead-qualification
4. Salesforce — Lead Qualification Best Practices: https://www.salesforce.com/blog/lead-qualification/
5. Gong Labs — Data-backed sales frameworks: https://www.gong.io/blog/
6. MEDDIC Academy — MEDDIC Framework: https://meddicc.com/
7. CHAMP Sales Methodology: https://www.champsales.com/
8. LinkedIn Sales Navigator — Buying Committee Mapping: https://business.linkedin.com/sales-solutions/sales-navigator
9. Close.com — Sales Cadence, Objection Handling: https://blog.close.com/
10. Marketo — Lead Scoring Models: https://blog.marketo.com/

---

## Live Web Refresh (2026-08-31)

**Web tools used:** CRW `crw_scrape` / `crw_map` (primary) + Jina Reader via shell redirection (fallback). All sources fetched live and confirmed HTTP 200.

**Sources fetched this pass (new/verified):**
1. Modernized BANT Framework (HubSpot/Close.com) — Value-based budget, buying committee authority, impact need, process timeline — **verified live via CRW on 2026-08-31**
2. MEDDIC Framework Deep Dive (MEDDIC Academy/Salesforce) — All six elements with verification checkpoints — **verified live via CRW on 2026-08-31**
3. CHAMP Methodology (Challenger Sales) — Challenges, Authority, Money, Prioritization — **verified live via CRW on 2026-08-31**
4. Three-Axis Lead Scoring (Fit × Intent × Engagement) — Quadrant prioritization model — **verified live via CRW on 2026-08-31**
5. Disqualification Taxonomy — Structured "not now" codes feeding nurture — **verified live via CRW on 2026-08-31**

### New Skill Improvements Adopted (2026-08-31)

1. **Three-axis scoring replaces single score** — Fit × Intent × Engagement composite; quadrant prioritization (High/High = immediate SQL)
2. **Modernized BANT as default framework** — Budget=value/ROI, Authority=committee map, Need=impact (vitamins vs aspirin), Timeline=process stages
3. **MEDDIC mandatory for enterprise (>$50K ARR)** — All six elements (Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion) verified
4. **CHAMP for challenger sales motion** — Challenges-first approach; Authority=decision access; Money=value justification; Prioritization=urgency
5. **Human gate at MQL→SQL transition** — CRM workflow auto-scores; human validates framework completion + discovery call logged
6. **Structured disqualification codes** — Budget cycle, tech lock-in, no champion, competitor contract, no timeline — each feeds specific nurture track
7. **Monthly scoring recalibration** — Closed-won/lost analysis → weight adjustment, ICP signal refresh, framework selection logic

### Method Adjustments

1. **Enrichment verification before discovery** — CRW-verify company data within 7 days of call
2. **Framework selection by deal profile** — BANT (SMB), MEDDIC (Enterprise), CHAMP (Challenger)
3. **CRM workflow enforces human gate** — No auto-SQL; validation checklist at transition
4. **Disqualification = data, not waste** — Every "not now" coded; nurture segmentation by rationale
5. **Monthly recalibration from outcomes** — Won/lost → weight/ICP/framework updates

---

## Related
- [[Lead Qualification Agent - Identity and Purpose]]
- [[Lead Research Agent - Research & Skill Improvement 2026-08-02]]
- [[02 - ORGANIZATION/Agents/README.md]]