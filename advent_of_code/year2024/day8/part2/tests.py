"""
This test suite validates the count_antinodes_harmonic function which calculates
the number of unique antinode locations on a map where antinodes occur at positions
that are exactly in line (horizontally, vertically, or diagonally) with at least 
two antennas of the same frequency. The tests cover:
1. A map with 'T' frequency antennas and '#' obstacles
2. A map with '0' and 'A' frequency antennas
"""

from solution import count_antinodes_harmonic


def test_map_with_t_frequency_antennas():
    input_map = (
        "T....#....\n"
        "...T......\n"
        ".T....#...\n"
        ".........#\n"
        "..#.......\n"
        ".......... \n"
        "...#......\n"
        ".......... \n"
        "....#.....\n"
        ".........."
    )
    result = count_antinodes_harmonic(input_map)
    assert result == 9, (
        f"Expected 9 antinodes for map with T-frequency antennas:\n{input_map}\n"
        f"but got {result}"
    )


def test_map_with_zero_and_a_frequency_antennas():
    input_map = (
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
    result = count_antinodes_harmonic(input_map)
    assert result == 34, (
        f"Expected 34 antinodes for map with 0 and A frequency antennas:\n{input_map}\n"
        f"but got {result}"
    )