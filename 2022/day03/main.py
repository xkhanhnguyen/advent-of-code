import string
import numpy as np

def get_data(filename): 
    with open(filename) as f:
        data = [x for x in f.read().strip().split("\n")]
        return data

def priority(data):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    keys = lower + upper
    
    values = np.arange(1,53)
    priority = dict(zip(keys, values))

    common1, common2 = [], []
    for line in data:
        string1 = line[:len(line)//2]
        string2 = line[len(line)//2:]
        common_characters = ''.join(set(string1).intersection(string2))
        common1.append(common_characters)
    
    part1 = [priority[char] for char in common1 if char in priority.keys()]

    # part 2
    subList = [data[n:n+3] for n in range(0, len(data), 3)]
    for group in subList:
        common_characters = ''.join(set(group[0]).intersection(group[1], group[2]))
        common2.append(common_characters)
    part2 = [priority[char] for char in common2 if char in priority.keys()]
    return sum(part1), sum(part2)




if __name__ == "__main__":
    data = get_data('input.txt')
    testing = get_data('test_data.txt')
    print('testing:', priority(testing))
    print('result:', priority(data))
