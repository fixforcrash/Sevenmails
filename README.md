# Agent Organization Configuration Repository

Central configuration, playbooks, and automation for the multi-agent Hermes organization.

## Structure

```
agent-org-config/
├── .github/
│   └── workflows/           # GitHub Actions CI/CD
├── playbooks/               # Agent playbooks by department
│   ├── TECHNICAL/
│   ├── SALES/
│   ├── MARKETING/
│   └── OPERATIONS/
├── soul-templates/          # Base SOUL.md templates per role
├── agent-profiles/          # Hermes agent configurations
│   └── <agent-id>/
│       ├── config.yaml
│       └── mcp_servers.yaml
├── scripts/                 # Sync and validation scripts
├── docs/                    # Documentation
├── .gitignore
└── LICENSE
```

## Quick Start

```bash
# Sync Vault → GitHub
python scripts/vault-to-github.py

# Sync GitHub → Vault
python scripts/github-to-vault.py

# Validate all frontmatter
python scripts/validate-frontmatter.py

# Check Mnemosyne sync
python scripts/mnemosyne-sync-check.py
```

## GitHub Actions Workflows

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `validate-playbooks.yml` | PR to main | Validate playbook frontmatter + structure |
| `validate-soul-md.yml` | PR to main | Validate SOUL.md structure |
| `sync-vault-to-github.yml` | Manual (workflow_dispatch) | Sync Obsidian Vault → GitHub |
| `sync-github-to-vault.yml` | Push to main | Sync GitHub → Obsidian Vault |

## Automation (n8n)

| Workflow | Schedule/Trigger | Purpose |
|----------|------------------|---------|
| Vault → GitHub Sync | Daily 02:00 | Automated sync |
| GitHub → Vault Sync | PR merged to main | Automated sync |
| Mnemosyne Drift Check | Weekly | Alert on sync drift |

## Sync Protocol

See [SYNC_PROTOCOL.md](docs/SYNC_PROTOCOL.md) for detailed bidirectional sync rules.

## License

MIT