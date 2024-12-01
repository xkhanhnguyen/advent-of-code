data = list(open('input.txt'))

p1 = [0.5]*len(data)
p2 = [1.0]*len(data)

for i, line in enumerate(data):
    w, h = map(str.split, line.split('|'))

    for j in range(len(set(w) & set(h))):
        p1[i] *= 2
        p2[i+j+1] += p2[i]

part1 = int_list = list(map(int, p1))
part2 = int_list = list(map(int, p2))


print('Part 1:', sum(part1))
print('Part 2:', sum(part2))