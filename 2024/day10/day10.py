def process_input(filename):
    result = []
    with open(filename) as puzzle_input:
        for row in puzzle_input:
            result.append([int(x) for x in row.strip()])
    return result


def score_trailhead(trailhead, topo_map):
    endpoints = []
    to_check = [trailhead]
    while len(to_check) > 0:
        location = to_check.pop()
        level = topo_map[location[1]][location[0]]
        surrounds = [[location[0], location[1] + 1],
                     [location[0], location[1] - 1],
                     [location[0] + 1, location[1]],
                     [location[0] - 1, location[1]]]
        for i in surrounds:
            if 0 <= i[0] < len(topo_map[0]) and 0 <= i[1] < len(topo_map):
                if level == 8 and topo_map[i[1]][i[0]] == 9 and i not in endpoints:
                    endpoints.append(i)
                elif topo_map[i[1]][i[0]] == level + 1:
                    to_check.append(i)
    return len(endpoints)


def get_scores(topo_map):
    total = 0
    for y in range(len(topo_map)):
        for x in range(len(topo_map[0])):
            if topo_map[y][x] == 0:
                score = score_trailhead([x, y], topo_map)
                total += score
    return total


input_map = process_input('input.txt')
print(f'Part 1: {get_scores(input_map)}')
