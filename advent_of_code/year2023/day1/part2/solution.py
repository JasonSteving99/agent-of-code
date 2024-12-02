"""
Solution for Advent of Code coding problem - day 1.
"""
from typing import Dict, List, Tuple
import sys

def extract_numbers_with_words(line: str) -> List[str]:
    """Extract numbers including spelled out words from a line."""
    numbers_map: Dict[str, str] = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    positions: List[Tuple[int, str]] = []
    # Find positions of numeric digits
    for i, char in enumerate(line):
        if char.isdigit():
            positions.append((i, char))
    
    # Find positions of spelled out numbers
    for word, digit in numbers_map.items():
        index = -1
        while True:
            index = line.find(word, index + 1)
            if index == -1:
                break
            positions.append((index, digit))
    
    # Sort by position and extract just the digits
    positions.sort(key=lambda x: x[0])
    return [pos[1] for pos in positions]

def sum_calibration_values(input_data: str) -> str:
    """Calculate the sum of calibration values from the input string."""
    total = 0
    for line in input_data.strip().split('\n'):
        if not line:
            continue
            
        digits = extract_numbers_with_words(line)
        if digits:
            # Form a two-digit number using first and last digit
            value = int(digits[0] + digits[-1])
            total += value
    
    return str(total)

def solution() -> str:
    """Read from stdin and return the solution."""
    return sum_calibration_values(sys.stdin.read())

if __name__ == "__main__":
    print(solution())