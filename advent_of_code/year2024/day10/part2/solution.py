from typing import List, Set, Tuple, Dict
import sys
from collections import defaultdict


def parse_map(input_str: str) -> List[List[int]]:
    """Parse the input string into a 2D grid of integers."""
    return [[int(c) if c.isdigit() else -1 for c in line] for line in input_str.strip().split('\n')]


def find_trailheads(grid: List[List[int]]) -> List[Tuple[int, int]]:
    """Find all positions with height 0 in the grid."""
    rows, cols = len(grid), len(grid[0])
    return [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]


def get_neighbors(pos: Tuple[int, int], grid: List[List[int]]) -> List[Tuple[int, int]]:
    """Get valid neighboring positions (up, down, left, right)."""
    r, c = pos
    rows, cols = len(grid), len(grid[0])
    neighbors = []
    
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # right, down, left, up
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] != -1:
            neighbors.append((new_r, new_c))
    
    return neighbors


def count_distinct_trails(start: Tuple[int, int], grid: List[List[int]]) -> int:
    """Count number of distinct hiking trails from start to height-9 positions."""
    rows, cols = len(grid), len(grid[0])
    paths = set()
    
    def encode_path(path: List[Tuple[int, int]]) -> str:
        """Convert path to string for uniqueness comparison."""
        return ','.join(f"{x},{y}" for x, y in path)
    
    def dfs(pos: Tuple[int, int], current_path: List[Tuple[int, int]], seen: Set[Tuple[int, int]]) -> None:
        r, c = pos
        
        if grid[r][c] == 9:  # Found a complete path to a peak
            paths.add(encode_path(current_path))
            return
        
        current_height = grid[r][c]
        for next_pos in get_neighbors(pos, grid):
            nr, nc = next_pos
            if next_pos not in seen and grid[nr][nc] == current_height + 1:
                dfs(next_pos, current_path + [next_pos], seen | {next_pos})
    
    dfs(start, [start], {start})
    return len(paths)


def calculate_total_trailhead_rating(input_map: str) -> int:
    """Calculate the sum of ratings for all trailheads in the map."""
    # Parse the input map
    grid = parse_map(input_map)
    
    # Find all trailheads (positions with height 0)
    trailheads = find_trailheads(grid)
    
    # Calculate rating for each trailhead
    total_rating = sum(count_distinct_trails(th, grid) for th in trailheads)
    
    return total_rating


def solution() -> int:
    """Read from stdin and return the solution."""
    input_data = sys.stdin.read()
    return calculate_total_trailhead_rating(input_data)


if __name__ == "__main__":
    print(solution())