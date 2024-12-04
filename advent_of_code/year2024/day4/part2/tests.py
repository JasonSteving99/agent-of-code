"""
Unit tests for the count_xmas function that identifies 'X-MAS' patterns in a grid.

An 'X-MAS' pattern consists of two 'MAS' strings arranged in an X shape.
Each 'MAS' sequence must be read left-to-right or top-to-bottom.
The tests verify the function's ability to:
1. Identify a single X-MAS pattern in a minimal 3x3 grid
2. Find multiple X-MAS patterns in a larger 10x10 grid
3. Handle grid input formatting with newline characters
"""

from solution import count_xmas


def test_minimal_grid_with_single_xmas():
    grid = "M.S\n.A.\nM.S"
    result = count_xmas(grid)
    assert result == 1, (
        f"Expected 1 X-MAS pattern in minimal 3x3 grid:\n{grid}\n"
        f"but got {result}"
    )


def test_larger_grid_with_multiple_xmas_patterns():
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
        f"Expected 9 X-MAS patterns in 10x10 grid:\n{grid}\n"
        f"but got {result}"
    )


def test_grid_formatting():
    """Test that the function properly handles grid input formatting with newlines"""
    # Same as first test but testing explicit newline handling
    grid = "M.S\n.A.\nM.S"
    assert len(grid.split("\n")) == 3, "Test grid should have exactly 3 rows"
    result = count_xmas(grid)
    assert result == 1, (
        f"Expected 1 X-MAS pattern in grid with explicit newlines:\n{grid}\n"
        f"but got {result}"
    )