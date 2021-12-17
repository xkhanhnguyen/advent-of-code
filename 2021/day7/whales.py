import time 
def get_data(file_name):
    with open(file_name) as f:
        raw_data = [int(x) for x in f.read().strip().split(",")]
    return raw_data

def fuel(input):
    part1, part2 = [], []
    for point in range(len(input)):
        distance = [abs(crab - point) for crab in input]
        diffs = sum([sum(list(range(d + 1))) for d in distance])
        
        part1.append(sum(distance))
        part2.append(diffs)
    
    return min(part1), min(part2)


if __name__ == '__main__':
   
    start = time.time()
    input = get_data('input.txt')
    elapsed = time.time()-start
    print('final result:', fuel(input))
    print("Time: %s seconds"%(elapsed))
    