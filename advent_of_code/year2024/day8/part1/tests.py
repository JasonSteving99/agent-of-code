"""
Test suite for count_antinodes function that counts unique antinodes in a grid map.

An antinode occurs at any point that is perfectly in line with two antennas of the
same frequency (indicated by same character), where one antenna is twice the distance 
from the antinode point compared to the other antenna.

The test focuses on a scenario with:
- Mixed frequency antennas ('0' and 'A')
- Multiple potential antinode locations
- Both horizontal and vertical alignments
"""

from solution import count_antinodes


def test_mixed_frequency_antenna_grid():
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
    
    # Explicit assertion message showing input and expected output
    assert result == 14, (
        f"Failed to count correct number of antinodes.\n"
        f"Input grid:\n{grid}\n"
        f"Expected: 14 antinodes\n"
        f"Got: {result} antinodes"
    )