
def read_conditions(file_path):
    # Read conditions from the given file and return a list of rows
    with open(file_path, "r") as f:
        return [line.strip() for line in f]

def count_arrangements_recursive(row, damaged_groups, dot_position, block_position, current, dp_cache):
    """
- Memoization Cache (dp_cache): The function uses a cache (dp_cache) to store the results of previously computed states. This helps avoid redundant calculations and improves performance.

- Base Case: The function starts with a base case to check if the end of the row (dot_position == len(row)) is reached. If so, it checks whether the conditions for a valid arrangement are met and returns 1 if true, indicating a valid arrangement.

- Exploring Arrangements: The function then iterates over possible states for the current position (dot_position) and explores different arrangements based on the current character (c) at that position.

- Recursion: The function makes recursive calls to itself, updating the state based on the explored arrangements. It considers situations where the current spring is operational (c == '.') or broken (c == '#'). The recursion explores different possibilities for the next position (dot_position + 1) and the next damaged group (block_position).

- Updating Cache and Returning Result: The calculated result (ans) for the current state is stored in the cache (dp_cache) before being returned. This ensures that the same state is not recalculated multiple times.
"""
    # Memoized recursive function to count arrangements based on conditions
    key = (dot_position, block_position, current)
    if key in dp_cache:
        return dp_cache[key]

    # Base case: end of the row
    if dot_position == len(row):
        if block_position == len(damaged_groups) and current == 0:
            return 1
        elif block_position == len(damaged_groups) - 1 and damaged_groups[block_position] == current:
            return 1
        else:
            return 0

    ans = 0
    for c in ['.', '#']:
        if row[dot_position] == c or row[dot_position] == '?':
            # Explore possible arrangements
            if c == '.' and current == 0:
                ans += count_arrangements_recursive(row, damaged_groups, dot_position + 1, block_position, 0, dp_cache)
            elif c == '.' and current > 0 and block_position < len(damaged_groups) and damaged_groups[block_position] == current:
                ans += count_arrangements_recursive(row, damaged_groups, dot_position + 1, block_position + 1, 0, dp_cache)
            elif c == '#':
                ans += count_arrangements_recursive(row, damaged_groups, dot_position + 1, block_position, current + 1, dp_cache)

    
    dp_cache[key] = ans
    return ans

def count_arrangements(row, damaged_groups):
    # Wrapper function to initialize the memoization cache
    dp_cache = {}
    return count_arrangements_recursive(row, damaged_groups, 0, 0, 0, dp_cache)

def part1(file_path):
    conditions = read_conditions(file_path)
    total_arrangements = 0

    # Process each row's condition and accumulate total arrangements
    for condition in conditions:
        row, damaged_groups = condition.split()
        damaged_groups = [int(x) for x in damaged_groups.split(',')]
        arrangements = count_arrangements(row, damaged_groups)
        total_arrangements += arrangements

    return total_arrangements

def part2(file_path):
    conditions = read_conditions(file_path)
    for part2 in [False,True]:
        total_arrangements = 0
        for condition in conditions:
            row, damaged_groups = condition.split()
            if part2:
                row = '?'.join([row, row, row, row, row])
                damaged_groups = ','.join([damaged_groups, damaged_groups, damaged_groups, damaged_groups, damaged_groups])
            damaged_groups = [int(x) for x in damaged_groups.split(',')]
            arrangements = count_arrangements(row, damaged_groups)
            total_arrangements += arrangements
    return total_arrangements

if __name__ == "__main__":

    # Example usage
    row_example = "?###????????"
    damaged_groups_example = [3, 2, 1]
    print('example', row_example, damaged_groups_example)
    result = count_arrangements(row_example, damaged_groups_example)
    print(result)


    file_path = 'input.txt'
    print('Part 1:', part1(file_path))
    print('Part 2', part2(file_path))
