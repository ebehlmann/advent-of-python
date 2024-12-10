def create_map_list(diskmap):
    result = []
    file_id = 0
    for i in range(len(diskmap)):
        if i % 2 == 0:
            result += [file_id for x in range(int(diskmap[i]))]
            file_id += 1
        else:
            result += ['.' for x in range(int(diskmap[i]))]
    return result


def is_freespace_maxed(diskmap):
    first_free = diskmap.index('.')
    total_free = diskmap.count('.')
    len_to_end = len(diskmap[first_free:])
    if len(diskmap[first_free:]) == total_free:
        return True
    return False


def maximize_free_space(diskmap):
    while not is_freespace_maxed(diskmap):
        current_id = [x for x in diskmap if x != '.'][-1]
        last_appearance = len(diskmap) - 1 - diskmap[::-1].index(current_id)
        destination = diskmap.index('.')
        diskmap[destination] = current_id
        diskmap[last_appearance] = '.'
    return diskmap


def calculate_checksum(blocks):
    total = 0
    for i in range(len(blocks)):
        if blocks[i] != '.':
            total += i * int(blocks[i])
    return total


def get_maximized_checksum(filename):
    with open(filename) as puzzle_input:
        data = puzzle_input.read()
    diskmap = create_map_list(data)
    maximized_diskmap = maximize_free_space(diskmap)
    checksum = calculate_checksum(maximized_diskmap)
    return checksum


print(f'Part 1: {get_maximized_checksum("input.txt")}')
