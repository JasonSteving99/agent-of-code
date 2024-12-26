"""Unit tests for the check_fit function which determines if a key fits into a lock.

The check_fit function takes two strings representing lock and key height patterns,
where each pattern is a comma-separated sequence of integer heights.
It returns "fit" if the key fits into the lock, or "overlap" if there's any overlap.

These tests verify that:
1. The function correctly identifies when key and lock shapes overlap
2. The function correctly identifies when key and lock shapes fit together
"""

from solution import check_fit
import pytest

def test_first_key_overlaps_with_first_lock():
    lock = "0,5,3,4,3"
    key = "5,0,2,1,3"
    result = check_fit(lock, key)
    assert result == "overlap", f"Expected 'overlap' for lock='{lock}' and key='{key}', but got '{result}'"

def test_second_key_overlaps_with_first_lock():
    lock = "0,5,3,4,3"
    key = "4,3,4,0,2"
    result = check_fit(lock, key)
    assert result == "overlap", f"Expected 'overlap' for lock='{lock}' and key='{key}', but got '{result}'"

def test_third_key_fits_first_lock():
    lock = "0,5,3,4,3"
    key = "3,0,2,0,1"
    result = check_fit(lock, key)
    assert result == "fit", f"Expected 'fit' for lock='{lock}' and key='{key}', but got '{result}'"

def test_first_key_overlaps_with_second_lock():
    lock = "1,2,0,5,3"
    key = "5,0,2,1,3"
    result = check_fit(lock, key)
    assert result == "overlap", f"Expected 'overlap' for lock='{lock}' and key='{key}', but got '{result}'"

def test_second_key_fits_second_lock():
    lock = "1,2,0,5,3"
    key = "4,3,4,0,2"
    result = check_fit(lock, key)
    assert result == "fit", f"Expected 'fit' for lock='{lock}' and key='{key}', but got '{result}'"

def test_third_key_fits_second_lock():
    lock = "1,2,0,5,3"
    key = "3,0,2,0,1"
    result = check_fit(lock, key)
    assert result == "fit", f"Expected 'fit' for lock='{lock}' and key='{key}', but got '{result}'"