import re

def clean_text(text):
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    part1_instruction = re.findall(mul_pattern, "".join(text))
    part2_instruction = re.findall(f"({mul_pattern}|{do_pattern}|{dont_pattern})", text)

    return part1_instruction, part2_instruction

def result(filename) -> int:
    with open(filename) as file:
        lines = file.read()

    part1_instruction, part2_instruction = clean_text(lines)
    
    part1 = sum(int(x) * int(y) for x, y in part1_instruction)

    enabled = True
    part2 = 0
    for instruction in part2_instruction:
        match instruction[0]:
            case "do()":
                enabled = True
            case "don't()":
                enabled = False
            case _ if enabled:
                part2 += int(instruction[1]) * int(instruction[2])

    return part1, part2


if __name__ == "__main__":
    print('Answer sample:', result('example.txt'))
    print('Answer:', result('input.txt'))