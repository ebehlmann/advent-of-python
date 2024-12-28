from math import floor
import numpy as np


def process_input(filename):
    claws = []
    current_claw = {}
    with open(filename) as puzzle_input:
        for line in puzzle_input:
            if "Button A" in line:
                parts = line.strip().replace('Button A: ', '').split(', ')
                current_claw['a_x'] = int(parts[0].replace('X+', ''))
                current_claw['a_y'] = int(parts[1].replace('Y+', ''))
            elif "Button B" in line:
                parts = line.strip().replace('Button B: ', '').split(', ')
                current_claw['b_x'] = int(parts[0].replace('X+', ''))
                current_claw['b_y'] = int(parts[1].replace('Y+', ''))
            elif "Prize" in line:
                parts = line.strip().replace('Prize: ', '').split(', ')
                current_claw['target_x'] = int(parts[0].replace('X=', ''))
                current_claw['target_y'] = int(parts[1].replace('Y=', ''))
                claws.append(current_claw)
                current_claw = {}
    return claws


def get_successes_point(a_x, a_y, b_x, b_y, target_x, target_y):
    claw = np.array([[a_x, b_x], [a_y, b_y]])
    target = np.array([target_x, target_y])
    result = np.linalg.solve(claw, target)
    a, b = list(np.round(result, 4))
    if a >= 0 and a % 1 == 0 and b >= 0 and b % 1 == 0:
        return int(a), int(b)
    return None, None


def simulate_claws(claws, convert_target=False):
    tokens = 0
    for claw in claws:
        if convert_target:
            claw['target_x'] += 10000000000000
            claw['target_y'] += 10000000000000
        a, b = get_successes_point(claw['a_x'], claw['a_y'], claw['b_x'], claw['b_y'], claw['target_x'], claw['target_y'])
        if a and b:
            tokens += a * 3 + b
    return tokens


input_claws = process_input('input.txt')
print(f'Part 1: {simulate_claws(input_claws)}')
print(f'Part 2: {simulate_claws(input_claws, True)}')
