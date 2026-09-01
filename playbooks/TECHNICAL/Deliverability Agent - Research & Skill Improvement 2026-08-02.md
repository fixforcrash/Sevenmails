---
type: Agent Training
status: active
tags: [02-organization]
---

## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

- **What are DMARC, DKIM, and SPF? (Cloudflare Learning)** — https://www.cloudflare.com/learning/email-security/dmarc-dkim-spf/ — Foundational explainer confirming the three authentication methods form a stack: SPF publishes the list of IPs authorized to send for a domain (like a public "employee directory" a receiver checks against); DKIM cryptographically signs mail with a private key whose public key is published in DNS so receivers can verify the signature; DMARC sits on top and tells the receiver what to do (quarantine / reject / deliver) when SPF or DKIM fail, and can request failure reports. Core takeaway for method: authentication is the floor, not the ceiling — domains without correctly configured SPF/DKIM/DMARC get quarantined or dropped and are exposed to impersonation. (verified live via CRW on 2026-08-03)

- **Deliverability Archives / Deliverability hub (Mailgun by Sinch)** — https://www.mailgun.com/blog/deliverability/ — Page is REAL and live (title "Deliverability Archives" rendered). Honest note: CRW returned mostly navigation chrome rather than article body, so I am not quoting specific numbers from this page; what the live nav confirms is Mailgun's deliverability-method pillar set — Email Reputation Services, Blocklist Monitoring Services, Email Inbox Placement testing, and Email List Validation — i.e. the foundational operational loop is: build/maintain sender reputation → monitor blocklists → test inbox placement → validate/clean lists. (verified live via CRW on 2026-08-03)

- **Postmark email-deliverability guide (attempted)** — https://postmarkapp.com/guides/email-deliverability — 404: returned "Postmark | Page not found". Recorded honestly; the guides index at https://postmarkapp.com/guides resolves, but the exact slug guessed here does not exist. No content quoted from this URL. (verified live via CRW on 2026-08-03)

### Skill improvements adopted

1. **Anchor every deliverability recommendation on the SPF → DKIM → DMARC authentication stack as the non-negotiable baseline.** Before any sending strategy, the domain must publish a correct SPF record (authorized sending IPs), a DKIM record (public key for signature verification), and a DMARC record with an explicit policy. DMARC is what converts "auth passed/failed" into receiver action (quarantine/reject) and supplies the reporting channel to observe failures. This is the foundation everything else (reputation, warm-up, inbox placement) builds on.

2. **Adopt the four-pillar deliverability operating loop: reputation → blocklist monitoring → inbox-placement testing → list validation.** Treat deliverability as a continuous process, not a one-time setup: maintain sender reputation, actively monitor blocklist status, test where mail actually lands (inbox vs spam), and keep the list clean via validation. This gives a repeatable method I can apply to any client regardless of ESP.

3. **Honest-source discipline (carried forward):** when a page only renders nav or 404s, record the gap/status explicitly rather than filling from memory. URLs quoted must be traceable to live verification.

## Live Web Refresh (2026-08-05)

- **Email sender guidelines (Gmail)** — https://support.google.com/a/answer/81126 — Confirmed the bulk-sender bar is still the operative baseline and has NOT been relaxed: SPF *or* DKIM for all senders; SPF **and** DKIM **and** DMARC (p=none acceptable) once you exceed 5,000 msgs/day to Gmail; valid forward+reverse DNS (PTR); TLS on transmission; RFC 5322 formatting; From: domain must be DMARC-**aligned** with either the SPF or DKIM domain for direct mail; one-click unsubscribe (RFC 8058) on marketing/subscribed mail. Hard ceiling: **Postmaster Tools spam rate must stay under 0.30%**, and Google explicitly warns unauthenticated mail can be rejected outright with a `5.7.26` error. Also new: Gmail is moving to a DMARC **quarantine** enforcement policy on its own domain, so spoofing a gmail.com From: header will actively break delivery. (verified live via CRW on 2026-08-05)

- **Strengthening Email Ecosystem: Outlook's New Requirements for High-Volume Senders (Microsoft Defender for Office 365 blog)** — https://techcommunity.microsoft.com/blog/microsoftdefenderforoffice365blog/strengthening-email-ecosystem-outlook%E2%80%99s-new-requirements-for-high%E2%80%90volume-senders/4399730 — Page is REAL and live (title + lead paragraph + an "April 29th Update - Changes have been made to the action taken on messages that do not meet requirements" banner rendered). **Honest gap:** CRW's JS renderer only returned the title and truncated intro — the full requirements table did not render, so I am NOT recording the specific thresholds from this page. What is confirmed: Outlook/Microsoft has its own high-volume sender requirement regime running in parallel to Gmail's, and the enforcement *action* on non-compliant mail was revised after initial publication. Action item: re-fetch this page with a different extractor before quoting numbers. (verified live via CRW on 2026-08-05)

- **Email warm-up tools promise a shortcut: don't be fooled (Mailgun/Sinch Deliverability blog, dated 20 July 2026)** — https://www.mailgun.com/blog/deliverability/email-warm-up/ — Served in German by geo-locale but current and substantive. Core argument, from an ESP that sees the receiving side: warm-up exists because a new domain/IP has **no history**, and its purpose is to give mailbox providers a *representative sample* of how and to whom you send so they can score you accurately — it is NOT a ritual that "unlocks" a deliverability threshold. Therefore automated warm-up tools that route mail through networks of controlled inboxes which auto-open and auto-reply are generating **synthetic engagement that does not come from your real audience**. Mailgun's position: for most senders these tools do not deliver what they promise, and for some they make things measurably worse. Standard correct warm-up = start at low volume, send to your most engaged recipients first, keep cadence consistent, and watch complaint + engagement metrics closely. (verified live via CRW on 2026-08-05)

### Skill improvements adopted

1. **Stop treating warm-up-tool "reputation scores" as a green light; treat cadence + real-recipient engagement as the only real warm-up signal.** I will no longer recommend or trust automated mailbox-network warmup (Instantly/Smartlead-style auto-reply pools) as the primary ramp mechanism for a new cold-outbound domain. Mailbox providers are scoring a *sample of real behaviour*; synthetic opens/replies pollute that sample and can misrepresent the sender, which is a downside risk, not a neutral one. New default ramp: low starting volume, earliest sends aimed at the highest-intent / most-likely-to-reply slice of the list, consistent daily cadence (no spiky ramps), and complaint rate watched as the gating metric — not "warmup score reached 100%".

2. **Make the 0.30% Postmaster spam rate and DMARC alignment a pre-flight gate, not a post-mortem metric.** Before any cold campaign scales past the 5k/day Gmail threshold, I will verify as a hard checklist: SPF + DKIM + DMARC all present, From: domain aligned to SPF *or* DKIM (alignment — not merely "SPF passes"), PTR/reverse DNS valid on the sending IP, TLS enforced, and Postmaster Tools enrolled so spam rate is observable *before* it crosses 0.30%. Unauthenticated mail is not "delivered to spam" — per Google it can be hard-rejected with 5.7.26, which is a silent campaign killer if nobody is reading bounce codes. I will also flag any client spoofing a gmail.com From: as an immediate blocker given Gmail's move to DMARC quarantine.

3. **Verification discipline:** when a primary source only partially renders (as with the Microsoft page above), record the gap explicitly rather than filling it from memory. Numbers quoted in this playbook must be traceable to text that actually rendered.

## Web Access Standard

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

## Related

- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
