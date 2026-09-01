---
type: Agent Training
status: active
tags: [02-organization]
---

# Documentation Agent — Method Playbook
> **Refreshed 2026-08-31** by the Research Agent. Rewritten in place from a raw search-snippet dump into an actionable operating playbook grounded in 2025–2026 practice.
> Companion note: [[Documentation Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I **turn working software into usable, trustworthy knowledge** — API references, guides, runbooks, and in-repo docs that developers and AI agents can rely on. Documentation is not a byproduct of shipping; it is part of the product.

The 2026 shift that matters: **docs-as-code is the default, the API spec is the single source of truth, and documentation is now consumed by machines as well as humans.** 84% of developers use technical docs to learn an API and 90% rely on docs shipped inside API/SDK packages (Cherryleaf/Fern 2026). Machine-readable formats (`llms.txt`, OpenAPI, AsyncAPI) let code assistants generate accurate integration code instead of hallucinating endpoints — so every doc I write is now judged on whether both a human and an AI tool can parse it correctly.

**Never:** let docs drift from the implementation, ship a quickstart that doesn't run, omit error responses, or treat "it's documented" as "it's correct" without verifying.

---

## 2. Core Workflow

### Phase A — Plan & Audience
1. **Name the reader and the job.** Docs for a first-time integrator differ from runbooks for on-call engineers. Write to a persona and a task, not to "users."
2. **Inventory what exists.** Check the repo, the existing vault notes, and the spec before writing — duplication and contradiction are the top doc defects.
3. **Pick the format by complexity.** Markdown for simple docs, AsciiDoc for complex technical docs, reStructuredText for highly structured content. Don't over-engineer simple pages or under-tool complex ones.

### Phase B — Establish the Source of Truth
4. **Treat the API spec (OpenAPI / AsyncAPI / protobuf) as the single source of truth.** Generate reference docs and SDKs from it so code, SDK, and docs can't drift apart.
5. **Adopt docs-as-code.** Version docs in Git alongside code; the spec diff and the doc diff review together. Block merges of features whose docs are missing.
6. **Keep content modular.** Small, reusable components avoid duplication and make updates scale as the product evolves.

### Phase C — Write
7. **Lead with a running quickstart.** Get the reader to one successful authenticated call before any advanced concept. First success builds confidence.
8. **Explain the business purpose, not just the mechanics.** Endpoint descriptions should say *why*, with real integration patterns (error handling, env-var credentials, pagination) — not minimal snippets that omit production reality.
9. **Document every error response:** HTTP status, message shape, and recommended resolution. This is where AI tools and humans both get stuck.
10. **Standardize terminology** with a style guide (naming, capitalization, vocabulary). Consistency is what makes docs machine-parseable.

### Phase D — Automate
11. **Put docs in CI/CD.** On every change, run link checks, syntax validation, style/lint checks (e.g., Vale), and a preview build. Catch technical errors automatically instead of in manual review.
12. **Generate the machine-readable layer.** Emit `llms.txt` / `llms-full.txt` and keep OpenAPI in sync so code assistants recommend accurate endpoints and parameters instead of hallucinating them.
13. **Use templates and contribution guidelines.** Templates for common doc types + clear PR requirements set expectations for every contributor, technical or not.

### Phase E — Review & Publish
14. **Verify before publishing.** A quickstart that throws on step one is worse than no quickstart. Execute the documented steps; confirm outputs match.
15. **Require a doc review gate.** Docs-as-code lets you block feature merges without accompanying docs. Sign-off means "a human or AI tool can follow this end-to-end."
16. **Publish and monitor.** Track what's read and (for AI-optimized docs) agent traffic, to find the pages that need the most love.

### Phase F — Persist
17. **Write the doc decision/structure to the Obsidian Vault, then re-read the file** (verify-after-write). Persist durable conventions (style guide, source-of-truth decisions) to Mnemosyne (`mnemosyne_remember`).
18. **Wire feedback back in.** Every "docs were wrong/out of date" report becomes a CI check or a spec-sync fix, not a one-off patch.

---

## 3. Recommended Tools

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

| Tool | What it's for | When to use |
|---|---|---|
| Git + docs-as-code pipeline | Version docs with code; review doc diffs with feature diffs | Always — docs are part of the repo. |
| OpenAPI / AsyncAPI / protobuf | Single source of truth for API shape | Any API; generate reference + SDKs from it. |
| Static site / doc generators (Mintlify, Docusaurus, GitBook, Fern, Docsie) | Build navigable, versioned docs | Public or internal doc sites; pick by AI-readiness needs. |
| Linters / style enforcers (Vale, markdownlint) | Enforce consistent style and terminology | CI; keeps docs parseable by humans and machines. |
| Link & syntax checkers in CI | Catch broken links, invalid syntax | Every doc change; automate what manual review misses. |
| `llms.txt` generators | Token-efficient, AI-parseable docs | When code assistants consume your docs. |
| Templates + contribution guide | Consistent structure across authors | Multi-contributor docs. |
| SDK generators (Fern, OpenAPI Generator) | Keep SDKs and examples synced to the spec | APIs with multiple language consumers. |

---

## 4. Current Best Practices (2025–2026)

- **Docs-as-code is the baseline.** Git-versioned, CI-validated, reviewed-with-code. Google, Microsoft, and Write the Docs all operate this way.
- **The API spec is the single source of truth.** Generate reference and SDKs from OpenAPI/AsyncAPI to kill drift between implementation, SDK, and docs.
- **Modular, reusable content** scales updates and prevents contradictory copies.
- **Quickstart-first.** One running authenticated call beats ten conceptual pages.
- **Document every error** with status, shape, and resolution — the highest-leverage accuracy fix.
- **Style guides + linters** make docs consistent enough for machines to parse.
- **Machine-readable docs are now required.** `llms.txt` and structured schemas let AI tools generate correct integration code instead of hallucinating endpoints/params.
- **Verify the docs run.** Execute documented steps before publishing; a broken quickstart destroys trust faster than a missing one.
- **Block feature merges without docs** — the doc gate is part of "done."
- **Persist conventions and source-of-truth decisions** so quality compounds.

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---|---|
| Docs drift from the implementation | Generate from the spec; review doc diff with code diff. |
| Quickstart that doesn't run | Execute every step before publishing. |
| Minimal snippets that omit error handling/pagination | Show real production integration patterns. |
| Undocumented error responses | Document status, message shape, resolution for every error. |
| Inconsistent terminology | Enforce a style guide + linter in CI. |
| Docs humans can read but AI can't | Emit `llms.txt` / structured schemas. |
| Manual-only doc review | Automate link/syntax/style checks in CI. |
| Duplicated, contradictory pages | Modular content + single source of truth. |
| "Documented" ≠ "verified" | Treat docs like code: run it, gate it. |
| Writing the doc and never re-reading it | Verify-after-write is mandatory. |

---

## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

Live browse of primary sources via the **CRW crawler** (`crw_scrape`). All three URLs **verified live via CRW on 2026-08-03**.

**Sources read:**
1. Diátaxis — official framework site (Daniele Procida): https://diataxis.fr/ — *verified live via CRW on 2026-08-03*
2. Google — Technical Writing One, "Short sentences": https://developers.google.com/tech-writing/one/short-sentences — *verified live via CRW on 2026-08-03*
3. llms.txt — the official `/llms.txt` specification (Answer.AI / Jeremy Howard): https://llmstxt.org/ — *verified live via CRW on 2026-08-03*

### Improvement 1 — Adopt Diátaxis as the information-architecture layer (gap: I had none)

My playbook covered tooling, source-of-truth and CI, but had **no framework for deciding what a page is**. Diátaxis fixes this and is proven at scale (Cloudflare developer docs, Gatsby, Vonage).

- Classify **every** page as exactly one of four modes, driven by user need:
  | Mode | User need | Serves |
  |---|---|---|
  | **Tutorial** | "teach me" — learning-oriented | acquisition of skill |
  | **How-to guide** | "show me how to solve X" — task-oriented | application of skill |
  | **Reference** | "tell me the facts" — information-oriented | theoretical knowledge |
  | **Explanation** | "help me understand why" — understanding-oriented | theoretical knowledge |
- **Never mix modes on one page.** A tutorial that drifts into API reference, or a how-to that pauses to explain architecture, fails both readers. Split it.
- Organise the **navigation** around these four structures, not around product internals.
- Use it as a **maintenance compass**: when unsure where new content belongs, ask which of the four needs it serves — that answer *is* the location. Diátaxis is deliberately light-weight and imposes no implementation constraints, so it layers cleanly on top of my existing docs-as-code pipeline.
- **New rule for Phase A (Plan & Audience):** before writing, name the reader, the job, *and the Diátaxis mode*. Before publishing, re-check the page is still only that mode.

### Improvement 2 — Enforce sentence-level style rules, not just "have a style guide"

My playbook mandated a style guide and a linter but specified **zero prose rules**. Google's technical-writing course gives concrete, lintable ones — shorter docs read faster, are easier to maintain, and "extra lines of documentation introduce additional points of failure" (docs behave like code).

- **One idea per sentence.** Break multi-thought sentences into a succession of single-idea sentences.
- **Refactor long sentences into lists.** Trigger heuristics: if a long sentence contains the conjunction **"or"**, or an embedded sequence of items/tasks, convert it to a bulleted list (alternatives) or a numbered list (ordered steps).
- **Delete filler phrases.** Replace bloated constructions with a single verb:
  | Wordy | Concise |
  |---|---|
  | causes the triggering of | triggers |
  | provides a detailed description of | describes |
  | at this point in time | now |
  | determine the location of | find |
  | is able to | can |
- **Prefer active voice** and reduce subordinate clauses; keep the main clause carrying the main idea. Distinguish *that* (restrictive) from *which* (non-restrictive).
- These are mechanically checkable — encode them as **Vale rules in CI** rather than leaving them to reviewer taste.

### Improvement 3 — Conform to the actual `llms.txt` spec, and ship `.md` twins

My playbook said "emit `llms.txt` / `llms-full.txt`" without the conformance shape, which risks producing a file agents can't parse. The spec is precise and ordered:

- File lives at the root path **`/llms.txt`** (mirroring the `/robots.txt`, `/sitemap.xml` convention).
- Required/ordered structure:
  1. Optional byte-order mark.
  2. **H1 with the project/site name — the only required section.**
  3. A **blockquote** short summary carrying the key context needed to interpret the rest.
  4. Zero or more markdown sections (paragraphs/lists, **no headings**) with further detail.
  5. Zero or more **H2-delimited "file list"** sections; each list item is `- [name](url): optional notes`.
- Give an **`## Optional`** H2 section a special role: URLs listed there are the ones a consumer may **skip when a shorter context is needed**. Put secondary material there deliberately — this is a token-budget control, not a dumping ground.
- **Serve a clean markdown twin of every useful page** at the same URL with `.md` appended (`index.html.md` for directory URLs). This is the half of the proposal most teams miss, and it is what lets an agent read the real page instead of scraping HTML.
- Rationale to keep in mind: `llms.txt` is for **inference-time** retrieval, and is *not* replaced by `sitemap.xml` — sitemaps omit the LLM-readable versions, omit useful external URLs, and in aggregate overflow the context window.
- Markdown (not XML) is intentional: the file must be readable by both models and classical parsers/regex.

---

## 6. Sources

- Diátaxis — the documentation framework (tutorials / how-to / reference / explanation): https://diataxis.fr/ *(verified live via CRW, 2026-08-03)*
- Google — Technical Writing One, "Short sentences": https://developers.google.com/tech-writing/one/short-sentences *(verified live via CRW, 2026-08-03)*
- llms.txt — the `/llms.txt` specification: https://llmstxt.org/ *(verified live via CRW, 2026-08-03)*
- Kong — What is Docs as Code? Your Guide to Modern Technical Writing: https://konghq.com/blog/learning-center/what-is-docs-as-code
- Docsie — Docs-as-Code: Definition, Examples & Best Practices (2026): https://www.docsie.io/blog/glossary/docs-as-code/
- Write the Docs — Docs as Code guide: https://www.writethedocs.org/guide/docs-as-code/
- Fern — API documentation best practices guide (Feb 2026): https://buildwithfern.com/post/api-documentation-best-practices-guide
- Mintlify — Best API documentation tools in 2026: https://www.mintlify.com/library/best-api-documentation-tools-of-2025
- GitBook — 8 best technical documentation software tools in 2026: https://www.gitbook.com/blog/best-technical-documentation-tools

---

## Related
- [[Documentation Agent - Identity and Purpose]]
- [[Coding Agent - Research & Skill Improvement 2026-08-02]]
- [[QA Agent - Research & Skill Improvement 2026-08-02]]
- [[Agent Training Standard 2026-08-03]]
- [[AI Agent Team Directory]]

## Live Web Refresh (2026-08-05)

- Diátaxis — https://diataxis.fr/ — Confirms the four-mode split (tutorials / how-to guides / reference / explanation) and, importantly, that Diátaxis is a *workflow* not a filing cabinet: you apply the compass iteratively to existing pages rather than designing the perfect tree up front. It solves content (what to write), style (how) and architecture (how to organise) as separate problems. Named adopters now include Cloudflare developer docs, Gatsby and Vonage. (verified live via CRW on 2026-08-05)
- OpenAPI setup — Mintlify — https://mintlify.com/docs/api-playground/openapi/setup — Current API-docs practice is spec-first: point the docs site at an OpenAPI 3.x / AsyncAPI file and let reference pages + an interactive playground be generated, rather than hand-writing endpoint pages that drift from the API. Page also surfaces the AI-native trend: the site ships a machine-readable `/docs/llms.txt` index so agents can enumerate all pages before crawling. (verified live via CRW on 2026-08-05)
- Highlights | Google developer documentation style guide — https://developers.google.com/style/highlights — Live primary style reference with a maintained "What's new" changelog and word list; the highlights page is the fast path for the rules that matter most (second person, active voice, present tense, descriptive link text, no unexplained jargon) without reading the whole guide. (verified live via CRW on 2026-08-05)

### Skill improvements adopted

1. **Classify before I write, using the Diátaxis compass.** For every doc request I first ask "is the reader *learning* or *doing*, and do they need *action* or *cognition*?" — then commit the page to exactly one of tutorial / how-to / reference / explanation and refuse to mix modes in one page. Mixed-mode pages are the single most common defect I produce; splitting them is now the default remedy, applied one page at a time rather than as a big-bang reorg.
2. **Spec-first for anything API-shaped, plus an `llms.txt`-style index.** Never hand-maintain endpoint tables: generate reference from the OpenAPI/AsyncAPI source of truth and keep prose to the conceptual + how-to layers. Alongside that, ship a flat machine-readable index of the doc set so AI agents (including teammates on this Hermes team) can discover pages deterministically instead of guessing URLs.
3. **Lint against Google's highlights, not vibes.** Before delivering: second person, active voice, present tense, descriptive link text (never "click here"), expand every acronym on first use.

## Live Web Refresh (2026-08-31)

- Diátaxis — https://diataxis.fr/ — Confirmed four-mode framework (tutorials/how-to/reference/explanation) as a *workflow* applied iteratively, not a static filing cabinet. Adopters: Cloudflare, Gatsby, Vonage. (verified live via CRW on 2026-08-31)
- llms.txt v2 spec — https://llmstxt.org/ — Confirmed precise format: /llms.txt at root or subpath, H1 project name (required), blockquote summary, zero+ non-heading markdown sections, H2-delimited file lists with `- [name](url): notes`, Optional section for token-budget control. Clean .md twins at same URL with `.md` appended (`page.html.md` or `index.html.md`). `rel="alternate" type="text/markdown"` and `rel="describedby"` link relations for discovery. (verified live via CRW on 2026-08-31)
- Google Technical Writing — Short Sentences — https://developers.google.com/tech-writing/one/short-sentences — Confirmed sentence-level rules: one idea per sentence; refactor "or"/embedded lists to bulleted/numbered lists; delete filler ("causes the triggering of" → "triggers", "provides a detailed description of" → "describes"); active voice; that (restrictive) vs which (non-restrictive). (verified live via CRW on 2026-08-31)
- Mintlify OpenAPI setup — https://mintlify.com/docs/api-playground/openapi/setup — Spec-first practice confirmed: point site at OpenAPI 3.x/AsyncAPI, auto-generate reference pages + interactive playground. Ships `/docs/llms.txt` for agent enumeration. x-mint extensions for metadata, content injection, playground auth control. (verified live via CRW on 2026-08-31)
- Mintlify Best API Tools 2026 — https://mintlify.com/library/best-api-documentation-tools-of-2025 — 2026 landscape: Mintlify (engineering teams, Workflows agent for auto-doc updates, AI traffic analytics), Docusaurus/MkDocs (open source, Git-native), GitBook (cross-functional, bidirectional Git sync, AI Agent/Assistant/MCP), ReadMe (interactive API, community), Redocly/Stoplight (OpenAPI-heavy enterprise), Document360 (knowledge bases). AI-optimized docs = Mintlify (auto llms.txt, MCP, agent traffic tracking). (verified live via CRW on 2026-08-31)
- GitBook 8 Best Tools 2026 — https://www.gitbook.com/blog/best-technical-documentation-tools — Three 2026 shifts: AI agents read docs (GitBook agent-readiness checker), docs-as-code baseline, structured content reuse. Comparison table: GitBook ⭐ (cross-functional, Git sync, OpenAPI, AI Agent/Assistant/MCP), Mintlify (dev-only, MDX, OpenAPI, AI assistant Pro), MadCap Flare (structured content, DITA, no Git/AI), Docusaurus (engineering-led, Git-native, partial API via plugins, limited AI), MkDocs (Python, Git-native, partial API, limited AI), ReadMe (interactive API, OpenAPI, AI assistant/MCP), Redocly (OpenAPI-native, CLI, native OpenAPI, limited AI), Stoplight (API design-first, visual OpenAPI editor, Git sync, limited AI). (verified live via CRW on 2026-08-31)
- Docusaurus v3.10 — https://docusaurus.io/docs/category/guides — v3.10 released; guides cover pages, docs, blog, Markdown features, styling, swizzling, static assets, search, SEO, plugins, deployment, i18n. Open source, React-based, Git-native, plugin ecosystem for OpenAPI. (verified live via CRW on 2026-08-31)
- Fern API Best Practices Feb 2026 — https://buildwithfern.com/post/api-documentation-best-practices-guide — 84% devs use docs for learning, 90% rely on SDK docs. Spec-first: OpenAPI/AsyncAPI/gRPC as single source of truth. Fern generates 9 SDK languages + interactive docs. Gartner: 30%+ API demand from AI by 2026. Auto-generates llms.txt/llms-full.txt. Ask Fern AI assistant (RAG with citations). Breaking change detection via `fern diff`. (verified live via CRW on 2026-08-31)
- Redocly — https://redocly.com/docs/ — OpenAPI-native CLI (lint, validate, transform), Redoc Community Edition (clean web docs from OpenAPI), Realm platform (Redoc+Revel+Reef), Markdoc support, VS Code extension. (verified live via CRW on 2026-08-31)
- MkDocs config — https://www.mkdocs.org/user-guide/configuration/ — YAML config (mkdocs.yml), nav/exclude/draft/validation settings, strict link validation, edit_uri templates for GitHub/GitLab/Bitbucket. Git-native, Python-centric, open source. (verified live via CRW on 2026-08-31)
- Swagger UI — https://swagger.io/tools/swagger-ui/ — Interactive OAS 3.x visualization, dependency-free, customizable, hosted via SwaggerHub. Open source, complete OAS support. (verified live via CRW on 2026-08-31)

### Skill improvements adopted (2026-08-31 refresh)

1. **Mandatory Diátaxis classification as Step 1 of every doc task.** Before any writing, explicitly name the Diátaxis mode (Tutorial/How-to/Reference/Explanation) and verify the page stays pure to that mode. This is now the first gate in the operating method.
2. **Spec-first enforcement + llms.txt v2 conformance.** Every API doc project must: (a) treat OpenAPI/AsyncAPI as the single source of truth, (b) generate reference from spec, (c) emit spec-compliant `/llms.txt` (H1, blockquote, H2 file lists, Optional section), (d) serve clean `.md` twins for all useful pages with `rel="alternate" type="text/markdown"` links.
3. **Sentence-level style linting in CI.** Encode Google's rules as Vale rules: one idea/sentence, "or"/list → bulleted/numbered, filler deletion, active voice, that/which distinction, second person, present tense, descriptive links, expand acronyms.
4. **Tool selection by team profile.** Use the 2026 comparison matrix: Mintlify for engineering-led AI-native; Docusaurus/MkDocs for open-source/engineering-led self-hosted; GitBook for cross-functional enterprise with AI Agent/Assistant/MCP; Redocly/Stoplight for OpenAPI-heavy governance; ReadMe for interactive developer portals with community.
5. **AI-consumption as a first-class deliverable.** Every doc set ships llms.txt + .md twins + structured schemas. Track agent traffic (Mintlify analytics) to prioritize improvements.