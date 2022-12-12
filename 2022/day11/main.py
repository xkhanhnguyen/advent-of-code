from collections import defaultdict
import re
def get_data(filename):
    with open(filename) as f:
        data = [l for l in f.read().splitlines()]
    return data

def process_data():
    data = get_data('input.txt')
    # print(data)
    items = [[[int(i) for i in data[x][18:].split(',')] for x in range(1, len(data), 7)]][0]
    operation = [(data[x][23:]) for x in range(2, len(data), 7)]
    test = [(int(data[x][21:])) for x in range(3, len(data), 7)]
    condition = [(int(data[x][29:]), int(data[x+1][30])) for x in range(4, len(data), 7)]
    monkey = [0] * len(test)
    return items, operation, test, condition, monkey

def main():
    items, operation, test, condition, monkey = process_data()
    step = 1
    for i in test:
        step *= i
    # print(step)
    for _ in range(10000):
        for i in range(len(monkey)):
            for j in range(len(items[i])):
                curr = items[i][j]
                # print('1 curr', curr)
                # print(monkey)
                if operation[i] == '* old':
                    curr *= curr
                elif operation[i][:2] == '* ':
                    curr *= int(operation[i][2:])
                elif operation[i][:2] == '+ ':
                    curr += int(operation[i][2:])
                # print('2 curr', curr)
                # curr = curr // 3
                curr = curr % step
                # print('3 curr', curr)
                
                
                if curr % test[i] == 0:
                    items[condition[i][0]].append(curr)
                    # print('item', items[condition[i][0]])
                else:
                    items[condition[i][1]].append(curr)
                    # print('item', items[condition[i][0]])
                # print('4 curr',curr)
                monkey[i] += 1
                # print(i)

                # print('update', monkey)
            items[i] = []
            # print('item after', items)
            # break
            # print(items)

            # print(curr)
    return sorted(monkey)[-1] * sorted(monkey)[-2]

if __name__ == "__main__":
    print(main())
    # print(process_data())
   

