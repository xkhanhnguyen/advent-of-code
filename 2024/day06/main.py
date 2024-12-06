def get_data(filename):
    with open(filename) as file:
        grid = [list(line.strip()) for line in file]  

    rows, cols = len(grid), len(grid[0])
    start_x, start_y = 0, 0 
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "^":
                start_x, start_y = x, y
    return grid, start_x, start_y

def visited_positions(grid, x, y):
    pos = (x, y)
    idx = 0
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))  # Up, Right, Down, Left
    rows, cols = len(grid), len(grid[0])

    visited = set()
    visited.add(pos)

    visited_entry = {}  

    while True:
        d = directions[idx]
        n = (pos[0] + d[0], pos[1] + d[1])

       
        if n[0] < 0 or n[0] >= rows or n[1] < 0 or n[1] >= cols:
            return True, visited, visited_entry  

        
        if grid[n[0]][n[1]] == "#":
            idx = (idx + 1) % 4 # turn right 90 degrees
            continue

        
        visited.add(n)
        if n not in visited_entry:
            visited_entry[n] = (pos, idx)
        elif visited_entry[n] == (pos, idx):
            return False, None, None  

        pos = n

def result(filename) -> tuple:
    grid, start_x, start_y = get_data(filename)
    is_leaving, visited, visited_entry = visited_positions(grid, start_x, start_y)
    # print(is_leaving, visited, visited_entry)
    part1 = len(visited)
    part2 = 0 
    return part1, part2

if __name__ == "__main__":
    print('Answer sample:', result('example.txt'))
    print('Answer:', result('input.txt'))
