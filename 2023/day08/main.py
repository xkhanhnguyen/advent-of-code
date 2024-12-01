import re

def process_data(data):
    instructions = list(data[0])
    node_list = {}
    for i in data[2:]:
        a = re.split(r"[\W]+", i)
        node_list[a[0]] = (a[1], a[2])
    return instructions, node_list

def follow_instructions(start_node, instructions, node_list):
    current_node = start_node
    steps = 0

    while True:
        for i in instructions:
            steps += 1
            node_tuple = node_list.get(current_node)
            if i == "L":
                current_node = node_tuple[0]
            else:
                current_node = node_tuple[1]

            if current_node == "ZZZ":
                return steps

if __name__ == '__main__':
    with open("input.txt") as f:
        data = [x.strip('\n') for x in f.readlines()]

    instructions, node_list = process_data(data)
    start_node = "AAA"

    total_steps = follow_instructions(start_node, instructions, node_list)
    print('Total Steps:', total_steps)
