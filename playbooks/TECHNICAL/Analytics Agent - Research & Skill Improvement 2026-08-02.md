---
type: Agent Training
status: active
tags: [02-organization]
---

# Analytics Agent — Method Playbook

> Companion note: [[Analytics Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I measure the sales pipeline and tell the team what to change. I track open rate, reply rate, positive reply rate, meetings booked, closed deals, revenue, ROI, and A/B testing results — then recommend improvements (messaging, targeting, cadence, segments).

**Never:** report a funnel rate I can't tie to source data; declare an A/B winner without reasonable significance.

---

## 2. Core Workflow

### Phase A — Pull
1. Pull metrics from the Campaign Manager (sends/replies), CRM Manager (stage conversions), Finance Agent (revenue/ROI).

### Phase B — Compute
2. Compute funnel rates (open → reply → positive → meeting → proposal → won) and ROI per campaign/segment.
3. Read A/B results from the Copywriter's copy library; call a winner at reasonable significance.

### Phase C — Recommend
4. Recommend concrete improvements; feed learnings back to the relevant agent.
5. Report a dashboard + recommendations to the Sales Director.

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
- HubSpot — *Sales metrics: What to track, how to track, & why* — https://blog.hubspot.com/sales/sales-metrics — verified live via CRW on 2026-08-03 (HTTP 200, updated 2025-10-30)
- Optimizely — *Statistical significance* (optimization glossary) — https://www.optimizely.com/optimization-glossary/statistical-significance/ — verified live via CRW on 2026-08-03 (HTTP 200, related entries dated Jun 2026)
- lemlist — *Cold email benchmarks* — https://www.lemlist.com/blog/cold-email-benchmarks — verified live via Jina on 2026-08-03 (HTTP 200; body returned mostly nav/product shell, so used only for outbound-channel + deliverability framing, not for quoted benchmark numbers)

### Improvement 1 — Split the metric set into leading vs lagging, and always pair activity with outcome
HubSpot's set gives me the canonical formulas I should compute rather than eyeball:
- Conversion rate = won deals / total opportunities × 100
- Win rate = won opportunities / total opportunities × 100 (the "bellwether" — best single predictor of future growth, and the fastest way to spot pipeline bottlenecks)
- Average sales cycle = total days to close all deals / total deals
- Cost of selling (sales expense ratio) = cost of sales / total value of sales × 100
- % revenue from new business vs existing customers; YoY growth; CLV
**Change to my workflow:** in Phase B I now report a leading block (sends, opens, replies, positive replies, meetings) *next to* a lagging block (win rate, cycle length, revenue, CLV). No activity metric ships to the Sales Director without the outcome metric it is supposed to move — high reply rate with a flat win rate is a targeting problem, not a copy win.

### Improvement 2 — ROI framing must net out cost of selling, and new-logo revenue must be read against retention
Percentage-of-revenue-from-new-business is a growth signal but HubSpot is explicit that it must be read in parallel with retention/churn and revenue from existing customers. Likewise, campaign "ROI" that ignores the sales expense ratio flatters an AI outbound team, whose tooling/inference/list costs sit in cost of sales.
**Change to my workflow:** every campaign/segment ROI I publish carries (a) fully-loaded cost of selling for that campaign, (b) split of new vs existing-customer revenue, (c) CLV-adjusted value rather than first-contract value. A campaign that wins cheap logos with low CLV gets flagged, not celebrated.

### Improvement 3 — A/B significance discipline: pre-register, run a full business cycle, never peek
Optimizely's guidance for classical stats: set minimum detectable effect (MDE) and sample size *in advance*, don't peek at interim results, don't test many goals or variations at once. Report both p-value and confidence interval — not just "B won". Duration math: total visitors needed = sample size × number of variations; estimated days = total visitors needed ÷ average daily volume. Most tests fail to reach significance for three reasons I should pre-empt: the change is too small, the baseline conversion rate is too low, or the team tracked too many goals. Minimum run of one full business cycle (≥7 days) to absorb day-of-week effects. If results must be monitored continuously, use a sequential-testing/false-discovery-rate approach (Optimizely Stats Engine style) instead of repeatedly re-reading a fixed-horizon t-test.
**Change to my workflow:** before the Copywriter launches a variant I record hypothesis, primary metric, MDE, required sample per arm, and planned end date; I refuse to call a winner early, and I state p-value + CI + observed lift when I do call one. Randomised, balanced assignment across segments is a precondition — an all-one-segment split is not a valid test.

---

## 6. Sources

- https://blog.hubspot.com/sales/sales-metrics — HubSpot, "Sales metrics: What to track, how to track, & why" (verified live via CRW on 2026-08-03)
- https://www.optimizely.com/optimization-glossary/statistical-significance/ — Optimizely, "Statistical significance" (verified live via CRW on 2026-08-03)
- https://www.lemlist.com/blog/cold-email-benchmarks — lemlist, "Cold email benchmarks" (verified live via Jina on 2026-08-03)

## Live Web Refresh (2026-08-05)

- Google Analytics 4 — Analytics dimensions and metrics — https://support.google.com/analytics/answer/9143382 — Canonical GA4 dimension/metric reference. Key takeaways: dimensions/metrics are grouped into Attribution, Ecommerce, Event, Traffic source, User lifetime, Predictive, Revenue and Search Console families; most are populated from event parameters, so measurement-plan design (event + parameter naming) directly determines which reporting dimensions exist. `(not set)` means NO value was sent (an empty string renders blank instead) — a critical distinction when triaging attribution gaps. Dimension/metric pairs can be mutually incompatible and grey out in Explorations. (verified live via CRW on 2026-08-05)
- Google Analytics 4 — Get started with attribution — https://support.google.com/analytics/answer/10596866 — GA4 Attribution reports expose exactly three models: Data-driven attribution, Paid and organic last click, and Google paid channels last click. Credit is assigned to touchpoints along the path to a "key event" (GA4's replacement term for conversions). Important rule: all attribution models EXCLUDE direct visits from receiving credit unless the entire path is direct. Multi-touch reality (several searches/ad clicks before purchase) is the stated reason last-click alone understates upper-funnel spend. (verified live via CRW on 2026-08-05)
- HubSpot Knowledge Base — sales forecast tool — https://knowledge.hubspot.com/forecasting/forecast-your-sales-with-the-forecast-tool — NOT VERIFIED. CRW fetch returned HubSpot's "Looks like you've drifted off course." not-found page rather than article content. Slug appears to have moved or been retired. No content claimed from this source; needs re-resolution via the HubSpot KB landing page or `crw map` on a future pass. (attempted live via CRW on 2026-08-05, failed)

### Skill improvements adopted

1. **Treat `(not set)` as a signal, not noise.** When a GA4 traffic-source or campaign dimension shows `(not set)`, the parameter was never sent — that is a tagging/instrumentation defect to escalate, not a data-quality footnote. Blank ≠ `(not set)`.
2. **Never report a single attribution number.** Pull the same key event under Data-driven AND Paid-and-organic-last-click, and report the delta as the "last-click blind spot" for upper-funnel channels.
3. **Caveat direct traffic explicitly.** Because GA4 models exclude direct from credit (unless the path is all-direct), any channel ROI table must footnote that direct-assisted paths are redistributed to other touchpoints.
4. **Design the measurement plan before the dashboard.** Since GA4 dimensions derive from event parameters, agree the event+parameter schema with the sales/marketing owner first; retrofitting a dimension is impossible retroactively.
5. **Pre-check dimension compatibility** before building an Exploration — incompatible dimension/metric pairs grey out and silently break scheduled reports.
6. **Source-hygiene rule (process).** Vendor KB slugs rot fast. Resolve article URLs from a landing page or `crw map` rather than guessing; if a fetch returns a vendor's not-found page, log it as unverified rather than inferring content from the title.

## Live Web Refresh (2026-08-31)

**Sources fetched this pass** (all verified live via CRW on 2026-08-31)
- Google Analytics 4 — Analytics dimensions and metrics — https://support.google.com/analytics/answer/9143382 (HTTP 200)
- Google Analytics 4 — Get started with attribution — https://support.google.com/analytics/answer/10596866 (HTTP 200)
- Google Analytics 4 — About key events — https://support.google.com/analytics/answer/9267568 (HTTP 200)
- Google Analytics 4 — What the value (not set) means in your reports — https://support.google.com/analytics/answer/13504892 (HTTP 200)
- Google Analytics 4 — Funnel exploration — https://support.google.com/analytics/answer/9327974 (HTTP 200)
- Google Analytics 4 — Cohort exploration — https://support.google.com/analytics/answer/9670133 (HTTP 200)
- Google Analytics 4 — Path exploration — https://support.google.com/analytics/answer/9317498 (HTTP 200)
- Google Analytics 4 — Free-form exploration — https://support.google.com/analytics/answer/9327972 (HTTP 200)
- Google Analytics 4 — Select attribution settings — https://support.google.com/analytics/answer/10597962 (HTTP 200)
- Google Analytics 4 — Consent mode on websites and mobile apps — https://support.google.com/analytics/answer/9976101 (HTTP 200)
- Google Analytics 4 — About custom dimensions and metrics — https://support.google.com/analytics/answer/10075209 (HTTP 200)
- Google Analytics 4 — Traffic-source dimensions, manual tagging, and auto-tagging — https://support.google.com/analytics/answer/11242870 (HTTP 200)
- Google Analytics 4 — Apply segments and filters — https://support.google.com/analytics/answer/9328518 (HTTP 200)
- BigQuery — Introduction to SQL — https://cloud.google.com/bigquery/docs/introduction-sql (HTTP 200, redirected)
- BigQuery — Optimize query computation — https://cloud.google.com/bigquery/docs/best-practices-performance-compute (HTTP 200, redirected)
- Optimizely — Statistical significance — https://www.optimizely.com/optimization-glossary/statistical-significance/ (HTTP 200)

### Key Updates Adopted

1. **GA4 Attribution Models Reduced to Three** — First click, linear, time decay, and position-based models deprecated November 2023. Only Data-driven, Paid and organic last click, and Google paid channels last click remain. Must update any documentation or dashboards referencing deprecated models.

2. **Key Events Replace "Conversions"** — GA4 terminology shift: "key event" = action important to business success. Any event can be marked as key event in Admin > Events. Used for cross-channel attribution and Google Ads conversion creation.

3. **Traffic Source — UTM Exclusivity Rule** — Critical: if ANY UTM parameter is present on a URL, GA derives ALL cross-channel traffic source dimensions from UTMs exclusively. Missing UTMs → (not set) gaps. Must set all relevant UTMs (source, medium, campaign, id, source_platform) or accept attribution gaps.

4. **Consent Mode v2 Modeling** — Denied consent triggers cookieless pings with coarse dims (UA, screen res, IP for country only). GA uses conversion modeling + behavioral modeling to fill gaps. Best practice: load tags BEFORE consent dialog, region-specific defaults, don't gate tag loading on consent.

5. **BigQuery JOIN Optimization** — Order: largest table first, then smallest, then remaining by decreasing size. Reduce with GROUP BY before JOIN. Use materialized views for frequent queries. Search indexes with SEARCH function for row lookups.

6. **A/B Test Discipline (Optimizely Stats Engine)** — Pre-register hypothesis, primary metric, MDE, sample size per arm, planned end date. Run ≥1 full business cycle (7 days). Stats Engine combines sequential testing + FDR control — enables real-time monitoring without peeking penalties. Report p-value + CI + observed lift.

7. **GA4 Explorations as Dashboards** — Save funnel/cohort/path explorations as reports. Export: Google Sheets, TSV, CSV, PDF, PDF (all tabs). Anomaly detection built into line charts (Bayesian state space-time series model).

8. **Custom Dimensions — Event-Scoped Now Property-Wide** — No longer per-event quota consumption. Remove duplicates across events to preserve quota. Avoid high-cardinality (unique IDs, timestamps, session IDs) — condense to (other) row.

9. **Attribution Settings — Lookback Windows** — Acquisition key events (first_open, first_visit): 30-day default (7-day option). All other key events: 90-day default (30/60/90 options). Applies to session attribution too.

10. **(not set) = Instrumentation Defect** — When a dimension shows (not set), the parameter was never sent. Treat as tagging/instrumentation defect to escalate, not a data-quality footnote. Blank ≠ (not set).

## Related

- [[02 - ORGANIZATION/Agents/Identity/Analytics Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Analytics Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/Identity/Campaign Analytics Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Campaign Analytics Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/Interviews/Analytics Agent - Interview 2026-08-10.md|02 - ORGANIZATION/Agents/Interviews/Analytics Agent - Interview 2026-08-10.md]]
- [[02 - ORGANIZATION/Agents/Playbooks/Campaign Analytics Agent - Research & Skill Improvement 2026-08-02.md|02 - ORGANIZATION/Agents/Playbooks/Campaign Analytics Agent - Research & Skill Improvement 2026-08-02.md]]
- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
- [[02 - ORGANIZATION/Agents/Training/Analytics Agent - Training.md|02 - ORGANIZATION/Agents/Training/Analytics Agent - Training.md]]
- [[02 - ORGANIZATION/Agents/Verification Logs/Analytics Agent - Verification Log 2026-08-05.md|02 - ORGANIZATION/Agents/Verification Logs/Analytics Agent - Verification Log 2026-08-05.md]]
- [[02 - ORGANIZATION/Memory Ledgers/analytics-agent.md|02 - ORGANIZATION/Memory Ledgers/analytics-agent.md]]
