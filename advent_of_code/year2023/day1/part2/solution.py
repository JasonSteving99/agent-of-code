from sys import stdin
from typing import List

def get_calibration_value(line: str) -> str:
    """
    Extract the first and last digits from a string and combine them into a two-digit number.
    
    Args:
        line: Input string that may contain digits mixed with other characters
    
    Returns:
        String representation of the two-digit number formed by the first and last digits
    """
    # Filter the string to only include digits
    digits = [c for c in line if c.isdigit()]
    
    if not digits:
        return "00"  # Handle case with no digits, though problem suggests this won't occur
        
    # Take first and last digit and combine them
    return digits[0] + digits[-1]

def solution() -> int:
    """
    Read calibration document from stdin, process each line to get calibration values,
    and return their sum.
    
    Returns:
        Sum of all calibration values in the document
    """
    # Read all lines from stdin
    lines = [line.strip() for line in stdin.readlines()]
    
    # Get calibration value for each line and convert to integer
    calibration_values = [int(get_calibration_value(line)) for line in lines]
    
    # Return the sum
    return sum(calibration_values)

if __name__ == "__main__":
    result = solution()
    print(result)