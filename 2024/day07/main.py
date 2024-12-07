def get_data(filename):
    equations = []
    with open(filename) as file:
        for line in file:
            test_value, numbers = line.split(":")
            equations.append((int(test_value), list(map(int, numbers.split()))))
    return equations

def solve(equations, part=1):
    result = []

    for test_value, numbers in equations:
        numbers_copy = numbers.copy()
        # print(f"Testing: {test_value} with numbers: {numbers}")

        if part == 1:
            possibles = [numbers_copy.pop(0)]
            found = False
            while numbers_copy and not found:
                curr = numbers_copy.pop(0)
                temp = {i + curr for i in possibles} | {i * curr for i in possibles}
                # print(f"  {possibles[0]} + {curr} = {possibles[0] + curr}, {possibles[0]} * {curr} = {possibles[0] * curr}")
                if test_value in temp:
                    found = True
                possibles = list(temp)

            if test_value in possibles:
                result.append(test_value)
                # print(f"p1: {test_value}")

        elif part == 2:
            possibles = [numbers_copy.pop(0)]
            while numbers_copy:
                curr = numbers_copy.pop(0)
                temp = [
                    v for p in possibles for v in [p + curr, p * curr, int(str(p) + str(curr))] if v <= test_value
                ]
                # print(f"{possibles[0]} + {curr} = {possibles[0] + curr}, {possibles[0]} * {curr} = {possibles[0] * curr}, \nconcat {str(possibles[0])}{str(curr)}")
                possibles = temp

            if test_value in possibles:
                result.append(test_value)
                # print(f"p2: {test_value}")

    return sum(result)

def result(filename) -> tuple:
    equations = get_data(filename)
    part1 = solve(equations, part=1) 
    part2 = solve(equations, part=2) 
    return part1, part2

if __name__ == "__main__":
    print('Answer sample:', result('example.txt'))
    print('Answer:', result('input.txt'))
