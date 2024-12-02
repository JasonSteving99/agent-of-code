from sys import stdin
from typing import List

def get_calibration_value(line: str) -> str:
    """
    Extract the first and last digits from a string and combine them into a two-digit number.
    
    Args:
        line: Input string that may contain digits mixed with other characters
    
    Returns:
        String representation of the two-digit number formed by the first and last digits

    Raises:
        ValueError: If the input string contains no digits
    """
    digits = [char for char in line if char.isdigit()]
    if not digits:
        raise ValueError("No digits found in the input string.")

    return digits[0] + digits[-1]


def solution() -> int:
    """
    Read calibration document from stdin, process each line to get calibration values,
    and return their sum.
    
    Returns:
        Sum of all calibration values in the document
    """
    lines = [line.strip() for line in stdin.readlines()]
    calibration_values = [int(get_calibration_value(line)) for line in lines]

    return sum(calibration_values)

if __name__ == "__main__":
    result = solution()
    print(result)