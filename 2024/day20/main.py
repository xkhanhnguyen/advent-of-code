from collections import deque

def get_and_parse_data(filename):
    """Read the racetrack map from a file and parse it into a grid, start, and end positions."""
    grid, start, end = [], None, None
    with open(filename, 'r') as file:
        for r, line in enumerate(file.readlines()):
            row = list(line.strip())
            grid.append(row)
            for c, char in enumerate(row):
                if char == "S":
                    start = (r, c)
                elif char == "E":
                    end = (r, c)
    return grid, start, end

def find_shortest_path(grid, start, end):
    """Find the shortest path from start to end using BFS."""
    rows, cols = len(grid), len(grid[0])
    visited = set()

    queue = deque([(start, 0, [start])])  # (position, steps, path)
    visited.add(start)

    while queue:
        (r, c), steps, path = queue.popleft()
        if (r, c) == end:
            return steps, path

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#" and (nr, nc) not in visited:
                new_path = path + [(nr, nc)]
                queue.append(((nr, nc), steps + 1, new_path))
                visited.add((nr, nc))

    return float('inf'), []  # No path found

def find_cheatable_pairs(path, savings, cheat_moves):
    pairs = set()

    for i in range(len(path) - savings):
        for j in range(i + 1 + savings, len(path)):
            p1 = path[i]
            p2 = path[j]
            manhattan = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            if (manhattan <= cheat_moves) and (savings <= j - i - manhattan):
                pairs.add((path[i], path[j]))
    return len(pairs)

def find_cheatable_pairs_in_range(path, savings, cheat_moves):
    cheats = 0

    coords_steps = {coord: i for i, coord in enumerate(path)}

    possible_ranges = []
    for dy in range(-cheat_moves, cheat_moves + 1):
        for dx in range(-cheat_moves, cheat_moves + 1):
            if dy == 0 and dx == 0:
                continue

            manhattan = abs(dy) + abs(dx)
            if manhattan > cheat_moves:
                continue

            possible_ranges.append((dy, dx, manhattan))

    for y, x in path:
        for dy, dx, manhattan in possible_ranges:
            ny, nx = y + dy, x + dx
            if (ny, nx) in coords_steps:
                if savings <= (coords_steps[(ny, nx)] - coords_steps[(y, x)] - manhattan):
                    cheats += 1
    return cheats

def solve(data):
    """Solve the problem using the given input data."""
    grid, start, end = get_and_parse_data(data)
    steps, path = find_shortest_path(grid, start, end)

    savings = 100
    cheat_moves = 2

    # Find the number of cheatable pairs
    cheatable_count = find_cheatable_pairs_in_range(path, savings, cheat_moves)
    return cheatable_count

     

if __name__ == "__main__":
    print('Answer for example.txt (part 1):', solve('example.txt'))
    print('Answer for input.txt (part 1):', solve('input.txt'))

