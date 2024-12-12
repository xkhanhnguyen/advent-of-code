def get_area_and_perimeter(grid, i, j, visited):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    queue = [(i, j)]
    region_letter = grid[i][j]
    area = 0
    perimeter = 0

    # BFS
    while queue:
        x, y = queue.pop(0)

        if (x, y) in visited:
            continue
        visited.add((x, y))
        area += 1

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == region_letter and (nx, ny) not in visited:
                    queue.append((nx, ny))
                elif grid[nx][ny] != region_letter:
                    perimeter += 1
            else:
                perimeter += 1

    return area, perimeter

def calculate_price(filename):
    with open(filename) as file:
        grid = [list(line.strip()) for line in file.readlines()]

    total_price = 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                area, perimeter = get_area_and_perimeter(grid, i, j, visited)
                total_price += area * perimeter

    return total_price


if __name__ == "__main__":
    print('Answer for example.txt:', calculate_price('example.txt'))
    print('Answer for input.txt:', calculate_price('input.txt'))
