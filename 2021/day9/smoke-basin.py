import os
import scipy
from scipy import ndimage
import numpy as np
def get_data(filename):
    current_dir = os.path.dirname(__file__)
    full_file_path = os.path.join(current_dir, filename)
    with open(full_file_path) as input_file:
        parsed_input = []
        for line in input_file.read().splitlines():
            parsed_input.append([int(x) for x in line])
    return parsed_input

class Basin:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid) # to check up and down
        self.width = len(grid[0]) # to check left and right

    def find_low_point(self):
        low_point = {} # key (x,y) cordinate, value is the low_point
        for y in range(0, self.height):
            for x in range(0, self.width):
                value = self.grid[y][x] # rows are the heights
                adjacent_location = []
                if x > 0: # left value
                    adjacent_location.append(self.grid[y][x-1])
                if x < self.width - 1:  # right column
                    adjacent_location.append(self.grid[y][x+1])
                if y > 0: # up
                    adjacent_location.append(self.grid[y-1][x])
                if y < self.height - 1:  # down
                    adjacent_location.append(self.grid[y+1][x])
                    
                if min(adjacent_location) > value:
                    low_point[(x,y)] = value
        
        risk_level = []
        for i in low_point.values():
            risk_level += [i + 1] 
        return sum(risk_level)        

def part2(flows):
    dl = len(flows[0])
    flows = np.array(flows)
    flows = flows.reshape(-1, dl)
    
    label, num_label = ndimage.label(flows < 9)
    
    size = np.bincount(label.ravel())
    
    top3 = sorted(size[1:], reverse=True)[:3]

    return np.prod(top3)


    
if __name__ == '__main__':
    flows = get_data('input.txt')
    basin = Basin(flows)
    risk_level = basin.find_low_point()
   
    print('part 1:', risk_level)
    print('part 2:', part2(flows))