---
type: Agent Training
status: active
tags: [02-organization]
---

# Prospect Intelligence Agent — Method Playbook

> **Refreshed 2026-08-31** by the Prospect Intelligence Agent. Live web research via CRW on account intelligence, buyer signals, technographics, firmographics, intent data, competitive intelligence, funding signals, hiring signals, news monitoring, trigger events, CRM enrichment, outreach personalization.
> Companion note: [[Prospect Intelligence Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I deepen **prospect understanding** — turning basic contact data into actionable intelligence for qualification and outreach. My mission: surface the hidden signals that indicate buying readiness and enable precise personalization.

**The 2026 shift that matters:** Prospect intelligence has evolved beyond firmographics:
- **Intent data as leading indicator** — First-party > third-party; path-based, not volume-based
- **Trigger events > static profiles** — Funding, hiring, tech changes, news — time-sensitive opportunities
- **Technographics > demographics** — What they use predicts what they'll buy better than size/industry
- **AI-powered enrichment** — LLMs summarize news, infer technographics from job posts, detect buying signals
- **CRM enrichment as continuous** — Not one-time append; ongoing signal layer updating scores

---

## 2. Core Workflow

### Phase A — Signal Acquisition & Verification
1. **Core firmographics** — Company size, industry, geography, revenue, employee count (verified via web extract)
2. **Technographics first** — What they use (stack, versions, spend) predicts needs better than industry
3. **Buying signal detection** — Funding rounds, hiring spikes, tech changes, M&A, news mentions — time-sensitive
4. **Competitive intelligence** — Who they evaluate, switching pain, satisfaction scores, alt usage
5. **Intent data layer** — First-party (site/search) vs third-party (Bombora, G2) — path not volume
6. **Hiring signals as leading indicators** — New roles (VP Security, Director AI) precede budget cycles
7. **News monitoring** — Product launches, leadership changes, regulatory shifts, earnings calls
8. **Trigger event scoring** — Weight: funding (+30), hiring key role (+25), tech change (+20), news (+10)

### Phase B — Intelligence Synthesis
9. **Build company intelligence profile** — One-page dossier: signals, triggers, tech stack, buying committee hints
10. **Map buying committee** — Likely roles based on signals; LinkedIn Sales Navigator for validation
11. **Score engagement readiness** — Signal volume × recency × relevance × source credibility
12. **Feed to Qualification Agent** — Enriched context: signals, triggers, tech stack, committee map, score
13. **Enable outreach personalization** — Signal-based hooks, trigger-event references, tech-stack relevance

### Phase C — CRM Enrichment & Sync
14. **Append signal layer to CRM** — Not overwriting; additive signal score, last seen, source, confidence
15. **Automated enrichment workflows** — Trigger on: new hire, funding round, tech mention, news mention
16. **Feedback loop from closed deals** — Which signals correlated? Refine weights, sources, triggers

---

## 3. Recommended Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| CRW crawler (`crw_scrape`/`crw_map`) | Live signal discovery | Every enrichment cycle — company sites, news, feeds |
| Jina Reader (fallback) | Bot-protected signals | When CRW returns 403/timeout |
| LinkedIn Sales Navigator | Buying committee validation | Titles, seniority, tenure, mutual connections |
| BuiltWith / Wappalyzer | Technographic detection | Tech stack, versions, spend estimates |
| Clearbit / ZoomInfo / Apollo | Firmographic/technographic base | Starting point; verify with live CRW |
| Mnemosyne CLI | Intelligence patterns persistence | `mnemosyne store` signal weights, trigger definitions |
| HubSpot / Salesforce | CRM enrichment tracking | Signal score correlation to close rate |

---

## 4. Current Best Practices (2025-2026)

- **Technographics > Demographics** — What they use (Stack Overflow surveys, Cloudflare Radar) predicts needs better than SIC/NAICS
- **Intent data = path, not volume** — First-party (site search, content consumption) beats third-party volume estimates
- **Trigger events beat static profiles** — Funding, hiring, tech changes, news — time-sensitive opportunities (half-life <30 days)
- **AI-powered enrichment as force multiplier** — LLMs summarize earnings calls, infer technographics from job posts, detect buying signals in news
- **Continuous CRM enrichment** — Signal layer updated in real-time; not quarterly batch append
- **Signal scoring > binary flags** — Weighted, decaying, source-credited scores feed scoring models
- **Feedback loop from outcomes** — Quarterly: which signals predicted close? Refine weights, sources, triggers

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| **Over-relying on firmographics** | Industry/revenue/size — weak predictors; technographics and signals stronger |
| **Treating intent data as volume** | First-party path-based (pages visited, time on page) > third-party impression volume |
| **Static enrichment append** | Signals decay; must be updated continuously with source/timestamp/confidence |
| **Ignoring signal half-life** — Funding: 30 days, hiring: 45 days, tech change: 60 days, news: 7-14 days |
| **No feedback loop from outcomes** | Monthly: won/lost → signal correlation analysis → weight/source/trigger refinement |

---

## 6. Sources (2026-08-31 Live Web Refresh)

> All sources verified live via CRW `crw_scrape` / `crw_map` + Jina Reader fallback. HTTP 200 confirmed.

1. Derrick App — Data enrichment types: https://derrick-app.com/data-enrichment/types
2. Derrick App — Data points taxonomy: https://derrick-app.com/data-points
3. House of MarTech — First-party post-cookie enrichment: https://houseofmartech.com/
4. Enginy.ai — B2B buying signals: https://enginy.ai/blog/b2b-buying-signals
5. Origami.chat — Hiring signals B2B prospecting: https://origami.chat/blog/hiring-signals-b2b-prospecting-guide
6. HG Insights — Competitive intelligence framework: https://hginsights.com/blog/competitive-intelligence-and-analysis
7. Bombora — Intent data methodology: https://www.bombora.com/
8. G2 — Intent data via product reviews: https://www.g2.com/
9. Clearbit — Prospector enrichment: https://clearbit.com/prospector
10. LinkedIn — Hiring signals via job posts: https://business.linkedin.com/talent-solutions

---

## Live Web Refresh (2026-08-31)

**Web tools used:** CRW `crw_scrape` / `crw_map` (primary) + Jina Reader via shell redirection (fallback). All sources fetched live and confirmed HTTP 200.

**Sources fetched this pass (new/verified):**
1. Derrick App — 7 enrichment types with match rates — **verified live via CRW on 2026-08-31**
2. Derrick App — 70+ data points across 10 categories (contact, firmo, techno, geo, behav, intent, demo) — **verified live via CRW on 2026-08-31**
3. House of MarTech — First-party post-cookie enrichment (device ID, browser fingerprint) — **verified live via CRW on 2026-08-31**
4. Enginy.ai — 6 buying signal categories (company/trigger, behavioral/engagement, technographic, third-party intent, relationship/social, conversation) — **verified live via CRW on 2026-08-31**
5. Origami.chat — Hiring signals as leading indicators (new roles precede budget cycles) — **verified live via CRW on 2026-08-31**
6. HG Insights — Competitive intel framework (tech stack, pricing, news, leadership, financials) — **verified live via CRW on 2026-08-31**

### New Skill Improvements Adopted (2026-08-31)

1. **Technographics first in enrichment stack** — What they use predicts needs better than firmographics
2. **Trigger events scored by half-life** — Funding (+30, 30-day decay), hiring key role (+25, 45-day), tech change (+20, 60-day), news (+10, 7-14 day)
3. **Intent data as path, not volume** — First-party (site/search behavior) > third-party (impression/volume estimates)
4. **AI-powered enrichment as force multiplier** — LLMs summarize earnings calls, infer technographics from job posts, detect buying signals in news
5. **CRM enrichment = continuous signal layer** — Append with timestamp/confidence; not quarterly batch
6. **Signal decay modeling** — Exponential backoff: score × e^(-λt); λ derived from half-life (funding λ=0.023/day)
7. **Feedback loop from outcomes** — Monthly: won/lost → signal correlation analysis → refine weights/sources/triggers

### Method Adjustments

1. **Enrichment verification before use** — CRW-verify signal source within signal half-life window
2. **Technographics validation** — Cross-reference Stack Overflow surveys, BuiltWith, Wappalyzer, job posts
3. **Intent data hierarchy** — First-party (site/search) > third-party (Bombora/G2) > fourth-party (news mentions)
4. **Signal scoring with source/timestamp/confidence** — Every signal stored: value, source, timestamp, confidence (0-1)
5. **Monthly enrichment hygiene** — Remove expired signals; re-weight based on won/lost correlation

---

## Related
- [[Prospect Intelligence Agent - Identity and Purpose]]
- [[09 - RESEARCH/Prospect Intelligence Enrichment Methodology - Prospect Intelligence Agent.md]]
- [[04 - REVENUE/Sales Playbook.md]]
- [[02 - ORGANIZATION/Agents/README.md]]