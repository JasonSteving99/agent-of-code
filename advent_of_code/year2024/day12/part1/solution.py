"""
Solution for Garden Groups problem
"""
from typing import Set, Dict, List, Tuple
from collections import deque


def get_region_area_perimeter(
    garden_map_lines: List[str], 
    start_pos: Tuple[int, int], 
    visited: Set[Tuple[int, int]], 
    plant_type: str,
    rows: int
) -> Tuple[int, int]:
    """Calculate area and perimeter of a region starting from given position."""
    area = 0
    perimeter = 0
    queue = deque([start_pos])
    region_points = set()
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c = queue.popleft()
        if (r, c) in region_points:
            continue

        region_points.add((r, c))
        visited.add((r, c))
        area += 1

        # Check all four sides for perimeter calculation and neighboring plots
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Count edge as perimeter if out of bounds or different plant type
            if nr < 0 or nr >= rows or nc < 0 or nc >= len(garden_map_lines[nr]) or (
                nr >=0 and nr < rows and nc >= 0 and nc < len(garden_map_lines[nr]) and garden_map_lines[nr][nc] != plant_type):
                perimeter += 1
            elif (nr, nc) not in region_points and (
                nr >= 0 and nr < rows and nc >= 0 and nc < len(garden_map_lines[nr])):
                queue.append((nr, nc))

    return area, perimeter


def calculate_total_fence_price(garden_map_str: str) -> str:
    """Calculate the total price of fencing all regions in the garden map."""
    # Convert string input to 2D list
    garden_map_lines = garden_map_str.strip().splitlines()
    rows = len(garden_map_lines)

    total_price = 0
    visited = set()

    # Iterate through each position in the garden
    for r in range(rows):
        cols = len(garden_map_lines[r])
        for c in range(cols):
            if (r, c) not in visited:
                area, perimeter = get_region_area_perimeter(
                    garden_map_lines, (r, c), visited, garden_map_lines[r][c], rows
                )
                region_price = area * perimeter
                total_price += region_price

    return str(total_price)


def solution() -> str:
    """Read input from stdin and return the solution."""
    import sys
    return calculate_total_fence_price(sys.stdin.read())
