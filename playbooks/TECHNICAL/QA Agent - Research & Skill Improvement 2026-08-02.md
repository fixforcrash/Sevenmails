---
type: Agent Training
status: active
tags: [02-organization]
---

# QA Agent — Method Playbook

> **Refreshed 2026-08-31** by the QA Agent (self-training). Live web research via CRW crawler — 11 sources verified 2026-08-31.
> Companion note: [[QA Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]] · Identity: `C:\Users\black\AppData\Local\hermes\profiles\qa-agent\SOUL.md`

---

## 1. Domain Summary

I **decide whether software is fit to ship** — designing and executing tests, measuring coverage and risk, and acting as the quality gate between implementation and release. My output is a verdict backed by evidence, not a feeling.

The 2026 shift that matters: **QA is continuous, risk-based, and AI-augmented — and it starts before the code does.** With 53% of code now AI-generated or AI-assisted (Sembi 2026 Software Quality Pulse), 61% of teams report *more* testing demand from that code while only 17% see significant gains from AI-driven testing. So the discipline is: shift testing left, automate at the right layer, prioritize by risk, and evaluate AI output with the same rigor you'd apply to any untrusted contributor.

**Never:** pass code on "it builds," equate coverage percentage with risk coverage, trust an AI-generated test that was never executed, or sign off without a reproducible failing-then-passing signal.

---

## 2. Core Workflow

### Phase A — Plan & Risk (before code exists)
1. **Translate the spec into testable acceptance criteria.** If a requirement can't be tested, it isn't done. Reuse the EARS-form criteria the Coding Agent derived.
2. **Rank by risk, not by convenience.** Risk-based prioritization runs the workflows with the highest failure risk first — driven by code-change frequency and historical defect density — instead of alphabetically or by coverage %.
3. **Choose the test mix:** unit (logic), integration (boundaries), end-to-end (critical user journeys), plus security and performance where the spec demands. Decide what is automated vs. exploratory.

### Phase B — Shift Left (test during development)
4. **Test as the code is written, not after.** Shift-left moves test design and execution earlier in the lifecycle — ideally from the design phase — so defects are caught when they're cheapest to fix (up to ~40% of post-release bugs are preventable this way).
5. **Enable developers to test their own code** in CI with fast feedback loops. QA's role becomes defining the strategy and the quality gate, not being the sole executer.
6. **Build the harness early.** Wire tests into the CI/CD pipeline before features land so every commit is checkable.

### Phase C — Automate (at the right layer)
7. **Follow the test automation pyramid.** A broad base of fast, cheap unit tests; a smaller layer of integration tests; a thin top of slow, expensive end-to-end tests. Inverting the pyramid (mostly E2E) produces a slow, flaky, expensive suite.
8. **Prefer self-healing and stable frameworks** for UI automation (Playwright over legacy Selenium where possible) to absorb AI-generated UI churn without constant maintenance.
9. **Automate the boring, explore the risky.** Routine regression → automation. Novel, ambiguous, adversarial behavior → human/agent exploration.

### Phase D — Execute & Evaluate
10. **Run the suite; capture real results.** A test you didn't execute is a test that doesn't exist. Report pass/fail with the actual output.
11. **Evaluate AI-generated code explicitly.** AI introduces prompt-injection exposure, insecure patterns absorbed from training data, and auth shortcuts traditional SAST misses — add AI-specific vulnerability coverage.
12. **Use agentic testing where it earns its keep.** Autonomous agents can read requirements, generate cases, and execute — but only trust their output after it has run and been reviewed (the 17%-gain gap is exactly the trust gap).

### Phase E — Report & Gate
13. **Issue an evidence-backed verdict.** "Ship / hold / ship-with-known-issues," each backed by what passed, what failed, and what's untested.
14. **Fail the gate on regressions.** A quality gate is meaningless if it always passes. Block merge on new failures and on coverage drops in risk areas.
15. **Hand off.** Defects → Debugging Agent; user-facing behavior changes → Documentation Agent; the green build → release.

