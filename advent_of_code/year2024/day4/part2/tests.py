"""
This test suite verifies the functionality of the count_xmas function that finds 'X-MAS' patterns
in a grid, where an X-MAS pattern consists of two 'MAS' strings arranged in an 'X' shape.
The tests cover:
1. Basic case with a single X-MAS pattern in a minimal 3x3 grid
2. Complex case with multiple X-MAS patterns in a larger 10x10 grid
"""

from solution import count_xmas


def test_minimal_grid_single_xmas_pattern():
    grid = "M.S\n.A.\nM.S"
    result = count_xmas(grid)
    assert result == 1, (
        f"Failed to find single X-MAS pattern in minimal 3x3 grid.\n"
        f"Input grid:\n{grid}\n"
        f"Expected: 1\n"
        f"Got: {result}"
    )


def test_larger_grid_multiple_xmas_patterns():
    grid = (
        ".M.S......\n"
        "..A..MSMS.\n"
        ".M.S.MAA..\n"
        "..A.ASMSM.\n"
        ".M.S.M....\n"
        "..........\n"
        "S.S.S.S.S.\n"
        ".A.A.A.A..\n"
        "M.M.M.M.M.\n"
        ".........."
    )
    result = count_xmas(grid)
    assert result == 9, (
        f"Failed to find all X-MAS patterns in 10x10 grid.\n"
        f"Input grid:\n{grid}\n"
        f"Expected: 9\n"
        f"Got: {result}"
    )


def test_input_contains_newlines():
    """Verify that the function correctly handles input with newline characters"""
    grid1 = "M.S\n.A.\nM.S"
    grid2 = "M.S\r\n.A.\r\nM.S"  # Windows-style line endings
    result1 = count_xmas(grid1)
    result2 = count_xmas(grid2)
    assert result1 == result2 == 1, (
        f"Different results for same grid with different line endings.\n"
        f"Unix-style (\\n) result: {result1}\n"
        f"Windows-style (\\r\\n) result: {result2}\n"
        f"Expected both to be: 1"
    )