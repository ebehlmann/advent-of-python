def process_input(filename):
    grid = []
    guard = None
    with open(filename) as puzzle_input:
        for row in puzzle_input:
            grid.append(row.strip())
            pos = row.find('^')
            if pos > -1:
                guard = [pos, len(grid) - 1]
    return grid, guard


def get_next_pos(current_pos, direction):
    if direction == 'N':
        return [current_pos[0], current_pos[1] - 1]
    elif direction == 'S':
        return [current_pos[0], current_pos[1] + 1]
    elif direction == 'E':
        return [current_pos[0] + 1, current_pos[1]]
    elif direction == 'W':
        return [current_pos[0] - 1, current_pos[1]]


def map_guard_route(grid, pos, direction):
    next_dirs = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    visited = [pos]
    while True:
        next_pos = get_next_pos(pos, direction)
        if next_pos[0] < 0 or next_pos[0] >= len(grid[0]) or next_pos[1] < 0 or next_pos[1] >= len(grid):
            break
        elif grid[next_pos[1]][next_pos[0]] == '#':
            direction = next_dirs[direction]
        else:
            if next_pos not in visited:
                visited.append(next_pos)
            pos = next_pos
    return len(visited)


grid_layout, guard_pos = process_input('input.txt')
print(f'Part 1: {map_guard_route(grid_layout, guard_pos, "N")}')