#!/usr/bin/env python3
"""
Validate SOUL.md structure - check for required sections and content.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List

REQUIRED_SECTIONS = [
    '## Identity',
    '## Mission',
    '## Responsibilities',
    '## Skills & Tools',
    '## Operating Standards',
    '## Quality Gates',
    '## Persistence Protocol',
    '## Communication Style',
    '## Memory Architecture',
    '## Chat Memory Format',
    '## Escalation Path'
]

def validate_structure(filepath: Path) -> List[str]:
    """Validate a SOUL.md has all required sections."""
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
    
    # Check for Chat Memory Format section (newer requirement)
    if '## Chat Memory Format' not in content:
        errors.append("Missing required section: ## Chat Memory Format")
    
    # Check for Three-Layer Persistence Protocol
    if 'Three-Layer Persistence' not in content and '3-Layer Persistence' not in content:
        warnings.append("Three-Layer Persistence Protocol not explicitly documented")
    
    # Check word count
    word_count = len(content.split())
    if word_count < 300:
        warnings.append(f"SOUL.md is very short ({word_count} words) - may be incomplete")
    
    result = errors
    if warnings:
        result.extend([f"WARNING: {w}" for w in warnings])
    
    return result

def main():
    parser = argparse.ArgumentParser(description='Validate SOUL.md structure')
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
            file_count += 1
            
            errors = validate_structure(md_file)
            if errors:
                all_errors[str(md_file)] = errors
    
    if all_errors:
        print(f"\n❌ SOUL.MD VALIDATION: {len(all_errors)} of {file_count} files have issues\n")
        for filepath, errors in all_errors.items():
            print(f"  {filepath}")
            for err in errors:
                print(f"    - {err}")
        sys.exit(1)
    else:
        print(f"✅ All {file_count} SOUL.md files passed structure validation")
        sys.exit(0)

if __name__ == '__main__':
    main()