def create_filesystem(lines, part):
    arr = []
    sizes = []
    locations = []
    is_file = True  # Alternate between file and free space
    block_id = 0

    for length in map(int, lines):
        if is_file:
            if part == 2:
                locations.append(len(arr))  # starting location
                sizes.append(length)  # size of the block
            arr.extend([block_id] * length)  # file arr
            block_id += 1
        else:
            arr.extend([None] * length)  # free space
        is_file = not is_file  # Toggle between file and free space

    if part == 2:
        return arr, sizes, locations
    return arr

def pretty_print(arr):
    print("".join(str(block) if block is not None else "." for block in arr))

def rearrange_arr_part1(arr):
    # Find the first free space and the last file block
    free = 0
    while arr[free] is not None:
        free += 1
                    
    occupied = len(arr) - 1
    while arr[occupied] is None:
        occupied -= 1
    
    # Move arr from the end to fill gaps
    while occupied > free:
        # pretty_print(arr)   
        arr[free], arr[occupied] = arr[occupied], None
        occupied -= 1
        while occupied >= 0 and arr[occupied] is None:
            occupied -= 1
        while free < len(arr) and arr[free] is not None:
            free += 1
    
    return arr


def rearrange_arr_part2(arr, sizes, locations):
    largest_block_idx = len(sizes) - 1
    while sizes[largest_block_idx] <= 0:  # Find the last valid block
        largest_block_idx -= 1

    for block_to_move in range(largest_block_idx, -1, -1):
        # pretty_print(arr)
        current_size = sizes[block_to_move]
        current_location = locations[block_to_move]

        
        free = 0
        free_space = 0

        while free < current_location and free_space < current_size:
            free += free_space
            free_space = 0
            while free < len(arr) and arr[free] is not None:
                free += 1
            while free + free_space < len(arr) and arr[free + free_space] is None:
                free_space += 1

        if free >= current_location:  # No valid free space found
            continue

        
        for i in range(current_size):
            arr[free + i] = block_to_move
            arr[current_location + i] = None
    return arr


def checksum(arr):
    score = 0
    for idx, block in enumerate(arr):
        if block is not None:
            score += idx * block
    return score


def result(filename):
    with open(filename) as file:
        lines = file.read().strip()

    # Part 1
    arr_part1 = create_filesystem(lines, part=1)
    rearranged_part1 = rearrange_arr_part1(arr_part1)
    part1_score = checksum(rearranged_part1)

    # Part 2
    arr_part2, sizes, locations = create_filesystem(lines, part=2)
    rearranged_part2 = rearrange_arr_part2(arr_part2, sizes, locations)
    part2_score = checksum(rearranged_part2)

    return part1_score, part2_score


if __name__ == "__main__":
    print('Answer for example.txt:', result('example.txt'))
    print('Answer for input.txt:', result('input.txt'))
