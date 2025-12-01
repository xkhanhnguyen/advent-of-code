def result(filename) -> int:
    with open(filename) as file:
        lines = file.read().strip().splitlines()

    # Dial starts at 50
    pos = 50

    part1 = 0  # count times ending position is 0
    part2 = 0  # count times any click passes through 0

    for line in lines:
        direction = line[0]
        distance = int(line[1:])

        # Determine step direction
        if direction == 'L':
            step = -1
        else:
            step = 1

        # Simulate the dial movement one click at a time
        for _ in range(distance):
            pos += step

            # wrap left
            while pos < 0:
                pos += 100

            # wrap right
            while pos >= 100:
                pos -= 100

            # part 2: ANY click landing on 0
            if pos == 0:
                part2 += 1

        # After finishing this rotation:
        if pos == 0:
            part1 += 1

    return part1, part2


if __name__ == "__main__":
    print('answer sample', result('example.txt'))
    print('answer', result('input.txt'))
