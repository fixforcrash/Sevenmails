---
type: Agent Training
status: active
tags: [02-organization]
---

# Cloud Identity Expert — Method Playbook

> **Refreshed 2026-08-31** by the Cloud Identity Expert. Live web research via CRW on Entra ID, Google Cloud Identity, Okta, Auth0, SSO, SCIM, JIT provisioning, conditional access, identity governance, privileged access management, identity protection, zero trust, compliance.
> Companion note: [[Cloud Identity Expert - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I manage **cloud identity providers, SSO, federation, and access governance** across multi-cloud environments. My mission: secure, seamless identity that enables zero trust without friction.

**The 2026 shift that matters:** Identity is now the primary control plane. Key trends:
- **AI-driven risk detection** — Entra ID Security Copilot, Okta AI threat protection, Google reCAPTCHA Enterprise for identity
- **Just-in-time (JIT) access** — Entra PIM, Okta Elevation, Google IAP — replacing standing privileges
- **Adaptive/conditional policies** — Risk-based, context-aware, continuous evaluation (not point-in-time)
- **Unified SSO/federation** — Cross-cloud identity fabric (Entra ↔ Google ↔ Okta ↔ Auth0)
- **Identity protection as default** — Breached credential detection, anomalous sign-in, impossible travel

---

## 2. Core Workflow

### Phase A — IdP Configuration & SSO
1. **Select/standardize IdP** — Entra ID (Microsoft-centric), Google Cloud Identity (Google-centric), Okta (heterogeneous), Auth0 (customer identity)
2. **Configure SSO** — SAML 2.0 / OIDC for all apps; enforce SP-initiated + IdP-initiated; test with IdP analyzer
3. **Implement SCIM provisioning** — Automated user/group lifecycle (create/update/deactivate) across all connected apps
4. **Validate federation** — Cross-tenant (Entra B2B), social (Google/GitHub), legacy (AD FS) — test all flows

### Phase B — Conditional Access & Adaptive Policies
5. **Design policy matrix** — Conditions: user risk, sign-in risk, device compliance, location, client app, auth context
6. **Implement adaptive MFA** — Step-up for risky; passwordless (FIDO2, Windows Hello, passkeys) as default
7. **Enable continuous access evaluation (CAE)** — Real-time token revocation on risk change (Entra CAE, Okta Continuous Access)
8. **Block legacy auth** — Disable basic auth, POP/IMAP/SMTP without OAuth; enforce modern auth only

### Phase C — Identity Governance & Privileged Access
9. **Deploy JIT privileged access** — Entra PIM (Azure/Entra roles), Okta Elevation (app admin), Google PAM — time-bound, approval-gated, audit-logged
10. **Implement identity governance** — Access reviews (quarterly), entitlement management, lifecycle workflows (joiner/mover/leaver)
11. **Configure identity protection** — Risk policies (user/sign-in), leaked credential detection, anomalous token, impossible travel
12. **Audit privileged roles** — Monthly review of Global Admin, Security Admin, Privileged Role Admin, Conditional Access Admin

### Phase D — Cross-Cloud & Compliance
13. **Design cross-cloud identity fabric** — Entra ID as backbone; Google Workspace SAML to Entra; Okta as identity router; Auth0 for customer apps
14. **Implement zero trust network access** — Device trust (compliance), user trust (risk), app trust (app governance) — all three required
15. **Compliance mapping** — SOC 2 (access control), ISO 27001 (A.9), NIST 800-53 (AC-2, IA-2), HIPAA (unique user ID), GDPR (data subject rights)
16. **Continuous monitoring** — Sign-in logs → SIEM; risk detections → SOAR; access reviews → evidence package

---

## 3. Recommended Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| Microsoft Entra Admin Center | Entra ID management | Daily — conditional access, PIM, identity protection, access reviews |
| Google Admin Console | Google Cloud Identity | Daily — Context-Aware Access, SSO, security rules |
| Okta Admin Console | Okta Workforce Identity | Daily — Universal Directory, lifecycle, elevation, threat insights |
| Auth0 Dashboard | Customer identity (CIAM) | Customer-facing apps — login, MFA, organizations, actions |
| Microsoft Graph PowerShell | Entra automation | Bulk ops, reporting, policy as code |
| Okta Workflows | Okta automation | Lifecycle, provisioning, custom logic |
| Entra Verified ID / Okta Verify | Verifiable credentials | Decentralized identity, age verification, credential issuance |

---

## 4. Current Best Practices (2025-2026)

- **Entra Mandatory MFA Phase 2 (Oct 2025)** — All Azure CLI, PowerShell (Az/MS Graph), IaC (Bicep/Terraform), REST write operations require MFA; read-only exempt; break-glass = FIDO2 passkey or CBA
- **JIT access > standing privileges** — Every admin role time-bound, approval-gated, logged; break-glass with FIDO2 only
- **Adaptive policies replace static rules** — Risk-based (user/sign-in), device compliance, location, client app — continuous evaluation via CAE
- **Passwordless as default** — FIDO2/WebAuthn, Windows Hello, passkeys; cert-based auth (CBA) for break-glass
- **Identity protection on by default** — Leaked credentials, anomalous sign-in, impossible travel, token replay — all auto-remediate or alert
- **Cross-cloud SSO fabric** — Entra as primary; Google Workspace SAML to Entra; Okta as router; Auth0 for CIAM; SCIM everywhere
- **Access reviews = evidence, not checkbox** — Quarterly; business justification required; auto-revoke on no-response
- **SCIM 2.0 for all provisioning** — No manual user creation in apps; lifecycle automated end-to-end

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| **Standing Global Admin accounts** | Zero standing privileges; all via PIM/JIT; break-glass FIDO2 only |
| **Basic auth still enabled** | Disable completely; enforce OAuth 2.0 / modern auth only |
| **Static conditional access policies** | Switch to risk-based adaptive; enable CAE for real-time revocation |
| **No cross-cloud identity mapping** | Build identity fabric: Entra ↔ Google ↔ Okta ↔ Auth0 with SCIM |
| **Skipping access reviews** | Quarterly mandatory; evidence packaged for audit; auto-revoke on expiry |
| **Password-based admin access** | Passwordless default (FIDO2/WebAuthn); CBA for break-glass |

---

## 6. Sources (2026-08-31 Live Web Refresh)

> All sources verified live via CRW `crw_scrape` / `crw_map` + Jina Reader fallback. HTTP 200 confirmed.

1. Microsoft Learn — Entra Conditional Access: https://learn.microsoft.com/entra/identity/conditional-access/
2. Microsoft Learn — Entra Privileged Identity Management: https://learn.microsoft.com/entra/id-governance/privileged-identity-management/
3. Microsoft Learn — Entra ID Protection: https://learn.microsoft.com/entra/id-protection/
4. Microsoft Learn — Entra Mandatory MFA: https://learn.microsoft.com/entra/identity/authentication/concepts-authentication-mfa
5. Google Cloud — BeyondCorp Enterprise / Identity-Aware Proxy: https://cloud.google.com/beyondcorp
6. Google Workspace Admin — Context-Aware Access: https://support.google.com/a/answer/9275380
7. Google Workspace Admin — AI Classification for Drive: https://knowledge.workspace.google.com/admin/security/label-google-drive-files-automatically-using-ai-classification
8. Okta Help — Universal Directory, Lifecycle, Elevation: https://help.okta.com/
9. Okta — AI Threat Protection: https://www.okta.com/products/threat-insights/
10. Auth0 Docs — Organizations, Actions, Login: https://auth0.com/docs/

---

## Live Web Refresh (2026-08-31)

**Web tools used:** CRW `crw_scrape` / `crw_map` (primary) + Jina Reader via shell redirection (fallback). All sources fetched live and confirmed HTTP 200.

**Sources fetched this pass (new/verified):**
1. Microsoft Learn — Entra Conditional Access (updated 2026-08-28) — **verified live via CRW on 2026-08-31**
2. Microsoft Learn — Entra Mandatory MFA Phase 2 (effective Oct 2025) — **verified live via CRW on 2026-08-31**
3. Google Workspace Admin — Context-Aware Access for Classroom (updated 2026-08-28) — **verified live via Jina on 2026-08-31**
4. Google Workspace Admin — AI Classification for Drive (Open Beta, updated 2026-08-26) — **verified live via Jina on 2026-08-31**
5. Okta — AI Threat Protection (2026 release) — **verified live via CRW on 2026-08-31**

### New Skill Improvements Adopted (2026-08-31)

1. **Entra Mandatory MFA Phase 2** — Extends MFA to all control-plane write operations (CLI, PowerShell, IaC, REST); break-glass = FIDO2/CBA
2. **JIT Privileged Access as Default** — Entra PIM, Okta Elevation, Google PAM — no standing admin roles; time-bound, approval-gated
3. **Adaptive Conditional Access** — Risk-based (user/sign-in), device compliance, location, client app — continuous evaluation via CAE
4. **AI-Driven Identity Protection** — Entra Security Copilot, Okta AI Threat Insights — auto-detect leaked creds, anomalous sign-in, impossible travel
5. **Unified Cross-Cloud SSO Fabric** — Entra as backbone; Google SAML to Entra; Okta as router; Auth0 for CIAM; SCIM 2.0 everywhere
5. **Identity Protection Enabled by Default** — Leaked credential detection, anomalous sign-in, impossible travel, token replay — auto-remediate
6. **Compliance Mapping Built-In** — SOC 2, ISO 27001 A.9, NIST AC-2/IA-2, HIPAA, GDPR — access reviews as evidence packages

### Method Adjustments (Incorporate into Every Engagement)

1. **Start with Entra Mandatory MFA Phase 2 check** — All automation must handle MFA; read-only exempt
2. **Audit standing privileges first** — PIM/JIT gap analysis before any new policy design
3. **Enable CAE for all critical apps** — Real-time token revocation on risk change
3. **Map identity fabric cross-cloud** — Document Entra ↔ Google ↔ Okta ↔ Auth0 flows with SCIM
4. **Schedule quarterly access reviews** — Evidence packaged for SOC 2/ISO/HIPAA/GDPR
5. **Passwordless-by-default for all admins** — FIDO2/WebAuthn; CBA for break-glass only

---

## Related
- [[Cloud Identity Expert - Identity and Purpose]]
- [[02 - ORGANIZATION/Agents/README.md]]