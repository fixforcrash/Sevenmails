---
type: Agent Training
status: active
tags: [02-organization]
---

# Migration Expert — Method Playbook

> **Refreshed 2026-08-03** by the Research Agent. Rewritten in place from a raw search-snippet dump into an actionable operating playbook grounded in 2025–2026 practice.
> Companion note: [[Migration Expert - Identity and Purpose]] · Standard: [[Agent Training Standard 2026-08-03]]

---

## 1. Domain Summary

I **move systems, data, and workloads from one environment to another with minimal risk and minimal (ideally zero) downtime.** Migration covers databases, applications, storage, and whole clouds (on-prem → cloud, cloud → cloud, cloud → on-prem). The discipline is about de-risking change: understanding dependencies, preserving integrity, and having a credible rollback.

The 2025–2026 shift that matters: **zero-downtime is now the default expectation, not a luxury.** Continuous replication, parallel-run (shadow) periods, and automated rollback are standard for production workloads, and managed services (DMS, Dataflow, Storage Transfer) have made live cutovers routine. AI-assisted schema mapping and validation are increasingly part of the toolchain.

**Never:** migrate without a full backup and tested restore, cut over without a parallel-run validation, or treat "it copied" as "it's correct" without checksum/row-count reconciliation.

---

## 2. Core Workflow

### Phase A — Discover and Assess
1. **Inventory everything** — databases, schemas, dependencies, volumes, network topology, and hidden couplings (cron, triggers, external consumers).
2. **Classify by criticality and volatility** to sequence the plan; identify the system-of-record vs derived data.
3. **Choose a strategy** — rehost (lift-and-shift), replatform, refactor, or replace — matched to the business goal, not the tool.

### Phase B — Plan and Prepare
4. **Establish a baseline backup + tested restore** before anything moves; this is the ultimate rollback.
5. **Set up continuous replication** (CDC / log shipping / object replication) from source to target to shrink the cutover delta.
6. **Map schemas and transforms** — resolve type mismatches, encoding, time zones, and identity/key collisions up front.

### Phase C — Validate in Parallel
7. **Run a parallel/shadow environment** — replicate source to target and run the new system alongside the old.
8. **Reconcile data** — row counts, checksums, and business-key spot checks; quantify drift continuously.
9. **Load and performance test** the target at production scale; fix bottlenecks before cutover.

### Phase D — Cut Over
10. **Lower DNS/TTLs and pick a low-traffic window**; freeze writes on the source if a true zero-downtime pattern isn't used.
11. **Execute the cutover runbook** — final sync, quiesce source, promote target, repoint traffic, verify health.
12. **Keep the source intact** during a parallel-run/monitoring period; do not decommission until confidence is high.

### Phase E — Stabilize and Persist
13. **Monitor post-cutover** for data drift, latency, and errors; keep rollback ready for the agreed burn-in window.
14. **Write the migration runbook and decisions to the Vault, then re-read the file** (verify-after-write). Persist reusable patterns (replication choice, rollback state) to Mnemosyne.

---

## 3. Recommended Tools

| Tool | What it's for | When to use |
|---|---|---|
| AWS DMS / Azure DMS / Google Datastream | Continuous DB replication & CDC | Heterogeneous or homogeneous DB migration. |
| Storage Transfer Service / `rclone` / `aws s3 sync` | Bulk object/file movement | Petabyte-scale storage migration. |
| `pg_dump`/`pg_restore`, `mysqldump`, `mongodump` | Logical backup/restore | Small DBs or as the baseline backup. |
| Schema-mapping tools (Cloud Data Fusion, Striim) | Map/transform schemas | Complex or legacy schema conversions. |
| Reconciliation scripts (row counts, checksums) | Verify data integrity post-move | Every migration, automated in CI. |
| Terraform / IaC | Reproduce target infrastructure | Replatform/refactor migrations. |
| `dig` + DNS TTL control | Traffic cutover via DNS | App-layer cutovers and rollback. |

---

