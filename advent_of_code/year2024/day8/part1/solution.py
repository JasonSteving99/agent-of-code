from typing import List, Set, Tuple
import sys

def count_antinodes(input_str: str) -> int:
    grid = [list(line) for line in input_str.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])

    antennas: dict[str, List[Tuple[int, int]]] = {}
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.':
                freq = grid[r][c]
                if freq not in antennas:
                    antennas[freq] = []
                antennas[freq].append((r, c))

    antinodes: Set[Tuple[int, int]] = set()
    for freq, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                r1, c1 = positions[i]
                r2, c2 = positions[j]

                dr = r2 - r1
                dc = c2 - c1

                # Calculate potential antinode positions
                ar1 = int(round(r1 - dr / 2))
                ac1 = int(round(c1 - dc / 2))
                ar2 = int(round(r2 + dr / 2))
                ac2 = int(round(c2 + dc / 2))

                if 0 <= ar1 < rows and 0 <= ac1 < cols:
                    antinodes.add((ar1, ac1))
                if 0 <= ar2 < rows and 0 <= ac2 < cols:
                    antinodes.add((ar2, ac2))

    return len(antinodes)

def solution() -> int:
    return count_antinodes(sys.stdin.read())