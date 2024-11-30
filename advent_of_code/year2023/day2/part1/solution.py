from typing import List

def is_game_possible(input: str) -> str:
    game_id_str, rounds_str = input.split(':')
    game_id = int(game_id_str.split()[1])
    rounds = rounds_str.split(';')
    for round in rounds:
        red = 0
        green = 0
        blue = 0
        cubes = round.split(',')
        for cube in cubes:
            count, color = cube.strip().split()
            count = int(count)
            if color == 'red':
                red = count
            elif color == 'green':
                green = count
            elif color == 'blue':
                blue = count
        if red > 12 or green > 13 or blue > 14:
            return ''
    return str(game_id)

def solution() -> int:
    total = 0
    while True:
        try:
            line = input()
            result = is_game_possible(line)
            if result:
                total += int(result)
        except EOFError:
            break
    return total