## 4. Current Best Practices (2025–2026)

- **Backup + tested restore first** — the rollback of last resort is non-negotiable.
- **Continuous replication shrinks cutover** — use CDC/log-shipping so the final delta is tiny.
- **Parallel-run before promoting** — validate the target against live traffic before it becomes primary.
- **Reconcile, don't assume** — row counts, checksums, and key spot-checks prove correctness.
- **Match strategy to goal** — lift-and-shift for speed, refactor for value; don't over-engineer.
- **Automate the runbook** so cutover is repeatable and rollback is one step.
- **Keep source alive through burn-in** — decommission only after the monitoring window passes.
- **Load-test the target at scale** before, not after, cutover.

---

## 5. Common Pitfalls

| Pitfall | Fix |
|---|---|
| No tested restore | Backup + prove restore before migrating. |
| Cutover with un-synced delta | Use continuous replication; final sync at cutover. |
| "Copied" assumed "correct" | Reconcile counts/checksums; spot-check keys. |
| No parallel-run validation | Shadow the target against live traffic. |
| Source deleted too early | Keep source through the burn-in window. |
| Schema type/encoding mismatches | Resolve mapping before load. |
| High TTL blocking fast rollback | Lower TTLs ahead of the window. |
| Runbook only in someone's head | Codify and rehearse it. |

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

Fresh primary-source pass focused on **tenant cutover and mailbox migration**, a gap in the prior cloud/DB-centric playbook.

**Sources fetched this pass:**
- Microsoft Learn — Plan a Microsoft 365 tenant-to-tenant migration: https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-tenant-to-tenant-migrations — *verified live via Jina on 2026-08-03*
- Microsoft Learn — What you need to know about migrating IMAP mailboxes to Microsoft 365: https://learn.microsoft.com/en-us/exchange/mailbox-migration/migrating-imap-mailboxes/migrating-imap-mailboxes — *verified live via Jina on 2026-08-03*
- AWS Prescriptive Guidance — Guide for AWS large migrations (phases / cutover): https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/introduction.html — *verified live via CRW on 2026-08-03 (HTTP 200)*

**Skill improvements adopted:**

1. **Plan the coexistence window, not just the cutover.** For tenant-to-tenant moves (M&A, divestiture, consolidation) users legitimately live in both tenants for a period. The plan must explicitly cover **identity/UPN mapping** (cross-tenant identity mapping; keep vs. reissue UPN), **domain transfer timing**, **inter-tenant mail routing**, **calendar free/busy sharing**, and **Teams federation**. Treat coexistence as a designed state with its own runbook — not as migration overrun.

2. **Sequence by workload dependency.** Workloads are coupled: **Teams content depends on Exchange mailboxes** (migrate mailboxes before or alongside Teams), and **OneDrive + SharePoint share a permissions model** (migrate together). Use an orchestrated multi-workload migration (Migration Orchestrator) when batches must stay coordinated; use per-workload cross-tenant tools only when you need independent timelines. Verify **target-tenant licenses exist before the wave starts** — missing licenses stall a batch mid-cutover.

3. **Neutralize retention policies before reconciliation, and respect hard tool limits.** Disable **MRM/archival policies** on target mailboxes before migrating: items those policies delete or archive get flagged "missing" by the migration tool, producing *perceived* data loss that masks *real* data loss during verification. Also pre-flight the platform ceilings: IMAP migration carries **mail only** (no contacts/calendar/tasks), caps at **500,000 items per mailbox** (newest → oldest) and **35 MB per message**, and **mailboxes on hold may block migration**. Raise per-user / per-IP / server connection limits on the source to lift throughput. Size waves from real throughput drivers — user count, mailbox and OneDrive/SharePoint volume, holds, and bandwidth — rather than a calendar guess.

---

## 6. Sources

