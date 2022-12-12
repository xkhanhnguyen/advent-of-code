import string
from collections import deque

char_to_int = {c: i for i, c in enumerate(string.ascii_lowercase)}
# print(char_to_int)
coordinates = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def get_data(filename):
    with open(filename) as f:
        grid = [l.strip() for l in f.readlines()]
    return grid


def can_move(grid, row_idx, col_idx, current_value):
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


def find_all_low_positions(grid):
    for row_idx, l in enumerate(grid):
        for col_idx, c in enumerate(l):
            if c == "S" or c == "a":
                yield (row_idx, col_idx)


def find_shortest_path(grid, start_positions):
    queue: deque[tuple[tuple[int, int], int]] = deque((p, 0) for p in start_positions)
    seen: set[tuple[int, int]] = set(start_positions)

    while queue:
        (current_row, current_col), current_step_count = queue.popleft()

        current_value = grid[current_row][current_col]

        if current_value == "E":
            print(current_step_count)
            return

        for offset_row, offset_col in coordinates:
            new_coord = (current_row + offset_row, current_col + offset_col)

            if new_coord not in seen and can_move(
                grid, new_coord[0], new_coord[1], current_value
            ):
                seen.add(new_coord)
                queue.append((new_coord, current_step_count + 1))

    print("No path to destination")


def part_one(grid):
    start_positions = [(ix,iy) for ix, row in enumerate(grid) for iy, i in enumerate(row) if i == 'S']
    find_shortest_path(grid, start_positions)


def part_two(grid):
    start_positions = list(find_all_low_positions(grid))
    find_shortest_path(grid, start_positions)


def main():
    grid = get_data('testing.txt')

    part_one(grid)
    part_two(grid)


if __name__ == "__main__":
    main()