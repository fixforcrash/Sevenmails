# Sync Protocol: Obsidian Vault ↔ GitHub

## Overview

This document defines the bidirectional synchronization protocol between the Obsidian Vault (source of truth for agent knowledge) and the GitHub repository (version control, CI/CD, collaboration).

## Principles

1. **Vault is authoritative** for content — GitHub mirrors Vault
2. **GitHub is authoritative** for version history, CI gates, and team collaboration
3. **Both directions** must be validated before applying changes
4. **Mnemosyne sync** is verified but not auto-synced (agent-owned)

## Sync Directions

### Vault → GitHub (Pull from Vault)

**Trigger:** Manual (workflow_dispatch) or Daily 02:00 via n8n

**Process:**
1. Run `scripts/vault-to-github.py`
2. Extract all playbooks from `02 - ORGANIZATION/Agents/Playbooks/`
3. Extract SOUL.md from each agent profile
4. Compare content hash with GitHub
5. Commit changes if different
6. Push to `main` branch

**Validation:**
- Frontmatter validation (`validate-frontmatter.py --type playbook`)
- Playbook structure validation (`validate-playbook-structure.py`)
- No merge conflicts (fast-forward only)

### GitHub → Vault (Push to Vault)

**Trigger:** Push to `main` branch (auto) or Manual (workflow_dispatch)

**Process:**
1. Run `scripts/github-to-vault.py`
2. Validate changed files (frontmatter + structure)
3. Apply changes to Vault playbooks by department
4. Apply SOUL.md changes to agent profiles
5. Verify write succeeded (read-back)

**Validation:**
- All validations must pass before write
- Rollback on any validation failure
- Notify Manager on failure

## Conflict Resolution

| Scenario | Resolution |
|----------|------------|
| Vault newer than GitHub | Vault wins (auto-sync) |
| GitHub newer than Vault | GitHub wins (auto-sync on merge) |
| Both changed | Manual resolution required — alert Manager |
| Frontmatter invalid | Block sync — fail CI |

## File Mapping

| Vault Path | GitHub Path |
|------------|-------------|
| `02 - ORGANIZATION/Agents/Playbooks/Technical/*.md` | `playbooks/TECHNICAL/*.md` |
| `02 - ORGANIZATION/Agents/Playbooks/Sales/*.md` | `playbooks/SALES/*.md` |
| `02 - ORGANIZATION/Agents/Playbooks/Marketing/*.md` | `playbooks/MARKETING/*.md` |
| `02 - ORGANIZATION/Agents/Playbooks/Operations/*.md` | `playbooks/OPERATIONS/*.md` |
| `profiles/<agent>/SOUL.md` | `soul-templates/<agent>.md` |
| `profiles/<agent>/config.yaml` | `agent-profiles/<agent>/config.yaml` |
| `profiles/<agent>/mcp_servers.yaml` | `agent-profiles/<agent>/mcp_servers.yaml` |

## Mnemosyne Sync (Separate)

Mnemosyne is **agent-owned** — not auto-synced by this protocol.

**Verification only:** `mnemosyne-sync-check.py` runs weekly to detect drift:
- Playbook modified vs Mnemosyne last update >24h → Alert
- Playbook exists but no Mnemosyne memories → Alert
- Mnemosyne memories but no playbook → Alert

**Remediation:** Agent must self-persist to Mnemosyne (via CLI). Manager routes alert to agent.

## CI/CD Gates

### Pull Request Gates (Required)
- ✅ `validate-playbooks.yml` — Frontmatter + structure
- ✅ `validate-soul-md.yml` — SOUL.md structure
- ✅ All checks must pass to merge

### Post-Merge Gates
- ✅ `sync-github-to-vault.yml` — Auto-sync to Vault
- ✅ `mnemosyne-sync-check.yml` — Verify agent sync (weekly)

## Monitoring & Alerts

| Alert | Channel | Frequency |
|-------|---------|-----------|
| Sync failure | Manager notification | Immediate |
| Mnemosyne drift >24h | Manager + Agent | Weekly |
| Validation failure | PR checks | Per PR |
| Drift >7 days | CEO escalation | Weekly |

## Manual Commands

```bash
# Local development
cd agent-org-config

# Vault → GitHub (preview)
python scripts/vault-to-github.py --dry-run

# Vault → GitHub (apply)
python scripts/vault-to-github.py

# GitHub → Vault (preview)
python scripts/github-to-vault.py --dry-run

# GitHub → Vault (apply)
python scripts/github-to-vault.py

# Validate all
python scripts/validate-frontmatter.py --dir playbooks --dir soul-templates
python scripts/validate-playbook-structure.py --dir playbooks
python scripts/validate-soul-md.py --dir soul-templates --dir agent-profiles

# Mnemosyne check
python scripts/mnemosyne-sync-check.py
```

## Rollback Procedure

If sync introduces issues:

1. **GitHub → Vault rollback:**
   ```bash
   git revert <commit-sha>
   git push
   # Triggers auto-sync to Vault
   ```

2. **Vault → GitHub rollback:**
   - Restore Vault from backup (Obsidian sync/history)
   - Re-run `vault-to-github.py`

3. **Emergency:** Disable n8n workflows, manual fix, re-enable.

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-09-01 | Initial protocol |