def result(filename) -> int:
    with open(filename) as file:
        lines = file.read().strip().splitlines()

    part1 = 0
    for line in lines:
        best = 0
        L = len(line)
        for i in range(L):
            a = int(line[i])
            for j in range(i + 1, L):
                b = int(line[j])
                val = 10 * a + b
                if val > best:
                    best = val
        part1 += best

    part2 = 0
    K = 12
    for line in lines:
        n = len(line)
        result_digits = []
        start = 0
        for need in range(K):
            # remaining digits we need to pick after this one
            remaining_needed = K - need - 1
            # the farthest index we can search
            end = n - remaining_needed
            # pick the largest digit between start and end-1
            best_digit = '0'
            best_pos = start
            for i in range(start, end):
                if line[i] > best_digit:
                    best_digit = line[i]
                    best_pos = i
            result_digits.append(best_digit)
            start = best_pos + 1
        part2 += int("".join(result_digits))

    return part1, part2


if __name__ == "__main__":
    print('answer sample', result('example.txt'))
    print('answer', result('input.txt'))
