def result(filename) -> int:
    with open(filename) as file:
        lines = file.read().strip().splitlines()

    ranges = []
    ids = []

    i = 0
    while i < len(lines) and lines[i] != "":
        a, b = lines[i].split("-")
        ranges.append((int(a), int(b)))
        i += 1

    i += 1 # skip blank line
    while i < len(lines):
        ids.append(int(lines[i]))
        i += 1

    part1 = 0
    for x in ids:
        for a, b in ranges:
            if a <= x <= b:
                part1 += 1
                break

    # part 2
    rs = sorted(ranges)
    merged = [rs[0]]
    for a, b in rs[1:]:
        x, y = merged[-1]
        if a <= y + 1:
            merged[-1] = (x, max(y, b))
        else:
            merged.append((a, b))

    part2 = sum(b - a + 1 for a, b in merged)

    return part1, part2


if __name__ == "__main__":
    print('answer sample', result('example.txt'))
    print('answer', result('input.txt'))
