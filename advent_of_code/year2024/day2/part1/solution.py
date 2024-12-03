"""
Solution to process nuclear reactor reports checking for safety based on level patterns.
"""
from typing import List


def is_report_safe(report: str) -> str:
    """Determine if a reactor report is safe based on level patterns.
    
    A report is safe if:
    1. The levels are either all increasing or all decreasing
    2. Adjacent levels differ by at least 1 and at most 3
    
    Args:
        report: A string of space-separated numbers representing levels
        
    Returns:
        'Safe' if the report meets safety criteria, 'Unsafe' otherwise
    """
    # Convert space-separated numbers to list of integers 
    levels = [int(x) for x in report.strip().split()]
    
    if len(levels) < 2:
        return "Unsafe"  # Reports should have at least 2 levels
        
    # Determine direction (increasing or decreasing) from first pair
    is_increasing = levels[1] > levels[0]
    prev_level = levels[0]
    
    for curr_level in levels[1:]:
        diff = curr_level - prev_level
        
        # Check if difference between adjacent levels is within bounds
        if abs(diff) < 1 or abs(diff) > 3:
            return "Unsafe"
            
        # Check if direction is consistent
        if is_increasing and diff < 0:
            return "Unsafe"
        if not is_increasing and diff > 0:
            return "Unsafe"
            
        prev_level = curr_level
        
    return "Safe"


def solution() -> int:
    """Read multiple reports from stdin and count the safe ones.
    
    Returns:
        The total number of safe reports.
    """
    safe_count = 0
    
    try:
        while True:
            line = input().strip()
            if not line:  # Handle empty lines or EOF
                break
            if is_report_safe(line) == "Safe":
                safe_count += 1
    except EOFError:
        pass
        
    return safe_count