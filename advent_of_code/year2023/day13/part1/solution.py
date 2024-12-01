"""Solution for Point of Incidence puzzle."""
from typing import List, Optional, Tuple
import sys


def transpose_pattern(pattern: List[str]) -> List[str]:
    """Transpose the pattern from rows to columns."""
    return ["".join(col) for col in zip(*pattern)]


def find_reflection(pattern: List[str]) -> Optional[int]:
    """Find the line of reflection in the pattern."""
    for i in range(1, len(pattern)):
        # For each possible reflection line between rows/columns i-1 and i
        rows_to_check = min(i, len(pattern) - i)
        is_reflection = True
        
        for offset in range(rows_to_check):
            if pattern[i - 1 - offset] != pattern[i + offset]:
                is_reflection = False
                break
                
        if is_reflection:
            return i
            
    return None


def calculate_reflection_value(pattern_str: str) -> int:
    """Calculate the reflection value for a single pattern.
    
    Args:
        pattern_str: String representation of the pattern using '.' and '#'
    
    Returns:
        int: The reflection value - columns to left of vertical reflection
             or 100 * rows above horizontal reflection
    """
    # Split the pattern into rows
    pattern = [line for line in pattern_str.strip().split('\n')]
    
    # First try to find horizontal reflection
    horizontal_reflection = find_reflection(pattern)
    if horizontal_reflection is not None:
        return horizontal_reflection * 100
        
    # If no horizontal reflection found, try vertical
    transposed = transpose_pattern(pattern)
    vertical_reflection = find_reflection(transposed)
    if vertical_reflection is not None:
        return vertical_reflection
        
    # There should always be a reflection according to puzzle rules
    raise ValueError("No reflection found in pattern")


def solution() -> int:
    """Read input from stdin and solve the problem.
    
    Returns:
        int: Sum of reflection values for all patterns
    """
    # Read all input
    input_text = sys.stdin.read().strip()
    
    # Split into individual patterns
    patterns = input_text.split('\n\n')
    
    # Calculate and sum the reflection value for each pattern
    total = sum(calculate_reflection_value(pattern) for pattern in patterns)
    
    return total