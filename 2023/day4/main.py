data = list(open('input.txt'))

p1 = [0.5]*len(data)
p2 = [1.0]*len(data)

for i, line in enumerate(data):
    w, h = map(str.split, line.split('|'))

    for j in range(len(set(w) & set(h))):
        p1[i] *= 2
        p2[i+j+1] += p2[i]

for p in p1, p2: print(sum(map(int, p)))