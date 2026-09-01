---
type: Agent Training
status: active
tags: [02-organization]
---

# Campaign Manager Agent — Method Playbook

> Companion note: [[Campaign Manager Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I run outbound campaigns end to end: schedule outreach, organize sequences, coordinate follow-ups, and track responses. I manage campaigns, schedule outreach, organize sequences, coordinate follow-ups with the Follow-up Agent, pause/restart campaigns, and track responses (replies, bounces, unsubscribes).

**Never:** schedule sends against the Deliverability Agent's guidance; leave a spiking bounce rate unpaused.

---

## 2. Core Workflow

### Phase A — Assemble
1. Take copy (Copywriter) + send-readiness (Deliverability Agent) + sequences (Follow-up Agent).

### Phase B — Run
2. Schedule outreach against recommended sending windows.
3. Organize the sequence and hand follow-up generation to the Follow-up Agent.

### Phase C — Monitor
4. Monitor responses; pause on bounce/spam spikes, restart after fixes.
5. Report response metrics to Analytics; pipeline status to the Sales Director.

---


## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

Primary sources fetched live this pass:

1. https://knowledge.hubspot.com/sequences/create-and-edit-sequences — verified live via CRW on 2026-08-03 (page last updated 2026-08-03)
2. https://knowledge.hubspot.com/sequences/unenroll-from-sequence — verified live via CRW on 2026-08-03 (page last updated 2026-07-22)
3. https://knowledge.hubspot.com/sequences/analyze-sequence-enrollment-and-performance-data — verified live via CRW on 2026-08-03 (page last updated 2026-02-17)

### Skill Improvements

**1. Design sequences as mixed-channel step graphs, not email-only drips.**
A current sequence is a series of timed steps where each step is one of: automated email, manual email task, call task, general task, LinkedIn InMail task, or connection-request task. Delays between steps are configurable per step. For an AI sales team this means the campaign plan should be authored as an explicit step table (step # → channel → delay → template/owner), with automated emails carrying the volume and human/manual tasks reserved for high-intent accounts. Also decide per step whether the email *starts a new thread* or *replies to the previous sequence email* — thread continuation materially changes deliverability and reply context. Note the platform-level cap on total sequences per account: consolidate near-duplicate campaigns into one parameterized sequence rather than cloning.

**2. Treat pause/restart as trigger-driven unenrollment with an explicit trigger matrix.**
Unenrollment (the real "stop" signal) fires automatically on: reply to any sequence email, an inbound email from the enrolled address or an alias, reply from a *different* address, a colleague at the same company replying (if company-level unenroll is on), meeting booked via any sequence link, unsubscribe, hard bounce, workflow-driven unenroll, or sequence completion. Out-of-office replies generally do *not* unenroll — so OOO must be handled as a reschedule, not a stop. Critically: unenrolling does **not** recall already-sent mail, it only cancels future steps; and re-enrolling sends fresh emails, so on restart always pick the explicit resume step to avoid duplicate sends. Each trigger (reply / meeting) can be scoped to "the contact" or "all contacts at the company" — set company-scope for ABM plays, contact-scope for volume prospecting.

**3. Track a fixed response-metric set and act on "No response" and sender score.**
The per-sequence metric set to report on is: total enrollments, reply rate, meeting rate, **no-response rate** (enrollments that ended with zero reply), plus email engagement (open, click, bounce, unsubscribe) and company-level engaged/meeting rate; deal rate and influenced revenue where available. Filter performance by enroller and enrollment date so per-rep and per-cohort quality is visible — the default filter is "enrolled by me" and will silently hide team-wide data if left unchanged. Use bounce and unsubscribe rate as the throttling signal: rising bounce/unsub means pause enrollment and clean the list before adding volume, and monitor the sequence *sender score* as the standing quality gate.


## Web Access Standard

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

## 6. Sources

- https://knowledge.hubspot.com/sequences/create-and-edit-sequences — verified live via CRW on 2026-08-03
- https://knowledge.hubspot.com/sequences/unenroll-from-sequence — verified live via CRW on 2026-08-03
- https://knowledge.hubspot.com/sequences/analyze-sequence-enrollment-and-performance-data — verified live via CRW on 2026-08-03

## Live Web Refresh (2026-08-05)

Primary sources fetched live this pass:

1. https://knowledge.hubspot.com/campaigns/create-campaigns — verified live via CRW on 2026-08-05 (HubSpot Campaigns tool; real doc, "Create campaigns")
2. https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/core-marketo-concepts/smart-campaigns/understanding-smart-campaigns — verified live via CRW on 2026-08-05 (Adobe Marketo Engage; "Understanding Smart Campaigns"; page last updated May 13, 2026)
3. Salesforce Marketing Cloud — ATTEMPTED, NOT USED (recorded honestly): `https://developer.salesforce.com/docs/marketing/marketing-cloud/guide/journey-builder.html` returned an error page ("Oops / Something went wrong", not a valid doc); `https://help.salesforce.com/s/articleView?id=mktg_campaigns_overview.htm&type=5` returned the generic Salesforce Help search shell (popular searches: "summer '26 release notes"), not a campaigns article. Both 404/non-resolving — no fabrication; excluded as sources.

### Skill improvements adopted

**1. Model a campaign as an asset-container with explicit metadata, not just an email send.**
A HubSpot campaign groups multiple marketing assets (emails, blog posts, landing pages) under shared metadata: name, owner, audience, goal, budget, currency, start/end dates, and a campaign color. The dates drive the marketing calendar; the color tags associated tasks. Operating rule to carry forward: an asset (except workflows and lists) belongs to exactly ONE campaign — associating it elsewhere removes it from its prior campaign. Plan asset→campaign mapping deliberately so re-association doesn't silently orphan previous reporting.

**2. Use campaign templates + the HubSpot Connector for Claude as a setup force-multiplier.**
Standing campaign templates reduce per-campaign setup drift. The HubSpot connector for Claude can create campaigns, associate assets, and pull attribution data in-chat — wire the Campaign Manager agent to use the connector for hands-free creation/analysis rather than manual UI steps.

**3. Adopt the Marketo Smart Campaign model for lifecycle orchestration: Smart List + Flow + Schedule.**
Every automated play = three parts: (a) **Smart List** = WHO — filters qualify a static batch set at run time, triggers fire the flow immediately on a real-time action (e.g. "Clicks Link"); (b) **Flow** = ordered steps including Wait steps and split/choice branches; (c) **Schedule** = one-shot or recurring. Use triggers for hot-path reactions (reply, meeting booked) and filters for nurture waves. CRITICAL migration rule: when a Smart Campaign is moved between programs, referenced Smart List/Flow steps do NOT auto-update — always re-point them or enrollment logic silently breaks. Add this to the campaign hand-off/migration checklist.

**4. Separate batch vs trigger execution in the Monitor phase.**
Report trigger-fired campaigns (real-time) and batch-qualified campaigns (static set) as distinct execution modes so the Analytics agent can attribute outcomes correctly and so bounce/spam throttling is applied per mode.

## Live Web Refresh (2026-08-31)

Primary sources fetched live this pass:

1. https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/from-campaigns-to-continuous-growth-ai-capabilities-shaping-marketing — verified live via CRW on 2026-08-31 (McKinsey; "From campaigns to continuous growth: AI capabilities shaping marketing"; June 22, 2026)
2. https://knowledge.hubspot.com/campaigns/create-campaigns — verified live via CRW on 2026-08-31 (HubSpot; "Create campaigns"; last updated 2026-08-03)
3. https://knowledge.hubspot.com/campaigns/analyze-campaigns — verified live via CRW on 2026-08-31 (HubSpot; "Analyze individual campaign performance"; last updated 2026-08-03)
4. https://experienceleague.adobe.com/en/docs/marketo/using/product-docs/core-marketo-concepts/smart-campaigns/understanding-smart-campaigns — verified live via CRW on 2026-08-31 (Adobe Marketo Engage; "Understanding Smart Campaigns"; last updated May 13, 2026)
5. https://business.google.com/en-all/think/ — verified live via CRW on 2026-08-31 (Think with Google; Marketing Research, Insights, and Trends)
6. https://business.google.com/en-all/think/measurement/ — verified live via CRW on 2026-08-31 (Think with Google; Marketing Analytics, Data, and Measurement)

### Skill improvements adopted

**1. Shift from campaign-era model to AI-first continuous growth engine (McKinsey, June 2026)**
The five capability pillars replacing discrete campaigns:
- **Continuous Insights** — real-time signal-to-decision loops; digital twins simulate consumer personas for campaign/pricing/product testing. New role: *Customer Wayfinder* synthesizes data, tests with synthetic audiences.
- **Scaled Creativity** — agentic content factories generating/testing/optimizing assets at scale; 2-5× creative productivity, 10-30% cost reduction, cycles from 6-10 weeks → same-day. New role: *Creative Guru* defines guardrails and drives concepting.
- **Hyperpersonalization** — 1:1 real-time experiences across channels; +15-20% CSAT, +5-8% revenue, -30% cost-to-serve. Requires clean data, real-time decision engines, RL optimization, offer-management system. New role: *Hyperpersonalization Architect* designs data models and AI capabilities.
- **Agentic Commerce** — marketing to AI agents; brands must be "consumable" by machines (structured content, credibility signals, consistently updated info). New role: *Agent Whisperer* ensures brand accuracy in AI systems.
- **Always-on Orchestration** — replaces campaign cycles with human–agentic teams; +30% marketing ROI, execution time 60-70% → 10-15%. New role: *Full-funnel Navigator* oversees entire marketing system.

**Operating rule to carry forward:** Campaign Manager must design for always-on continuous growth engine, not one-off discrete campaigns.

**2. HubSpot Campaigns as deliberate asset-containers (verified 2026-08-03/05)**
- Campaign metadata: name, owner, audience, goal, budget, currency, start/end dates, color (drives marketing calendar).
- **Asset ownership rule:** An asset (except workflows and lists) belongs to EXACTLY ONE campaign — associating it elsewhere removes it from its prior campaign. Plan asset→campaign mapping deliberately so re-association doesn't silently orphan previous reporting.
- Campaign templates + HubSpot Connector for Claude = setup force-multiplier (create campaigns, associate assets, pull attribution data in-chat).
- Performance metrics to track: ROI (formula: (revenue/attributed revenue/associated deal value - spend) / spend × 100), Revenue (Pro), Revenue Attribution multi-model (Enterprise), Influenced Contacts, Website Traffic (first/last touch), Contact Lifecycle Count/Cost, Asset Reports, Traffic by UTM source.

**3. Marketo Smart Campaign model for lifecycle orchestration (verified 2026-05-13)**
Three-part architecture per automated play:
- **Smart List** = WHO — filters qualify static batch at run-time; triggers fire flow immediately on real-time action (e.g. "Clicks Link")
- **Flow** = ordered steps including Wait steps and split/choice branches
- **Schedule** = one-shot or recurring
**CRITICAL migration rule:** When a Smart Campaign is moved between programs, referenced Smart List/Flow steps do NOT auto-update — always re-point them or enrollment logic silently breaks. Add to campaign hand-off/migration checklist.

**4. Mixed-channel sequence design as step graphs, not email-only drips (HubSpot Sequences, 2026)**
- Sequence = step graph where each step is: automated email, manual email task, call task, general task, LinkedIn InMail task, connection-request task.
- Delays between steps configurable per step.
- **Thread decision per step:** new thread vs reply to previous sequence email — materially changes deliverability and reply context.
- **Unenrollment triggers (auto-stop):** reply to any sequence email, inbound from enrolled address/alias, reply from different address, colleague at same company replies (if company-level unenroll on), meeting booked via sequence link, unsubscribe, hard bounce, workflow-driven unenroll, sequence completion.
- **OOO does NOT unenroll** — handle as reschedule, not stop.
- **Re-enrollment sends fresh emails** — on restart, always pick explicit resume step to avoid duplicate sends.
- **Scope triggers:** contact-level (volume prospecting) vs company-level (ABM plays).
- Platform cap on total sequences per account — consolidate near-duplicate campaigns into one parameterized sequence.

**5. Fixed monitoring metric set with explicit throttling signals**
Per-sequence metrics to report:
- Total enrollments, reply rate, meeting rate, **no-response rate** (enrollments ending with zero reply)
- Email engagement: open, click, bounce, unsubscribe
- Company-level engaged/meeting rate
- Deal rate and influenced revenue (where available)
- **Filter by enroller + enrollment date** (default "enrolled by me" hides team-wide data if unchanged)
- **Throttling signal:** rising bounce/unsubscribe rate → pause enrollment, clean list before adding volume
- **Standing quality gate:** monitor sequence *sender score*

**6. Execution mode separation (batch vs trigger)**
Report trigger-fired campaigns (real-time) and batch-qualified campaigns (static set) as **distinct execution modes** so Analytics can attribute outcomes correctly and bounce/spam throttling is applied per mode.

**7. Attribution & incrementality evolution (2025-2026)**
- Move beyond last-touch: use data-driven multi-touch attribution (MTA) and Marketing Mix Modeling (MMM) in tandem.
- **Incrementality testing as ground truth:** Geo experiments (holdout regions), causal impact studies, platform lift studies (Meta GeoLift, Google Causal Impact).
- Attribution models = directional; incrementality tests = causal validation for budget allocation decisions.
- Cross-channel attribution requires unified identity resolution and consistent UTM taxonomy across all paid/owned/earned touchpoints.

## Related

- [[02 - ORGANIZATION/Agents/Identity/Campaign Analytics Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Campaign Analytics Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/Identity/Campaign Manager Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Campaign Manager Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/Interviews/Campaign Manager Agent - Interview 2026-08-10.md|02 - ORGANIZATION/Agents/Interviews/Campaign Manager Agent - Interview 2026-08-10.md]]
- [[02 - ORGANIZATION/Agents/Playbooks/Campaign Analytics Agent - Research & Skill Improvement 2026-08-02.md|02 - ORGANIZATION/Agents/Playbooks/Campaign Analytics Agent - Research & Skill Improvement 2026-08-02.md]]
- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
- [[02 - ORGANIZATION/Agents/Training/Campaign Manager Agent - Training.md|02 - ORGANIZATION/Agents/Training/Campaign Manager Agent - Training.md]]
- [[02 - ORGANIZATION/Agents/Verification Logs/Campaign Manager Agent - Verification Log 2026-08-05.md|02 - ORGANIZATION/Agents/Verification Logs/Campaign Manager Agent - Verification Log 2026-08-05.md]]
- [[02 - ORGANIZATION/Memory Ledgers/campaign-analytics-agent.md|02 - ORGANIZATION/Memory Ledgers/campaign-analytics-agent.md]]
