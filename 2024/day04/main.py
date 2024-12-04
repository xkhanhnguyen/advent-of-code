import re

def count_word(rows, word):
    cnt = 0
    for line in rows:
        cnt += line.count(word)
        
        reversed_row = line[::-1]
        cnt += reversed_row.count(word)
    return cnt

def extract_vertical(rows):
    max_row = max(len(rows) for r in rows)
    vertical_words = []
    for i in range(max_row):
        word = ''.join(row[i] for row in rows)
        vertical_words.append(word)
    return vertical_words

def extract_diagonals(lines, direction):
    diagonals = []
    rows = len(lines)
    cols = len(lines[0])
    if direction == "LR" or direction == "lr":
        #top left to bottom right 
        for start in range(-rows+1, cols):
            word = ""
            for row in range(rows):
                col = row + start
                if 0 <= col < cols:
                    word += lines[row][col]
            diagonals.append(word)

    elif direction == "RL" or direction == 'rl':
        # top right to bottom left
        for start in range(cols + rows - 1):
            word = ""
            for row in range(rows):
                col = start - row
                if 0 <= col < cols:
                    word += lines[row][col]
            diagonals.append(word)
    return diagonals

def find_x_mas(lines):
    rows = len(lines)
    cols = len(lines[0])
    cnt = 0
    check = {"M", "S"}
    for r in range(1, rows-1):
        for c in range(1, cols - 1):
            if lines[r][c] == "A":
                if {lines[r-1][c-1], lines[r+1][c+1]} == check and \
                {lines[r-1][c+1], lines[r+1][c-1]} == check:
                    cnt += 1
    return cnt

def result(filename) -> int:
    with open(filename, 'r') as file:
        rows = [line.strip() for line in file]

    vertical_words = extract_vertical(rows)
    diagonal_words_lr = extract_diagonals(rows, 'LR')
    diagonal_words_rl = extract_diagonals(rows, 'RL')

    horizontal = count_word(rows, "XMAS")
    vertical = count_word(vertical_words, "XMAS")
    diagonal = count_word(diagonal_words_lr, "XMAS") + count_word(diagonal_words_rl, "XMAS")

    part1 = horizontal + vertical + diagonal
    part2 = find_x_mas(rows)

    return part1, part2


if __name__ == "__main__":
    print('Answer sample:', result('example.txt'))
    print('Answer:', result('input.txt'))