def get_data(filename):
    with open(filename, "r") as file:
        lines = file.read().strip().split("\n")
    towel_patterns = lines[0].split(", ")  # First line contains towel patterns
    desired_designs = lines[2:]  # Remaining lines after the blank line are designs
    return towel_patterns, desired_designs

def can_make_design(design, patterns, original_design=None, cache=None):
    if original_design is None:
        original_design = design  # Keep the full design for debugging
    if cache is None:
        cache = {}  # Initialize the memoization dictionary

    if design in cache:
        return cache[design]

    if not design:
        return True  # Fully matched the design

    for pattern in patterns:
        if design.startswith(pattern):
            if can_make_design(design[len(pattern):], patterns, original_design, cache):
                cache[design] = True
                return True  # Found a valid way to match the design

    cache[design] = False  # No pattern matched
    return False

def count_ways_to_make_design(design, patterns, cache=None):
    if cache is None:
        cache = {}  # Initialize the memoization dictionary

    if design in cache:
        return cache[design]

    if not design:
        return 1  

    part2 = 0
    for pattern in patterns:
        if design.startswith(pattern):
            part2 += count_ways_to_make_design(design[len(pattern):], patterns, cache)

    cache[design] = part2
    return part2

def result(data, count_ways=False):
    patterns, designs = get_data(data)
    if count_ways:
        part2 = 0
        for design in designs:
            memo = {}  # Create a fresh memoization dictionary for each design
            ways = count_ways_to_make_design(design, patterns, memo)
            print(f"Design '{design}' can be made in {ways} ways.")
            part2 += ways
        return part2
    else:
        part1 = 0
        for design in designs:
            if can_make_design(design, patterns):
                print(f"Design '{design}' can be made with {patterns}")
                part1 += 1
            # else:
            #     print(f"Design '{design}' cannot be made with the available patterns.")
        return part1

if __name__ == "__main__":
    print('Answer for example.txt (part 1):', result('example.txt'))
    print('Answer for example.txt (part 2):', result('example.txt', count_ways=True))
    print('Answer for input.txt (part 1):', result('input.txt'))
    print('Answer for input.txt (part 2):', result('input.txt', count_ways=True))
