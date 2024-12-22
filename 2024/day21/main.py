from collections import deque

# Define the numeric keypad layout
NUMERIC_KEYPAD = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['0', 'A']
]

# Directional keypad for the robot's arm movement (represented by coordinates)
DIRECTIONS = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

# Helper function to find the position of a button on the numeric keypad
def find_position(keypad, key):
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] == key:
                return r, c
    return None

# Function to get the shortest path length from start to target on the numeric keypad
def bfs(start, target):
    queue = deque([(start, 0)])  # Queue of (position, steps)
    visited = set([start])  # Set to track visited positions

    while queue:
        (x, y), steps = queue.popleft()

        # If we've reached the target
        if NUMERIC_KEYPAD[x][y] == target:
            return steps
        
        # Try moving in all 4 directions
        for direction in DIRECTIONS.values():
            nx, ny = x + direction[0], y + direction[1]
            if 0 <= nx < len(NUMERIC_KEYPAD) and 0 <= ny < len(NUMERIC_KEYPAD[nx]):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))
    
    return float('inf')  # If no path found (which shouldn't happen in a valid case)

# Read in the data from a file
def get_data(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Solve the problem
def solve():
    codes = get_data('example.txt')
    
    total_complexity = 0
    
    for code in codes:
        numeric_code = int(code[:-1])  # Get the numeric part (ignoring the 'A')
        sequence = code[:-1]  # The sequence to press
        
        # Start from position 'A' on the keypad
        start_pos = find_position(NUMERIC_KEYPAD, 'A')
        
        total_steps = 0
        current_position = start_pos
        
        for digit in sequence:
            # Get the shortest path to the next digit in the sequence
            steps_to_digit = bfs(current_position, digit)
            total_steps += steps_to_digit  # Add steps to the total
            current_position = find_position(NUMERIC_KEYPAD, digit)  # Update current position
        
        # Calculate the complexity
        complexity = total_steps * numeric_code
        total_complexity += complexity
        
        # Print the code and its corresponding sequence length
        print(f"Code: {code}, Sequence Length: {total_steps}")
    
    print(f"Total Complexity: {total_complexity}")

# Main function to run the solution
if __name__ == "__main__":
    solve()
