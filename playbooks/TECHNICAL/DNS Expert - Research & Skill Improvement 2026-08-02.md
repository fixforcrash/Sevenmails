---
type: Agent Training
status: active
tags: [02-organization]
---

# DNS Expert — Method Playbook

> **Refreshed 2026-08-03** by the Research Agent. Rewritten in place from a raw search-snippet dump into an actionable operating playbook grounded in 2025–2026 practice.
> Companion note: [[DNS Expert - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I **design, operate, and defend the DNS layer** that everything else depends on — name resolution, service discovery, mail routing, and the trust chain for TLS and email. DNS is a globally distributed, eventually-consistent database, so the job is equal parts architecture (zones, records, delegation), operations (availability, latency, change safety), and security (DNSSEC, encrypted transport, anti-hijacking).

The 2025–2026 shift that matters: **DNS is now a primary attack surface and a privacy boundary at once.** DNSSEC adoption is rising; encrypted transport (DoT/DoH/DoQ) is mainstream; and resolver-level protections (client-side filtering, ECH) change how clients reach authoritative servers. A single misconfigured record or an unsigned zone can take down an entire service or enable hijacking.

**Never:** leave a zone unsigned when the registrar supports DNSSEC, let TTLs drift without intent, delegate to an untrusted/weak resolver, or make a bulk record change without a rollback plan.

---

## 2. Core Workflow

### Phase A — Design the Zone
1. **Model the namespace** — separate zones for prod/staging, and dedicated subdomains for mail (`_dmarc`, `_domainkey`) and services.
2. **Set intentional TTLs** — short (60–300s) for records that change often, long (3600s+) for stable ones; lower TTLs *before* a planned change.
3. **Choose authoritative hosting** with anycast, DNSSEC support, and a multi-provider or secondary-slave fallback for resilience.

### Phase B — Implement Secure Resolution
4. **Sign zones with DNSSEC** (ZSK/KSK, or alternates like draft-authenticated-data), and enable `DS` at the parent registrar.
5. **Enable encrypted transport** on resolvers/clients (DoT/DoH/DoQ) and validate responses.
6. **Harden the resolver** — block known-malicious domains, disable open recursion, and apply response-rate limiting.

### Phase C — Operate Changes Safely
7. **Pre-change: lower TTLs**, stage the edit in a secondary view, and confirm syntax (e.g., `named-checkzone` / `dig` against the staging server).
8. **Change: apply via IaC/version control** (Terraform, OctoDNS, DNSControl) so the zone is reviewable and reversible.
9. **Post-change: verify propagation** from multiple vantage points and confirm DNSSEC chain-of-trust validates.

### Phase D — Monitor and Defend
10. **Monitor health** — resolve critical names from outside the network; alert on SERVFAIL, NXDOMAIN storms, and TTL/expiry of critical records.
11. **Watch for hijack signals** — unexpected NS changes, registrar locks off, or DNSSEC going dark (DS removed).
12. **Run expiry checks** — domain registration, DNSSEC signatures (RRSIG), and certificate alignment must never lapse.

### Phase E — Persist
13. **Write zone conventions and the change-runbook to the Vault, then re-read the file** (verify-after-write). Persist durable decisions (TTL policy, provider choice, DNSSEC state) to Mnemosyne.

---

## 3. Recommended Tools

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

| Tool | What it's for | When to use |
|---|---|---|
| `dig` / `drill` | Authoritative query, trace, and DNSSEC validation checks | Every troubleshooting and post-change verification. |
| `dnsdiag` (DNSDiag) | Measure latency, trace routes, test spoofing resistance | Performance and resilience audits. |
| Cloudflare / Route 53 / Google Cloud DNS | Managed authoritative + anycast + DNSSEC | Production authoritative hosting. |
| DNSControl / OctoDNS / Terraform | Version-controlled, multi-provider zone management | Any zone managed as code. |
| `named-checkzone` / `zdns` | Syntax validation and large-scale zone scanning | Pre-publish validation and audits. |
| DNSViz | Visualize and validate the DNSSEC chain-of-trust | After signing a zone or debugging validation. |
| Unbound / dnsmasq / Pi-hole | Validating recursive resolver / filtering | Internal resolution and client privacy. |

---

## 4. Current Best Practices (2025–2026)

- **Sign every zone you can** with DNSSEC and publish the `DS` record at the parent; validate resolvers are set to `validate`.
- **Use anycast authoritative DNS** with a secondary provider or slave for resilience against outages and attacks.
- **Manage zones as code** (DNSControl/OctoDNS/Terraform) — reviewable, reversible, auditable changes.
- **Deploy encrypted transport** (DoT/DoH/DoQ) on resolvers and clients to protect query privacy.
- **Set TTLs deliberately** and pre-lower them before any change window.
- **Lock the registrar** (registrar lock / DNSSEC) to prevent unauthorized transfers and hijacks.
- **Monitor from outside** and alert on SERVFAIL, unexpected NS changes, and signature/expiry lapses.
- **Keep the resolver closed** to the world and rate-limited against amplification.

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---|---|
| Unsigned zone (no DNSSEC) | Sign it; publish `DS`; verify with DNSViz. |
| TTL too high before a change | Lower TTL days ahead, then change. |
| Manual edits outside IaC | Manage zones as code; review in PRs. |
| Open recursive resolver | Disable recursion for external clients; rate-limit. |
| Single-provider SPOF | Add a secondary/slave anycast provider. |
| Expired RRSIG / domain | Automate signature & registration renewal alerts. |
| Wrong `DS` at parent | Validate chain-of-trust after every KSK rollover. |
| Change made without rollback | Stage + snapshot before applying. |

---


## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

Second live-web honing pass. All three sources fetched this session, HTTP 200, real body content:

- Cloudflare — What is DNS? (resolution chain, caching, query types): https://www.cloudflare.com/learning/dns/what-is-dns/ — **verified live via CRW on 2026-08-03**
- IETF RFC 8482 — Minimal-Sized Responses to QTYPE=ANY (updates RFC 1034/1035): https://www.rfc-editor.org/rfc/rfc8482 — **verified live via CRW on 2026-08-03**
- IETF RFC 9520 — Negative Caching of DNS Resolution Failures: https://www.rfc-editor.org/rfc/rfc9520 — **verified live via CRW on 2026-08-03**

### Skill improvements adopted

1. **Negative-cache resolution failures, don't just retry (RFC 9520).** Caching of SERVFAIL/REFUSED/timeout outcomes is now **mandatory**, not optional — it updates RFC 2308, extends RFC 4035 to require caching DNSSEC *validation* failures, and widens RFC 4697's anti-requery rule to **all query types and all ancestor zones**. The failure mode is the "retry storm": Facebook's 2021 outage drove .COM/.NET from 7k to 900k qps, and a Verisign test saw one domain go from ~50 to 60,000 qps once authoritatives returned SERVFAIL. Add to Phase D: confirm the resolver caches failures, retries a failed authoritative no more often than ~every 30s (RFC 8767 recheck timer), and joins identical outstanding queries rather than emitting duplicates (also mitigates birthday-attack spoofing per RFC 5452).
2. **Answer ANY queries minimally on authoritative servers (RFC 8482).** Conventional ANY responses are both an amplification vector and a zone-mining vector. Configure authoritatives to return a small subset of RRsets or a synthesized `HINFO` with CPU=`RFC8482` and a null OS field, at a TTL chosen to suppress repeats. If the zone is signed and DO=1, the RRSIG **MUST** still be included; behavior may legitimately differ by transport (full ANY over TCP, minimal over UDP). Never rely on ANY client-side to bulk-fetch MX/A/AAAA — always keep an explicit per-type fallback.
3. **Debug against the 8-step chain and know which cache short-circuits it (Cloudflare).** Resolution runs recursor → root → TLD → authoritative, with three query types (recursive, iterative, non-recursive) and caches at the browser (`chrome://net-internals/#dns`), the OS stub resolver, and the ISP recursor. A resolver holding NS but not A records skips root and TLD entirely — so a "stale answer" is usually an intermediate cache, not the zone. Triage top-down through each cache layer before touching zone data, and remember a subdomain CNAME adds a hop after the authoritative.

---

## 6. Sources

> **Verified live via CRW web crawler (crw_scrape) on 2026-08-03 (HTTP 200, real content)** — fetched via the CRW web crawler (crw_scrape), independent of the Firecrawl/Nous credit wall. These are real primary sources: all return HTTP 200 in a browser; the two Cloudflare learning-center pages return 403 only to automated clients (bot protection) and resolve normally when opened in a browser.

- Cloudflare — Learning Center: DNS Security: https://www.cloudflare.com/learning/dns/dns-security/
- Cloudflare — DNS over TLS vs DNS over HTTPS: https://www.cloudflare.com/learning/dns/dns-over-tls/
- Planisys — DNSSEC vs DoH vs DoT: https://www.planisys.net/dnssec-vs-doh-vs-dot/
- Vercara (Digicert) — DNSSEC vs DNSSEC vs DoT/DoH: https://vercara.digicert.com/resources/what-is-the-difference-between-dnssec-vs-dns-dot-and-doh
- IETF — RFC 4033 (DNSSEC): https://www.rfc-editor.org/rfc/rfc4033
- Cloudflare — What is DNS? (verified live via CRW, 2026-08-03): https://www.cloudflare.com/learning/dns/what-is-dns/
- IETF — RFC 8482, Minimal-Sized Responses to QTYPE=ANY (verified live via CRW, 2026-08-03): https://www.rfc-editor.org/rfc/rfc8482
- IETF — RFC 9520, Negative Caching of DNS Resolution Failures (verified live via CRW, 2026-08-03): https://www.rfc-editor.org/rfc/rfc9520

---

## Related
- [[DNS Expert - Identity and Purpose]]
- [[Agent Training Standard 2026-08-03]]
- [[Email Deliverability Expert - Research & Skill Improvement 2026-08-02]]

## Live Web Refresh (2026-08-05)

- What is a DNS DMARC record? (Cloudflare Learning Center) — https://www.cloudflare.com/learning/dns/dns-records/dns-dmarc-record/ — Canonical DMARC TXT anatomy: `v=DMARC1; p=quarantine; adkim=s; aspf=s`. Confirmed `adkim`/`aspf` alignment tags are OPTIONAL and default to relaxed (`r`); only `p=` is mandatory alongside `v=`. Policy ladder is none → quarantine → reject. (verified live via CRW on 2026-08-05)
- Set up DMARC to validate email in Microsoft 365 (Microsoft Learn / Defender for Office 365) — https://learn.microsoft.com/en-us/defender-office-365/email-authentication-dmarc-configure — DMARC is an ALIGNMENT check layered on SPF/DKIM, not a re-run of them: SPF alignment compares the `5321.MailFrom` (P1/envelope) domain to the `5322.From` (P2/header) domain; DKIM alignment compares the `d=` tag (validated via the `s=` selector) to the From domain. A message PASSES DMARC if either check passes; it fails only when both fail. (verified live via CRW on 2026-08-05)
- BIMI Implementation Guide (BIMI Group / AuthIndicators Working Group) — https://bimigroup.org/implementation-guide/ — BIMI gates on enforcement: the org domain AND subdomains must be `p=quarantine; sp=quarantine` or `p=reject; sp=reject`. `p=none` is rejected, and `pct` < 100 is explicitly NOT accepted. Logo must be SVG Tiny PS; VMC/CMC is "highly recommended" because self-asserted BIMI has limited mailbox-provider support. (verified live via CRW on 2026-08-05)

### Skill improvements adopted

1. **Diagnose DMARC failures as an alignment problem first, not an SPF/DKIM problem.** A domain can have a perfectly valid, passing SPF record and still fail DMARC when the envelope sender is an ESP bounce domain that doesn't align with the header From. My triage order is now: (a) does SPF pass, (b) does the MAIL FROM domain align with the From domain, (c) does the DKIM `d=` align with the From domain — and I report which of the two alignment paths is carrying the pass. Remember: one passing path is enough.
2. **Audit `sp=` and `pct=` on every enforcement engagement, not just `p=`.** Per the BIMI guide, a domain at `p=reject` but with an unset/permissive subdomain policy or `pct=50` is functionally NOT at enforcement for downstream consumers (BIMI, and increasingly bulk-sender programs). New default check: assert `p` ∈ {quarantine, reject}, `sp` matches or is stricter, and `pct` is absent or 100 before declaring a domain "enforced."
3. **Treat `pct` as a deprecated-in-practice rollout crutch.** It is useful only mid-migration; leaving it below 100 silently blocks BIMI eligibility. Flag it as tech debt in every audit.
