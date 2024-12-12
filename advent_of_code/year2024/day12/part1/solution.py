```python
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Set, Tuple
import sys


@dataclass
class Region:
    char: str
    area: int = 0
    perimeter: int = 0


def get_neighbors(r: int, c: int, rows: int, cols: int) -> List[Tuple[int, int]]:
    """Returns valid neighboring coordinates for a given position."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc))
    return neighbors


def find_region(
    start: Tuple[int, int],
    garden: List[str],
    visited: Set[Tuple[int, int]],
) -> Tuple[int, int, Set[Tuple[int, int]]]:
    """Find a complete region using flood fill and return its area and perimeter."""
    rows, cols = len(garden), len(garden[0])
    char = garden[start[0]][start[1]]
    region = set([start])
    to_visit = [start]
    perimeter = 0

    while to_visit:
        r, c = to_visit.pop()
        neighbors = get_neighbors(r, c, rows, cols)

        # Count perimeter by checking all four sides
        edges = 4
        for nr, nc in neighbors:
            if garden[nr][nc] == char:
                edges -= 1
                if (nr, nc) not in region:
                    to_visit.append((nr, nc))
                    region.add((nr, nc))
        perimeter += edges

    visited.update(region)
    return len(region), perimeter, region


def calculate_total_fence_price(garden_map: str) -> str:
    """Calculate the total price of fencing for all regions in the garden."""
    garden = garden_map.strip().split('\n')
    if not garden:
        return "0"

    visited = set()
    total_price = 0
    rows, cols = len(garden), len(garden[0])

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                area, perimeter, _ = find_region((r, c), garden, visited)
                price = area * perimeter
                total_price += price

    return str(total_price)


def solution() -> str:
    """Read input from stdin and return the solution."""
    return calculate_total_fence_price(sys.stdin.read())

```