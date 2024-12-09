"""Unit tests for compact_disk_and_calculate_checksum function.

This set of tests verifies the disk compaction and checksum calculation functionality where:
1. Disk map is represented as a string with numerical digits representing file IDs
2. Files are moved from right to left into free space, moving whole files at a time
3. Files are moved in order from largest file ID to smallest
4. Checksum is calculated as sum of (block_index * file_ID) for each block
5. Empty spaces (.) are skipped in checksum calculation
"""

from solution import compact_disk_and_calculate_checksum


def test_compact_disk_example():
    """Test disk compaction and checksum calculation for the example case.
    This test verifies that the function correctly:
    - Compacts files from right to left
    - Moves whole files at a time 
    - Processes files in descending ID order
    - Calculates checksum based on final positions
    """
    # Given
    disk_map = "2333133121414131402"
    expected_checksum = 2858
    
    # When
    actual_checksum = compact_disk_and_calculate_checksum(disk_map)
    
    # Then
    assert actual_checksum == expected_checksum, (
        f"Failed to calculate correct checksum after compacting disk.\n"
        f"Input disk map: {disk_map}\n"
        f"Expected checksum: {expected_checksum}\n"
        f"Actual checksum: {actual_checksum}"
    )