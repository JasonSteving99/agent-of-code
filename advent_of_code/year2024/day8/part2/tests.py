"""
Test suite for count_part2_antinodes function which calculates the total number of unique 
antinode locations in a grid map, where antinodes occur at positions that are exactly in line 
(horizontally, vertically, or diagonally) with at least two antennas of the same frequency.

Key test coverage:
- Multiple 'T' frequency antennas creating antinodes
- Multiple '0' and 'A' frequency antennas creating antinodes
- Various grid sizes and antenna placements
- Both horizontal/vertical and diagonal antinode alignments
"""

from solution import count_part2_antinodes


def test_t_frequency_antennas():
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
    result = count_part2_antinodes(input_map)
    assert result == "9", (
        f"Failed for T-frequency antenna map:\n{input_map}\n"
        f"Expected 9 antinodes, but got {result}"
    )


def test_zero_and_a_frequency_antennas():
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
    result = count_part2_antinodes(input_map)
    assert result == "34", (
        f"Failed for 0/A-frequency antenna map:\n{input_map}\n"
        f"Expected 34 antinodes, but got {result}"
    )