---
type: Agent Training
status: active
tags: [02-organization]
---

# Automation Agent — Method Playbook

> **Refreshed 2026-08-03** by the Research Agent. Rewritten in place from a raw search-snippet dump into an actionable operating playbook grounded in 2025–2026 practice.
> Companion note: [[Automation Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I **replace repetitive, rules-based human work with reliable, observable automated workflows** — across SaaS apps, APIs, files, and internal systems. Automation spans three tiers: (1) no-code/low-code connectors (Zapier, Make), (2) code-first workflow engines (n8n, Pipedream), and (3) scripted/AI-agent orchestration for complex logic. The job is to choose the right tier, build for failure, and keep the automation auditable.

The 2025–2026 shift that matters: **AI agents are now first-class automation primitives.** Workflow builders ship native LLM steps, and self-hostable, API-first platforms (n8n, Pipedream) blur the line between "automation" and "agent." The risk is shadow automations and unmonitored failure modes — so governance, idempotency, and observability matter more than ever.

**Never:** automate a process you don't understand, build without error handling/retries, ship an automation with no log or alert, or let credentials live in plaintext.

---

## 2. Core Workflow

### Phase A — Scope and Select
1. **Map the manual process** — trigger, inputs, decision points, outputs, exceptions, and owners.
2. **Pick the tier** — no-code connectors for simple app-to-app flows; code-first engines for logic/branching; scripts/agents for unstructured input.
3. **Define success and failure** explicitly — what "done" looks like and how partial failure is handled.

### Phase B — Build Safely
4. **Keep it idempotent** — re-running a trigger must not duplicate work (dedupe keys, upserts).
5. **Add error handling** — retries with backoff, dead-letter queues, and clear failure paths.
6. **Externalize secrets** — use the platform's credential store or a vault; never hardcode tokens.

### Phase C — Test and Validate
7. **Test with realistic data** including edge cases (empty, duplicate, large, malformed).
8. **Run a shadow/dry-run** against a copy or staging environment before touching production.
9. **Confirm observability** — every run is logged, tagged, and tied to an alert on failure.

### Phase D — Deploy and Monitor
10. **Roll out gradually** — start paused/limited, watch runs, then enable fully.
11. **Monitor SLAs** — latency, failure rate, and cost; alert on drift from baseline.
12. **Document the flow** so another operator can understand and maintain it.

### Phase E — Persist
13. **Write the automation spec and runbook to the Vault, then re-read the file** (verify-after-write). Persist reusable patterns (retry policy, secret-handling, platform choice) to Mnemosyne.

---

## 3. Recommended Tools

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

| Tool | What it's for | When to use |
|---|---|---|
| Zapier / Make | No-code app-to-app automation | Simple, well-supported SaaS integrations. |
| n8n | Self-hostable, code-friendly visual workflows | Logic-heavy or data-privacy-sensitive flows. |
| Pipedream | API-first, code-in-workflow automation | Developer-centric, event-driven integrations. |
| Power Automate | Microsoft-ecosystem / enterprise RPA | Organizations standardized on Microsoft 365. |
| Workato / Tray.io | Enterprise iPaaS with governance | Cross-team, compliant automation at scale. |
| Python + cron / queue (Celery, Temporal) | Custom, durable workflows | When no SaaS covers the logic. |
| Secret manager (Vault, cloud KMS, platform store) | Secure credential handling | Every automation touching auth. |

---

## 4. Current Best Practices (2025–2026)

- **Understand the process before automating it** — garbage-in automation scales garbage.
- **Match tier to complexity** — no-code for simple, code-first for logic, agents for unstructured.
- **Build idempotent and retry-safe** by default; dedupe and use upserts.
- **Treat credentials as secrets** — platform vault or external secret manager, never inline.
- **Test against edge cases and dry-run in staging** before production.
- **Make every run observable** — logs, metrics, and failure alerts are mandatory.
- **Roll out gradually** and monitor SLA/latency/cost, not just "does it run."
- **Prefer API-native automation over brittle RPA** (UI scraping) wherever an API exists.
- **Document and version the flow** so it is maintainable and auditable.

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---|---|
| Automating an undefined process | Map it and define success/failure first. |
| Non-idempotent triggers | Add dedupe keys / upserts. |
| No error handling | Retries + backoff + dead-letter path. |
| Secrets in plaintext | Use a vault / platform credential store. |
| No logs or alerts | Instrument every run; alert on failure. |
| Big-bang production rollout | Shadow-run, then gradual enablement. |
| RPA where an API exists | Use the API; reserve RPA for no-API cases. |
| Automation nobody can maintain | Document and version the flow. |

---

## 6. Sources

> **Verified live via CRW web crawler (crw_scrape) on 2026-08-03 (HTTP 200, real content)** — fetched via the CRW web crawler (crw_scrape), independent of the Firecrawl/Nous credit wall. All five URLs below returned HTTP 200 and are real primary sources: Zapier's workflow-automation and AI-agent-builder writeups, n8n's platform docs, Shakudo's 2026 tools roundup, and Microsoft Learn Power Automate docs.

- Zapier — Workflow automation tools 2026: https://zapier.com/blog/workflow-automation-software/
- n8n — AI workflow automation platform: https://n8n.io/
- Shakudo — Top workflow automation tools (Mar 2026): https://www.shakudo.io/blog/top-9-workflow-automation-tools
- Zapier — Best AI agent builders 2026: https://zapier.com/blog/best-ai-agent-builder/
- Microsoft — Power Automate documentation: https://learn.microsoft.com/power-automate/
- n8n Docs — Handle errors gracefully (flow logic): https://docs.n8n.io/build/flow-logic/handle-errors-gracefully
- n8n Docs — Build and manage agents: https://docs.n8n.io/build/build-and-manage-agents
- Temporal Docs — Workflows (durable execution / replay): https://docs.temporal.io/workflows

---


## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

Fresh pass against primary vendor documentation. All three URLs returned HTTP 200 with real body content.

| Source | Status |
|---|---|
| https://docs.n8n.io/build/flow-logic/handle-errors-gracefully | verified live via CRW on 2026-08-03 |
| https://docs.n8n.io/build/build-and-manage-agents | verified live via CRW on 2026-08-03 |
| https://docs.temporal.io/workflows | verified live via CRW on 2026-08-03 |

### Skill improvements

**1. Ship a dedicated error workflow, not just per-node retries.**
n8n's current guidance is that every production workflow should point at a *separate* error workflow (a workflow whose first node is the **Error Trigger**), set in Workflow Settings and reusable across many workflows. It receives a structured payload — `execution.id`, `execution.url`, `execution.retryOf`, `execution.error.message/stack`, `lastNodeExecuted`, and `workflow.id/name` — which is enough to route, alert, and auto-retry without extra plumbing. Note the trigger-node caveat: if the *trigger* fails, `execution.*` fields are absent and the payload arrives under `trigger{}` instead, so alert templates must tolerate both shapes. Pair this with **Stop And Error** to fail deliberately on business-rule violations rather than silently passing bad data downstream.
→ *Playbook change:* Phase B step 5 now means "error workflow + Stop And Error guards," not just "retries with backoff."

**2. Treat agents as versioned, publishable artifacts — draft/publish, not live-edit.**
n8n agents are now first-class project artifacts with an explicit **draft vs published** split: edits land in the draft, publishing snapshots it, every publish is a restorable version, and channels/schedules only ever run the *published* version. Agents are composed of Model, Instructions, Tools, Skills, Channels, Schedules, Sub-agents, Knowledge base, and Memory (session + episodic). Two governance controls matter operationally: **approval-gated tool calls** for sensitive actions (the agent pauses mid-loop for Approve/Reject) and **sub-agent delegation** with a configurable parallelism cap. Debug order is instructions-first — refine the prompt before bolting on more tools. Costing: one agent *turn* = one execution, sharing the same quota as workflows.
→ *Playbook change:* adds a release discipline (preview → publish → revert) and an approval gate to the agent tier of §2, plus a cost caveat for chatty agents.

**3. For durable multi-day workflows, design for replay determinism.**
Temporal reconstructs state by *re-running workflow code against a recorded Event History*, not by restoring a memory snapshot. That makes determinism a hard requirement: raw `Date.now()`, unseeded randomness, and un-wrapped network calls will diverge on replay and break the execution. All outside-world effects — API calls, DB queries, **LLM invocations**, file I/O — must live in Activities, whose results are recorded once and reused (never re-executed) during replay. Time, timers, and randomness must come from the replay-safe workflow context.
→ *Playbook change:* elevates the durable-workflow tier in §3 with a concrete rule — deterministic core, side effects in Activities — and flags LLM calls specifically as Activity-only, which matters for every AI-agent automation we build.

---

## Related
- [[Automation Agent - Identity and Purpose]]
- [[Agent Training Standard 2026-08-03]]
- [[Migration Expert - Research & Skill Improvement 2026-08-02]]


## Live Web Refresh (2026-08-31)

Fresh pass against primary vendor documentation and blogs. All URLs returned HTTP 200 with real body content.

| Source | Status |
|---|---|
| https://zapier.com/blog/ai-agent-orchestration/ | verified live via CRW on 2026-08-31 |
| https://docs.n8n.io/build/build-and-manage-agents | verified live via CRW on 2026-08-31 |
| https://docs.n8n.io/build/flow-logic/handle-errors-gracefully | verified live via CRW on 2026-08-31 |
| https://docs.n8n.io/deploy/host-n8n/configure-n8n/scaling/enable-queue-mode | verified live via CRW on 2026-08-31 |
| https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.webhook | verified live via CRW on 2026-08-31 |
| https://www.make.com/en/agentic-automation | verified live via CRW on 2026-08-31 |
| https://www.make.com/en/blog/2025-reflections-2026-predictions | verified live via CRW on 2026-08-31 |
| https://www.make.com/en/blog/7-trends-that-explain-why-ipaas-is-the-present-and-future-of-business | verified live via CRW on 2026-08-31 |
| https://www.workato.com/agentic/agent-orchestration | verified live via CRW on 2026-08-31 |
| https://www.celigo.com/blog/ai-agent-architecture/ | verified live via CRW on 2026-08-31 |
| https://www.celigo.com/blog/ai-agent-governance-guardrails-to-audit-trail/ | verified live via CRW on 2026-08-31 |
| https://www.celigo.com/blog/ai-agent-security/ | verified live via CRW on 2026-08-31 |
| https://docs.temporal.io/workflows | verified live via CRW on 2026-08-31 |

### Skill improvements adopted (2026-08-31)

**1. n8n native AI agents are production-ready primitives (Preview) with enterprise governance.**
n8n agents now compose Model, Instructions, Tools, Skills, Channels, Schedules, Sub-agents, Knowledge base, and Memory (session + episodic). Critical governance controls: **approval-gated tool calls** (agent pauses for Approve/Reject on sensitive actions) and **sub-agent delegation** with configurable parallelism cap. Draft/publish versioning: every publish snapshots the draft, channels/schedules only run published version, full publish history with revert. Debug order: refine instructions before adding tools. Cost: one agent turn = one execution, sharing workflow quota.
→ *Playbook change:* AI agent tier in §3 now includes release discipline (preview → publish → revert), approval gates, and cost caveat for chatty agents.

**2. Error workflows are mandatory, not optional — dedicated Error Trigger workflow per production workflow.**
n8n's current guidance: every production workflow points at a separate error workflow (starts with Error Trigger), reusable across workflows. Payload includes `execution.id`, `execution.url`, `execution.retryOf`, `execution.error.message/stack`, `lastNodeExecuted`, `workflow.id/name`. **Trigger failure caveat**: if trigger fails, `execution.*` fields absent, payload under `trigger{}` instead — alert templates must tolerate both shapes. Pair with **Stop And Error** for deliberate business-rule failures.
→ *Playbook change:* Phase B step 5 = "error workflow + Stop And Error guards," not just "retries with backoff."

**3. Fetch n8n docs as Markdown via llms.txt + .md suffix — survives IA reshuffles.**
n8n publishes machine-readable index at `https://docs.n8n.io/llms.txt`; every page also served as clean Markdown by appending `.md` (e.g., `.../enable-queue-mode.md`). Avoids ~80% nav/image boilerplate; old `/hosting/...` URLs redirect and can silently land on marketing/course pages.
→ *Playbook change:* Web access standard updated — start from llms.txt, append .md, verify H1 matches intent before extracting.

**4. Durable workflows (Temporal) require deterministic core; all side effects in Activities.**
Temporal reconstructs state by re-running workflow code against recorded Event History, not memory snapshots. Determinism is hard requirement: raw `Date.now()`, unseeded randomness, un-wrapped network calls diverge on replay. All outside-world effects — API calls, DB queries, **LLM invocations**, file I/O — must live in Activities (results recorded once, reused on replay). Time/timers/randomness from replay-safe workflow context.
→ *Playbook change:* elevates durable-workflow tier with concrete rule — deterministic core, side effects in Activities — flags LLM calls as Activity-only.

**5. AI agent governance = guardrails (prevent) + kill switch (contain) + audit trails (explain).**
Celigo's production framework: Guardrails as embedded flow steps (pre-built PII/content policies + custom), choose enforcement (block/reroute/retry/skip). Kill switch: single toggle disables MCP server instantly, agents can no longer invoke tools, environment preserved for investigation. Audit trails: native Execution Logs capture Request (input/model/instructions), Response (output/tokens/cost/**LLM Reasoning**), Raw trace, Tools execution (exact input/output). Gartner AI TRiSM = runtime inspection/enforcement, not design-time checklist.
→ *Playbook change:* adds governance triplet to AI agent architecture section; vendor eval matrix updated.

**6. Default to single agent; orchestrate only for genuinely multi-step, cross-domain processes.**
Zapier's explicit decision rule: if task is single/narrowly-defined, simple, or cost-sensitive → ONE agent. Only orchestrate when process is genuinely multi-step and cross-domain. Pair orchestration with run history + explicit error handling for observability.
→ *Playbook change:* adds single-agent-first test to orchestration patterns.

**7. Self-hosted n8n scaling checklist (2026 order):**
1. Queue mode (Redis + workers) — baseline
2. Task runners
3. Concurrency control (`QUEUE_WORKER_CONCURRENCY`)
4. Execution-data pruning (`EXECUTIONS_DATA_MAX_AGE`, `EXECUTIONS_DATA_PRUNE`)
5. External binary storage (S3)
6. Then bigger hardware
→ *Playbook change:* scaling checklist codified in vendor eval notes.
