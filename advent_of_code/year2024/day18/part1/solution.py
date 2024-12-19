from typing import List, Set, Tuple
from collections import deque
import sys


def get_coordinates(input_str: str) -> List[Tuple[int, int]]:
    """Parse input string into list of x,y coordinates."""
    coordinates = []
    for line in input_str.strip().splitlines():
        x, y = map(int, line.split(','))
        coordinates.append((x, y))
    return coordinates


def create_grid(coordinates: List[Tuple[int, int]], max_bytes: int = 1024) -> Set[Tuple[int, int]]:
    """Create a set of corrupted coordinates after simulating byte falls."""
    corrupted = set()
    for i, (x, y) in enumerate(coordinates):
        if i >= max_bytes:
            break
        corrupted.add((x, y))
    return corrupted


def get_valid_moves(pos: Tuple[int, int], grid_size: int) -> List[Tuple[int, int]]:
    """Get valid adjacent positions from current position."""
    x, y = pos
    moves = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    ]
    return [(x, y) for x, y in moves if 0 <= x <= grid_size and 0 <= y <= grid_size]


def shortest_path_bfs(start: Tuple[int, int], end: Tuple[int, int], 
                     corrupted: Set[Tuple[int, int]], grid_size: int) -> int:
    """Find shortest path from start to end avoiding corrupted positions using BFS."""
    queue = deque([(start, 0)])  # (position, steps)
    visited = {start}

    while queue:
        pos, steps = queue.popleft()
        if pos == end:
            return steps

        for next_pos in get_valid_moves(pos, grid_size):
            if next_pos not in visited and next_pos not in corrupted:
                visited.add(next_pos)
                queue.append((next_pos, steps + 1))

    return -1  # No path found


def shortest_path_after_byte_falls(input_str: str, grid_size: int = 70) -> int:
    """
    Find the shortest path from (0,0) to (grid_size, grid_size) after simulating byte falls.
    
    Args:
        input_str: String containing coordinates of falling bytes
        grid_size: Size of the grid (default 70)
        
    Returns:
        Minimum number of steps needed to reach the exit
    """
    # Parse input and create corrupted grid
    coordinates = get_coordinates(input_str)
    corrupted = create_grid(coordinates)

    # Find shortest path from (0,0) to (grid_size, grid_size)
    start = (0, 0)
    end = (grid_size, grid_size)
    
    return shortest_path_bfs(start, end, corrupted, grid_size)


def solution() -> int:
    """Read from stdin and return the solution."""
    input_data = sys.stdin.read()
    return shortest_path_after_byte_falls(input_data)


if __name__ == "__main__":
    print(solution())
