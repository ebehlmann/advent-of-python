def process_input(filename):
    result = []
    with open(filename) as puzzle_input:
        for line in puzzle_input:
            result.append(list(line.strip()))
    return result


def get_fence_count(location, farm_map):
    total = 0
    surrounds = [[location[0], location[1] + 1],
                 [location[0], location[1] - 1],
                 [location[0] + 1, location[1]],
                 [location[0] - 1, location[1]]]
    for i in surrounds:
        if 0 <= i[0] < len(farm_map[0]) and 0 <= i[1] < len(farm_map):
            if farm_map[i[1]][i[0]] != farm_map[location[1]][location[0]]:
                total += 1
        else:
            total += 1
    return total


def get_plants_and_locs(farm_map):
    result = {}
    for y in range(len(farm_map)):
        for x in range(len(farm_map[0])):
            plant_type = farm_map[y][x]
            if plant_type in result:
                result[plant_type].append([x, y])
            else:
                result[plant_type] = [[x, y]]
    return result


def split_areas(plant_locs):
    areas = []
    while len(plant_locs) > 0:
        area = [plant_locs.pop()]
        to_check = [area[0]]
        while len(to_check) > 0:
            current_item = to_check.pop()
            to_add = [loc for loc in plant_locs if
                      (current_item[0] == loc[0] and abs(current_item[1]-loc[1]) == 1) or
                      (abs(current_item[0] - loc[0]) == 1 and current_item[1] == loc[1])
                      ]
            if len(to_add) > 0:
                area = area + to_add
                to_check = to_check + to_add
                plant_locs = [loc for loc in plant_locs if loc not in to_add]
        areas.append(area)
    return areas


def get_fence_cost(farm_map):
    cost = 0
    plants = get_plants_and_locs(farm_map)
    for plant, locs in plants.items():
        areas = split_areas(locs)
        for area in areas:
            fencing = 0
            for loc in area:
                fencing += get_fence_count(loc, farm_map)
            cost += len(area) * fencing
    return cost


input_map = process_input('input.txt')
print(f'Part 1: {get_fence_cost(input_map)}')
