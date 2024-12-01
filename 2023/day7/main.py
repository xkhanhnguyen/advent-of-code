from collections import Counter

with open("input.txt") as f:
    data = f.read().strip()


def hand_type(hand):
    c = Counter(hand)
    counts = [0] if (jokers := c.pop("*", 0)) == 5 else sorted(c.values())
    # The most efficient use of a joker is always as the most common non-joker card
    counts[-1] += jokers
    if counts[-1] == 5:
        return 7
    elif counts[-1] == 4:
        return 6
    elif counts[-2:] == [2, 3]:
        return 5
    elif counts[-1] == 3:
        return 4
    elif counts[-2:] == [2, 2]:
        return 3
    elif counts[-1] == 2:
        return 2
    else:
        return 1


def calculate_hand_score(hand):
    return hand_type(hand)

def map_card_values(hand):
    return [*map("*23456789TJQKA".index, hand)]

def process_data(data):
    lines = [line.split() for line in data.split("\n")]
    sorted_hands = sorted((calculate_hand_score(hand), *map_card_values(hand), int(bid)) for hand, bid in lines)
    return sorted_hands

def calculate_total_score(sorted_hands):
    total_score = 0
    for rank, (_, *card_values, bid) in enumerate(sorted_hands, 1):
        total_score += rank * bid
    return total_score

def solve(data):
    sorted_hands = process_data(data)
    total_score = calculate_total_score(sorted_hands)
    return total_score


if __name__ == '__main__':
    
    # Part 1
    print('Part 1:', solve(data))

    # Part 2
    print('Part 2:', solve(data.replace("J", "*")))
