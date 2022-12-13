import string
from collections import deque


def get_data(filename):
    with open(filename) as f:
        grid = [l.strip() for l in f.readlines()]
    return grid


def can_move(grid, row_idx, col_idx, current_value):
    char_to_int = {c: i for i, c in enumerate(string.ascii_lowercase)}
    # out of range
    if (
        row_idx < 0
        or col_idx < 0
        or row_idx >= len(grid)
        or col_idx >= len(grid[0])
    ):
        return False

    if current_value == "S":
        current_value = "a"

    location = grid[row_idx][col_idx]

    if location == "E":
        location = "z"


    return char_to_int[location] <= char_to_int[current_value] + 1


# def find_all_low_positions(grid):
#     for row_idx, l in enumerate(grid):
#         for col_idx, c in enumerate(l):
#             if c == "S" or c == "a":
#                 yield (row_idx, col_idx)


def find_shortest_path(grid, start_positions):
    
    # print(char_to_int)
    
    # 'R': (1, 0),
    # 'L': (-1, 0),
    # 'U': (0, 1),
    # 'D': (0, -1)
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque((p, 0) for p in start_positions) # deque[tuple[tuple[(curr_row, curr_col], current_step_count]]
    # print(queue)
    # seen to keep track of which letter we have passes before
    visited = set(start_positions) # set[tuple[int, int]]

    while queue: # while the queuq isn't empty 
        (curr_row, curr_col), current_step_count = queue.popleft() # grab the first letter of the queue
        # print(curr_row, curr_col)
        current_value = grid[curr_row][curr_col]
        # print(current_value, curr_row, curr_col)
        if current_value == 'E': # check if the letter = 'E'
            print(current_step_count)
            return True

        for x ,y  in move:
            update_position = (curr_row + x, curr_col + y)
            print(update_position)
            # only updatethe new position, of we have never seen it before
            # new_coord[0] = row_idx
            # new_coord[1] = col_idx
            if update_position not in visited and can_move(grid, update_position[0], update_position[1], current_value):
                visited.add(update_position)
                queue.append((update_position, current_step_count + 1)) # mark the position as visited

    print("No path to destination")
    return False


def part_one(grid):
    start_positions = [(ix,iy) for ix, row in enumerate(grid) for iy, i in enumerate(row) if i == 'S']
    find_shortest_path(grid, start_positions)


def part_two(grid):
#     start_positions = list(find_all_low_positions(grid))
#     find_shortest_path(grid, start_positions)
    return 0

def main():
    grid = get_data('testing.txt')

    part_one(grid)
    part_two(grid)


if __name__ == "__main__":
    main()