### Phase F — Persist
16. **Write the QA verdict + test strategy to the Obsidian Vault, then re-read the file** (verify-after-write). Persist durable quality lessons to Mnemosyne (`mnemosyne_remember`).
17. **Feed failures back into the pyramid.** Every escaped defect becomes a new automated test so the suite grows toward the risks that actually bite.

---

## 3. Recommended Tools

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

| Tool | What it's for | When to use |
|---|---|---|
| Unit test frameworks (pytest, JUnit, vitest, jest) | Fast base of the pyramid | Every module; run on every commit. |
| Integration / API test tools (Postman, REST-assured, Supertest) | Boundary and contract testing | Service and API layers. |
| E2E / UI automation (Playwright, Selenium, Cypress) | Critical user-journey coverage | Thin top of the pyramid; prefer Playwright for self-healing UI. |
| CI/CD pipeline (GitHub Actions, GitLab CI, Jenkins) | Continuous testing + quality gate | Every commit/PR; block on regression. |
| Test management (Testomat.io, Xray, qTest) | Case design, traceability, reporting | Teams needing spec-to-case traceability. |
| SAST / DAST / secret scanning (Semgrep, OWASP ZAP, gitleaks) | Security in the pipeline | Every build; add AI-specific vuln coverage. |
| Risk-based prioritization engine | Order tests by failure risk | Large suites where running everything is too slow. |
| Agentic testing platforms (Playwright + Claude Code agents, Maxim AI) | Generate/execute tests from requirements | When spec-to-case drift is the bottleneck. |
| Coverage tools (JaCoCo, coverage.py, Istanbul) | Measure what's exercised | As a *risk* signal, never as the sole gate. |

---

## 4. Current Best Practices (2025–2026)

- **Risk-based, not coverage-based.** Coverage % is a vanity metric if it misses the workflows that actually break. Prioritize by change frequency and historical defect density.
- **Shift left decisively.** Anticipate tests from the design phase; catch defects when they're ~40%-cheaper-to-fix.
- **Respect the pyramid.** Fast unit base, minimal E2E top. Inverted pyramids are slow, flaky, and expensive.
- **Continuous testing in CI/CD is the norm.** Testing is a pipeline stage, not a phase after coding.
- **Treat AI-generated code as an untrusted contributor.** 53% of code is AI-assisted, but only 17% of teams see real testing gains — add AI-specific security and behavior evaluation.
- **Automate regression, explore the novel.** Save human judgment for ambiguous and adversarial cases.
- **Quality gates must be able to fail.** A gate that always passes is theater.
- **Agentic testing is a force multiplier, not a replacement.** Trust only what has run and been reviewed.
- **Self-healing UI automation** absorbs AI-driven UI churn and cuts maintenance toil.
- **Persist escaped defects as new tests** so quality compounds.

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---|---|
| "It builds, so it's good" | Require executed tests + a verdict, not a green compile. |
| Coverage % mistaken for risk coverage | Prioritize by failure risk; track workflow coverage. |
| Inverted pyramid (mostly E2E) | Push tests down to fast unit/integration layers. |
| Trusting an AI-generated test that never ran | Execute it; review the result before counting it. |
| Quality gate that always passes | Block merges on regression and risk-area coverage drops. |
| Testing only after code is "done" | Shift left — design tests from the spec/design phase. |
| Missing AI-specific vulns | Add prompt-injection / insecure-pattern coverage to SAST. |
| Manual-only regression | Automate the boring; reserve humans for novel/ambiguous. |
| Sign-off without a failing→passing signal | Demand reproducible evidence of the fix. |
| Writing the verdict and never re-reading it | Verify-after-write is mandatory. |

---

## 6. Sources

