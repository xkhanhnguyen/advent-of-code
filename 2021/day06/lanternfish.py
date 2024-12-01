
from  collections import defaultdict

def get_data(file_name):
    with open(file_name) as f:
        raw_data = f.read().strip().split(",")
        freq = defaultdict(int) # key: internal timer, value is the frequency 
        for i in raw_data:
            freq[int(i)] += 1
    return freq

    
# solution for both part 1 and 2    
def solution(input, num_days):
    for _ in range(num_days):
        # new_fish to store the frequency fo each day
        new_fish = defaultdict(int)

        for fish in input:
            if fish == 0:
                new_fish[6] += input[fish] 
                new_fish[8] = input[fish]
            else:
                new_fish[fish - 1] += input[fish]
        
        input = new_fish

    
    return sum(v for v in new_fish.values())

if __name__ == '__main__':
    input = get_data('input.txt')
    # example = get_data('ex.txt')
    num_days = 256
    # print('example:', part1(example, num_days))
    print('answer:', solution(input, num_days))