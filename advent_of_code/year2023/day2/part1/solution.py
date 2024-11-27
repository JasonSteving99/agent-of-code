from typing import List

def is_game_possible(game_str: str) -> str:
    game_id_str, reveals_str = game_str.split(':')
    game_id = int(game_id_str.split()[1])
    reveals = reveals_str.split(';')
    for reveal in reveals:
        counts = {"red": 0, "green": 0, "blue": 0}
        for cube_count in reveal.split(','):
            count, color = cube_count.strip().split()
            counts[color] = int(count)
        if counts["red"] > 12 or counts["green"] > 13 or counts["blue"] > 14:
            return ""
    return str(game_id)

def solution() -> str:
    total = 0
    while True:
        try:
            line = input()
            result = is_game_possible(line)
            if result:
                total += int(result)
        except EOFError:
            break
    return str(total)

