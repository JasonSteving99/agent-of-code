"""Solution for Disk Fragmenter problem - Part 2."""
from dataclasses import dataclass
from typing import List, Tuple, Optional
import sys


@dataclass
class File:
    """Representation of a file on disk."""
    id: int
    size: int
    start_pos: int


def parse_disk_map(disk_map: str) -> Tuple[List[int], List[int]]:
    """Parse disk map into file and space sizes."""
    file_sizes = [int(disk_map[i]) for i in range(0, len(disk_map), 2)]
    space_sizes = [int(disk_map[i]) for i in range(1, len(disk_map), 2)]
    return file_sizes, space_sizes


def create_blocks_and_files(file_sizes: List[int], space_sizes: List[int]) -> Tuple[List[int], List[File]]:
    """Create block representation and file objects."""
    blocks: List[int] = []
    files: List[File] = []
    current_pos = 0
    
    for file_id, (file_size, space_size) in enumerate(zip(file_sizes, space_sizes + [0])):
        files.append(File(id=file_id, size=file_size, start_pos=current_pos))
        blocks.extend([file_id] * file_size)
        blocks.extend([-1] * space_size)
        current_pos += file_size + space_size
        
    return blocks, files


def find_leftmost_space(blocks: List[int], size_needed: int) -> Optional[int]:
    """Find the leftmost contiguous space that can fit the file."""
    current_size = 0
    start_pos = -1
    
    for i, block in enumerate(blocks):
        if block == -1:
            if start_pos == -1:
                start_pos = i
            current_size += 1
            if current_size >= size_needed:
                return start_pos
        else:
            current_size = 0
            start_pos = -1
            
    return None


def move_file(blocks: List[int], file: File, new_pos: int) -> None:
    """Move an entire file from its current position to a new position."""
    # Clear old position
    for i in range(file.start_pos, file.start_pos + file.size):
        blocks[i] = -1
    
    # Place file in new position
    for i in range(new_pos, new_pos + file.size):
        blocks[i] = file.id


def compact_disk(blocks: List[int], files: List[File]) -> List[int]:
    """Compact the disk by moving whole files from highest to lowest ID."""
    # Sort files by ID in descending order
    sorted_files = sorted(files, key=lambda x: x.id, reverse=True)
    
    for file in sorted_files:
        # Find if the file can be moved to a leftmost position
        target_pos = find_leftmost_space(blocks, file.size)
        
        if target_pos is not None and target_pos < file.start_pos:
            move_file(blocks, file, target_pos)
            
    return blocks


def calculate_checksum(blocks: List[int]) -> int:
    """Calculate filesystem checksum."""
    return sum(pos * file_id for pos, file_id in enumerate(blocks) if file_id != -1)


def compact_disk_and_calculate_checksum(disk_map: str) -> int:
    """Calculate the disk checksum after compacting using whole file movement."""
    file_sizes, space_sizes = parse_disk_map(disk_map)
    blocks, files = create_blocks_and_files(file_sizes, space_sizes)
    compacted_blocks = compact_disk(blocks, files)
    return calculate_checksum(compacted_blocks)


def solution() -> int:
    """Read disk map from stdin and return the checksum."""
    disk_map = sys.stdin.readline().strip()
    return compact_disk_and_calculate_checksum(disk_map)