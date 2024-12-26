"""
Tests for the check_fit function that determines if a key pattern can fit into a lock pattern.

The tests verify:
1. Detection of overlaps in different columns (first, second, and last)
2. Successful fit scenarios where key and lock patterns are compatible
3. Correct interpretation of the height patterns for both key and lock

Each test includes a key pattern (first string block) and lock pattern (second string block),
comparing their vertical heights to determine compatibility.
"""

from solution import check_fit


def test_overlap_in_last_column():
    key_lock_pattern = """#####
.####
.####
.####
.#.#.
.#...
.....

.....
#....
#....
#...#
#.#.#
#.###
#####"""
    assert check_fit(key_lock_pattern, key_lock_pattern) == "0,5,3,4,3 and 5,0,2,1,3: overlap in the last column", \
        f"Expected overlap detection in last column for pattern:\n{key_lock_pattern}"


def test_overlap_in_second_column():
    key_lock_pattern = """#####
.####
.####
.####
.#.#.
.#...
.....

.....
.....
#.#..
###..
###.#
###.#
#####"""
    assert check_fit(key_lock_pattern, key_lock_pattern) == "0,5,3,4,3 and 4,3,4,0,2: overlap in the second column", \
        f"Expected overlap detection in second column for pattern:\n{key_lock_pattern}"


def test_successful_fit_first_key():
    key_lock_pattern = """#####
.####
.####
.####
.#.#.
.#...
.....

.....
.....
.....
#....
#.#..
#.#.#
#####"""
    assert check_fit(key_lock_pattern, key_lock_pattern) == "0,5,3,4,3 and 3,0,2,0,1: all columns fit!", \
        f"Expected successful fit for pattern:\n{key_lock_pattern}"


def test_overlap_in_first_column():
    key_lock_pattern = """#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####"""
    assert check_fit(key_lock_pattern, key_lock_pattern) == "1,2,0,5,3 and 5,0,2,1,3: overlap in the first column", \
        f"Expected overlap detection in first column for pattern:\n{key_lock_pattern}"


def test_successful_fit_second_key():
    key_lock_pattern = """#####
##.##
.#.##
...##
...#.
...#.
.....

.....
.....
#.#..
###..
###.#
###.#
#####"""
    assert check_fit(key_lock_pattern, key_lock_pattern) == "1,2,0,5,3 and 4,3,4,0,2: all columns fit!", \
        f"Expected successful fit for pattern:\n{key_lock_pattern}"


def test_successful_fit_third_key():
    key_lock_pattern = """#####
##.##
.#.##
...##
...#.
...#.
.....

.....
.....
.....
#....
#.#..
#.#.#
#####"""
    assert check_fit(key_lock_pattern, key_lock_pattern) == "1,2,0,5,3 and 3,0,2,0,1: all columns fit!", \
        f"Expected successful fit for pattern:\n{key_lock_pattern}"