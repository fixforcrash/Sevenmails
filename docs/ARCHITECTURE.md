# Architecture: Agent Organization Configuration

## System Overview

```
┌─────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  Obsidian Vault │────▶│  GitHub Repo     │────▶│  Hermes Agents   │
│  (Source of     │     │  (Version Ctrl,  │     │  (Runtime        │
│   Truth)        │     │   CI/CD, Sync)   │     │   Execution)     │
└─────────────────┘     └──────────────────┘     └──────────────────┘
        │                       │                       │
        │              ┌────────┴────────┐              │
        │              │                 │              │
        ▼              ▼                 ▼              ▼
   Playbooks       GitHub Actions      Mnemosyne      Agent Profiles
   SOUL.md         n8n Workflows       (per-agent)    (config.yaml)
   Agent Registry  Validation          Persistence    MCP Servers
```

## Components

### 1. Obsidian Vault (Primary Knowledge Store)
- **Location:** `C:/Users/black/Documents/Obsidian Vault/`
- **Structure:**
  - `02 - ORGANIZATION/Agents/Playbooks/` — 44 playbooks by department
  - `02 - ORGANIZATION/Agents/Agent ID Registry.md` — Master agent registry
  - `02 - ORGANIZATION/Manager Chat Memory/` — Daily chat logs
  - Agent-specific research/verification logs

### 2. GitHub Repository (Version Control & Automation)
- **Repo:** `agent-org-config`
- **Structure:**
  - `playbooks/` — Mirrored playbooks by department
  - `soul-templates/` — SOUL.md templates per agent
  - `agent-profiles/` — Hermes config per agent
  - `.github/workflows/` — CI/CD pipelines
  - `scripts/` — Sync and validation tools
  - `docs/` — Architecture, protocols, contributing

### 3. Hermes Agents (Runtime Execution)
- **Profiles:** `C:/Users/black/AppData/Local/hermes/profiles/<agent-id>/`
- **Config:** `config.yaml`, `mcp_servers.yaml`
- **Memory:** `mnemosyne/data/mnememosyne.db` (per-agent)
- **Skills:** Loaded from `~/.hermes/skills/` + profile skills

### 4. Mnemosyne (Agent Personal Memory)
- **Database:** `profiles/<agent>/mnemosyne/data/mnememosyne.db`
- **Isolation:** Each agent owns its namespace
- **CLI:** `mnemosyne store/recall/update` (subagents use CLI)

### 5. Automation Layer (n8n + GitHub Actions)
- **GitHub Actions:** Validation, sync triggers
- **n8n Workflows:** Scheduled bidirectional sync
- **Monitoring:** Drift detection, alerting

## Data Flow

### Playbook Updates
```
Agent Research → Vault Playbook → vault-to-github.py → GitHub → CI Validate → 
github-to-vault.py → Vault (verified) → Agent Reload
```

### SOUL.md Updates
```
CEO Consent → Orchestrator updates SOUL.md → Vault sync → GitHub sync → 
Agent Profile updated → Agent reloads identity
```

### Mnemosyne Persistence
```
Agent Task Complete → Agent CLI: mnemosyne store → Agent DB → 
Weekly check: mnemosyne-sync-check.py → Drift Alert if >24h
```

## Validation Gates

| Gate | When | What |
|------|------|------|
| Frontmatter | PR, Sync | Required fields, types, enums |
| Structure | PR, Sync | Required sections, content depth |
| SOUL.md | PR, Sync | Required sections, format |
| Mnemosyne | Weekly | Playbook vs memory freshness |
| Sync | Auto | Bidirectional consistency |

## Security

- **GitHub Token:** Stored in GitHub Actions secrets / n8n credentials
- **Agent Profiles:** Local only, not in Git
- **Mnemosyne:** Per-agent isolation, no cross-access
- **Vault:** Local filesystem, Obsidian sync optional

## Scaling Considerations

- **Playbook count:** 44 → 100+ (script handles dynamically)
- **Agent count:** 46 → 100+ (registry drives discovery)
- **Sync frequency:** Daily → Hourly (n8n adjustable)
- **Validation:** Parallel execution (GitHub Actions matrix)

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Vault write fails | Read-back verify | Retry + alert |
| GitHub push fails | Actions status | Manual retry |
| Validation false positive | Manual review | Adjust rules |
| Mnemosyne drift | Weekly check | Agent self-fix |
| n8n down | Workflow status | Manual sync scripts |