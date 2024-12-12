NEXT_DIRS = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}


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
    visited = [pos]
    while True:
        next_pos = get_next_pos(pos, direction)
        if next_pos[0] < 0 or next_pos[0] >= len(grid[0]) or next_pos[1] < 0 or next_pos[1] >= len(grid):
            break
        elif grid[next_pos[1]][next_pos[0]] == '#':
            direction = NEXT_DIRS[direction]
        else:
            if next_pos not in visited:
                visited.append(next_pos)
            pos = next_pos
    return visited


def is_looped(route):
    visited = route.copy()
    current = visited.pop()
    if current in visited and len(visited) > 1:
        last_occurrence = len(visited) - 1 - visited[::-1].index(current)
        if last_occurrence != 0:
            if visited[-1] == visited[last_occurrence-1]:
                return True
    return False


def test_obstructions(grid, pos, direction, possible_obstructions):
    successful_obstructions = 0
    for obstruction in possible_obstructions:
        if obstruction != pos:
            route = [pos]
            current_pos = pos
            current_direction = direction
            while True:
                next_pos = get_next_pos(current_pos, current_direction)
                if next_pos[0] < 0 or next_pos[0] >= len(grid[0]) or next_pos[1] < 0 or next_pos[1] >= len(grid):
                    break
                elif grid[next_pos[1]][next_pos[0]] == '#' or next_pos == obstruction:
                    current_direction = NEXT_DIRS[current_direction]
                else:
                    current_pos = next_pos
                    route.append(current_pos)
                    if is_looped(route):
                        successful_obstructions += 1
                        break
    return successful_obstructions



grid_layout, guard_pos = process_input('input.txt')
visited = map_guard_route(grid_layout, guard_pos, "N")
print(f'Part 1: {len(visited)}')
print(f'Part 2: {test_obstructions(grid_layout, guard_pos, "N", visited)}')
