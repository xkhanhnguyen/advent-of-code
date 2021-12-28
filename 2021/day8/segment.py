import time
import itertools
def get_data(file_name):
    with open(file_name) as f:
        raw_data = f.read().strip().split("\n")
        data_part1 = [line[line.index("|") + 2:].split(" ") for line in raw_data]

        data_part2 = [
        [
            sorted(line[:line.index("|") - 1].split(" ")),
            line[line.index("|") + 2:].split(" ")
        ] for line in raw_data
    ]
    return data_part1, data_part2

def part1(data1):
    count = 0
    for line in data1:
        for i in line:
            if len(i) in (2,3,4,7):
                count +=1
        
    return count


def part2 (data2):
    digits_key = [
                    "abcefg", #0
                    "cf", #1
                    "acdeg", #2
                    "acdfg", #3
                    "bcdf", #4
                    "abdfg",#5
                    "abdefg", #6
                    "acf", #7 
                    "abcdefg", #8 
                    "abcdfg" #9
                ]
    digits = tuple(sorted(digits_key))
    ans = 0

    for line in data2:
        clues = line[0]
        assert len(clues) == 10

        num = line[1]
    # Try all possible substitutions
        for sigma in itertools.permutations("abcdefg"):
            # Reencode digits
            key = {}
            for c in "abcdefg":
                key[c] = sigma["abcdefg".index(c)]
            
            new_clues = [] * 10 # len of 10
            for clue in clues:
                x = ""
                for char in clue:
                    x += key[char]
                x = "".join(sorted(x))
                new_clues.append(x)
            
            new_clues.sort()

            if tuple(new_clues) == digits:
                # Get the number it's supposed to be
                n = []
                for d in num:
                    x = ""
                    for char in d:
                        x += key[char]
                    x = "".join(sorted(x))
                    n.append(digits_key.index(x))
                
                ans += int("".join([str(i) for i in n]))

                break

    return ans

if __name__ == '__main__':
   
    start = time.time()
    data1, data2 = get_data('input.txt')
    
    print('part 1:', part1(data1))
    print('part 2:', part2(data2))

    elapsed = time.time()-start
    print('time:', elapsed)