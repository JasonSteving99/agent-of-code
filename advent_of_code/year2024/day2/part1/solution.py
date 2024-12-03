"""Solution for Day 2: Red-Nosed Reports."""
from typing import List


def classify_report(report: str) -> str:
    """Classify a report as 'safe' or 'unsafe' based on the rules.
    
    A report is safe if:
    1. The levels are either all increasing or all decreasing
    2. Adjacent levels differ by at least 1 and at most 3
    """
    # Convert report string to list of integers
    levels: List[int] = [int(x) for x in report.split()]
    
    if len(levels) < 2:
        return "unsafe"  # Single number or empty report is unsafe
        
    # Determine if sequence is increasing or decreasing from first pair
    increasing: bool | None = None
    prev: int = levels[0]
    
    for curr in levels[1:]:
        diff = curr - prev
        
        # Check if difference is within valid range (1-3 or -3 to -1)
        if abs(diff) < 1 or abs(diff) > 3:
            return "unsafe"
            
        # Set direction on first pair
        if increasing is None:
            increasing = diff > 0
        # Check if direction remains consistent
        elif (diff > 0) != increasing:
            return "unsafe"
            
        prev = curr
    
    return "safe"


def solution() -> int:
    """Read input reports and count how many are safe."""
    reports: List[str] = []
    try:
        while True:
            line = input().strip()
            if not line:
                break
            reports.append(line)
    except EOFError:
        pass

    safe_count = sum(1 for report in reports if classify_report(report) == "safe")
    return safe_count