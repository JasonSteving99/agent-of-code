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

                if dx == 0:
                    ax = x1
                    ay1 = y1 - dy
                    ay2 = y2 + dy

                    if 0 <= ax < rows and 0 <= ay1 < cols:
                        antinodes.add((ax, ay1))
                    if 0 <= ax < rows and 0 <= ay2 < cols:
                        antinodes.add((ax, ay2))
                        
                elif dy == 0:
                    ay = y1
                    ax1 = x1 - dx
                    ax2 = x2 + dx

                    if 0 <= ax1 < rows and 0 <= ay < cols:
                        antinodes.add((ax1, ay))
                    if 0 <= ax2 < rows and 0 <= ay < cols:
                        antinodes.add((ax2, ay))
                else:
                    # Antinode 1
                    ax1 = x1 - dx // 2
                    ay1 = y1 - dy // 2
                    if 0 <= ax1 < rows and 0 <= ay1 < cols:
                        antinodes.add((ax1, ay1))

                    # Antinode 2
                    ax2 = x2 + dx // 2
                    ay2 = y2 + dy // 2
                    if 0 <= ax2 < rows and 0 <= ay2 < cols:
                        antinodes.add((ax2, ay2))
    return len(antinodes)

def solution() -> int:
    return count_antinodes(sys.stdin.read())