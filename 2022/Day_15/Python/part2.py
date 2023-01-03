from collections import defaultdict
from time import time

#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = [line.lstrip('Sensor at x=').rstrip().split(':') for line in f.readlines()]

    for index, line in enumerate(lines):
        lines[index][0] = line[0].split(', y=')
        lines[index][1] = line[1].lstrip(' closest beacon is at x=')
        lines[index][1] = line[1].split(', y=')
        lines[index][0] = [int(lines[index][0][0]),int(lines[index][0][1])]
        lines[index][1] = [int(lines[index][1][0]),int(lines[index][1][1])]

scanners, beacons = [line[0] for line in lines], [line[1] for line in lines]

#Y = 20
Y=4000000
possible = set()

bcns = defaultdict(lambda: False)
scns = defaultdict(lambda: False)

for beacon in beacons:
    bcns[tuple(beacon)] = True
for scanner in scanners:
    scns[tuple(scanner)] = True

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def findPoints(scanner, beacon, Y):
    rch = manhattan(scanner, beacon) + 1
    x, y = scanner
    possible = set()

    for r in range(rch):
            possible.add((x-r, y-(rch-r)))
            possible.add((x+r, y-(rch-r)))
            possible.add((x-r, y+(rch-r)))
            possible.add((x+r, y+(rch-r)))
    return possible

def cleanPoints(points, Y):
    to_remove = set()
    for point in points:
        if point[0] < 0 or point[1] < 0 or point[0] > Y or point[1] > Y:
            to_remove.add(point)
    points = points.difference(to_remove)
    return points

def findAllPoints(scanners, beacons, Y):
    possible = set()
    for index, scanner in enumerate(scanners):
        possible.update(findPoints(scanner, beacons[index], Y))
    return possible

def findBeacon(scanners, beacons, bcns, scns, points):
    for index, point in enumerate(points):
        num, n = 0, len(scanners)
        for index, scanner in enumerate(scanners):
            if manhattan(scanner, beacons[index]) < manhattan(scanner, point) and not bcns[point] and not scns[point]:
                num += 1
            else:
                break
        if num == n:
            return point

def findTuningFreq(x, y):
    return 4000000 * x + y

start = time()
points = findAllPoints(scanners, beacons, Y)
end = time()
print('The number of points is ', len(points))
print('Time to find all points was ', end - start)
start = time()
points = cleanPoints(points, Y)
end = time()
print('The number of points now is ', len(points))
print('Time to clean points was ', end - start)
start = time()
x, y = findBeacon(scanners, beacons, bcns, scns, points)
end = time()
print('The distress beacon is at ', (x,y))
print('Time to find actual distress beacon was', end - start)
start = time()
ans = findTuningFreq(x, y)
end = time()
print('The final answer is, the tuning frequency is ', ans)
print('And that shouldn\'t take any time at all ', end - start)