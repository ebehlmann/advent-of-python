def process_input(filename):
    with open(filename) as puzzle_input:
        data = puzzle_input.read()
    result = []
    file_id = 0
    for i in range(len(data)):
        if i % 2 == 0:
            result += [file_id for x in range(int(data[i]))]
            file_id += 1
        else:
            result += ['.' for x in range(int(data[i]))]
    return result


def is_freespace_maxed(diskmap):
    first_free = diskmap.index('.')
    total_free = diskmap.count('.')
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


def rearrange_files(diskmap):
    file = diskmap[-1]
    while file >= 0:
        original_location = diskmap.index(file)
        block_needed = diskmap.count(file)
        destination = ''.join(['.' if x == '.' else 'x' for x in diskmap_input]).find('.' * block_needed)
        if -1 < destination < original_location:
            for i in range(destination, destination + block_needed):
                diskmap[i] = file
            for j in range(original_location, original_location + block_needed):
                diskmap[j] = '.'
        file -= 1
    return diskmap


def calculate_checksum(blocks):
    total = 0
    for i in range(len(blocks)):
        if blocks[i] != '.':
            total += i * int(blocks[i])
    return total


def get_maximized_checksum(diskmap):
    maximized_diskmap = maximize_free_space(diskmap)
    checksum = calculate_checksum(maximized_diskmap)
    return checksum


def get_rearranged_checksum(diskmap):
    rearranged_diskmap = rearrange_files(diskmap)
    checksum = calculate_checksum(rearranged_diskmap)
    return checksum


diskmap_input = process_input('input.txt')
print(f'Part 1: {get_maximized_checksum(diskmap_input)}')
diskmap_input = process_input('input.txt')
print(f'Part 2: {get_rearranged_checksum(diskmap_input)}')
