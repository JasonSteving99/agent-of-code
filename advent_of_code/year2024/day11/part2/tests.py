"""
Tests for stone evolution simulation after 75 blinks (part 2).

This test suite verifies that given a string containing initial stone energy levels,
the function correctly simulates the stone energy evolution after 75 blinks following
the specified rules. Each stone on every blink distributes its energy to adjacent stones.
"""

from solution import simulate_stone_evolution_part_2


def test_five_stones_sequence():
    """Test stone evolution with a sequence of 5 stones with varying energy levels."""
    initial_stones = "0 1 10 99 999"
    expected = 149161030616311
    
    result = simulate_stone_evolution_part_2(initial_stones)
    
    assert result == expected, (
        f"Stone evolution simulation failed for input '{initial_stones}'. "
        f"Expected result: '{expected}', but got '{result}'"
    )


def test_two_stones_sequence():
    """Test stone evolution with a sequence of 2 stones."""
    initial_stones = "125 17"
    expected = 65601038650482
    
    result = simulate_stone_evolution_part_2(initial_stones)
    
    assert result == expected, (
        f"Stone evolution simulation failed for input '{initial_stones}'. "
        f"Expected result: '{expected}', but got '{result}'"
    )