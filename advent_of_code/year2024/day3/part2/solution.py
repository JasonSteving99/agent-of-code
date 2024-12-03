"""Solution for Part 2 of Mull It Over problem - keeping track of enabled multiplications."""
import re
from typing import Optional, Match


def calculate_enabled_multiplications(memory: str) -> int:
    """Calculate sum of enabled multiplication results from corrupted memory.
    
    Args:
        memory: String containing corrupted memory with mul/do/don't instructions
    
    Returns:
        Sum of all enabled multiplication results
    """
    total = 0
    enabled = True  # Multiplications are enabled by default
    
    # Process memory left to right
    pos = 0
    while pos < len(memory):
        # Look for mul instructions
        mul_match = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', memory[pos:])
        # Look for do/don't instructions
        do_match = re.match(r'do\(\)', memory[pos:])
        dont_match = re.match(r"don't\(\)", memory[pos:])
        
        # Handle each type of instruction
        if do_match:
            enabled = True
            pos += do_match.end()
        elif dont_match:
            enabled = False
            pos += dont_match.end()
        elif mul_match and enabled:
            # Only process multiplication if currently enabled
            num1 = int(mul_match.group(1))
            num2 = int(mul_match.group(2))
            total += num1 * num2
            pos += mul_match.end()
        else:
            # Skip any invalid/corrupted characters
            pos += 1
            
    return total


def solution() -> int:
    """Read input from stdin and solve the problem."""
    import sys
    memory = sys.stdin.read().strip()
    return calculate_enabled_multiplications(memory)


if __name__ == "__main__":
    print(solution())