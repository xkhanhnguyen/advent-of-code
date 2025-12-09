parent = []
size = []

def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

def union(u, v):
    ru, rv = find(u), find(v)
    if ru == rv:
        return False
    if size[ru] < size[rv]:
        ru, rv = rv, ru
    parent[rv] = ru
    size[ru] += size[rv]
    return True


def result(filename) -> int:
    with open(filename) as file:
        lines = file.read().strip().splitlines()

    pts = [tuple(map(int, line.split(','))) for line in lines if line.strip()]
    n = len(pts)

    pairs = []
    for i in range(n):
        xi, yi, zi = pts[i]
        for j in range(i+1, n):
            xj, yj, zj = pts[j]
            dx, dy, dz = xi - xj, yi - yj, zi - zj
            dist = dx*dx + dy*dy + dz*dz
            pairs.append((dist, i, j))
    pairs.sort(key=lambda x: x[0])

    global parent, size
    parent = list(range(n))
    size = [1] * n
    comps_left = n
    part2 = 0

    # part 1 limit
    if filename == "example.txt":
        limit = min(10, len(pairs))
    else:
        limit = min(1000, len(pairs))

    # process pairs for part 1 and keep going for part 2
    for idx, (dist, i, j) in enumerate(pairs):
        merged = union(i, j)
        if merged:
            comps_left -= 1

        # record part1 at limit
        if idx + 1 == limit:
            comps = {}
            for x in range(n):
                r = find(x)
                comps[r] = comps.get(r, 0) + 1
            sizes_list = sorted(comps.values(), reverse=True)
            sizes_list += [1] * max(0, 3 - len(sizes_list))
            print(f'Top 3: {sizes_list[0]}, {sizes_list[1]}, {sizes_list[2]}')
            part1 = sizes_list[0] * sizes_list[1] * sizes_list[2]

        # part2
        if merged and comps_left == 1 and part2 == 0:
            print(f'points {pts[i]}, {pts[j]}')
            part2 = pts[i][0] * pts[j][0]
            break

    return part1, part2


if __name__ == "__main__":
    print("answer sample", result("example.txt"))
    print("answer", result("input.txt"))
