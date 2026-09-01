#!/usr/bin/env python3
"""
Sync GitHub repo playbooks to Obsidian Vault.
Applies changes from GitHub to Vault structure.
"""

import os
import sys
import argparse
from pathlib import Path
import frontmatter

GITHUB_PLAYBOOKS = Path("C:/Users/black/Documents/Obsidian Vault/agent-org-config/playbooks")
VAULT_PLAYBOOKS = Path("C:/Users/black/Documents/Obsidian Vault/02 - ORGANIZATION/Agents/Playbooks")

GITHUB_SOUL = Path("C:/Users/black/Documents/Obsidian Vault/agent-org-config/soul-templates")
VAULT_AGENTS = Path("C:/Users/black/AppData/Local/hermes/profiles")

DEPT_MAP_REVERSE = {
    'TECHNICAL': 'Technical',
    'SALES': 'Sales',
    'MARKETING': 'Marketing',
    'OPERATIONS': 'Operations'
}

def get_vault_dept(filepath: Path) -> str:
    """Determine Vault department folder from GitHub structure."""
    # Parent directory name
    parent = filepath.parent.name
    if parent in DEPT_MAP_REVERSE:
        return DEPT_MAP_REVERSE[parent]
    
    # Fallback: check frontmatter
    try:
        post = frontmatter.load(filepath)
        dept = post.metadata.get('department', '')
        if dept in DEPT_MAP_REVERSE.values():
            return dept
    except:
        pass
    
    return 'Technical'  # default

def sync_playbooks(dry_run: bool = False) -> int:
    """Sync playbooks from GitHub to Vault."""
    changes = 0
    
    if not GITHUB_PLAYBOOKS.exists():
        print(f"❌ GitHub playbooks not found: {GITHUB_PLAYBOOKS}")
        return 0
    
    for md_file in GITHUB_PLAYBOOKS.rglob('*.md'):
        if md_file.name in ['README.md', 'INDEX.md']:
            continue
        
        dept = get_vault_dept(md_file)
        dest_dir = VAULT_PLAYBOOKS / dept
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / md_file.name
        
        src_content = md_file.read_text(encoding='utf-8')
        
        if dest.exists():
            dest_content = dest.read_text(encoding='utf-8')
            if src_content == dest_content:
                continue  # No changes
        
        if dry_run:
            print(f"[DRY RUN] Would sync: {md_file.name} → {dept}/")
        else:
            dest.write_text(src_content, encoding='utf-8')
            print(f"Synced: {md_file.name} → {dept}/")
        changes += 1
    
    return changes

def sync_soul_templates(dry_run: bool = False) -> int:
    """Sync SOUL templates from GitHub to agent profiles."""
    changes = 0
    
    if not GITHUB_SOUL.exists():
        return 0
    
    for md_file in GITHUB_SOUL.rglob('*.md'):
        if md_file.name in ['README.md', 'INDEX.md']:
            continue
        
        # Agent ID from filename (without .md)
        agent_id = md_file.stem
        dest_dir = VAULT_AGENTS / agent_id
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / 'SOUL.md'
        
        src_content = md_file.read_text(encoding='utf-8')
        
        if dest.exists():
            dest_content = dest.read_text(encoding='utf-8')
            if src_content == dest_content:
                continue
        
        if dry_run:
            print(f"[DRY RUN] Would sync SOUL: {agent_id}")
        else:
            dest.write_text(src_content, encoding='utf-8')
            print(f"Synced SOUL: {agent_id}")
        changes += 1
    
    return changes

def main():
    parser = argparse.ArgumentParser(description='Sync GitHub to Vault')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be synced')
    args = parser.parse_args()
    
    total_changes = 0
    
    print("Syncing playbooks...")
    total_changes += sync_playbooks(args.dry_run)
    
    print("Syncing SOUL templates...")
    total_changes += sync_soul_templates(args.dry_run)
    
    print(f"\n{'DRY RUN: ' if args.dry_run else ''}Total changes: {total_changes}")
    
    if total_changes == 0:
        print("✅ Already in sync")

if __name__ == '__main__':
    main()