"""
Test suite for count_design_arrangements function that calculates the number of different ways
to arrange towel designs using available patterns.

The function accepts a string input containing:
1. A comma-separated list of available towel patterns
2. A blank line separator
3. A list of newline-separated towel designs

The function should return the total number of different possible arrangements
for all given designs using the available patterns.
"""

from solution import count_design_arrangements

def test_multiple_designs_arrangement_count():
    # Test input with multiple patterns and designs
    input_str = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

    # This tests a complex case with:
    # - 8 available patterns: r, wr, b, g, bwu, rb, gb, br
    # - 8 different towel designs to arrange
    result = count_design_arrangements(input_str)
    
    assert result == 16, (
        f"Failed to correctly count arrangements for multiple designs.\n"
        f"Input:\n{input_str}\n"
        f"Expected: 16\n"
        f"Got: {result}"
    )