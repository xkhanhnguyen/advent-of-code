def neighbor_count(r, c, height, width, grid) -> int:
    cnt = 0
    for ro in (-1, 0, 1):
        for co in (-1, 0, 1):
            if ro == 0 and co == 0:
                continue
            rr = r + ro
            cc = c + co
            if 0 <= rr < height and 0 <= cc < width and grid[rr][cc] == '@':
                cnt += 1
    return cnt


def result(filename) -> int:
    with open(filename) as file:
        lines = file.read().strip().splitlines()

    height = len(lines)
    width = len(lines[0]) if height else 0
    grid = [list(line) for line in lines]

    part1 = 0
    for r in range(height):
        for c in range(width):
            if grid[r][c] == '@':
                if neighbor_count(r, c, height, width, grid) < 4:
                    part1 += 1

    part2 = 0
    while True:
        to_remove = []
        for r in range(height):
            for c in range(width):
                if grid[r][c] == '@':
                    if neighbor_count(r, c, height, width, grid) < 4:
                        to_remove.append((r, c))

        if not to_remove:
            break

        for r, c in to_remove:
            grid[r][c] = '.'

        part2 += len(to_remove)

    return part1, part2


if __name__ == "__main__":
    print('answer sample', result('example.txt'))
    print('answer', result('input.txt'))
