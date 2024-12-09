"""
Solution for Day 9: Disk Fragmenter.
Takes a disk map and returns checksum after defragmentation.
"""
from typing import List, Tuple

def parse_disk_map(disk_map: str) -> List[Tuple[int, int]]:
    """Parse disk map into a list of (file_length, free_space) tuples."""
    segments = [int(c) for c in disk_map]
    result = []
    for i in range(0, len(segments), 2):
        file_length = segments[i]
        free_space = segments[i + 1] if i + 1 < len(segments) else 0
        result.append((file_length, free_space))
    return result

def create_block_representation(parsed_disk_map: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Create a list of (file_id, length) tuples from parsed disk map."""
    blocks: List[Tuple[int, int]] = []
    for i, (file_length, _) in enumerate(parsed_disk_map):
        blocks.append((i, file_length))
    return blocks

def compact_disk(blocks: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Compact disk by moving files to leftmost possible position."""
    compacted_blocks = blocks.copy()
    total_blocks = sum(length for _, length in blocks)
    result = []
    current_pos = 0

    while current_pos < total_blocks and compacted_blocks:
        file_id, length = compacted_blocks.pop(0)
        result.append((file_id, length))
        current_pos += length

    return result

def calculate_checksum(blocks: List[Tuple[int, int]]) -> int:
    """Calculate filesystem checksum based on file positions and IDs."""
    checksum = 0
    current_pos = 0

    for file_id, length in blocks:
        for pos in range(current_pos, current_pos + length):
            checksum += pos * file_id
        current_pos += length

    return checksum

def calculate_disk_checksum(disk_map: str) -> int:
    """
    Calculate the checksum of a disk after compacting all files.

    Args:
        disk_map: A string representing the disk map

    Returns:
        The filesystem checksum after compaction
    """
    parsed_disk_map = parse_disk_map(disk_map)
    blocks = create_block_representation(parsed_disk_map)
    compacted_blocks = compact_disk(blocks)
    return calculate_checksum(compacted_blocks)

def solution() -> int:
    """Read input from stdin and return the solution."""
    disk_map = input().strip()
    return calculate_disk_checksum(disk_map)