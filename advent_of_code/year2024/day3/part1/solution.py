"""Solution for Mull It Over puzzle - calc sum of valid mul() operations."""
import re
import sys
from typing import List, Match, Optional

def sum_valid_mul_operations(text: str) -> int:
    """
    Process a text string and sum the results of all valid mul() operations.
    
    Args:
        text: Input string with mul operations mixed with corrupted data
        
    Returns:
        Sum of all valid multiplication results
    """
    # RegEx to match mul(X,Y) where X and Y are 1-3 digit numbers
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    total = 0
    
    # Find all matches in the text
    for match in re.finditer(pattern, text):
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        total += num1 * num2
        
    return total

def solution() -> int:
    """
    Read input from stdin and return solution.
    
    Returns:
        Integer result representing sum of all valid multiplication results
    """
    # Read all input lines and join them into a single string
    content = ''.join(sys.stdin.readlines())
    return sum_valid_mul_operations(content)

if __name__ == "__main__":
    print(solution())