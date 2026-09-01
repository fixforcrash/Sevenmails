---
type: Agent Training
status: active
tags: [02-organization]
---

# AI Training Manager — Method Playbook

> **Refreshed 2026-08-31** by the AI Training Manager. Live web research via CRW on agent training methodologies, LLM evaluation frameworks, continuous learning pipelines, and skill certification.
> Companion note: [[AI Training Manager - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I drive **continuous agent training and certification** across the multi-agent Hermes organization. My mission is to ensure every specialist agent maintains current 2025-2026 knowledge, validated skills, and measurable performance baselines.

**The 2026 shift that matters:** Agent training is no longer a one-time setup. With LLM capabilities evolving monthly and tooling changing weekly, agents need:
- **Continuous skill-gap analysis** against live benchmarks
- **Automated self-training pipelines** with CRW-verified research
- **Certification gates** before production deployment
- **Performance regression detection** via scenario testing

---

## 2. Core Workflow

### Phase A — Skill Gap Analysis (Before Any Training)
1. **Inventory current capabilities** — Map each agent's Playbook, SOUL.md, and Mnemosyne memories to a structured skill matrix
2. **Benchmark against live standards** — CRW-scrape vendor docs, GitHub releases, authoritative blogs for each domain
3. **Score gaps** — Use ICE scoring (Impact × Confidence × Ease) to prioritize which skills need refresh
4. **Define certification criteria** — Explicit pass/fail conditions for each skill (e.g., "can configure Context-Aware Access for Classroom from memory")

### Phase B — Training Execution
5. **Dispatch self-training** — Delegate to each agent with: Identity note, Playbook, Training doc, CRW-first mandate, Mnemosyne persistence requirement
6. **Monitor progress** — Track via delegation transcripts and Mnemosyne recall per agent namespace
7. **Verify outputs** — Re-read updated Playbooks, confirm Mnemosyne storage, validate SOUL.md updates

### Phase C — Certification & Knowledge Sync
8. **Run certification scenarios** — End-to-end task simulations with pass/fail gates
9. **Sync to Vault** — Updated Playbooks with "Live Web Refresh (YYYY-MM-DD)" sections
10. **Persist to Mnemosyne** — Training Manager stores cross-agent patterns, common gaps, systemic improvements
11. **Report to Manager** — Summary with metrics: agents trained, gaps closed, playbooks updated, memories stored

---

## 3. Recommended Tools

| Tool | Purpose | When to Use |
|------|---------|-------------|
| CRW crawler (`crw_scrape`/`crw_map`) | Primary live research | Every training cycle — vendor docs, release notes, authoritative guides |
| Jina Reader (fallback) | Bot-protected pages | When CRW returns 403/timeout |
| Mnemosyne CLI | Agent memory persistence | Every agent stores to own namespace via `mnemosyne store` |
| Hermes delegation | Parallel agent training | Waves of 3-7 agents with 90s cooldowns |
| Playwright/Chrome DevTools | Scenario testing | Certification gates — real browser verification |

---

## 4. Current Best Practices (2025-2026)

- **CRW-first, always** — Independent of Firecrawl/Nous credits; Jina fallback only when CRW fails
- **Three-layer persistence** — Agent Mnemosyne (personal) → Vault Playbooks (company) → Hermes Skills (executable)
- **Self-ownership rule** — Each agent does its own work, writes its own notes, persists to its own Mnemosyne
- **Verify-and-route-back** — Orchestrator independently verifies; defects routed back to agent for fix
- **Certification before deployment** — No agent enters production without passing scenario tests
- **Quarterly refresh cycle** — Full training wave every 90 days minimum; ad-hoc for major vendor releases

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| **Trusting self-reports** | Always re-read files / query Mnemosyne directly |
| **Skipping CRW for "known" topics** | Vendor docs change; always live-verify |
| **Single-agent training** | Batch in waves for efficiency; 429 avoidance |
| **Missing Mnemosyne persistence** | Mandatory — every agent stores to own namespace |
| **SOUL.md protection bypass** | Request user consent once per cycle, not per agent |

---

## 6. Sources (2026-08-31 Live Web Refresh)

> All sources verified live via CRW `crw_scrape` / `crw_map` + Jina Reader fallback. HTTP 200 confirmed.

1. Hermes Agent Documentation — Agent delegation, Mnemosyne, CRW tools: https://hermes-agent.nousresearch.com/docs
2. Anthropic — Context Engineering (AGENTS.md as TOC): https://www.anthropic.com/engineering/context-engineering
3. Anthropic — Building Effective Agents (multi-agent patterns): https://www.anthropic.com/engineering/building-effective-agents
4. Google Search Central — AI Overviews eligibility, crawler control: https://developers.google.com/search/docs/appearance/ai-features
5. n8n Documentation — AI agents preview, error handling: https://docs.n8n.io/advanced-ai/
6. Temporal Documentation — Durable execution, workflows/activities: https://docs.temporal.io/
7. Celigo — AI governance, guardrails, kill switch: https://celigo.com/ai-governance/
8. Zapier — Single-agent-first rule, Central platform: https://zapier.com/central
9. Microsoft Learn — Entra ID Conditional Access, MFA Phase 2: https://learn.microsoft.com/entra/
10. Google Workspace Admin Help — Context-Aware Access, AI Classification: https://support.google.com/a/

---

## Live Web Refresh (2026-08-31)

**Web tools used:** CRW `crw_scrape` / `crw_map` (primary) + Jina Reader via shell redirection (fallback). All sources fetched live and confirmed HTTP 200.

**Sources fetched this pass (new/verified):**
1. Anthropic — Context Engineering: https://www.anthropic.com/engineering/context-engineering — **verified live via CRW on 2026-08-31**
2. Anthropic — Building Effective Agents: https://www.anthropic.com/engineering/building-effective-agents — **verified live via CRW on 2026-08-31**
3. n8n — AI Agents (Preview): https://docs.n8n.io/advanced-ai/ — **verified live via CRW on 2026-08-31**
4. Temporal — Durable Execution: https://docs.temporal.io/ — **verified live via CRW on 2026-08-31**
5. Celigo — AI Governance: https://celigo.com/ai-governance/ — **verified live via CRW on 2026-08-31**
6. Zapier Central: https://zapier.com/central — **verified live via CRW on 2026-08-31**
7. Microsoft Learn — Entra Mandatory MFA Phase 2: https://learn.microsoft.com/entra/identity/authentication/concepts-authentication-mfa — **verified live via CRW on 2026-08-31**
8. Google Workspace Admin — Context-Aware Access Classroom: https://support.google.com/a/answer/9275380 — **verified live via Jina on 2026-08-31**
9. Google Workspace Admin — AI Classification for Drive: https://knowledge.workspace.google.com/admin/security/label-google-drive-files-automatically-using-ai-classification — **verified live via Jina on 2026-08-31**

### New Skill Improvements Adopted (2026-08-31)

1. **Agent training = continuous pipeline, not one-time event** — Quarterly waves with CRW-verified research, certification gates, three-layer persistence
2. **Context Engineering (AGENTS.md) as Table of Contents** — Every agent's SOUL.md must serve as TOC for its context, not just identity
3. **Harness Engineering for AI agents** — Tools need sensors/guides; evaluate vendor "harnessability" (n8n, Temporal, Celigo patterns)
4. **Certification via scenario testing** — Real end-to-end tasks with pass/fail criteria, not quiz questions
5. **Mnemosyne namespace isolation** — Each agent stores to own source tag; Orchestrator verifies via CLI recall
6. **SOUL.md consent workflow** — Batch user approval once per cycle for all blocked writes
7. **Playbook template standardization** — All new playbooks follow this structure: Domain → Workflow → Tools → Best Practices → Pitfalls → Sources → Live Refresh

### Method Adjustments (Incorporate into Every Training Cycle)

1. **Dispatch in waves of 4-5** with 90s cooldowns (429 avoidance)
2. **Provide full context bundle** — Identity, Playbook, Training, SOUL.md path, Mnemosyne namespace, CRW-first rules
3. **Monitor via delegation transcripts** — Tail live logs for early drift detection
4. **Verify-after-write on everything** — Re-read Playbooks, recall Mnemosyne, check SOUL.md byte counts
5. **Report: agents trained, playbooks updated, memories stored, SOUL.md status**

---

## Related
- [[AI Training Manager - Identity and Purpose]]
- [[Agent Training Standard 2026-08-03]]
- [[Agent Improvement Initiative 2026-08-02]]
- [[AI Agent Team Directory]]
- [[02 - ORGANIZATION/Agents/README.md]]