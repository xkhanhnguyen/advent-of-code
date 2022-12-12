
import numpy as np
import re
def get_data(filename): 
    procedure = []
    with open(filename) as f:
        crates, moves = [x for x in f.read().split("\n\n")]
        chars = [list(s) for s in crates.split('\n')[:-1]]
        temp = np.array(chars, dtype=np.unicode_).transpose()
        stacks = [temp[index] for index in range(1, len(temp), 4)]
        stacks = [[s for s in row if s != ' '] for row in stacks]

        for move in moves.split('\n'):
            Move, From, To = [int(x) for x in re.findall(r'\d+', move)]
            procedure.append([Move, From - 1, To - 1])
        return stacks, procedure

def part1 (crates, procedure):
    for Move, From, To in procedure:   
        for i in range(Move):
            top = crates[From].pop(0)
            crates[To].insert(0, top)
    part1 = ''.join([crate[0] for crate in crates])

    return part1

def part2 ():
    crates, procedure = get_data('input.txt')
    for Move, From, To in procedure:  
        crates[To] = crates[From][:Move] + crates[To]
        crates[From] = crates[From][Move:]
    part2 = ''.join([crate[0] for crate in crates])

    return part2



if __name__ == "__main__":
    # crates, procedure = get_data('testing.txt')
    crates, procedure = get_data('input.txt') 
    print('part1', part1(crates, procedure))
    print('part2', part2())
    
