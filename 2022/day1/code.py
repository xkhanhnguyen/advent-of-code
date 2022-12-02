def result(filename):
    ans = []
    with open(filename) as file:
        score = 0
        for line in file.readlines():
            numb = line.strip()
            if numb == '':
                ans.append(score)
                score = 0
            else:
                score += int(numb)

    part1 =  max(ans)

    ans = sorted(ans)
    # print(ans)
    part2 =  ans[-1] + ans[-2] + ans[-3]

    return part1, part2


if __name__ == "__main__":
    print('answer', result('input.txt'))
