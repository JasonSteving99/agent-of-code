"""Solution for Red-Nosed Reports."""
from sys import stdin
from typing import List


def is_report_safe(report: str) -> str:
    """
    Determine if a given report is safe according to the reactor safety rules.
    
    Args:
        report: A string containing space-separated numbers representing levels
        
    Returns:
        'safe' if the report meets all safety criteria, 'unsafe' otherwise
    """
    # Convert report string to list of integers
    levels = [int(x) for x in report.strip().split()]
    
    if len(levels) < 2:
        return 'unsafe'
    
    # Check if levels are all increasing or all decreasing
    is_increasing = None
    
    # Compare adjacent numbers
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i-1]
        
        # If diff is 0, report is unsafe
        if diff == 0:
            return 'unsafe'
            
        # Set direction on first comparison if not set
        if is_increasing is None:
            is_increasing = diff > 0
            
        # Check if direction changes
        elif (diff > 0) != is_increasing:
            return 'unsafe'
            
        # Check if difference is more than 3
        if abs(diff) > 3:
            return 'unsafe'
    
    return 'safe'


def solution() -> int:
    """
    Read reports from stdin and count how many of them are safe.
    
    Returns:
        The count of safe reports
    """
    safe_count = 0
    
    # Read all reports
    for line in stdin:
        if line.strip():
            if is_report_safe(line) == 'safe':
                safe_count += 1
    
    return safe_count


if __name__ == "__main__":
    print(solution())