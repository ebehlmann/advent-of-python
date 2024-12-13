import time
from math import floor


def process_input(filename):
    with open(filename) as puzzle_input:
        data = puzzle_input.read()
        return [int(x) for x in data.split()]


def split_stone(stone):
    stone_string = str(stone)
    midpoint = floor(len(stone_string) / 2)
    return [int(stone_string[:midpoint]), int(stone_string[midpoint:])]


def transform_stone(stone):
    if stone == 0:
        return 1
    elif len(str(stone)) % 2 == 0:
        return split_stone(stone)
    else:
        return stone * 2024


def blink(stones):
    new_row = []
    for stone in stones:
        new_value = transform_stone(stone)
        if isinstance(new_value, list):
            new_row = new_row + new_value
        else:
            new_row.append(new_value)
    return new_row


def blinks(stones, blink_count):
    for x in range(blink_count):
        start = time.time()
        stones = blink(stones)
        end = time.time()
        print(f"{end - start} for {x}")
    return len(stones)


input_stones = process_input('input.txt')
print(f'Part 1: {blinks(input_stones, 25)}')
