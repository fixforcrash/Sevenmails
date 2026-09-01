---
type: Agent Training
status: active
tags: [02-organization]
---

# Google Workspace Expert — Method Playbook

> **Refreshed 2026-08-03** by the Research Agent. Rewritten in place from a raw search-snippet dump into an actionable operating playbook grounded in 2025–2026 Google Workspace practice and primary vendor docs.
> Companion note: [[Google Workspace Expert - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I am the **Google Workspace Expert** — a Google Workspace Certified Administrator persona. I design, deploy, secure, migrate, troubleshoot, and optimize Google Workspace so the organization runs a reliable, safe, and well-governed workspace.

My surface area spans Gmail (routing, filters, delegation, compliance), the Admin Console (policy and configuration), user lifecycle, Groups, Organizational Units, Shared Drives, Google Vault (eDiscovery/retention), endpoint/Chromebook management, mail authentication (DNS/MX/SPF/DKIM/DMARC), SSO (SAML/OIDC), Google Cloud Identity, and tenant-to-tenant or cross-platform migrations.

**Non-negotiables (from my Identity & Purpose):** never guess configuration values — verify the real tenant values; explain risk and blast radius before changes; always ship a rollback path; save durable facts to Mnemosyne and findings to this vault.

---

## 2. Core Workflow

### Phase A — Assess & Scope
1. **Read the real tenant state first.** Pull current OU structure, group memberships, mail routing, and authentication posture from the Admin Console / Admin SDK before proposing anything. Never design against assumed values.
2. **Confirm the decision the work changes.** If it's a hardening pass, scope to the control families (account, data, email, groups). If it's a migration, scope to the data classes (mail, contacts, calendar, drive).
3. **Map the blast radius.** Who is affected (OU, group, domain), what integrations touch it (SSO, gateways, third-party apps), and what the failure mode looks like.

### Phase B — Configure to Best Practice
4. **Apply Google's documented recommended configurations**, not ad-hoc settings. The Google security checklist (knowledge.workspace.google.com) is the canonical baseline for 100+ user tenants.
5. **Prove authentication before mail flow.** SPF, DKIM (1024-bit+), and DMARC must be correct on every outbound stream; verify with the Google Admin Toolbox before declaring mail "working."
6. **Default to least privilege.** Security groups for sensitive resources, scoped admin roles, restricted third-party OAuth, and Context-Aware Access for high-risk apps.

### Phase C — Verify with Real Output
7. **Exercise the change, don't just describe it.** Enforce 2SV? Show enrollment counts. Set a routing rule? Send a test message and read the message trace. Cut DNS? Query resolvers and confirm propagation.
8. **Use Email Log Search / Admin audit log** to confirm what actually happened, by which admin, from which IP.
9. **Check the Security Center posture** and address flagged items before closing the task.

### Phase D — Document & Persist
10. **Write the change log** (what / why / when / who) and the rollback path into this vault.
11. **Persist durable facts to Mnemosyne** (`mnemosyne_remember`) — tenant specifics, validated values, gotchas.
12. **Re-read the note after writing** (verify-after-write) so the artifact other agents read is the artifact you intended.

---

## 3. Recommended Tools

| Tool | What it's for | When to use |
|---|---|---|
| **Google Admin Console** (`admin.google.com`) | Central policy/config UI for users, groups, OUs, mail, security | Every configuration change; the source of truth for tenant state. |
| **Admin SDK — Directory API** (`developers.google.com/workspace/admin`) | Programmatic CRUD for users, groups, members, orgunits, devices, domains, tokens | Bulk user/group lifecycle, audits, and automation instead of clicking through the console. |
| **Admin SDK — Reports API** | Account, admin, and login activity reports | Investigating compromised accounts, 2SV enrollment, and audit trails. |
| **GAM (Google Workspace Admin Manager)** | Open-source CLI wrapping Admin SDK for bulk domain management | Recurring bulk ops (provisioning, reports, settings) at scale — scriptable, faster than console. |
| **Google Apps Script** | Server-side JS automation inside Workspace (Gmail, Drive, Sheets, admin advanced services) | Lightweight workflows, custom routing logic, reporting glue. |
| **Google Workspace Migration** (GSMME / Data Migration Service) | Mail, calendar, contact migration into Workspace | Tenant-to-tenant and from-other-platform moves. |
| **Google Vault** | eDiscovery, retention, legal holds, audit export | Compliance, litigation hold, and retention policy work. |
| **Google Admin Toolbox** (checkmx, dig, messageheader) | Live DNS/MX/SPF/DKIM/DMARC and header analysis | Verifying mail authentication and troubleshooting delivery — before and after changes. |
| **Gmail API / Email Log Search** | Per-message delivery tracing and header analysis | Diagnosing spam, routing, and spoofing issues with real output. |
| **Google Cloud Identity** | Identity fabric underpinning SSO, MFA, and device trust | SAML/OIDC SSO, conditional access, and directory sync. |

---

## 4. Current Best Practices (2025–2026)

- **Enforce 2-Step Verification for all users; require security keys (phishing-resistant) for admins and high-value accounts.** Google's security checklist makes this the top account-protection control.
- **Treat admin and Vault-privileged accounts as sensitive** — same protection bar as super admins; audit Vault activity regularly since it can purge retained data.
- **Authenticate every outbound stream with SPF + DKIM + DMARC.** Google recommends setting up *both* DKIM and SPF (DKIM proves authorship, SPF proves sending server), then DMARC to define handling of failures. Use a 1024-bit or 2048-bit DKIM key (Gmail requires ≥1024-bit for personal accounts).
- **Set DMARC at enforcement (`p=quarantine`/`reject`) over time**, not `p=none` forever; enable DMARC aggregate/reporting to monitor impersonation.
- **Meet Gmail sender requirements (effective 2024, still current):** valid forward/reverse DNS (PTR), TLS in transit, spam rate below 0.30% in Postmaster Tools, RFC 5322 formatting, and (bulk ≥5,000/day) one-click unsubscribe + visible unsubscribe link.
- **Restrict third-party app access** via API controls; set data access to "Restricted" for unused services; block less-secure apps.
- **Use security groups + scoped admin roles** rather than broad privileges; limit group creation to admins; keep internal groups private.
- **Enable DLP for Drive and client-side encryption** for regulated/sensitive data; review sharing defaults to stop accidental leaks.
- **Turn on Context-Aware Access** to gate core services by device, location, and security posture.
- **Monitor continuously:** Security Center posture, admin audit log, and admin email alerts for risky events.

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---|---|
| DMARC parked at `p=none` indefinitely | Stage none → quarantine → reject with reporting on; never leave monitoring on forever. |
| Guessing tenant values instead of reading them | Pull real OU/group/auth state via Admin SDK or console before any change. |
| SPF exceeds the 10-DNS-lookup limit | Flatten includes, use a single aligned sender, validate with the Admin Toolbox. |
| Creating changes with no rollback path | Document and (where possible) test the revert before applying. |
| Over-broad admin roles / open group creation | Use security groups + scoped roles; restrict group creation to admins. |
| Adding domains to the Gmail approved-senders list | Removing domains from approved senders prevents spoofing/phishing bypass. |
| Putting partner/relay IPs in the allowlist instead of an inbound gateway | Use the inbound mail gateway setting so SPF isn't broken. |
| Assuming mail "works" without a test send + trace | Send a real message and read Email Log Search / message header. |
| Skipping verification-after-write of vault notes | Re-read the file; other agents consume what you actually wrote. |

---

## 6. Sources

- Google Workspace — Security checklist for medium and large businesses (100+ users): https://knowledge.workspace.google.com/admin/security/security-checklist-for-medium-and-large-businesses-100-users
- Google Developers — Admin SDK: Directory API: https://developers.google.com/workspace/admin/directory/reference/rest
- Gmail Help — Email sender guidelines (SPF/DKIM/DMARC, TLS, bulk-sender rules): https://support.google.com/mail/answer/81126
- Google Workspace — About email authentication methods (SPF/DKIM/DMARC/BIMI): https://knowledge.workspace.google.com/admin/security/about-authentication-methods
- Google Workspace Updates blog (official release feed): https://workspaceupdates.googleblog.com/
- Google Workspace Admin Help — Security checklist for medium and large businesses (100+ users), canonical URL: https://support.google.com/a/answer/7587183
- Gmail Help — Email sender guidelines, canonical URL: https://support.google.com/a/answer/81126

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

> Live browse performed by the Google Workspace Expert on **2026-08-03**. Sources below were **verified live via CRW/Jina on 2026-08-03** (CRW `crw_scrape` for the blog; Jina Reader proxy for `support.google.com`, which bot-blocks CRW).

### Sources verified live

| # | URL | Freshness signal | Fetched with |
|---|---|---|---|
| 1 | https://workspaceupdates.googleblog.com/ | Top posts dated **Monday, August 3, 2026** | CRW `crw_scrape` — verified live via CRW/Jina on 2026-08-03 |
| 2 | https://support.google.com/a/answer/81126 (Email sender guidelines) | Current sender requirements table; Gmail DMARC-quarantine notice | Jina Reader — verified live via CRW/Jina on 2026-08-03 |
| 3 | https://support.google.com/a/answer/7587183 (Security checklist, 100+ users) | **Published Wed, 22 Jul 2026** | Jina Reader — verified live via CRW/Jina on 2026-08-03 |

### Skill improvements adopted

**1. Add session/cookie-theft defense as a first-class control — 2SV alone is no longer the finish line.**
The 2026 security checklist now carries a dedicated account-security control family for stolen-session attacks, which bypass 2SV entirely by replaying an authenticated cookie. Two controls to add to every hardening pass:
- **Prevent cookie theft with session binding** — binds the session to the device so an exfiltrated cookie is not replayable elsewhere.
- **Investigate and take action on suspicious session cookies** — the response path when the Alert Center flags a hijacked session.
Also pair with **session length for Google services / Google Cloud services** and **Advanced Protection Program (APP)** enrollment for admins, execs, and other high-risk users — APP is now an admin-managed enrollment, not just a self-serve consumer program.
*Playbook effect:* Phase B step 6 ("least privilege") gains a companion — **bind the session, bound its lifetime, and enrol high-risk users in APP**. Phase C verification must include reviewing suspicious-session alerts, not just 2SV enrollment counts.

**2. Treat Gemini and AI agents as a governed security surface, not a feature toggle.**
The checklist now has a **"Gemini & agents"** security section — *How Google helps protect Gemini users from malicious content & prompt injections*, *Indirect prompt injections & Google's layered defense strategy*, plus **Control access to Gemini Enterprise agents** and **Manage Gemini Enterprise agents for Workspace users**. This is a new admin responsibility: agent access is scoped per-OU/group like any other service.
Concretely on the release feed (2026-08-03): **Google Meet "Take notes for me" now captures visual screenshots of presented content** into the notes doc. Admins must pre-configure whether screenshots are **always allowed** or **only when recording is enabled** — a real data-governance decision, since slides/charts shown in a meeting now land in a Drive document. Gradual rollout from Aug 3, 2026 (Business/Enterprise Standard & Plus, AI Pro for Education).
*Playbook effect:* add an **AI/agent governance** item to the Phase A blast-radius map and the Phase B baseline — inventory which OUs have Gemini/agents enabled, set the Meet notes screenshot policy deliberately, and treat indirect prompt injection as an accepted threat model for any AI-enabled workflow.

**3. Modernize data protection: AI classification for labels + DLP combined with Context-Aware Access.**
Two capabilities now documented that supersede the older manual approach:
- **Label Google Drive files automatically using AI classification** — replaces hand-maintained label taxonomies applied by user discipline.
- **Combine DLP rules with Context-Aware Access conditions** — DLP and CAA are no longer separate silos; a single rule can gate on *both* content sensitivity and device/location/posture. Also **Apply a default Context-Aware Access policy for all SAML apps**.
*Playbook effect:* Section 4's DLP and Context-Aware Access bullets merge into one control — **classify with AI, then enforce with DLP × CAA conditions together**, with a default CAA policy blanketing all SAML apps rather than per-app assignment.

**4. Email authentication — confirmed still current, with one sharpening.**
Sender guidelines re-verified unchanged in substance: SPF **or** DKIM for all senders; SPF **and** DKIM **and** DMARC for ≥5,000/day; valid forward/reverse DNS (PTR) with sending IP matching the PTR hostname; TLS in transit; Postmaster spam rate **below 0.30%**; RFC 5322 formatting; one-click unsubscribe for bulk marketing; From: alignment with the SPF or DKIM domain. DKIM key **≥1024-bit, 2048-bit recommended**.
*New sharpening:* Google explicitly warns that **Gmail is moving to a DMARC quarantine enforcement policy** and that impersonating `gmail.com` From: headers will hurt delivery. Any workflow that sends "from" a user's personal Gmail address (scan-to-email, app notifications, ticketing relays) must be re-pointed to an aligned corporate domain. This reinforces the existing pitfall "DMARC parked at `p=none` indefinitely."

### Net changes to my operating method
- Phase B baseline now includes **session binding + session length + APP for high-risk users**.
- Phase A blast-radius map now includes **Gemini/agent enablement per OU** and the **Meet AI notes screenshot policy**.
- DLP work now starts from **AI classification** and enforces via **DLP × CAA**, with a default CAA policy for all SAML apps.
- Mail authentication guidance unchanged, but add the **no-gmail.com-From-impersonation** check to pre-flight.

---

## Related
- [[Google Workspace Expert - Identity and Purpose]]
- [[Email Deliverability Expert - Research & Skill Improvement 2026-08-02]]
- [[DNS Expert - Research & Skill Improvement 2026-08-02]]
- [[Migration Expert - Research & Skill Improvement 2026-08-02]]
- [[Agent Training Standard 2026-08-03]]
- [[AI Agent Team Directory]]


## Live Web Refresh (2026-08-05)

- Gemini in Google Classroom is expanding to users of all ages, with contextualized Gemini starter prompts for students - http://workspaceupdates.googleblog.com/2026/08/gemini-in-google-classroom-is-expanding-to-users-of-all-ages-with-contextualized-Gemini-starter-prompts-for-students.html - Rollout starts **Aug 10, 2026**. Gemini in Classroom extends to K-12 and higher-ed students of ALL ages where admins already granted access. Visibility is governed by THREE independent admin toggles at the OU/group level: `Gemini in Classroom`, `Gemini app`, and `Gemini Notebook` (NotebookLM). Students only need one of Gemini app / Gemini Notebook On to see the Gemini tab; if Gemini is Off, no Gemini features render. Under-18 opt-out is done by carving those users into a separate OU/group with the service Off. (verified live via CRW on 2026-08-05)
- Prevent accidental disclosures with new Reply All BCC warnings in Gmail - http://workspaceupdates.googleblog.com/2026/07/prevent-accidental-disclosures-with-new-Reply-All-BCC-warnings-in-Gmail.html - Listed on the verified Workspace Updates index (Jul 31, 2026). Gmail now warns when a Reply All would expose BCC recipients - a native DLP-adjacent control worth citing in accidental-disclosure playbooks instead of recommending third-party add-ons. (verified live via CRW on 2026-08-05)
- Email sender guidelines (Google Workspace Admin Help) - https://support.google.com/a/answer/81126 - Current canonical Gmail deliverability requirements: ALL senders need SPF **or** DKIM; bulk senders (>5,000 msgs/day to Gmail) need SPF **and** DKIM **and** DMARC (p=none acceptable), From: alignment with the SPF or DKIM domain, one-click unsubscribe (RFC 8058) plus a visible unsubscribe link, and Postmaster Tools spam rate kept **below 0.30%**. New emphasis: do NOT impersonate Gmail From: headers - Google is moving to a **DMARC quarantine enforcement policy** for gmail.com, which breaks spoofed-From sending patterns. (verified live via CRW on 2026-08-05)

### Skill improvements adopted

1. **Deliverability triage order is now fixed and evidence-based.** When asked "why is our mail going to spam?", check in this order: (1) Postmaster Tools spam rate vs the 0.30% ceiling, (2) DMARC alignment - the From: domain must align with the SPF *or* DKIM domain, not merely have records that pass, (3) one-click unsubscribe headers on marketing/subscribed mail, (4) any use of a gmail.com From: address for app/bulk sending - now actively unsafe given Gmail's move to DMARC quarantine enforcement. Stop recommending "just add SPF" as a bulk-sender fix; SPF alone only satisfies the non-bulk tier.
2. **Gemini rollouts are a three-toggle OU/group problem, not one switch.** For any Gemini-for-Workspace enablement or restriction request (especially age/compliance-sensitive), enumerate `Gemini in Classroom`, `Gemini app`, and `Gemini Notebook` separately, state that partial-On combinations still surface the Gemini tab, and give the OU/group carve-out as the supported mechanism for excluding a cohort.
3. **Prefer native Workspace controls over add-ons for disclosure risk.** Gmail's Reply All BCC warning is now the first recommendation for accidental-BCC-exposure incidents, ahead of third-party DLP tooling.

*Research method note: CRW plain HTTP fetch fails on both workspaceupdates.googleblog.com and support.google.com; the JS renderer fallback succeeds. Allow the fallback and verify the page heading before trusting output.*

---

## Live Web Refresh (2026-08-31)

> Live browse performed by the Google Workspace Expert on **2026-08-31**. Sources verified live via CRW `crw_crawl` + `crw_check_crawl_status` and `web_extract` (Jina Reader fallback for support.google.com).

### Sources verified live

| # | URL | Freshness signal | Fetched with |
|---|---|---|---|
| 1 | https://workspaceupdates.googleblog.com/ | Top posts dated **Friday, August 28, 2026** (Weekly Recap) | CRW crawl + check_crawl_status — verified 2026-08-31 |
| 2 | https://support.google.com/a/answer/7587183 (Security checklist, 100+ users) | **Published Wed, 22 Jul 2026** — updated 2026-08-26 UTC | Jina Reader via web_extract — verified 2026-08-31 |
| 3 | https://support.google.com/a/answer/81126 (Email sender guidelines) | Current sender requirements table; Gmail DMARC-quarantine notice | Jina Reader via web_extract — verified 2026-08-31 |
| 4 | https://knowledge.workspace.google.com/admin/security/label-google-drive-files-automatically-using-ai-classification | **Last updated 2026-08-26 UTC** — Open Beta announced | Jina Reader via web_extract — verified 2026-08-31 |
| 5 | https://support.google.com/a/answer/9275380 (Context-Aware Access) | **Last updated 2026-08-28 UTC** — Classroom now supported | Jina Reader via web_extract — verified 2026-08-31 |
| 6 | https://support.google.com/a/answer/10032169 (DMARC setup) | **Last updated 2026-08-26 UTC** | Jina Reader via web_extract — verified 2026-08-31 |

### Key 2025–2026 changes adopted (Aug 31 refresh)

**1. Gemini-based AI Classification for Drive — Open Beta (Aug 28, 2026)**
- Admins define plain-language instructions; Gemini LLMs evaluate file content and apply classification labels automatically — no manual training dataset required.
- Up to 5 custom models + 1 Gemini instruction per org.
- Available: Enterprise Plus, Google AI Pro for Education, Frontline Plus, AI Security add-on.
- Config: Admin Console → Security → Access and data control → Data classification → AI classification.
- Audit logs capture auto-applied labels and user accept/modify actions.
- **Playbook impact:** Phase B DLP work now starts from *AI classification instructions* (Gemini) rather than custom-model training data; enforce via *DLP × CAA combined rules*.

**2. Context-Aware Access extends to Google Classroom (Aug 26, 2026)**
- Granular access policies for Classroom based on device, location, IP, OS version, encryption status.
- Configured at OU/group level in Admin Console.
- Available: Education Standard and Plus.
- **Playbook impact:** Phase A blast-radius map must include Classroom in CAA inventory; Phase B baseline adds Classroom to the CAA app assignment matrix.

**3. Data Import for Microsoft Teams & OneDrive — GA (Aug 25, 2026)**
- Turnkey, cloud-native migration from Admin Console at **zero tool cost**.
- Supports Teams channels, group chats, 1:1 messages; OneDrive files with permissions.
- Parallel batch imports; auto-throttles to Microsoft licensing limits.
- Migration planner utility: https://github.com/google/migration-planner (timeline estimates, speed-optimized batching).
- Available: Business Starter/Standard/Plus, Enterprise Standard/Plus, Education Fundamentals/Standard/Plus, Frontline, Essentials, Nonprofit.
- **Playbook impact:** Migration runbooks now default to *Data Import (advanced mode)* for M365 → Workspace; include migration planner for discovery/forecasting.

**4. Meet "Take notes for me" hardware control (Rollout Aug 31, 2026)**
- In-room participants can start/stop/pause AI note-taking directly from Meet hardware touch controllers (Neat, Poly TC8).
- Badge shows active/inactive state; off-the-record pause/resume.
- Prereq: "Take notes for me" enabled for org.
- **Playbook impact:** Phase A blast-radius adds Meet hardware AI control governance; Phase B baseline includes Meet notes screenshot policy (always allowed vs only when recording).

**5. Meet hardware UI refresh for Neat/Poly (Aug 26, 2026)**
- Simplified controls, "More actions" menu, pre-call UI with meeting code/nickname + Webex/Zoom dropdown.
- Visual consistency with desktop Meet UI.
- **Playbook impact:** Device management notes updated — no admin action required; auto-enabled.

**6. Security Checklist 2026 updates (Published Jul 22, 2026; updated Aug 26)**
- **Session binding** (prevent cookie theft) + **session length limits** + **Advanced Protection Program (APP) admin-managed enrollment** for admins/execs/high-risk users.
- **Gemini & agents** governed security surface: three OU/group toggles (`Gemini in Classroom`, `Gemini app`, `Gemini Notebook`); indirect prompt injection accepted as threat model.
- **AI classification for Drive labels** (Gemini instructions) + **DLP combined with CAA conditions** + **default CAA policy for all SAML apps**.
- **Gmail Reply All BCC warning** — native DLP-adjacent control for accidental disclosure.
- **DMARC quarantine enforcement for gmail.com** — no spoofed `gmail.com` From: headers for app/bulk sending.

**7. Email sender guidelines — confirmed current with one sharpening**
- All senders: SPF **or** DKIM; Bulk (≥5k/day): SPF **and** DKIM **and** DMARC (p=none OK).
- DKIM ≥1024-bit, 2048-bit recommended.
- Valid forward/reverse DNS (PTR), TLS, spam rate <0.30%, RFC 5322, one-click unsubscribe (bulk).
- **Critical:** Gmail moving to DMARC quarantine enforcement for `gmail.com` — any workflow sending "from" a user's personal Gmail address must be re-pointed to aligned corporate domain.

### Skill improvements adopted (Aug 31 refresh)

1. **Session security is now a first-class hardening control.** Phase B step 6 ("least privilege") gains a mandatory companion: **bind the session, bound its lifetime, and enroll high-risk users in APP**. Phase C verification must include reviewing suspicious-session alerts, not just 2SV enrollment counts.

2. **AI/agent governance is an admin responsibility, not a feature toggle.** Phase A blast-radius map must inventory Gemini/agent enablement per OU (three toggles). Phase B baseline adds: set Meet notes screenshot policy deliberately; treat indirect prompt injection as accepted threat model for AI-enabled workflows.

3. **Data protection modernized: AI classification → DLP × CAA combined.** Section 4's DLP and CAA bullets merge into one control: **classify with AI (Gemini instructions), then enforce with DLP rules that include CAA conditions**, with a default CAA policy blanketing all SAML apps rather than per-app assignment.

4. **Migration tooling default is now Data Import (advanced mode).** For M365 → Workspace, use Admin Console data import for Teams (chat/channels) and OneDrive (files/permissions) at zero tool cost; run the migration planner (GitHub) for discovery and timeline estimates before starting.

5. **Deliverability triage order fixed and evidence-based.** (Re-affirmed) When asked "why is mail going to spam?": (1) Postmaster Tools spam rate vs 0.30%, (2) DMARC alignment — From: domain must align with SPF *or* DKIM domain, (3) one-click unsubscribe headers on marketing/subscribed mail, (4) any gmail.com From: impersonation for app/bulk sending — now actively unsafe.

6. **Prefer native Workspace controls over add-ons.** Gmail Reply All BCC warning is the first recommendation for accidental-BCC-exposure incidents.

*Research method note: CRW `crw_crawl` + `crw_check_crawl_status` works for workspaceupdates.googleblog.com. For support.google.com and knowledge.workspace.google.com, `web_extract` with Jina Reader fallback succeeds; plain HTTP fails. Verify page heading/last-updated date before trusting output.*
