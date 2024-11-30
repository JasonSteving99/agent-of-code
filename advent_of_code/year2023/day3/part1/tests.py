# These tests cover identifying "part numbers" adjacent to symbols and calculating their sum.
from solution import sum_part_numbers
import pytest

@pytest.mark.parametrize("test_input,expected", [("467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..", 4361)])
def test_sum_part_numbers(test_input, expected):
    actual = sum_part_numbers(test_input)
    assert actual == expected, f"Input: {test_input}, Expected: {expected}, Actual: {actual}"