"""
Advent of Code 2023 - Day 1 Solution
Parse calibration values from strings by extracting first and last digits.
"""
import sys
from typing import List


def solution() -> int:
    """Read input from stdin and return sum of calibration values."""
    lines = [line.strip() for line in sys.stdin]
    return sum(int(get_calibration_value(line)) for line in lines)


def get_calibration_value(text: str) -> str:
    """Extract first and last digit from a string to form a two-digit number.
    
    Args:
        text: Input string containing at least one digit
    
    Returns:
        Two digit string number formed by first and last digits in input
        
    Raises:
        ValueError: If the input string contains no digits.
        
    Examples:
        >>> get_calibration_value("1abc2")
        '12'
        >>> get_calibration_value("pqr3stu8vwx")
        '38'
        >>> get_calibration_value("a1b2c3d4e5f")
        '15'
        >>> get_calibration_value("treb7uchet")
        '77'
    """
    # Extract all digits from the string
    digits = [c for c in text if c.isdigit()]
    
    # Raise ValueError if no digits are found
    if not digits:
        raise ValueError("Input string must contain at least one digit.")

    # Return first and last digit concatenated
    # Since we know input is valid and contains at least one digit,
    # if there's only one digit, use it twice
    if len(digits) == 1:
        return digits[0] * 2

    return digits[0] + digits[-1]


if __name__ == '__main__':
    print(solution())