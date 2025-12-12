def count_paths(adj, start, goal):
    paths = 0
    stack = [(start, {start})]

    while stack:
        node, visited = stack.pop()
        if node == goal:
            paths += 1
            continue
        for nxt in adj.get(node, []):
            if nxt not in visited:
                visited_next = set(visited)
                visited_next.add(nxt)
                stack.append((nxt, visited_next))
    return paths


def count_paths_require(adj, start, goal, required):
    paths = 0
    start_found = set([start]) & required
    stack = [(start, {start}, start_found)]

    while stack:
        node, visited, found = stack.pop()
        if node == goal:
            if required.issubset(found):
                paths += 1
            continue
        for nxt in adj.get(node, []):
            if nxt not in visited:
                visited_next = set(visited)
                visited_next.add(nxt)

                found_next = set(found)
                if nxt in required:
                    found_next.add(nxt)

                stack.append((nxt, visited_next, found_next))
    return paths


def result(filename) -> int:
    with open(filename) as file:
        lines = file.read().strip().splitlines()

    adj = {}
    for line in lines:
        if not line.strip():
            continue
        name, outs = line.split(':', 1)
        adj[name.strip()] = outs.strip().split()


    part1 = count_paths(adj, 'you', 'out')
    part2 = 0 #incomplete
    # part2 = count_paths_require(adj, 'svr', 'out', {'dac', 'fft'})

    return part1, part2


if __name__ == "__main__":
    print('answer sample', result('example.txt'))
    print('answer', result('input.txt'))
