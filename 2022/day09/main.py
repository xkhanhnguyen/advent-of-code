import numpy as np 

def get_data(filename):
    with open(filename) as f:
        data = [l for l in f.read().split('\n')]
    motions = [line.split(' ') for line in data]
    return motions

def positions(motions):
    
    grid = []
    x, y = 0, 0
    x_max, x_min = 0, 0
    y_max, y_min = 0, 0
    for (direction, step) in motions:
        if direction == 'R':
            x += int(step)
        if direction == 'L':
            x -= int(step)

        x_max = max(x, x_max)
        x_min = min(x, x_min)


        if direction == 'U':
            y += int(step)
        if direction == 'D':
            y -= int(step)

        y_max = max(y, y_max)
        y_min = min(y, y_min)

        
    # print('min', abs(x_min), abs(y_min))
    # print('max', abs(x_max), abs(y_max))
    x = abs(x_min) + x_max + 1
    y = abs(y_min) + y_max + 1 
    starting_pos = [abs(x_min), abs(y_min)]

    
    # print(h, v, starting_pos)
    # grid size v x h
    grid = [[0 for i in range(x)] for j in range(y)]
    # print(grid)
    grid[starting_pos[1]][starting_pos[0]] = 1
    # print(grid)

    return grid, starting_pos

def move_knots(grid, motions, starting_pos, knots):
    position = [[starting_pos[0], starting_pos[1]] for i in range(knots)]
    # print(position)
    for (direction, step) in motions:
        step = int(step)
        while step > 0:
            
            # print(direction, step)
            # H moves 
            # start at (0, 0), 
            # 'R': (1, 0),
            # 'L': (-1, 0),
            # 'U': (0, 1),
            # 'D': (0, -1)
            if direction == 'U':
                position[0][1] += 1
            if direction == 'D':
                position[0][1] -= 1
            if direction == 'R':
                position[0][0] += 1
            if direction == 'L':
                position[0][0] -= 1

            # print('update', position)
            # update tail
            for i in range(1, knots):
                cur = position[i]
                prev = position[i-1]
               
                # right
                if prev[0] - cur[0] > 1:  
                    cur[0] += 1
                    if prev[1] - cur[1] > 1:  
                        cur[1] += 1
                    elif cur[1] - prev[1] > 1:  
                        cur[1] -= 1
                    else:  
                        cur[1] = prev[1]
                # left
                if cur[0] - prev[0] > 1:  
                    cur[0] -= 1
                    if prev[1] - cur[1] > 1:  
                        cur[1] += 1
                    elif cur[1] - prev[1] > 1:  
                        cur[1] -= 1
                    else:  
                        cur[1] = prev[1]

                # up
                if prev[1] - cur[1] > 1: 
                    cur[1] += 1
                    if prev[0] - cur[0] > 1:
                        cur[0] += 1
                    elif cur[0] - prev[0] > 1: 
                        cur[0] -= 1
                    else: 
                        cur[0] = prev[0]

                # down
                if cur[1] - prev[1] > 1: 
                    cur[1] -= 1

                    if prev[0] - cur[0] > 1:  
                        cur[0] += 1
                    elif cur[0] - prev[0] > 1:  
                        cur[0] -= 1
                    else: 
                        cur[0] = prev[0]

            # update grid with new tail pos
            grid[position[-1][1]][position[-1][0]] = 1
            step -= 1
            # print('update grid', position[-1][1],position[-1][0])
            # print(grid)

    visited = sum(sum(line) for line in grid)
    return grid, visited



if __name__ == "__main__":


    motions = get_data('input.txt')
    grid, starting_pos = positions(motions)
    grid, visited = move_knots(grid, motions, starting_pos, knots = 10)
    # for line in grid:
    #     print( line)
    print(visited)
    

