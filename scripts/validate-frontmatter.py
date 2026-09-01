#!/usr/bin/env python3
"""
Validate YAML frontmatter in Markdown files.
Ensures required fields exist and have correct types.
"""

import os
import sys
import yaml
import argparse
from pathlib import Path
from typing import Dict, List, Any, Optional

PLAYBOOK_REQUIRED = ['type', 'status', 'tags', 'maintained_by']
SOUL_REQUIRED = ['type', 'status', 'tags', 'maintained_by', 'agent_id', 'role', 'department']

def validate_frontmatter(filepath: Path, required_fields: List[str]) -> List[str]:
    """Validate a single file's frontmatter. Returns list of errors."""
    errors = []
    
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return [f"Failed to read: {e}"]
    
    if not content.startswith('---'):
        return [f"No frontmatter delimiter (---) at start"]
    
    try:
        # Extract frontmatter between first and second ---
        parts = content.split('---', 2)
        if len(parts) < 3:
            return [f"Incomplete frontmatter (need opening and closing ---)"]
        
        fm_text = parts[1]
        fm = yaml.safe_load(fm_text)
        
        if fm is None:
            return [f"Empty frontmatter"]
        
        # Check required fields
        for field in required_fields:
            if field not in fm:
                errors.append(f"Missing required field: {field}")
            elif isinstance(fm[field], str) and fm[field].startswith('<') and fm[field].endswith('>'):
                # Placeholder value in template - skip validation error
                pass
        
        # Type checks
        if 'tags' in fm and not isinstance(fm['tags'], list):
            errors.append(f"'tags' must be a list")
        
        if 'status' in fm and fm['status'] not in ['active', 'draft', 'archived', 'deprecated']:
            errors.append(f"'status' must be one of: active, draft, archived, deprecated")
            
    except yaml.YAMLError as e:
        errors.append(f"YAML parse error: {e}")
    except Exception as e:
        errors.append(f"Validation error: {e}")
    
    return errors

def main():
    parser = argparse.ArgumentParser(description='Validate frontmatter in Markdown files')
    parser.add_argument('--dir', action='append', required=True, help='Directory to scan')
    parser.add_argument('--type', choices=['playbook', 'soul', 'auto'], default='auto', help='Validation type')
    args = parser.parse_args()
    
    all_errors = {}
    file_count = 0
    
    for dir_path in args.dir:
        dir_path = Path(dir_path)
        if not dir_path.exists():
            print(f"Directory not found: {dir_path}")
            continue
        
        for md_file in dir_path.rglob('*.md'):
            file_count += 1
            
            if args.type == 'auto':
                if 'playbooks' in str(md_file):
                    required = PLAYBOOK_REQUIRED
                elif 'soul' in str(md_file) or 'agent-profiles' in str(md_file):
                    required = SOUL_REQUIRED
                else:
                    required = []
            elif args.type == 'playbook':
                required = PLAYBOOK_REQUIRED
            else:
                required = SOUL_REQUIRED
            
            errors = validate_frontmatter(md_file, required)
            if errors:
                all_errors[str(md_file)] = errors
    
    if all_errors:
        print(f"\n❌ VALIDATION FAILED: {len(all_errors)} of {file_count} files have errors\n")
        for filepath, errors in all_errors.items():
            print(f"  {filepath}")
            for err in errors:
                print(f"    - {err}")
        sys.exit(1)
    else:
        print(f"✅ All {file_count} files passed frontmatter validation")
        sys.exit(0)

if __name__ == '__main__':
    main()