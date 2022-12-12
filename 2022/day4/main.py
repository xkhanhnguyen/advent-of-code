

def get_data(filename): 
    with open(filename) as f:
        data = [x for x in f.read().strip().split("\n")]
    
    first, second = [], []
    for line in data:
        assignments = line.strip().split(",")
        first_a = assignments[0].split("-")
        first.append((int(first_a[0]), int(first_a[1])))
        second_a = assignments[1].split("-")
        second.append((int(second_a[0]), int(second_a[1])))
    return first, second 

def pairs(data):
    """
    .234.....  2-4
    .....678.  6-8

    .23......  2-3
    ...45....  4-5

    ....567..  5-7
    ......789  7-9

    .2345678.  2-8
    ..34567..  3-7

    .....6...  6-6
    ...456...  4-6

    .23456...  2-6
    ...45678.  4-8
    """
    part1, part2 = 0, 0
    for first, second in zip(*data):
        
        range1 = set(list(range(first[0], first[1] + 1)))
        range2 = set(list(range(second[0], second[1] + 1)))
        common = range1 & range2
        
        if len(common) == len(range1) or len(common) == len(range2):
            part1 += 1
        not_empty_set = (len(common) != 0)
        if not_empty_set:
            part2 +=1

    return part1, part2


if __name__ == "__main__":
    data = get_data('input.txt')
    testing = get_data('testing_data.txt')
    print('testing:', pairs(testing))
    print('answer:', pairs(data))
