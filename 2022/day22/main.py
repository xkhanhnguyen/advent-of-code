import re

def get_data(filename):
    with open(filename) as f:
        data = [line for line in f.read().split('\n\n')]
    return data


if __name__ == "__main__":
    print(get_data('testing.txt'))