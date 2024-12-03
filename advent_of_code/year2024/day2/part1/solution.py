"""Analyze reactor reports for safety based on level patterns."""
from typing import List
import sys

def is_report_safe(report: str) -> str:
    """
    Determine if a reactor report is safe based on level patterns.
    
    A report is safe if:
    1. All levels are either increasing or decreasing
    2. Adjacent levels differ by at least 1 and at most 3
    
    Args:
        report (str): Space-separated string of numbers representing levels
        
    Returns:
        str: "safe" if report meets safety criteria, "unsafe" otherwise
    """
    # Convert report string to list of integers
    levels = [int(x) for x in report.split()]
    
    if len(levels) < 2:
        return "unsafe"
        
    # Check first pair to determine if sequence should be increasing or decreasing
    is_increasing = levels[1] > levels[0]
    
    # Track previous number for comparison
    prev = levels[0]
    
    for curr in levels[1:]:
        diff = curr - prev
        
        # Check if difference is within valid range (1-3)
        if abs(diff) < 1 or abs(diff) > 3:
            return "unsafe"
            
        # Check if direction maintains consistency
        if is_increasing and diff <= 0:
            return "unsafe"
        if not is_increasing and diff >= 0:
            return "unsafe"
            
        prev = curr
    
    return "safe"

def solution() -> int:
    """
    Read reactor reports from stdin and count how many are safe.
    
    Returns:
        int: Count of safe reports
    """
    safe_count = 0
    
    for line in sys.stdin:
        if line.strip():  # Skip empty lines
            if is_report_safe(line.strip()) == "safe":
                safe_count += 1
                
    return safe_count

if __name__ == "__main__":
    result = solution()
    print(result)  # Only print if run as script