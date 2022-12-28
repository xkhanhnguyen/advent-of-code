from collections import namedtuple
import re

with open('input.txt') as inputfile:
    lines = [b.strip() for b in inputfile.readlines()]

# Sensor at x=20, y=1: closest beacon is at x=15, y=3
Sensor = namedtuple('Sensor', 'x, y')
Beacon = namedtuple('Beacon', 'x, y')

sbList = []
for line in lines:
    numbers = [int(n) for n in re.findall('-?\d+', line)]
    sbList.append((Sensor(numbers[0], numbers[1]), Beacon(numbers[2], numbers[3])))

def getDistance(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)

blocked = set()
rowOfInterest = 2000000
for sensor, beacon in sbList:
    distance = getDistance(sensor, beacon)
    
    if rowOfInterest - sensor.y > distance:
        continue

    taken = abs(rowOfInterest - sensor.y)
    rest = distance - taken

    for x in range(sensor.x - rest, sensor.x + rest + 1):
        blocked.add(x)

for sensor, beacon in sbList:
    if beacon.x in blocked and beacon.y == 2000000:
        blocked.remove(beacon.x)

print(f'part 1: {len(blocked)}')

# part 2

size = 5000 # 10000 -> 177 blocks to check, 5000 -> 333 blocks to check
reviewThese = []
for r in range(4000000 // size):
    row = r * size
    for i in range(4000000 // size):
        isAllIn = False
        ul = Beacon((size * i),        row)
        ur = Beacon((size * i + size), row)
        ll = Beacon((size * i),        row + size)
        lr = Beacon((size * i + size), row + size) 
        corners = [ul, ur, ll, lr]
        for sensor, beacon in sbList:
            sensorDistance = getDistance(sensor, beacon)
            enclosed = [getDistance(c, sensor) <= sensorDistance for c in corners]
            if all(enclosed):
                isAllIn = True
                break
        if not isAllIn:
            reviewThese.append(corners)


def isRowFull(rowOfInterest, left, right):
    blocked = set()
    for sensor, beacon in sbList:
        distance = getDistance(sensor, beacon)
        
        if rowOfInterest - sensor.y > distance:
            continue

        taken = abs(rowOfInterest - sensor.y)
        rest = distance - taken

        sensorLower = sensor.x - rest
        sensorUpper = sensor.x + rest
        if sensorUpper < left:
            continue
        if sensorLower > right:
            continue

        start = max(left, sensor.x - rest)
        end = min(right, sensor.x + rest)
        for x in range(start, end + 1):
            blocked.add(x)

    if len(blocked) == (right - left) + 1:
        return True, -1, -1
    else:
        # find the missing number
        missing = [x for x in range(left, right + 1) if not x in blocked]
        return (False, rowOfInterest, missing[0])


found = False
# Having run the program already, I know that the answer
# is in reviewThese[299].
for ul, ur, ll, lr in reviewThese[299:]:
    for row in range(ul.y, ll.y + 1):
        left = ul.x
        right = ur.x
        isfull = isRowFull(row, left, right)
        if not isfull[0]:
            answerRow = isfull[1]
            answerCol = isfull[2]
            found = True
            break
    if found:
        break

print(f'part 2: {answerCol * 4000000 + answerRow}')



