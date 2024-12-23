# Read data from example.txt and process it

def get_data(filename):
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f]


def calculate_next_secret(secret):
    # Step 1: Multiply by 64, mix, and prune
    secret = ((secret * 64) ^ secret) % 16777216
    # Step 2: Divide by 32 (rounded down), mix, and prune
    secret = ((secret // 32) ^ secret) % 16777216
    # Step 3: Multiply by 2048, mix, and prune
    secret = ((secret * 2048) ^ secret) % 16777216
    return secret


def simulate_buyer_secrets(initial_secret, steps):
    secret = initial_secret
    for _ in range(steps):
        secret = calculate_next_secret(secret)
    return secret


def solve(filename, part=1):
    initial_secrets = get_data(filename)

    
    steps = 2000
    final_secrets = [simulate_buyer_secrets(secret, steps) for secret in initial_secrets]

    
    return sum(final_secrets)


if __name__ == "__main__":
    print("The sum of the 2000th secret number for each buyer is:", solve("example.txt"))
    print("The sum of the 2000th secret number for each buyer is:", solve("input.txt"))
