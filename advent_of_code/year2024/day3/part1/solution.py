from typing import Optional
import re


def sum_of_multiplications(input_str: str) -> int:
    """
    Extracts and sums up the results of all valid multiplication instructions from a given input string.
    Each valid instruction must be in the format mul(X,Y) where X and Y are 1-3 digit numbers.
    
    Args:
        input_str: A string containing potential multiplication instructions mixed with corrupted data
        
    Returns:
        The sum of all valid multiplication results
    """
    # Define regex pattern for valid mul expressions
    # Matches mul( followed by 1-3 digits, comma, 1-3 digits, and closing )
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all matches in the input string
    matches = re.finditer(pattern, input_str)
    
    total = 0
    for match in matches:
        # Extract the numbers from each valid mul instruction
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        
        # Multiply the numbers and add to total
        total += num1 * num2
    
    return total


def solution() -> int:
    """
    Reads input from stdin and returns the sum of all valid multiplication results.
    """
    # Read all input as a single string
    input_data = input().strip()
    return sum_of_multiplications(input_data)