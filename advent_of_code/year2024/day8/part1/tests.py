"""
Tests for the count_antinodes function that calculates the number of unique locations 
containing antinodes in a grid of antennas based on resonant collinearity conditions.

The function takes a string input representing a grid where:
- '.' represents empty space
- '0' represents type-0 antennas 
- 'A' represents type-A antennas

The function should count locations where antinodes form based on antenna resonance patterns
according to the collinearity rules.
"""

from solution import count_antinodes

def test_complex_antenna_grid():
    # Test case with a mix of type-0 and type-A antennas
    input_grid = (
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
    
    expected_antinodes = 14
    result = count_antinodes(input_grid)
    
    assert result == expected_antinodes, (
        f"Failed to correctly count antinodes in grid.\n"
        f"Input grid:\n{input_grid}\n"
        f"Expected {expected_antinodes} antinodes, but got {result}"
    )