from typing import List, Set, Tuple
import sys


def parse_map(input_str: str) -> List[List[int]]:
    """Parse the input string into a 2D grid of integers."""
    return [[int(c) for c in line] for line in input_str.strip().split('\n')]


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
        if 0 <= new_r < rows and 0 <= new_c < cols:
            neighbors.append((new_r, new_c))
    
    return neighbors


def count_reachable_peaks(start: Tuple[int, int], grid: List[List[int]]) -> int:
    """Count number of height-9 positions reachable via valid hiking trails from start."""
    rows, cols = len(grid), len(grid[0])
    visited = set()
    reachable_peaks = set()
    
    def dfs(pos: Tuple[int, int], current_height: int, path: Set[Tuple[int, int]]) -> None:
        if pos in path:  # Avoid cycles
            return
        
        r, c = pos
        if grid[r][c] != current_height:  # Must increase by exactly 1
            return
            
        if grid[r][c] == 9:  # Found a peak
            reachable_peaks.add(pos)
            return
            
        new_path = path | {pos}
        for next_pos in get_neighbors(pos, grid):
            nr, nc = next_pos
            if grid[nr][nc] == current_height + 1:  # Only consider positions with height + 1
                if (pos, next_pos) not in visited:
                    visited.add((pos, next_pos))
                    dfs(next_pos, current_height + 1, new_path)
    
    dfs(start, 0, set())
    return len(reachable_peaks)


def calculate_total_trailhead_score(input_map: str) -> int:
    """Calculate the sum of scores for all trailheads in the map."""
    # Parse the input map
    grid = parse_map(input_map)
    
    # Find all trailheads (positions with height 0)
    trailheads = find_trailheads(grid)
    
    # Calculate score for each trailhead
    total_score = sum(count_reachable_peaks(th, grid) for th in trailheads)
    
    return total_score


def solution() -> int:
    """Read from stdin and return the solution."""
    input_data = sys.stdin.read()
    return calculate_total_trailhead_score(input_data)


if __name__ == "__main__":
    print(solution())