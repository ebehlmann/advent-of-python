from math import floor


def process_input(filename):
    stones = {}
    with open(filename) as puzzle_input:
        data = puzzle_input.read().split()
        for i in data:
            stones[int(i)] = 1
    return stones


def split_stone(stone):
    stone_string = str(stone)
    midpoint = floor(len(stone_string) / 2)
    return [int(stone_string[:midpoint]), int(stone_string[midpoint:])]


def transform_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        return split_stone(stone)
    else:
        return [stone * 2024]


def blink(stones):
    new_row = {}
    for stone, count in stones.items():
        new_values = transform_stone(stone)
        for i in new_values:
            if i in new_row:
                new_row[i] += count
            else:
                new_row[i] = count
    return new_row


def blinks(stones, blink_count):
    for x in range(blink_count):
        stones = blink(stones)
    return sum(stones.values())


input_stones = process_input('input.txt')
print(f'Part 1: {blinks(input_stones, 25)}')
print(f'Part 2: {blinks(input_stones, 75)}')
