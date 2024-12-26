"""
Unit tests for counting compatible lock and key pairs.

The tests verify the function's ability to:
1. Parse input string containing schematics for both locks and keys
2. Interpret pin height patterns correctly
3. Compare lock and key schematics to determine compatibility
4. Count and return the number of unique compatible pairs
"""

from solution import count_compatible_lock_key_pairs

def test_complex_lock_key_example():
    schematic = """#####
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

    result = count_compatible_lock_key_pairs(schematic)
    
    # The test asserts that for this complex pattern of 
    # multiple locks and keys, exactly 3 compatible pairs exist
    assert result == 3, (
        f"Expected 3 compatible lock-key pairs for the given schematic, "
        f"but got {result}. Input schematic:\n{schematic}"
    )