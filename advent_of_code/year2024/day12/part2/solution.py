from typing import List, Set, Dict, Tuple
from collections import deque

def get_regions(grid: List[List[str]]) -> Dict[Tuple[int, int], List[Tuple[int, int]]]:
    height = len(grid)
    width = len(grid[0])
    visited = set()
    regions = {}
    
    def get_neighbors(r: int, c: int) -> List[Tuple[int, int]]:
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < height and 0 <= nc < width and 
                grid[nr][nc] == grid[r][c]):
                neighbors.append((nr, nc))
        return neighbors
    
    for r in range(height):
        for c in range(width):
            if (r, c) not in visited:
                plant = grid[r][c]
                region = []
                queue = deque([(r, c)])
                visited.add((r, c))
                
                while queue:
                    curr_r, curr_c = queue.popleft()
                    region.append((curr_r, curr_c))
                    
                    for nr, nc in get_neighbors(curr_r, curr_c):
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc))
                
                for pos in region:
                    regions[pos] = region
                    
    return regions

def count_region_sides(region: List[Tuple[int, int]], grid: List[List[str]]) -> int:
    height = len(grid)
    width = len(grid[0])
    region_set = set(region)
    vertical_edges = set()
    horizontal_edges = set()

    for r, c in region:
        # Check for vertical edges
        if c + 1 < width and (r, c + 1) not in region_set or c + 1 == width:
            vertical_edges.add((r, c + 1))
        if c > 0 and (r, c - 1) not in region_set or c == 0:
            vertical_edges.add((r, c))
        
        # Check for horizontal edges
        if r + 1 < height and (r + 1, c) not in region_set or r + 1 == height:
            horizontal_edges.add((r + 1, c))
        if r > 0 and (r - 1, c) not in region_set or r == 0:
            horizontal_edges.add((r, c))
    
    vertical_sides = 0
    horizontal_sides = 0

    # Count continuous vertical sides
    vertical_edges_by_column = {}
    for r, c in vertical_edges:
        if c not in vertical_edges_by_column:
            vertical_edges_by_column[c] = []
        vertical_edges_by_column[c].append(r)
    
    for c in vertical_edges_by_column:
      rows = sorted(vertical_edges_by_column[c])
      if rows:
        vertical_sides += 1
        for i in range(1, len(rows)):
          if rows[i] != rows[i-1] + 1:
            vertical_sides += 1

    
    #Count continuous horizontal sides
    horizontal_edges_by_row = {}
    for r, c in horizontal_edges:
      if r not in horizontal_edges_by_row:
        horizontal_edges_by_row[r] = []
      horizontal_edges_by_row[r].append(c)
    
    for r in horizontal_edges_by_row:
      cols = sorted(horizontal_edges_by_row[r])
      if cols:
        horizontal_sides += 1
        for i in range(1, len(cols)):
          if cols[i] != cols[i-1] + 1:
            horizontal_sides += 1

    
    return vertical_sides + horizontal_sides

def calculate_total_price_with_bulk_discount(input_str: str) -> int:
    # Convert input string to grid
    grid = [list(line) for line in input_str.strip().split('\n')]
    
    # Get all regions
    regions = get_regions(grid)
    
    # Calculate total price
    total_price = 0
    processed_regions = set()
    
    for pos in regions:
        region = regions[pos]
        # Convert to tuple for hashing
        region_tuple = tuple(sorted(region))
        
        if region_tuple not in processed_regions:
            area = len(region)
            num_sides = count_region_sides(region, grid)
            price = area * num_sides
            total_price += price
            processed_regions.add(region_tuple)
    
    return total_price

def solution() -> int:
    # Read input from stdin
    import sys
    input_data = sys.stdin.read().strip()
    return calculate_total_price_with_bulk_discount(input_data)