---
type: Agent Training
status: active
tags: [02-organization]
---

# Lead Research Agent — Method Playbook

> Companion note: [[Lead Research Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I find companies that match our services and produce structured, enriched lead records. I research businesses, find websites, identify industries, find decision-makers, verify information, and enrich lead data. Every record I output carries Company, Industry, Location, Website, Employee Size, Technology Stack, and an Opportunity Score.

**Never:** pass unverified or fabricated data; score a lead I haven't verified the website and decision-maker for.

---

## 2. Core Workflow

### Phase A — Source
1. Take the target segment / ICP from the Sales Director.
2. Source companies via web research (CRW `crw_scrape`/`crw_map`, public directories, company sites).

### Phase B — Enrich & Verify
3. Capture the output fields; cross-check website and decision-maker before scoring.
4. Compute an Opportunity Score from ICP fit + buying signals.

### Phase C — Handoff
5. Hand verified, scored leads to the ICP & List Building Agent.

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

Sources fetched this pass:

1. https://www.lusha.com/blog/b2b-data-enrichment/ — "What is B2B data enrichment? A complete guide for GTM teams (2026)" (modified 2026-07-15) — verified live via CRW on 2026-08-03
2. https://www.lusha.com/blog/lead-enrichment/ — "What is lead enrichment? Definition, benefits, and top tools" — verified live via Jina on 2026-08-03 (Cloudflare-blocked to CRW)
3. https://business.linkedin.com/sales-solutions/sales-navigator — LinkedIn Sales Navigator product/methodology page — verified live via Jina on 2026-08-03

### Skill improvements adopted

**1. Separate prospecting from enrichment as two distinct passes.** Prospecting finds net-new contacts matching the ICP from a blank list; enrichment completes records that already exist. Running them as one blurred step wastes budget. Practice: pass A = ICP-filtered discovery (title, industry, headcount, geo), pass B = field completion on the surviving records only.

**2. Enrich only the fields that predict conversion, and treat data as decaying.** B2B contact data decays ~22.5%/year and the average B2B professional changes jobs every ~18 months, so any record older than a quarter is suspect. Gartner puts poor data quality at ~$12.9M/yr average cost; IBM found 43% of COOs rank data quality their top data challenge and >25% of orgs lose >$5M/yr. Practice: anchor the enrichment schema to the ICP (revenue, headcount, industry, tech stack) rather than appending every available field, and stamp each record with a capture date + re-verify before outreach.

**3. Score on dynamic signals, not just static firmographics.** The highest-value layer is technographics + buying signals (funding rounds, hiring/job-post velocity, exec changes such as a new CRO, intent data) laid on top of static firmographic fields — these are what change the conversation. Practice: opportunity score = ICP fit (firmographic match) x signal recency (a signal in the last 30–90 days outranks a perfect-fit account with no event).

**4. Verification discipline for an AI sales team.** ~45% of business leaders cite data accuracy as a leading barrier to scaling AI; scoring models and AI-drafted outreach are only as good as the underlying records. Practice: never pass an unverified email/phone into an automated sequence — mark provenance (source + fetch date + verification method) on every enriched field, and prefer verified direct dials over inferred/pattern-guessed contacts.

**Fetch-tooling note:** vendor blog URLs churn fast — Apollo `/blog/lead-scoring` and `/magazine/lead-scoring` both 404'd and BuiltWith's blog path 404'd. Lusha is behind Cloudflare. Verify a URL returns HTTP 200 with real body content before citing it; fall back to Jina reader for anti-bot interstitials.

## 6. Sources

- https://www.lusha.com/blog/b2b-data-enrichment/ — verified live via CRW on 2026-08-03
- https://www.lusha.com/blog/lead-enrichment/ — verified live via Jina on 2026-08-03
- https://business.linkedin.com/sales-solutions/sales-navigator — verified live via Jina on 2026-08-03

## Live Web Refresh (2026-08-05)

- The GTM with Clay Blog (index) — https://clay.com/blog — Current 2025-2026 practitioner roadmap of the enrichment market: waterfall enrichment across 200+ providers, TAM sourcing via natural-language search over company+people+job data, "Lookalikes" off best customers, and MCP exposure of enrichment functions directly to reps in AI tools. Confirms the market has moved from single-vendor lists (Apollo/ZoomInfo) to multi-provider orchestration layers. (verified live via CRW on 2026-08-05)
- The GTM Signal Your Competitors Can't Buy (How First-Party Signals Become Your GTM Moat) — https://clay.com/blog/how-first-party-signals-become-your-gtm-moat — Verkada's Cody Leovic argues rented third-party intent data is commoditized because every competitor can buy the same feed; the durable edge is mining first-party signals already owned: CRM notes, email replies, call transcripts, product usage. Intent should be constructed from owned exhaust, not purchased. (verified live via CRW on 2026-08-05)
- Introducing Account Research Agents to Clay — https://clay.com/blog/account-research-agents — Enrichment is shifting from point-in-time waterfall lookups to always-on research agents that continuously re-check accounts and fire expansion / re-engagement plays when facts change. Also notes open-weight models now usable for long-running agent research tasks (cost control on high-volume enrichment). (verified live via CRW on 2026-08-05)

### Skill improvements adopted

1. **Rank first-party signals above purchased intent in every prospecting brief.** Before recommending any third-party intent vendor, I will first inventory the client's owned signal surfaces (CRM notes, reply text, call transcripts, product/usage logs, support tickets, web sessions) and build the scoring model on those. Third-party intent gets used only as a *coverage filler* for accounts with no owned signal — never as the primary ranking input, because a bought feed is by definition also in a competitor's hands.
2. **Treat enrichment as a continuous agent loop, not a one-shot waterfall.** New default deliverable: a re-check cadence (trigger-based monitoring for job changes, funding, tech installs, headcount deltas) that re-scores accounts and emits a play, rather than a static enriched CSV. Pair with cost control — route long-running/bulk research passes to cheap open-weight models and reserve premium calls for the final verification hop and for records that already cleared a signal threshold.
3. **Verification discipline reconfirmed:** two of my first candidate URLs (clay.com/blog/waterfall-enrichment, gtmonly.com 2025 state-of-GTM-data) returned 404 bodies with HTTP 200-style output. Always scrape the blog *index* first, harvest live article slugs from it, then scrape the article — and confirm a unique H1 per page before citing.

## Live Web Refresh (2026-08-31)

Sources fetched this pass (all verified live via CRW on 2026-08-31):

1. https://www.clay.com/guides/waterfall-enrichment — "The Complete Guide to Waterfall Enrichment (2026)" — Clay's 2025 work email benchmark showing no single provider clears both 95% quality and 90% coverage; cheapest-first waterfall reaches both
2. https://www.clay.com/guides/ideal-customer-profile — "The Complete Guide to ICP (2026)" — Signal-based ICP from closed-won vs closed-lost; four dimensions (firmographic floor, technographic, behavioral signals, product behavior); fit vs intent as separate axes
3. https://www.clay.com/guides/intent-data — "The Complete Guide to Intent Data (2026)" — Fit vs intent distinction; first-party vs third-party intent; signal types with freshness windows; custom signals as competitive moat
4. https://www.clay.com/guides/b2b-prospecting — "The Complete Guide to B2B Prospecting (2026)" — Volume vs targeted prospecting; 10k bought list → 4% actionable; data layer underneath (data, agents, orchestration, execution)
5. https://www.clay.com/guides/what-is-technographic-data — "What Is Technographic Data? (2026 Guide)" — Technographics as decisions not demographics; scraped vs install-base intelligence; four plays (displacement, integration-fit, scoring, personalization); HG Insights + waterfall
6. https://www.clay.com/guides/what-is-firmographic-data — "What Is Firmographic Data? (2026 Guide)" — Firmographics as least accurate category (mid-80s ceiling); gate on observable, score on inferred; waterfall + AI verification + scheduled refresh
7. https://www.clay.com/guides/how-to-find-work-email-address — "How to Find Work Email Addresses at Scale (2026)" — Corner pieces (name, domain, profile URL); waterfall across 100+ providers; free inference ~31%; catch-all validation modes; EU benchmarks; re-verification cadence
8. https://www.clay.com/guides/how-to-verify-email-addresses — "How to Verify Email Addresses (2026 Guide)" — Three checks (syntax, MX, SMTP); validation vs verification; catch-all problem (~5pt accuracy drop); waterfall verification; ZeroBounce 99.25% non-catch-all, Findymail 94.99% catch-all
9. https://www.clay.com/guides/how-to-build-a-targeted-prospect-list — "How to Build a Targeted Prospect List (2026)" — ICP definition first; signal stacking for sourcing; multi-thread contacts per deal complexity; waterfall enrichment; verify before load; fit x intent scoring
10. https://www.clay.com/guides/how-to-keep-crm-data-fresh — "How to Keep CRM Data Fresh Automatically (2026)" — Dynamic refresh list + job-change monitor + conditional write; ~3-5%/month decay; trust hierarchy; per-tier cadence
11. https://www.clay.com/guides/how-to-enrich-salesforce-records — "How to Enrich Salesforce Records (2026)" — Loop not one-time; filtered import; measure decay first; waterfall enrichment; verify gate; Update action on Record ID; dynamic list schedule
12. https://www.clay.com/guides/how-to-clean-and-standardize-crm-data — "How to Clean and Standardize CRM Data (2026)" — Inconsistent vs missing data; free deterministic normalizers first; canonical mapping with AI formulas; health scoring (Verified/Incomplete/Rotted); write-back on Record ID; entry-point standardization rule

### Skill improvements adopted

1. **Separate prospecting from enrichment as two distinct passes.** Prospecting finds net-new contacts matching the ICP from a blank list; enrichment completes records that already exist. Running them as one blurred step wastes budget.

2. **Enrich only the fields that predict conversion, and treat data as decaying.** B2B contact data decays ~22.5%/year and the average B2B professional changes jobs every ~18 months, so any record older than a quarter is suspect. Gartner puts poor data quality at ~$12.9M/yr average cost; IBM found 43% of COOs rank data quality their top data challenge and >25% of orgs lose >$5M/yr. Practice: anchor the enrichment schema to the ICP (revenue, headcount, industry, tech stack) rather than appending every available field, and stamp each record with a capture date + re-verify before outreach.

3. **Score on dynamic signals, not just static firmographics.** The highest-value layer is technographics + buying signals (funding rounds, hiring/job-post velocity, exec changes such as a new CRO, intent data) laid on top of static firmographic fields — these are what change the conversation. Practice: opportunity score = ICP fit (firmographic match) x signal recency (a signal in the last 30–90 days outranks a perfect-fit account with no event).

4. **Verification discipline for an AI sales team.** ~45% of business leaders cite data accuracy as a leading barrier to scaling AI; scoring models and AI-drafted outreach are only as good as the underlying records. Practice: never pass an unverified email/phone into an automated sequence — mark provenance (source + fetch date + verification method) on every enriched field, and prefer verified direct dials over inferred/pattern-guessed contacts.

5. **Rank first-party signals above purchased intent in every prospecting brief.** Before recommending any third-party intent vendor, I will first inventory the client's owned signal surfaces (CRM notes, reply text, call transcripts, product/usage logs, support tickets, web sessions) and build the scoring model on those. Third-party intent gets used only as a *coverage filler* for accounts with no owned signal — never as the primary ranking input, because a bought feed is by definition also in a competitor's hands.

6. **Treat enrichment as a continuous agent loop, not a one-shot waterfall.** New default deliverable: a re-check cadence (trigger-based monitoring for job changes, funding, tech installs, headcount deltas) that re-scores accounts and emits a play, rather than a static enriched CSV. Pair with cost control — route long-running/bulk research passes to cheap open-weight models and reserve premium calls for the final verification hop and for records that already cleared a signal threshold.

7. **Waterfall enrichment for coverage + accuracy.** Chain providers cheapest-first; stop at first confident result. No single provider wins both quality and coverage. Waterfall reaches coverage of all providers at accuracy of best one. Cost = path each record walks, not sum of stack. Order: cheapest confident provider first (runs on every record), broadest specialist last (catches long tail). Set confidence threshold strict for cold outreach.

8. **ICP built backward from closed-won, not forward from planning slide.** Export won/lost accounts, enrich on firmographics/technographics/signals, find attributes appearing far more in wins than losses. Four layers: firmographics (size, industry, revenue) set boundary; technographics (tools run) sharpen fit/timing; behavioral signals (funding, hiring, news) indicate intent; product behavior (usage thresholds) for PLG. Score fit and intent separately, then combine.

9. **Technographics = decisions, not demographics.** What a company runs reflects a purposeful decision with budget attached; size/industry rarely change. Two collection methods: scraped/pixel detection (fast/cheap, surface-only, goes stale) vs install-base intelligence (HG Insights: spend, contract terms, adoption timing, usage trends). Treat scraped as fit filter; install-base as action trigger. Waterfall: cheap detection first → escalate to install-base intelligence only for accounts you'll act on.

10. **Firmographics: gate on observable, score on inferred.** Industry/headcount/location = observable, safe to hard-filter. Revenue/growth stage = inferred, weight in scoring not gating. Best firmographic providers top out mid-80s accuracy; revenue hardest (best 88% accuracy at 42% coverage). Combine providers in waterfall + AI verification (Claygent) + schedule refresh.

11. **Email finding: corner pieces first.** Full name + company domain + professional profile URL = corner pieces unlocking waterfall. Domain matters most (providers use it to construct/verify). Waterfall across 100+ providers, free inference first (~31% coverage), then paid. Validate deliverability before shipping (catch-all domains = meaningful share; Findymail leads catch-all at 94.99% quality, 100% coverage, $0.30). EU: BetterContact (91% quality, 90% coverage). Re-verify every 30–60 days (~2–3%/month decay).

12. **Email verification: three checks (syntax → domain MX → mailbox SMTP).** Validation ≠ verification. Catch-all problem: verifiers can't distinguish real vs fake on accept-all domains (accuracy drops ~5pts). Waterfall verification cheapest-first. Gate every value before write; hold conflicts for review.

13. **CRM freshness loop: dynamic list + job-change monitor + conditional write.** Last Enrichment Date field → dynamic list filtered on age. Job changes = highest-value signal (champion left = hole; new hire = warm lead with budget in first 100 days). Monitor via LinkedIn URL. Conditional write: only overwrite if incoming value is fresher + more confident; trust hierarchy: rep-verified > high-confidence enrichment > monitor-flagged > stale source. Exclude manually maintained fields. Schedule per tier: active deals daily/weekly, target accounts weekly/monthly, general monthly/quarterly, closed-lost never.

14. **CRM cleaning: standardize first, enrich second.** Most "dirty CRM" = inconsistent data (same entity, 5 spellings), not missing data. Separate inconsistent from missing. Free deterministic normalizers (company name, phone, date, whitespace) before AI. Canonical mapping: decide single value per variant, map all to it (AI formula for judgment calls). Validate emails for deliverability, score health (Verified/Incomplete/Rotted), route by state. Write back keyed on CRM Record ID (Update action), test in sandbox first. Standardization rule at entry point so it stays clean.

### Updated Output Record (per lead)
- **Company** · **Industry** · **Location** · **Website** · **Employee Size** · **Technology Stack** · **Opportunity Score** (0–100, fit × signal recency)
- **Provenance**: source + fetch date + verification method per enriched field
- **Capture date** + **re-verify due date** (30–60 days for emails)
- **Signal stack**: active buying signals with timestamps (funding, hiring, technographic change, leadership change, first-party intent)
- **Fit/Intent breakdown**: separate fit score and intent score, not just blended

## Related

- [[02 - ORGANIZATION/Agents/Identity/Lead Qualification Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Lead Qualification Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/Identity/Lead Research Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Lead Research Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/Interviews/Lead Research Agent - Interview 2026-08-10.md|02 - ORGANIZATION/Agents/Interviews/Lead Research Agent - Interview 2026-08-10.md]]
- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
- [[02 - ORGANIZATION/Agents/Training/Lead Qualification Agent - Training.md|02 - ORGANIZATION/Agents/Training/Lead Qualification Agent - Training.md]]
- [[02 - ORGANIZATION/Agents/Training/Lead Research Agent - Training.md|02 - ORGANIZATION/Agents/Training/Lead Research Agent - Training.md]]
- [[02 - ORGANIZATION/Agents/Training/Marketing Lead - Training.md|02 - ORGANIZATION/Agents/Training/Marketing Lead - Training.md]]
- [[02 - ORGANIZATION/Agents/Verification Logs/Lead Research Agent - Verification Log 2026-08-05.md|02 - ORGANIZATION/Agents/Verification Logs/Lead Research Agent - Verification Log 2026-08-05.md]]
