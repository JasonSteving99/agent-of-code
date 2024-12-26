"""Unit tests for the parse_schematics function.

The parse_schematics function takes a string input containing ASCII art representations of 
lock and key schematics separated by empty lines, where:
- Each schematic is 7 lines high
- '#' represents solid material
- '.' represents empty space
- Each line should be 5 characters wide

The function should return a list of tuples, where each tuple contains two lists of integers 
representing the heights of lock and key pins calculated from the schematics.
The heights are determined by counting the '#' characters from bottom to top in each column.
"""

from solution import parse_schematics


def test_parse_two_schematics():
    input_str = """#####
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
    
    result = parse_schematics(input_str)
    assert len(result) == 1, f"Expected 1 lock-key pair, but got {len(result)}"
    lock_heights, key_heights = result[0]
    
    expected_lock = [0, 5, 3, 4, 3]
    expected_key = [5, 0, 2, 1, 3]
    
    assert lock_heights == expected_lock, \
        f"Lock heights mismatch. Expected {expected_lock}, got {lock_heights}"
    assert key_heights == expected_key, \
        f"Key heights mismatch. Expected {expected_key}, got {key_heights}"


def test_parse_four_schematics():
    input_str = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
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
#####

.....
.....
#.#..
###..
###.#
###.#
#####"""
    
    result = parse_schematics(input_str)
    assert len(result) == 2, f"Expected 2 lock-key pairs, but got {len(result)}"
    
    expected_pairs = [
        ([0, 5, 3, 4, 3], [1, 2, 0, 5, 3]),
        ([5, 0, 2, 1, 3], [4, 3, 4, 0, 2])
    ]
    
    for i, (lock_heights, key_heights) in enumerate(result):
        expected_lock, expected_key = expected_pairs[i]
        assert lock_heights == expected_lock, \
            f"Lock heights mismatch for pair {i}. Expected {expected_lock}, got {lock_heights}"
        assert key_heights == expected_key, \
            f"Key heights mismatch for pair {i}. Expected {expected_key}, got {key_heights}"


def test_parse_five_schematics():
    input_str = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
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
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""
    
    result = parse_schematics(input_str)
    assert len(result) == 3, f"Expected 3 lock-key pairs, but got {len(result)}"
    
    expected_pairs = [
        ([0, 5, 3, 4, 3], [1, 2, 0, 5, 3]),
        ([5, 0, 2, 1, 3], [4, 3, 4, 0, 2]),
        ([3, 0, 2, 0, 1], [3, 0, 2, 0, 1])
    ]
    
    for i, (lock_heights, key_heights) in enumerate(result):
        expected_lock, expected_key = expected_pairs[i]
        assert lock_heights == expected_lock, \
            f"Lock heights mismatch for pair {i}. Expected {expected_lock}, got {lock_heights}"
        assert key_heights == expected_key, \
            f"Key heights mismatch for pair {i}. Expected {expected_key}, got {key_heights}"