from math import floor


def process_input(filename):
    robots = []
    with open(filename) as puzzle_input:
        for line in puzzle_input:
            parts = line.strip().split()
            robot = {
                'loc': [int(x) for x in parts[0].replace('p=', '').split(',')],
                'vel': [int(x) for x in parts[1].replace('v=', '').split(',')]
            }
            robots.append(robot)
    return robots


def simulate_path(robot, moves, len_x, len_y):
    x = (robot['loc'][0] + (moves * robot['vel'][0])) % len_x
    y = (robot['loc'][1] + (moves * robot['vel'][1])) % len_y
    return [x, y]


def get_safety_factor(robots, len_x, len_y):
    x_midpoint = floor(len_x / 2)
    y_midpoint = floor(len_y / 2)
    a = [i for i in robots if i['loc'][0] < x_midpoint and i['loc'][1] < y_midpoint]
    b = [i for i in robots if i['loc'][0] > x_midpoint and i['loc'][1] < y_midpoint]
    c = [i for i in robots if i['loc'][0] < x_midpoint and i['loc'][1] > y_midpoint]
    d = [i for i in robots if i['loc'][0] > x_midpoint and i['loc'][1] > y_midpoint]
    return len(a) * len(b) * len(c) * len(d)


def simulate_robots(robots, moves, len_x, len_y):
    new_locs = []
    for robot in robots:
        new_locs.append({
            'loc': simulate_path(robot, moves, len_x, len_y),
            'vel': robot['vel']
        })
    return new_locs


def plot_robots(robots, len_x, len_y, move_no):
    grid = [['.' for x in range(len_x)] for y in range(len_y)]
    for robot in robots:
        grid[robot['loc'][1]][robot['loc'][0]] = 'X'
    for row in grid:
        if 'XXXXXXXXXX' in ''.join(row):
            print(f'\nMoves: {move_no}')
            print('\n'.join([''.join(row) for row in grid]))
            break


def print_robot_map(robots, len_x, len_y):
    initial_robots = robots
    for move in range(1, 100000):
        robots = simulate_robots(robots, 1, len_x, len_y)
        if robots == initial_robots:
            break
        plot_robots(robots, len_x, len_y, move)


input_robots = process_input('input.txt')
after_100_moves = simulate_robots(input_robots, 100, 11, 7)
print(f'Part 1: {get_safety_factor(after_100_moves, 11, 7)}')
input_robots = process_input('input.txt')
print_robot_map(input_robots, 101, 103)
