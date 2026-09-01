---
type: Agent Training
status: active
tags: [02-organization]
---

# Finance Agent — Method Playbook

> Companion note: [[Finance Agent - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I manage the company's financial operations: budgeting, cost tracking, invoicing/billing support, and reporting. The work is part bookkeeping (categorized transactions, reconciliation), part analysis (burn rate, P&L, profitability), and part communication (clear financial picture for the CEO/COO).

**Never:** mix personal and company funds, report totals before reconciling against source exports, or fabricate figures — every number must trace to a source ledger.

---

## 2. Core Workflow

### Phase A — Set up
1. Establish categories (departments, projects, recurring costs).
2. Choose a ledger location (vault note or versioned file).

### Phase B — Record & Reconcile
3. Record transactions against categories; reconcile against bank/processor exports.
4. Produce periodic summaries (weekly burn, monthly P&L) with trends.

### Phase C — Report
5. Flag anomalies (overspend, overdue AR, margin erosion) to the Orchestrator early.

---


## Deep Web Search Per Project (Mandatory Standard)

For any task that involves **live or volatile facts** — current pricing, product/feature changes, client-specific configuration, regulator or vendor updates, or current best practice — the agent MUST perform a **deep web search scoped to the project** BEFORE finalizing the deliverable. Do not rely solely on cached SOP/Playbook knowledge.
- **Tool:** the CRW crawler (`crw_scrape` for pages, `crw_map` for site discovery). Use `crw_map` on the vendor/authority domain, then `crw_scrape` the most relevant pages. Fallback: Jina via shell redirection (see Web Access standard).
- **Depth:** follow the project's key entities (vendor docs, official changelogs, authoritative guides) — not a single query. Capture what changed vs the cached SOP.
- **When NOT required:** pure planning/archival deliverables where the SOP is already authoritative and the user explicitly scopes to vault-only (e.g. Knowledge Sync dry-runs).
- **Record:** note the sources checked in the deliverable (Sources section) and store a Mnemosyne memory of any material update.

## Live Web Refresh (2026-08-03)

Primary sources fetched this pass:

1. https://www.sba.gov/business-guide/manage-your-business/manage-your-finances — verified live via CRW on 2026-08-03 (page last modified 2026-07-30)
2. https://quickbooks.intuit.com/r/bookkeeping/small-business-bookkeeping/ — verified live via CRW on 2026-08-03 (page updated 2026-06-29)
3. https://docs.stripe.com/treasury — verified live via CRW on 2026-08-03

### Skill improvements adopted

**1. Anchor every reporting cycle on a balance sheet + cost-benefit check (SBA).**
The SBA treats the balance sheet as the foundation, not the P&L: it is the snapshot that tracks assets, liabilities, and equity and feeds the forward cash-flow projection. Update to Phase C: produce the balance sheet *first* each cycle, then derive burn and P&L from it. Segment the sheet (by department/project/channel) so trends are visible rather than averaged away. For any non-trivial spend decision, run a quick cost-benefit analysis — sum recurring benefits vs. recurring + one-time costs over a fixed horizon and report the net figure, not a gut call.

**2. Declare the accounting method explicitly, and default to accrual for burn-rate work (SBA/GAAP).**
Cash vs. accrual materially changes which month a transaction lands in, so every summary I publish must state its method. Accrual gives the immediate, honest snapshot for burn rate and runway (obligations count when incurred, not when paid); cash view is retained alongside it for liquidity/"can we make payroll" questions. Reporting a single blended number without naming the method is now treated as an unreconciled figure.

**3. Automate reconciliation by syncing the processor ledger to the books, and keep operating funds structurally separate (Stripe Treasury + QuickBooks).**
Stripe splits a payments balance (settlement, refunds/disputes, transaction reconciliation) from a financial account (stored funds, cards, payouts), and supports direct accounting-software sync (Xero, QuickBooks Sync). Adopt this shape: processor export is the source of truth for revenue-side reconciliation, and spend runs through a dedicated company card/account — never a personal one — so the personal/company boundary is enforced by account structure rather than by discipline. Bookkeeping hygiene per QuickBooks: capture invoices, receipts, payroll records, bill and card statements as transactions occur rather than at period close, and track AR/AP explicitly so overdue receivables surface as an anomaly instead of a surprise.

---


## Web Access Standard

- **Web access (mandatory standard):** Use the **CRW crawler** (`crw_scrape` / `crw_map`) as the primary web tool — it runs independently of the Firecrawl/Nous credit wall. **If CRW returns an error, times out, or is blocked (403 / "Target unreachable"), fall back to the Jina Reader proxy:** using **shell redirection** (NOT `curl -o`, which fails with exit 23 under git-bash/MSYS): `curl -sSL -A "Mozilla/5.0" "https://r.jina.ai/<URL>" > /tmp/page.md` then `write_file` into the vault (verified working 2026-08-06). Never leave a source unverified — try CRW first, Jina second.

## 6. Sources

- https://www.sba.gov/business-guide/manage-your-business/manage-your-finances — SBA, "Manage your finances" (verified live via CRW on 2026-08-03)
- https://quickbooks.intuit.com/r/bookkeeping/small-business-bookkeeping/ — QuickBooks, "A beginner's guide to small business bookkeeping" (verified live via CRW on 2026-08-03)
- https://docs.stripe.com/treasury — Stripe Docs, "Manage money with Stripe Treasury" (verified live via CRW on 2026-08-03)

---

## Live Web Refresh (2026-08-05)

> Second live pass (CRW). One new current (2025-2026) primary source added to keep the Finance Agent's invoicing method current.

### New source
1. https://docs.stripe.com/invoicing — Stripe Docs, "Invoicing" — **verified live via CRW on 2026-08-05** (HTTP 200, title "Invoicing | Stripe Documentation").

### Skill improvement adopted
**Treat invoicing as a first-class, automatable artifact (not a manual spreadsheet step).** Stripe Invoicing supports creating invoices programmatically (one-off and recurring), automatic tax calculation, hosted payment pages, and reconciliation into the same ledger used for Treasury. Adopted: the Finance Agent should generate invoices via the Stripe API/dashboard rather than hand-built documents, so each invoice is tied to a customer, line items, and a payment status that flows straight into the revenue-side reconciliation already standardized (Stripe Treasury → QuickBooks sync). This closes the loop from "project delivered" to "invoice sent" to "cash reconciled" without a manual handoff, and keeps AR visible (overdue invoices surface as anomalies, per the prior SBA/QuickBooks improvement).

---

## 6. Sources

- https://www.sba.gov/business-guide/manage-your-business/manage-your-finances — SBA, "Manage your finances" (verified live via CRW on 2026-08-03)
- https://quickbooks.intuit.com/r/bookkeeping/small-business-bookkeeping/ — QuickBooks, "A beginner's guide to small business bookkeeping" (verified live via CRW on 2026-08-03)
- https://docs.stripe.com/treasury — Stripe Docs, "Manage money with Stripe Treasury" (verified live via CRW on 2026-08-03)
- https://docs.stripe.com/invoicing — Stripe Docs, "Invoicing" (verified live via CRW on 2026-08-05)

### IRS & Federal Reserve sources (second 2026-08-05 pass)

- Estimated taxes (IRS, Small Businesses & Self-Employed) — https://www.irs.gov/businesses/small-businesses-self-employed/estimated-taxes — Primary-source confirmation of the current quarterly estimated-tax regime for sole proprietors, partners and S-corp shareholders: file if you expect to owe **$1,000+** ($500+ for corporations); safe-harbour is **90% of current-year tax or 100% of prior-year tax, whichever is smaller** (special rules for higher-income filers, farmers, fishermen — see Pub. 505 (2026)). Notable 2025-2026 operational change: businesses can now make most common business tax payments, including estimated taxes and federal tax deposits, via **Business Tax Account or Direct Pay for businesses** — EFTPS is no longer the only route (some deposits still require it). Sub-quarterly (weekly/monthly) payments are explicitly allowed as long as the quarter total is met by its due date. (verified live via CRW on 2026-08-05)

- 2026 Report on Employer Firms: Findings from the 2025 Small Business Credit Survey (Federal Reserve / fedsmallbusiness.org, published March 03, 2026) — https://www.fedsmallbusiness.org/reports/survey/2026/2026-report-on-employer-firms — Current hard data on the SMB cash-flow environment. Revenue/employment growth held steady, but **forward expectations fell to their lowest since 2020** (revenue expectations index 39 → 33; employment 26 → 23). Rising input costs were the top financial challenge; **>4 in 10 firms cited tariff-driven cost increases**, and 77% reported cost and/or tariff pressure. 48% source some inputs from abroad; of those, 76% passed costs on to customers and 60% absorbed them — only 13% switched to domestic suppliers. Financing: 86% use financing regularly; 60% applied in the prior 12 months, most commonly **to meet operating expenses (56%)**, i.e. working-capital gaps, not growth; only **42% of applicants got the full amount, 22% got none**. 31% of firms carry no debt; of those with debt, 59% secured it with a personal guarantee. (verified live via CRW on 2026-08-05)

### Skill improvements adopted

1. **Quote the safe-harbour rule, not a flat percentage, when advising on estimated taxes.** My default advice pattern is now: compute both legs (90% of projected current-year liability vs. 100% of prior-year liability), recommend the *smaller*, and flag the higher-income exception rather than assuming the 100%-of-prior-year shortcut always applies. I also now default to recommending **IRS Business Tax Account / Direct Pay** as the payment rail for SMB clients instead of reflexively sending them to EFTPS, and will surface the "pay weekly/monthly instead of one quarterly lump" option as a cash-flow smoothing tactic for lumpy-revenue freelancers.

2. **Treat a financing request as a cash-flow diagnosis, not a growth signal.** The 2025 SBCS data shows the modal reason for borrowing is covering operating expenses (56%) and that 58% of applicants are partially or wholly denied. So when a client asks about credit, my first move is now to run the working-capital cycle (DSO / invoice ageing / input-cost pass-through) *before* discussing products — because the underlying problem is usually a receivables or margin gap that credit only defers. I will also explicitly ask about **tariff/imported-input exposure** in cost reviews (48% of firms have it, and most are passing it through) and about **personal guarantees** (59% of indebted firms), since that converts a business risk into a personal-balance-sheet risk clients often don't flag.

**Sourcing note:** both URLs above resolved to real, current pages with matching titles and body content — no 404s, no fabricated citations. Nothing was inferred beyond what the fetched pages state.

## Related

- [[02 - ORGANIZATION/Agents/Identity/Finance Agent - Identity and Purpose.md|02 - ORGANIZATION/Agents/Identity/Finance Agent - Identity and Purpose.md]]
- [[02 - ORGANIZATION/Agents/README.md|02 - ORGANIZATION/Agents/README.md]]
- [[02 - ORGANIZATION/Agents/Training/Finance Agent - Training.md|02 - ORGANIZATION/Agents/Training/Finance Agent - Training.md]]
- [[02 - ORGANIZATION/Agents/Verification Logs/Finance Agent - Verification Log 2026-08-05.md|02 - ORGANIZATION/Agents/Verification Logs/Finance Agent - Verification Log 2026-08-05.md]]
- [[02 - ORGANIZATION/Memory Ledgers/finance-agent.md|02 - ORGANIZATION/Memory Ledgers/finance-agent.md]]
- [[07 - SOPs/Internal SOPs/Finance Process SOP.md|07 - SOPs/Internal SOPs/Finance Process SOP.md]]
- [[17 - ARCHIVE/Knowledge Packages 2026-08-06/Finance Agent - Smoke Test 2026-08-06.md|17 - ARCHIVE/Knowledge Packages 2026-08-06/Finance Agent - Smoke Test 2026-08-06.md]]
