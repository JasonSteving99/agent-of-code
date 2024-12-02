#!/usr/bin/env python3.12
"""Solution to Advent of Code calibration value extraction problem."""

import sys
from typing import TextIO


def extract_calibration_value(line: str) -> str:
    """Extract the calibration value from a line of text.
    
    The calibration value is formed by combining the first and last digits 
    (in that order) to form a single two-digit number.
    
    Args:
        line: A line of text containing at least one digit
        
    Returns:
        A string containing the two-digit calibration value
        
    Examples:
        >>> extract_calibration_value("1abc2")
        '12'
        >>> extract_calibration_value("pqr3stu8vwx")
        '38'
        >>> extract_calibration_value("a1b2c3d4e5f")
        '15'
        >>> extract_calibration_value("treb7uchet")
        '77'
    """
    # Extract all digits from the line
    digits = [char for char in line if char.isdigit()]
    
    # Return the first and last digits concatenated
    # Note: When there's only one digit, use it for both first and last
    return digits[0] + digits[-1]


def solve(input_stream: TextIO = sys.stdin) -> int:
    """Calculate sum of calibration values from input stream.
    
    Args:
        input_stream: Text stream containing lines of calibration data
        
    Returns:
        Sum of all calibration values
    """
    total = 0
    for line in input_stream:
        # Strip whitespace and get calibration value
        cal_value = extract_calibration_value(line.strip())
        # Convert to integer and add to total
        total += int(cal_value)
    return total


def solution() -> int:
    """Solve the puzzle by reading from stdin."""
    return solve()


if __name__ == "__main__":
    print(solution())  # Only print if run directly