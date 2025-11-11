#!/usr/bin/env python3
"""
Clean up app.js by removing console.log statements and unused code
while preserving functionality.
"""

import re

def clean_js_file(input_file: str, output_file: str) -> None:
    """Remove console.log statements and clean up code."""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    cleaned_lines = []
    skip_next = False
    
    for i, line in enumerate(lines):
        # Skip console.log lines but preserve fetch chains
        if 'console.log' in line:
            # Check if this is part of a fetch chain
            if 'fetch(' in line or '.then(' in line or 'return' in line:
                # Remove only the console.log part
                line = re.sub(r'console\.log\([^)]*\);\s*', '', line)
                cleaned_lines.append(line)
            else:
                # Skip standalone console.log lines
                continue
        else:
            cleaned_lines.append(line)
    
    # Write cleaned content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)
    
    print(f"Cleaned {len(lines)} lines down to {len(cleaned_lines)} lines")
    print(f"Removed {len(lines) - len(cleaned_lines)} lines")

if __name__ == '__main__':
    clean_js_file('app.js', 'app_cleaned.js')

