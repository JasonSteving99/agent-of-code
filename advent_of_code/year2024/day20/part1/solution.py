"""Solution for Race Condition puzzle."""
from typing import List, Tuple, Set, Dict, Optional
from collections import deque
from heapq import heappush, heappop
import sys

def shortest_path_without_cheats(racetrack: str) -> int:
    """Find the shortest path from start to end without cheating."""
    # Parse the racetrack into a 2D grid
    grid = [list(line) for line in racetrack.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    
    # Find start and end positions
    start = end = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    
    # Dijkstra's algorithm
    def get_neighbors(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
        r, c = pos
        neighbors = []
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_r, new_c = r + dr, c + dc
            if (0 <= new_r < rows and 
                0 <= new_c < cols and 
                grid[new_r][new_c] in ['.', 'E']):
                neighbors.append((new_r, new_c))
        return neighbors
    
    # Priority queue for Dijkstra's [(distance, position)]
    pq = [(0, start)]
    distances = {start: 0}
    
    while pq:
        dist, pos = heappop(pq)
        if pos == end:
            return dist
        
        if dist > distances[pos]:
            continue
            
        for next_pos in get_neighbors(pos):
            new_dist = dist + 1
            if next_pos not in distances or new_dist < distances[next_pos]:
                distances[next_pos] = new_dist
                heappush(pq, (new_dist, next_pos))
    
    # If no path found
    return -1

def solution() -> int:
    """Read input from stdin and solve the problem."""
    input_text = sys.stdin.read()
    return shortest_path_without_cheats(input_text)

if __name__ == "__main__":
    print(solution())