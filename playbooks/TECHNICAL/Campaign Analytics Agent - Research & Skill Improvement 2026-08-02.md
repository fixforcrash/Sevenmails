---
type: Agent Training
status: active
tags: [02-organization]
---

# Campaign Analytics Agent - Research & Skill Improvement



## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

- Email sender guidelines (Google Workspace Admin Help) — https://support.google.com/a/answer/81126 — Gmail's binding sender requirements: SPF **or** DKIM for all senders; SPF **and** DKIM **and** DMARC for bulk senders (>5,000 msgs/day); valid forward+reverse DNS (PTR) records; TLS required for transmission (added Dec 2023); RFC 5322 message formatting; **spam rate in Postmaster Tools must stay below 0.30%**; From: header domain must be DMARC-aligned with the SPF or DKIM domain; marketing/subscribed mail must support one-click unsubscribe plus a visible unsubscribe link. Gmail From: header impersonation is met with DMARC quarantine enforcement. (verified live via CRW on 2026-08-03)
- Mailgun Deliverability blog hub — https://www.mailgun.com/blog/deliverability — Current practitioner guidance on inbox placement: BIMI as the payoff for solid authentication, why "email warm-up tools" are a false shortcut versus genuine reputation building, the argument that blocklisting is a symptom rather than the root problem, treating test sends as real sends (the inbox is not a sandbox), and the DMARCbis standardization status. Confirms deliverability analytics must be reputation-centric, not just open/click-centric. (verified live via CRW on 2026-08-03)
- **404 — recorded honestly, not fabricated:** https://www.twilio.com/docs/sendgrid/ui/sending-email/deliverability-metrics returned Twilio's "Error 404 — Oops! Page not found". Also https://www.mailgun.com/blog/deliverability/email-deliverability-metrics/ returned Mailgun's "Page not found". Neither page's content is represented above. The working Mailgun URL was resolved via `crw map` rather than slug guessing.

### Skill improvements adopted

1. **Treat the 0.30% Postmaster spam rate as the hard campaign KPI ceiling.** Report it alongside open/click rates in every campaign readout; a campaign that "performs" while drifting toward 0.3% is failing, not winning.
2. **Authentication posture is an analytics dimension.** Segment deliverability reporting by SPF/DKIM/DMARC alignment status and PTR/TLS validity — unexplained placement drops are usually alignment failures, not creative failures.
3. **Tier reporting by send volume.** Apply the >5,000/day bulk-sender rule set (SPF+DKIM+DMARC, one-click unsubscribe) as a distinct compliance checklist rather than a single blanket standard.
4. **Instrument one-click unsubscribe (RFC 8058) as a first-class metric.** Rising unsubscribe rate with a falling spam-complaint rate is a healthy signal, not a loss — score them as a pair.
5. **Discount reputation shortcuts in attribution models.** Warm-up-tool engagement and internal test sends both pollute engagement baselines; exclude them from A/B test populations and from cohort attribution.
6. **Verify URLs before citing.** Resolve real paths via `crw map` on a known landing page; log 404s explicitly instead of inferring content from a slug.

## Live Web Refresh (2026-08-05)

- Email sender guidelines (Gmail / Google Workspace Admin Help) — https://support.google.com/a/answer/81126 — Primary-source thresholds I must measure campaigns against: Postmaster Tools spam rate must stay **below 0.30%** (hard ceiling, not an average); senders >5,000 msgs/day to Gmail need SPF **and** DKIM **and** DMARC (p=none acceptable), valid forward+reverse DNS/PTR, TLS transport, RFC 5322 formatting, and one-click unsubscribe honored within 2 days. Gmail applies DMARC quarantine to From: header impersonation. (verified live via CRW on 2026-08-05)
- Strengthening Email Ecosystem: Outlook's New Requirements for High-Volume Senders (Microsoft Community Hub / Defender for Office 365 blog) — https://techcommunity.microsoft.com/blog/microsoft-defender-for-office-365-blog/strengthening-email-ecosystem-outlooks-new-requirements-for-highvolume-senders/4399730 — Outlook.com/Hotmail/Live now enforce SPF+DKIM+DMARC alignment for high-volume senders (>5k/day); non-compliant mail is routed to Junk and later rejected. Confirms deliverability requirements are now **multi-mailbox-provider**, so inbox-placement reporting must be segmented by receiving domain, not reported as one blended rate. (verified live via CRW on 2026-08-05)
- NOTE: mailgun.com/blog/deliverability/email-deliverability-metrics and twilio.com/en-us/blog/insights/email-deliverability-metrics both returned 404 on 2026-08-05 — dropped rather than cited. Always verify page title before trusting a scrape.

