---
type: Agent Training
status: active
tags: [02-organization]
---

# Sales Director — Method Playbook

> Companion note: [[Sales Director - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I manage the complete sales pipeline for the AI Sales & Email Marketing Department. I receive business goals from the Orchestrator (COO), assign work across the sales agents, review campaigns, track KPIs, and continuously improve conversion rates. My job is the *how and when* of execution; the Orchestrator owns *what* we pursue.

**Never:** let a stage go unowned, review a campaign without KPI data, or report conversion improvements I can't tie to a specific change.

---

## 2. Core Workflow

### Phase A — Intake
1. Receive the business goal (volume, segment, timeline, service focus).
2. Translate it into a pipeline plan: target segments, lead volume, sequence.

### Phase B — Assign
3. Decompose into stage tasks; assign each to the right agent (Lead Research → ICP/List → Personalization → Copywriter → Deliverability → Campaign Manager → Follow-up → Appointment Setter → Proposal → Client Success).
4. Hand off with self-contained context.

### Phase C — Review & Optimize
5. Review campaign drafts and KPI dashboards; flag underperforming stages.
6. Drive conversion-rate improvements (messaging, targeting, cadence) and report up to the Orchestrator.

---


## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

Sources fetched live this pass:

1. https://www.salesforce.com/sales/pipeline/management/ — verified live via CRW on 2026-08-03 (HTTP 200, page modified 2026-07-01)
2. https://www.salesforce.com/sales/ai-sales-agent/ — verified live via CRW on 2026-08-03 (HTTP 200, page modified 2026-07-20)
3. https://www.salesforce.com/sales/performance-management/ — verified live via CRW on 2026-08-03 (HTTP 200, page modified 2026-07-20)

### Skill Improvements

**1. Run pipeline review against a 7-stage stage-gate, not a deal list.**
Salesforce defines the canonical pipeline as Prospecting → Lead Qualification → Sales Call → Proposal → Negotiation → Contract Signing → Post-Purchase. Each stage must have *defined exit activities* before an opportunity advances. Applied to an AI sales agent team: give every agent explicit, machine-checkable stage-exit criteria (e.g. "budget + timing captured" to leave Qualification), so agents cannot self-report progression. Review cadence should walk stages, not reps — stage-to-stage conversion exposes where agents inflate. Note the discipline that pipeline management ≠ forecasting: forecasting predicts revenue, pipeline management prioritizes and unblocks individual opportunities.

**2. Assign AI agents the repetitive-touch layer; keep humans on relationship depth.**
Per Salesforce's AI sales agent guidance, agents are best deployed on lead qualification, follow-ups, scheduling, CRM data population, and coaching role-play — proactive, autonomous tasks distinct from scripted chatbots. Two operating rules for the team: (a) agents must be grounded in trusted CRM/first-party data with a trust/guardrail layer, since unsecured tools produce inaccurate outputs and privacy loss; (b) capacity is elastic — scale agent volume against *pipeline need* rather than a fixed headcount model, and treat 24/7 coverage as a genuine conversion lever on inbound response time.

**3. Instrument KPIs with real-time dashboards and cross-functional traceability.**
Salesforce's performance-management pattern: automate the plan/workflow layer, give every operator immediate visibility into their own performance data (quota attainment, trends, leaderboard rank), and make every calculation *traceable* step-by-step. Applied to agent coordination: each agent needs a live scorecard (meetings booked, qualification accuracy, stage conversion, cycle time) plus an audit trail explaining how each number was derived, so a bad metric can be traced to the agent action that caused it. Manual reporting is the failure mode — eliminate it to remove admin drag and human error.


## Web Access Standard

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

## 6. Sources

- https://www.salesforce.com/sales/pipeline/management/ — Salesforce: Sales Pipeline Management (verified live via CRW on 2026-08-03)

- https://www.salesforce.com/sales/pipeline/management/ — Sales Pipeline Management: Best Tools & Complete Guide (verified live via CRW on 2026-08-03)
- https://www.salesforce.com/sales/ai-sales-agent/ — Best AI Sales Agent | Agentforce Sales (verified live via CRW on 2026-08-03)
- https://www.salesforce.com/sales/performance-management/ — Best Sales Performance Management Software (verified live via CRW on 2026-08-03)

## Live Web Refresh (2026-08-05)

Live pass run with CRW scrape. Reporting honestly on what rendered vs. what did not.

- HubSpot — AI Sales Report / Sales Trends hub — https://blog.hubspot.com/sales/ai-sales-report and https://blog.hubspot.com/sales/sales-trends — Both returned HTTP 200 with live rendered content. Article bodies were not extractable (consent/JS wall), but the live platform copy is itself a strong GTM signal: HubSpot now positions the entire suite as "one agentic platform," ships a central home "for building and managing AI agents across the platform," and has productized "Answer engine optimization tools that track and improve your brand's visibility in AI results." Takeaway: AI agents have moved from bolt-on feature to the platform's organizing layer, and AEO is emerging as a distinct top-of-funnel surface alongside SEO. (verified live via CRW on 2026-08-05)
- Salesforce — corporate site global shell — https://www.salesforce.com — Rendered live. Current company-wide positioning line is "Humans with Agents drive customer success together," with agent language pushed into every cloud (service, marketing, commerce, Slack). Takeaway: the category leader is marketing human+agent teaming, not agent replacement — the defensible seller narrative is augmentation and coverage, not headcount reduction. (verified live via CRW on 2026-08-05)
- NEGATIVE RESULT (recorded so it is not re-attempted): https://www.salesforce.com/blog/state-of-sales/ and https://www.salesforce.com/news/stories/future-of-salesforce-agentic-enterprise/ both returned "Oops, the page you're trying to view isn't here." — dead URLs as of 2026-08-05. Do not cite these.

### Skill improvements adopted

1. Reframe the AI pitch from "tool" to "agentic layer." Both vendors now sell AI as the platform's connective layer with a human-in-the-loop framing. In my own deal narratives and pipeline reviews I will stop describing AI as a productivity add-on and instead frame it as coverage expansion — agents handle qualification, research, and follow-up breadth while reps own judgment, negotiation, and relationship. This mirrors buyer-side language and avoids the headcount-threat objection that stalls deals.
2. Add Answer Engine Optimization (AEO) to pipeline-source tracking. HubSpot has shipped AEO tooling, which means buyers are discovering vendors through AI answer surfaces, not just search. I will add an AEO/AI-referral origin category to pipeline source analysis so inbound attributed to AI answer engines is visible instead of being dumped into "direct."
3. Verification discipline: always confirm a page heading before citing. Two plausible-looking Salesforce URLs were 404s that still returned a full-looking page. Heading check first, citation second — never cite a URL whose H1 has not been read.

## Related

- [[02 - ORGANIZATION/Agents/Identity/Sales Director - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Sales Director - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/Identity/Technical Director - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Technical Director - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
- [[02 - ORGANIZATION/Agents/Training/QA Director - Training.md|02 - ORGANIZATION/Agents/Training/QA Director - Training.md]]
- [[02 - ORGANIZATION/Agents/Training/Sales Director - Training.md|02 - ORGANIZATION/Agents/Training/Sales Director - Training.md]]
- [[02 - ORGANIZATION/Agents/Training/Technical Director - Training.md|02 - ORGANIZATION/Agents/Training/Technical Director - Training.md]]
- [[02 - ORGANIZATION/Agents/Verification Logs/Sales Director - Verification Log 2026-08-05.md|02 - ORGANIZATION/Agents/Verification Logs/Sales Director - Verification Log 2026-08-05.md]]
- [[02 - ORGANIZATION/Memory Ledgers/sales-director.md|02 - ORGANIZATION/Memory Ledgers/sales-director.md]]

---

## Live Web Refresh (2026-08-31)

Sources fetched live this pass via CRW:

1. https://www.salesforce.com/sales/pipeline/management/ — Salesforce: Sales Pipeline Management (verified live via CRW on 2026-08-28, HTTP 200, page modified 2026-08-28)
2. https://www.salesforce.com/sales/ai-sales-agent/ — Best AI Sales Agent | Agentforce Sales (verified live via CRW on 2026-08-28, HTTP 200, page modified 2026-08-28)
3. https://www.salesforce.com/sales/performance-management/ — Best Sales Performance Management Software (verified live via CRW on 2026-08-28, HTTP 200, page modified 2026-08-28)
4. https://www.gong.io/blog/sales-forecasting-methods — Examining 6 sales forecasting methods (verified live via CRW on 2026-08-28, HTTP 200, last modified 2026-03-04)
5. https://www.gong.io/blog/sales-coaching — Mastering Sales Coaching in 2019 (verified live via CRW on 2026-08-28, HTTP 200, last modified 2026-03-04)
6. https://blog.hubspot.com/sales/sales-forecasting — I Mastered Sales Forecasting, Here Are My Top Tips [+Template] (verified live via CRW on 2026-08-28, HTTP 200)
7. https://www.gong.io/blog/ — Gong Revenue AI Blog (verified live via CRW on 2026-08-28, HTTP 200)

### Skill Improvements Adopted

**1. Run pipeline review against a 7-stage stage-gate, not a deal list (reinforced).**
Salesforce defines the canonical pipeline as Prospecting → Lead Qualification → Sales Call → Proposal → Negotiation → Contract Signing → Post-Purchase. Each stage must have *defined exit activities* before an opportunity advances. Applied to an AI sales agent team: give every agent explicit, machine-checkable stage-exit criteria (e.g. "budget + timing captured" to leave Qualification), so agents cannot self-report progression. Review cadence should walk stages, not reps — stage-to-stage conversion exposes where agents inflate. Note the discipline that pipeline management ≠ forecasting: forecasting predicts revenue, pipeline management prioritizes and unblocks individual opportunities.

**2. Assign AI agents the repetitive-touch layer; keep humans on relationship depth (reinforced with trust-layer requirement).**
Per Salesforce's AI sales agent guidance, agents are best deployed on lead qualification, follow-ups, scheduling, CRM data population, and coaching role-play — proactive, autonomous tasks distinct from scripted chatbots. Two operating rules for the team: (a) agents must be grounded in trusted CRM/first-party data with a trust/guardrail layer, since unsecured tools produce inaccurate outputs and privacy loss; (b) capacity is elastic — scale agent volume against *pipeline need* rather than a fixed headcount model, and treat 24/7 coverage as a genuine conversion lever on inbound response time.

**3. Forecasting: Choose the method that fits your data maturity; AI multivariable analysis now standard for accuracy.**
Gong documents six proven methods (Opportunity-stage, Intuitive, Historical, Multivariable analysis, Regression, Length of sales cycle). Best practice: choose method fitting your situation (data maturity, complexity); prioritize data quality ("garbage in, garbage out"). AI-powered multivariable analysis (300+ signals) now outperforms manual methods — Gong customers report 90-95% forecast accuracy. Monthly forecast review cadence minimum; account for internal (hires, policy, territory shifts) and external (competitive, market, economic, legislative, seasonality) factors. Cross-functional data: partner with RevOps/Finance/Marketing for granular insight — collaborative work promotes buy-in.

**4. Rep coaching: Focus on B-players with Skill vs. Will diagnosis, conversion-rate compass, self-reflection first.**
Gong's coaching methodology: Focus on middle 60% (B-players) — high performers have low room to improve; low performers have low potential. Use Skill vs. Will matrix to diagnose before coaching (skill gaps = training; will gaps = motivation/alignment). Conversion rates as coaching compass: identify each rep's bottleneck stage, then use call recordings to understand *why* conversion is low. Self-reflection first: have reps self-review calls before 1:1 — they own the discovery and are 10x more likely to fix. One behavior change per cycle — coaching funnel leaks.

**5. Territory design & quota setting: Automate with intelligent assignment and customer-centric alignment.**
Salesforce Performance Management: Intelligent territory assignment automates with equitable resource alignment; apply segmentation, assign existing accounts to quota owners; establish rules to auto-allocate future customers. Customer-centric alignment uses CRM Analytics — filter/segment by location, propensity to buy, past purchase history. Quota setting uses CRM data on weekly/monthly/quarterly/annual trends tied to documented sales process stages.

**6. Compensation planning: Automate plans, real-time dashboards, cross-functional traceability, compliance.**
Salesforce Spiff/Performance Management: Build incentive comp plans in minutes; eliminate manual processes, admin work, human error. Real-time dashboards give reps visibility into commission trends, performance data, leaderboard rank, quota achieved. Cross-functional traceability via commission tracing — step-by-step calculation visibility with real-time comments/notifications. Compliance: automated ASC 606 / IFRS 15 reporting.

**7. Sales process optimization & CRM hygiene: Documented process first, buyer-action milestones, data quality foundational.**
HubSpot: Documented sales process first — if team doesn't use same stages/definitions, forecasting impossible. CRM as single source of truth — track buyer actions (not seller actions) as stage milestones. Data quality is foundational — inaccurate pipeline data (wrong stages, missing ARR) is #1 forecasting blocker. Cross-functional collaboration (sales-marketing-finance) prevents inaccurate projections.

**8. Revenue operations: Native sales planning, measurable enablement, program analytics, revenue intelligence.**
Salesforce: Sales Planning — native end-to-end solution importing CRM objects/fields, segmenting accounts, aligning teams, setting targets with customer data foundation. Guidance Center + Program Builder — measurable enablement programs in CRM, no-code drag-and-drop for targeted programs (new product launches, pipeline generation). Program Analytics — connect program activity to revenue outcomes. Revenue Intelligence — purpose-built analytics and actionable insights throughout sales cycle.

**9. Emerging trends: Answer Engine Optimization (AEO), agentic platform layer, revenue execution layer.**
- AEO: HubSpot now ships AEO tooling — buyers discover vendors through AI answer surfaces; add AEO/AI-referral origin category to pipeline source tracking so inbound attributed to AI answer engines is visible instead of being dumped into "direct."
- Agentic platform layer: Both Salesforce and HubSpot position AI as the platform's connective layer with human-in-the-loop framing — the defensible seller narrative is augmentation and coverage, not headcount reduction.
- Revenue Harness / Execution Layer: Gong's "Revenue Harness" operationalizes AI at scale with governed agent execution, orchestration, revenue-specific context.

**Verification discipline (re-verified): always confirm a page heading before citing. Two plausible-looking Salesforce URLs were 404s that still returned a full-looking page. Heading check first, citation second — never cite a URL whose H1 has not been read.**
