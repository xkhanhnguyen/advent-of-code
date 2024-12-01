# from collections import Counter
def get_data(file_name):
    """
    Read in the input file

    Args
    ----
    file_name: input file. 
    example get_data('input.txt')

    Returns
    -------
    all_drawn_numbers: 1D array of all drawn numbers
    
    board: 2D array, a set of cards ( puzzle input)
        
    """

    with open(file_name) as f:
        all_drawn_numbers = [int(item) for item in f.readline().strip('\n').split(',')]
        board = []
        while f.readline():
            card = []
            for i in range(5):
                card.extend([int(x) for x in f.readline().strip('\n').split(' ') if x != ''])
            
            board.append(card)
    return all_drawn_numbers, board, card

def winner(card):
    """
    Check for winner of the game

    Args
    ----
    card 1D array shape (25,)

    Returns
    -------
    True if win o.w
        
    """
    position = 0
    for i in range(5):

        if card[position] + card[position + 1]\
             + card[position + 2] + card[position + 3] + card[position + 4] == 5:
            return True
        position += 5
    
    position = 0 
    for i in range(5):
        if card[position] + card[position + 5]\
             + card[position + 10] + card[position + 15] + card[position + 20] == 5:
            return True
        position += 1

    return False


def part1(all_drawn_numbers, board):
    """
    Finding the sum of all unmarked numbers on the winning board
    multiply that sum by the number that was just called when the board won

    Args
    ----
    all_drawn_numbers: 1D array of all drawn numbers
    
    board: 2D array, a set of cards ( puzzle input)

    Returns
    -------
    The sum of the winning board
        
    """
    found = False
    while found == False:
        number = all_drawn_numbers[0]
        all_drawn_numbers = all_drawn_numbers[1:]
        for card in board:
            for i in range(len(card)):
                if card[i] == number:
                    card[i] = 1
        for card in board:
            if winner(card):
                total = sum([x for x in card if x != 1])
                found = True
    return total * number

def part2(all_drawn_numbers, board):
    """
    Finding the sum of all unmarked numbers on the last winning board
    multiply that sum by the number that was just called when the board won

    Args
    ----
    all_drawn_numbers: 1D array of all drawn numbers
    
    board: 2D array, a set of cards ( puzzle input)

    Returns
    -------
    The sum of the last to win
        
    """
    found = False
    while found == False:
        number = all_drawn_numbers[0]
        all_drawn_numbers = all_drawn_numbers[1:]
        for card in range(len(board)): # loop through each card
            for i in range(len(board[card])):
                if board[card][i] == number:
                    board[card][i] = 1

        i = 0
        while i < len(board): # play until the last card 
            if winner(board[i]): 
                if len(board) > 1: # find the winner for the last card
                    board.pop(i)
                
                else:
                    found = True  
                    break  
            else:
                i += 1
        
    total = sum([x for x in board[i] if x != 1])
                
    return total * number



if __name__ == "__main__":
    # all_drawn_numbers, board, card = get_data('example.txt')
    # print('example 1:', part1(all_drawn_numbers, board))
    # print('example 1:', part2(all_drawn_numbers, board))
    
    all_drawn_numbers, board, card = get_data('input.txt')
    print('part 1:', part1(all_drawn_numbers, board))
    print('part 2:', part2(all_drawn_numbers, board))






