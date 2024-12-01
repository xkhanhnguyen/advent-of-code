def find_column_reflection(grid, c, p2):
    COL = len(grid[0])

    l = min(c, COL - c)
    errors = 0

    for r in range(len(grid)):
        for i in range(l):
            cl = c - 1 - i
            cr = c + i
            if not grid[r][cl] == grid[r][cr]:
                errors += 1

    return errors == (1 if p2 else 0)


def find_row_reflection(grid, r, p2):
    ROW = len(grid)
    errors = 0

    l = min(r, ROW - r)
    for c in range(len(grid[0])):
        for i in range(l):
            rl = r - 1 - i
            rr = r + i
            if not grid[rl][c] == grid[rr][c]:
                errors += 1

    return errors == (1 if p2 else 0)


def find_reflections(grid, p2=False):
    for c in range(1, len(grid[0])):
        if find_column_reflection(grid, c, p2):
            return c

    for r in range(1, len(grid)):
        if find_row_reflection(grid, r, p2):
            return r * 100

    return 0


def get_data(file, p2=False):
    with open(file, 'r') as fp:
        blocks = [block for block in fp.read().split("\n\n")]

    total_reflection = 0
    for block in blocks:
        grid = [[char for char in line] for line in block.splitlines()]
        total_reflection += find_reflections(grid, p2)

    return total_reflection


# Part 1
print("Part 1 (test): ", get_data('example.txt'))
print("Part 1: ", get_data('input.txt'))
print("\n\n")
# Part 2
print("Part 2 (test): ", get_data('example.txt', True))
print("Part 2: ", get_data('input.txt', True))



