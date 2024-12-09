"""
This test suite covers the calculate_disk_checksum function which processes a disk map string
and returns a checksum value. The function should:
1. Take a string input representing disk sectors
2. Process and compact the disk map according to some rules
3. Return either an integer checksum for valid cases, or None for cases that don't produce a final checksum

The exact compacting and checksum calculation rules will be implemented in the solution,
these tests verify the expected input/output behavior based on provided examples.
"""

from solution import calculate_disk_checksum


def test_calculate_disk_checksum_with_valid_long_input():
    """Test calculate_disk_checksum with a longer input that produces a valid checksum."""
    # Given a longer disk map string
    disk_map = "2333133121414131402"
    
    # When calculating the checksum
    result = calculate_disk_checksum(disk_map)
    
    # Then we expect the specific checksum value
    assert result == 1928, \
        f"calculate_disk_checksum('{disk_map}') returned {result}, expected 1928"


def test_calculate_disk_checksum_with_short_input_returning_null():
    """Test calculate_disk_checksum with a shorter input that should return None."""
    # Given a shorter disk map string
    disk_map = "12345"
    
    # When calculating the checksum
    result = calculate_disk_checksum(disk_map)
    
    # Then we expect None as the result
    assert result is None, \
        f"calculate_disk_checksum('{disk_map}') returned {result}, expected None"