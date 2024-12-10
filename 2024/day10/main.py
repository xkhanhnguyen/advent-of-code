def get_score(grid, i, j):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, left, right
    # [(0, 1), (1, 0), (0, -1), (-1, 0)]
    

    endpoints = []
    queue = [(i, j)]
    visited = set()
    #BFS
    while queue:
        x, y = queue.pop(0)
        # if (x,y) in visited:
        #     continue
        # visited.add((x,y))

        curr = grid[x][y]
        next_val = curr + 1
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == next_val:
                if next_val == 9:
                    endpoints.append((nx, ny))
                else:
                    queue.append((nx, ny))
            
            
    return endpoints
def result(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file.readlines()]
    grid  = [list(map(int, line)) for line in lines]
    
    part1 = 0
    part2 = 0 
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                # print(f"for this point: {grid[i][j]}, corr:{i, j}")
                endpoints = get_score(grid, i, j)
                # print(endpoints)
                part1 += len(set(endpoints))
                part2 += len(endpoints)
    
    return part1, part2

if __name__ == "__main__":
    print('Answer for example.txt:', result('example.txt'))
    print('Answer for input.txt:', result('input.txt'))
