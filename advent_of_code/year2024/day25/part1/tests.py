"""
This test suite validates the check_key_fit function which determines whether a key fits a lock
based on their pin heights. The function takes a list of two lists (lock pins and key pins) and
returns either 'fit' or 'overlap'.

Test cases cover:
1. Cases where the key doesn't fit (returns 'overlap')
2. Cases where the key fits perfectly (returns 'fit')
"""

from solution import check_key_fit


def test_first_key_overlaps_with_first_lock():
    lock_and_key = [[0, 5, 3, 4, 3], [5, 0, 2, 1, 3]]
    result = check_key_fit(lock_and_key)
    assert result == "overlap", f"Expected 'overlap' for lock pins {lock_and_key[0]} and key pins {lock_and_key[1]}, but got '{result}'"


def test_second_key_overlaps_with_first_lock():
    lock_and_key = [[0, 5, 3, 4, 3], [4, 3, 4, 0, 2]]
    result = check_key_fit(lock_and_key)
    assert result == "overlap", f"Expected 'overlap' for lock pins {lock_and_key[0]} and key pins {lock_and_key[1]}, but got '{result}'"


def test_third_key_fits_first_lock():
    lock_and_key = [[0, 5, 3, 4, 3], [3, 0, 2, 0, 1]]
    result = check_key_fit(lock_and_key)
    assert result == "fit", f"Expected 'fit' for lock pins {lock_and_key[0]} and key pins {lock_and_key[1]}, but got '{result}'"


def test_first_key_overlaps_with_second_lock():
    lock_and_key = [[1, 2, 0, 5, 3], [5, 0, 2, 1, 3]]
    result = check_key_fit(lock_and_key)
    assert result == "overlap", f"Expected 'overlap' for lock pins {lock_and_key[0]} and key pins {lock_and_key[1]}, but got '{result}'"


def test_second_key_fits_second_lock():
    lock_and_key = [[1, 2, 0, 5, 3], [4, 3, 4, 0, 2]]
    result = check_key_fit(lock_and_key)
    assert result == "fit", f"Expected 'fit' for lock pins {lock_and_key[0]} and key pins {lock_and_key[1]}, but got '{result}'"


def test_third_key_fits_second_lock():
    lock_and_key = [[1, 2, 0, 5, 3], [3, 0, 2, 0, 1]]
    result = check_key_fit(lock_and_key)
    assert result == "fit", f"Expected 'fit' for lock pins {lock_and_key[0]} and key pins {lock_and_key[1]}, but got '{result}'"