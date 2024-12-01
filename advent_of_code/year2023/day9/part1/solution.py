"""Solution for Day 9: Mirage Maintenance."""
from sys import stdin
from typing import List


def extrapolate_history(history_str: str) -> int:
    """Calculate the extrapolated value for a given number history.
    
    Args:
        history_str: A string of space-separated numbers representing the history
        
    Returns:
        The extrapolated next value in the sequence
    """
    # Convert string input to list of integers
    numbers = [int(x) for x in history_str.strip().split()]
    
    # Generate sequence of differences until all zeros
    sequences = [numbers]
    while not all(x == 0 for x in sequences[-1]):
        current = sequences[-1]
        diffs = []
        for i in range(len(current) - 1):
            diffs.append(current[i + 1] - current[i])
        sequences.append(diffs)
    
    # Extrapolate next value from bottom up
    sequences[-1].append(0)  # Add zero to bottom sequence
    
    # Work backwards through sequences to fill in extrapolated values
    for i in range(len(sequences) - 2, -1, -1):
        current_seq = sequences[i]
        below_seq = sequences[i + 1]
        next_value = current_seq[-1] + below_seq[-1]
        current_seq.append(next_value)
    
    return sequences[0][-1]


def solution() -> int:
    """Read histories from stdin and return sum of extrapolated values.
    
    Returns:
        The sum of all extrapolated values
    """
    total = 0
    for line in stdin:
        if line.strip():  # Skip empty lines
            total += extrapolate_history(line)
    return total


if __name__ == "__main__":
    print(solution())