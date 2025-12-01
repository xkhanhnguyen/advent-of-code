def parse_input(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    initial_values, gate_rules = {}, []
    for line in lines:
        if ":" in line:
            wire, value = line.split(": ")
            initial_values[wire] = int(value)
        elif line:
            gate_rules.append(line.split())

    return initial_values, gate_rules

def evaluate_gate(input1, input2, operation):
    if operation == "AND":
        return input1 & input2
    elif operation == "OR":
        return input1 | input2
    elif operation == "XOR":
        return input1 ^ input2

def simulate_circuit(initial_values, gate_rules):
    wires = {**initial_values}
    unresolved = gate_rules[:]

    while unresolved:
        for rule in unresolved[:]:
            input1, gate, input2, _, output = rule
            if input1 in wires and input2 in wires:
                wires[output] = evaluate_gate(wires[input1], wires[input2], gate)
                unresolved.remove(rule)

    return wires

def solve(filename):
    initial_values, gate_rules = parse_input(filename)
    wire_values = simulate_circuit(initial_values, gate_rules)

    # Extract and sort 'z' wires by significance
    z_wires = [value for wire, value in sorted(wire_values.items()) if wire.startswith("z")]
    decimal_output = int("".join(map(str, z_wires[::-1])), 2)

    return decimal_output

if __name__ == "__main__":
    print(f"Part1: ({solve('example.txt')}, {solve('input.txt')})")
