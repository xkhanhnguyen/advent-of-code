import operator
 
OP = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.floordiv}
 
def get_data(filename):
    monkeys = {}
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip().split(' ')
            # print(line[0])
            key = line[0][:-1]
            if len(line) == 2:
                monkeys[key] = int(line[1])
            else:
                monkeys[key] = line[1:]
    
    return monkeys

def part1(monkeys, m):
    yell = monkeys[m]
    # print(yell)
    if yell is None or isinstance(yell, int):
        return yell
    
    m1, op, m2 = yell
    s1 = part1(monkeys, m1)
    s2 = part1(monkeys, m2)
    if s1 and s2:
        return OP[op](s1, s2)
    else:
        return None


 
def part2(monkeys, m, target):
    yell = monkeys[m]
    if isinstance(yell, int): return yell
    if yell is None: return target
    
    m1, op, m2 = yell
    s1 = part1(monkeys, m1)
    s2 = part1(monkeys, m2)
    
    if s1 is None: # x op s2 = target
        match op:
            case '+':
                return part2(monkeys, m1, target - s2)
            case '-':
                return part2(monkeys, m1, target + s2)
            case '*':
                return part2(monkeys, m1, target // s2)
            case '/':
                return part2(monkeys, m1, target * s2)
    
    elif s2 is None: # s1 op x = target
        match op:
            case '+':
                return part2(monkeys, m2, target - s1)
            case '-':
                return part2(monkeys, m2, -(target - s1))
            case '*':
                return part2(monkeys, m2, target // s1)
            case '/':
                return part2(monkeys, m2, s1 // target)
 


if __name__ == "__main__":
    monkeys = get_data('input.txt')
    # print(monkeys)
    print('Part 1:', part1(monkeys, 'root'))
    monkeys['humn'] = None
    monkeys['root'][1] = '-'
    print('Part 2:', part2(monkeys, 'root', 0))