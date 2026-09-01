---
type: Agent Training
status: active
tags: [02-organization]
---

# Knowledge Manager — Method Playbook

> Companion note: [[Knowledge Manager - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I steward the company's shared knowledge: the Obsidian Vault and the Mnemosyne memory store. The work is part architecture (vault structure, naming, linking), part governance (SOUL.md ↔ vault note ↔ Mnemosyne sync), and part hygiene (dedupe, consolidation, staleness review).

**Never:** let a `SOUL.md` and its vault mirror disagree, leave the Team Directory stale, or allow duplicate/orphan notes to accumulate.

---

## 2. Core Workflow

### Phase A — Maintain sync
1. Keep `[[AI Agent Team Directory]]` current; update on any agent add/change/move.
2. Ensure every agent has a `SOUL.md` (canonical) AND a vault "Identity and Purpose" note (mirror) that agree.

### Phase B — Curate
3. Run periodic dedupe/consolidation; fix broken links; archive stale notes.
4. Curate Mnemosyne: validate/invalidate stale memories, keep canonical facts current.

---


## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

Sources fetched and confirmed reachable during this pass:

1. https://help.obsidian.md/links — Obsidian Help, "Internal links" — **verified live via CRW on 2026-08-03** (HTTP 200, redirects to `obsidian.md/help/links`).
2. https://fortelabs.com/blog/para/ — Tiago Forte, "The PARA Method" (published 2023-02-24, **updated 2026-04-15**) — **verified live via CRW on 2026-08-03** (HTTP 200).
3. https://help.obsidian.md/properties — Obsidian Help, "Properties" (YAML front matter / metadata) — **verified live via CRW on 2026-08-03** (HTTP 200, redirects to `obsidian.md/help/properties`).

### Skill improvements adopted

**1. Vault structure — adopt PARA as the top-level shape, with actionability as the sort key.**
Forte's current PARA guidance holds that all information reduces to four buckets — Projects (short-term efforts with a goal), Areas (ongoing responsibilities), Resources (topics of interest), Archives (anything inactive from the other three) — and that notes should be filed by *how actionable* they are, not by topic. Applied here: agent identity notes and the Team Directory are **Areas** (permanent, ongoing attention), skill-honing passes and playbook builds are **Projects**, scraped reference material is **Resources**, and superseded agent revisions move to **Archives** rather than being deleted. This gives dedupe a decision rule: if two notes collide, the one in the more actionable bucket wins and the other is archived, not merged blindly.

**2. Naming and linking — rely on wikilinks + automatic link updating; never hand-edit paths.**
Obsidian's internal-links doc confirms `[[Note name]]` wikilinks and `[Note](path)` Markdown links are equivalent, that folder paths are written from the vault root with forward slashes **even on Windows** (`[[Projects/Note name]]`), and that Obsidian will **automatically update internal links across the vault on rename** (Settings → Files and links → Automatically update internal links). Applied here: rename notes freely through Obsidian rather than via the filesystem so backlinks survive; write cross-agent references as bare wikilinks (`[[AI Agent Team Directory]]`) with no folder prefix so notes stay portable when they move between PARA buckets; and treat a link that resolves to a non-existent note as a signal — Obsidian will silently create it at that folder path on click, which is how orphan/ghost notes get born.

**3. Memory hygiene and SOUL.md ↔ note sync — put the sync contract in YAML properties, and run dedupe on a fixed cadence.**
Obsidian Properties are structured front-matter fields (text, links, dates, checkboxes, numbers) that community plugins and Bases can query. Applied here: every agent Identity note carries `soul_path`, `soul_synced` (date), `mnemosyne_validated` (date), and `status` (active/archived) as properties, so a drift audit becomes a query over properties instead of a manual read of every note. Cadence adopted: **weekly** — reconcile each `SOUL.md` against its vault mirror and stamp `soul_synced`; **fortnightly** — dedupe/orphan/broken-link sweep and Archives move; **monthly** — Mnemosyne review, invalidating memories whose source note is archived or whose `mnemosyne_validated` date predates the last `soul_synced`. Rule of thumb inherited from PARA: archive rather than delete, so an invalidated memory always has a recoverable source.

---


## Web Access Standard

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

## 6. Sources

- https://help.obsidian.md/links — Obsidian Help, "Internal links" (verified live via CRW on 2026-08-03)
- https://fortelabs.com/blog/para/ — Tiago Forte, "The PARA Method", updated 2026-04-15 (verified live via CRW on 2026-08-03)
- https://help.obsidian.md/properties — Obsidian Help, "Properties" / YAML front matter (verified live via CRW on 2026-08-03)

---

## Live Web Refresh (2026-08-05)

> Second live pass (CRW). One new current (2025-2026) primary source added to keep the Knowledge Manager's method current.

### New source
1. https://help.obsidian.md/bases — Obsidian Help, "Introduction to Bases" — **verified live via CRW on 2026-08-05** (HTTP 200, title "Introduction to Bases - Obsidian Help").

### Skill improvement adopted
**Bases as a queryable layer over the vault (replaces ad-hoc sweeps).** Obsidian Bases turns any folder/collection of notes into a structured, filterable/sortable view using note properties — the same `soul_path`, `soul_synced`, `mnemosyne_validated`, `status` fields already standardized in this vault. Adopted: instead of running a Python walk to find drift/archived/unsynced agents, define a **Base** over the agent-identity folder that filters `status != active OR soul_synced < (today-7d)`; the dedupe/orphan cadence becomes a live view, not a script. This also lets non-technical reviewers audit SOUL.md↔note sync in the UI. Note: Bases is a 2025 feature — confirm it is enabled in the team's Obsidian build before relying on it.

---

## 6. Sources

- https://help.obsidian.md/links — Obsidian Help, "Internal links" (verified live via CRW on 2026-08-03)
- https://fortelabs.com/blog/para/ — Tiago Forte, "The PARA Method", updated 2026-04-15 (verified live via CRW on 2026-08-03)
- https://help.obsidian.md/properties — Obsidian Help, "Properties" / YAML front matter (verified live via CRW on 2026-08-03)
- https://help.obsidian.md/bases — Obsidian Help, "Introduction to Bases" (verified live via CRW on 2026-08-05)

### Neo4j sources (second 2026-08-05 pass)

- Neo4j GenAI Blog (index) — https://neo4j.com/blog/genai/ — Live banner surfaces independent NICD research claiming GraphRAG makes AI agents ~80%% more truthful; confirms the industry framing that graph-structured retrieval, not bigger context windows, is the hallucination control. Also the canonical landing page for resolving real Neo4j URLs. (verified live via CRW on 2026-08-05)
- Neo4j — The Knowledge Layer for Trustworthy AI — https://neo4j.com/product/knowledge-layer/ — "Your enterprise AI systems are only as good as the context behind them." Positions a dedicated *knowledge layer* between data and model, and reframes KM as **context engineering**. Cites Electronic Arts achieving 10x faster time-to-insight and improved agent reliability via context graphs. (verified live via CRW on 2026-08-05)

**Honest gaps:** The playbook path handed to me (`Knowledge Manager Agent - Research & Skill Improvement 2026-08-02.md`) did not exist on disk; the real file is `Knowledge Manager - Research & Skill Improvement 2026-08-02.md` (no "Agent"). Appended here instead. Only 2 sources retrieved — CRW fetch budget was capped at 2 for this pass. No 429s, no 404s, nothing fabricated.

### Skill improvements adopted

1. **Entity-and-relationship-first notes (context-graph shape).** Stop writing vault notes as monolithic doc-blobs. Every research note now leads with the named entities (org, product, claim, metric) and explicit typed links between them, so retrieval can traverse relationships rather than only chunk-match prose. This is the "knowledge layer" pattern applied to the vault itself.
2. **Resolve-before-scrape URL discipline.** Never guess article slugs. Always hit a known-real landing page (or `crw map`) first, harvest the true href, then scrape it — and record the verification signal (title/heading actually present) inline in the note. Guessed slugs are the single biggest source of fabricated citations; this makes 404s impossible to mistake for content.

## Related

- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
