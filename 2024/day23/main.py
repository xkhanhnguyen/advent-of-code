from collections import defaultdict

def get_data(file_path):
    connections = []
    with open(file_path, 'r') as file:
        for line in file:
            a, b = line.strip().split('-')
            connections.append((a, b))
    return connections

def find_triangles(connections):
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)


    triangles = set()
    for node in graph:
        neighbors = graph[node]
        for neighbor in neighbors:
            common_neighbors = neighbors.intersection(graph[neighbor])
            for common in common_neighbors:
                triangle = tuple(sorted([node, neighbor, common]))
                triangles.add(triangle)

    return triangles

def find_largest_clique(connections):
    graph = defaultdict(set)
    for a, b in connections:
        graph[a].add(b)
        graph[b].add(a)

    # Use a greedy approach to find the largest clique
    def bron_kerbosch(R, P, X):
        if not P and not X:
            yield R
        while P:
            v = P.pop()
            yield from bron_kerbosch(R.union({v}), P.intersection(graph[v]), X.intersection(graph[v]))
            X.add(v)

    nodes = set(graph.keys())
    largest_clique = max(bron_kerbosch(set(), nodes, set()), key=len)
    return sorted(largest_clique)

def solve(file_path, part=1):
    connections = get_data(file_path)

    if part == 1:
        triangles = find_triangles(connections)

        triangles_with_t = [triangle for triangle in triangles if any(comp.startswith('t') for comp in triangle)]

        # print("Total triangles:", len(triangles))
        # print("Triangles containing 't':", len(triangles_with_t))

        return len(triangles_with_t)

    elif part == 2:
        largest_clique = find_largest_clique(connections)
        password = ",".join(largest_clique)
        # print("Largest clique:", largest_clique)
        # print("Password:", password)

        return password

def main():
    print(f"Part1: ({solve('example.txt', part=1)}, {solve('input.txt',part=1)})")
    print(f"Part2: ([{solve('example.txt', part=2)}],[{solve('input.txt',part=2)}])")
if __name__ == "__main__":
    main()
