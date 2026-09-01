---
type: Agent Training
status: active
tags: [02-organization]
---

# ICP & List Building Agent — Method Playbook

> Companion note: [[ICP & List Building Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I define who we sell to and turn researched leads into clean, prioritized, de-duplicated prospect lists. I define the ideal client profile (driven by our services: Google Workspace, Microsoft 365, email migrations, DNS, SPF/DKIM/DMARC, email deliverability), build prospect lists, segment industries, prioritize high-value leads, remove duplicates, and qualify prospects.

**Never:** hand off a list with duplicate domains; qualify a prospect without a verifiable decision-maker or need signal.

---

## 2. Core Workflow

### Phase A — Define ICP
1. Take the ICP definition and raw leads from the Lead Research Agent / Sales Director.
2. Segment by industry and fit (SaaS, Agencies, Law Firms, Healthcare, Manufacturing, E-commerce).

### Phase B — Build & Clean
3. Score and prioritize high-value leads (ICP fit + Opportunity Score + intent signals).
4. De-duplicate (same domain/company across sources).

### Phase C — Qualify & Handoff
5. Qualify each prospect; pass clean lists to Personalization → Copywriter.

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

1. ZoomInfo — *What Is an Ideal Customer Profile? ICP Guide for B2B* — https://pipeline.zoominfo.com/marketing/ideal-customer-profile — verified live via CRW on 2026-08-03
2. HubSpot — *Lead Scoring Explained: How to Identify and Prioritize High-Quality Prospects* — https://blog.hubspot.com/marketing/lead-scoring-instructions — verified live via CRW on 2026-08-03
3. HubSpot — *Customer Segmentation: How to Segment Users & Clients Effectively* — https://blog.hubspot.com/service/customer-segmentation — verified live via Jina on 2026-08-03

**Skill improvements adopted**

1. **Separate account-level ICP from person-level persona, and gate list building on ICP first.** ICP answers "which companies should we talk to at all"; persona answers "how do we talk to people inside them." Build every list by qualifying the *account* first (firmographics + technographics + budget/use-case fit), then attach contacts. This kills the most common failure mode: right person, wrong company. Add psychographic/environmental filters that predict *ability* to buy — risk tolerance, regulatory bar, expansion vs. consolidation stage — since these often beat revenue band as a qualifier.

2. **Score on two independent axes — Fit and Interest — never one blended number.** Fit = firmographic/technographic/ICP match (explicit data). Interest = behavioral/intent signals (page views, pricing-page hits, demo requests, email/social engagement, source quality with referrals weighted highest). A high-fit/low-interest account is a nurture target; low-fit/high-interest is a time sink. Prioritize the list by Fit × Interest quadrant, not a single 0–100 score. Refresh the ICP quarterly and immediately on trigger events (new product, churn in a formerly strong segment, win/loss pattern shift) — an ICP older than six months is likely misaligned.

3. **Bake negative scoring and spam detection into dedup/hygiene as a first-class list-cleaning step.** Deduct or drop on: free-mail domains (gmail/yahoo) in a B2B list, uncapitalized name/company fields, keyboard-mash inputs (`asdf`, `999-999-9999`), and decayed engagement (stopped opening, stopped visiting). Enrich to fill gaps *before* dedup so records match on canonical company domain rather than free-text company name — de-duplication on enriched domain is what actually collapses duplicates. Turn the finished ICP into a Best-Fit / Good-Fit / Bad-Fit rubric written into CRM fields so every list is scored identically and reproducibly, rather than living in a slide deck.

## 6. Sources

- https://pipeline.zoominfo.com/marketing/ideal-customer-profile — ZoomInfo, ICP Guide for B2B (verified live via CRW on 2026-08-03)
- https://blog.hubspot.com/marketing/lead-scoring-instructions — HubSpot, Lead Scoring Explained (verified live via CRW on 2026-08-03)
- https://blog.hubspot.com/service/customer-segmentation — HubSpot, Customer Segmentation (verified live via Jina on 2026-08-03)


## Live Web Refresh (2026-08-05)

- How to Create an Ideal Customer Profile (ICP) With Template (Cognism) - https://www.cognism.com/blog/ideal-customer-profile - Confirms a 5-step ICP build loop: (1) identify "super users" from closed-won / high-retention accounts, (2) interview them, (3) analyse the data, (4) fill an ICP template, (5) refine continuously. Key firmographic axis called out explicitly: employee count / company size must reconcile with your total addressable market figure - ICP and TAM are one linked model, not two separate exercises. Buyer persona (person) is kept distinct from ICP (account). (verified live via CRW on 2026-08-05 - H1 plus full article headings returned)
- lemlist - Ideal Customer Profile guide plus product surface - https://www.lemlist.com/blog/ideal-customer-profile - Page serves live; article body is client-rendered so only the shell/IA was retrievable. What is legible is the 2026 vendor stack shape around ICP work: ICP-fit account identification -> verified contact enrichment -> intent-signal agents -> multichannel sequencing, with "Intent Signal Agents" and "Data Enrichment Agents" now sold as distinct agentic layers. Signal: technographic/intent enrichment has moved from a data field to an always-on agent step in the list-building pipeline. (verified live via CRW on 2026-08-05 - served 200, not a 404)
- Negative result worth recording: clay.com/blog/ideal-customer-profile, zoominfo.com/blog/ideal-customer-profile and userpilot.com/blog/ideal-customer-profile all returned 404 / "Not Found" / "Oops, you're lost!" on 2026-08-05. Vendor blog URLs recalled from memory are stale at a high rate. (verified live via CRW on 2026-08-05)

### Skill improvements adopted

1. Bind ICP to TAM in one artifact. Stop shipping an ICP doc and a TAM model separately. Every firmographic band I set (employee count, revenue, geo, industry) must be written with the account count it implies, so the ICP itself outputs TAM -> SAM -> SOM. If a band cannot be counted, it is not a usable ICP criterion.
2. Treat enrichment and intent as a pipeline stage, not a column. Restructure list-building runs as: fit filter (firmographic) -> technographic / install-base filter -> signal layer (hiring, funding, stack change, intent) -> contact verification -> sequence. The signal layer is recurring, not a one-time append at list creation.
3. Verify every citation URL before writing it. Three of five vendor blog URLs 404'd this session. Rule: CRW-scrape and confirm a real H1/title before a URL enters a playbook, deliverable, or source list.

## Live Web Refresh (2026-08-31)

**Sources fetched this pass**

1. ZoomInfo — *What Is an Ideal Customer Profile? ICP Guide for B2B* — https://pipeline.zoominfo.com/marketing/ideal-customer-profile — verified live via web_extract on 2026-08-31
2. HubSpot — *Lead Scoring Explained: How to Identify and Prioritize High-Quality Prospects* — https://blog.hubspot.com/marketing/lead-scoring-instructions — verified live via web_extract on 2026-08-31
3. Cognism — *How to Create an Ideal Customer Profile (ICP) With Template* — https://www.cognism.com/blog/ideal-customer-profile — verified live via web_extract on 2026-08-31 (published 2025-09-29, updated 2026-04-16)
4. Spanglobal Services — *B2B Intent Data Guide 2025: How to Identify Buyers Before Competitors* — https://www.spanglobalservices.com/blog/revenue-driven-marketers-guide-to-b2b-intent-data-in-2025/ — verified live via web_extract on 2026-08-31 (published 2025-09-19)
5. LeadMagic — *Waterfall Enrichment: Complete B2B Guide* — https://leadmagic.io/blog/waterfall-enrichment-guide — verified live via web_extract on 2026-08-31 (published 2026-07-30)
6. CheckNumber.ai — *Beyond the Raw List: A Framework for B2B Contact Data Hygiene* — https://checknumber.ai/blog/b2b-contact-list-hygiene — verified live via web_extract on 2026-08-31 (published 2026-08-10)
7. B2B Data Index — *Email List Hygiene: What It Is, Why It Matters, and How to Do It* — https://b2bdataindex.com/blog/email-list-hygiene-guide — verified live via web_extract on 2026-08-31 (published 2025-10-30)
8. Jay Mount Consulting — *The Data Waterfall: Multi-Provider Enrichment Methodology for B2B Teams* — https://jaymountconsulting.com/learn/courses/data-waterfall-clay — verified live via web_extract on 2026-08-31

**Skill improvements adopted**

1. **ICP ≠ Persona — strict separation.** ZoomInfo and Cognism both confirm: ICP is account-level (which companies), persona is individual-level (who to talk to, how to message). Build every list by qualifying the *account* first (firmographics + technographics + budget/use-case fit), then attach contacts. This kills the most common failure mode: right person, wrong company. Add psychographic/environmental filters that predict *ability* to buy — risk tolerance, regulatory bar, expansion vs. consolidation stage — since these often beat revenue band as a qualifier.

2. **Two-axis scoring — Fit × Interest — never one blended number.** HubSpot and ZoomInfo both support this. Fit = firmographic/technographic/ICP match (explicit data). Interest = behavioral/intent signals (pricing-page hits, demo requests, content consumption, competitor research, source quality with referrals weighted highest). A high-fit/low-interest account is a nurture target; low-fit/high-interest is a time sink. Prioritize the list by Fit × Interest quadrant, not a single 0–100 score. Refresh the ICP quarterly and immediately on trigger events (new product, churn in a formerly strong segment, win/loss pattern shift) — an ICP older than six months is likely misaligned.

3. **Bake negative scoring and spam detection into dedup/hygiene as a first-class list-cleaning step.** HubSpot explicitly calls this out. Deduct or drop on: free-mail domains (gmail/yahoo) in a B2B list, uncapitalized name/company fields, keyboard-mash inputs (`asdf`, `999-999-9999`), and decayed engagement (stopped opening, stopped visiting). Enrich to fill gaps *before* dedup so records match on canonical company domain rather than free-text company name — de-duplication on enriched domain is what actually collapses duplicates. Turn the finished ICP into a Best-Fit / Good-Fit / Bad-Fit rubric written into CRM fields so every list is scored identically and reproducibly, rather than living in a slide deck.

4. **Waterfall enrichment is the standard for contact coverage.** Single providers cover 40-70%; waterfall (2-3 providers) achieves 85-95% at lower cost per record. Orchestration: Clay, Apollo, Instantly, or custom (n8n/Make/Zapier). Provider order: highest-accuracy/real-time first (e.g., LeadMagic), fallbacks (Apollo, Hunter) on misses only — conditional, not parallel. Validate ONCE at the end — not inside each finder step (wastes credits, conflicting statuses). Catch-all resolution: 30-40% of B2B domains accept-all; resolve with specialized tool rather than discarding. Cost target: ~$0.05-0.12 per fully enriched validated contact vs $0.50-1.00 on static lists. Measure $/sendable contact, not $/lookup or raw match rate.

5. **Intent data is now a pipeline layer, not a column.** Spanglobal 2025 guide confirms: 80% of B2B sales interactions occur through digital channels in 2025 (up from 17% in 2023). Buyers conduct ~12 online searches before visiting a brand's website and are 60-90% through decision process by first contact. Intent data gives visibility into the hidden research phase. Types: first-party (website behavior, content downloads, email interactions) and third-party (publisher networks, review sites G2/TrustRadius/Capterra, social media, search behavior). Signal taxonomy: content consumption, search intent, technographic intent (stack changes), firmographic intent (growth/funding/leadership changes). Applications: ABM precision, sales timing, content strategy, competitive intelligence.

6. **List hygiene is continuous, not one-time.** B2B email lists decay ~22-25%/year (job changes primary driver); tech sector 50-65%/year (18-24 month median tenure). Pre-campaign: export → upload to NeverBounce/ZeroBounce/Bouncer → remove Invalid + Disposable → evaluate catch-all per risk tolerance → import. Ongoing: suppress hard bounces immediately; permanent suppression for unsubscribes; re-verify segments >90 days old; pause campaign if bounce rate >3% on first 200 sends. Thresholds: hard bounce <2% safe, spam complaint <0.1% safe.

7. **CRM integration requires reproducible scoring fields.** Write ICP fit tier (Best-Fit/Good-Fit/Bad-Fit) and Fit/Interest quadrant to CRM fields so every list is scored identically. Sync enriched contacts with source attribution (which provider found what). Handoff package: qualified list + qualification notes per high-value lead + ICP definition doc.

## Related

- [[02 - ORGANIZATION/Agents/Identity/ICP & List Building Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/ICP & List Building Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
- [[02 - ORGANIZATION/Agents/Training/ICP & List Building Agent - Training.md|02 - ORGANIZATION/Agents/Training/ICP & List Building Agent - Training.md]]
- [[02 - ORGANIZATION/Agents/Verification Logs/ICP & List Building Agent - Verification Log 2026-08-05.md|02 - ORGANIZATION/Agents/Verification Logs/ICP & List Building Agent - Verification Log 2026-08-05.md]]
- [[02 - ORGANIZATION/Memory Ledgers/icp-list-building-agent.md|02 - ORGANIZATION/Memory Ledgers/icp-list-building-agent.md]]
- [[02 - ORGANIZATION/Team Meta/Mnemosyne Compliance - ICP & List Building Agent.md|02 - ORGANIZATION/Team Meta/Mnemosyne Compliance - ICP & List Building Agent.md]]
- [[08 - KNOWLEDGE/Obsidian Wiki/wiki/concepts/graphrag.md|08 - KNOWLEDGE/Obsidian Wiki/wiki/concepts/graphrag.md]]
- [[17 - ARCHIVE/Knowledge Packages 2026-08-06/ICP & List Building Agent - Smoke Test 2026-08-06.md|17 - ARCHIVE/Knowledge Packages 2026-08-06/ICP & List Building Agent - Smoke Test 2026-08-06.md]]