### Skill improvements adopted

1. **Segment every deliverability metric by receiving mailbox provider.** Gmail and Outlook now enforce different-but-parallel authentication regimes, so a single blended delivery/open rate hides provider-specific throttling. New default: break delivered / bounced / spam-complaint / open by recipient domain group (Gmail, Microsoft, Yahoo, other) in all campaign reports.
2. **Treat the 0.30% Postmaster spam rate as a hard guardrail metric, not a KPI.** Add it as a threshold alert alongside campaign KPIs; if a variant in an A/B test pushes spam rate toward 0.30%, kill the variant regardless of its open/click lift — deliverability damage outlasts the test win.
3. **Verify-before-cite discipline:** confirm page title in CRW output (2 of 4 candidate URLs were 404s this session) before recording any source.

## Web Access Standard

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

## Live Web Refresh (2026-08-31) — Campaign Analytics Knowledge Refresh

### Attribution Modeling & Unified Measurement
- **Source:** Kochava AIM (verified 2026-08-31 via Jina), Meta Robyn GitHub (verified 2026-08-31 via Jina), Rockerbox product pages (verified 2026-08-31 via Jina)
- Touch attribution unreliable due to privacy changes (iOS 14+, SKAdNetwork, cookie deprecation)
- Shift to **unified measurement triangle**: MTA (Multi-Touch Attribution) + MMM (Marketing Mix Modeling) + Incrementality Testing
- MTA tools: Rockerbox MTA, AppsFlyer
- MMM tools: 
  - Meta Robyn (open-source, Ridge regression, multi-objective evolutionary algorithm for hyperparameter optimization, time-series decomposition, gradient-based budget allocation)
  - Kochava AIM (SaaS, Bayesian + nonlinear regression, daily auto-update, targets 95%+ 2-week forecast accuracy, privacy-first aggregated market-level data)
  - Rockerbox MMM
- Privacy-first: aggregated market-level data, no user-level PII required

### Incrementality Testing
- **Source:** Rockerbox Testing (verified 2026-08-31 via Jina)
- Methods: geo-testing, difference-in-differences, randomized control trials
- Validates MTA and MMM results
- Key use cases: 
  - Brand SEM incrementality (organic vs paid)
  - Budget optimization
  - Resolving MTA vs MMM conflicts
  - Retail/wholesale channel impact (Amazon, major partners)
- Testing completes unified measurement triangle: MTA + MMM + Testing

### Marketing Mix Modeling (Next-Gen)
- **Source:** Kochava AIM product pages (verified 2026-08-31 via Jina)
- **Traditional MMM:** consultative/agency (manual, point-in-time, expensive, static) or in-house (Robyn, point-in-time, requires data scientist, static monthly/quarterly)
- **Next-gen SaaS MMM (Kochava AIM):** auto-updates daily, actionable data, low resources, cost-effective, designed for marketers
- Core methodology: Bayesian + nonlinear regression, continuous learning with incoming data
- Onboarding: ~4 weeks end-to-end
- Privacy: only aggregated market-level data, no user-level data

### A/B Testing & Statistical Significance
- **Source:** Evan Miller "How Not To Run an A/B Test" (verified 2026-08-31 via Jina)
- Fix sample size in advance: n = 16 * σ²/δ²
- Repeated significance testing (peeking) inflates false positives: peeking 10× makes reported 1% significance actually 5%
- Peeking table: 1 peek → need 2.9% reported for 5% actual; 10 peeks → need 1.0% reported for 5% actual
- Best practice: commit to sample size, no peeking until experiment complete
- Advanced: sequential design (Pocock group sequential) or Bayesian design for valid anytime stopping

