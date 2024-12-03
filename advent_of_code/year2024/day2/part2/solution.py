"""Solution handling part 2 of this problem."""
from typing import List
import sys

def is_valid_difference(a: int, b: int) -> bool:
    """Check if difference between adjacent numbers is valid."""
    diff = abs(a - b)
    return diff >= 1 and diff <= 3

def is_sequence_safe(numbers: List[int]) -> bool:
    """Check if a sequence of numbers is safe according to original rules."""
    if len(numbers) < 2:
        return True

    # Check if it's increasing or decreasing
    is_increasing = numbers[1] > numbers[0]
    
    for i in range(len(numbers) - 1):
        # Check if direction is consistent
        curr_increasing = numbers[i + 1] > numbers[i]
        if curr_increasing != is_increasing:
            return False
        
        # Check if difference is valid
        if not is_valid_difference(numbers[i], numbers[i + 1]):
            return False
            
    return True

def is_report_safe_with_dampener(report: str) -> str:
    """
    Check if a report is safe with Problem Dampener.
    A report is safe if it's already safe or becomes safe by removing one number.
    """
    # Parse the numbers from the report
    numbers = [int(x) for x in report.strip().split()]
    
    # First check if report is already safe
    if is_sequence_safe(numbers):
        return "safe"
        
    # Try removing each number one at a time
    for i in range(len(numbers)):
        # Create new list without the current number
        test_numbers = numbers[:i] + numbers[i + 1:]
        
        # Check if removing this number makes the sequence safe
        if is_sequence_safe(test_numbers):
            return "safe"
            
    return "unsafe"

def solution() -> int:
    """
    Solve the problem by reading reports from stdin and counting safe reports.
    """
    safe_count = 0
    
    for line in sys.stdin:
        if line.strip():
            result = is_report_safe_with_dampener(line)
            if result == "safe":
                safe_count += 1
                
    return safe_count