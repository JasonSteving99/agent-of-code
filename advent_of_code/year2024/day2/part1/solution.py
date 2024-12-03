from typing import List
import sys

def is_report_safe(report: str) -> str:
    """
    Given a report consisting of space-separated numbers,
    determines whether the report is safe based on reactor safety criteria.
    Returns "safe" if levels are monotonically increasing or decreasing with
    differences between adjacent levels between 1 and 3 inclusive.
    Returns "unsafe" otherwise.
    """
    numbers = list(map(int, report.split()))
    
    # Need at least two numbers to compare
    if len(numbers) < 2:
        return "unsafe"
    
    # Determine if sequence is increasing or decreasing based on first difference
    first_diff = numbers[1] - numbers[0]
    if first_diff == 0:
        return "unsafe"
    is_increasing = first_diff > 0
    
    # Check all adjacent pairs
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        
        # Check if difference is too small or too large
        if abs(diff) < 1 or abs(diff) > 3:
            return "unsafe"
        
        # Check if direction changes
        if (is_increasing and diff < 0) or (not is_increasing and diff > 0):
            return "unsafe"
            
    return "safe"

def solution() -> int:
    """
    Read reports from stdin and return the count of safe reports.
    Each report is a line of space-separated numbers.
    """
    safe_count = 0
    for line in sys.stdin:
        if is_report_safe(line.strip()) == "safe":
            safe_count += 1
    return safe_count

if __name__ == "__main__":
    print(solution())