def get_data(file_name):
    with open(file_name) as f:
        data = f.read().strip().split("Split From Here")
        data = [d.strip().split("\n") for d in data]
        return data

if __name__ == "__main__":
    data = get_data('input.txt')
    # print('part 1:', part1(data))
    # print('part 2:', part2(data))
