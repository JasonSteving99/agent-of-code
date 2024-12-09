"""
These tests cover the disk defragmentation and checksum calculation functionality.
The tests verify:
1. Processing of a complex disk map with multiple files and free spaces
2. Handling of a simple disk map case that cannot be defragmented
"""

from solution import calculate_disk_checksum


def test_complex_disk_map_with_checksum():
    disk_map = "2333133121414131402"
    expected_checksum = 1928
    result = calculate_disk_checksum(disk_map)
    assert result == expected_checksum, (
        f"Failed to calculate correct checksum for disk map '{disk_map}'\n"
        f"Expected: {expected_checksum}, but got: {result}"
    )


def test_simple_disk_map_no_checksum():
    disk_map = "12345"
    expected_result = None
    result = calculate_disk_checksum(disk_map)
    assert result == expected_result, (
        f"Failed to handle simple disk map '{disk_map}' correctly\n"
        f"Expected: {expected_result}, but got: {result}"
    )