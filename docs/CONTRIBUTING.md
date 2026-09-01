# Contributing to Agent Organization Config

## Welcome

This repository manages the configuration, playbooks, and automation for our multi-agent Hermes organization. All agents, playbooks, and operational protocols are version-controlled here.

## How to Contribute

### 1. Playbook Updates

**For agents updating their own playbooks:**
1. Edit your playbook in the Obsidian Vault at `02 - ORGANIZATION/Agents/Playbooks/<DEPT>/`
2. Run local sync: `python scripts/vault-to-github.py`
3. Create PR with changes
4. CI validates frontmatter + structure
5. Merge triggers auto-sync back to Vault

**For Manager/Orchestrator updating playbooks:**
1. Create branch: `git checkout -b playbook/<agent-id>-<change>`
2. Edit files in `playbooks/<DEPT>/`
3. Run validation locally: `python scripts/validate-frontmatter.py --dir playbooks --type playbook`
4. Push and create PR
5. Auto-merge on CI pass

### 2. SOUL.md Updates

**Requires CEO consent for protected writes.**

1. Orchestrator updates SOUL.md in agent profile (with consent)
2. Sync to GitHub: `python scripts/vault-to-github.py` (copies to `soul-templates/`)
3. Create PR
4. CI validates SOUL.md structure
5. Merge triggers sync to all agent profiles

### 3. Agent Profile Config

1. Edit `agent-profiles/<agent-id>/config.yaml` or `mcp_servers.yaml`
2. Validate YAML syntax
3. Create PR
3. On merge: Deploy to agent Hermes profile (automation handles)

### 4. Scripts & Automation

1. Edit scripts in `scripts/`
2. Test locally with `--dry-run`
3. Create PR
4. CI runs validation

### 5. Documentation

1. Edit docs in `docs/`
2. Create PR
3. No validation gates (markdown only)

## Validation Requirements

All PRs must pass:
- ✅ `validate-playbooks.yml` (if playbooks changed)
- ✅ `validate-soul-md.yml` (if SOUL.md changed)
- ✅ YAML syntax for config files

## Branch Protection

- `main` branch: Protected
- Required reviews: 1 (Manager/Orchestrator)
- Required checks: All CI workflows
- No force push

## Commit Message Convention

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New playbook/feature
- `fix`: Bug fix in playbook/script
- `docs`: Documentation only
- `chore`: Sync, maintenance, deps
- `refactor`: Restructure without behavior change

**Scopes:**
- `playbook`: Playbook content
- `soul`: SOUL.md templates
- `config`: Agent profiles
- `script`: Sync/validation scripts
- `workflow`: GitHub Actions
- `docs`: Documentation

**Examples:**
```
feat(playbook): add DSPM verification to microsoft365-expert playbook
fix(script): handle missing frontmatter in vault-to-github
chore(sync): daily vault-to-github sync
docs(arch): update architecture diagram
```

## Local Development

```bash
# Clone
git clone https://github.com/your-org/agent-org-config.git
cd agent-org-config

# Install deps
pip install pyyaml frontmatter

# Test sync (dry run)
python scripts/vault-to-github.py --dry-run
python scripts/github-to-vault.py --dry-run

# Validate
python scripts/validate-frontmatter.py --dir playbooks --dir soul-templates
python scripts/validate-playbook-structure.py --dir playbooks
python scripts/validate-soul-md.py --dir soul-templates --dir agent-profiles

# Mnemosyne check
python scripts/mnemosyne-sync-check.py
```

## Sync Protocol

See [SYNC_PROTOCOL.md](SYNC_PROTOCOL.md) for detailed bidirectional sync rules.

## Architecture

See [ARCHITECTURE.md](ARCHITECTURE.md) for system overview.

## Questions?

Contact the Orchestrator AI (Manager) or CEO.