from typing import Dict, Set, Tuple, List
from collections import deque

def calculate_total_fence_price(input_str: str) -> str:
    """
    Calculate the total price of fencing all regions in the garden map.
    
    Args:
        input_str: String representing the garden map
        
    Returns:
        String representation of total fencing price
    """
    if not input_str:
        return "0"
        
    # Convert input to grid
    grid = [list(line) for line in input_str.splitlines()]
    rows, cols = len(grid), len(grid[0])
    
    # Track visited cells to avoid processing same region twice
    visited = set()
    
    def get_neighbors(r: int, c: int) -> List[Tuple[int, int]]:
        """Get valid neighboring cells with same plant type."""
        plant = grid[r][c]
        neighbors = []
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == plant:
                neighbors.append((nr, nc))
        return neighbors
    
    def calculate_region_price(start_r: int, start_c: int) -> int:
        """Calculate price for a single region using BFS."""
        plant = grid[start_r][start_c]
        region = set()
        perimeter = 0
        queue = deque([(start_r, start_c)])
        region.add((start_r, start_c))
        
        while queue:
            r, c = queue.popleft()
            # Count perimeter sides
            sides = 4
            for nr, nc in get_neighbors(r, c):
                if (nr, nc) in region:
                    sides -= 1
                else:
                    queue.append((nr, nc))
                    region.add((nr, nc))
            perimeter += sides
            
        area = len(region)
        visited.update(region)
        return area * perimeter
    
    # Process each unvisited cell
    total_price = 0
    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited:
                total_price += calculate_region_price(r, c)
                
    return str(total_price)

def solution() -> str:
    """Read input from stdin and solve the problem."""
    import sys
    input_data = sys.stdin.read().strip()
    return calculate_total_fence_price(input_data)