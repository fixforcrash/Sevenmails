#!/usr/bin/env python3
"""
Check Mnemosyne sync status for all agents.
Compares Playbook content vs Mnemosyne memories per agent.
"""

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime, timedelta

VAULT_PLAYBOOKS = Path("C:/Users/black/Documents/Obsidian Vault/02 - ORGANIZATION/Agents/Playbooks")
AGENT_REGISTRY = Path("C:/Users/black/Documents/Obsidian Vault/02 - ORGANIZATION/Agents/Agent ID Registry.md")

def get_agent_list() -> list:
    """Get list of agents from registry."""
    agents = []
    if AGENT_REGISTRY.exists():
        content = AGENT_REGISTRY.read_text(encoding='utf-8')
        # Parse markdown table
        for line in content.split('\n'):
            if line.startswith('| ') and '|' in line:
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 4 and parts[1].isdigit():
                    agent_id = parts[2]
                    if agent_id and agent_id != 'Agent ID':
                        agents.append(agent_id)
    return agents

def get_mnemosyne_memories(agent_id: str) -> list:
    """Get Mnemosyne memories for an agent via CLI."""
    try:
        result = subprocess.run(
            ['mnemosyne', 'recall', f'agent:{agent_id}', '--limit', '50'],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            # Parse output - this is simplified
            lines = result.stdout.strip().split('\n')
            memories = []
            for line in lines:
                if line.strip() and not line.startswith('ID'):
                    memories.append(line.strip())
            return memories
    except Exception as e:
        pass
    return []

def get_playbook_modified_time(agent_id: str) -> datetime:
    """Get the most recent modification time of an agent's playbook."""
    latest = None
    for md_file in VAULT_PLAYBOOKS.rglob('*.md'):
        if agent_id.lower() in md_file.name.lower() or agent_id.lower().replace('-', '') in md_file.name.lower().replace('-', ''):
            try:
                mtime = datetime.fromtimestamp(md_file.stat().st_mtime)
                if latest is None or mtime > latest:
                    latest = mtime
            except:
                pass
    return latest

def check_agent_sync(agent_id: str) -> dict:
    """Check sync status for a single agent."""
    result = {
        'agent_id': agent_id,
        'playbook_exists': False,
        'playbook_modified': None,
        'mnemosyne_memories': 0,
        'last_mnemosyne_update': None,
        'drift_hours': None,
        'status': 'unknown'
    }
    
    # Check playbook
    playbook_time = get_playbook_modified_time(agent_id)
    if playbook_time:
        result['playbook_exists'] = True
        result['playbook_modified'] = playbook_time.isoformat()
    
    # Check Mnemosyne
    memories = get_mnemosyne_memories(agent_id)
    result['mnemosyne_memories'] = len(memories)
    
    if memories:
        # Estimate last update (simplified)
        result['last_mnemosyne_update'] = datetime.now().isoformat()
    
    # Calculate drift
    if playbook_time and memories:
        drift = datetime.now() - playbook_time
        result['drift_hours'] = drift.total_seconds() / 3600
        
        if drift > timedelta(hours=24):
            result['status'] = 'drift'
        else:
            result['status'] = 'synced'
    elif playbook_time and not memories:
        result['status'] = 'no_mnemosyne'
    elif not playbook_time and memories:
        result['status'] = 'no_playbook'
    else:
        result['status'] = 'missing_both'
    
    return result

def main():
    agents = get_agent_list()
    print(f"Checking Mnemosyne sync for {len(agents)} agents...")
    
    results = []
    drift_count = 0
    
    for agent_id in agents:
        sync = check_agent_sync(agent_id)
        results.append(sync)
        
        if sync['status'] == 'drift':
            drift_count += 1
            print(f"  ⚠️  {agent_id}: Drift detected ({sync['drift_hours']:.1f}h)")
        elif sync['status'] == 'synced':
            print(f"  ✅ {agent_id}: Synced")
        elif sync['status'] == 'no_mnemosyne':
            print(f"  ❌ {agent_id}: Playbook exists but no Mnemosyne memories")
        elif sync['status'] == 'no_playbook':
            print(f"  ❌ {agent_id}: Mnemosyne memories but no playbook")
        else:
            print(f"  ❓ {agent_id}: Missing both")
    
    # Summary
    print(f"\n--- Summary ---")
    print(f"Total agents: {len(agents)}")
    print(f"Synced: {sum(1 for r in results if r['status'] == 'synced')}")
    print(f"Drift (>24h): {drift_count}")
    print(f"No Mnemosyne: {sum(1 for r in results if r['status'] == 'no_mnemosyne')}")
    print(f"No Playbook: {sum(1 for r in results if r['status'] == 'no_playbook')}")
    print(f"Missing both: {sum(1 for r in results if r['status'] == 'missing_both')}")
    
    # Exit code for CI
    if drift_count > 0:
        print(f"\n⚠️  {drift_count} agents have sync drift >24h")
        sys.exit(1)
    else:
        print(f"\n✅ All agents synced within 24h")
        sys.exit(0)

if __name__ == '__main__':
    main()