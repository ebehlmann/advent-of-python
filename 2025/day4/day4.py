def process_input(filename):
    result = []
    with open (filename, 'r') as diagram:
        for row in diagram:
            result.append([x for x in row.strip()])
    return result


def count_surrounding_rolls(diagram, current_x, current_y):
    result = 0
    for x in range(max(0, current_x-1), min(len(diagram[0]), current_x+2)):
        for y in range(max(0, current_y-1), min(len(diagram), current_y+2)):
            if diagram[y][x] == '@' and (x != current_x or y != current_y):
                result += 1
    return result


def remove_rolls_round(diagram):
    removals = 0
    new_diagram = []
    for y in range(len(diagram)):
        new_row = []
        for x in range(len(diagram[0])):
            if diagram[y][x] == '@' and count_surrounding_rolls(diagram, x, y) < 4:
                removals += 1
                new_row.append('.')
            else:
                new_row.append(diagram[y][x])
        new_diagram.append(new_row)
    return new_diagram, removals


def remove_rolls(filename):
    diagram = process_input(filename)
    removals_per_round = []
    while True:
        diagram, removals = remove_rolls_round(diagram)
        if removals == 0:
            break
        removals_per_round.append(removals)
    return removals_per_round


roll_removal_result = remove_rolls('input.txt')
print(f"Part 1: {roll_removal_result[0]}")
print(f"Part 2: {sum(roll_removal_result)}")
