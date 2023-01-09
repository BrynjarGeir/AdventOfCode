from collections import defaultdict

prefix = '../data/'
file = prefix + 'test'
#file = prefix + 'complex'
#file = prefix + 'input'

with open(file) as f:
    lines = f.readlines()

def populateGrid(lines):
    blizzards = defaultdict(lambda: [])
    start,end, n, bounds = None, None, n, (0, len(lines)-1, 0, len(lines[0])-1)
    for index, line in enumerate(line):
        if not start:
            start = (0, line.index('.'))
        elif index == n-1:
            end = (n-1, line.index('.'))
        else:
            for i,c in enumerate(line):
                if c != '.' and c != '#':
                    blizzards[c].append((index, i))
    return start, end, blizzards, bounds

def movement(point, type, bounds):
    move = {'>':(0,1), '<':(0,-1), 'v':(1,0), '^':(-1,0)}
    xmin, xmax, ymin, ymax = bounds
    new_point = (point[0] + move[type][0], point[1] + move[type][1])
    if new_point[0] <= xmin:
        return (xmax-1, point[1])
    elif new_point[0] >= xmax:
        return (xmin+1, point[1])
    elif new_point[1] <= ymin:
        return (point[0], ymax-1)
    elif new_point[1] >= ymax:
        return (point[0], ymin+1)
    else:
        return new_point

def updateGrid(blizzards, bounds):
    new_grid = defaultdict(lambda: [])
    for type in blizzards:
        for blizzard in blizzards[type]:
            new_point = movement(blizzard, type, bounds)
            new_grid[type].append(new_point)
    return new_grid