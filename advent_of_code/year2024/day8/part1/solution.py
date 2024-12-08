from typing import List, Set, Tuple
import sys

def count_antinodes(input_str: str) -> int:
    # Parse the input grid
    grid = [list(line) for line in input_str.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    
    # Get antenna positions by frequency
    antennas: dict[str, List[Tuple[int, int]]] = {}
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] not in '.':
                freq = grid[i][j]
                if freq not in antennas:
                    antennas[freq] = []
                antennas[freq].append((i, j))
                
    # Find all antinodes
    antinodes: Set[Tuple[int, int]] = set()
    
    # For each frequency
    for freq, positions in antennas.items():
        n = len(positions)
        # Compare all pairs of antennas with same frequency
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                
                # Check if one point is twice as far from potential antinode as the other
                # This creates two possible antinodes for each pair
                
                # Find vector between points
                dx = x2 - x1
                dy = y2 - y1
                
                # First antinode: extend 1/2 distance before first point
                ax = x1 - dx//2
                ay = y1 - dy//2
                if 0 <= ax < rows and 0 <= ay < cols:
                    antinodes.add((ax, ay))
                
                # Second antinode: extend 1/2 distance after second point
                ax = x2 + dx//2
                ay = y2 + dy//2
                if 0 <= ax < rows and 0 <= ay < cols:
                    antinodes.add((ax, ay))
    
    return len(antinodes)

def solution() -> int:
    return count_antinodes(sys.stdin.read())