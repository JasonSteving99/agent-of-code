"""Unit tests for count_fitting_lock_key_pairs function.

The function should analyze a string input containing ASCII art representations of locks and keys,
where:
- '#' represents solid material
- '.' represents empty space
- Each lock/key is a 7x5 grid
- Input contains multiple patterns separated by newlines
- Function counts how many unique lock/key pairs can fit together

Key patterns need to be rotated and inverted to check if they fit with lock patterns.
The example demonstrates determining fitting pairs from multiple lock and key patterns.
"""

from solution import count_fitting_lock_key_pairs


def test_sample_lock_key_patterns():
    input_schematic = """#####
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
    
    result = count_fitting_lock_key_pairs(input_schematic)
    
    # Validate that for the given complex set of lock/key patterns,
    # exactly 3 unique fitting pairs are found after considering all
    # possible rotations and transformations
    assert result == 3, (
        f"Expected 3 fitting lock/key pairs for the sample input, "
        f"but got {result}. Input was a multi-pattern schematic with "
        "5 different 7x5 grids of locks and keys."
    )