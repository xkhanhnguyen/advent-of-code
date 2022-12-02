# Player1: A for Rock, B for Paper, and C for Scissors
# Player2: X for Rock, Y for Paper, and Z for Scissors
# shape: 1 for Rock, 2 for Paper, and 3 for Scissors
def get_data(filename): 
    with open(filename) as f:
        data = [x for x in f.read().strip().split("\n")]
        return data
    
# 0 if you lost, 3 if the round was a draw, and 6 if you won).
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
def drawing_score(input):
    p1 = {'A X': 4, 'A Y': 8, 'A Z': 3,
        'B X': 1, 'B Y': 5, 'B Z': 9,
        'C X': 7, 'C Y': 2, 'C Z': 6
    }
    p2 = {'A X': 3, 'A Y': 4, 'A Z': 8,
        'B X': 1, 'B Y': 5, 'B Z': 9,
        'C X': 2, 'C Y': 6, 'C Z': 7
    }
    ans1, ans2 = 0, 0
    for i in input:
        ans1 += p1[i]
        ans2 += p2[i]
    return ans1, ans2


if __name__ == "__main__":
    input_test = ['A Y', 'B X', 'C Z']
    data = get_data('input.txt')
    # print(data)
    test_result = drawing_score(input_test)
    ans = drawing_score(data)
    print(test_result)
    print(ans)
    # print(get_data('input.txt'))

