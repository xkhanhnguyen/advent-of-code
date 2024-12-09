import itertools

def get_data(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def distance(x, y):
    return (x[0] - y[0], x[1] - y[1])

def solve(lines, part=1):
    positions = {}
    antinodes = set()
    rows = len(lines)
    cols = max(len(line) for line in lines)
    
    for row in range(rows):
        for col, pos in enumerate(lines[row]):
            if pos not in ('.', '#'):
                positions.setdefault(pos, []).append((row, col))

    for antenna, points in positions.items():
        for p1, p2 in itertools.combinations(points, 2):
            d = distance(p1, p2)

            if part == 1:
                antinode1 = (p1[0] - d[0] * 2, p1[1] - d[1] * 2)
                antinode2 = (p2[0] + d[0] * 2, p2[1] + d[1] * 2)
                if 0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols:
                    antinodes.add(antinode1)
                if 0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols:
                    antinodes.add(antinode2)
                
            elif part == 2:
                antinode1 = (p1[0] - d[0], p1[1] - d[1])
                antinode2 = (p2[0] + d[0], p2[1] + d[1])
                while 0 <= antinode1[0] < rows and 0 <= antinode1[1] < cols:
                    antinodes.add(antinode1)
                    antinode1 = (antinode1[0] - d[0], antinode1[1] - d[1])
                while 0 <= antinode2[0] < rows and 0 <= antinode2[1] < cols:
                    antinodes.add(antinode2)
                    antinode2 = (antinode2[0] + d[0], antinode2[1] + d[1])
            
    return len(antinodes)

def result(filename):
    lines = get_data(filename)
    part1 = solve(lines, part=1)
    part2 = solve(lines, part=2)
    return part1, part2

if __name__ == "__main__":
    print('Answer sample:', result('example.txt'))
    print('Answer:', result('input.txt'))
