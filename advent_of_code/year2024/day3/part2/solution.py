import sys
from typing import List, Tuple
import re

def calculate_enabled_multiplications(inp: str) -> int:
    """
    Calculate sum of enabled multiplication results from corrupted program memory.
    Takes into account do() and don't() instructions that enable/disable future mul operations.
    
    Args:
        inp: A string containing the corrupted program with mul, do, and don't instructions
        
    Returns:
        Sum of all enabled multiplication results
    """
    result = 0
    # Multiplications enabled by default
    enabled = True  
    
    # Match both control flow (do/don't) and multiplication instructions
    pattern = r'(?:do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\))'
    matches = re.finditer(pattern, inp)
    
    for match in matches:
        instruction = match.group()
        
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif instruction.startswith("mul("):
            # Only process multiplication if currently enabled
            if enabled:
                # Extract numbers from mul instruction
                nums = re.findall(r'\d+', instruction)
                if len(nums) == 2:  # Ensure valid mul instruction
                    x, y = int(nums[0]), int(nums[1])
                    result += x * y
    
    return result

def solution() -> int:
    """Read from stdin and return solution."""
    return calculate_enabled_multiplications(sys.stdin.read().strip())

if __name__ == "__main__":
    print(solution())