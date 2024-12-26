"""
This test suite verifies the check_fit function which determines whether a key fits a lock based on pin heights.
The function accepts two lists of integers representing:
1. Lock pin heights (first argument)
2. Key pin heights (second argument)
And returns either "fit" or "overlap" as a string based on whether the key properly fits the lock.

A key fits a lock when its pin heights, when added to the lock's pin heights, create a valid pin setup.
A key overlaps when its pin heights would interfere with the lock's pin heights.
"""

from solution import check_fit
import pytest

def test_first_example_key_overlaps_lock():
    lock_pins = [0, 5, 3, 4, 3]
    key_pins = [5, 0, 2, 1, 3]
    result = check_fit(lock_pins, key_pins)
    assert result == "overlap", f"Expected 'overlap' for lock pins {lock_pins} and key pins {key_pins}, but got '{result}'"

def test_second_example_key_overlaps_lock():
    lock_pins = [0, 5, 3, 4, 3]
    key_pins = [4, 3, 4, 0, 2]
    result = check_fit(lock_pins, key_pins)
    assert result == "overlap", f"Expected 'overlap' for lock pins {lock_pins} and key pins {key_pins}, but got '{result}'"

def test_third_example_key_fits_lock():
    lock_pins = [0, 5, 3, 4, 3]
    key_pins = [3, 0, 2, 0, 1]
    result = check_fit(lock_pins, key_pins)
    assert result == "fit", f"Expected 'fit' for lock pins {lock_pins} and key pins {key_pins}, but got '{result}'"

def test_fourth_example_key_overlaps_lock():
    lock_pins = [1, 2, 0, 5, 3]
    key_pins = [5, 0, 2, 1, 3]
    result = check_fit(lock_pins, key_pins)
    assert result == "overlap", f"Expected 'overlap' for lock pins {lock_pins} and key pins {key_pins}, but got '{result}'"

def test_fifth_example_key_fits_lock():
    lock_pins = [1, 2, 0, 5, 3]
    key_pins = [4, 3, 4, 0, 2]
    result = check_fit(lock_pins, key_pins)
    assert result == "fit", f"Expected 'fit' for lock pins {lock_pins} and key pins {key_pins}, but got '{result}'"

def test_sixth_example_key_fits_lock():
    lock_pins = [1, 2, 0, 5, 3]
    key_pins = [3, 0, 2, 0, 1]
    result = check_fit(lock_pins, key_pins)
    assert result == "fit", f"Expected 'fit' for lock pins {lock_pins} and key pins {key_pins}, but got '{result}'"