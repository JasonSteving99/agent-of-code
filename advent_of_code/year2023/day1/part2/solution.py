import sys
from typing import List


def get_calibration_value(line: str) -> str:
    """Extract the first and last digit from a string and combine them into a two-digit string.
    
    Args:
        line: A string that contains at least one digit.
    
    Returns:
        A string of exactly two digits, representing the calibration value.
        The first digit is the first digit found in the input string,
        and the last digit is the last digit found in the input string.
    """
    # Find all digits in the string
    digits = [c for c in line if c.isdigit()]
    
    # Return the first and last digit concatenated
    # If there's only one digit, use it twice
    return digits[0] + digits[-1]


def solution() -> int:
    """Read calibration document from stdin and calculate sum of calibration values.
    
    Returns:
        The sum of all calibration values from the input document.
    """
    # Read all lines from stdin
    lines: List[str] = [line.strip() for line in sys.stdin]
    
    # Calculate calibration values for each line and sum them
    total = sum(int(get_calibration_value(line)) for line in lines)
    
    return total


if __name__ == "__main__":
    print(solution())