> **Verified live via CRW web crawler (crw_scrape) on 2026-08-03 (HTTP 200, real content)** — fetched via the CRW web crawler (crw_scrape), independent of the Firecrawl/Nous credit wall. All five URLs below returned HTTP 200 and are real primary sources: AWS "what is cloud migration", Google Cloud Database Migration Service, New Relic downtime-avoidance strategies, Northflank's 2026 AWS migration guide, and Microsoft Learn Azure Migrate docs.

- AWS — What is cloud migration? / DMS: https://aws.amazon.com/what-is/cloud-migration/
- Google Cloud — Database Migration Service / Dataflow: https://cloud.google.com/database-migration
- New Relic — Strategies to avoid downtime in cloud migration: https://newrelic.com/blog/infrastructure-monitoring/migrating-data-to-cloud-avoid-downtime-strategies
- Northflank — AWS cloud migration guide 2026: https://northflank.com/blog/aws-cloud-migration-guide
- Microsoft Learn — Azure Migrate: https://learn.microsoft.com/azure/migrate/

**Added 2026-08-03 live refresh (tenant cutover / mailbox migration):**
- Microsoft Learn — Plan a Microsoft 365 tenant-to-tenant migration: https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-tenant-to-tenant-migrations *(verified live via Jina on 2026-08-03)*
- Microsoft Learn — Migrating IMAP mailboxes to Microsoft 365: https://learn.microsoft.com/en-us/exchange/mailbox-migration/migrating-imap-mailboxes/migrating-imap-mailboxes *(verified live via Jina on 2026-08-03)*
- AWS Prescriptive Guidance — Guide for AWS large migrations: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/introduction.html *(verified live via CRW on 2026-08-03)*

---

## Related
- [[Migration Expert - Identity and Purpose]]
- [[Agent Training Standard 2026-08-03]]
- [[DNS Expert - Research & Skill Improvement 2026-08-02]]

## Live Web Refresh (2026-08-05)

- Ways to migrate multiple email accounts to Microsoft 365 or Office 365 — https://learn.microsoft.com/en-us/exchange/mailbox-migration/mailbox-migration — Canonical decision tree for on-prem Exchange to Exchange Online: cutover (up to 2000 mailboxes, but Microsoft explicitly recommends 150 or fewer in practice due to provisioning/move time), staged (Exchange 2003/2007, over 2000), hybrid (Exchange 2010+ or batches over time), IMAP, and the PST Import Service (network upload or drive shipping). Always pre-check Exchange Online limits plus migration best practices BEFORE sizing batches. (verified live via CRW on 2026-08-05)
- Cross-tenant mailbox migration (Microsoft 365 Enterprise) — https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-mailbox-migration — Merger/divestiture path using New-MigrationBatch plus MRS under the "Move Mailboxes" management role. Target user MUST pre-exist as a MailUser with correct attributes or the move fails. Post-move the source mailbox is converted to a MailUser with targetAddress/ExternalEmailAddress stamped for coexistence and mail routing. Hard blockers: mailboxes on ANY hold are blocked; only user-visible content (mail, contacts, calendar, tasks, notes) moves; the source mailbox is deleted and is NOT recoverable or discoverable afterwards. Requires a paid per-user Cross-Tenant User Data Migration add-on license (assignable source or target side) with no exceptions; a missing license throws CrossTenantMigrationWithoutLicensePermanentException. Scope is enforced via a mail-enabled security group in the source tenant. (verified live via CRW on 2026-08-05)
- Google Workspace Admin Help — Data migration hub — https://support.google.com/a/answer/6167194 — Reachable only via the JS renderer; the direct HTTP fetch failed and only navigation chrome was returned, so no substantive content was extracted. Recorded as a CRW retrieval limitation, not as a sourced finding. (partially verified live via CRW on 2026-08-05)

### Skill improvements adopted

