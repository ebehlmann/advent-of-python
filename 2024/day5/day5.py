from math import floor


def process_input(filename):
    rules = []
    updates = []
    with open(filename) as puzzle_input:
        for line in puzzle_input:
            if '|' in line:
                rules.append([int(x) for x in line.strip().split('|')])
            elif ',' in line:
                updates.append([int(x) for x in line.strip().split(',')])
    return rules, updates


def is_valid(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True


def get_middle_page_sum(rules, updates):
    total = 0
    for update in updates:
        if is_valid(update, rules):
            total += update[floor(len(update) / 2)]
    return total


def fix_update(rules, update):
    result = []
    for x in update:
        must_follow = [result.index(y[0]) for y in rules if y[1] == x and y[0] in result]
        if len(must_follow) > 0:
            result.insert(max(must_follow) + 1, x)
        else:
            result.insert(0, x)
    return result


def get_middle_page_sum_fixed(rules, updates):
    total = 0
    for update in updates:
        if not is_valid(update, rules):
            fixed = fix_update(rules, update)
            total += fixed[floor(len(update) / 2)]
    return total


rule_inputs, update_inputs = process_input('input.txt')
print(f'Part 1: {get_middle_page_sum(rule_inputs, update_inputs)}')
print(f'Part 2: {get_middle_page_sum_fixed(rule_inputs, update_inputs)}')
