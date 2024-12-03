"""Solution for 'Report Safety Analysis' puzzle."""
from typing import List
import sys


def is_report_safe(report: str) -> str:
    """
    Determine if a reactor report is safe based on level patterns.
    
    A report is safe if:
    1. Levels are either all increasing or all decreasing
    2. Adjacent levels differ by at least 1 and at most 3
    
    Args:
        report (str): A space-separated string of integer levels
        
    Returns:
        str: 'safe' if the report meets safety criteria, 'unsafe' otherwise
    """
    # Convert report string to list of integers
    levels = [int(x) for x in report.split()]
    
    if len(levels) < 2:
        return "unsafe"
        
    # Check first difference to determine if should be increasing or decreasing
    is_increasing = None
    first_diff = levels[1] - levels[0]
    
    if first_diff == 0:  # No change between adjacent numbers
        return "unsafe"
    elif first_diff > 0:
        is_increasing = True
    else:
        is_increasing = False
        
    # Check each adjacent pair
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i-1]
        
        # Check if difference is too small/large or zero
        if abs(diff) < 1 or abs(diff) > 3:
            return "unsafe"
            
        # Check if direction changes
        if (is_increasing and diff < 0) or (not is_increasing and diff > 0):
            return "unsafe"
            
    return "safe"


def solution() -> int:
    """
    Read reports from stdin and count how many are safe.
    
    Returns:
        int: The number of safe reports
    """
    safe_count = 0
    
    # Read each line as a report
    for line in sys.stdin:
        report = line.strip()
        if not report:  # Skip empty lines
            continue
        if is_report_safe(report) == "safe":
            safe_count += 1
            
    return safe_count