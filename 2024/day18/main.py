size = None
corrupted = None
corrupted_length = None
grid = None

def parse_data(data):
    global corrupted, size, corrupted_length
    corrupted = [[*map(int, line.split(","))] for line in data]
    size = 71
    corrupted_length = 1024

    if len(corrupted) == 25:  # test input
        size = 7
        corrupted_length = 12

    set_grid()

def set_grid():
    global grid
    grid = [["."] * size for _ in range(size)]
    for x, y in corrupted[:corrupted_length]:
        grid[y][x] = "#"

def add_corrupted(cx, cy):
    global grid
    if grid is not None:
        grid[cy][cx] = "#"

def get_shortest_path_steps():
    global grid, size
    start = (0, 0)
    end = (size - 1, size - 1)

    # BFS
    queue = [(start, 0)]  # pos, length
    seen = set()
    while queue:
        pos, length = queue.pop(0)
        if pos == end:
            return length
        if pos in seen:
            continue
        seen.add(pos)
        x, y = pos
        for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < size and 0 <= ny < size and grid[ny][nx] == ".":
                queue.append(((nx, ny), length + 1))
    return -1  # no path

def part1(data):
    global corrupted_length
    corrupted_length = 1024  # default value
    parse_data(data)
    return get_shortest_path_steps()

def part2(data):
    global corrupted_length
    corrupted_length = 1024  # default value
    parse_data(data)

    start = corrupted_length
    end = len(corrupted)

    while end - start > 1:
        mid = (start + end) // 2
        corrupted_length = mid
        set_grid()
        steps = get_shortest_path_steps()
        if steps == -1:
            end = mid
        else:
            start = mid

    return f"{corrupted[end-1][0]},{corrupted[end-1][1]}"

def main():
    # Reading data from a text file
    with open('input.txt', 'r') as file:
        data = file.readlines()

    # Removing newline characters from each line
    data = [line.strip() for line in data]

    # Part 1
    result_part1 = part1(data)
    print(f"Part 1 result: {result_part1}")

    # Part 2
    result_part2 = part2(data)
    print(f"Part 2 result: {result_part2}")

if __name__ == "__main__":
    main()
