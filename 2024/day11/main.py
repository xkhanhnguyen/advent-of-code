tracking = {}

def blink(stone, blinking_times):
    if blinking_times == 0:
        return 1

    if (stone, blinking_times) in tracking:
        return tracking[(stone, blinking_times)]

    if stone == 0:
        size = blink(1, blinking_times - 1)
    else:
        stone_str = str(stone)
        num = len(stone_str)
        if num % 2 == 0:
            left = int(stone_str[:num // 2])
            right = int(stone_str[num // 2:])
            size = blink(left, blinking_times - 1) + blink(right, blinking_times - 1)
        else:  # Odd number of digits
            size = blink(stone * 2024, blinking_times - 1)

    tracking[(stone, blinking_times)] = size
    
    return size

def count_stones(stone, blinking_times):
    stones = map(int, stone)
    return sum(blink(stone, blinking_times) for stone in stones)

def result(filename):
    with open(filename) as file:
        initial_arrangement = file.read().split()
    part1 = count_stones(initial_arrangement, 25)
    part2 = count_stones(initial_arrangement, 75)  

    return part1, part2

if __name__ == "__main__":
    print('Answer for example.txt:', result('example.txt'))
    print('Answer for input.txt:', result('input.txt'))