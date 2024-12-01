# This test suite covers the function extrapolate_history(history: str) -> int
# It is based on examples of input/output pairs provided as part of the problem description.
# The tests below verify that the function behaves as expected for these specific examples.

from solution import extrapolate_history
import pytest

@pytest.mark.parametrize("history, expected", [("0 3 6 9 12 15", 18), ("1 3 6 10 15 21", 28), ("10 13 16 21 30 45", 68)])
def test_extrapolate_history(history, expected):
    actual = extrapolate_history(history)
    assert actual == expected, f"For history = '{history}', expected {expected}, but got {actual}"
