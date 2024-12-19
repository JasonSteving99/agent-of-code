"""Solution for finding the first byte that blocks path to exit."""
from collections import deque
from typing import List, Set, Tuple


def find_first_blocking_byte(input_data: str) -> str:
    """Find coordinates of first byte that makes exit unreachable."""
    # Parse the falling bytes coordinates
    falling_coords: List[Tuple[int, int]] = []
    for line in input_data.strip().splitlines():
        x, y = map(int, line.strip().split(','))
        falling_coords.append((x, y))

    # Get grid size from input coordinates
    max_x = max(x for x, _ in falling_coords)
    max_y = max(y for _, y in falling_coords)
    grid_size = max(max_x, max_y) + 1

    def has_path_to_exit(corrupted: Set[Tuple[int, int]]) -> bool:
        """Check if there is still a path to exit using BFS."""
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        start = (0, 0)
        target = (grid_size - 1, grid_size - 1)
        
        queue = deque([start])
        visited = {start}
        
        while queue:
            x, y = queue.popleft()
            
            if (x, y) == target:
                return True
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                if (0 <= new_x < grid_size and 
                    0 <= new_y < grid_size and 
                    (new_x, new_y) not in visited and 
                    (new_x, new_y) not in corrupted):
                    
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
        
        return False

    # Try adding bytes one by one until path is blocked
    corrupted: Set[Tuple[int, int]] = set()
    
    for x, y in falling_coords:
        corrupted.add((x, y))
        # If no path exists after adding this byte, it's the blocking one
        if not has_path_to_exit(corrupted):
            return f"{x},{y}"
    
    # Should not reach here according to problem statement
    return "-1,-1"


def solution() -> str:
    """Read from stdin and solve the problem."""
    import sys
    input_data = sys.stdin.read()
    return find_first_blocking_byte(input_data)


if __name__ == "__main__":
    print(solution())