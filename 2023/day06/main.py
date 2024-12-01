from functools import reduce
import sys
from typing import List, Tuple




def read_lines_to_list() -> List[str]:
    lines: List[str] = []
    with open('input.txt') as f:
        for line in f:
            line = line.strip()
            lines.append(line)

    return lines


def calculate_distance(held, remaining):
    return remaining * held


def part1():
    lines = read_lines_to_list()
    times = [int(val) for val in lines[0].split(":")[1].strip().split()]
    records = [int(val) for val in lines[1].split(":")[1].strip().split()]

    races = [(time, distance) for (time, distance) in zip(times, records)]

    num_ways = []

    for time, record in races:
        wins = 0
        for i in range(time + 1):
            if calculate_distance(i, time - i) > record:
                wins += 1

        num_ways.append(wins)

    result = reduce((lambda x, y: x * y), num_ways)
    return result


def part2():
    lines = read_lines_to_list()
    time = int("".join(lines[0].split(":")[1].strip().split()))
    record = int("".join(lines[1].split(":")[1].strip().split()))

    wins = 0
    for i in range(time + 1):
        if calculate_distance(i, time - i) > record:
            wins += 1

    return wins


if __name__ == '__main__':
    print('Part 1:', part1())
    print('Part 2:', part2())