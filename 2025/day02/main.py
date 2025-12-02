def result(filename) -> int:
    with open(filename) as file:
        lines = file.read().strip().splitlines()

    line = lines[0]
    parts = line.split(',')

    # p1
    part1 = 0
    for p in parts:
        a, b = map(int, p.split('-'))
        for n in range(a, b + 1):
            s = str(n)
            if len(s) % 2 == 0:
                mid = len(s) // 2
                if s[:mid] == s[mid:]:
                    part1 += n

    # p2
    part2 = 0
    for p in parts:
        a, b = map(int, p.split('-'))
        for n in range(a, b + 1):
            s = str(n)

            # make doubled string
            t = s + s
            # remove first and last char
            u = t[1:-1]

            # if original appears inside, it is repeating
            if s in u:
                part2 += n


    return part1, part2


if __name__ == "__main__":
    print('answer sample', result('example.txt'))
    print('answer', result('input.txt'))
