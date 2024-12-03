from typing import List
import sys

def is_report_safe_without_dampener(levels: List[int]) -> bool:
    if len(levels) < 2:
        return True
    
    # Check that each adjacent pair differs by 1-3
    # and all values follow same direction (increasing or decreasing)
    diffs = [levels[i] - levels[i-1] for i in range(1, len(levels))]
    
    # Check all differences are between 1 and 3 or between -3 and -1
    valid_diffs = all(1 <= diff <= 3 or -3 <= diff <= -1 for diff in diffs)
    if not valid_diffs:
        return False
        
    # Check all differences have same sign (all increasing or all decreasing)
    return all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)

def is_report_safe_with_dampener(report: str) -> str:
    levels = list(map(int, report.strip().split()))
    
    # First check if safe without removing any level
    if is_report_safe_without_dampener(levels):
        return "safe"
    
    # Try removing each level one at a time and check if resulting sequence is safe
    for i in range(len(levels)):
        # Create new list without level at index i
        test_levels = levels[:i] + levels[i+1:]
        if is_report_safe_without_dampener(test_levels):
            return "safe"
    
    return "unsafe"

def solution() -> int:
    reports = sys.stdin.read().strip().split('\n')
    safe_count = sum(1 for report in reports if is_report_safe_with_dampener(report) == "safe")
    return safe_count