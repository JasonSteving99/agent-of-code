from typing import List, Match, Optional
import re

def calculate_enabled_multiplications(input_str: str) -> int:
    # Initialize the total and enabled state (True by default)
    total = 0
    enabled = True
    
    # Pattern for valid mul instructions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    # Pattern for do/don't instructions
    do_pattern = r'do\(\)'
    dont_pattern = r"don't\(\)"
    
    # Process the string character by character to handle instructions in order
    current_pos = 0
    while current_pos < len(input_str):
        # Look for do/don't instructions first as they affect future operations
        do_match = re.match(do_pattern, input_str[current_pos:])
        if do_match:
            enabled = True
            current_pos += len(do_match.group(0))
            continue

        dont_match = re.match(dont_pattern, input_str[current_pos:])
        if dont_match:
            enabled = False
            current_pos += len(dont_match.group(0))
            continue

        # Look for mul instructions
        mul_match = re.match(mul_pattern, input_str[current_pos:])
        if mul_match:
            # Only process multiplication if enabled
            if enabled:
                num1 = int(mul_match.group(1))
                num2 = int(mul_match.group(2))
                total += num1 * num2
            current_pos += len(mul_match.group(0))
        else:
            current_pos += 1

    return total

def solution() -> int:
    # Read input from stdin
    return calculate_enabled_multiplications(input())