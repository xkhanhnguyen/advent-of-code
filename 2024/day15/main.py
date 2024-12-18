dirs = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}
def get_data(file_path):
    with open(file_path, "r") as file:
        return file.read().splitlines()
    
def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()

def get_robot_pos(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "@":
                return (i, j)

def moving(grid, pos, moves, part):
    for move in moves:
        ny = pos[0] + dirs[move][0]
        nx = pos[1] + dirs[move][1]

        if grid[ny][nx] == ".":
            pos = (ny, nx)
        elif grid[ny][nx] == "#":
            continue
        else:
            edges, adjs = get_adjs_and_edges(grid, pos, move, part)
            blocked = 0
            dy, dx = dirs[move]
            for cell in edges:
                ny, nx = (cell[0] + dy, cell[1] + dx)
                if grid[ny][nx] == "#":
                    blocked += 1
            if blocked == 0:
                grid = update_grid(grid, adjs, move)
                pos = (pos[0] + dy, pos[1] + dx)

        # print_grid(grid)  
    return grid

def get_adjs_and_edges(grid, pos, move, part):
    y, x = pos
    dy, dx = dirs[move]
    adjs = set()

    if part == 1 or move in "<>":
        while True:
            ny, nx = y + dy, x + dx
            if grid[ny][nx] in ".#":
                return [(ny - dy, nx - dx)], adjs
            y, x = ny, nx
            adjs.add((y, x))
    else:
        edges = []
        queue = [(y, x)]
        while queue:
            y, x = queue.pop(0)
            if (y, x) in adjs:
                continue
            adjs.add((y, x))
            ny, nx = y + dy, x + dx
            if grid[ny][nx] in ".#":
                edges.append((y, x))
            elif grid[ny][nx] == "[":
                queue.extend([(ny, nx), (ny, nx + 1)])
            elif grid[ny][nx] == "]":
                queue.extend([(ny, nx), (ny, nx - 1)])
        return edges, adjs - {(pos[0], pos[1])}

def update_grid(grid, visited, move):
    dy, dx = dirs[move]
    cells = sorted(
        visited, key=lambda x: (x[0], x[1]) if move in "^v" else (x[1], x[0])
    )
    if move in "v>":
        cells.reverse()
    for y, x in cells:
        ny, nx = y + dy, x + dx
        grid[ny][nx] = grid[y][x]
        grid[y][x] = "."
    return grid

def get_coords_sum(grid, part):
    target = "[" if part == 2 else "O"
    return sum(
        100 * r + c
        for r, row in enumerate(grid)
        for c, cell in enumerate(row)
        if cell == target
    )

def resize_grid(grid):
    _mappings = {"#": "##", "O": "[]", ".": "..", "@": "@."}
    return [list("".join(_mappings[c] for c in row)) for row in grid]

def solve(data, part):
    grid, moves = "\n".join(data).split("\n\n")
    grid = [list(row) for row in grid.split("\n")]
    moves = list("".join(moves.split("\n")))

    if part == 2:
        grid = resize_grid(grid)

    pos = get_robot_pos(grid)
    grid[pos[0]][pos[1]] = "."  # Remove robot marker

    grid = moving(grid, pos, moves, part)
    return get_coords_sum(grid, part)



if __name__ == "__main__":
    data = get_data("input.txt")

    result_part1 = solve(data, part=1)
    result_part2 = solve(data, part=2)

    print("Part 1 result:", result_part1)
    print("Part 2 result:", result_part2)
