def process_input(filename):
    layout = []
    moves = ''
    with open(filename) as puzzle_input:
        for row in puzzle_input:
            if row[0] == '#':
                layout.append(list(row.strip()))
            elif row[0] in ['<', '>', '^', 'v']:
                moves += row.strip()
    return layout, moves


def shift_boxes(row):
    robot = row.index('@')
    try:
        free_space = row[robot:].index('.')
        wall = row[robot:].index('#')
        if free_space < wall:
            return row[:robot] + ['.'] + row[robot:robot+free_space] + row[robot+free_space + 1:]
        return row
    except ValueError:
        return row


def transpose_layout(layout):
    return list(map(list, zip(*layout)))


def find_robot_row(layout):
    for i in range(len(layout)):
        if '@' in layout[i]:
            return i


def plot_move(layout, move):
    if move == '>':
        row_index = find_robot_row(layout)
        shifted = shift_boxes(layout[row_index])
        layout[row_index] = shifted
    elif move == '<':
        row_index = find_robot_row(layout)
        shifted = shift_boxes(layout[row_index][::-1])
        layout[row_index] = shifted[::-1]
    elif move == 'v':
        transposed = transpose_layout(layout)
        row_index = find_robot_row(transposed)
        shifted = shift_boxes(transposed[row_index])
        transposed[row_index] = shifted
        layout = transpose_layout(transposed)
    elif move == '^':
        transposed = transpose_layout(layout)
        row_index = find_robot_row(transposed)
        shifted = shift_boxes(transposed[row_index][::-1])
        transposed[row_index] = shifted[::-1]
        layout = transpose_layout(transposed)
    return layout


def get_gps_totals(layout, moves):
    for i in range(len(moves)):
        layout = plot_move(layout, moves[i])
    total = 0
    for y in range(len(layout)):
        for x in range(len(layout[0])):
            if layout[y][x] == 'O':
                total += (100 * y + x)
    return total


input_layout, input_moves = process_input('input.txt')
print(f'Part 1: {get_gps_totals(input_layout, input_moves)}')
