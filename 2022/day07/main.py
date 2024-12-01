import re
from collections import defaultdict

## messy code, need to clean up
def get_data(filename: str) -> list[str]: 
    """
        - / (dir)
        - a (dir)
            - e (dir)
                - i (file, size=584)
            - f (file, size=29116)
            - g (file, size=2557)
            - h.lst (file, size=62596)
        - b.txt (file, size=14848514)
        - c.dat (file, size=8504156)
        - d (dir)
            - j (file, size=4060174)
            - d.log (file, size=8033020)
            - d.ext (file, size=5626152)
            - k (file, size=7214296)
            
    """
    dir, path = [], []
    result = defaultdict(int)
    with open(filename) as f:
        data = [x for x in f.read().split("\n")]
        for index, line in enumerate(data):
            # print(line, index)
            if '..' in line:
                dir.pop()
            elif '$ cd' in line:
                dir.append(line.strip()[5:])
            elif line[0].isdigit():
                size, file = line.split()
                # print(dir)  
                for i in range(len(dir)):
                    result[''.join(dir[:i+1])] += int(size)
                    # print(path[:i+1], size, file)
                    folders = ''.join(dir[:i + 1]) + ' ' + file + ' ' + size
                    # print(folders)
                    path.append(folders.split())
                #    key = path[:i+1]
                #    value += int(size)
                #    print(key, value)
                #    folders['/'.join(path[:i + 1])] += int(size)
                # print(path)    
                # print(folders)
    return path, result

    

def total_size(path):
        
        sub_folder, total_size = [], []
        print(path)
        for folder in range(len(path)):
            if path[folder][0] != '/':
                sub_folder.append(path[folder])
        total = int(sub_folder[0][2])
        for folder in range(len(sub_folder)-1):
            # print(total, '--1')
            if sub_folder[folder][0] == sub_folder[folder+1][0]:
                
                # print(total, sub_folder[folder][2], sub_folder[folder+1][2])
                total += int(sub_folder[folder+1][2])
                folder += 1
                total = total 
            else:
                total_size.append(total)
                total = int(sub_folder[folder+1][2])

        total_size.append(total)    
                # same_path = groupby(path, lambda x : x[0])
                # for key, group in same_path:
                #     if key != '/':
                #         key_and_group = {key : list(group)}
                #         print('hehere')
                #     for i in list(group):
                #         print(i)
            # else:

        part1 = sum(size for size in total_size if  size < 100000)
        print(total_size)
        return part1


if __name__ == "__main__":
    data, result = get_data('testing.txt')
    # print(result)
    print(total_size(data))
    # print(sum(value for key,value in result.items() if  value < 100000))
    # print(min(value for key,value in result.items() if  value >= 30000000 - (70000000 - result['/'])))