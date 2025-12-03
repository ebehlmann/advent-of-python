import math


def turn_dial(dial, current, direction, clicks):
    if direction == "R":
        position = dial[(current + clicks) % len(dial)]
        passed_zero = current != 0 and clicks >= (len(dial) - current)
    elif direction == "L":
        position = dial[(current - clicks) % len(dial)]
        passed_zero = current != 0 and clicks >= current
    else:
        return dial[current], False
    return position, passed_zero


def get_password(max_clicks, starting_pos, filename, count_passes=False):
    dial = [x for x in range(max_clicks)]
    result = 1 if starting_pos == 0 else 0
    pos = starting_pos
    with open(filename, 'r') as puzzle_input:
        for line in puzzle_input:
            direction = line[0]
            total_clicks = int(line[1:].strip())
            if count_passes:
                result += math.floor(total_clicks / max_clicks)
            pos, passed_zero = turn_dial(dial, pos, direction, total_clicks % max_clicks)

            if count_passes:
                result += 1 if passed_zero else 0
            else:
                result += 1 if pos == 0 else 0
    return result


print(f"Part 1: {get_password(100, 50, 'input.txt')}")
print(f"Part 1: {get_password(100, 50, 'input.txt', True)}")