- Testomat.io — Software Testing Trends 2026: The Ultimate QA Guide: https://testomat.io/blog/software-testing-trends/
- Ranorex — 8 Software Testing Trends Shaping QA in 2026: https://www.ranorex.com/blog/software-testing-trends-2023/
- Inflectra — Software Testing Trends & Expectations for 2026: https://www.inflectra.com/Ideas/Whitepaper/Software-Testing-Trends.aspx
- ACCELQ — The Test Automation Pyramid: What is it & How to Use it in 2026: https://www.accelq.com/blog/test-automation-pyramid/
- Testomat.io — Testing Pyramid: Strategy, Layers & Best Practices 2026: https://testomat.io/blog/testing-pyramid-role-in-modern-software-testing-strategies/
- Datadog — Best practices for shift-left testing: https://www.datadoghq.com/blog/shift-left-testing-best-practices/
- Google Testing Blog — Choosing Values for Robust Tests (2026-06-04): https://testing.googleblog.com/2026/06/choosing-values-for-robust-tests.html
- Playwright — Test Agents (planner / generator / healer): https://playwright.dev/docs/test-agents
- Playwright — Release notes (v1.62): https://playwright.dev/docs/release-notes

---


## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

Live browse performed with the **CRW MCP crawler** (`crw_scrape`). All three fetched with HTTP 200 — **verified live via CRW on 2026-08-03**.

| # | Source | URL | Status |
|---|---|---|---|
| 1 | Google Testing Blog — *Choosing Values for Robust Tests* (TotT, 2026-06-04) | https://testing.googleblog.com/2026/06/choosing-values-for-robust-tests.html | verified live via CRW on 2026-08-03 |
| 2 | Playwright Docs — *Test Agents* (planner / generator / healer) | https://playwright.dev/docs/test-agents | verified live via CRW on 2026-08-03 |
| 3 | Playwright Docs — *Release notes* (v1.62 current) | https://playwright.dev/docs/release-notes | verified live via CRW on 2026-08-03 |

### Improvement 1 — Never assert with default-valued test data (the "zero trap")

Google's June 2026 TotT shows a test that **passes against a broken implementation** purely because the chosen value collided with the default:

```cpp
void MyMap::insert(int key, int value) {
  internal_map_[key];   // BUG: value is never stored
}

TEST(MyMapTest, Insert) {
  MyMap my_map;
  my_map.insert(1, 0);
  EXPECT_EQ(my_map.get(1), 0);  // passes anyway — 0 is the default-init value
}
```

**New rule for Phase A/D:** pick *distinctive, non-default* values — never `0`, `""`, `null`, `false`, or an empty collection — for any value the code under test is supposed to write. If swapping the implementation for a no-op would still make the test pass, the test proves nothing. Add "would a no-op pass this?" to the test-review checklist, and apply it hardest to AI-generated tests, which default to placeholder values.

### Improvement 2 — Run agentic testing as a reviewable planner → generator → healer pipeline

Playwright now ships three first-class agents (`npx playwright init-agents --loop=vscode|claude|codex|opencode`):

- **planner** explores the app and emits a **Markdown test plan** (`specs/*.md`)
- **generator** turns that plan into Playwright test files
- **healer** runs the suite and repairs failing tests

The key insight: the Markdown plan is a **human-reviewable artifact between exploration and code**. This resolves the playbook's "trust only what has run and been reviewed" tension — review the *plan* (cheap, readable) rather than only auditing generated code. Also required: a **`seed.spec.ts`** that performs global setup/fixtures; the planner executes it and uses it as the style template for every generated test. Caveat to hold: the **healer must not be allowed to auto-weaken assertions** to make a suite green — treat healer diffs as PRs needing review, since a "healed" test can silently become a no-op (see Improvement 1).

### Improvement 3 — Instrument for flake forensics instead of just retrying

Playwright v1.62 upgrades flake handling from "retry and hope" to evidence collection. Adopt in CI configs:

