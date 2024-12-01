def get_data(filename):
    with open(filename) as f:
        data = [l.strip() for l in f.readlines()]
    grid = [[int(x) for x in list(line)] for line in data]
    return grid

def is_visible(row_idx, col_idx, grid):
    if row_idx == 0 or row_idx == len(grid) - 1:
        return True
    if col_idx == 0 or col_idx == len(grid[row_idx]) - 1:
        return True
    
    height = grid[row_idx][col_idx]
    row = grid[row_idx]
    col = [grid[row_idx][col_idx] for row_idx in range(len(grid))]

    left = all(x < height for x in row[:col_idx])
    right = all(x < height for x in row[col_idx + 1:])
    up = all(x < height for x in col[:row_idx])
    down = all(x < height for x in col[row_idx + 1:])

    
    return left or right or up or down


def get_score (row_idx, col_idx, grid):
    height = grid[row_idx][col_idx]
    row = grid[row_idx]
    col = [grid[row_idx][col_idx] for row_idx in range(len(grid))]

    left, right, up, down = 0, 0, 0, 0

    # check left
    for x in reversed(row[:col_idx]):
        left += 1
        if x >= height:
            break
    
    # check right
    for x in row[col_idx+1:]:
        right += 1
        if x >= height:
            break
    
    # check up
    for x in reversed(col[:row_idx]):
        up += 1
        if x >= height:
            break

    # check down
    for x in col[row_idx+1:]:
        down += 1
        if x >= height:
            break
    
    return left * right * up * down 

def ans(grid):
    part1 = sum([is_visible(row, col, grid)
             for row in range(len(grid))
             for col in range(len(grid[row]))])


    part2 = max([get_score(row, col, grid)
             for row in range(len(grid))
             for col in range(len(grid[row]))])

    return part1, part2

if __name__ == "__main__":
    data = get_data('input.txt')
    print( ans(data))