"""Solution for pathfinding in memory grid problem."""
from collections import deque
from typing import List, Set, Tuple


def shortest_path_after_kilobyte(input_data: str) -> int:
    # Parse the falling bytes coordinates
    falling_coords: List[Tuple[int, int]] = []
    for line in input_data.strip().splitlines():
        x, y = map(int, line.strip().split(','))
        falling_coords.append((x, y))

    # Take only first 1024 bytes (kilobyte)
    falling_coords = falling_coords[:1024]

    # Get grid size (in actual problem it's 70x70)
    max_x = max(x for x, _ in falling_coords)
    max_y = max(y for _, y in falling_coords)
    grid_size = max(max_x, max_y) + 1

    # Create set of corrupted coordinates
    corrupted: Set[Tuple[int, int]] = set(falling_coords)

    def bfs() -> int:
        # Directions: up, right, down, left
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        
        # Start position and target position
        start = (0, 0)
        target = (grid_size - 1, grid_size - 1)
        
        # Queue for BFS: (x, y, steps)
        queue = deque([(start[0], start[1], 0)])
        visited = {start}
        
        while queue:
            x, y, steps = queue.popleft()
            
            # If we reached target, return steps
            if (x, y) == target:
                return steps
            
            # Try all directions
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                # Check if new position is valid:
                # 1. Within grid bounds
                # 2. Not visited
                # 3. Not corrupted
                if (0 <= new_x < grid_size and 
                    0 <= new_y < grid_size and 
                    (new_x, new_y) not in visited and 
                    (new_x, new_y) not in corrupted):
                    
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y, steps + 1))
        
        # If no path found (shouldn't happen according to problem)
        return -1

    # Return shortest path length
    return bfs()


def solution() -> int:
    """Read from stdin and solve the problem."""
    import sys
    input_data = sys.stdin.read()
    return shortest_path_after_kilobyte(input_data)


if __name__ == "__main__":
    print(solution())