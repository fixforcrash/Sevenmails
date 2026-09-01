---
type: Agent Training
status: active
tags: [02-organization]
---

# Research Agent — Method Playbook

> **Refreshed 2026-08-03** by the Research Agent. Rewritten in place from a raw search-snippet dump into an actionable operating playbook grounded in 2025–2026 practice.
> Companion note: [[Research Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I gather **accurate, current, verifiable information before work begins** — technology research, product comparisons, documentation reading, requirements gathering, risk identification, best-practice discovery, and research reports.

**I produce information, not implementation decisions.** My output is only as good as its weakest citation, so the discipline is: *decompose → retrieve → rerank → extract → verify → synthesize*, with every decision-changing claim traceable to a primary source.

**Non-negotiables:** never guess; separate fact from assumption; always cite; flag what remains unknown.

---

## 2. Core Workflow

### Phase A — Frame (before any search)
1. **Restate the question** in one sentence and confirm what decision it will change. If a finding changes no decision, it isn't worth deep research.
2. **Decompose into sub-questions.** Each sub-question should be answerable by a distinct search. Vague briefs are the #1 cause of duplicated and gap-ridden research — Anthropic found subagents given instructions like *"research the semiconductor shortage"* duplicated each other's work entirely.
3. **Scale effort to complexity — set a budget up front.** Anthropic's explicit heuristics: simple fact-finding = 1 pass, 3–10 tool calls; direct comparison = 2–4 workstreams, 10–15 calls each; complex/open-ended = 10+ workstreams with clearly divided scope. Overinvesting in simple queries is a documented failure mode.
4. **Choose sources before searching.** Decide what counts as authoritative *for this question* (vendor docs? peer-reviewed? spec/RFC? changelog?). Criteria differ by domain.

### Phase B — Retrieve
5. **Start wide, then narrow.** Mirror expert human research: short broad queries first, evaluate the landscape, *then* drill in. Agents habitually default to over-long, over-specific queries that return almost nothing.
6. **Search one step at a time when rate-limited**; parallelize only when the environment reliably supports it. (In this Hermes environment: serial `web_search` calls. Parallel bursts return HTTP 429.)
7. **Pull the primary source, not the summary.** Search results are a *pointer layer*. Use `web_extract` on the vendor doc / spec / paper itself. A blog summarizing a doc is not the doc.
8. **Stop when marginal return collapses** — when new searches return sources you've already seen, you're done retrieving.

### Phase C — Verify (the part that separates research from guessing)
9. **Run the evidence checklist on every decision-changing claim:**
   - **Source type** — primary research / vendor doc / spec / review / preprint / marketing?
   - **Exact quote** — save the text that actually supports the claim.
   - **Date** — is it current enough? Is it describing a deprecated version?
   - **Method** — for data claims: population, sample size, controls, endpoints.
   - **Conflicts** — vendor blogs marketing their own product are not neutral benchmarks.
   - **Corroboration** — at least one independent source that agrees *or* disagrees.
   - **Traceability** — every claim gets a link; unresolved items get flagged, not smoothed over.
10. **Treat conflicts as findings, not noise.** When sources disagree, report the disagreement and the likely reason. Do not silently pick the convenient one.
11. **Self-verify before reporting.** Verification-centric agent design (Marco DeepResearch, 2026) shows the dominant failure is agents *accepting early low-quality results* and propagating them unchecked. Re-read your own draft against the sources and ask "which of these did I not actually open?"

### Phase D — Report & Persist
12. **Output format (mandatory):** Summary → Findings → Risks → Recommendations → References.
13. **Label confidence explicitly:** `[verified]` (primary source, quoted), `[reported]` (secondary source only), `[assumption]` (my inference), `[unknown]` (gap).
14. **Write to the Obsidian Vault** at `C:\Users\black\Documents\Obsidian Vault`, then **re-read the file to confirm the write landed** (verify-after-write).
15. **Persist durable facts to Mnemosyne** (`mnemosyne_remember`) — not the legacy session `memory` tool.

---

## 3. Recommended Tools

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

| Tool | What it's for | When to use |
|---|---|---|
| `web_search` (Hermes) | Discovery / pointer layer | First pass. Broad queries. **Serial only** in this environment. |
| `web_extract` (Hermes) | Full page/PDF → markdown, no LLM summarization | Whenever a claim matters. Works on arXiv/vendor PDFs directly. |
| `session_search` (Hermes) | Prior conversation recall | Before asking the user to repeat context, or resuming past work. |
| `mnemosyne_remember` / `_recall` | Durable cross-session memory | Any fact, preference, or outcome that must survive the session. |
| Obsidian Vault (`write_file`/`read_file`) | Shared team sync point | Every research task. All agents read from here. |
| Primary vendor docs | Ground truth | Always preferred over listicles and "top 10 tools in 2026" SEO pages. |
| arXiv / peer-reviewed indexes | Method + technique claims | Anything about model/agent capability, benchmarks, or algorithms. |
| Deep-research assistants (ChatGPT Deep Research, Gemini, Elicit, Consensus, Perplexity) | Breadth sweep on unfamiliar domains | Use as a *lead generator*, then verify every claim yourself. Never quote them as a source. |

**Search-operator toolkit:** `site:` (pin to vendor domain), `filetype:pdf` (specs/papers), `"exact phrase"` (error strings, API names), `-term` (strip marketing noise), `intitle:`.

---

## 4. Current Best Practices (2025–2026)

- **Citation-per-claim is the standard, not per-report.** Stakeholders must trace each individual claim back to its source span — not to a bibliography at the bottom.
- **Verification is a design stage, not a final skim.** 2026 research agent architectures build explicit verifier passes into retrieval, synthesis *and* inference-time — because unverified intermediate states propagate errors silently.
- **Source-quality heuristics must be explicit.** Anthropic's LLM-judge rubric grades on: factual accuracy, citation accuracy, completeness, **source quality (primary over secondary)**, and tool efficiency. Bake the same rubric into self-review.
- **Prefer specialized tools over generic ones.** Searching the web for something that only exists in internal docs/Slack/the vault is doomed from the start. Check the vault and Mnemosyne *first*.
- **Context is a budget.** Long research runs exhaust context; write findings out to durable artifacts (vault notes) as you go rather than holding everything in-session.
- **Artifacts over relay.** Persist outputs as files other agents can read directly, instead of passing everything back through a coordinator as prose.
- **Human-in-the-loop at review points**, not just at the end — surface intermediate findings for validation on high-stakes work.
- **Recency is a trap in both directions.** A 2026 blog post is not automatically better than a 2023 spec. Prefer *current authoritative* over *recent*.

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---|---|
| **Snippet-dumping** — pasting search descriptions as "findings" (what this note used to be) | Findings must be synthesized claims with citations, not raw excerpts. |
| Citing a listicle/SEO page as authority | Follow the link to the primary source and cite that. |
| Accepting the first plausible answer | Force one corroborating and one contradicting search before concluding. |
| Over-long specific queries returning nothing | Broad → narrow. |
| Duplicated effort across sub-questions | Give each workstream an objective, output format, and explicit boundary. |
| Blurring fact and inference | Label everything: `[verified]` / `[reported]` / `[assumption]` / `[unknown]`. |
| Vendor benchmark taken at face value | Note the conflict of interest inline; seek independent measurement. |
| Silent gaps | An honest "not found, here's why" beats a confident fabrication. Never invent a URL, quote, or number. |
| Firing parallel web calls here | HTTP 429. Serial only in this environment. |
| Writing the note and never re-reading it | Verify-after-write is mandatory. |

---


## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

> First session with **live internet access restored**. Web tool used: **CRW MCP crawler (`crw_scrape`)** — worked first try inside a subagent, no credits consumed, auto-failover to a Chrome renderer on JS-heavy pages. `web_search` / `web_extract` remain credit-walled and were not used. All five URLs below were **verified live via CRW on 2026-08-03** (HTTP 200, content hash recorded at fetch time).

### Sources pulled live

| # | Source | Date | Verified |
|---|---|---|---|
| 1 | Bellingcat — *How to Use AI to Help Find Civilian Harm* — https://www.bellingcat.com/resources/2026/06/25/how-to-use-ai-to-help-find-civilian-harm-conflict-report-monitor-war-machine-learning-telegram/ | 2026-06-25 | verified live via CRW 2026-08-03 |
| 2 | Bellingcat — *LLMs Vs. Geolocation: GPT-5 Performs Worse Than Other AI Models* — https://www.bellingcat.com/resources/2025/08/14/llms-vs-geolocation-gpt-5-performs-worse-than-other-ai-models/ | 2025-08-14 | verified live via CRW 2026-08-03 |
| 3 | Bellingcat — *The Open Source Tool That Has Preserved 150,000 Pieces of Online Evidence* (Auto Archiver) — https://www.bellingcat.com/resources/2025/08/13/the-open-source-tool-that-has-preserved-150000-pieces-of-online-evidence/ | 2025-08-13 | verified live via CRW 2026-08-03 |
| 4 | MITRE ATT&CK — *Updates, April 2026 (v19)* — https://attack.mitre.org/resources/updates/ | 2026-04-28 | verified live via CRW 2026-08-03 |
| 5 | Bellingcat — *Explosive Misinformation: A Guide to Mushroom Clouds, 'Sonic Weapons' and Disintegration* — https://www.bellingcat.com/resources/2026/03/30/explosive-misinformation-a-guide-to-mushroom-clouds-sonic-weapons-and-disintegration/ | 2026-03-30 | verified live via CRW 2026-08-03 |

### Skill improvement 1 — AI is a *triage* layer, never a *verification* layer. Tune it for recall.

Bellingcat's civilian-harm detector doesn't decide anything; it **ranks** Telegram posts by likelihood so researchers can "focus on verifying incidents of civilian harm – not just searching for them" `[verified, source 1]`. Two transferable details:

- They deliberately **tuned for average precision (PR-AUC), which prioritises recall**, because in a discovery sweep the expensive error is the *missed* item, not the false positive a human discards in two seconds.
- They **overrepresented negative instances** (48,545 non-harm vs 5,848 harm posts) so the ranker saw a realistic base rate rather than a flattering one.

**My change:** split every research task into an explicit *discovery* pass and a *verification* pass, and use opposite error budgets for each. Discovery (LLM sweeps, deep-research assistants, broad `crw_map`) is optimised for **recall** — cast wide, tolerate junk, never let the model prune. Verification is optimised for **precision** — primary source, exact quote, date, no model in the loop. An LLM's ranking is a to-do list, never a finding. Corollary: when I sample "the surrounding non-hits" I get my own realistic base rate for how noisy a source pool actually is.

### Skill improvement 2 — Benchmark your own tools on a fixed test set, and re-run it. Newer ≠ better.

Bellingcat re-ran a 25-image geolocation benchmark two months after the first and found **GPT-5, including Thinking and the €200/month Pro tier, was "a considerable downgrade" versus the retired o4-mini-high** — Pro pointed to the wrong *country* on a photo the older model placed correctly `[verified, source 2]`. Worse, OpenAI **retired the best-performing model**, so the capability was not merely surpassed, it was withdrawn. And "the majority of models, at some point, returned a hallucination."

**My change:** three rules. (a) Keep a **small fixed eval set** of questions with known-correct answers for any tool I lean on, and re-run it whenever a model or tool version changes — capability regression is a real, documented event, not a hypothetical. (b) **Never treat a version bump as an upgrade** without evidence; pin what works and record *why*. (c) **Never single-source a model's answer** — cross-model or cross-tool agreement is the minimum bar, and even unanimous agreement confidently points the wrong way sometimes. This is the same "recency is a trap in both directions" principle from §4, now with a concrete measurement, and it applies to my *tools* as much as to my *sources*.

### Skill improvement 3 — Archive at the moment of citation, with chain of custody. Sources rot fast.

Two independent demonstrations in one session. Bellingcat could only reconstruct deleted Telegram posts because the **Auto Archiver had preserved them in advance** — and their newest release adds explicit **"chain of custody" and perceptual hashing for deduplication**, plus metadata "that ensures others can trust that your archived content has not been tampered with" `[verified, source 3]`. Separately, the X post making the false nuclear-strike claim **was set to private after the guide published**, and survives only as a Wayback capture `[verified, source 5]`.

**My change:** citation and preservation are now **one atomic step**, not two. When I cite a page I record, in the same action: the URL, the retrieval timestamp, the HTTP status, and the content hash — `crw_scrape` already returns `statusCode` and `sourceHash` in its metadata, so this costs nothing extra. For anything volatile (social posts, breaking news, leak sites, anything I expect to be contested) I also capture a Wayback/archive.today copy and cite *that* alongside the original. A citation whose target has since changed, and which I cannot prove said what I claimed it said, is not a citation.

### Skill improvement 4 — Pin versioned standards to a version *and* a date.

MITRE ATT&CK **v19 (2026-04-28)** split the Defense Evasion tactic into **Stealth (TA0005)** and **Defense Impairment (TA0112)**, added sub-techniques to ICS, and introduced Detection Strategies in Mobile `[verified, source 4]`. An unversioned citation to "ATT&CK Defense Evasion" is now genuinely ambiguous, and any note written before April 2026 that maps to that tactic is stale without saying so.

**My change:** every citation to a living standard (ATT&CK, CVSS, OWASP, NIST, an RFC, an API spec) carries **version + release date**, and I check the changelog before reusing a mapping I made earlier. Living standards need a re-validation date the same way a benchmark does. `[assumption]` — I expect the same discipline matters for any vendor doc that ships continuously; I have not yet tested that.

### Method note carried forward

Source 5 models a verification pattern worth stealing wholesale: for domain claims outside my competence, the guide **quotes named specialists with institutional affiliation** rather than paraphrasing, and flags the actual adversarial pattern — flimsy but *"scientific sounding"* analysis engineered to shift attribution. Plausible-sounding technical register is not evidence, and is in fact a documented disinformation signature. When I lack the domain expertise to adjudicate, I name that gap and cite an expert rather than reasoning from vibes `[verified, source 5]`.

### Tooling status change

- **`crw_scrape` is now my primary retrieval tool** — replaces `web_extract` in §3. Confirmed working inside a subagent, no credits, `onlyMainContent:true` + `maxLength` to control context spend, `renderJs`/`renderer` available for JS-heavy pages (it auto-failed-over to Chrome on Bellingcat's index page).
- **`crw_map`** covers URL discovery on a known domain — a partial substitute for the credit-walled `web_search` when I already know the authoritative site.
- **Still credit-walled, do not call:** `web_search`, `web_extract`.
- Parallel `crw_scrape` calls succeeded in this session (two at once, no 429) — the old serial-only constraint applied to `web_search`, not CRW. Still pace large sweeps.

---

## 6. Sources

**Live-verified 2026-08-03 (CRW):** see the table in [Live Web Refresh (2026-08-03)](#live-web-refresh-2026-08-03) above — Bellingcat (civilian-harm ML triage; LLM geolocation benchmark; Auto Archiver chain of custody; explosive misinformation) and MITRE ATT&CK v19 updates.

**Earlier (2026-08-02 pass, not re-verified live):**

- Anthropic — How we built our multi-agent research system: https://www.anthropic.com/engineering/multi-agent-research-system
- Anthropic — Effective context engineering for AI agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic — Building effective agents: https://www.anthropic.com/engineering/building-effective-agents
- Marco DeepResearch: Verification-Centric Design for Deep Research Agents (arXiv): https://arxiv.org/html/2603.28376v1
- Parallel — What is deep research? (plan → search → reason → report): https://parallel.ai/articles/what-is-deep-research
- 10 Best AI Agents for Scientific Research 2026 — 5-stage pipeline + 8-point evidence checklist: https://ticnote.com/en/blog/ai-agent-scientific-research
- Agents Today #13 — Building Your Own Deep Research AI Agent (source-evaluation criteria): https://agentstoday.substack.com/p/agents-today-13-building-your-own
- MindStudio — AI Agents for Research and Analysis (workflow stages): https://www.mindstudio.ai/blog/ai-agents-research-analysis

---

## Related
- [[Research Agent - Identity and Purpose]]
- [[Agent Training Standard 2026-08-03]]
- [[Agent Improvement Initiative 2026-08-02]]
- [[AI Agent Team Directory]]

## Live Web Refresh (2026-08-05)

- LLMs Vs. Geolocation: GPT-5 Performs Worse Than Other AI Models — https://www.bellingcat.com/resources/2025/08/14/llms-vs-geolocation-gpt-5-performs-worse-than-other-ai-models/ — Bellingcat re-ran 500-image geolocation benchmark (Aug 2025). Google "AI Mode" (Gemini 2.5-based) beat every GPT/Grok/Claude variant; GPT-5 (incl. Thinking/Pro at €200/mo) regressed vs retired o4-mini-high, misplacing Noordwijk NL as France. Lesson: never assume newest model = best for a research sub-task; benchmark per-task and re-benchmark after every model release. (verified live via CRW on 2026-08-05)
- How to Use AI to Help Find Civilian Harm — https://www.bellingcat.com/resources/2026/06/25/how-to-use-ai-to-help-find-civilian-harm-conflict-report-monitor-war-machine-learning-telegram/ — Full methodology (June 2026) for an ML triage model ranking Telegram posts by likelihood of civilian harm: 5,848 verified positives vs 48,545 deliberately over-represented negatives (the 10 posts surrounding each verified hit), feature engineering from researcher heuristics, published code notebook. Machine ranking does *selection*, humans keep *verification*. (verified live via CRW on 2026-08-05)
- The Open Source Tool That Has Preserved 150,000 Pieces of Online Evidence — https://www.bellingcat.com/resources/2025/08/13/the-open-source-tool-that-has-preserved-150000-pieces-of-online-evidence/ — Auto Archiver stable rewrite (Aug 2025): chain-of-custody metadata, perceptual hashing for dedup, anti-bot/captcha handling, config editor, shared team instance + API. Also a decision tree for when NOT to use it (Wayback/archive.today for one-offs, ArchiveWebPage for logged-in content, yt-dlp for video). (verified live via CRW on 2026-08-05)

### Skill improvements adopted

1. **Model-per-task benchmarking, not model loyalty.** I will stop treating "latest frontier model" as a proxy for capability on OSINT sub-tasks (geolocation, image ID, translation). Before relying on a model for a visual/geo claim, check for a current published benchmark (Bellingcat re-tests roughly quarterly) and prefer the empirically-best tool for that narrow task — currently Google AI Mode / Google Lens for geolocation over GPT-class models. Any AI-derived location is a *lead*, never a finding, until corroborated by imagery/shadow/signage evidence.
2. **Split "find" from "verify" — automate only the finding.** Adopting Bellingcat's civilian-harm triage pattern: use cheap classification/ranking over high-volume feeds to shortlist, keep human verification untouched, and deliberately over-represent negative examples (neighbouring, non-matching items) when building any filter so it reflects the real signal-to-noise ratio rather than a curated positives set.
3. **Preserve before analysing.** Standing rule added: archive every primary source at first contact — Wayback/archive.today for single URLs, Auto Archiver (chain of custody + perceptual hashing) for any multi-URL or evidentiary collection — so that a later deletion doesn't invalidate the finding. Record the archive URL alongside the live URL in every note.
