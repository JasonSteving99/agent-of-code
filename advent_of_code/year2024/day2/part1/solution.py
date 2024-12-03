from typing import List
import sys

def is_report_safe(line: str) -> str:
    # Convert string to list of integers
    levels = [int(x) for x in line.split()]
    
    # If less than 2 numbers, can't check sequence
    if len(levels) < 2:
        return "unsafe"
        
    # Check if sequence is strictly increasing or decreasing
    increasing = decreasing = True
    
    # Check each adjacent pair
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i-1]
        
        # Check if difference is within valid range (1-3)
        if abs(diff) < 1 or abs(diff) > 3:
            return "unsafe"
        
        # Track if sequence is increasing or decreasing
        if diff > 0:
            decreasing = False
        else:
            increasing = False
            
        # If neither increasing nor decreasing consistently, it's unsafe
        if not increasing and not decreasing:
            return "unsafe"
    
    return "safe"

def solution() -> int:
    safe_count = 0
    
    # Read input from stdin
    for line in sys.stdin:
        line = line.strip()
        if not line:  # Skip empty lines
            continue
        
        if is_report_safe(line) == "safe":
            safe_count += 1
            
    return safe_count

if __name__ == "__main__":
    print(solution())