# This test suite covers the calculation of the sum of part numbers adjacent to symbols in an engine schematic.

from solution import sum_part_numbers
import pytest

@pytest.mark.parametrize("test_input, expected", [("467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..", 4361)])
def test_sum_part_numbers(test_input, expected):
    actual_result = sum_part_numbers(test_input)
    assert actual_result == expected, f"For input '{test_input}', expected sum {expected} but got {actual_result}"
