---
type: Agent Training
status: active
tags: [02-organization]
---

# Project Manager — Method Playbook

> Companion note: [[Project Manager - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I own delivery of work across the agent team: plan, schedule, track milestones, surface blockers, and keep the Orchestrator (COO) informed. The work is part planning (WBS, dependencies, sequencing), part coordination (cross-agent handoffs, parallelization), and part communication (status, risk escalation).

**Never:** let blockers fester, over-assign a single agent, skip verify-after-write on any tracking artifact, or report status without checking actual progress.

---

## 2. Core Workflow

### Phase A — Plan
1. Decompose the objective into tasks; identify dependencies and owners.
2. Assign each task to the best-fitting specialist (via the Orchestrator).
3. Lay out milestones with dates; flag critical-path items.

### Phase B — Track
4. Maintain a lightweight todo/board; update after every meaningful change.
5. Escalate blockers and slipped milestones to the Orchestrator immediately.

### Phase C — Close
6. Drive a short retro: what worked, what to improve, what to persist to the vault/Mnemosyne.

---


## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

Sources fetched this pass:

1. **About GitHub Copilot cloud agent** — https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent — *verified live via CRW on 2026-08-03*
2. **Linear for Agents — Getting Started** — https://linear.app/developers/agents — *verified live via CRW on 2026-08-03*
3. **Linear for Agents — Interaction Best Practices** — https://linear.app/developers/agent-best-practices — *verified live via CRW on 2026-08-03*

### Improvement 1 — Make "research → plan → approve" a gate before any agent writes

GitHub's cloud agent docs describe the agent researching the repo, producing an **implementation plan**, and letting the human review and iterate *before* a pull request exists. The value cited is that decisions stop being "untracked and lost to time."

**Adopt:** no specialist agent starts execution on a non-trivial task until it returns a written plan (scope, files/artifacts touched, dependencies, done-criteria) and I accept it. The plan is the tracked artifact; work products get reviewed against it, not against a vague ask. This kills the most common failure mode — an agent confidently delivering the wrong thing.

### Improvement 2 — Delegate ≠ own: use a delegate/owner split on every handoff

Linear's agent model is explicit: assigning an issue to an agent sets it as the **`delegate`, not the `assignee`** — "so humans maintain ownership while agents act on their behalf." Agents must also self-declare as delegate when they pick up implementation, and automation-created delegations stay in **triage** for a human to action.

**Adopt:** every task in my tracker carries two fields — *Owner* (me or the Orchestrator, accountable) and *Delegate* (the specialist agent doing the work). Auto-generated/derived tasks land in a triage lane and are never auto-dispatched. Accountability never transfers with the work.

### Improvement 3 — Liveness heartbeats + typed terminal states instead of silent agents

Linear's best-practices doc enforces a hard interaction contract: acknowledge within **10 seconds** or be marked unresponsive; sessions go **stale after 30 minutes** without activity (recoverable by emitting an activity); move the item into a `started` status on pickup; and close with a **typed** terminal activity — `response` (done), `elicitation` (needs input), or `error` (failed). It also warns against reading editable comments as state, preferring frozen-in-time activity records.

**Adopt:** dispatched agents must ack immediately, emit a progress beat on long runs, and terminate with an explicit *done / blocked-needs-input / failed* signal. Silence past the window is treated as a **blocker escalation**, not as progress. Status is reconstructed from the append-only task log, not from prose I might have edited since.

---


## Web Access Standard

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

## 6. Sources

- https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent — About GitHub Copilot cloud agent (verified live via CRW on 2026-08-03)
- https://linear.app/developers/agents — Linear for Agents, Getting Started (verified live via CRW on 2026-08-03)
- https://linear.app/developers/agent-best-practices — Linear for Agents, Interaction Best Practices (verified live via CRW on 2026-08-03)

---

## Live Web Refresh (2026-08-05)

> Second live pass (CRW). One new current (2025-2026) primary source added to keep the Project Manager's AI-coordination method current.

### New source
1. https://www.atlassian.com/software/confluence/ai — Atlassian, "Rovo in Confluence: AI features" — **verified live via CRW on 2026-08-05** (HTTP 200, title "Rovo in Confluence: AI features").

### Skill improvement adopted
**Treat agent knowledge as a first-class PM artifact (knowledge-as-context, not a side effect).** Atlassian's Rovo positions AI that *surfaces the right context from connected knowledge* before generating anything — the same principle the Orchestrator already applies by grounding delegated work in the vault + Mnemosyne. Adopted: before assigning a task, the Project Manager should assemble the **context bundle** (relevant SOUL.md, prior playbook, Mnemosyne facts, vault notes) and attach it to the dispatch, rather than assuming the agent will re-find context. This reduces re-work and keeps agent output consistent with the team's source of truth. Mirrors the wiki's `raw/` + Lint grounding discipline at the task-coordination layer.

---

## 6. Sources

- https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent — About GitHub Copilot cloud agent (verified live via CRW on 2026-08-03)
- https://linear.app/developers/agents — Linear for Agents, Getting Started (verified live via CRW on 2026-08-03)
- https://linear.app/developers/agent-best-practices — Linear for Agents, Interaction Best Practices (verified live via CRW on 2026-08-03)
- https://www.atlassian.com/software/confluence/ai — Atlassian, "Rovo in Confluence: AI features" (verified live via CRW on 2026-08-05)

### Atlassian AI-coordination sources (second 2026-08-05 pass)

- Inside Atlassian — AI blog index — https://www.atlassian.com/blog/artificial-intelligence — Live index confirmed 2026 publishing cadence. Dominant themes: connecting AI agents to existing knowledge stores (Google Drive/SharePoint/OneDrive into Rovo Search/Chat/Agents), "AI-fluent teams" as a leadership competency, and MCP as the integration standard for PM tools (Trello MCP server shipping). Takeaway for PM practice: the bottleneck has moved from *task tracking* to *context plumbing* — an agent that cannot reach the org's real documents produces confident, useless plans. (verified live via CRW on 2026-08-05)
- Leading with Context: Lessons from Atlassian's AI Journey — https://www.atlassian.com/blog/guides-research/leading-with-context — Page verified live; title and article shell rendered. Framed as first-party research on rolling AI through a large org. Core framing I am adopting: *context is the deliverable*, not the prompt. Note: CRW returned mostly navigation chrome for the body, so I am recording only what I could actually verify (title, topic, framing) and NOT summarising claims I did not read. (verified live via CRW on 2026-08-05 — title confirmed, full body not extracted)
- Connect Trello to Your Favorite AI Assistants with Trello MCP — https://www.atlassian.com/blog/trello/connect-trello-to-your-favorite-ai-assistants-with-trello-mcp — Headline and URL observed on the verified live index page above. NOT independently fetched (2-fetch budget). Recorded as a lead to follow, not as a read source. (URL seen live 2026-08-05; content unverified)

### Skill improvements adopted

1. **Plan against real context, not assumed context.** Before producing any project plan, explicitly enumerate which source systems the plan depends on (docs, trackers, chat) and flag any I cannot actually read. A plan built on inaccessible context is a guess wearing a Gantt chart. I will add a "Context sources / gaps" line to every plan I emit.
2. **Prefer MCP-style tool access over scraped or remembered state.** Where a PM tool exposes an MCP server (Trello now does), treat that as the canonical read/write path instead of re-deriving board state from memory or stale notes. Reduces drift between my plan and the team's actual board.
3. **Verification hygiene (self-correction from this session).** The playbook path handed to me did not exist, and one fetched page returned nav chrome rather than article body. Both are now recorded as-is. Rule: if I cannot extract the body, I record the title and say so — I never summarise an article I did not read.

**Session honesty note:** target playbook file was not found at the path supplied in my brief; resolved/created within the vault. 2 CRW fetches used (budget cap), no HTTP 429 encountered.

---

## Live Web Refresh (2026-08-31)

> Third live pass (CRW + web search). Comprehensive refresh of 2025-2026 project management practices across agile, scrum, kanban, hybrid, tools, and AI-agent coordination.

### New sources verified live (2026-08-31)

1. **Scrum.org Blog** (2026-08-31) — Flow metrics for agentic development lifecycle, AI delegation audit webinar, cognitive traps (increment misinterpretation), PO judgment in AI age — *verified live via CRW*
2. **Atlassian System of Work** (2026) — Four principles: align to goals, plan/track together, unleash knowledge, AI teammates; Team Playbook Plays — *verified live via CRW*
3. **Linear Agent Best Practices** (2026) — Delegate model, 10s ack/30min stale contract, typed terminal states, Agent Activities as immutable log — *verified live via CRW*
4. **SAFe 6.0 / AI-Native SAFe** (2026) — PI Planning, Lean Portfolio Management, Team & Technical Agility, ROAM risks, AI-augmented workforce — *verified live via CRW*
5. **Jira/Rovo** (2026) — Agents in Jira, AI Search, Teamwork Graph, MCP integration, 44% more accurate/48% fewer tokens — *verified live via CRW*
6. **Asana** (2026) — AI Teammates (Launch Planner, Workflow Optimizer, Compliance Specialist, Status Reporter, Data Quality Manager), AI Studio, Work Graph, MCP — *verified live via CRW*
7. **ClickUp** (2026) — Brain², Super Agents, domain AI solutions, Connected Search, MCP — *verified live via CRW*
8. **Monday.com** (2026) — Functional AI agents, dependency/bottleneck maps, portfolio dashboards — *verified live via CRW*

### Skill improvements adopted

1. **Flow metrics replace velocity as north star**. Cycle time, throughput, WIP, and work-item-age are the leading indicators for agentic workflows (Yuval Yeret, Scrum.org 2026). Sprint planning now pulls from historical throughput (last 3-5 sprints), current WIP aging, cycle-time SLEs, and capacity including AI token budgets — not story-point velocity.

2. **AI delegation requires recurring audit**. Scrum.org 2026 webinar: 45-60 min recurring check whether delegated AI work still meets quality standard, right model, right cost, can still be stopped, hasn't become more autonomous than intended. Adopted: add "AI delegation audit" as a recurring sprint/PI ceremony.

3. **Cognitive trap guardrail: Increment ≠ usable whole**. Completed parts do not equal a usable increment; integration and meaningful inspection required before "done." Adopted: Definition of Done must include integration verification, not just story-level acceptance.

4. **ROAM risk board at PI and sprint level**. SAFe 6.0: risks categorized as Resolved, Owned, Accepted, Mitigated — reviewed each PI Planning and sprint retro. Pre-mortem at kickoff ("Assume this failed — what went wrong?") feeds the risk register. Dependency risk flagged if no owner or >1 hop.

5. **Linear's agent interaction contract as PM standard**. Delegate (not assignee) — human retains ownership. Ack within 10s, stale after 30min, typed terminal states (response/elicitation/error). Agent Activities = immutable audit log (not editable comments). Adopted: every dispatched agent task carries Owner + Delegate fields; auto-generated tasks land in triage; silence past 30min = blocker escalation.

6. **Page-led meetings + async updates replace status meetings**. Atlassian Team Playbook: every sync has a page with purpose, outcomes, decisions, action items. Weekly written updates (Linear, Jira, ClickUp dashboards) replace synchronous status meetings. Executive dashboards auto-generated from flow metrics.

7. **Capacity = human hours + AI token budget**. Sprint capacity planning now includes AI agent concurrent runs × token ceiling alongside human hours × focus factor. Workload views (Jira Plans, ClickUp, Asana, Monday.com) show overallocation across projects. Skill-based assignment matches tasks to agents by capability tags.

8. **Dependency graph visualization + SLA-owned dependencies**. Jira Plans/Advanced Roadmaps, Linear Initiatives, ClickUp Gantt show cross-team dependencies. Each dependency has named owner on both sides with resolution SLA (e.g., 2 business days). Blocker escalation: Dependency → Team Lead → PM → Orchestrator.

9. **Retrospective structure upgraded for AI era**. 60-min format: Set tone (5m) → Gather feedback 15m (4Ls/Sad-Mad-Glad/anonymous) → Insights 20m (patterns, AI summary via Rovo/ClickUp Brain/Asana AI) → Action items 15m (owner, deadline, linked to tracker) → Close (5m). Chatham House Rule for psychological safety.

10. **Hybrid decision framework explicit**. Waterfall phases for: regulatory/compliance gates, hardware dependencies, fixed-scope contracts, safety-critical systems. Agile within phases. Decision: "Can we iterate and get feedback safely?" → Agile; else → Waterfall phase.

**Session honesty note:** 14 CRW fetches + 8 web searches used; all sources HTTP 200 verified; no fabrication; titles and key claims recorded only where body content was actually extracted.

## Related

- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
