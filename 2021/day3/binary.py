from collections import Counter
def get_data(file_name):
    with open(file_name) as f:
        """ 
        strip to remove any leading (spaces at the beginning) 
        and trailing (spaces at the end) characters 
        (space is the default leading character to remove)
        """
        dt = f.read().split("Split From Here") 
        dt = [d.strip().split("\n") for d in dt]
        data = [d for data in dt for d in data]
        return data



def part1(data):
    gamma, epsilon = [], []
    for i in range(len(data[0])): 
        count = Counter([num[i] for num in data])
        if count['1'] > count['0']:
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')
    g = int("".join(gamma), 2)
    e = int("".join(epsilon), 2)
    return g * e

def part2(data):
    oxy = data[::]
    co2 = data[::]
    for i in range(len(data[0])): 
        count = Counter([num[i] for num in oxy])
        if count['1'] >= count['0']:
            o = '1'
        else:
            o = '0'
        oxy = list(filter(lambda x: x[i] == o, oxy))
        if len(oxy) == 1:
            break

    for i in range(len(data[0])): 
        count = Counter([num[i] for num in co2])
        if count['1'] >= count['0']:
            c = '0'
        else:
            c = '1'
        co2 = list(filter(lambda x: x[i] == c, co2))    
        if len(co2) == 1:
            break
    o = int("".join(oxy), 2)
    c = int("".join(co2), 2)
    return o * c
            

if __name__ == "__main__":
    data = get_data('input.txt')

    """
    gamma '10110 or 22 decimal
    epsilon 01001 or 9 decimal 
    output 22 * 9 = 198
    """

    ex = ['00100', '11110', '10110', '10111', '10101', '01111',
            '00111', '11100', '10000', '11001', '00010', '01010']
    
    
    # print('example part 1', part1(ex))
    # print('example part 2', part2(ex))
    print('part 1:', part1(data))
    print('part 2:', part2(data))
