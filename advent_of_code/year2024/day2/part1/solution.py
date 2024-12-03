```python
from typing import List

def is_report_safe(report: str) -> str:
    """
    Determine if a reactor report is safe based on level patterns.
    
    Args:
        report: A string of space-separated numbers representing the levels
        
    Returns:
        "safe" if the report meets safety criteria, "unsafe" otherwise
    """
    # Convert report string to list of integers
    levels = [int(x) for x in report.split()]
    
    # Check if there are adjacent identical numbers
    for i in range(len(levels) - 1):
        if levels[i] == levels[i + 1]:
            return "unsafe"
    
    # Check if sequence is monotonic and differences are within bounds
    is_increasing = None
    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]
        
        # First difference determines if sequence should be increasing or decreasing
        if is_increasing is None:
            is_increasing = diff > 0
        
        # Check if direction changes
        if (diff > 0) != is_increasing:
            return "unsafe"
        
        # Check if difference is within bounds (1-3)
        if abs(diff) < 1 or abs(diff) > 3:
            return "unsafe"
    
    return "safe"

def solution() -> int:
    """
    Read reports from stdin and count the number of safe reports.
    
    Returns:
        The count of safe reports
    """
    safe_count = 0
    try:
        while True:
            line = input().strip()
            if not line:
                break
            if is_report_safe(line) == "safe":
                safe_count += 1
    except EOFError:
        pass
    
    return safe_count

if __name__ == "__main__":
    print(solution())
```