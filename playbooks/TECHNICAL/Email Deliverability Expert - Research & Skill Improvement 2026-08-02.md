---
type: Agent Training
status: active
tags: [02-organization]
---

# Email Deliverability Expert — Method Playbook

> **Refreshed 2026-08-31** by the Email Deliverability Expert (live CRW research). Updated from the 2026-08-03 version with new primary-source findings from Google, Yahoo, Microsoft, and industry sources.
> Companion note: [[Email Deliverability Expert - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I **get legitimate mail into the inbox and keep it there.** Deliverability in 2025–2026 is governed by three layers: (1) authentication — SPF, DKIM, DMARC, ARC, BIMI; (2) platform sender requirements — Google's, Yahoo's, Microsoft's, and Apple's bulk-sender rules; and (3) sender reputation and engagement. The work is part engineering (DNS records, MTA/ESP configuration), part strategy (list hygiene, content, cadence), and part continuous monitoring.

The 2026 shift that matters: **unauthenticated and non-compliant bulk mail is now rejected outright by Gmail, Yahoo, and Outlook rather than merely delayed**, and one-click unsubscribe (RFC 8058) is effectively mandatory for bulk senders. Reputation is earned per-domain and per-IP, so isolation and warm-up are non-negotiable. Gmail's enforcement escalated in **November 2025** from filtering to **temporary and permanent rejections** (5xx SMTP codes). Bulk-sender status at the primary domain level is **permanent once crossed** (5,000 msgs/day aggregate across all subdomains).

**Never:** send from unauthenticated domains, buy or rent lists, ignore spam complaints, mix promotional and transactional streams, or let a single shared-IP neighbor tank your reputation.

---

## 2. Core Workflow

### Phase A — Authenticate the Domain

1. **Publish SPF (TXT)** authorizing every sending source; keep the include chain **under 10 DNS lookups** to avoid `permerror`.
2. **Enable DKIM signing** on the MTA/ESP; use keys **≥2048-bit** and rotate on a quarterly schedule; align `d=` with the From-domain.
3. **Publish DMARC** starting at `p=none` with `rua` reporting, then progress to `quarantine`, then `reject` once alignment is verified.
4. **Confirm DMARC alignment** — the From-domain must align (SPF-enforced or DKIM-enforced) with the Organizational Domain.
5. **Deploy ARC (RFC 8617)** for any forwarding path or mailing-list service — Yahoo requires this.
6. **Publish BIMI** (with VMC) after reaching `p=quarantine` or `reject` for brand logo display in Gmail, Yahoo, Apple Mail, Fastmail.

### Phase B — Meet Bulk-Sender Requirements (Gmail, Yahoo, Outlook)

7. **Implement one-click unsubscribe** via the `List-Unsubscribe` header + `List-Unsubscribe-Post: List-Unsubscribe=One-Click` (RFC 8058), plus a visible in-body unsubscribe link. Honor within **24 hours** (Yahoo requires 2 days; aim for immediate).
8. **Keep the spam-complaint rate below 0.10%** (target); treat **>0.30%** (Gmail/Yahoo/Outlook hard ceiling) as a deliverability failure.
   - **Critical**: Yahoo computes spam rate on **inbox-delivered mail only** — normalize CFL data against *inbox* volume, not total sends.
9. **Enforce DMARC with aligned SPF/DKIM** for any domain sending >5,000 messages/day to Gmail. **Status is permanent** once the primary domain crosses the threshold (all subdomains aggregate).
10. **Use TLS on transmission** for *all* senders (Google requirement since Dec 2023) — verify with `openssl s_client -starttls smtp -connect mx:25`.
11. **Valid forward and reverse DNS (PTR)** on every sending IP — matching A/AAAA + PTR records.

### Phase C — Warm and Protect Reputation

12. **Warm up new IPs/domains** by ramping volume gradually over **4–8 weeks**, weighted toward most engaged recipients first.
    - Week 1: 50–500/day (last 30-day openers/clickers)
    - Week 2: 500–2,000/day (last 60–90-day engaged)
    - Week 3: 2,000–7,000/day (watch for Gmail/Outlook throttling)
    - Weeks 4–5: 7,000–30,000/day (full clean list)
    - Weeks 6–8: 30,000–100,000+/day (target volume)
    - **Golden Rule**: Send best content to best recipients first; consistent send time daily.
13. **Separate streams** — dedicated subdomains and/or IPs for transactional vs marketing vs system mail; never mix them.
    - Example: `tx.brand.com`, `news.brand.com`, `alerts.brand.com`
14. **Maintain list hygiene** — process bounces, enforce suppression lists, run a sunset policy for disengaged contacts.
    - Double opt-in preferred (15–25% conversion drop, 50%+ better long-term placement)
    - Sunset at **90 days** no engagement — re-engagement campaign or suppress
    - Validate imports (ZeroBounce, NeverBounce, MillionVerifier)
    - Remove hard bounces instantly; suppress soft bounces after 3 consecutive failures

### Phase D — Monitor and Tune

15. **Measure inbox placement** with seed-list testing (GlockApps, Validity/250ok) and process Feedback-Loop (FBL) complaints automatically.
    - Gmail FBL: requires `Feedback-ID` header (format: `a:b:c:SenderID` with 5–15 char SenderID) for campaign-level granularity
    - Yahoo CFL: DKIM-domain enrollment via Sender Hub; ARF reports
    - Microsoft: SNDS (IP reputation) + JMRP (individual ARF complaints) via unified portal
16. **Review dashboards weekly** — **Google Postmaster Tools v2 Compliance Status dashboard first** (Google's own verdict on requirements), then Spam Rate, Authentication, Delivery Errors, Feedback Loop; Microsoft SNDS; Yahoo Sender Hub; DMARC aggregate reports.
17. **Investigate reputation drops immediately** — isolate the offending stream, pause it, and remediate before resuming.
    - Diagnostic order: Authentication (mail-tester.com 9+/10) → Postmaster Compliance → Bounce spike → Complaint >0.3% → Blocklist → Infra changes → Content changes → Forwarder anomalies

### Phase E — Persist

18. **Write deliverability decisions and SOPs to the Obsidian Vault, then re-read the file** (verify-after-write). Persist durable conventions (subdomain policy, DMARC rollout state, warmup schedule, compliance checklist) to Mnemosyne (`mnemosyne store`).

---

## 3. Recommended Tools

| Tool | What it's for | When to use |
|---|---|---|
| MTA / ESP (Postfix, Microsoft 365, Google Workspace, SendGrid, Amazon SES, Postmark) | Sending platform with DKIM signing & reputation controls | Baseline for any outbound program |
| SPF/DKIM/DMARC validators (MXToolbox, DMARCian, Google Admin Toolbox) | Validate records, lookups, and alignment | Before first send and after every DNS change |
| **Google Postmaster Tools v2** | **Compliance Status (primary), Gmail reputation, spam rate, domain/IP metrics, FBL** | **Any program sending bulk mail to Gmail — check Compliance Status first** |
| Microsoft SNDS / JMRP | Outlook IP reputation, complaint ARF reports | Any program sending to Outlook/Hotmail/Live |
| Yahoo Sender Hub / CFL | Yahoo reputation, ARF complaints | Any program sending to Yahoo/AOL |
| DMARC report analyzers (Postmark, Dmarcian, Valimail) | Parse `rua`/`ruf` XML aggregate reports | Ongoing DMARC monitoring after `p=none`+ |
| Seed-list / inbox-placement (GlockApps, Validity/250ok) | Measure inbox vs spam folder placement | Pre-launch validation and periodic audits |
| List verification (ZeroBounce, NeverBounce, MillionVerifier) | Reduce bounces, clean imports | List import, re-engagement, and sunset decisions |
| mail-tester.com | Comprehensive auth/content/blacklist test | Quick diagnostic — expect 9+/10 |

---

## 4. Current Best Practices (2025–2026)

- **Authentication is the floor, not the goal:** SPF + DKIM + DMARC enforced at `reject` for every sending domain.
- **One-click unsubscribe is mandatory** for bulk mail (RFC 8058); Gmail, Yahoo, Outlook treat its absence as a compliance failure.
- **Keep complaint rate under 0.10%**; anything approaching 0.30% triggers throttling or rejection.
- **Separate subdomains/IPs** for transactional vs promotional traffic — never co-mingle.
- **Warm up cold IPs/domains gradually** over 4–8 weeks; do not blast from a new reputation.
- **Monitor DMARC aggregate reports and Gmail Postmaster continuously**, not quarterly. **Compliance Status dashboard is the new primary artifact.**
- **List hygiene beats volume:** suppress hard bounces instantly, honor unsubscribes in real time, sunset the disengaged at 90 days.
- **Align your From-domain** so DMARC passes on SPF *or* DKIM alignment.
- **TLS required for ALL senders** — not just bulk. Add STARTTLS check to every audit.
- **Yahoo spam rate = complaints / inbox-delivered** — CFL data against gross sends understates true rate.
- **ARC (RFC 8617) required for forwarding** — deploy on any mailing-list/forwarding path.
- **Bulk-sender status is permanent** at the primary domain — once 5,000/day crossed (aggregate across subdomains), ≥5k controls mandatory forever.
- **Gmail enforcement = rejection (5xx) post-Nov 2025** — diagnose by SMTP response class: 4xx=throttle/backoff/fix+retry; 5xx=requirement breach/stop+remediate.
- **Outlook consumer enforcement May 2025** — SPF+DKIM+DMARC alignment for >5k/day; rejection code `550 5.7.515`.
- **Apple Business Connect** emerging for iCloud Mail sender verification — monitor adoption.

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---|---|
| SPF exceeds 10 DNS lookups (`permerror`) | Flatten includes or use SPF macros |
| DKIM not aligned for DMARC | Sign with the From-domain (`d=fromdomain.com`), or align SPF |
| No one-click unsubscribe | Add `List-Unsubscribe` + `List-Unsubscribe-Post: List-Unsubscribe=One-Click` (RFC 8058) |
| Marketing sent on the transactional IP | Split subdomains/IPs by stream |
| Cold-IP volume blast | Gradual warm-up over 4–8 weeks; engaged recipients first |
| DMARC reports ignored | Wire `rua` to analyzer; review weekly |
| Bought/rented lists | Use only opt-in, verified, engaged lists |
| Written SOP never re-read | Verify-after-write is mandatory |
| Low spam rate but low engagement | Gmail silently filtering to spam — verify with seed test |
| Multiple DMARC records on same domain | Exactly one at `_dmarc.domain.com` |
| No ARC on forwarding path | Deploy ARC sealing for mailing lists/forwarders |
| Missing Feedback-ID header | Add `Feedback-ID: a:b:c:SenderID` for Gmail FBL campaign granularity |
| TLS not verified on transmission | `openssl s_client -starttls smtp -connect mx:25` on every sending IP |
| PTR missing or generic | Valid, meaningful, non-generic reverse DNS per sending IP |

---

## 6. Sources (Primary, Verified Live)

> All sources below fetched and verified via CRW crawler (`mcp__crw__crw_scrape`) or Jina Reader proxy on the dates noted. HTTP 200 with real content confirmed.

### Google (Gmail / Google Workspace)
- **Email sender guidelines**: https://support.google.com/a/answer/81126 — *verified live via CRW 2026-08-05*
- **Email sender guidelines FAQ / Postmaster Compliance**: https://support.google.com/mail/answer/14289100 — *verified live via CRW 2026-08-05*
  - Confirms: Compliance Status dashboard, permanent bulk-sender status at primary domain, Nov 2025 rejection enforcement, TLS requirement for all senders (Dec 2023), Gmail DMARC quarantine on own From: domain

### Yahoo
- **Sender Best Practices**: https://senders.yahooinc.com/best-practices/ — *verified live via CRW 2026-08-05*
- **FAQs**: https://senders.yahooinc.com/faqs/ — *verified live via CRW 2026-08-05*
  - Confirms: ARC required for forwarding, spam rate = complaints/inbox-delivered, CFL enrollment via Sender Hub (DKIM-domain based), 2-day unsubscribe honor, one-click unsubscribe required for marketing only, no IP-based CFL

### Microsoft (Outlook.com / Hotmail / Live)
- **Strengthening Email Ecosystem: Outlook's New Requirements for High-Volume Senders**: https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730 — *verified live via CRW 2026-08-05*
  - Confirms: May 5, 2025 enforcement start, SPF+DKIM+DMARC alignment for >5k/day, rejection code `550 5.7.515`, SNDS+JMRP unified portal, safe sender list not honored

### Standards Bodies
- **DMARC.org Overview**: https://dmarc.org/overview/ — *verified live via CRW 2026-08-03*
- **RFC 8058 — One-Click Unsubscribe**: https://www.rfc-editor.org/rfc/rfc8058 — *verified live via CRW 2026-08-03*
- **BIMI Group**: https://bimigroup.org/ — *verified live via CRW 2026-08-31*

### Industry Guides (Secondary, Cross-Referenced)
- **Mailflow Authority — Email Deliverability Best Practices 2026**: https://mailflowauthority.com/email-deliverability/email-deliverability-best-practices-2026 — *CRW 2026-08-31*
- **Markana Media — Email Deliverability Checklist 2026**: https://markanamedia.com/blog/email-deliverability-spf-dkim-dmarc-2026/ — *CRW 2026-08-31*
- **BulkEmailSetup — IP Warm-Up Schedule (Exact Daily Volumes)**: https://bulkemailsetup.com/ip-warm-up-schedule-for-email/ — *CRW 2026-08-31*
- **Knock — Email Domain Warmup Calculator**: https://knock.app/tools/email-domain-warmup-calculator — *CRW 2026-08-31*
- **InboxAlly — Gmail Complaint Feedback Loop Setup**: https://www.inboxally.com/docs/provider-deliverability-guides/gmail-complaint-feedback-loop-setup/ — *CRW 2026-08-31*
- **CloudServerForEmail — Gmail Postmaster Tools v2 Complete Guide 2025**: https://www.cloudserverforemail.com/blog/email-deliverability/gmail-postmaster-tools-v2-complete-guide-2025.html — *CRW 2026-08-31*

---

## 7. Web Access (Mandatory Standard)

Web access is required for live research/verification. Use this uniform chain (enforced company-wide):
- **Primary: the CRW crawler** (`mcp__crw__crw_scrape` / `mcp__crw__crw_map`) — independent of the Firecrawl/Nous paid-credit wall.
- **Fallback (CRW error/timeout/403/'Target unreachable')**: the Jina Reader proxy via shell redirection (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06).
- If both fail, mark the source **unverified** — never fabricate.

---

## 8. Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool**: the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth**: follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required**: pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record**: note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

---

## 9. Live Web Refresh Log

### 2026-08-03 (Initial Refresh)
- Verified Google, Yahoo, DMARC.org primary sources
- Added: TLS for all senders, Gmail DMARC quarantine on own domain, Yahoo ARC requirement, Yahoo spam rate = inbox-delivered denominator

### 2026-08-05 (Second Pass)
- Verified Google FAQ (Compliance dashboard, permanent bulk status, Nov 2025 rejection enforcement)
- Verified Microsoft Outlook enforcement (May 2025, 550 5.7.515)
- Adopted: SMTP response class diagnosis, Compliance Status dashboard as first audit artifact, primary-domain aggregation for bulk status, PTR+TLS on all-senders checklist

### 2026-08-31 (This Refresh — Third Pass)
- Verified Yahoo FAQs (CFL details, ARC, unsubscribe specifics, DKIM 2048-bit recommendation)
- Verified BIMI Group (implementation steps, VMC requirement, supporting MBPs)
- Verified industry guides: 4-8 week warmup schedule, Gmail FBL `Feedback-ID` header format, Postmaster Tools v2 Compliance Status as primary metric, Microsoft SNDS+JMRP unified portal, Apple Business Connect emerging
- Updated: Warmup timeline from 2-4 weeks → 4-8 weeks with day-by-day volumes
- Updated: Diagnostic order with Compliance Status first
- Added: BIMI as Phase A step 6, ARC as Phase A step 5
- Added: Microsoft SNDS/JMRP, Yahoo CFL ARF, Gmail FBL `Feedback-ID` to monitoring tools
- Added: Double opt-in, sunset at 90 days, 24-hour unsubscribe honor to list hygiene
- Added: Key updates table with verification dates and impact

---

## Related
- [[Email Deliverability Expert - Identity and Purpose]]
- [[Agent Training Standard 2026-08-03]]
- [[DNS Expert - Research & Skill Improvement 2026-08-02]]