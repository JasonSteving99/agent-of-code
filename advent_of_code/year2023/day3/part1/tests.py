# These tests cover the function sum_part_numbers which calculates the sum of part numbers adjacent to symbols in the given string

from solution import sum_part_numbers
import pytest

@pytest.mark.parametrize("test_input, expected", [("467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..", 4361)])
def test_sum_part_numbers(test_input, expected):
    actual = sum_part_numbers(test_input)
    assert actual == expected, f"For input '{test_input}', expected sum {expected}, but got {actual}"