1. **Gate every cross-tenant move on licensing and holds BEFORE building the batch.** New pre-flight order: (a) confirm Cross-Tenant User Data Migration add-on licenses are purchased and assigned, (b) enumerate and release/expire litigation and retention holds, (c) verify target MailUser objects exist with correct attributes, (d) confirm the source-side mail-enabled security group scope. Skipping (a) or (b) produces hard failures, not warnings, and because the source mailbox is deleted post-move there is no rollback. Treat cross-tenant as one-way and require a verified export/backup before cutover.
2. **Size cutover batches by real-world throughput, not the documented ceiling.** Microsoft's own guidance states the 2,000-mailbox cutover ceiling is unrealistic and that roughly 150 mailboxes is the practical cap. Adopt: any migration over 150 mailboxes defaults to staged or hybrid coexistence, and batch sizing is validated against Exchange Online limits and migration best-practice docs during planning rather than discovered mid-cutover.

---

## Live Web Refresh (2026-08-31) — Microsoft 365 ↔ Google Workspace, Tenant-to-Tenant, IMAP, Coexistence, Cutover, Licensing, Post-Migration Validation

**Sources fetched this pass (all verified live via web_extract/crw 2026-08-31):**

**Google Workspace Data Import Tool (Exchange Online → Google Workspace):**
- About the data import tool: https://knowledge.workspace.google.com/admin/migrate — Overview of default vs advanced import methods, supported editions (updated 2026-08-26)
- What's imported from Exchange Online: https://knowledge.workspace.google.com/admin/migrate/whats-migrated-in-an-exchange-online-migration — Complete data coverage matrix (email, calendar, contacts, tasks; what's NOT imported) (updated 2026-08-26)
- Use default data import method for Exchange Online: https://knowledge.workspace.google.com/admin/migrate/migrate-data-from-an-exchange-online-account — Step-by-step, CSV mapping, delta imports (updated 2026-08-26)
- Use advanced data import method for Exchange Online: https://knowledge.workspace.google.com/admin/migrate/migrate-exchange-online-data-in-batches — Azure app setup, 5,000 users/batch, 10 batches, identity map, delta imports (updated 2026-08-31)
- Set up Azure application for Exchange Online: https://knowledge.workspace.google.com/admin/migrate/set-up-microsoft-entra-for-enterprise — PowerShell script + manual Azure portal steps for app registration, permissions, client secret (updated 2026-08-26)
- Run delta import for Exchange Online: https://knowledge.workspace.google.com/admin/migrate/run-a-delta-migration — Incremental sync behavior, limitations (updated 2026-08-26)
- Understand Exchange Online data import reports: https://knowledge.workspace.google.com/admin/migrate/understand-exchange-online-data-migration-reports — Report fields, error codes, troubleshooting (updated 2026-08-26)
- Troubleshoot Exchange Online data imports: https://knowledge.workspace.google.com/admin/migrate/troubleshoot-exchange-online-data-migrations — Common errors, calendar declined events, email count discrepancy (updated 2026-08-26)
- Google Workspace migration product matrix: https://knowledge.workspace.google.com/admin/migrate/google-workspace-migration-product-matrix — Tool selection by data source and user count (updated 2026-08-26)
- Check events for data import tool: https://knowledge.workspace.google.com/admin/migrate/check-events-for-the-new-data-migration-service — Audit log events for migration tracking (updated 2026-08-26)

**Microsoft 365 Tenant-to-Tenant Migration:**
- Plan a Microsoft 365 tenant-to-tenant migration: https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-tenant-to-tenant-migrations — Architecture models, workload dependencies, coexistence, licensing, timeline (updated 2026-06-19)
- Migration Orchestrator overview: https://learn.microsoft.com/en-us/microsoft-365/enterprise/migration-orchestrator-1-overview — Supported workloads (Exchange, OneDrive, Teams chats, Teams meetings), licensing, identity mapping requirement, scope limits (updated 2026)
- Migration Orchestrator planning and prerequisites: https://learn.microsoft.com/en-us/microsoft-365/enterprise/migration-orchestrator-2-planning-prerequisites — Prevalidation checks, identity mapping ordering, mailbox/OneDrive provisioning prevention (updated 2026)
- Cross-tenant mailbox migration: https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-mailbox-migration — MRS-based move, MailUser setup, licensing, endpoint/org relationship config, error codes (updated 2026)
- Cross-Tenant Identity Mapping (CTIM): https://learn.microsoft.com/en-us/microsoft-365/enterprise/cross-tenant-identity-mapping — Required for Orchestrator, optional for standalone; 5-phase workflow, MailUser attribute requirements (ExchangeGuid, ArchiveGuid, LegacyExchangeDN x500, UPN, PrimarySMTP, TargetAddress), hybrid vs cloud-only write process (updated 2026)
- Migrating IMAP mailboxes to Microsoft 365: https://learn.microsoft.com/en-us/exchange/mailbox-migration/migrating-imap-mailboxes/migrating-imap-mailboxes — IMAP limitations (mail only, 500k items, 35MB, MRM policy interference) (updated 2026)

