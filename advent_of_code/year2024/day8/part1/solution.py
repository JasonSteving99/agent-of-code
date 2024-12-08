"""Day 8: Resonant Collinearity Solution."""

def count_antinodes(grid_str: str) -> int:
    """Count unique locations of antinodes."""
    # Parse input grid
    grid = [list(line) for line in grid_str.strip().splitlines()]
    rows, cols = len(grid), len(grid[0])

    # Find antennas by frequency
    antennas = {}
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != '.':
                freq = grid[i][j]
                if freq not in antennas:
                    antennas[freq] = []
                antennas[freq].append((i, j))

    # Set to store unique antinode locations
    antinodes = set()

    # For each frequency, find antinodes
    for freq, positions in antennas.items():
        # Need at least 2 antennas of the same frequency
        if len(positions) < 2:
            continue

        # Check all pairs of antennas with same frequency
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Vector from first to second antenna
                dx = x2 - x1
                dy = y2 - y1

                # Calculate antinode positions
                # First antinode: one unit away from the first antenna
                ax1 = x1 - dx
                ay1 = y1 - dy
                if 0 <= ax1 < rows and 0 <= ay1 < cols:
                    antinodes.add((ax1, ay1))

                # Second antinode: one unit away from the second antenna
                ax2 = x2 + dx
                ay2 = y2 + dy
                if 0 <= ax2 < rows and 0 <= ay2 < cols:
                    antinodes.add((ax2, ay2))

    return len(antinodes)

def solution() -> int:
    """Read input from stdin and return the solution."""
    import sys
    grid = sys.stdin.read()
    return count_antinodes(grid)