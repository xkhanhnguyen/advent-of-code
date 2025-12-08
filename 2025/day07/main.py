def result(filename) -> int:
    with open(filename) as file:
        rows = file.read().strip().splitlines()

    R = len(rows)
    C = max(len(r) for r in rows)
    g = [r.ljust(C, '.') for r in rows]

    for r in range(R):
        if 'S' in g[r]:
            sr, sc = r, g[r].index('S')
            break

    beams = {(sr+1, sc)}
    part1 = 0

    while beams:
        new_beams = set()
        splitters = set()

        for r, c in beams:
            if 0 <= r < R and 0 <= c < C:
                if g[r][c] == '^':
                    splitters.add((r, c))
                else:
                    new_beams.add((r+1, c))

        if not splitters and not new_beams:
            break

        part1 += len(splitters)

        # left/right beams start one row below splitter
        for r, c in splitters:
            if c > 0:
                new_beams.add((r+1, c-1))
            if c+1 < C:
                new_beams.add((r+1, c+1))

        beams = new_beams

    return part1, 0


if __name__ == "__main__":
    print("answer sample", result("example.txt"))
    print("answer", result("input.txt"))
