
import functools

def get_data(filename):
    with open(filename) as f:

        data = [l.split('\n') for l in f.read().split('\n\n')]
    packets = [[eval(x[0]), eval(x[1])] for x in data]
    add_divider = [eval(x) for x in open(filename).read().split()] + [[[2]]]+ [[[6]]]
    # print(add_divider)
    return packets, add_divider


def compare(left, right):
    # print("L:",left,"\nR:",right,"\n\n") 
    if type(left) is int and type(right) is int:
        if left < right: return 1
            # print('l<r, return True, next pair')
        if left > right: return -1
            # print('l>r') 
        else:            return 0

    if type(left) is int: left = [left]
    if type(right) is int: right = [right]

    if left == [] and right != []: return 1
    # print('[] left ..')
    if left != [] and right == []: return -1
    # print('[] right')
    if left == [] and right == []: return 0
    # print('start comapring pairs')

    pairs = compare(left[0],right[0])
    if pairs:
        return pairs
    else:
        return compare(left[1:],right[1:])

    

if __name__ == "__main__":
    part1, part2 = get_data('input.txt')
    rightorder = [i for i in range(1,len(part1)+1) if compare(part1[i-1][0],part1[i-1][1]) == 1]
    
    # print('rightorder', rightorder)
    print('part1', sum(rightorder))
    packet_order = sorted(part2, key=functools.cmp_to_key(compare), reverse = True)
    # print(packet_order)
    decoder_key = (packet_order.index([[2]]) + 1 )* (packet_order.index([[6]])+ 1)
    print('part2', decoder_key)
