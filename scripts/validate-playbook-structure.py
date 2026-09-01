#!/usr/bin/env python3
"""
Validate Playbook structure - check for required sections and content.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Dict

REQUIRED_SECTIONS = [
    '## Identity',
    '## Mission',
    '## Responsibilities',
    '## Skills & Tools',
    '## Operating Standards',
    '## Quality Gates',
    '## Persistence Protocol',
    '## Communication Style',
    '## Escalation Path',
    '## Live Web Refresh'
]

def validate_structure(filepath: Path) -> List[str]:
    """Validate a playbook has all required sections."""
    errors = []
    warnings = []
    
    try:
        content = filepath.read_text(encoding='utf-8')
    except Exception as e:
        return [f"Failed to read: {e}"]
    
    # Check for required sections
    for section in REQUIRED_SECTIONS:
        if section not in content:
            errors.append(f"Missing required section: {section}")
    
    # Check for Live Web Refresh with date
    if '## Live Web Refresh' in content:
        import re
        date_match = re.search(r'Live Web Refresh.*?(\d{4}-\d{2}-\d{2})', content)
        if not date_match:
            warnings.append("Live Web Refresh section found but no date (YYYY-MM-DD)")
        else:
            # Check if date is recent (within 90 days)
            from datetime import datetime, timedelta
            try:
                refresh_date = datetime.strptime(date_match.group(1), '%Y-%m-%d')
                if datetime.now() - refresh_date > timedelta(days=90):
                    warnings.append(f"Live Web Refresh date is >90 days old: {date_match.group(1)}")
            except:
                pass
    
    # Check word count (should be substantial)
    word_count = len(content.split())
    if word_count < 500:
        warnings.append(f"Playbook is very short ({word_count} words) - may be incomplete")
    
    # Return errors + warnings
    result = errors
    if warnings:
        result.extend([f"WARNING: {w}" for w in warnings])
    
    return result

def main():
    parser = argparse.ArgumentParser(description='Validate Playbook structure')
    parser.add_argument('--dir', action='append', required=True, help='Directory to scan')
    args = parser.parse_args()
    
    all_errors = {}
    file_count = 0
    
    for dir_path in args.dir:
        dir_path = Path(dir_path)
        if not dir_path.exists():
            print(f"Directory not found: {dir_path}")
            continue
        
        for md_file in dir_path.rglob('*.md'):
            # Skip non-playbook files
            if 'README' in md_file.name or 'INDEX' in md_file.name:
                continue
            file_count += 1
            
            errors = validate_structure(md_file)
            if errors:
                all_errors[str(md_file)] = errors
    
    if all_errors:
        print(f"\n❌ STRUCTURE VALIDATION: {len(all_errors)} of {file_count} files have issues\n")
        for filepath, errors in all_errors.items():
            print(f"  {filepath}")
            for err in errors:
                print(f"    - {err}")
        sys.exit(1)
    else:
        print(f"✅ All {file_count} playbooks passed structure validation")
        sys.exit(0)

if __name__ == '__main__':
    main()