- `trace: 'retain-on-failure-and-retries'` — keeps a trace for **every** attempt, so a passing run can be diffed against a failing one from the same flaky test. `video` now supports the same modes (`'on-all-retries'`, `'retain-on-first-failure'`, `'retain-on-failure-and-retries'`).
- `failOnFlakyTests` — surfaced to reporters, so a flaky pass can **fail the gate** (directly serves the "a gate that always passes is theatre" rule).
- Per-step `timeout` on `test.step(...)` and `test.step.skip()` — localises a hang to the step instead of blowing the whole test timeout.
- `expect.soft.poll(...)` — collect multiple soft assertion failures in one run rather than stopping at the first.
- `--update-snapshots=changed --update-source-method=3way` — update only genuinely changed snapshots, avoiding blanket re-baselining that erases real regressions.
- UI Mode can now filter to **only tests affected by source changes** — a practical implementation of the playbook's risk-based prioritization.

---

## Related
- [[QA Agent - Identity and Purpose]]
- [[Coding Agent - Research & Skill Improvement 2026-08-02]]
- [[Debugging Agent - Research & Skill Improvement 2026-08-02]]
- [[Agent Training Standard 2026-08-03]]
- [[AI Agent Team Directory]]


## Live Web Refresh (2026-08-05)

- **LLM Evals: Everything You Need to Know (Evals FAQ)** — https://hamel.dev/blog/posts/evals-faq/ — Hamel Husain + Shreya Shankar's curated FAQ from teaching 700+ engineers/PMs. Core stack: error analysis on *traces* is the highest-ROI activity; a purpose-built data viewer is the single most important eval investment; LLM-as-judge must be built via "critique shadowing" aligned to ONE principal domain expert making binary pass/fail judgments with written critiques, not vague 1-5 Likert scores. Eval maturity ladder = L1 unit tests/assertions → L2 human & model eval → L3 A/B testing. (verified live via CRW on 2026-08-05)
- **Building effective agents** — https://www.anthropic.com/engineering/building-effective-agents — Anthropic Engineering. Distinguishes *workflows* (LLMs orchestrated through predefined code paths) from *agents* (LLM dynamically directs its own process/tool use). QA implication: these are two different test surfaces — workflows are deterministically path-testable, agents are not and require outcome+process evals. Also warns frameworks obscure underlying prompts/responses, making debugging (and thus test observability) harder. (verified live via CRW on 2026-08-05)
- **How we built our multi-agent research system** — https://www.anthropic.com/engineering/multi-agent-research-system — Anthropic Engineering. The most concrete primary source on *agentic* evaluation. Key claims: traditional "input X → path Y → output Z" evals break for multi-agent systems because agents take different valid paths to the same goal; start evals immediately with ~20 queries representing real usage (effect sizes early on are huge, 30%→80%, so small N is enough); a SINGLE LLM-judge call emitting a 0.0-1.0 score plus a pass/fail grade beat multiple specialized judges on consistency and human alignment; human testing still catches what automation misses (they caught a source-quality bias toward SEO content farms over academic PDFs). Also: multi-agent systems have *emergent* behavior — small lead-agent prompt changes unpredictably shift subagent behavior, so test interaction patterns, not just individual agents. (verified live via CRW on 2026-08-05)

### Skill improvements adopted

1. **Stop path-asserting agent runs; assert on outcome + process-reasonableness instead.** For any multi-step/agentic feature I test, I will no longer write brittle assertions pinning an exact tool-call sequence. Instead each test case gets (a) an outcome assertion (did it reach a correct end state?) and (b) a bounded process assertion (did it stay within a sane effort budget — tool-call count, token spend, no duplicate/looping subtasks?). This directly follows the Anthropic finding that identical inputs legitimately produce different valid trajectories.
2. **Default to a single rubric-driven LLM judge returning one 0.0-1.0 score + a pass/fail, not a panel of judges.** Rubric dimensions I will standardize on: factual accuracy, citation accuracy, completeness, source quality, tool efficiency. Multiple specialized judges are a later optimization, only after error analysis shows one judge is conflating failure modes.
3. **Start every new eval at ~20 real-usage cases, immediately — never block on building a "proper" 200-case suite.** Pair it with binary pass/fail + a written critique per failure (critique shadowing), because free-text critiques are what later become the judge prompt and the taxonomy for error analysis.
4. **Treat the trace viewer as a first-class deliverable.** Before writing more assertions on a flaky agent feature, build/verify the ability to read full traces; error analysis over traces outranks adding test cases.

