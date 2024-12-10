from itertools import combinations


def map_antennas(filename):
    city_map = []
    frequencies = {}
    with open(filename) as puzzle_input:
        for line in puzzle_input:
            for x in range(len(line.strip())):
                if line[x] != '.':
                    if line[x] in frequencies:
                        frequencies[line[x]].append([x, len(city_map)])
                    else:
                        frequencies[line[x]] = [[x, len(city_map)]]
            city_map.append(line.strip())
    return city_map, frequencies


def is_on_map(x, y, city_map):
    if x < 0 or y < 0 or x >= len(city_map[0]) or y >= len(city_map):
        return False
    return True


def get_antinodes_for_pair(ant1, ant2):
    node1 = [ant1[0] + (ant1[0] - ant2[0]), ant1[1] + (ant1[1] - ant2[1])]
    node2 = [ant2[0] + (ant2[0] - ant1[0]), ant2[1] + (ant2[1] - ant1[1])]
    return [node1, node2]


def get_antinode_count(frequencies, city_map):
    antinodes = []
    for frequency, locs in frequencies.items():
        pairs = combinations(locs, 2)
        for pair in pairs:
            nodes = get_antinodes_for_pair(pair[0], pair[1])
            for node in nodes:
                if is_on_map(node[0], node[1], city_map) and node not in antinodes:
                    antinodes.append(node)
    return len(antinodes)


input_map, input_frequencies = map_antennas('input.txt')
print(f'Part 1: {get_antinode_count(input_frequencies, input_map)}')
