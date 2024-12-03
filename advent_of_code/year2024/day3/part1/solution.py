import re
import sys
from typing import Optional, List

def sum_of_multiplications(text: str) -> int:
    """
    Parse a string containing mul(X,Y) instructions and return the sum of all valid multiplications.
    
    Args:
        text: String containing potentially corrupted text with mul(X,Y) instructions
        
    Returns:
        Sum of all valid multiplications found in the text
    """
    # Pattern matches mul(X,Y) where X and Y are 1-3 digit numbers
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all valid mul instructions
    matches = re.finditer(pattern, text)
    
    # Calculate sum of multiplications
    total = 0
    for match in matches:
        x = int(match.group(1))
        y = int(match.group(2))
        total += x * y
        
    return total

def solution() -> int:
    """
    Read input from stdin and return the sum of all valid multiplications.
    """
    # Read all input from stdin
    text = sys.stdin.read()
    return sum_of_multiplications(text)

if __name__ == '__main__':
    print(solution())