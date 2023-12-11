from copy import deepcopy as dp


def read_data(file_path):
    with open(file_path) as f:
        return [line.strip('\n') for line in f.readlines()]

def extract_columns(data):
    cols = []
    for item in data:
        cols.append(item)
        if "#" not in item:
            cols.append(item)
    return list(zip(*cols))

def find_hash_positions(matrix):
    positions = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "#":
                positions.add((i, j))
    return list(positions)

def calculate_distance_sum(positions):
    counts = 0
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            counts += abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1])
    return counts

def part1(data):
    cols_matrix = extract_columns(data)
    rows_matrix = dp(cols_matrix)
    cols_matrix = extract_columns(rows_matrix)
    positions = find_hash_positions(cols_matrix)
    return calculate_distance_sum(positions)

# Part 2
def find_rows_without_hash(grid):
    return [i for i in range(len(grid)) if "#" not in grid[i]]

def find_columns_without_hash(grid):
    return [r for r in range(len(grid[0])) if all(grid[i][r] != "#" for i in range(len(grid)))]

def calculate_positions(grid, rows_without_hash, columns_without_hash):
    positions = set()
    row_offset = 0
    column_offset = 0

    for i in range(len(grid)):
        if i in rows_without_hash:
            row_offset += 1000000
            row_offset -= 1
        column_offset = 0
        for r in range(len(grid[0])):
            if r in columns_without_hash:
                column_offset += 1000000
                column_offset -= 1
            if grid[i][r] == "#":
                positions.add((i + row_offset, r + column_offset))

    return list(positions)


def part2(data):
    rows_without_hash = find_rows_without_hash(data)
    columns_without_hash = find_columns_without_hash(data)

    print("Rows without '#':", rows_without_hash)
    print("Columns without '#':", columns_without_hash)

    positions = calculate_positions(data, rows_without_hash, columns_without_hash)
    
    return calculate_distance_sum(positions)


if __name__ == "__main__":
    file_path = "input.txt"
    data = read_data(file_path)
    print('Part 1:', part1(data))
    print('Part 2:', part2(data))
