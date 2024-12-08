"""
Tests for count_antinodes function that counts unique antinode locations on a grid map.

An antinode is a point in line with two antennas of the same frequency, where one antenna
is twice as far from the antinode as the other. The tests verify calculation of antinodes
for given antenna configurations.

The grid map is represented as a string with newline-separated rows. Each character can be:
- '.' representing empty space
- '0','A', etc. representing antennas of different frequencies
"""

from solution import count_antinodes


def test_count_antinodes_with_mixed_frequencies():
    # Test case with both '0' and 'A' frequency antennas
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
        f"Expected {expected_antinodes} antinodes for the given grid with '0' and 'A' "
        f"frequency antennas, but got {result}. Input grid:\n{input_grid}"
    )