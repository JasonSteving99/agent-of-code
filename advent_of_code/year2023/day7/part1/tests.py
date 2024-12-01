# Unit tests for the 'calculate_total_winnings' function covering basic examples.
# These tests check the total winnings calculation based on hand rankings and bids.

from solution import calculate_total_winnings
import pytest

@pytest.mark.parametrize("hands_and_bids, expected_winnings", [
    ("32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483", 6440),
])
def test_calculate_total_winnings(hands_and_bids, expected_winnings):
    actual_winnings = calculate_total_winnings(hands_and_bids)
    assert actual_winnings == expected_winnings, f"For hands and bids '{hands_and_bids}', expected winnings {expected_winnings}, but got {actual_winnings}"
