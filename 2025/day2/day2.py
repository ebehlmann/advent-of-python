import math


def is_valid_part_1(product_id):
    if len(product_id) % 2 == 0:
        halfway = int(len(product_id) / 2)
        if product_id[0:halfway] == product_id[halfway:]:
            return False
    return True


def is_valid_part_2(product_id):
    for group_size in range(math.floor(len(product_id) / 2), 0, -1):
        if len(product_id) % group_size == 0:
            groups = []
            for i in range(0, len(product_id), group_size):
                groups.append(product_id[i:i + group_size])
            equal_groups = True
            for group in groups:
                if group != groups[0]:
                    equal_groups = False
                    break
            if equal_groups:
                return False
    return True


def process_range(start, end, validity_function):
    invalid = 0
    for i in range(start, end + 1, 1):
        if not validity_function(str(i)):
            invalid += i
    return invalid


def process_input(filename, validity_function):
    result = 0
    with open(filename, 'r') as puzzle_input:
        data = puzzle_input.read()
        ranges = data.split(",")
        for r in ranges:
            range_split = r.strip().split("-")
            result += process_range(int(range_split[0]), int(range_split[1]), validity_function)
    return result


print(f"Part 1: {process_input('input.txt', is_valid_part_1)}")
print(f"Part 2: {process_input('input.txt', is_valid_part_2)}")
