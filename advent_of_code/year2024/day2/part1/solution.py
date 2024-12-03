from typing import List, Optional
import sys


def is_report_safe(report: str) -> str:
    """Check if a report is safe based on provided rules.
    
    Args:
        report: String containing space-separated numbers representing levels.
        
    Returns:
        "safe" if the report meets safety criteria, "unsafe" otherwise.
    """
    # Convert the report string to a list of integers
    levels = [int(x) for x in report.split()]
    
    if len(levels) < 2:
        return "unsafe"
    
    # Check if levels are strictly increasing or decreasing
    differences = [levels[i+1] - levels[i] for i in range(len(levels)-1)]
    
    # Check if all differences are in the same direction (all positive or all negative)
    if not (all(d > 0 for d in differences) or all(d < 0 for d in differences)):
        return "unsafe"
    
    # Check if differences are between 1 and 3 inclusive
    if not all(1 <= abs(d) <= 3 for d in differences):
        return "unsafe"
    
    return "safe"


def solution() -> int:
    """Read input from stdin and process all reports.
    
    Returns:
        Number of safe reports in the input.
    """
    safe_count = 0
    
    # Read all lines from stdin
    for line in sys.stdin:
        report = line.strip()
        if not report:  # Skip empty lines
            continue
        
        if is_report_safe(report) == "safe":
            safe_count += 1
    
    return safe_count