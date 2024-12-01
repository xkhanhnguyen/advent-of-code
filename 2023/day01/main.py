import re
NUMBERS = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
def result(filename) -> int:
    with open(filename) as file:
        part1, part2 = 0, 0
        for line in file.readlines():
            digits1, digits2 = [], []
            for c in line:
                if c.isdigit():
                    digits1.append(c)
            numb1 = digits1[0] + digits1[-1]

            part1 +=  int(numb1)

            r = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
            pattern = re.compile(r)
            for w in pattern.findall(line):
                if w.isdigit():
                    digits2.append(w)
                elif w in NUMBERS:
                    digits2.append(NUMBERS[w])
                numb2 = digits2[0] + digits2[-1]
            part2 += int(numb2)

    return part1, part2


if __name__ == "__main__":
    print('answer', result('input.txt'))
