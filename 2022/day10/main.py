from collections import defaultdict
def get_data(filename):
    with open(filename) as f:
        data = [l for l in f.read().strip().split('\n')]
    cycles =  [line.split(' ') for line in data]
    for c in cycles:
        if c[0] =='noop':
            c.append('0')
    return cycles
    
def execute(program):
    count_loop, X = 0, 1
    X_value = defaultdict(int)
    for (ins, cycle) in program:
        cycle = int(cycle)
        if ins == 'noop':
            count_loop += 1
            X_value[count_loop] = X
            # print('if', 'count_loop=', count_loop, '\t X=', X, '\t X_value', X_value)
            # print('\n\n')
        else:
            count_loop += 1
            X_value[count_loop] = X
            # print('else1', ins, cycle, '\t count_loop=', count_loop, '\t X=', X, '\t X_value', X_value)
            # print('\n')
            count_loop += 1
            X_value[count_loop] = X
            X += cycle
            # print('else2', ins, cycle, '\t count_loop=', count_loop, '\t X=', X, '\t X_value', X_value)    
            # print('\n')
            # print('after','count=', count_loop, 'X=', X, 'X_value', X_value)
            # print('\n')
    # print(X_value)
        # temp = 0
    # for x in range(20, 221, 40):
        # print(x)
        # print(X_value[x])
        #     temp += X_value[x]
        # print(temp,'here')
    signal = sum(X_value[x] * x for x in range(20, 221, 40))        
    
    return signal, X_value

 




if __name__ == "__main__":
    data = get_data('input.txt')
    # print(data)
    signal, X_value =  execute(data)
    print('part1', signal)

    
    part2 = ''.join(('#') if X_value[cycle] - 1 <= ((cycle % 40 - 1) %40) <= X_value[cycle] + 1
                    else ''.join('.') for cycle in range(1, 241))
    s = ''
    for i in range(0,len(part2),40):
        s = s+part2[i:i+40]
        s = s+'\n'
    print(s)
    # print(part2)
   
        # print(part2[40:80])
        # print(part2[80:120])
        # print(part2[120:160])
        # print(part2[160:200])
        # print(part2[200:240])
   
    