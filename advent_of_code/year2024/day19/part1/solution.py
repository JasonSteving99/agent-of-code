from typing import List, Set
import sys

def is_design_possible(patterns: str, design: str) -> bool:
    # Convert patterns string into a set of patterns
    pattern_set = {pat.strip() for pat in patterns.split(',')}

    def can_make_design(remaining: str, memo: dict) -> bool:
        if not remaining:  # Base case: empty string means we found a valid split
            return True
        
        if remaining in memo:  # If we've seen this substring before, return cached result
            return memo[remaining]
        
        # Try each pattern as a prefix
        for pattern in pattern_set:
            if remaining.startswith(pattern):
                if can_make_design(remaining[len(pattern):], memo):
                    memo[remaining] = True
                    return True
                    
        memo[remaining] = False
        return False

    # Use dynamic programming with memoization
    return can_make_design(design, {})

def solution() -> int:
    # Read input from stdin
    input_lines = sys.stdin.read().strip().split('\n')
    
    # First line contains the patterns
    patterns = input_lines[0]
    
    # Skip the blank line and get designs
    designs = [line for line in input_lines[2:] if line]
    
    # Count possible designs
    count = sum(1 for design in designs if is_design_possible(patterns, design))
    
    return count