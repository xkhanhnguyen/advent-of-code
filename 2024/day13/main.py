import math
from itertools import product

def parse_input(file_name, part):
    machines = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 4):  # Each machine has 4 lines of data
            button_a = tuple(map(int, lines[i].strip().split(': ')[1].replace('X+', '').replace('Y+', '').split(', ')))
            button_b = tuple(map(int, lines[i + 1].strip().split(': ')[1].replace('X+', '').replace('Y+', '').split(', ')))
            prize = tuple(map(int, lines[i + 2].strip().split(': ')[1].replace('X=', '').replace('Y=', '').split(', ')))
            if part == 2:
                # Increase prize by large constant for part 2
                prize = (prize[0] + 10000000000000, prize[1] + 10000000000000)
            machines.append((button_a, button_b, prize))
    return machines

def solve_claw_machine(button_a, button_b, prize, max_presses=100):
    ax, ay = button_a
    bx, by = button_b
    px, py = prize

    # Debug: Print prize values
    print(f"Prize: {prize}, Button A: {button_a}, Button B: {button_b}")

    # Iterate over possible presses of A and B (0 to max_presses)
    min_tokens = math.inf
    best_a, best_b = -1, -1

    for a, b in product(range(max_presses + 1), repeat=2):
        if a * ax + b * bx == px and a * ay + b * by == py:
            tokens = a * 3 + b   # Cost: 3 tokens for A, 1 token for B
            if tokens < min_tokens:
                min_tokens = tokens
                best_a, best_b = a, b

    # Debug: Print the result for this machine
    print(f"Min tokens: {min_tokens}, Best A: {best_a}, Best B: {best_b}")

    return min_tokens if min_tokens != math.inf else None, best_a, best_b

def result(file_name, part=1):
    machines = parse_input(file_name, part)
    total_tokens = 0
    total_prizes = 0

    for machine in machines:
        button_a, button_b, prize = machine
        min_tokens, best_a, best_b = solve_claw_machine(button_a, button_b, prize, max_presses=10000 if part == 2 else 100)

        if min_tokens is not None:
            total_tokens += min_tokens
            total_prizes += 1

    return total_tokens, total_prizes

if __name__ == "__main__":
    print('Answer for example.txt (Part 1):', result('example.txt', part=1))
    print('Answer for example.txt (Part 2):', result('example.txt', part=2))
    print('Answer for input.txt (Part 1):', result('input.txt', part=1))
    print('Answer for input.txt (Part 2):', result('input.txt', part=2))
