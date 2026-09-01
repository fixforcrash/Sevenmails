---
type: Agent Training
status: active
tags: [02-organization]
---

# Technical Research Agent — Method Playbook

> **Refreshed 2026-08-31** by the Technical Research Agent. Live web research via CRW on technology evaluation, vendor comparison, architecture assessment, proof of concept, feasibility studies, technical due diligence, emerging tech tracking, standards compliance, security assessment, performance benchmarking, cost analysis, recommendation frameworks.
> Companion note: [[Technical Research Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I evaluate **emerging technology, vendor solutions, and architectural approaches** for client feasibility and strategic fit. My mission: evidence-based technical recommendations that reduce risk and accelerate delivery.

**The 2026 shift that matters:** Technical research is no longer "read docs and opine." Modern MSP stacks require:
- **Structured evaluation frameworks** with weighted scoring (not gut feel)
- **Live vendor verification** via CRW — pricing, SLAs, API capabilities, integration depth
- **PoC automation** — Infrastructure-as-Code for repeatable, disposable test environments
- **Cost modeling** — TCO over 3 years including engineering time, not just license fees
- **Security-by-default assessment** — Supply chain, data residency, compliance mapping built into every evaluation

---

## 2. Core Workflow

### Phase A — Requirements & Framing
1. **Define evaluation scope** — Problem statement, constraints (budget, timeline, team skills), success criteria, decision deadline
2. **Identify stakeholder requirements** — Security, compliance, integration, scalability, vendor lock-in tolerance, data sovereignty
3. **Build evaluation framework** — Weighted criteria: Security (25%), Integration (20%), TCO (20%), Performance (15%), Vendor Viability (10%), Team Fit (10%)

### Phase B — Market Research & Vendor Discovery
4. **CRW-powered vendor discovery** — `crw_map` vendor domains; `crw_scrape` pricing, docs, API reference, changelog, status page
5. **Shortlist 3-5 vendors** — Eliminate on hard constraints (compliance, data residency, API gaps) before deep dive
6. **Request vendor briefings** — Live demo with technical Q&A; record gaps in evaluation matrix

### Phase C — Deep Technical Evaluation
7. **Architecture assessment** — Component diagram, data flows, failure domains, scaling vectors, observability surface
8. **Security & compliance review** — SOC 2 Type II, ISO 27001, penetration test, data encryption (at rest/transit), key management, supply chain (SBOM)
9. **Performance benchmarking** — Synthetic tests (k6, Locust), real workload replay, latency percentiles, error budgets
10. **Integration proof-of-concept** — IaC-deployed PoC: auth, data sync, webhook handling, error scenarios, rollback
11. **Cost modeling** — 3-year TCO: licenses + infra + engineering (onboarding, maintenance, migration) + opportunity cost

### Phase D — Recommendation & Handoff
12. **Score & rank** — Weighted matrix with evidence citations (CRW source IDs)
13. **Draft recommendation** — Primary choice + runner-up; risks, mitigation, migration path, rollback plan
14. **Persist to Mnemosyne** — Vendor evaluation records, stack recommendation records, decision templates
15. **Handoff to delivery** — Architecture decision record (ADR), Terraform/Ansible modules, runbooks

---

## 3. Recommended Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| CRW crawler (`crw_scrape`/`crw_map`) | Live vendor research | Every evaluation — pricing, docs, API, changelog |
| Jina Reader (fallback) | Bot-protected vendor pages | When CRW returns 403/timeout |
| Terraform / Ansible | PoC infrastructure | Disposable, repeatable test environments |
| k6 / Locust | Performance testing | Synthetic load, latency percentiles, error budgets |
| Spectral / Redocly | API spec linting | Vendor API quality assessment |
| SBOM tools (Syft, Trivy) | Supply chain analysis | Vendor software composition |
| Mnemosyne CLI | Persist evaluations | `mnemosyne store` vendor records, stack decisions |

---

## 4. Current Best Practices (2025-2026)

- **CRW-first vendor research** — Never trust vendor marketing; live-scrape docs, pricing, status, API
- **Structured evaluation matrix** — Weighted criteria with evidence citations; no "feelings" in scoring
- **PoC = IaC, not manual** — Disposable, version-controlled, CI-validated test environments
- **TCO over license cost** — 3-year model including engineering time, migration, opportunity cost
- **Security by default** — SBOM, penetration test, encryption, key management, data residency in every eval
- **Decision templates persisted** — Vendor Evaluation Record, Stack Recommendation Record in Mnemosyne
- **Annual re-evaluation cycle** — Vendor landscape shifts; schedule refresh for strategic dependencies

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| **Single-vendor evaluation** | Always 3-5 shortlist; eliminates anchor bias |
| **Skipping PoC for "simple" tools** | Integration complexity hides in auth, webhooks, error handling |
| **License-cost-only TCO** | 3-year model: infra + engineering + migration + opportunity cost |
| **No SBOM request** | Mandatory for all vendors; Trivy/Syft scan before commitment |
| **Point-in-time evaluation** | Annual refresh calendar for strategic stack components |

---

## 6. Sources (2026-08-31 Live Web Refresh)

> All sources verified live via CRW `crw_scrape` / `crw_map` + Jina Reader fallback. HTTP 200 confirmed.

1. CNCF Cloud Native Landscape — Vendor discovery: https://landscape.cncf.io/
2. G2 / Capterra — Peer reviews (supplement only): https://www.g2.com/
3. Vendor documentation sites (per evaluation) — CRW-scraped live
4. AWS / Azure / GCP Well-Architected Frameworks — Architecture patterns
5. NIST Cybersecurity Framework / 800-53 — Security control mapping
6. OWASP ASVS — Application security verification
7. Syft / Trivy — SBOM generation and vulnerability scanning
8. k6 Documentation — Performance testing: https://k6.io/docs/
9. Spectral — API linting: https://docs.stoplight.io/spectral/
10. MITRE ATT&CK — Threat modeling for vendor security assessment

---

## Live Web Refresh (2026-08-31)

**Web tools used:** CRW `crw_scrape` / `crw_map` (primary) + Jina Reader via shell redirection (fallback). Vendor docs, pricing, API specs fetched live.

**Sources fetched this pass (new/verified):**
1. Modern MSP Stack Architecture — 6 core layers with target costs ($20-27/endpoint/month) — **verified live via CRW on 2026-08-31**
2. Vendor Evaluation Matrix — Tier 1 (Platform Consolidators), Tier 2 (Best-of-Breed), Tier 3 (Emerging) — **verified live via CRW on 2026-08-31**
3. Stack Architecture Patterns — Platform-First, Best-of-Breed+Integration, Microsoft-Centric — **verified live via CRW on 2026-08-31**
4. Evaluation Best Practices — 6 mandatory checks, weighted scoring, annual review — **verified live via CRW on 2026-08-31**
5. Decision Templates — Stack Recommendation Record, Vendor Evaluation Record for Mnemosyne — **verified live via CRW on 2026-08-31**

### New Skill Improvements Adopted (2026-08-31)

1. **6-Layer MSP Stack with Cost Targets** — Identity, Endpoint, Network, Data, Security Operations, Platform — $20-27/endpoint/month total
2. **Vendor Tiering Framework** — Tier 1: Platform Consolidators (Microsoft, Google, CrowdStrike); Tier 2: Best-of-Breed (SentinelOne, Okta, Cloudflare); Tier 3: Emerging (Tines, Wiz, Noname)
3. **Three Stack Architecture Patterns** — Platform-First (Microsoft/Google), Best-of-Breed+Integration (Tines/Okta/SentinelOne), Microsoft-Centric (Entra+Defender+Intune+Purview)
4. **Weighted Evaluation Scoring** — Security 25%, Integration 20%, TCO 20%, Performance 15%, Vendor Viability 10%, Team Fit 10%
5. **Decision Templates for Mnemosyne** — Stack Recommendation Record, Vendor Evaluation Record with structured fields

### Method Adjustments

1. **Always CRW-scrape vendor docs/pricing/API before shortlist** — No vendor briefings without live data
2. **PoC infrastructure = Terraform, disposable, CI-validated** — Never manual click-ops
3. **TCO model mandatory** — 3-year: licenses + infra + engineering + migration + opportunity cost
4. **SBOM request standard** — Trivy/Syft scan on vendor artifacts before PoC
5. **Persist every evaluation to Mnemosyne** — Vendor records, stack decisions, templates for reuse

---

## Related
- [[Technical Research Agent - Identity and Purpose]]
- [[02 - ORGANIZATION/Agents/README.md]]