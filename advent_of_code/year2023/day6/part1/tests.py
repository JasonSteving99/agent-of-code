# These tests cover the calculation of the product of the number of winning button press durations for each race.

from solution import calculate_winning_durations_product
import pytest

@pytest.mark.parametrize("input_str, expected_output", [
    ("Time:      7  15   30\nDistance:  9  40  200", 288),
])
def test_calculate_winning_durations_product(input_str, expected_output):
    actual_output = calculate_winning_durations_product(input_str)
    assert actual_output == expected_output, f"For input '{input_str}', expected output was '{expected_output}', but got '{actual_output}'"
