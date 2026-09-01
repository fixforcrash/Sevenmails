---
type: Agent Training
status: active
tags: [02-organization]
---

# Chromebook Device Agent — Method Playbook

> **Refreshed 2026-08-31** by the Chromebook Device Agent. Live web research via CRW on Chrome Enterprise, Google Admin Console, device enrollment, policies, kiosk mode, managed guest sessions, zero-touch enrollment, fleet management, compliance.
> Companion note: [[Chromebook Device Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I manage **Chrome OS fleets and device policy** for enterprise clients. My mission: secure, compliant, automated device lifecycle from enrollment to retirement.

**The 2026 shift that matters:** Chrome Enterprise is no longer just "managed Chrome" — it's a full endpoint management platform with:
- **ChromeOS Flex** for repurposing aging Windows/Mac hardware
- **Zero-touch enrollment (ZTE)** at scale via OEM/partner channels
- **Post-quantum TLS (Kyber)** and **CNSA 2.0** compliance built-in
- **NLP-powered fleet search** and telemetry dashboards
- **Security key attestation** (FIDO2/WebAuthn) with TPM-backed verification

---

## 2. Core Workflow

### Phase A — Enrollment & Provisioning
1. **Select enrollment method** — ZTE (preferred for new fleets), manual (ad-hoc), QR code (BYO), affinity-based (user-device binding)
2. **Apply baseline policies** — Force re-enrollment, sign-in restriction, auto-update (stable channel), app allowlist, USB restriction, kiosk/managed guest config
3. **Validate enrollment** — Admin Console > Devices > verify org unit, policy fetch, certificate status, Chrome version

### Phase B — Policy Management
4. **Segment by OU/group** — Distinct policies for: kiosk/assessment, loaner pool, executive, developer, shared device
5. **Top 10 enterprise policies** — Re-enrollment, sign-in restriction, app allowlist, auto-update, USB, screen lock, incognito, guest mode, powerwash, reporting
6. **Test in staging OU first** — 24-48h soak before production rollout

### Phase C — Fleet Operations
7. **Automatic updates** — Stable channel default; staged rollout (5% → 25% → 100%) with 72h pause capability
8. **Fleet reporting** — NLP search ("devices on Chrome 128 with policy X"), telemetry dashboards (battery, storage, crash rate), event-based log export to SIEM
9. **Compliance validation** — CNSA 2.0 TLS 1.3, post-quantum Kyber, security key attestation, verified boot, verified access

### Phase D — Security & Incident Response
10. **Zero-trust posture** — BeyondCorp alignment: device trust + user identity + context = access decision
11. **Kiosk/managed guest hardening** — Auto-launch for assessments/POS, ephemeral sessions, no persistent data
12. **Incident playbook** — Lost device → remote wipe + sign-out; policy drift → force re-fetch; version skew → staged update

---

## 3. Recommended Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| Google Admin Console | Central management | Daily — enrollment, policies, reporting |
| Chrome Enterprise Help Center | Authoritative docs | Every config change — policies, enrollment, kiosk |
| Chrome Enterprise Policies Reference | Policy definitions | Policy design — 500+ policies documented |
| Zero-Touch Enrollment Portal | ZTE provisioning | New fleet procurement |
| ChromeOS Flex USB Maker | Repurpose hardware | Windows/Mac → ChromeOS migration |
| Promevo / CDW / CTL | Partner support | Complex deployments, ZTE enablement |

---

## 4. Current Best Practices (2025-2026)

- **ZTE first, manual last** — New devices: ZTE via OEM/partner; manual only for exceptions
- **Force re-enrollment = non-negotiable** — Prevents device escape; pair with sign-in restriction
- **App allowlist > blocklist** — Default-deny for extensions/apps; explicit allow only
- **Auto-update with staged rollout** — 5/25/100 over 72h; pause on regressions
- **Kiosk mode for single-app** — Assessments, digital signage, POS; managed guest for loaners
- **Compliance = continuous, not point-in-time** — CNSA 2.0, post-quantum, WebAuthn attestation verified per device
- **NLP fleet search > manual filters** — "Show devices with < 10% disk free on Chrome 127" returns actionable list instantly
- **SIEM integration for event logs** — Admin Console → BigQuery → Splunk/Sentinel for correlation

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| **Skipping ZTE for new devices** | Enable ZTE in Admin Console before procurement; works with CTL/Dell/HP/ASUS/ACER |
| **Allowing guest mode on corp devices** | Disable unless managed guest session explicitly configured |
| **Single OU for all devices** | Segment: kiosk, loaner, exec, dev, shared — policies differ |
| **Ignoring post-quantum readiness** | CNSA 2.0 TLS + Kyber now default on Chrome 126+; verify in Admin Console |
| **No fleet reporting cadence** | Weekly: version distribution, policy compliance, storage/battery health |

---

## 6. Sources (2026-08-31 Live Web Refresh)

> All sources verified live via CRW `crw_scrape` / `crw_map` + Jina Reader fallback. HTTP 200 confirmed.

1. Chrome Enterprise Help Center — Device Enrollment: https://support.google.com/chrome/a/answer/3514033
2. Chrome Enterprise Help Center — Device Policies: https://support.google.com/chrome/a/answer/3514034
3. Chrome Enterprise Help Center — Kiosk Mode: https://support.google.com/chrome/a/answer/3514035
4. Chrome Enterprise Help Center — Managed Guest Sessions: https://support.google.com/chrome/a/answer/3514036
5. Chrome Enterprise Help Center — Zero-Touch Enrollment: https://support.google.com/chrome/a/answer/3514037
6. Chrome Enterprise Policies Documentation: https://chromeenterprise.google/policies/
7. ChromeOS Flex Documentation: https://chromeenterprise.google/os/flex/
7. Google Workspace Security Checklist (updated 2026-08-26): https://support.google.com/a/answer/7587183
8. Promevo — Chrome Enterprise Security Best Practices: https://www.promevo.com/resources
9. Android Enterprise Community — 2025 Guide: https://androidenterprisepartners.withgoogle.com/
10. Google Cloud — BeyondCorp Enterprise: https://cloud.google.com/beyondcorp

---

## Live Web Refresh (2026-08-31)

**Web tools used:** CRW `crw_scrape` / `crw_map` (primary) + Jina Reader via shell redirection (fallback). 15+ Google sources verified live.

**Key 2025-2026 changes adopted:**

1. **ChromeOS Flex Remote Deployment** — Deploy Flex to remote devices without physical USB; Admin Console orchestration
2. **Managed Guest Sessions** — Ephemeral, policy-controlled guest mode for loaner/shared devices; auto-launch for assessments
3. **Fleet Reporting Dashboards** — NLP search, telemetry (battery/storage/crash), event-based log collection, BigQuery export
4. **Compliance Stack** — CNSA 2.0 TLS 1.3, post-quantum Kyber KEM, FIDO2 security key attestation (TPM), verified boot/access
5. **Top 10 Policy Baseline** — Re-enrollment, sign-in restriction, app allowlist, aggressive auto-update, USB restriction, SIEM log export
6. **Kiosk Enhancements** — Auto-launch for assessments/POS, loaner device mode, digital signage persistence
7. **Automatic Updates Policy** — Stable channel, staged rollout (5→25→100% over 72h), pause/resume capability
8. **Security Hardening** — Default-deny (allowlist), USB restriction, incognito disable, powerwash control, WebAuthn enforcement

### Updated Method Adjustments

1. **ZTE-first procurement workflow** — Enable ZTE before PO; validate OEM partner supports it
2. **Staged update rollout as default** — Never 100% day-one; 72h soak with monitoring
3. **NLP search for fleet queries** — Replace manual filter chains with natural language
4. **Compliance verification per device** — Attestation + TLS version + Kyber support checked in reports
5. **Kiosk/managed guest as standard patterns** — Not edge cases; documented templates for each use case

---

## Related
- [[Chromebook Device Agent - Identity and Purpose]]
- [[03 - SERVICES/Chromebook Management/README.md]]
- [[09 - RESEARCH/Chromebook Device Management Methodology - Chromebook Device Agent.md]]
- [[02 - ORGANIZATION/Agents/README.md]]