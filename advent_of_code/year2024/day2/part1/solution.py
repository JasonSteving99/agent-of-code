"""Solve the Red-Nosed Reports problem."""
from typing import List


def is_report_safe(report: str) -> str:
    """
    Determine if a reactor report is safe.
    
    A report is safe if:
    1. The levels are either all increasing or all decreasing
    2. Any two adjacent levels differ by at least one and at most three
    
    Args:
        report: Space-separated string of numbers representing levels
        
    Returns:
        'Safe' if report meets safety criteria, 'Unsafe' otherwise
    """
    # Convert report string to list of integers
    levels = [int(x) for x in report.split()]
    
    # Check if two adjacent numbers are equal
    for i in range(len(levels) - 1):
        if levels[i] == levels[i + 1]:
            return "Unsafe"
    
    # Calculate differences between adjacent numbers
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]
    
    # Check if differences are within allowed range
    if not all(1 <= abs(diff) <= 3 for diff in diffs):
        return "Unsafe"
    
    # Check if all differences have the same sign (all increasing or all decreasing)
    if not (all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)):
        return "Unsafe"
    
    return "Safe"


def solution() -> int:
    """
    Read reports from stdin and count how many are safe.
    
    Returns:
        Number of safe reports
    """
    reports = []
    try:
        while True:
            line = input().strip()
            if not line:
                break
            reports.append(line)
    except EOFError:
        pass
    
    return sum(1 for report in reports if is_report_safe(report) == "Safe")