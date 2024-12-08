from itertools import product


def process_input(filename):
    equations = []
    with open(filename) as puzzle_input:
        for line in puzzle_input:
            parts = line.split(':')
            if len(parts) == 2:
                equations.append({
                    'numbers': [int(x) for x in parts[1].strip().split()],
                    'result': int(parts[0].strip())
                })
    return equations


def get_possible_operator_arrangements(count, include_concat=False):
    operators = ['+', '*']
    if include_concat:
        operators.append('||')
    return list(product(operators, repeat=count))


def test_equation(numbers, operators, result):
    total = numbers[0]
    i = 1
    while i < len(numbers):
        if operators[i-1] == '+':
            total += numbers[i]
        elif operators[i-1] == '*':
            total *= numbers[i]
        else:
            total = int(str(total) + str(numbers[i]))
        i += 1
    if total == result:
        return True
    return False


def get_calibration_result(equations, include_concat):
    result = 0
    for equation in equations:
        possible_operators = get_possible_operator_arrangements(len(equation['numbers']) - 1, include_concat)
        for operators in possible_operators:
            if test_equation(equation['numbers'], operators, equation['result']):
                result += equation['result']
                break
    return result


input_equations = process_input('input.txt')
print(f'Part 1: {get_calibration_result(input_equations, False)}')
print(f'Part 2: {get_calibration_result(input_equations, True)}')