### Cohort Analysis
- **Source:** Klaviyo Cohort Analysis blog (verified 2026-08-31 via Jina, published 2025-02-19)
- Groups by cohorting event (first purchase, SMS consent, email consent) and tracks reporting events over time
- Pre-built reports: post-purchase repeat rate, repeat purchases, SMS→first order, email→first order
- Customize by channel, product, timeframe, discount codes, double opt-in
- Exclusive to Marketing Analytics + Advanced CDP tiers (Klaviyo)

### Funnel & ROAS Optimization
- **Source:** Playbook existing knowledge (Gmail/Outlook deliverability requirements verified 2026-08-03, 2026-08-05)
- Funnel rates: sent → open → reply → positive reply → meeting → proposal → won
- ROAS optimization via channel mix optimization informed by MMM budget allocation
- Budget allocation: scenario planning with MMM (short/mid/long term), saturation curves, channel saturation points
- Deliverability KPI ceiling: Gmail Postmaster spam rate <0.30%, segment by provider (Gmail, Microsoft, Yahoo)
- Outlook.com/Hotmail/Live now enforce SPF+DKIM+DMARC alignment for >5k/day senders

### LTV/CAC
- Cohort analysis reveals repeat purchase patterns and time-to-conversion
- Compare performance across channels, products, timeframes
- Identify which strategies drive long-term revenue growth

### Skill improvements adopted (2026-08-31)

1. **Adopt unified measurement triangle (MTA + MMM + Incrementality Testing) as default framework** — no single method is sufficient in privacy-first era. Every campaign readout should reference which method(s) support the conclusion.

2. **Use next-gen SaaS MMM (Kochava AIM) as reference architecture** — daily auto-updating, Bayesian + nonlinear, 95% 2-week forecast accuracy, 4-week onboarding, privacy-first. This replaces static consultative/in-house MMM as the recommended approach.

3. **Enforce sample-size discipline in A/B testing** — no peeking. Calculate n = 16 * σ²/δ² upfront. If interim analysis needed, use sequential (Pocock) or Bayesian design; never stop early based on p-value.

4. **Segment all attribution/deliverability by mailbox provider** — Gmail (0.30% spam ceiling, SPF+DKIM+DMARC for bulk), Outlook (SPF+DKIM+DMARC for high-volume), Yahoo, other. Single blended rates hide provider-specific throttling.

5. **Treat incrementality testing as the validation layer** — geo-testing, diff-in-diff, RCTs validate MTA/MMM. Budget decisions should cite incrementality evidence, not just attributed ROAS.

6. **Verify URLs before citing; log 404s honestly** — multiple candidate URLs returned 404 this session (Segment, Airbyte, HBR, McKinsey, Optimizely, Rockerbox blog, Meta). Resolve real paths via `crw map` or Jina; drop 404s rather than inferring content.

## Related

- [[02 - ORGANIZATION/Agents/Identity/Analytics Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Analytics Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/Identity/Campaign Analytics Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Campaign Analytics Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/Identity/Campaign Manager Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Campaign Manager Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/Interviews/Analytics Agent - Interview 2026-08-10.md|02 - ORGANIZATION/Agents/Interviews/Analytics Agent - Interview 2026-08-10.md]]
- [[02 - ORGANIZATION/Agents/Interviews/Campaign Manager Agent - Interview 2026-08-10.md|02 - ORGANIZATION/Agents/Interviews/Campaign Manager Agent - Interview 2026-08-10.md]]
- [[02 - ORGANIZATION/Agents/Playbooks/Analytics Agent - Research & Skill Improvement 2026-08-02.md|02 - ORGANIZATION/Agents/Playbooks/Analytics Agent - Research & Skill Improvement 2026-08-02.md]]
- [[02 - ORGANIZATION/Agents/Playbooks/Campaign Manager Agent - Research & Skill Improvement 2026-08-02.md|02 - ORGANIZATION/Agents/Playbooks/Campaign Manager Agent - Research & Skill Improvement 2026-08-02.md]]
- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
