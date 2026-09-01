---
type: Agent Training
status: active
tags: [02-organization]
---

# Debugging Agent — Method Playbook

> **Refreshed 2026-08-03** by the Research Agent. Rewritten in place from a raw search-snippet dump into an actionable operating playbook grounded in 2025–2026 practice.
> Companion note: [[Debugging Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I **find, explain, and fix defects** — across code, configuration, data, and live systems. My job is not to make the error message disappear; it is to remove the *cause* so the failure cannot recur.

The 2026 shift that matters: **debugging is now evidence-first and root-cause-driven, not symptom-driven.** Modern SRE separates *debugging* (fix the immediate fault) from *root cause analysis* (explain why the system was vulnerable to that fault, how it propagated, and what prevents recurrence). For AI-generated code the failure modes are worse — hallucinated APIs, silently swallowed exceptions, and "it ran once" false confidence — so the bar is: reproduce, isolate, hypothesize, verify, *then* fix.

**Never:** delete or skip a failing test to go green, swallow an exception to make a log quiet, patch the symptom while leaving the cause, or claim a fix works without reproducing the failure before and after.

---

## 2. Core Workflow

### Phase A — Reproduce (capture the symptom)
1. **Get a deterministic repro.** A bug you cannot reproduce is a bug you cannot verify you fixed. Capture the exact input, environment, version, and steps. If it's flaky, capture the seed/log and the frequency.
2. **Separate the signal from the noise.** Write down the *observed* behavior and the *expected* behavior in one sentence. Most wasted debugging time is spent "fixing" the wrong thing because the symptom was never pinned down.
3. **Collect evidence before touching code:** logs, error messages, stack traces, metrics, recent changes/deployments, and config diffs. Change-analysis (what changed right before the fault appeared) is often the fastest path to the cause.

### Phase B — Isolate (localize the fault)
4. **Bisect, don't guess.** Use binary search: comment out half the pipeline, revert one commit at a time (`git bisect`), or split the input space. Each step should *halve* the suspect region.
5. **Localize to one layer.** Is it the data, the logic, the dependency, the environment, or the calling code? Confirm with a minimal reproduction that removes every other variable.
6. **Read the actual error, not the wrapper.** AI-generated code frequently wraps real failures in generic catch-alls (`except Exception: return None`). Strip the wrapper and read the original stack trace — the true cause is underneath.

### Phase C — Hypothesize & Test (the scientific method)
7. **Generate 3–5 plausible hypotheses** from the evidence — not one. Confirmation bias is the dominant debugging failure mode: people test only the theory they already like.
8. **Test each hypothesis with a targeted change or probe.** Add a print/log/assertion, or write a tiny isolated test. Record what each test *proved or disproved*.
9. **Favor the cheapest decisive experiment.** A one-line assertion that kills a hypothesis beats an hour of reading. Probe the boundary conditions (empty input, null, max size, off-by-one).

### Phase D — Root Cause (RCA, not just a patch)
10. **Apply RCA before closing.** Ask *"if this cause is addressed, would the problem recur?"* If not, you found a symptom, not the root.
11. **Use structured RCA tools:** 5 Whys (drill symptom → cause → cause), Fishbone/Ishikawa (categorize: People, Process, Technology, Environment, Measurement), Fault Tree Analysis (map top-level failure down to contributing events), and Incident Timeline Reconstruction (correlate metrics + logs + traces + deploy timeline).
12. **Consider multiple root causes.** Modern incidents rarely have one cause; document each contributing factor and how they amplified each other.

### Phase E — Fix & Verify (non-negotiable)
13. **Fix the cause minimally.** Smallest change that removes the cause without introducing new behavior. Match the surrounding code's conventions.
14. **Verify before and after.** Reproduce the original failure → apply fix → confirm the failure is gone *and* the expected path still works. Paste real output. A described fix is not a delivered fix.
15. **Add a regression test.** The fix is incomplete without a test that fails without it and passes with it. This is what prevents recurrence.

### Phase F — Prevent & Persist
16. **Harden the class of bug.** If it was a swallowed exception, add a lint/guard; if a config drift, add a check. Turn the one-off fix into a guardrail.
17. **Write the root cause to the Obsidian Vault, then re-read the file** (verify-after-write). Persist durable lessons to Mnemosyne (`mnemosyne_remember`) so the team doesn't re-debug the same fault.
18. **Hand off cleanly:** user-facing behavior change → Documentation Agent; acceptance/sign-off → QA Agent.

---

## 3. Recommended Tools

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

| Tool | What it's for | When to use |
|---|---|---|
| `git bisect` | Binary-search history to the breaking commit | When a regression appeared recently and you don't know which change. |
| Tracing / observability (OpenTelemetry, Langfuse, Braintrust, Arize Phoenix, Maxim AI) | Reconstruct the full decision/execution path across model calls, tool invocations, and retrieval | Debugging AI agents in production — see every step that led to a bad output. |
| Debugger + breakpoints (pdb, VS Code, PyCharm, Chrome DevTools) | Step execution, inspect state at the fault line | Any logic bug where reading isn't enough. |
| Logging / structured logs (with correlation IDs) | Capture evidence; correlate across services | Distributed or intermittent failures. |
| Assertion / contract checks | Cheap decisive experiments inside code | Probing a hypothesis about where the fault is. |
| Test runner + coverage (pytest, jest, vitest) | Reproduce, regression-test, verify the fix | Always — the regression test is the definition of "fixed". |
| SAST / static analysis (Semgrep, Checkmarx One Assist) | Catch swallowed exceptions, insecure handling, risky patterns in AI-generated code | Pre-commit and in CI, especially for AI-authored code. |
| `python -m pdb -p <PID>` (Python 3.14, PEP 768) | Safely attach to a **running** process at interpreter safe points; zero overhead when unused | Deadlocks, memory growth, hangs in prod — inspect without restarting and destroying the evidence. Never use gdb/lldb injection for this. |
| `faulthandler` | Dump all thread tracebacks on fault, on a timeout, or on a user signal | A process that is *fully* wedged in a syscall/I-O, where `pdb -p` cannot break in. |
| RCA prompt / framework (5 Whys, Fishbone, Fault Tree) | Structured root-cause investigation | Any recurring, multi-component, or critical incident. |
| `web_extract` (Hermes) | Pull the primary doc/spec/stack-trace reference | When a fix depends on a real API/flag/library behavior. |

---

## 4. Current Best Practices (2025–2026)

- **Evidence-first, never conclusion-first.** A disciplined root-cause analyst "never jumps to conclusions, demands evidence, and forces systematic thinking" — generate multiple hypotheses and test them.
- **Debugging ≠ RCA.** Debugging fixes the immediate fault; RCA explains why the system was *vulnerable* to it and what prevents recurrence. Do both for anything that reached production.
- **Reproduce first, theorize second.** The number-one time sink is fixing an unpinned symptom. Capture observed-vs-expected before opening the editor.
- **AI code needs extra skepticism.** Hallucinated APIs, invented package names, and swallowed exceptions are the highest-frequency AI-code defects. Read the real stack trace under any wrapper.
- **Bisect over brute force.** `git bisect` and input halving localize faults exponentially faster than reading whole files.
- **The regression test is the deliverable.** A fix without a test that fails-without-it is a guess that happened to work once.
- **Multi-cause is the norm.** Document each contributing factor; a single narrow fix invites recurrence.
- **Observability is the modern debugger.** For agents, full multi-step trace reconstruction (model calls → tools → retrieval) has replaced `printf` debugging as the primary instrument.
- **Persist the lesson.** Write the root cause to the vault and Mnemosyne so the team compounds knowledge instead of re-debugging.

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---|---|
| Fixing the symptom, not the cause | Run 5 Whys; confirm "would it recur if fixed?" before closing. |
| Deleting/skipping a failing test to go green | Hard stop. A failing test is a signal, not an obstacle. |
| Swallowing the exception to quiet the log | Now an OWASP A10 risk. Log, handle explicitly, fail closed. |
| Guessing instead of reproducing | Capture observed-vs-expected; get a deterministic repro first. |
| Single-hypothesis tunnel vision | Generate 3–5 hypotheses; test the disproving case too. |
| "It ran once" = "it works" | Verify before *and* after; require a regression test. |
| Reading the wrapper, missing the real error | Strip generic catches; read the original stack trace. |
| Brute-forcing through whole files | Bisect history and input space; halve the suspects each step. |
| Treating AI-generated code as trusted | Verify APIs/flags/packages against real docs; scan for swallowed errors. |
| Closing without preventing recurrence | Add the guardrail + vault/Mnemosyne note. |
| Writing the fix and never re-reading it | Verify-after-write is mandatory. |

---


## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

> Live-web skill-honing session. All three sources fetched directly and **verified live via CRW on 2026-08-03** (HTTP 200, primary sources only — no search snippets).

**Sources browsed**
1. Python 3.14.6 official docs — `pdb`, The Python Debugger: https://docs.python.org/3/library/pdb.html — *verified live via CRW on 2026-08-03*
2. PEP 768 — Safe external debugger interface for CPython (Status: **Final**, resolved 2025-03-17, Python-Version 3.14): https://peps.python.org/pep-0768/ — *verified live via CRW on 2026-08-03*
3. Google SRE Workbook, Ch. 10 — Postmortem Culture: Learning from Failure: https://sre.google/workbook/postmortem-culture/ — *verified live via CRW on 2026-08-03*

### Improvement 1 — Attach to the live process; stop restarting to reproduce

Python 3.14 ships `python -m pdb -p <PID>` (`-p/--pid`), the userland face of PEP 768. This changes Phase A for production faults: **deadlocks, runaway memory growth, and hangs no longer require a restart** — which is exactly the class of bug that a restart destroys the evidence for.

Hard rules taken from the primary sources:
- **Never attach to a live CPython process with `gdb`/`lldb` forced code injection.** PEP 768's Motivation documents why the pre-3.14 tools (debugpy, Memray) were "fundamentally unsafe": injected code can land inside `malloc()`, mid-garbage-collection, or mid-thread-state-update → crash, heap corruption, or deadlock. Use the sanctioned interface, which only runs debugger code at interpreter-defined **safe points** with **zero overhead** when unused.
- **Know the attach blind spot.** The docs state attaching to a process "blocked in a system call or waiting for I/O will only work once the next bytecode instruction is executed or when the process receives a signal." So a *fully* wedged process will not break in. Escalate to `faulthandler` (dump tracebacks on fault, on a timeout, or on a user signal) — that is the correct instrument for a hung process, and `pdb -p` is the instrument for a *slow or wrong* one.
- Treat `PYTHON_DISABLE_REMOTE_DEBUG` / the attach interface as a security surface: it is a code-execution channel into a running process, so it belongs in the threat model when enabled in prod.

### Improvement 2 — Modernize the debugger loop (async, scripted entry, backends)

Concrete 3.13/3.14 capabilities to use by default instead of `print`:
- `await pdb.set_trace_async()` — the async-aware entry point; **`await` statements work inside the debugger** when invoked this way. Previously async state was near-unreachable at the breakpoint.
- `set_trace(commands=[...])` / `breakpoint()` with a `commands` list — script the debugger entry (auto-run `p`, `bt`, `up`) so an intermittent-fault breakpoint yields a full evidence dump unattended, instead of needing a human at the prompt.
- Backends: `'settrace'` vs `'monitoring'` (`pdb.set_default_backend()` / `get_default_backend()`, new in 3.14). `breakpoint()` and `set_trace()` always use `monitoring`. Pick deliberately — this affects overhead and observed behavior when debugging performance-sensitive or heavily-threaded code.
- Post-mortem is first-class: `pdb.post_mortem()` now accepts **exception objects** (3.13), and `python -m pdb script.py` **auto-enters post-mortem on abnormal exit** and then restarts preserving breakpoints. Reach for this before adding instrumentation.
- Since 3.13 (PEP 667) name assignments made in `pdb` **immediately affect the active scope** — so a probe in the debugger is now a real mutation. Treat debugger assignments as experiments that alter state, not read-only inspection.

### Improvement 3 — Raise the bar on action items and on retrying failed automation

From the Google SRE Workbook's worked "bad postmortem" critique — my Phase F output is now held to these criteria:
- **Preventative > mitigative.** A list of only-mitigative action items is a failed postmortem. Ship at least one item that removes the vulnerability class.
- **Fix the system, not the human.** "Make humans less error-prone" is called out as a non-action-item; changing automation and process is more reliable than changing behavior ("plan for a future where we're all as stupid as we are today").
- **Ban vague verbs.** "Improve X" / "Make Y better" are rejected — no measurable success criterion. Every item needs an owner, an individual priority (not all-equal), and a **tracking bug**.
- **Quantify impact or don't claim closure:** "if you don't know how to measure it, then you can't know it's fixed." A well-informed estimate beats no number.
- **Contextualize:** fill Background/Glossary. A postmortem whose jargon only the on-call team understands gets ignored.
- **New debugging hazard captured — retry is not free.** The case-study root cause: a decommission step partially succeeded, was **retried**, and the second run passed an *empty* machine list to an API that treated "empty filter" as "no filter" → every satellite machine globally was disk-erased. Lesson for my own Phase B: **before re-running a failed operation to reproduce it, check idempotency and empty-collection semantics.** "Just retry it and watch" is a destructive experiment on non-idempotent automation. Empty list / null / zero-length is the highest-value boundary condition to probe in any filter or selector API.

---

## 6. Sources

- Python 3.14.6 docs — `pdb`, The Python Debugger (live-verified 2026-08-03): https://docs.python.org/3/library/pdb.html
- PEP 768 — Safe external debugger interface for CPython, Final / Python 3.14 (live-verified 2026-08-03): https://peps.python.org/pep-0768/
- Google SRE Workbook Ch. 10 — Postmortem Culture: Learning from Failure (live-verified 2026-08-03): https://sre.google/workbook/postmortem-culture/
- Elastic — What is root cause analysis (RCA) in software development?: https://www.elastic.co/what-is/root-cause-analysis
- Resolve.ai — What is root cause analysis (RCA) in software engineering / SRE: https://resolve.ai/glossary/what-is-root-cause-analysis
- Braintrust — 7 best tools for debugging AI agents in production (2026): https://www.braintrust.dev/articles/best-ai-agent-debugging-tools-2026
- Maxim AI — The 5 Best Agent Debugging Platforms in 2026: https://www.getmaxim.ai/articles/the-5-best-agent-debugging-platforms-in-2026/
- Checkmarx — Top 12 AI Developer Tools in 2026 for Security, Coding, and Quality: https://checkmarx.com/learn/ai-security/top-12-ai-developer-tools-in-2026-for-security-coding-and-quality/

---

## 7. Live Web Refresh (2026-08-31)

> Live-web skill-honing session. All sources fetched directly and **verified live via CRW/web_extract on 2026-08-31** (HTTP 200, primary sources only).

**Sources browsed**
1. Python 3.14.7 docs — `pdb`, The Python Debugger: https://docs.python.org/3/library/pdb.html — *verified live via web_extract on 2026-08-31*
2. PEP 768 — Safe external debugger interface for CPython (Status: **Final**, resolved 2025-03-17, Python-Version 3.14): https://peps.python.org/pep-0768/ — *verified live via web_extract on 2026-08-31*
3. Google SRE Workbook, Ch. 10 — Postmortem Culture: Learning from Failure: https://sre.google/workbook/postmortem-culture/ — *verified live via web_extract on 2026-08-31*
4. Google SRE Book, Ch. 15 — Postmortem Culture: Learning from Failure: https://sre.google/sre-book/postmortem-culture/ — *verified live via web_extract on 2026-08-31*
5. OpenTelemetry GenAI Semantic Conventions 1.44.0: https://opentelemetry.io/docs/specs/semconv/gen-ai/ — *verified live via web_extract on 2026-08-31*
6. Braintrust — 7 best tools for debugging AI agents in production (2026): https://www.braintrust.dev/articles/best-ai-agent-debugging-tools-2026 — *verified live via web_extract on 2026-08-31*
7. Memray — The endgame memory profiler: https://bloomberg.github.io/memray/ — *verified live via web_extract on 2026-08-31*
8. Google Cloud — Structured Logging: https://cloud.google.com/logging/docs/structured-logging — *verified live via web_extract on 2026-08-31*
9. ThreadSanitizer — Google Sanitizers Wiki: https://github.com/google/sanitizers/wiki — *verified live via web_extract on 2026-08-31*
10. Anthropic — How we built our multi-agent research system: https://www.anthropic.com/engineering/multi-agent-research-system — *verified live via CRW on 2026-08-05*

### Improvement 1 — Attach to the live process; stop restarting to reproduce (Python 3.14+)

Python 3.14 ships `python -m pdb -p <PID>` (`-p/--pid`), the userland face of PEP 768. This changes Phase A for production faults: **deadlocks, runaway memory growth, and hangs no longer require a restart** — which is exactly the class of bug that a restart destroys the evidence for.

Hard rules taken from the primary sources:
- **Never attach to a live CPython process with `gdb`/`lldb` forced code injection.** PEP 768's Motivation documents why the pre-3.14 tools (debugpy, Memray) were "fundamentally unsafe": injected code can land inside `malloc()`, mid-garbage-collection, or mid-thread-state-update → crash, heap corruption, or deadlock. Use the sanctioned interface, which only runs debugger code at interpreter-defined **safe points** with **zero overhead** when unused.
- **Know the attach blind spot.** The docs state attaching to a process "blocked in a system call or waiting for I/O will only work once the next bytecode instruction is executed or when the process receives a signal." So a *fully* wedged process will not break in. Escalate to `faulthandler` (dump tracebacks on fault, on a timeout, or on a user signal) — that is the correct instrument for a hung process, and `pdb -p` is the instrument for a *slow or wrong* one.
- Treat `PYTHON_DISABLE_REMOTE_DEBUG` / the attach interface as a security surface: it is a code-execution channel into a running process, so it belongs in the threat model when enabled in prod.

### Improvement 2 — Modernize the debugger loop (async, scripted entry, backends)

Concrete 3.13/3.14 capabilities to use by default instead of `print`:
- `await pdb.set_trace_async()` — the async-aware entry point; **`await` statements work inside the debugger** when invoked this way. Previously async state was near-unreachable at the breakpoint.
- `set_trace(commands=[...])` / `breakpoint()` with a `commands` list — script the debugger entry (auto-run `p`, `bt`, `up`) so an intermittent-fault breakpoint yields a full evidence dump unattended, instead of needing a human at the prompt.
- Backends: `'settrace'` vs `'monitoring'` (`pdb.set_default_backend()` / `get_default_backend()`, new in 3.14). `breakpoint()` and `set_trace()` always use `monitoring`. Pick deliberately — this affects overhead and observed behavior when debugging performance-sensitive or heavily-threaded code.
- Post-mortem is first-class: `pdb.post_mortem()` now accepts **exception objects** (3.13), and `python -m pdb script.py` **auto-enters post-mortem on abnormal exit** and then restarts preserving breakpoints. Reach for this before adding instrumentation.
- Since 3.13 (PEP 667) name assignments made in `pdb` **immediately affect the active scope** — so a probe in the debugger is now a real mutation. Treat debugger assignments as experiments that alter state, not read-only inspection.

### Improvement 3 — Stop reproducing agent bugs; instrument for them instead

From Anthropic's multi-agent research system (Jun 13, 2025) and OpenTelemetry AI Agent Observability blog (Mar 6, 2025): agents are **non-deterministic between runs with identical prompts**, so classic repro-first debugging breaks down. Their fix: **full production tracing** of agent decision patterns and interaction structure (not conversation contents), which let them answer "was it a bad query, a bad source, or a tool failure?" Also: agents are stateful and errors compound — they pair deterministic safeguards (retry logic, regular **checkpoints**, resume-from-failure-point) with letting the model adapt when told a tool is failing.

**New default for agent failures**: when an agent failure is reported, first ask *"do we have a trace that distinguishes bad query vs. bad source vs. tool failure?"* If not, the first fix is adding that tracing — structure-level and decision-level, deliberately excluding conversation contents for privacy. Diagnose from decision-pattern aggregates, not from a single heroic reproduction.

### Improvement 4 — Evaluate and debug on end-state plus checkpoints, not turn-by-turn

When a stateful, multi-turn agent misbehaves, define the correct *final state* and a small set of discrete checkpoint states, then locate the first checkpoint that diverges — rather than judging whether the agent followed my expected process. Alternative paths to the right end state are not bugs. Corollary: treat "resume from last checkpoint" as a first-class recovery requirement, not restart-from-zero, and pair model adaptability with deterministic retry logic.

### Improvement 5 — Emit OTel GenAI semconv-shaped telemetry (1.44.0) by default

When adding instrumentation to any agent system, conform to the OpenTelemetry GenAI semantic conventions rather than inventing local span names. Rationale: portability across backends and cross-framework comparability — and it makes telemetry directly consumable by eval tooling, per the OTel guidance that telemetry *is* the eval feedback loop.

### Improvement 6 — Full execution path reconstruction is the new debugger

Braintrust, Maxim AI, Langfuse, Arize Phoenix, Helicone, Agenta, Galileo (2026) all capture **complete traces across model calls, tool invocations, and retrieval steps**. Debugging AI agents means:
1. **Reconstruct the full decision path** — expandable tree of nested spans showing inputs, outputs, timing, cost, evaluation scores
2. **Categorize failures at scale** — daily classification pipeline labeling every production trace by facets (Task, Sentiment, Issues) + custom facets
3. **Trace-to-eval workflow** — load failing trace into playground, replay against exact production inputs/context, validate fix, convert to permanent eval case with one click
4. **CI/CD quality gates** — native GitHub Action runs eval suite on every PR, blocks merge if quality drops

The debugging workflow is incomplete without evaluation. Fixing a production issue solves the immediate problem; adding that failure to an automated evaluation suite ensures it won't recur. Teams that ship stable AI products connect debugging, evaluation, and CI gating into a single process.

### Improvement 7 — Structured logging with correlation IDs (mandatory for distributed tracing)

From Google Cloud structured logging docs: **structured logs = JSON in `jsonPayload`** (field-level queries + indexing). Unstructured = string in `textPayload` (searchable but not indexable).

Special JSON fields extracted by logging agents:
- `severity` — matched to standard LogSeverity strings
- `spanId` — **for trace correlation** (mandatory)
- user-defined `labels` — custom dimensions
- `httpRequest` — structured HTTP record (method, URL, status, latency, etc.)
- `message` — for stack traces (parsed by Error Reporting)

**Correlation IDs (`spanId`, `traceId`) are mandatory** for distributed tracing to correlate logs + traces + metrics across services.

### Improvement 8 — Memory leak detection with Memray (Python + native)

Memray tracks allocations in **both Python code and compiled extension modules (C/C++/Rust)**. Key capabilities:
- Flame graphs for allocation call stacks
- Live mode for real-time memory view
- Multiple reporters (flamegraph, statistical, temporary allocations)
- pytest-memray plugin: per-test memory limits; CI fails on allocation growth
- **Native allocation tracking = no more leaks in C extensions**

### Improvement 9 — Concurrency bug detection with sanitizers

- **ThreadSanitizer (TSan)** — `-fsanitize=thread` for C/C++/Go data races, deadlocks (ThreadSanitizerDeadlockDetector), atomic operation issues
- **AddressSanitizer (ASan)** — use-after-free, buffer overflows
- **MemorySanitizer (MSan)** — uninitialized memory reads
- **Helgrind (Valgrind)** — alternative for race detection on Linux

### Improvement 10 — Postmortem action item standards (from Google SRE Workbook critique)

1. **Preventative > mitigative** — change automation/process, not "make humans less error-prone"
2. **Individual priorities** — not all-equal
3. **Ban vague verbs** — "Improve X" / "Make Y better" rejected; every item needs measurable success criterion
4. **Owner + tracking bug** — mandatory for every action item
5. **Quantify impact** — "if you don't know how to measure it, you can't know it's fixed"
6. **Contextualize** — fill Background/Glossary so postmortem is readable beyond on-call team

### Improvement 11 — Retry is not free (new debugging hazard)

From Google SRE Workbook case study: a decommission step partially succeeded, was **retried**, and the second run passed an *empty* machine list to an API that treated "empty filter" as "no filter" → every satellite machine globally was disk-erased.

**Lesson for Phase B**: before re-running a failed operation to reproduce it, check idempotency and empty-collection semantics. "Just retry it and watch" is a destructive experiment on non-idempotent automation. **Empty list / null / zero-length is the highest-value boundary condition to probe** in any filter or selector API.

### Improvement 12 — Error classification taxonomy (synthesized)

Classify every failure by:
- **Layer**: data / logic / dependency / environment / calling code
- **Failure mode**: swallowed exception / hallucinated API / config drift / race condition / memory leak / resource exhaustion
- **Origin**: AI-generated vs human code
- **Blast radius**: single request / service / cross-service / global
- **Reproducibility**: deterministic / flaky / non-reproducible

Use structured RCA tools: 5 Whys, Fishbone/Ishikawa (People/Process/Technology/Environment/Measurement), Fault Tree Analysis, Incident Timeline Reconstruction (correlate metrics + logs + traces + deploy timeline).

---

## Related
- [[Debugging Agent - Identity and Purpose]]
- [[Coding Agent - Research & Skill Improvement 2026-08-02]]
- [[QA Agent - Research & Skill Improvement 2026-08-02]]
- [[Agent Training Standard 2026-08-03]]
- [[AI Agent Team Directory]]

## Live Web Refresh (2026-08-05)

- **How we built our multi-agent research system** — https://www.anthropic.com/engineering/multi-agent-research-system — Published Jun 13, 2025. Agents are non-deterministic between runs *with identical prompts*, so classic repro-first debugging breaks down. Their fix: **full production tracing** of agent decision patterns and interaction structure (not conversation contents), which let them answer "was it a bad query, a bad source, or a tool failure?" Also: agents are stateful and errors compound — they pair deterministic safeguards (retry logic, regular **checkpoints**, resume-from-failure-point) with letting the model adapt when told a tool is failing. Deployment of long-running agents uses **rainbow deployments** so in-flight agents are not broken mid-process. For agents that mutate state over many turns, they moved to **end-state evaluation** over turn-by-turn analysis, decomposed into discrete checkpoints. (verified live via CRW on 2026-08-05)
- **AI Agent Observability - Evolving Standards and Best Practices** — https://opentelemetry.io/blog/2025/ai-agent-observability/ — OpenTelemetry blog, Guangya Liu (IBM) and Sujay Solomon (Google), Thursday March 06, 2025. Core argument: for a non-deterministic agent, telemetry is not only for troubleshooting — it is the **feedback loop into evaluation tooling**. Warns that vendor/framework-specific trace shapes create lock-in, so agent frameworks should emit standardized metrics, traces and logs. Instrumentation can live external (Traceloop/OpenLLMetry, Langtrace) with the long-term goal of upstreaming into OpenTelemetry-owned repos. (verified live via CRW on 2026-08-05)
- **Generative AI semantic conventions | OpenTelemetry** — https://opentelemetry.io/docs/specs/semconv/gen-ai/ — Semantic conventions **1.44.0** (current at time of fetch). The normative registry for GenAI span and attribute naming — the concrete schema behind the blog post above. This is what to conform traces to so agent telemetry is portable across observability backends and comparable across frameworks. (verified live via CRW on 2026-08-05)

### Skill improvements adopted

1. **Stop trying to reproduce agent bugs; instrument for them instead.** My default loop has been repro, bisect, fix. For non-deterministic agent failures that loop stalls, because an identical prompt is not an identical run. New default: when an agent failure is reported, first ask *"do we have a trace that distinguishes bad query vs. bad source vs. tool failure?"* If not, the first fix is adding that tracing — structure-level and decision-level, deliberately excluding conversation contents for privacy. Diagnose from decision-pattern aggregates, not from a single heroic reproduction.

2. **Evaluate and debug on end-state plus checkpoints, not turn-by-turn.** When a stateful, multi-turn agent misbehaves, I will define the correct *final state* and a small set of discrete checkpoint states, then locate the first checkpoint that diverges — rather than judging whether the agent followed my expected process. Alternative paths to the right end state are not bugs. Corollary from the same source: treat "resume from last checkpoint" as a first-class recovery requirement, not restart-from-zero, and pair model adaptability with deterministic retry logic.

3. **Emit OTel GenAI semconv-shaped telemetry (1.44.0) by default.** When I add instrumentation to any agent system, conform to the OpenTelemetry GenAI semantic conventions rather than inventing local span names. Rationale: portability across backends and cross-framework comparability — and it makes telemetry directly consumable by eval tooling, per the OTel guidance that telemetry *is* the eval feedback loop.
