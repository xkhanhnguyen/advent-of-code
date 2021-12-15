import math
from collections import Counter
def get_data(file_name):
    """
    Read in the input file

    Args
    ----
    file_name: input file. 
    example get_data('input.txt')

    Returns
    -------
    a list of points
        
    """

    with open(file_name) as f:
        data = []
        for line in f.read().splitlines():
            start, end = tuple(line.split('->'))
            start = tuple([int(x) for x in start.strip().split(',')])
            end = tuple([int(x) for x in end.strip().split(',')])
            data.append((start, end))
    return data

def check_lines(lines):
    """
    Read in the input file

    Args
    ----
    file_name: input file. 
    example get_data('input.txt')

    Returns
    -------
    all points for only horizontal and vertical lines:
    lines where either x1 = x2 or y1 = y2.
        
    """
    
    filter_lines = []
    for l in lines:
        start, end = l
        if start[1] == end[1] or start[0] == end[0]:
            filter_lines.append(l)
    return filter_lines

def get_point(line):
    """
    To get all points of all the lines from check_lines

    Args
    ----
    all points satisfied the condition of part 1

    Returns
    -------
    All entries and covered points
    For example: An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    
    """
    point = []
    start, end = line
    rise = end[1] - start[1]
    run = end[0] - start[0]
    common_denominator = math.gcd(rise, run)
    x_slope = int(run / common_denominator)
    y_slope = int(rise / common_denominator)
    current_point = start
    while current_point != end:
        point.append(current_point)
        x, y = current_point
        current_point = (x + x_slope, y + y_slope)
    point.append(current_point)    
    return point


def get_points_on_all_lines(lines):
    """
    To get all points of all the lines from check_lines

    Args
    ----
    all points satisfied the condition of part 1

    Returns
    -------
    All entries and covered points
    For example: An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    
    """
    all_points = []
    for l in lines:
        all_points += get_point(l)
    return all_points


def hydrothermal_venture(point):
    """
    Points that at least 2 lines overlap 
    
    Args
    ----
    all points from get_points_on_all_lines

    Returns
    -------
    All entries and covered points
    For example: An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
    
    """
    colliding_points = []
    for p, count in Counter(point).items():
        if count > 1:
            colliding_points.append(p)
    return len(colliding_points)


if __name__ == "__main__":
    input = get_data('input.txt')

    # part 1
    filtered_lines = check_lines(input)
    all_points = get_points_on_all_lines(filtered_lines)
    print('part 1:', hydrothermal_venture(all_points))
    
    # part 2
    """
    Because part 2 consider diagonal lines as well,
    we skipped the check_lines
    
    """
    part2_points = get_points_on_all_lines(input)
    print('part 2:', hydrothermal_venture(part2_points))