---

## Live Web Refresh (2026-08-31)

Live browse performed with the **CRW MCP crawler** (`crw_scrape`). All 11 sources fetched with HTTP 200 — **verified live via CRW on 2026-08-31**.

| # | Source | URL | Status |
|---|---|---|---|
| 1 | Testomat.io — *Software Testing Trends 2026: The Future of Quality Assurance* | https://testomat.io/blog/software-testing-trends/ | verified live via CRW on 2026-08-31 |
| 2 | Ranorex — *Software Testing Trends 2026: 8 Data-Backed QA Shifts* | https://www.ranorex.com/blog/software-testing-trends-2023/ | verified live via CRW on 2026-08-31 |
| 3 | Inflectra — *Software Testing Trends & Expectations for 2026* | https://www.inflectra.com/Ideas/Whitepaper/Software-Testing-Trends.aspx | verified live via CRW on 2026-08-31 |
| 4 | Google Testing Blog — *Choosing Values for Robust Tests* (TotT, 2026-06-04) | https://testing.googleblog.com/2026/06/choosing-values-for-robust-tests.html | verified live via CRW on 2026-08-31 |
| 5 | Playwright Docs — *Test Agents* (planner / generator / healer) | https://playwright.dev/docs/test-agents | verified live via CRW on 2026-08-31 |
| 6 | Playwright Docs — *Release notes* (v1.62 current) | https://playwright.dev/docs/release-notes | verified live via CRW on 2026-08-31 |
| 7 | Hamel Husain + Shreya Shankar — *LLM Evals: Everything You Need to Know (Evals FAQ)* | https://hamel.dev/blog/posts/evals-faq/ | verified live via CRW on 2026-08-31 |
| 8 | Anthropic Engineering — *Building Effective AI Agents* | https://www.anthropic.com/engineering/building-effective-agents | verified live via CRW on 2026-08-31 |
| 9 | Anthropic Engineering — *How we built our multi-agent research system* | https://www.anthropic.com/engineering/multi-agent-research-system | verified live via CRW on 2026-08-31 |
| 10 | Playwright Docs — *Accessibility testing* with @axe-core/playwright | https://playwright.dev/docs/accessibility-testing | verified live via CRW on 2026-08-31 |
| 11 | Grafana Labs — *Grafana k6 documentation* (performance testing) | https://grafana.com/docs/k6/latest/ | verified live via CRW on 2026-08-31 |

### Key Data Points (2025–2026)

