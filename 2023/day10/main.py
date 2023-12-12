from queue import Queue

def read_map(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f]

def find_start_position(grid):
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == "S":
                return x, y

def create_neighbors():
    return {
        "|": [(0, -1), (0, 1)],
        "-": [(-1, 0), (1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(-1, 0), (0, 1)],
        "F": [(1, 0), (0, 1)],
    }

def find_max_distance(grid, start_pos, neighbors):
    q = Queue()
    x, y = start_pos
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        c = grid[y + dy][x + dx]
        if c in neighbors:
            for dx2, dy2 in neighbors[c]:
                if x == x + dx + dx2 and y == y + dy + dy2:
                    q.put((1, (x + dx, y + dy)))

    dists = {(x, y): 0}

    while not q.empty():
        d, (x, y) = q.get()

        if (x, y) in dists:
            continue

        dists[(x, y)] = d

        for dx, dy in neighbors[grid[y][x]]:
            q.put((d + 1, (x + dx, y + dy)))

    return max(dists.values())

def count_inside_regions(grid, dists, width, height):
    inside_count = 0
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if (x, y) in dists:
                continue

            crosses = 0
            x2, y2 = x, y

            while x2 < width and y2 < height:
                c2 = grid[y2][x2]
                if (x2, y2) in dists and c2 != "L" and c2 != "7":
                    crosses += 1
                x2 += 1
                y2 += 1

            if crosses % 2 == 1:
                inside_count += 1

    return inside_count

if __name__ == "__main__":
    file_path = "input.txt"
    m = read_map(file_path)
    neighbors = create_neighbors()
    start_pos = find_start_position(m)

    max_distance = find_max_distance(m, start_pos, neighbors)
    print(f"Part 1: {max_distance}")

    width = len(m[0])
    height = len(m)
    dists = {(start_pos[0], start_pos[1]): 0}

    inside_count = count_inside_regions(m, dists, width, height)
    print(f"Part 2: {inside_count}")
