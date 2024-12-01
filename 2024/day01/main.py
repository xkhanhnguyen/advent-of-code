from collections import Counter
def result(filename) -> int:
    with open(filename) as file:
        lines = file.read().strip().splitlines()
        left, right = [], []

    for line in lines:
        parts = line.split()  
        left.append(int(parts[0]))
        right.append(int(parts[1]))
    diff = [abs(l - r) for l, r in zip(sorted(left), sorted(right))]
    part1 = sum(diff)


    right_counts = Counter(right)

    part2 = sum(num * right_counts[num] for num in left)
    return part1, part2


if __name__ == "__main__":
    print('answer sample', result('example.txt'))
    print('answer', result('input.txt'))
