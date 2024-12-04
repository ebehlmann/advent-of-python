import re

MULT_PATTERN = r"mul\(\d{1,3},\d{1,3}\)"


def get_valid_instructions(filename):
    with open(filename, 'r') as puzzle_input:
        return re.findall(MULT_PATTERN, puzzle_input.read())


def get_valid_instructions_with_conditionals(filename):
    enable_pattern = r"do\(\)"
    disable_pattern = r"don\'t\(\)"
    enabled_instructions = []
    with open(filename, 'r') as puzzle_input:
        dos = re.split(enable_pattern, puzzle_input.read())
    for do in dos:
        disable_point = re.search(disable_pattern, do)
        if disable_point:
            do = do[:disable_point.start()]
        enabled_instructions += re.findall(MULT_PATTERN, do)
    return enabled_instructions


def process_multiplications(instructions):
    result = 0
    for instruction in instructions:
        instruction = instruction.replace('mul(', '').replace(')', '')
        digits = [int(x) for x in instruction.split(',')]
        result += digits[0] * digits[1]
    return result


valid_instructions = get_valid_instructions('input.txt')
get_valid_instructions_with_conditionals = get_valid_instructions_with_conditionals('input.txt')
print(f'Part 1: {process_multiplications(valid_instructions)}')
print(f'Part 2: {process_multiplications(get_valid_instructions_with_conditionals)}')
