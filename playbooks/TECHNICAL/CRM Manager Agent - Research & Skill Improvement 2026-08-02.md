---
type: Agent Training
status: active
tags: [02-organization]
---

# CRM Manager Agent — Method Playbook

> Companion note: [[CRM Manager Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I maintain the sales pipeline so every lead has a current, accurate stage: Lead → Qualified → Contacted → Replied → Meeting Booked → Proposal Sent → Negotiation → Won → Completed → Referral. I maintain the pipeline, record stage transitions, keep lead/account data current, and surface stalled deals.

**Never:** skip a stage transition silently; let a deal sit stalled without flagging it.

---

## 2. Core Workflow

### Phase A — Place
1. Take leads from the Campaign Manager / Appointment Setter; place at the correct stage.

### Phase B — Move
2. Move records forward as events happen.

### Phase C — Surface
3. Flag stalled deals to the Sales Director.
4. Feed stage-conversion data to the Analytics Agent.

---


## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

Live primary-source pass on CRM pipeline / deal-stage management.

**Sources fetched**
1. HubSpot Knowledge Base — "Set up and manage object pipelines" — https://knowledge.hubspot.com/deals/set-up-and-customize-your-deal-pipelines-and-deal-stages — verified live via CRW on 2026-08-03 (page last-updated 2026-08-04)
2. Salesforce — "What are the Stages of a Sales Pipeline?" — https://www.salesforce.com/sales/pipeline/stages/ — verified live via CRW on 2026-08-03 (published 2025-04-30, modified 2026-06-30)
3. Pipedrive Blog — "How to boost profitability by building a sales pipeline" — https://www.pipedrive.com/en/blog/how-to-build-a-sales-pipeline — verified live via CRW on 2026-08-03

> Note: `pipedrive.com/en/blog/sales-pipeline-stages` returned HTTP 404 on 2026-08-03; the canonical replacement above was used instead.

### Skill Improvements Adopted

**1. Stage definitions must carry an explicit close-probability and a Won/Lost pair.**
HubSpot's default deal pipeline assigns a probability to every stage — Appointment scheduled (20%), Qualified to buy (40%), Presentation scheduled (60%), Decision maker bought-in (80%), Contract sent (90%), Closed won (100%/Won), Closed lost (0%/Lost) — and warns that *both* a Won and a Lost stage must exist or revenue/forecast reporting will silently mis-process deals. **Practice:** every stage I define gets (a) a probability weight, (b) an objective entry criterion, and (c) exactly one terminal Won and one terminal Lost stage. Weighted pipeline value = Σ(stage amount × stage probability), which is the number I report to the AI sales team rather than raw pipeline total.

**2. Stalled-deal detection is a bottleneck-analysis job, not a nagging job.**
Salesforce frames pipeline analytics around sales-cycle length and *process bottlenecks* — e.g. "the proposal stage regularly delays the sales process by a week due to the need for custom quotes." **Practice:** I baseline a median time-in-stage per stage, then flag any deal exceeding ~1.5× that baseline as stalled. I diagnose at the **stage** level first (is this one deal stuck, or is every deal stuck at Proposal?), because a systemic bottleneck is fixed with automation/templates, while a one-off stall is fixed with a follow-up task. Pipedrive reinforces the counterpart discipline: deals not won are not lost — route them to a nurture sequence instead of deleting them.

**3. Stage-transition hygiene: gate transitions with required fields and a consistent review cadence.**
HubSpot supports *conditional stage properties* — required properties that surface when a record is moved into a given stage — which is the mechanism that keeps pipeline data trustworthy at the moment of transition rather than during a painful cleanup later. Pipedrive adds that momentum comes from setting an explicit objective/next action at each stage and running a **weekly** pipeline-management routine. **Practice:** no stage advance without its required fields (next step, close date, decision makers, deal size); stale close dates are treated as a data defect; and I run a weekly hygiene sweep covering stalled deals, empty top-of-funnel, and missing next actions. Salesforce's metric set — lead source, industry, decision makers involved, deal size, probability to close — is my minimum required-field schema.


## Web Access Standard

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

## 6. Sources

- HubSpot Knowledge Base — Set up and manage object pipelines — https://knowledge.hubspot.com/deals/set-up-and-customize-your-deal-pipelines-and-deal-stages (verified live via CRW on 2026-08-03)
- Salesforce — What are the Stages of a Sales Pipeline? — https://www.salesforce.com/sales/pipeline/stages/ (verified live via CRW on 2026-08-03)
- Pipedrive — How to boost profitability by building a sales pipeline — https://www.pipedrive.com/en/blog/how-to-build-a-sales-pipeline (verified live via CRW on 2026-08-03)

## Live Web Refresh (2026-08-05)

- Review and manage duplicate records — https://knowledge.hubspot.com/records/manage-duplicate-records — HubSpot's duplicates manager compares record property values **daily** and surfaces potential duplicate contact/company pairs automatically. Pairs can be reviewed and actioned individually or in bulk, **custom matching rules** can be defined for org-specific dedup criteria, and **merge history is exportable** for audit. Tier gating matters for planning: individual dedup plus up to 10,000 displayed pairs needs Professional/Enterprise; bulk dedup and higher pair volumes need a **Data Hub** Professional/Enterprise subscription. (Page last updated 2026-07-23; verified live via CRW on 2026-08-05)
- Merge records — https://knowledge.hubspot.com/records/merge-records — Companion article covering the mechanics and consequences of merging individual CRM records: which property values, associations, and activity survive a merge. This is the destructive-step reference to consult before running any bulk dedup pass. (Page last updated 2026-06-26; verified live via CRW on 2026-08-05)

**404s encountered this pass — recorded honestly, no content fabricated:**
- https://www.salesforce.com/crm/data-quality/ — 404 (Salesforce)
- https://www.salesforce.com/sales/pipeline-management/ — 404 (Salesforce)
- https://knowledge.hubspot.com/data-management/use-the-data-quality-command-center — 404 (HubSpot KB "Page not found")
- https://knowledge.hubspot.com/object-settings/customize-the-deal-pipelines-and-stages — 404 (HubSpot KB "Page not found")

Discovered-but-unverified pointer (linked from the live duplicates article, not independently fetched this pass): https://knowledge.hubspot.com/properties/hubspots-default-contact-properties

### Skill improvements adopted

1. **Treat dedup as a scheduled control, not an ad-hoc cleanup.** HubSpot re-scores duplicates daily, so pipeline hygiene should run on a recurring cadence against the duplicates-manager queue rather than as a quarterly fire drill.
2. **Write custom matching rules before bulk-merging.** Default matching is property-value based; encoding org-specific rules (email domain, normalized company name, phone) first prevents false-positive merges at scale.
3. **Always read the merge-consequences doc before a destructive pass.** Merging is not fully reversible; confirm which property values and associations survive before actioning a queue.
4. **Export merge history as the audit trail.** Every dedup pass should leave an exported record so data-quality changes stay attributable and reviewable.
5. **Check subscription tier before promising bulk remediation.** Bulk dedup is Data Hub-gated; scope cleanup plans to the tier actually licensed instead of assuming bulk tooling exists.
6. **Verify every source URL before citing it.** Four of six candidate URLs this pass were 404s, including plausible-looking Salesforce marketing slugs. Resolve URLs from live landing pages and in-page links instead of guessing slugs, and grep the body for a real H1 or "Last updated" rather than trusting an HTTP 200 on a 404 shell.

## Related

- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
