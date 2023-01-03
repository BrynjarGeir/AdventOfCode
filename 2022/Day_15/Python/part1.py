from collections import defaultdict

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

#y = 10
y=2000000
impossible = set()

#minX = min([minX, lines[index][0][0] + lines[index][1][0], lines[index][0][0] - lines[index][1][0]])
#maxX = max([maxX, lines[index][0][0] + lines[index][1][0], lines[index][0][0] - lines[index][1][0]])
minX, maxX, = float('inf'), -float('inf')

bcns = defaultdict(lambda: False)

for beacon in beacons:
    bcns[tuple(beacon)] = True

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def reach(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

reachesY = []
for index, scanner in enumerate(scanners):
    rch = reach(scanner, beacons[index])
    if scanner[1] + rch >= y and scanner[1] - rch <= y:
        reachesY.append(index)
    elif scanner[1] - rch >= y and scanner[1] + rch <= y:
        reachesY.append(index)
    minX = min([minX, scanner[0] + rch, scanner[0] - rch])
    maxX = max([maxX, scanner[0] + rch, scanner[0] - rch])

for c in range(minX, maxX+1):
    for index in reachesY:
        if manhattan(scanners[index], beacons[index]) >= manhattan(scanners[index], (c, y)) and not bcns[(c,y)]:
            impossible.add((c,y))
            break

print(len(impossible))
