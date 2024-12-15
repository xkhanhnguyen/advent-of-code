def parse_and_update(filename, time_steps=None):
    robots = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split()
                p = tuple(map(int, parts[0][2:].split(',')))  # Extract position (x, y)
                v = tuple(map(int, parts[1][2:].split(',')))  # Extract velocity (vx, vy)
                robots.append({'pos': p, 'vel': v})

    if time_steps is not None:
        GRID_WIDTH = 101
        GRID_HEIGHT = 103

        for _ in range(time_steps):
            for robot in robots:
                x, y = robot['pos']
                vx, vy = robot['vel']

                x = (x + vx) % GRID_WIDTH
                y = (y + vy) % GRID_HEIGHT
                robot['pos'] = (x, y)

    return robots

def solve_part_one(filename, time_steps=100):
    robots = parse_and_update(filename, time_steps)

    GRID_WIDTH = 101
    GRID_HEIGHT = 103
    mid_x, mid_y = GRID_WIDTH // 2, GRID_HEIGHT // 2
    quadrants = [0, 0, 0, 0]  # [Q1, Q2, Q3, Q4]

    for robot in robots:
        x, y = robot['pos']
        if x == mid_x or y == mid_y:
            continue  # Ignore robots in the middle
        if x > mid_x and y < mid_y:
            quadrants[0] += 1  # q1
        elif x < mid_x and y < mid_y:
            quadrants[1] += 1  # q2
        elif x < mid_x and y > mid_y:
            quadrants[2] += 1  # q3
        elif x > mid_x and y > mid_y:
            quadrants[3] += 1  # q4

    safety_factor = 1
    for count in quadrants:
        safety_factor *= count

    return quadrants, safety_factor

def solve_part_two(filename):
    robots = parse_and_update(filename)

    GRID_WIDTH = 101
    GRID_HEIGHT = 103

    t = 0
    while True:
        t += 1
        pos = set()

        for robot in robots:
            x, y = robot['pos']
            vx, vy = robot['vel']

            x = (x + t * vx) % GRID_WIDTH
            y = (y + t * vy) % GRID_HEIGHT
            pos.add((x, y))

        if len(pos) == len(robots):
            return t

        if t > 10000:
            return "Pattern not found within the limit"

if __name__ == '__main__':
    # Part 1 solution
    print('Answer for example.txt (Part 1):', solve_part_one('example.txt', 100))
    print('Answer for input.txt (Part 1):', solve_part_one('input.txt', 100))

    # Part 2 solution
    print('Answer for example.txt (Part 2): Time:', solve_part_two('example.txt'))
    print('Answer for input.txt (Part 2): Time:', solve_part_two('input.txt'))
