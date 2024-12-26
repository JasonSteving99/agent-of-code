"""
Tests for the lock/key combination counting function.

The function should:
1. Parse a string input containing multiple lock and key schematics
2. Analyze potential lock/key pairs to find valid combinations where pins don't overlap
3. Return the count of valid lock/key combinations

Key test focus:
- Parsing multi-line string input with lock/key schematics
- Finding compatible lock/key pairs based on pin heights
- Counting total number of valid combinations
"""

from solution import count_valid_lock_key_combinations


def test_complex_lock_key_combination_example():
    input_schematics = """#####
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
    
    result = count_valid_lock_key_combinations(input_schematics)
    
    assert result == 3, (
        f"Expected 3 valid lock/key combinations for the given schematics:\n"
        f"{input_schematics}\n"
        f"but got {result}"
    )