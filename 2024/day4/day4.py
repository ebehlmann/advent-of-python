def process_input(filename):
    with open(filename, 'r') as puzzle_input:
        lines = [line.rstrip() for line in puzzle_input]
    return lines


def get_diagonals(lines):
    diagonals = []
    for i in range(len(lines[0])):
        y = i
        x = 0
        line = ''
        while y >= 0:
            line += lines[x][y]
            y -= 1
            x += 1
        diagonals.append(line)
    for i in range(1, len(lines)):
        x = i
        y = len(lines[0]) - 1
        line = ''
        while x < len(lines):
            line += lines[x][y]
            y -= 1
            x += 1
        diagonals.append(line)
    return diagonals


def transpose(lines):
    return [''.join(list(row)) for row in zip(*lines)]


def reverse(lines):
    return [row[::-1] for row in lines]


def count_instances(target_word, lines):
    total = 0
    for line in lines:
        total += line.count(target_word)
        total += line.count(target_word[::-1])
    return total


def count_words(target_word, lines):
    total = 0
    total += count_instances(target_word, lines)
    total += count_instances(target_word, transpose(lines))
    total += count_instances(target_word, get_diagonals(lines))
    total += count_instances(target_word, get_diagonals(reverse(lines)))
    return total


def count_x_mas(lines):
    count = 0
    for x in range(1, len(lines)-1):
        for y in range(1, len(lines[0])-1):
            if lines[x][y] == 'A':
                if lines[x-1][y-1] + lines[x+1][y+1] in ['MS', 'SM']:
                    if lines[x-1][y+1] + lines[x+1][y-1] in ['MS', 'SM']:
                        count += 1
    return count


puzzle = process_input('input.txt')
print(f'Part 1: {count_words("XMAS", puzzle)}')
print(f'Part 2: {count_x_mas(puzzle)}')
