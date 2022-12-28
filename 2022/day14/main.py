import re


def get_data(filename):
    with open(filename) as f:
        data = [line.rstrip() for line in f]
    return data

def process_input(lines):
    s_map = {(500, 0): 'x'}

    for this_line in lines:
        x_index = 2
        y_index = 3

        rock_coords = [int(y) for y in re.split(",| -> ", this_line)]
        

        while y_index < len(rock_coords):
            current_x, current_y = [rock_coords[x_index - 2], rock_coords[y_index - 2]]
            end_x, end_y = [rock_coords[x_index], rock_coords[y_index]]

            x_diff = end_x - current_x
            y_diff = end_y - current_y
            x_inc = y_inc = 0
            if x_diff:
                x_inc = x_diff//abs(x_diff) 
                end_x += x_inc  
            if y_diff:
                y_inc = y_diff//abs(y_diff)
                end_y += y_inc

            # Add lines from current (start) to end
            while current_x != end_x or current_y != end_y:
                s_map[(current_x, current_y)] = "#"
                current_x += x_inc
                current_y += y_inc

            x_index += 2
            y_index += 2
    return s_map


def pour_sand(s_map, c_floor):
    origin = (500, 0)
    sand_x, sand_y = origin
    max_y = max([k[1] for k in s_map])

    while True:
        if sand_y > max_y:
            return s_map, False
        elif (sand_x, sand_y + 1) not in s_map:
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in s_map:
            sand_x -= 1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in s_map:
            sand_x += 1
            sand_y += 1
        elif (sand_x, sand_y) == origin:
            s_map[(sand_x, sand_y)] = 'o'
            return sand_map, False
        else:
            s_map[(sand_x, sand_y)] = 'o'
            break

    return sand_map, True


def display_map(s_map):
    min_x = min([k[0] for k in s_map]) - 1
    max_x = max([k[0] for k in s_map]) + 2
    min_y = min([k[1] for k in s_map]) - 1
    max_y = max([k[1] for k in s_map]) + 2

    for this_row in range(min_y, max_y):
        row_print = ''
        for this_col in range(min_x, max_x):
            if (this_col, this_row) not in s_map.keys():
                row_print += '+'
            elif s_map[(this_col, this_row)] == '#':
                row_print += '#'
            elif s_map[(this_col, this_row)] == 'o':
                row_print += 'o'
            elif s_map[(this_col, this_row)] == 'x':
                row_print += 'x'
        print(row_print)



if __name__ == "__main__":
    data = get_data('input.txt')
    sand_map = process_input(data)
    cave_floor = max([k[1] for k in sand_map]) + 2

    keep_going = True
    
    while keep_going:
        sand_map, keep_going = pour_sand(sand_map, cave_floor)
    
    display_map(sand_map)

    sand_count = len([sand_map[f] for f in sand_map if sand_map[f] == 'o'])
    print(f"Result: {sand_count}")