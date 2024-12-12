"""
Solution for Garden Groups problem.
"""
from typing import List, Set, Tuple


def get_perimeter_and_area(garden_map: List[List[str]], visited: Set[Tuple[int, int]], 
                          row: int, col: int, letter: str) -> Tuple[int, int]:
    """Calculate perimeter and area for a region starting at given position."""
    if (row < 0 or col < 0 or row >= len(garden_map) or col >= len(garden_map[0]) or 
        (row, col) in visited or garden_map[row][col] != letter):
        return 0, 0

    visited.add((row, col))
    perimeter = 0
    area = 1

    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_row, new_col = row + dr, col + dc

        if (new_row < 0 or new_col < 0 or 
            new_row >= len(garden_map) or new_col >= len(garden_map[0]) or
            garden_map[new_row][new_col] != letter):
            perimeter += 1
        else:
            if (new_row, new_col) not in visited:  # Only recurse if not visited
                _, sub_area = get_perimeter_and_area(garden_map, visited, new_row, new_col, letter)
                area += sub_area

    return perimeter, area


def calculate_total_fence_price(input_map: str) -> str:
    """Calculate total price of fencing for all regions in the garden map."""
    garden_map = [list(line) for line in input_map.strip().split('\n')]

    if not garden_map:
        return "0"

    visited = set()
    total_price = 0
    rows, cols = len(garden_map), len(garden_map[0])

    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited:
                letter = garden_map[row][col]
                perimeter, area = get_perimeter_and_area(garden_map, visited, row, col, letter)
                total_price += area * perimeter

    return str(total_price)


def solution() -> str:
    """Read from stdin and return the solution."""
    import sys
    input_data = sys.stdin.read()
    return calculate_total_fence_price(input_data)