- **53% of all code is AI-generated or AI-assisted** (Sembi 2026 Software Quality Pulse)
- **61% of teams report moderate to dramatic increases in QA workload** from AI code
- **Only 17% of teams say AI-driven testing has delivered significant gains**
- **Self-healing automation reduces broken tests by 35-50% per release** when paired with object repository
- **Codeless testing market: $2.7B (2025) → $11.4B (2035), 15.6% CAGR** — hybrid (codeless + code) is the winning architecture
- **Shift-left practices prevent up to 40% of post-release bugs** — defect escape rate is the metric that matters, not coverage %
- **Desktop testing remains critical for enterprise** (Win32, WPF, WinForms, SAP, Java) — web-first frameworks don't cover it
- **Security testing market: $14.5B (2024) → $43.9B (2029), 24.7% CAGR** — AI/LLM threats now top-3 priority (32% of teams)
- **Playwright Test Agents** — planner (Markdown plan), generator (executable tests), healer (auto-repair) — review the *plan* before generated code
- **Playwright v1.62 flake forensics**: `trace: 'retain-on-failure-and-retries'`, `failOnFlakyTests`, per-step `timeout`, `expect.soft.poll()`, `--update-snapshots=changed --update-source-method=3way`, UI Mode filters to tests affected by source changes
- **Google's "zero trap"**: never use `0`, `""`, `null`, `false`, or empty collection as test values — if a no-op passes, test proves nothing
- **LLM Eval Maturity Ladder**: L1 unit tests/assertions → L2 human & model eval → L3 A/B testing
- **Error analysis on traces = highest-ROI activity** for LLM evals; purpose-built data viewer = single most important eval investment
- **Single rubric-driven LLM judge (0.0-1.0 + pass/fail + critique)** beats panel of judges on consistency & human alignment
- **Start evals at ~20 real-usage cases immediately** — effect sizes early are huge (30%→80%)
- **Multi-agent systems**: don't path-assert; assert on outcome + bounded process (tool-call budget, no duplicate/looping subtasks)
- **Workflows vs Agents** (Anthropic): workflows = predefined code paths; agents = LLM dynamically directs own process/tool use — different test surfaces
- **k6**: open-source, developer-friendly performance testing; browser API for browser metrics; CI/CD integration; chaos/resilience testing with xk6-disruptor
- **Accessibility**: `@axe-core/playwright` for automated WCAG 2.1/2.2 AA scanning; combine with manual assessment (Accessibility Insights for Web)
- **Synthetic test data**: AI-generated realistic data for privacy compliance, edge cases, referential integrity, dynamic per-run generation

### Improvement 4 — Never assert with default-valued test data (the "zero trap")

Google's June 2026 TotT shows a test that **passes against a broken implementation** purely because the chosen value collided with the default:

```cpp
void MyMap::insert(int key, int value) {
  internal_map_[key];   // BUG: value is never stored
}

TEST(MyMapTest, Insert) {
  MyMap my_map;
  my_map.insert(1, 0);
  EXPECT_EQ(my_map.get(1), 0);  // passes anyway — 0 is the default-init value
}
```

**New rule for Phase A/D:** pick *distinctive, non-default* values — never `0`, `""`, `null`, `false`, or an empty collection — for any value the code under test is supposed to write. If swapping the implementation for a no-op would still make the test pass, the test proves nothing. Add "would a no-op pass this?" to the test-review checklist, and apply it hardest to AI-generated tests, which default to placeholder values.

### Improvement 5 — Run agentic testing as a reviewable planner → generator → healer pipeline

Playwright now ships three first-class agents (`npx playwright init-agents --loop=vscode|claude|codex|opencode`):

- **planner** explores the app and emits a **Markdown test plan** (`specs/*.md`)
- **generator** turns that plan into Playwright test files
- **healer** runs the suite and repairs failing tests

The key insight: the Markdown plan is a **human-reviewable artifact between exploration and code**. This resolves the playbook's "trust only what has run and been reviewed" tension — review the *plan* (cheap, readable) rather than only auditing generated code. Also required: a **`seed.spec.ts`** that performs global setup/fixtures; the planner executes it and uses it as the style template for every generated test. Caveat to hold: the **healer must not be allowed to auto-weaken assertions** to make a suite green — treat healer diffs as PRs needing review, since a "healed" test can silently become a no-op (see Improvement 4).

### Improvement 6 — Instrument for flake forensics instead of just retrying

Playwright v1.62 upgrades flake handling from "retry and hope" to evidence collection. Adopt in CI configs:

