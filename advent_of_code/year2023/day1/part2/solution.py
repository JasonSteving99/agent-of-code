"""Implementation for Advent of Code 2023 Day 1: Trebuchet."""
from sys import stdin
from typing import List


def get_calibration_value(line: str) -> str:
    """Extract calibration value from input line by finding first and last digits."""
    # Store only digits from the line
    digits = [char for char in line if char.isdigit()]
    
    # If there are any digits, take first and last
    if digits:
        return digits[0] + digits[-1]
    
    # Return '00' if no digits found (though this shouldn't happen per problem spec)
    return '00'


def solution() -> int:
    """
    Read calibration document from stdin and return sum of calibration values.
    
    Returns:
        int: Sum of all calibration values in the document
    """
    # Read all lines from stdin
    lines: List[str] = [line.strip() for line in stdin.readlines()]
    
    # Get calibration value for each line and convert to integer
    calibration_values: List[int] = [
        int(get_calibration_value(line)) for line in lines
    ]
    
    # Return sum of all calibration values
    return sum(calibration_values)