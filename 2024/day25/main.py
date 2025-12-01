def convert_to_heights(schematic, from_top):
    """Converts the schematic into heights of the columns."""
    num_columns = len(schematic[0]) if schematic else 0
    heights = [0] * num_columns  

    for col in range(num_columns):
        for row in range(len(schematic)):
            if schematic[row][col] == "#":
                if from_top:
                    heights[col] += 1
                else:
                    heights[col] = len(schematic) - row  # For keys, count from the bottom

    return heights


def get_data(filename):
    """Reads the schematics from the file and classifies them into locks and keys."""
    with open(filename, "r") as file:
        data = file.read().split("\n\n")

    locks = []
    keys = []

    for item in data:
        item = item.split("\n")
        # Transpose the rows to columns
        cols = [[row[c] for row in item] for c in range(len(item[0]))]
        # Calculate the height of the columns
        heights = [col.count("#") - 1 for col in cols]

        # Classify based on the first row's count of "#"
        if item[0].count("#") == 5:
            locks.append(heights)
        else:
            keys.append(heights)

    return locks, keys


def solve(locks, keys):
    """Finds the number of unique lock/key pairs that fit without overlapping."""
    valid_pairs = set()  # Use a set to track unique (lock_idx, key_idx) pairs

    for lock_idx, lock in enumerate(locks):
        for key_idx, key in enumerate(keys):
            # Ensure all columns are compared properly
            if len(lock) != len(key):
                continue  # Skip if lock and key don't align in column count

            # Check if the lock and key fit in all columns
            if all(lock[i] + key[i] <= 5 for i in range(len(lock))):
                valid_pairs.add((lock_idx, key_idx))

    return len(valid_pairs)  # Return the count of unique valid pairs


if __name__ == "__main__":
    locks, keys = get_data("input.txt")
    print(f"Part1: {solve(locks, keys)}")
