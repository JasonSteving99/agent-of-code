"""
Tests for `check_fit` function that validates lock and key fitting patterns.

The tests cover:
- Each lock must have '#' in top row and '.' in bottom row
- Each key must have '.' in top row and '#' in bottom row
- Locks and keys must fit without pin overlaps in any column
- Returns count of unique fitting lock/key pairs
"""

from solution import check_fit

def test_complex_lock_and_key_patterns():
    # Input contains 2 locks and 3 keys in a specific pattern format
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
    
    # Function should return 3 as there are 3 valid lock/key combinations that fit
    result = check_fit(input_str)
    assert result == 3, f"Expected 3 valid lock/key combinations, but got {result} for input:\n{input_str}"