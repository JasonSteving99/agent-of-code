"""Solution for calculating scratchcard points."""
from sys import stdin
import re
from typing import List, Set


def parse_line(line: str) -> tuple[Set[int], Set[int]]:
    """Parse a single line into winning numbers and numbers you have."""
    # Remove the "Card X: " prefix and split into two parts
    numbers_part = line.split(": ")[1]
    winning_part, have_part = numbers_part.split(" | ")
    
    # Convert each part into a set of integers
    winning_nums = set(int(num) for num in re.findall(r'\d+', winning_part))
    have_nums = set(int(num) for num in re.findall(r'\d+', have_part))
    
    return winning_nums, have_nums


def calculate_scratchcard_points(input_line: str) -> int:
    """Calculate points for a scratchcard based on matching numbers.
    
    Args:
        input_line: A string representing a scratchcard line in format:
                   "Card X: w1 w2 ... wn | h1 h2 ... hm"
                   where w's are winning numbers and h's are numbers you have
    
    Returns:
        int: The number of points the card is worth
    """
    winning_nums, have_nums = parse_line(input_line)
    
    # Find all matching numbers
    matches = winning_nums.intersection(have_nums)
    
    # If no matches, return 0 points
    if not matches:
        return 0
    
    # First match is worth 1 point, each subsequent match doubles the value
    return 1 << (len(matches) - 1)


def solution() -> int:
    """Read all input lines and calculate total points."""
    total_points = 0
    
    for line in stdin:
        if line.strip():  # Skip empty lines
            total_points += calculate_scratchcard_points(line.strip())
    
    return total_points


if __name__ == "__main__":
    print(solution())