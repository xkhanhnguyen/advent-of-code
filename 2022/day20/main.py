def get_data(filename):
    data = []
    with open(filename) as f:
        for i, line in enumerate(f.readlines()):
            if line.strip():
                data.append((i, int(line)))
    return data            


def part1(sequence):
    order = sequence[:]
    
    for index, numb in order:
        for i in range(len(sequence)):
            if sequence[i][0] == index:
                break
        for _ in range(abs(numb)):
            swap = (i + (numb//abs(numb))) % len(sequence)
            sequence[i], sequence[swap] = sequence[swap], sequence[i]
            i = swap
    for i in range(len(sequence)):
        if sequence[i][1] == 0:
            break
    a = sequence[(i+1000)%len(sequence)][1]
    b = sequence[(i+2000)%len(sequence)][1]
    c = sequence[(i+3000)%len(sequence)][1]

    return a + b + c

def part2(sequence):
    key = 811589153
    order = sequence[:]
    data = [(index, key*numb) for (index, numb) in order]
    
    for count in range(10):
        for index, numb in order:
            for i in range(len(data)):
                if data[i][0] == index:
                    break
            swaps = data[i][1] % (len(data)-1)
            for _ in range(abs(swaps)):
                swap_i = (i + (swaps//abs(swaps))) % len(data)
                data[i], data[swap_i] = data[swap_i], data[i]
                i = swap_i
        print(count+1, data)
    
    for i in range(len(sequence)):
        if data[i][1] == 0:
            break
    a = sequence[(i+1000)%len(data)][1]
    b = sequence[(i+2000)%len(data)][1]
    c = sequence[(i+3000)%len(data)][1]
    print(a, b, c)
    return  a + b + c

if __name__ == "__main__":
    data = get_data('testing.txt')
    print(part1(data))
    print(part2(data))

