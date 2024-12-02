def is_safe(row):
    is_sorted =  row == sorted(row) or row == sorted(row, reverse=True)
    is_in_range = all(1 <= abs(row[i] - row[i + 1]) <= 3 for i in range(len(row) - 1))
    return is_sorted and is_in_range


def result(filename) -> int:
    with open(filename) as file:
        lines = file.read().splitlines()
    
    part1, part2 = 0, 0
    for line in lines:
        row = list(map(int, line.split()))
        if is_safe(row):
            part1 += 1
            part2 += 1
            continue

        for i in range(len(row)):
            modified = row[:i] + row[i+1:]
            if is_safe(modified):
                part2 += 1
                break
     
    return part1, part2


if __name__ == "__main__":
    print('answer sample', result('example.txt'))
    print('answer', result('input.txt'))
