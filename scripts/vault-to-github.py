#!/usr/bin/env python3
"""
Sync Obsidian Vault playbooks to GitHub repo.
Extracts playbooks from Vault and writes to GitHub structure.
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
from datetime import datetime
import frontmatter
import yaml

VAULT_PLAYBOOKS = Path("C:/Users/black/Documents/Obsidian Vault/02 - ORGANIZATION/Agents/Playbooks")
GITHUB_PLAYBOOKS = Path("C:/Users/black/Documents/Obsidian Vault/agent-org-config/playbooks")

DEPT_MAP = {
    'Technical': 'TECHNICAL',
    'Sales': 'SALES', 
    'Marketing': 'MARKETING',
    'Operations': 'OPERATIONS'
}

def get_department(filepath: Path) -> str:
    """Determine department from file path or frontmatter."""
    try:
        post = frontmatter.load(filepath)
        dept = post.metadata.get('department', '')
        if dept in DEPT_MAP:
            return DEPT_MAP[dept]
    except:
        pass
    
    # Fallback: guess from path
    parts = str(filepath).lower()
    if 'technical' in parts:
        return 'TECHNICAL'
    elif 'sales' in parts:
        return 'SALES'
    elif 'marketing' in parts:
        return 'MARKETING'
    elif 'operations' in parts or 'ops' in parts:
        return 'OPERATIONS'
    
    return 'TECHNICAL'  # default

def sync_file(src: Path, dry_run: bool = False) -> bool:
    """Sync a single playbook file. Returns True if changes made."""
    dept = get_department(src)
    dest_dir = GITHUB_PLAYBOOKS / dept
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name
    
    # Read source
    src_content = src.read_text(encoding='utf-8')
    
    # Check if destination exists and differs
    if dest.exists():
        dest_content = dest.read_text(encoding='utf-8')
        if src_content == dest_content:
            return False  # No changes
    
    if dry_run:
        print(f"[DRY RUN] Would sync: {src.name} → {dept}/")
        return True
    
    # Write to destination
    dest.write_text(src_content, encoding='utf-8')
    print(f"Synced: {src.name} → {dept}/")
    return True

def main():
    parser = argparse.ArgumentParser(description='Sync Vault playbooks to GitHub')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be synced')
    args = parser.parse_args()
    
    if not VAULT_PLAYBOOKS.exists():
        print(f"❌ Vault playbooks not found: {VAULT_PLAYBOOKS}")
        sys.exit(1)
    
    changes = 0
    total = 0
    
    for md_file in VAULT_PLAYBOOKS.rglob('*.md'):
        if md_file.name in ['README.md', 'INDEX.md', 'Agent ID Registry.md']:
            continue
        total += 1
        if sync_file(md_file, args.dry_run):
            changes += 1
    
    # Also sync SOUL templates from agent profiles
    vault_agents = Path("C:/Users/black/AppData/Local/hermes/profiles")
    if vault_agents.exists():
        for agent_dir in vault_agents.iterdir():
            if agent_dir.is_dir() and agent_dir.name != 'orchestrator-ai':
                soul_file = agent_dir / 'SOUL.md'
                if soul_file.exists():
                    dest_dir = Path("C:/Users/black/Documents/Obsidian Vault/agent-org-config/soul-templates")
                    dest_dir.mkdir(parents=True, exist_ok=True)
                    dest = dest_dir / f"{agent_dir.name}.md"
                    
                    src_content = soul_file.read_text(encoding='utf-8')
                    if not dest.exists() or dest.read_text(encoding='utf-8') != src_content:
                        if not args.dry_run:
                            dest.write_text(src_content, encoding='utf-8')
                            print(f"Synced SOUL: {agent_dir.name}.md")
                        else:
                            print(f"[DRY RUN] Would sync SOUL: {agent_dir.name}.md")
                        changes += 1
                    total += 1
    
    print(f"\n{'DRY RUN: ' if args.dry_run else ''}Total: {total}, Changes: {changes}")
    
    # Output for GitHub Actions
    if os.environ.get('GITHUB_ACTIONS'):
        print(f"changes={'true' if changes > 0 else 'false'}")
        with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
            f.write(f"changes={'true' if changes > 0 else 'false'}\n")

if __name__ == '__main__':
    main()