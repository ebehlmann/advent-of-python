def process_input(filename):
    result = []
    with open(filename) as puzzle_input:
        for row in puzzle_input:
            result.append([int(x) for x in row.strip()])
    return result


def score_trailhead(trailhead, topo_map):
    endpoints = []
    to_check = [trailhead]
    paths = []
    while len(to_check) > 0:
        location = to_check.pop()
        level = topo_map[location[1]][location[0]]
        surrounds = [[location[0], location[1] + 1],
                     [location[0], location[1] - 1],
                     [location[0] + 1, location[1]],
                     [location[0] - 1, location[1]]]
        for i in surrounds:
            if 0 <= i[0] < len(topo_map[0]) and 0 <= i[1] < len(topo_map):
                if topo_map[i[1]][i[0]] == level + 1:
                    if level == 0:
                        paths.append([location, i])
                    else:
                        for x in range(len(paths)):
                            if len(paths[x]) > level and paths[x][level] == location:
                                if len(paths[x]) == level + 1:
                                    paths[x].append(i)
                                elif paths[x][level + 1] != i:
                                    to_add = paths[x].copy()[:level + 1] + [i]
                                    if to_add not in paths:
                                        paths.append(to_add)
                    if topo_map[i[1]][i[0]] == 9 and i not in endpoints:
                        endpoints.append(i)
                    else:
                        to_check.append(i)
    full_paths = []
    for x in paths:
        if len(x) == 10 and x not in full_paths:
            full_paths.append(x)
    return len(endpoints), len(full_paths)


def get_scores(topo_map):
    total_score = 0
    total_rating = 0
    for y in range(len(topo_map)):
        for x in range(len(topo_map[0])):
            if topo_map[y][x] == 0:
                score, rating = score_trailhead([x, y], topo_map)
                total_score += score
                total_rating += rating
    return total_score, total_rating


input_map = process_input('input.txt')
result_score, result_rating = get_scores(input_map)
print(f'Part 1: {result_score}')
print(f'Part 2: {result_rating}')
