from typing import List
import sys

def is_report_safe(report: str) -> str:
    """
    Check if a given report is safe according to the Red-Nosed reactor safety criteria.
    
    Args:
        report: A string containing space-separated integers representing levels.
        
    Returns:
        "Safe" if the report meets safety criteria, "Unsafe" otherwise.
    """
    # Convert report string to list of integers
    levels = [int(x) for x in report.strip().split()]
    
    if len(levels) < 2:
        return "Unsafe"  # Single number or empty report is unsafe
    
    # Check first difference to determine if we should expect increasing or decreasing
    diff = levels[1] - levels[0]
    
    # Invalid if first difference is not between 1 and 3 inclusive
    if abs(diff) < 1 or abs(diff) > 3:
        return "Unsafe"
    
    # Expected increasing if first difference is positive
    should_increase = diff > 0
    
    # Check all adjacent pairs
    for i in range(1, len(levels)):
        curr_diff = levels[i] - levels[i-1]
        
        # Check if difference is within valid range (1-3)
        if abs(curr_diff) < 1 or abs(curr_diff) > 3:
            return "Unsafe"
        
        # Check if direction maintains consistency
        if should_increase and curr_diff <= 0:
            return "Unsafe"
        if not should_increase and curr_diff >= 0:
            return "Unsafe"
    
    return "Safe"

def solution() -> int:
    """
    Process all reports from stdin and count how many are safe.
    
    Returns:
        The number of safe reports.
    """
    safe_count = 0
    
    # Read each line from stdin
    for line in sys.stdin:
        if is_report_safe(line) == "Safe":
            safe_count += 1
            
    return safe_count

if __name__ == "__main__":
    print(solution())