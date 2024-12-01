def process_input(filename):
    list1 = []
    list2 = []
    with open(filename, 'r') as puzzle_input:
        for line in puzzle_input:
            parts = line.split('   ')
            if len(parts) == 2:
                list1.append(int(parts[0]))
                list2.append(int(parts[1]))
    return list1, list2


def calculate_difference(list1, list2):
    list1.sort()
    list2.sort()
    diff = 0
    for x in range(len(list1)):
        diff += abs(list1[x] - list2[x])
    return diff


def calculate_similarity_score(list1, list2):
    score = 0
    for x in list1:
        matches = [y for y in list2 if y == x]
        score += x * len(matches)
    return score


sites1, sites2 = process_input('input.txt')
print(f'Part 1: {calculate_difference(sites1, sites2)}')
print(f'Part 2: {calculate_similarity_score(sites1, sites2)}')
