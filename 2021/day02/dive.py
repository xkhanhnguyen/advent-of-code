def get_data(filename): 
    with open(filename) as f:
        data = [x for x in f.read().split("\n")]
        return data


def part1(data):
    position = 0
    depth = 0
    for i in data:   
        k, v = i.split()
        if k == 'forward':
            position += int(v)
        if k == 'up':
            depth -= int(v)
        if k == 'down':
            depth += int(v)
    return position * depth
  

def part2(data):
    position = 0
    depth = 0
    aim = 0
    for i in data:   
        k, v = i.split()
        if k == 'forward':
            position += int(v)
            depth += int(v) * aim
        if k == 'up':
            aim -= int(v)
        if k == 'down':
            aim += int(v)
    return position * depth



if __name__ == "__main__":
    data = get_data('input.txt')
    print('part 1:', part1(data))
    print('part 2:', part2(data))