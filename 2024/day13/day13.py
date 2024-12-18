from math import floor


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


def get_successes(a_x, a_y, b_x, b_y, target_x, target_y):
    successes = []
    for a in range(0, 101):
        for b in range(0, 101):
            x = (a * a_x) + (b * b_x)
            y = (a * a_y) + (b * b_y)
            if x == target_x and y == target_y:
                successes.append({'A': a, 'B': b})
            elif x > target_x or y > target_y:
                break
    return successes


def get_successes_no_limits(a_x, a_y, b_x, b_y, target_x, target_y):
    successes = []
    # case of 100% A's and 0 B's
    if target_x % a_x == 0 and target_y % a_y == 0 and (target_x/a_x) == (target_y/a_y):
        successes.append({'A': floor(target_x / a_x), 'B': 0})


def simulate_claws(claws):
    tokens = 0
    for claw in claws:
        successes = get_successes(claw['a_x'], claw['a_y'], claw['b_x'], claw['b_y'], claw['target_x'], claw['target_y'])
        if len(successes) > 0:
            min_tokens = 400
            for success in successes:
                price = (success['A'] * 3) + success['B']
                if price < min_tokens:
                    min_tokens = price
            tokens += min_tokens
    return tokens


input_claws = process_input('input.txt')
print(f'Part 1: {simulate_claws(input_claws)}')
