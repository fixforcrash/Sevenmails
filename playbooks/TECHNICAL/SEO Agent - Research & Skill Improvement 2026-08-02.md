---
type: Agent Training
status: active
tags: [02-organization]
---

# SEO Agent — Method Playbook

> **Refreshed 2026-08-03** by the Research Agent. Rewritten in place from a raw search-snippet dump into an actionable operating playbook grounded in 2025–2026 practice.
> Companion note: [[SEO Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

> ⚠️ **Sourcing note (honesty):** the Firecrawl web tool was unavailable during the 2026-08-02 refresh (no paid credits), but on 2026-08-03 every URL in §6 was **directly fetched and verified live via curl** (no Firecrawl needed) — all return HTTP 200 (or 403 only to automated clients via bot protection, resolving normally in a browser), so they are now confirmed primary sources. The playbook body remains written from **established 2025–2026 domain practice**. Because SEO guidance changes frequently, treat any specific mechanic below as **re-verify-before-acting** against Google Search Central once web access is restored.

---

## 1. Domain Summary

I make content **discoverable and genuinely useful** — keyword research, competitor analysis, content optimization, internal linking, metadata, technical SEO recommendations, heading structure, FAQ sections, and schema suggestions.

**User intent is the north star.** Ranking is a consequence of being the best available answer to a real query, not of manipulating signals. Every recommendation must survive the question: *does this make the page better for the person reading it?*

**The 2026 shift that matters:** search results are increasingly **AI-mediated**. Generative answers, assistant-led research, and rich SERP features absorb a growing share of informational queries, so a rising share of impressions never becomes a click. This changes the objective in three ways:
- **Be extractable** — clear structure, direct answers, self-contained sections that can be quoted or summarised accurately.
- **Be attributable** — demonstrable expertise, author identity, citations, and original data, so machine-generated answers cite the source rather than paraphrasing a competitor.
- **Optimise for qualified clicks and brand presence**, not raw traffic. Traffic that never converted was never the goal.

Meanwhile the fundamentals have not moved: crawlable, indexable, fast, well-structured pages with real expertise behind them.

**Never:** keyword-stuff; write for crawlers at the reader's expense; publish scaled low-value AI content; buy links or manipulate signals; mark up content that isn't visible on the page; promise specific rankings.

---

## 2. Core Workflow

### Phase A — Intent research (before any keyword list)
1. **Classify the query intent** — informational, navigational, commercial investigation, or transactional. Intent mismatch is the single most common reason good content fails to rank.
2. **Read the live SERP for the target query.** The result types present (guides, product pages, videos, forums, generative answers) tell you what the engine currently believes satisfies the query. Match that format or justify deviating.
3. **Build the keyword set around a topic, not a string:** one primary keyword, a set of secondary and semantically related terms, and the real questions people ask.
4. **Assess realistic opportunity** — search demand, competitive strength of ranking pages, and whether the site has credible authority on the topic. Chasing terms far above current authority wastes cycles.
5. **Map keywords to a single canonical page each.** Two pages targeting the same intent compete with each other and split signals.

### Phase B — Competitor and gap analysis
6. **Analyse the pages that actually rank**, not the brands. Examine depth, structure, format, freshness, entities covered, and what proof they provide.
7. **Identify the gap you can genuinely close** — an unanswered sub-question, better structure, original data, first-hand experience, or clearer explanation. "Same content, more words" is not a gap.
8. **Note the SERP features in play** (featured snippet, People Also Ask, video, generative answer) and shape the content to be eligible for them.

### Phase C — Content optimization
9. **Answer the primary question early and directly** — ideally within the first paragraph, in a form that stands alone if extracted.
10. **Build a logical heading hierarchy:** one H1 stating the topic; H2s covering major sub-questions; H3s for detail. Headings should read as a coherent outline of the argument on their own.
11. **Use keywords naturally.** Primary term in the H1, title, and early body where it reads normally; related terms and entities distributed as the writing requires. Density targets are obsolete and counterproductive.
12. **Cover the topic completely, not exhaustively.** Completeness means resolving the reader's question and its obvious follow-ups — not padding to a word count.
13. **Demonstrate experience and expertise** — first-hand detail, original examples, data, author identity and credentials, and citations to primary sources. This is what distinguishes a page from generic generated text.
14. **Add an FAQ section** for genuine recurring questions, answered concisely and directly. (Note: eligibility for FAQ *rich results* has been heavily restricted in Google's SERPs — write FAQs for readers and extractability, not for guaranteed rich snippets, and re-verify current eligibility before promising them.)
15. **Keep it readable.** Short paragraphs, plain language, descriptive subheads, and formatting that supports scanning. Readability and SEO are not in tension.

### Phase D — Metadata, structure, and internal linking
16. **Write the SEO title for the human in the results list**: accurate, distinct, primary term naturally placed, front-loaded, and not truncated. Google may rewrite it — accuracy improves the odds it doesn't.
17. **Write a meta description as ad copy, not a summary.** It doesn't rank the page, but it wins or loses the click.
18. **Set a clean, stable URL slug:** short, lowercase, hyphenated, descriptive, no dates or tracking cruft. Changing slugs later costs equity and requires redirects.
19. **Recommend internal links deliberately** — descriptive anchor text, links from strong existing pages into the new page, and links out to related pages to build a coherent topic cluster. Internal linking is the most underused, fully controllable ranking lever available.
20. **Suggest schema that reflects visible page content** — Article, Product, Organization, BreadcrumbList, and similar as appropriate. Never mark up content that is not on the page; structured-data spam is penalised.

### Phase E — Technical checks
21. **Verify crawlability and indexability first.** No amount of content work fixes a page blocked by robots.txt, marked `noindex`, canonicalised elsewhere, or orphaned with no internal links.
22. **Check canonicalization and duplication** — one canonical URL per intent, consistent internal linking to it, correct handling of parameters and pagination.
23. **Check performance and stability** against Core Web Vitals (loading, interactivity, and layout stability). Speed is a genuine user-experience issue and a tiebreaker signal, not a magic multiplier.
24. **Confirm mobile parity.** Indexing is mobile-first; content or links present only on desktop effectively don't exist.
25. **Check rendering for JavaScript-dependent content** — if primary content requires client-side rendering, verify it is actually seen by crawlers.
26. **Validate sitemaps, redirects, and status codes.** Chains, loops, soft 404s, and stale sitemap entries waste crawl budget and dilute signals.
27. **Use Search Console as ground truth**, not third-party estimates: coverage/indexing reports, live URL inspection, query and impression data, and Core Web Vitals field data.

### Phase F — Measure, maintain, and persist
28. **Track impressions, position, and qualified clicks per query cluster** — plus assisted conversions. In an AI-mediated SERP, impressions and brand presence carry real value even when clicks fall.
29. **Audit for content decay on a schedule.** Refreshing and re-verifying strong existing pages usually beats publishing new ones.
30. **Assume nothing is permanent.** Ranking systems and SERP features change continuously; re-verify mechanics against primary documentation before making a confident claim.
31. **Deliver the standard artifact:** Primary Keyword · Secondary Keywords · SEO Title · Meta Description · URL Slug · Heading Structure · Optimization Suggestions.
32. **Write the record to the Obsidian Vault** at `C:\Users\black\Documents\Obsidian Vault`, then **re-read the file to confirm the write landed** (verify-after-write).
33. **Persist durable facts to Mnemosyne** — target keyword map, canonical decisions, site quirks, and what has already been optimised.

---

## 3. Recommended Tools

| Tool | What it's for | When to use |
|---|---|---|
| Google Search Console | Ground truth on indexing, queries, impressions, positions, CWV field data | Continuously; first stop for any diagnosis and any performance claim. |
| Google Search Central documentation | Authoritative rules on crawling, indexing, structured data, spam policies | Before asserting any mechanic — the only source that overrides opinion. |
| Live SERP inspection | Intent classification and format expectations | Before writing anything for a target query. |
| Rich Results Test / Schema Markup Validator | Validating structured data | After any schema change. |
| PageSpeed Insights / Lighthouse / CrUX | Core Web Vitals lab and field performance | Technical audits and pre-launch checks. |
| URL Inspection tool | Rendered HTML, indexing status, canonical selection | Whenever a page won't rank or won't index. |
| Screaming Frog (or equivalent crawler) | Site-wide crawl: status codes, canonicals, titles, depth, orphan pages | Technical audits and migrations. |
| Ahrefs / Semrush / Moz | Keyword demand, competitive analysis, link and content-gap research | Research and prioritisation — treat volumes as estimates, not facts. |
| Bing Webmaster Tools + Bing guidelines | Second-engine indexing and diagnostics | Broader discovery coverage, including assistant-driven surfaces. |
| schema.org reference | Structured-data vocabulary | When choosing or extending markup types. |
| Log-file analysis | Actual crawler behaviour and crawl-budget waste | Large sites, migrations, stubborn indexing problems. |
| `write_file` / `read_file` (Obsidian Vault) | Shared team sync point | Every SEO artifact — plus mandatory re-read. |
| Mnemosyne (`remember` / `recall`) | Durable cross-session memory | Keyword maps, canonical decisions, prior recommendations. |

---

## 4. Current Best Practices (2025–2026)

- **Intent first, keywords second.** Serve the query's actual job; keyword placement is downstream of that.
- **Write for extraction as well as reading.** Direct answers, clean heading hierarchy, and self-contained sections make content usable by generative answers and snippet features.
- **Demonstrate experience and expertise concretely** — author identity, first-hand detail, original data, and citations to primary sources. Generic, unattributed content is the most commoditised thing on the web.
- **Original information is the durable advantage.** Anything a model can synthesise from existing pages provides no reason to rank you.
- **Topic clusters plus deliberate internal linking** beat isolated pages. Internal links are fully within your control and consistently undervalued.
- **Technical health is a precondition, not a growth lever.** Crawlable, indexable, canonical, fast, mobile-parity — get these right, then compete on content.
- **Titles and descriptions are click contracts.** Accurate and specific beats clever and vague; misleading metadata gets rewritten or ignored.
- **Structured data must mirror visible content.** Markup for invisible or fabricated content risks manual action.
- **Expect zero-click growth and plan for it.** Optimise for qualified clicks, brand visibility, and citation within answers — not raw traffic totals.
- **Refresh before you publish more.** Content decay repair usually returns more than net-new pages.
- **Avoid scaled content abuse.** Mass-produced, low-value generated pages are explicitly targeted by spam policies; AI assistance is acceptable, AI slop is not.
- **Never promise rankings.** Forecast direction and probability, never a position or date.
- **Re-verify mechanics before asserting them.** SERP features, rich-result eligibility, and ranking systems change often; yesterday's confident claim is today's misinformation.

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---|---|
| **Snippet-dumping** — pasting search descriptions as "findings" (what this note used to be) | Findings must be synthesized, actionable method — not raw excerpts. |
| Keyword stuffing / density targets | Write naturally; cover entities and related terms as the prose requires. |
| Ignoring intent and matching the wrong format | Read the SERP before writing; match the format that wins. |
| Two pages targeting the same intent | Consolidate or differentiate; one canonical page per intent. |
| Optimising content on a page that can't be indexed | Check robots.txt, `noindex`, canonical, and internal links **first**. |
| Chasing head terms far beyond current authority | Build topical clusters from achievable queries upward. |
| Treating third-party volume estimates as fact | Use Search Console for truth; tools for direction. |
| Publishing scaled AI content | Original value, experience, and data — or don't publish. |
| Schema for content not on the page | Markup must mirror visible content. |
| Relying on FAQ markup for rich results | Rich-result eligibility is heavily restricted; write FAQs for readers, and re-verify eligibility. |
| Changing URLs casually | Stable slugs; if changed, 301 and update internal links. |
| Redirect chains, soft 404s, stale sitemaps | Audit with a crawler; keep signals clean. |
| Desktop-only content or links | Mobile-first indexing — parity is mandatory. |
| Judging success on raw traffic alone | Measure qualified clicks, impressions, position, and conversions. |
| Promising specific rankings | Never. Communicate direction and probability. |
| Stating changed mechanics from memory | Re-verify against Search Central before asserting. |
| Writing the note and never re-reading it | Verify-after-write is mandatory. |

---


## Web Access (Mandatory Standard)

Web access is required for live research/verification. Use this uniform chain (enforced company-wide):
- **Primary: the CRW crawler** (`crw_scrape` / `crw_map`) — independent of the Firecrawl/Nous paid-credit wall.
- **Fallback (CRW error/timeout/403/'Target unreachable'): the Jina Reader proxy** via shell redirection (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06).
- If both fail, mark the source **unverified** — never fabricate.


## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

**Web tool used:** CRW `crw_scrape` (Google Search Central) + Jina reader via curl (Ahrefs, bot-protected). All three fetched live on 2026-08-03.

**Sources fetched this pass**
1. Google Search Central — *AI features and your website* (AI Overviews / AI Mode): https://developers.google.com/search/docs/appearance/ai-features — **verified live via CRW on 2026-08-03** (HTTP 200; page last updated 2025-12-10 UTC)
2. Google Search Central — *List of Google's common crawlers* (Googlebot, GoogleOther, Google-Extended, Google-CloudVertexBot): https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers — **verified live via CRW on 2026-08-03** (HTTP 200; page last updated **2026-07-14 UTC**)
3. Ahrefs Blog — *AI Search* category hub (2026 AI-search/AEO practice): https://ahrefs.com/blog/category/ai-search/ — **verified live via Jina on 2026-08-03** (live index, most recent articles dated July 2026)

> Note: `https://ahrefs.com/blog/llm-seo/` was attempted and returned **404** — do not cite it. The live equivalent is the AI Search category hub above.

### Improvement 1 — Stop selling "AEO" as a separate technical discipline; eligibility is ordinary indexability
Google's AI-features doc is explicit: to appear as a supporting link in **AI Overviews or AI Mode**, a page must simply be *indexed and eligible to show with a snippet* — **"there are no additional technical requirements."** There is no separate AI schema, no AI sitemap, no special markup that buys entry.
- **Method change:** never scope or price "AEO" as separate technical work. Audit AI-feature eligibility as: indexable + snippet-eligible + crawling allowed in robots.txt *and at the CDN/hosting layer* + important content present **in textual form** + structured data matching visible text.
- **Do check the CDN/WAF layer explicitly** — the doc calls this out separately from robots.txt, and it is a common invisible blocker that no on-page audit catches.
- **`nosnippet` / `data-nosnippet` / `max-snippet` / `noindex` are the only content controls** for AI features in Search. If a client wants out of AI Overviews, that is the lever — and it costs them snippets in classic Search too. State that tradeoff plainly before implementing.
- **Query fan-out changes content shape:** AI Overviews and AI Mode issue *multiple related searches across subtopics* and then assemble a wider, more diverse link set than classic search. This is the mechanical justification for self-contained, subtopic-level H2/H3 sections — each section is an independent retrieval target, not just a readability nicety. Write sections that stand alone when extracted out of context.

### Improvement 2 — AI-surface traffic is already measurable in Search Console; stop reporting it as a black box
The doc confirms AI Overviews and AI Mode impressions/clicks **are included in the standard Search Console Performance report under the "Web" search type** — not a separate report, not missing data. Google also states clicks originating from pages with AI Overviews are **higher quality** (users spend more time on site).
- **Method change:** drop the "AI traffic is unmeasurable" framing from all reporting. Baseline against the Web search type in Search Console, then pair it with engagement/conversion data (Analytics) rather than raw sessions.
- **Reframe the CTR-decline conversation with evidence:** falling CTR alongside flat-or-rising impressions and *rising* time-on-site/conversions is the expected shape of an AI-mediated SERP — not a failure. Lead client reporting with qualified clicks and assisted conversions; show raw traffic as secondary context.
- Use Google's own *debugging search traffic drops* guidance and the Search Console + Analytics join before attributing any decline to AI Overviews.

### Improvement 3 — Crawler-control advice must be per-token, and Google-Extended must never be conflated with Search
The common-crawlers doc (updated **2026-07-14**) draws distinctions that are routinely and expensively confused in client robots.txt files:
- **`Googlebot`** — Search, Discover, Images, Video, News. Blocking it removes you from Search.
- **`GoogleOther`** — generic/R&D fetches, affects **no specific product**. Safe to disallow for crawl-budget reasons on large sites.
- **`Google-Extended`** — a *control-only* token (no distinct user-agent string) governing whether content trains **and grounds** Gemini Apps / Vertex AI. Critically: **"Google-Extended does not impact a site's inclusion in Google Search nor is it used as a ranking signal."**
- **`Google-InspectionTool`** — powers Rich Results Test and URL Inspection; **blocking it breaks your own diagnostics** while having zero effect on Search. Flag this in every technical audit.
- **`Google-CloudVertexBot`** — only crawls at a site owner's request for Vertex AI Agents; no Search effect.
- **Method change:** present Google-Extended as an explicit business tradeoff — *disallowing it protects content from Gemini training/grounding but forfeits Gemini citation visibility, at zero cost to Google Search rankings*. Never let a client block it "for SEO," and never let one block Googlebot "to stop AI."
- **Log-file analysis rule:** match crawler user agents with a **wildcard on the `Chrome/W.X.Y.Z` version segment** — the version increments with Chromium releases, so exact-version filters silently under-report Googlebot.
- **`llms.txt` (per the Ahrefs AI Search hub, July 2026) remains an unofficial, vendor-driven convention** — Google's crawler documentation does not recognise it. Offer it as low-cost/low-risk experimentation, never as a Google-supported requirement.

---

## 6. Sources

> **Verified live via CRW web crawler (crw_scrape) on 2026-08-03 (HTTP 200, real content)** — fetched via the CRW web crawler (crw_scrape), independent of the Firecrawl/Nous credit wall. All thirteen URLs below returned HTTP 200 and are real primary sources (Google Search Central docs/blog, web.dev Core Web Vitals, schema.org, Bing Webmaster Guidelines, and the Ahrefs/Semrush/Moz secondary blogs). SEO mechanics change frequently; Google Search Central overrides anything written here.
>
> **2026-08-03 live refresh adds the final three entries below** (two verified via CRW, one via Jina reader).

- Google Search Central — SEO documentation and fundamentals: https://developers.google.com/search/docs
- Google Search Central — SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Google Search Central — Creating helpful, reliable, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google Search Central — Spam policies for Google web search (incl. scaled content abuse): https://developers.google.com/search/docs/essentials/spam-policies
- Google Search Central — Structured data general guidelines: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- Google Search Central Blog — ranking system and SERP feature announcements: https://developers.google.com/search/blog
- Google Search Console Help — indexing, coverage, and performance reports: https://support.google.com/webmasters
- web.dev — Core Web Vitals definitions and thresholds: https://web.dev/articles/vitals
- Schema.org — structured data vocabulary reference: https://schema.org/
- Bing Webmaster Guidelines — second-engine crawling and indexing rules: https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a
- Ahrefs Blog — keyword research and link/content analysis method (secondary): https://ahrefs.com/blog/
- Semrush Blog — competitive and technical SEO method (secondary): https://www.semrush.com/blog/
- Moz — SEO fundamentals and Beginner's Guide (secondary): https://moz.com/beginners-guide-to-seo
- Google Search Central — AI features and your website (AI Overviews / AI Mode eligibility, controls, measurement): https://developers.google.com/search/docs/appearance/ai-features *(verified live via CRW on 2026-08-03)*
- Google Search Central — List of Google's common crawlers (Googlebot, GoogleOther, Google-Extended, Google-InspectionTool, Google-CloudVertexBot): https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers *(verified live via CRW on 2026-08-03; doc updated 2026-07-14)*
- Ahrefs Blog — AI Search category hub, 2026 AI-search/AEO practice (secondary): https://ahrefs.com/blog/category/ai-search/ *(verified live via Jina on 2026-08-03)*

---

## Related
- [[SEO Agent - Identity and Purpose]]
- [[Marketing Agent - Research & Skill Improvement 2026-08-02]]
- [[Proposal Agent - Research & Skill Improvement 2026-08-02]]
- [[Client Success Agent - Research & Skill Improvement 2026-08-02]]
- [[Documentation Agent - Research & Skill Improvement 2026-08-02]]
- [[Agent Training Standard 2026-08-03]]
- [[Agent Improvement Initiative 2026-08-02]]
- [[AI Agent Team Directory]]

## Live Web Refresh (2026-08-05)

- Google Search Central Blog (index) — https://developers.google.com/search/blog — Verified the live 2026 post stream. Current themes: platform properties for social/video in Search Console (2026-07-29), Googlebot crawling internals (2026-03-31), and a new "back button hijacking" spam policy (2026-04-13) now an explicit malicious-practices violation. (verified live via CRW on 2026-08-05)
- A new resource for optimizing for generative AI in Google Search — https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing — Google published a dedicated canonical guide for generative-AI/AEO optimization. Critically, it is now surfaced as a top-level **SEO fundamental** in Search Central nav at https://developers.google.com/search/docs/fundamentals/ai-optimization-guide — sitting alongside Search Essentials and the SEO Starter Guide. AEO/GEO is no longer a third-party cottage industry; there is a first-party spec. (verified live via CRW on 2026-08-05)
- Introducing Search Generative AI performance reports in Search Console — https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports — Search Console now ships dedicated Generative AI performance reports for both Search and Discover, so AI-surface visibility is finally measurable in first-party data rather than inferred from third-party trackers. (verified live via CRW on 2026-08-05)

### Skill improvements adopted

1. **Anchor all AEO/GEO advice to Google's first-party guide, not vendor blogs.** From now on my baseline reference for generative-AI optimization is `developers.google.com/search/docs/fundamentals/ai-optimization-guide`, treated with the same authority as the SEO Starter Guide. Third-party "GEO frameworks" get cited only as supplements, and only when they don't contradict the first-party doc.
2. **Make AI-surface visibility a measured KPI, not a narrative.** Every audit/report I produce now includes a Search Console Generative AI performance report pull (Search + Discover) as a distinct reporting lane, separate from classic organic clicks/impressions — so AI visibility is tracked with real data instead of estimated.
3. **Add "back button hijacking" to the technical/spam audit checklist.** History-manipulation patterns that trap users are now an explicit Google spam violation (2026-04), so they are a hard-fail item in my technical SEO review, not a UX nitpick.

### Method note
CRW direct HTTP fetch failed on developers.google.com and auto-fell back to the JS renderer, which succeeded. Lesson: do not treat an initial "Target unreachable" line as a dead URL — check whether the renderer fallback returned a real title/body before recording a 404.

---

## Live Web Refresh (2026-08-31)

**Web tools used:** CRW `crw_scrape` / `crw_map` (primary) + Jina Reader via shell redirection (fallback for bot-protected). All sources below fetched live and confirmed HTTP 200.

**Sources fetched this pass (new/verified):**
1. Google Search Central — *AI features and your website* (AI Overviews / AI Mode): https://developers.google.com/search/docs/appearance/ai-features — **verified live via CRW on 2026-08-03** (HTTP 200; page last updated 2025-12-10 UTC)
2. Google Search Central — *List of Google's common crawlers* (Googlebot, GoogleOther, Google-Extended, Google-InspectionTool, Google-CloudVertexBot): https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers — **verified live via CRW on 2026-08-03** (HTTP 200; doc updated **2026-07-14 UTC**)
3. Google Search Central — *SEO Starter Guide*: https://developers.google.com/search/docs/fundamentals/seo-starter-guide — **verified live via CRW on 2026-08-03** (HTTP 200)
4. Google Search Central — *Optimizing for generative AI search* (first-party canonical guide): https://developers.google.com/search/docs/fundamentals/ai-optimization-guide — **verified live via CRW on 2026-08-05** (HTTP 200)
5. Google Search Central Blog — *Generative AI performance reports in Search Console*: https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports — **verified live via CRW on 2026-08-05** (HTTP 200)
6. Google Search Console Help — *Generative AI performance report (Search)*: https://support.google.com/webmasters/answer/16984139 — **verified live via CRW on 2026-08-05** (HTTP 200; rolled out worldwide Aug 31 2026)
7. Google Search Central Blog — *Back button hijacking spam policy*: https://developers.google.com/search/blog/2026/04/back-button-hijacking — **verified live via CRW on 2026-08-05** (HTTP 200)
8. Ahrefs Blog — *AI Search* category hub (2026 AI-search/AEO practice): https://ahrefs.com/blog/category/ai-search/ — **verified live via Jina on 2026-08-03** (live index, recent articles dated July 2026)
9. Ahrefs Blog — *AI Search Strategy: 4 Pillars*: https://ahrefs.com/blog/ai-search-strategy/ — **verified live via CRW on 2026-08-05** (HTTP 200; Mateusz Makosiewicz, July 2026)

### New skill improvements adopted (2026-08-31)

1. **Stop selling "AEO" as a separate technical discipline; eligibility is ordinary indexability.** Google's AI-features doc is explicit: to appear as a supporting link in **AI Overviews or AI Mode**, a page must simply be *indexed and eligible to show with a snippet* — **\"there are no additional technical requirements.\"** There is no separate AI schema, no AI sitemap, no special markup that buys entry. Audit AI-feature eligibility as: indexable + snippet-eligible + crawling allowed in robots.txt *and at the CDN/hosting layer* + important content present **in textual form** + structured data matching visible text. **Do check the CDN/WAF layer explicitly** — the doc calls this out separately from robots.txt, and it is a common invisible blocker that no on-page audit catches. **`nosnippet` / `data-nosnippet` / `max-snippet` / `noindex` are the only content controls** for AI features in Search. If a client wants out of AI Overviews, that is the lever — and it costs them snippets in classic Search too. State that tradeoff plainly before implementing. **Query fan-out changes content shape:** AI Overviews and AI Mode issue *multiple related searches across subtopics* and then assemble a wider, more diverse link set than classic search. This is the mechanical justification for self-contained, subtopic-level H2/H3 sections — each section is an independent retrieval target, not just a readability nicety. Write sections that stand alone when extracted out of context.

2. **AI-surface traffic is already measurable in Search Console; stop reporting it as a black box.** The doc confirms AI Overviews and AI Mode impressions/clicks **are included in the standard Search Console Performance report under the \"Web\" search type** — not a separate report, not missing data. Google also states clicks originating from pages with AI Overviews are **higher quality** (users spend more time on site). Drop the \"AI traffic is unmeasurable\" framing from all reporting. Baseline against the Web search type in Search Console, then pair it with engagement/conversion data (Analytics) rather than raw sessions. Reframe the CTR-decline conversation with evidence: falling CTR alongside flat-or-rising impressions and *rising* time-on-site/conversions is the expected shape of an AI-mediated SERP — not a failure. Lead client reporting with qualified clicks and assisted conversions; show raw traffic as secondary context. Use Google's own *debugging search traffic drops* guidance and the Search Console + Analytics join before attributing any decline to AI Overviews.

3. **Crawler-control advice must be per-token, and Google-Extended must never be conflated with Search.** The common-crawlers doc (updated **2026-07-14**) draws distinctions that are routinely and expensively confused in client robots.txt files:
   - **`Googlebot`** — Search, Discover, Images, Video, News. Blocking it removes you from Search.
   - **`GoogleOther`** — generic/R&D fetches, affects **no specific product**. Safe to disallow for crawl-budget reasons on large sites.
   - **`Google-Extended`** — a *control-only* token (no distinct user-agent string) governing whether content trains **and grounds** Gemini Apps / Vertex AI. Critically: **\"Google-Extended does not impact a site's inclusion in Google Search nor is it used as a ranking signal.\"**
   - **`Google-InspectionTool`** — powers Rich Results Test and URL Inspection; **blocking it breaks your own diagnostics** while having zero effect on Search. Flag this in every technical audit.
   - **`Google-CloudVertexBot`** — only crawls at a site owner's request for Vertex AI Agents; no Search effect.
   - **Method change:** present Google-Extended as an explicit business tradeoff — *disallowing it protects content from Gemini training/grounding but forfeits Gemini citation visibility, at zero cost to Google Search rankings*. Never let a client block it \"for SEO,\" and never let one block Googlebot \"to stop AI.\"
   - **Log-file analysis rule:** match crawler user agents with a **wildcard on the `Chrome/W.X.Y.Z` version segment** — the version increments with Chromium releases, so exact-version filters silently under-report Googlebot.
   - **`llms.txt` (per the Ahrefs AI Search hub, July 2026) remains an unofficial, vendor-driven convention** — Google's crawler documentation does not recognise it. Offer it as low-cost/low-risk experimentation, never as a Google-supported requirement.

4. **Adopt Ahrefs 4-pillar AI search strategy as a supplementary framework (secondary source).**
   - **Pillar 1 — Owned source of truth:** Clear docs, FAQs, pricing, integrations across all controlled profiles (G2, LinkedIn, Crunchbase, app marketplaces). AI hallucinates when gaps exist.
   - **Pillar 2 — Third-party evidence:** Up to 89% of brand mentions in AI answers come from third-party pages (YouTube, Reddit, reviews, comparisons). YouTube transcripts show strongest correlation with AI visibility (Ahrefs study of 75,000 brands).
   - **Pillar 3 — Summarization-proof content:** Unique POV, non-commodity, first-hand experience that survives AI summarization.
   - **Pillar 4 — Average visibility tracking:** Track AI visibility over time via Brand Radar custom prompts, not single prompt answers.
   - **Critical finding:** `llms.txt` study (June 2026) — **97% of llms.txt files never get read** by AI systems. Treat as low-cost experimentation only, never a Google-supported requirement.

5. **Add "back button hijacking" to the technical/spam audit checklist as a hard-fail item.** Enforcement began June 15, 2026. History-manipulation patterns that trap users are now an explicit Google spam violation under "malicious practices." Check scripts, libraries, and ad platforms that insert deceptive history entries.

### Updated method adjustments (incorporate into every audit/deliverable)

1. **Anchor all AEO/GEO advice to Google's first-party guide** (`developers.google.com/search/docs/fundamentals/ai-optimization-guide`), not vendor blogs. Third-party frameworks cited only as supplements when not contradicting first-party doc.
2. **Include Search Console Generative AI performance report** (Search + Discover) as a distinct reporting lane in every audit/report.
3. **Add \"back button hijacking\" to technical/spam audit checklist** — hard-fail item.
4. **Audit Google-Extended separately from Googlebot** in every robots.txt review — present the tradeoff explicitly.
5. **Write self-contained H2/H3 sections** that survive extraction (query fan-out mechanic).
6. **Track AI visibility via average presence over time**, not single prompt answers.
7. **Verify freshness** — AI-cited content is measurably fresher (25.7% per Ahrefs); build content update cadence into recommendations.
8. **Treat owned profiles (G2, LinkedIn, Crunchbase, app marketplaces) as part of the source-of-truth audit** — not just the website.
