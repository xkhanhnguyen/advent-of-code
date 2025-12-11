def result(filename) -> int:
    with open(filename) as file:
        lines = file.read().strip().splitlines()

    pts = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        x, y = map(int, line.split(','))
        pts.append((x, y))

    part1 = 0
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        for j in range(i+1, n):
            x2, y2 = pts[j]
            w = abs(x1 - x2) + 1
            h = abs(y1 - y2) + 1
            area = w * h
            if area > part1:
                part1 = area

    return part1, 0


if __name__ == "__main__":
    print('answer sample', result('example.txt'))
    print('answer', result('input.txt'))
