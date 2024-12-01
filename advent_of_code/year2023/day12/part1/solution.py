from typing import List, Dict, Tuple
import sys
import functools

def is_valid_pattern(pattern: str, groups: List[int]) -> bool:
    # Split pattern by '.' and filter empty strings to get damaged groups
    damaged_groups = [len(grp) for grp in pattern.split('.') if grp]
    return damaged_groups == groups


def count_spring_arrangements(springs: str, groups: List[int]) -> int:
    pattern = springs.split()[0]

    @functools.lru_cache(maxsize=None)
    def solve(pidx: int, gidx: int, curr_len: int) -> int:
        # Base case: reached end of pattern
        if pidx == len(pattern):
            # If we've used all groups and no current group in progress
            if gidx == len(groups) and curr_len == 0:
                return 1
            # If we're on the last group and it matches current length
            if gidx == len(groups) - 1 and curr_len == groups[gidx]:
                return 1
            return 0

        result = 0

        for c in ['.', '#']:
            if pattern[pidx] == '?' or pattern[pidx] == c:
                if c == '.':
                    # End current group if exists
                    if curr_len > 0:
                        if gidx < len(groups) and curr_len == groups[gidx]:
                            result += solve(pidx + 1, gidx + 1, 0)
                    else:
                        result += solve(pidx + 1, gidx, 0)
                else:  # c == '#'
                    # Continue or start damaged group
                    if gidx < len(groups) and curr_len + 1 <= groups[gidx]:
                        result += solve(pidx + 1, gidx, curr_len + 1)

        return result

    return solve(0, 0, 0)


def solution() -> int:
    # Read input from stdin
    lines = sys.stdin.read().strip().split('\n')

    # Process each line and sum up the results
    total = 0
    for line in lines:
        parts = line.split()
        springs_pattern = parts[0]
        groups_str = parts[1]
        groups_list = [int(x) for x in groups_str.split(',')]
        total += count_spring_arrangements(springs_pattern, groups_list)

    return total

if __name__ == "__main__":
    print(solution())
