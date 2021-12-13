# part 1
def part1(file_name):
    count = 0
    with open(file_name) as f:
        input_file = f.readlines()
        for i in range(len(input_file)-1):
            if int(input_file[i]) < int(input_file[i +1]):    # Compare previous with the current
                count += 1

    return count

# part 2
def part2(file_name):
    count = 0
    with open(file_name) as f:
        rows = [int(r) for r in f]
        
        for i in range(len(rows)-3):
            first = rows[i] + rows[i+1] + rows[i+2]
            second = rows[i+1] + rows[i+2] + rows[i+3]
            if first < second: # Compare previous with the current
                count += 1

    return count


if __name__ == "__main__":
    print('part 1:', part1('input.txt'))
    print('part 2:', part2('input.txt'))

