from typing import List, Set, Tuple
import sys

def count_antinodes(input_str: str) -> int:
    grid = [list(line) for line in input_str.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    
    antennas: dict[str, List[Tuple[int, int]]] = {}
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != '.':
                freq = grid[i][j]
                if freq not in antennas:
                    antennas[freq] = []
                antennas[freq].append((i, j))
    
    antinodes: Set[Tuple[int, int]] = set()
    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                dx = x2 - x1
                dy = y2 - y1
                
                ax = int(round(x1 - dx / 2))
                ay = int(round(y1 - dy / 2))
                if 0 <= ax < rows and 0 <= ay < cols:
                    antinodes.add((ax, ay))

                ax = int(round(x2 + dx / 2))
                ay = int(round(y2 + dy / 2))
                if 0 <= ax < rows and 0 <= ay < cols:
                    antinodes.add((ax, ay))
                    
    return len(antinodes)

def solution() -> int:
    return count_antinodes(sys.stdin.read())