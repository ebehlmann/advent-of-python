def get_max_joltage(bank, digits):
    batteries = [int(x) for x in bank]
    result = []
    while True:
        offset = digits - len(result) - 1
        next_battery = max(batteries[:-offset]) if offset > 0 else max(batteries)
        result.append(next_battery)
        if len(result) == digits:
            break
        pos = batteries[:-(digits-len(result))].index(next_battery)
        batteries = batteries[pos+1:]
    return int(''.join([str(x) for x in result]))


def get_total_joltage(filename, digits):
    total = 0
    with open(filename, 'r') as puzzle_input:
        for bank in puzzle_input:
            total += get_max_joltage(bank.strip(), digits)
    return total


print(f"Part 1: {get_total_joltage('input.txt', 2)}")
print(f"Part 2: {get_total_joltage('input.txt', 12)}")