### Skill improvements adopted (2026-08-31)

1. **Google Workspace Data Import Tool is now the primary self-service path for M365→Google migrations** (replacing GWMME for most scenarios). Two tiers: Default (shared quota, 1,000 users) and Advanced (dedicated Azure app quota, 5,000 users/batch, 10 concurrent batches). Use Advanced for >1,000 users or when you need In-Place Archives, Group mailboxes, event attachments, calendar permissions. Identity mapping via CSV (Source Exchange Email → Target GUser); UPN must match if different from mail.

2. **Delta imports are critical for both directions** — Google: run delta after initial import to capture new/updated data; don't run if destination email changed. Microsoft: Migration Orchestrator handles incremental passes; cross-tenant mailbox migration is one-way (source deleted). Always validate with reports: Google provides user summary + import reports with error codes; Microsoft provides batch reports + CTIM validation (`Get-CtimReport`, `Verify-CtimWrittenAttributes`).

3. **Email count discrepancies are expected and documented** — Exchange counts duplicates across folders; Gmail consolidates to single message + multiple labels. The "Emails imported" total should match "Emails discovered" total, not the source folder count. This is NOT data loss.

4. **MRM/archival policies on TARGET must be disabled BEFORE migration** — Both Microsoft and Google docs warn: policies that delete/archive items cause migration tools to flag them as "missing" = perceived data loss masking real data loss. This applies to IMAP migrations to M365 and data imports to Google Workspace.

5. **IMAP migration is mail-only with hard limits** — 500,000 items/mailbox (newest→oldest), 35MB/message, no contacts/calendar/tasks. Source connection limits (per-user, per-IP, server/firewall) must be raised for throughput. Target mailboxes must exist + be licensed first.

6. **Tenant-to-tenant coexistence window must be designed, not endured** — Plan for: mail routing (source MailUser targetAddress stamps), calendar free/busy sharing, Teams federation. CTIM attributes (LegacyExchangeDN as x500 proxyAddresses) are critical for reply/autocomplete continuity. Treat coexistence as a designed state with its own runbook.

7. **Cross-Tenant User Data Migration license is a hard gate** — Per-user, one-time fee, assignable source or target side, NO exceptions. Migration fails with `CrossTenantMigrationWithoutLicensePermanentException` if missing. Source mailbox is DELETED post-migration (no rollback, no recovery). Pre-flight order: (1) licenses purchased/assigned, (2) holds released/expired, (3) target MailUser objects verified (ExchangeGuid, ArchiveGuid, LegacyExchangeDN, UPN, PrimarySMTP, TargetAddress), (4) source mail-enabled security group scope confirmed.

8. **Batch sizing: practical cap ~150 mailboxes** — Microsoft's documented 2,000 ceiling is unrealistic. Size waves by real throughput drivers: mailbox volume, OneDrive/SharePoint size, holds, bandwidth. Migration Orchestrator sequences multi-workload batches automatically (mailboxes before/with Teams; OneDrive+SharePoint together).

9. **Migration tools are productivity features, NOT compliance tools** — Both Microsoft and Google explicitly state this. Organizations are responsible for legal compliance (retention, holds, eDiscovery) independently of migration tooling.
