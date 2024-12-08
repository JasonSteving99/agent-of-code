"""Unit tests for the count_antinodes function.

Given a grid where:
- '.' represents empty cells
- Characters (digits or letters) represent antennas with specific frequencies
- Antinodes form at points that are equidistant from pairs of antennas with the same frequency
- The tests verify that the function correctly counts unique antinode locations
"""

from solution import count_antinodes

def test_grid_with_zeros_and_uppercase_a():
    # Test grid with four '0' antennas and three 'A' antennas
    grid = (
        "............\n"
        "........0...\n"
        ".....0......\n"
        ".......0....\n"
        "....0.......\n"
        "......A.....\n"
        "............\n"
        "............\n"
        "........A...\n"
        ".........A..\n"
        "............\n"
        "............"
    )
    
    result = count_antinodes(grid)
    assert result == 14, (
        f"Expected 14 antinodes for grid with four '0' antennas and three 'A' antennas, "
        f"but got {result}.\nInput grid:\n{grid}"
    )