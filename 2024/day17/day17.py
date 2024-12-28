from math import floor


def process_input(filename):
    data = {}
    with open(filename) as puzzle_input:
        for line in puzzle_input:
            if 'Register' in line:
                register, value = line.strip().replace('Register ', '').split(': ')
                data[register] = int(value)
            elif 'Program' in line:
                data['Program'] = [int(x) for x in line.strip().replace('Program: ', '').split(',')]
    return data


def get_combo_operand(a, b, c, operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    else:
        print("invalid operand")


def execute(a, b, c, program):
    output = []
    i = 0
    while i < len(program) - 1:
        opcode, operand = program[i:i+2]
        combo = get_combo_operand(a, b, c, operand)
        match opcode:
            case 0:
                a = floor(a / (2 ** combo))
            case 1:
                b ^= operand
            case 2:
                b = combo % 8
            case 3:
                if a != 0:
                    i = operand - 2
            case 4:
                b ^= c
            case 5:
                output.append(combo % 8)
            case 6:
                b = floor(a / (2 ** combo))
            case 7:
                c = floor(a / (2 ** combo))
        i += 2
    return ','.join([str(x) for x in output])


input_program = process_input('input.txt')
print(f"Part 1: {execute(input_program['A'], input_program['B'], input_program['C'], input_program['Program'])}")