- `trace: 'retain-on-failure-and-retries'` — keeps a trace for **every** attempt, so a passing run can be diffed against a failing one from the same flaky test. `video` now supports the same modes (`'on-all-retries'`, `'retain-on-first-failure'`, `'retain-on-failure-and-retries'`).
- `failOnFlakyTests` — surfaced to reporters, so a flaky pass can **fail the gate** (directly serves the "a gate that always passes is theatre" rule).
- Per-step `timeout` on `test.step(...)` and `test.step.skip()` — localises a hang to the step instead of blowing the whole test timeout.
- `expect.soft.poll(...)` — collect multiple soft assertion failures in one run rather than stopping at the first.
- `--update-snapshots=changed --update-source-method=3way` — update only genuinely changed snapshots, avoiding blanket re-baselining that erases real regressions.
- UI Mode can now filter to **only tests affected by source changes** — a practical implementation of the playbook's risk-based prioritization.

### Improvement 7 — LLM/Agent evals: error analysis on traces first, single judge, start small

From Hamel Husain + Shreya Shankar (700+ engineers taught) and Anthropic multi-agent research:

1. **Error analysis on traces is the highest-ROI activity** — build/verify the trace viewer before writing more assertions. A purpose-built data viewer is the single most important eval investment.
2. **Default to a single rubric-driven LLM judge** returning one 0.0-1.0 score + a pass/fail grade + a written critique (built via "critique shadowing" aligned to ONE principal domain expert making binary pass/fail judgments). Multiple specialized judges are a later optimization, only after error analysis shows one judge is conflating failure modes.
3. **Start every new eval at ~20 real-usage cases immediately** — effect sizes early on are huge (30%→80%), so small N is enough. Pair with binary pass/fail + written critique per failure (critique shadowing), because free-text critiques later become the judge prompt and the taxonomy for error analysis.
4. **Eval maturity ladder**: L1 unit tests/assertions → L2 human & model eval → L3 A/B testing. Don't skip levels.

### Improvement 8 — Multi-agent systems: assert on outcome + bounded process, not exact paths

From Anthropic's multi-agent research system:

- **Workflows** (predefined code paths) are deterministically path-testable.
- **Agents** (LLM dynamically directs own process/tool use) are NOT path-testable — identical inputs legitimately produce different valid trajectories.
- **Test assertion pattern**: each test case gets (a) an **outcome assertion** (did it reach a correct end state?) and (b) a **bounded process assertion** (did it stay within a sane effort budget — tool-call count, token spend, no duplicate/looping subtasks?).
- Frameworks obscure underlying prompts/responses, making debugging (and thus test observability) harder — invest in trace viewing.
- Human testing still catches what automation misses (e.g., source-quality bias toward SEO content farms over academic PDFs).
- Multi-agent systems have *emergent* behavior — small lead-agent prompt changes unpredictably shift subagent behavior, so test interaction patterns, not just individual agents.

### Improvement 9 — Security testing: AI-specific vulnerability coverage mandatory

From Ranorex and Inflectra 2026 data:

- AI and LLM threats already rank among the **top three security priorities** for 2026, cited by 32% of teams alongside data breaches and cloud misconfigurations.
- AI-generated code introduces: **prompt injection risks**, **insecure patterns absorbed from training data**, and **authentication shortcuts** that traditional SAST signatures were not designed to catch.
- In mature pipelines: SAST on every commit, DAST and SCA per-build or daily, **unified reporting** (security failures block same release gates as functional failures), **AI-specific vulnerability coverage**.

### Improvement 10 — Synthetic test data by default for privacy, edge cases, and scale

From Inflectra and Testomat.io 2026:

- Generative AI has reached the ability to generate **truly realistic synthetic data** — privacy compliance without manual masking, unlimited volume without storage constraints, domain-appropriate data for realistic testing, edge case coverage including rare scenarios, referential integrity maintenance across related data, dynamic generation for each test run.
- Tools: Tonic.ai, Gretel, Synthesized, Inflectra Rapise AI — integrate into test data management pipeline.
- Quality of synthetic data is vital — not "lazy data" that degrades test effectiveness.

### Improvement 11 — Performance testing with k6 integrated in CI/CD

From Grafana k6 documentation (verified live):

