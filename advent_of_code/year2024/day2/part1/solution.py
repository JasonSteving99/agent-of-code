from typing import List, Optional
import sys

def is_report_safe(report: str) -> str:
    """
    Check if a report is safe based on reactor safety criteria.
    A report is safe if:
    1. Levels are either all increasing or all decreasing
    2. Adjacent levels differ by at least 1 and at most 3
    
    Args:
        report: A string containing space-separated integers representing levels
        
    Returns:
        'safe' if the report meets safety criteria, 'unsafe' otherwise
    """
    # Convert string of space-separated numbers to list of integers
    levels = [int(x) for x in report.split()]
    
    # Check if there are at least 2 levels to compare
    if len(levels) < 2:
        return "unsafe"
    
    # Determine if sequence should be increasing or decreasing
    is_increasing: Optional[bool] = None
    
    # Check each adjacent pair
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i-1]
        
        # If difference is 0 or outside allowed range (-3 to -1 or 1 to 3)
        if diff == 0 or abs(diff) > 3:
            return "unsafe"
            
        # For first pair, determine if sequence is increasing or decreasing
        if is_increasing is None:
            is_increasing = diff > 0
        # For subsequent pairs, ensure direction remains consistent
        elif (diff > 0) != is_increasing:
            return "unsafe"
            
    return "safe"

def solution() -> int:
    """
    Read reports from stdin and count how many are safe.
    
    Returns:
        The number of safe reports.
    """
    safe_count = 0
    
    # Read each line from stdin
    for line in sys.stdin:
        line = line.strip()
        if line:  # Skip empty lines
            if is_report_safe(line) == "safe":
                safe_count += 1
                
    return safe_count

if __name__ == "__main__":
    print(solution())