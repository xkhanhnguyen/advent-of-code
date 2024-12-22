def get_data(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

    registers = {'A': 0, 'B': 0, 'C': 0}
    program = []

    for line in lines:
        if line.startswith("Register A"):
            registers['A'] = int(line.split(": ")[1])
        elif line.startswith("Register B"):
            registers['B'] = int(line.split(": ")[1])
        elif line.startswith("Register C"):
            registers['C'] = int(line.split(": ")[1])
        elif line.startswith("Program"):
            program = list(map(int, line.split(": ")[1].split(",")))

    return registers, program


def execute_program(registers, program):
    pointer = 0
    output = []

    def get_combo_value(operand):
        if operand <= 3:
            return operand  
        elif operand == 4:
            return registers['A']
        elif operand == 5:
            return registers['B']
        elif operand == 6:
            return registers['C']
        return None  

    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer + 1]

        if opcode == 0:  
            combo_value = get_combo_value(operand)
            registers['A'] //= (2 ** combo_value)
        elif opcode == 1:  
            registers['B'] ^= operand
        elif opcode == 2:  
            combo_value = get_combo_value(operand)
            registers['B'] = combo_value % 8
        elif opcode == 3:  
            if registers['A'] != 0:
                pointer = operand
                continue
        elif opcode == 4:  
            registers['B'] ^= registers['C']
        elif opcode == 5:  
            combo_value = get_combo_value(operand)
            output.append(combo_value % 8)
        elif opcode == 6:  
            combo_value = get_combo_value(operand)
            registers['B'] = registers['A'] // (2 ** combo_value)
        elif opcode == 7:  
            combo_value = get_combo_value(operand)
            registers['C'] = registers['A'] // (2 ** combo_value)

        pointer += 2

    return ",".join(map(str, output))


def find_lowest_valid_a(program, start_a=1, max_attempts=90_000_000):
    def generate_output(a, program):
        registers = {'A': a, 'B': 0, 'C': 0}
        pointer = 0
        output = []

        def get_combo_value(operand):
            if operand <= 3:
                return operand
            elif operand == 4:
                return registers['A']
            elif operand == 5:
                return registers['B']
            elif operand == 6:
                return registers['C']
            return None

        while pointer < len(program):
            opcode = program[pointer]
            operand = program[pointer + 1]

            if opcode == 0: 
                combo_value = get_combo_value(operand)
                registers['A'] //= (2 ** combo_value)
            elif opcode == 1: 
                registers['B'] ^= operand
            elif opcode == 2:  
                combo_value = get_combo_value(operand)
                registers['B'] = combo_value % 8
            elif opcode == 3:  
                if registers['A'] != 0:
                    pointer = operand
                    continue
            elif opcode == 4:  
                registers['B'] ^= registers['C']
            elif opcode == 5: 
                combo_value = get_combo_value(operand)
                output.append(combo_value % 8)

                
                if len(output) > len(program) or output[-1] != program[len(output) - 1]:
                    return None
            elif opcode == 6:
                combo_value = get_combo_value(operand)
                registers['B'] = registers['A'] // (2 ** combo_value)
            elif opcode == 7: 
                combo_value = get_combo_value(operand)
                registers['C'] = registers['A'] // (2 ** combo_value)

            pointer += 2

            
            if len(output) == len(program):
                return output

        return output

    print("Starting here...")

    a = start_a
    while a <= max_attempts:
        output = generate_output(a, program)

        if output == program:  # Exact match
            print(f"Success! Lowest valid A: {a}")
            return a

        if a % 10_000_000 == 0:
            print(f"A = {a}... Still searching.")

        a += 1  # Increment search space

    print("No valid A found within the specified range.")
    return None


def solve(part, filename):
    registers, program = get_data(filename)

    if part == 1:
        result = execute_program(registers, program)
        print("Part 1:", result)
    elif part == 2:
        solution_a = find_lowest_valid_a(program)
        print(f"Lowest valid A: {solution_a}")



if __name__ == "__main__":
    (solve(part=1, filename='example.txt'),solve(part=2, filename='example.txt'))
    (solve(part=1, filename='input.txt'),solve(part=2, filename='input.txt'))
