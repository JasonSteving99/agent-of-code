"""Solution for Disk Fragmenter problem."""
from typing import List, Tuple
import sys


def parse_disk_map(disk_map: str) -> Tuple[List[int], List[int]]:
    """Parse disk map into file and space sizes."""
    file_sizes = [int(disk_map[i]) for i in range(0, len(disk_map), 2)]
    space_sizes = [int(disk_map[i]) for i in range(1, len(disk_map), 2)]
    return file_sizes, space_sizes


def create_block_representation(file_sizes: List[int], space_sizes: List[int]) -> List[int]:
    """Create block representation where each element represents file ID or -1 for space."""
    blocks: List[int] = []
    for file_id, (file_size, space_size) in enumerate(zip(file_sizes, space_sizes + [0])):
        blocks.extend([file_id] * file_size)
        blocks.extend([-1] * space_size)
    return blocks


def compact_disk(blocks: List[int]) -> List[int]:
    """Compact the disk by moving files to the left."""
    while True:
        # Find leftmost free space
        left_space = -1
        for i, block in enumerate(blocks):
            if block == -1:
                left_space = i
                break
        if left_space == -1:
            break

        # Find rightmost file block
        right_file = -1
        right_file_id = -1
        for i in range(len(blocks) - 1, -1, -1):
            if blocks[i] != -1:
                right_file = i
                right_file_id = blocks[i]
                break
        if right_file == -1 or right_file < left_space:
            break

        # Move file block
        blocks[left_space] = right_file_id
        blocks[right_file] = -1

    return blocks


def calculate_checksum(blocks: List[int]) -> int:
    """Calculate filesystem checksum."""
    return sum(pos * file_id for pos, file_id in enumerate(blocks) if file_id != -1)


def calculate_disk_checksum(disk_map: str) -> int:
    """Calculate the disk checksum after compacting."""
    file_sizes, space_sizes = parse_disk_map(disk_map)
    blocks = create_block_representation(file_sizes, space_sizes)
    compacted_blocks = compact_disk(blocks)
    return calculate_checksum(compacted_blocks)


def solution() -> int:
    """Read disk map from stdin and return the checksum."""
    disk_map = sys.stdin.readline().strip()
    return calculate_disk_checksum(disk_map)