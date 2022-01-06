import os 

def get_data(filename):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append(line)
    return parsed_input


def part_1(data):
    pairs = ["()", "[]", "<>", "{}"]
    points = {
                ")": 3,
                "]": 57,
                "}": 1197,
                ">": 25137
            }
    total_score = 0
    for line in data:
        stack = []
        score = 0
        find = True 
        for char in line:
            for p in pairs:
                if char == p[0]:
                    stack.append(char)
                elif char == p[1]:
                    if stack[-1] == p[0]:
                        stack.pop()
                    else:
                        find = False
                        break
            
            if find == False:
                score = points[char]
                break
        total_score += score    
    return total_score

def part_2(data):
    pairs = ["()", "[]", "<>", "{}"]
    scores = {
                "(": 1,
                "[": 2,
                "{": 3,
                "<": 4
            }
    
    ans = []
    for line in data:
        stack = []
        total_score = 0
        find = True 
        for char in line:
            for p in pairs:
                if char == p[0]:
                    stack.append(char)
                elif char == p[1]:
                    if stack[-1] == p[0]:
                        stack.pop()
                    else:
                        find = False
                        break
            
            if not find:
                break
        
        if not find:
            continue
                
        for char in stack[::-1]:
            total_score *= 5
            total_score += scores[char] 
        ans.append(total_score)
        
    
    ans.sort()
    mid_score = ans[len(ans) // 2]
    return mid_score
if __name__ == '__main__':
    data = get_data("input.txt")
    
    print('part 1:', part_1(data))
    print('part 2:', part_2(data))


    # print('part 1:', part_1('{([(<{}[<>[]}>{[]{[(<()>'))
    # print('part 2:', part_2('{([(<{}[<>[]}>{[]{[(<()>'))