- k6 is open-source, developer-friendly, extensible performance testing tool optimized for minimal resource consumption.
- Test types: **load, stress, spike, soak, browser performance testing** (via k6 browser API for real-user metrics).
- **CI/CD integration**: automate performance testing as part of development/release cycle.
- **Synthetic monitoring**: schedule tests to run frequently with minimal load, continuously validating production performance/availability.
- **Chaos/resilience testing**: simulate traffic as part of chaos experiments, inject faults in Kubernetes with xk6-disruptor.
- **Infrastructure testing**: extensions for new protocols or direct system testing.

### Improvement 12 — Accessibility testing integrated with @axe-core/playwright

From Playwright docs (verified live):

- Automated accessibility tests via `@axe-core/playwright` package — detects color contrast, missing labels, duplicate IDs, WCAG violations.
- Scan entire page or specific parts; configure with WCAG tags (`wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa`).
- Handle known issues: `exclude()` elements, `disableRules()`, or use **snapshots of violation fingerprints** (not full violations array) for granular known-issue allowance.
- Export full scan results as test attachments for debugging.
- Use **test fixtures** for common axe configuration (shared rules, excluded elements, attached reports).
- **Disclaimer**: automated tests detect some common problems; many accessibility problems require manual testing — combine with Accessibility Insights for Web (free, open-source, walks through WCAG 2.1 AA coverage).

### Improvement 13 — Cross-platform testing from single object repository

From Ranorex 2026 data:

- **Desktop testing remains critical** for enterprise (manufacturing, financial services, healthcare IT, enterprise software) — Win32, WPF, WinForms, UWP, SAP, Java applications.
- Web-first frameworks (Playwright, Selenium) **structurally cannot reach** native desktop apps.
- Winning architecture: **single object repository** centralizing element definitions regardless of platform (web, desktop, mobile) — update definition once, every test inherits the change.
- Cross-platform coverage must run in **same CI/CD pipeline** with unified reporting.

### Skill improvements adopted (2026-08-31)

1. **Never assert with default-valued test data (zero trap).** Pick distinctive, non-default values for any value the code under test is supposed to write. Add "would a no-op pass this?" to test-review checklist — apply hardest to AI-generated tests.

2. **Run agentic testing as reviewable planner → generator → healer pipeline.** Review the Markdown *plan* (cheap, readable) before generated code. Healer diffs = PRs needing review; never allow auto-weakening of assertions.

3. **Instrument for flake forensics instead of just retrying.** Retain traces/videos on all retries; fail gate on flaky passes; per-step timeouts; soft assertions; update only genuinely changed snapshots; UI Mode filter to tests affected by source changes.

4. **LLM/Agent evals: error analysis on traces first.** Build trace viewer as first-class deliverable. Single rubric-driven LLM judge (0.0-1.0 + pass/fail + critique via critique shadowing). Start at ~20 real-usage cases immediately with binary pass/fail + written critique.

5. **Multi-agent systems: assert on outcome + bounded process-reasonableness.** Not exact tool-call sequences. Identical inputs legitimately produce different valid trajectories.

6. **Security testing: AI-specific vulnerability coverage mandatory.** Prompt injection, training-data insecure patterns, auth shortcuts — add to SAST/DAST/SCA pipeline with unified reporting.

7. **Synthetic test data by default.** Privacy-compliant, unlimited volume, domain-appropriate, edge cases, referential integrity, dynamic per-run generation.

8. **Performance testing with k6 in CI/CD.** Load/stress/spike/soak on every significant change; browser API for real-user metrics; synthetic monitoring in production.

9. **Accessibility testing integrated in every run.** `@axe-core/playwright` with WCAG tags; fixtures for known issues; attach full scan results for debugging.

10. **Cross-platform from single object repository.** Desktop (Win32/WPF/WinForms/UWP/SAP/Java) + web + mobile from one framework — Ranorex Studio or equivalent.
