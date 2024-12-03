from typing import List, Optional
import sys

def check_valid_sequence(levels: List[int]) -> bool:
    """Check if a sequence of levels is valid (all increasing or decreasing with correct differences)."""
    if len(levels) < 2:
        return True
        
    diff = levels[1] - levels[0]
    is_increasing = diff > 0
    
    for i in range(1, len(levels)):
        curr_diff = levels[i] - levels[i-1]
        if curr_diff == 0:  # No difference between adjacent numbers
            return False
        if abs(curr_diff) > 3:  # Difference greater than 3
            return False
        if (is_increasing and curr_diff < 0) or (not is_increasing and curr_diff > 0):
            return False
            
    return True

def is_safe_with_removal(levels: List[int]) -> bool:
    """Check if a report becomes safe after removing any single number."""
    if check_valid_sequence(levels):
        return True
        
    # Try removing each number and check if sequence becomes valid
    for i in range(len(levels)):
        test_levels = levels[:i] + levels[i+1:]
        if check_valid_sequence(test_levels):
            return True
            
    return False

def is_report_safe_with_dampener(report: str) -> str:
    """Determine if a report is safe with the Problem Dampener feature."""
    # Convert report string into list of integers
    levels = [int(x) for x in report.strip().split()]
    
    return "safe" if is_safe_with_removal(levels) else "unsafe"

def solution() -> int:
    """Read input from stdin and count the number of safe reports."""
    safe_count = 0
    
    for line in sys.stdin:
        if line.strip():  # Skip empty lines
            if is_report_safe_with_dampener(line) == "safe":
                safe_count += 1
                
    return safe_count