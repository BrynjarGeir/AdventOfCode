from collections import defaultdict

prefix = '../data/'
#file = prefix + 'test'
file = prefix + 'complex'
#file = prefix + 'input'

with open(file) as f:
    lines = [line.rstrip() for line in f.readlines()]

# Populates a dict where key is type of blizzard (direction) and value is set of all placements of that type of blizzard (no doubles because then always doubles)
def populateGrid(lines):
    blizzards = defaultdict(lambda: set())
    start, end, bounds = None, None, (0, len(lines)-1, 0, len(lines[0])-1)
    for index, line in enumerate(lines):
        if not start:
            start = (index, line.index('.'))
        elif index == bounds[1]:
            end = (index, line.index('.'))
        else:
            for i,c in enumerate(line):
                if c != '.' and c != '#':
                    blizzards[c].add((index, i))
    return start, end, blizzards, bounds

# move any blizzard single blizzard to new position
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

# update all the blizzards and return the new grid
def updateGrid(blizzards, bounds):
    new_grid = defaultdict(lambda: [])
    for type in blizzards:
        for blizzard in blizzards[type]:
            new_point = movement(blizzard, type, bounds)
            new_grid[type].append(new_point)
    return new_grid

# Get the manhattan distance between two points
def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# find every possible next position
def findOpenNeighbours(blizzards, point, points):
    x,y = point
    blz = set([b for c in blizzards for b in blizzards[c]])
    nghbs = [(x+1, y), (x-1,y), (x,y+1), (x,y-1), (x,y)]
    nghbs = [point for point in nghbs if point not in blz and point in points]
    return nghbs

# Just returns the current state of blizzards (just a different format from blizzards)
def getCurrentState(blizzards):
    a,b,c,d = '>', '<', '^', 'v'
    a, b, c, d = tuple(sorted(list(blizzards[a]))), tuple(sorted(list(blizzards[b]))), tuple(sorted(list(blizzards[c]))), tuple(sorted(list(blizzards[d])))
    return a,b,c,d

# Update the seen state so that when standing in certain point you have a certain state of blizzards
def updateSeenState(seen, current_state, point):
    a,b,c,d = current_state
    blz = (a,b,c,d,point)
    seen.add(blz)
    return seen

# Get the point with the minimum distance
def getNode(points, dist):
    min_dist = float('inf')
    ans = None
    for point in points:
        if dist[point] < min_dist:
            ans = point
            min_dist = dist[point]
    return ans

# Like a normal bfs but checking visited is just a bit more complex (because of changing grid!)
def djikstra (blizzards, points, dist, prev, bounds):
    seen, q, minute = set(), [points[0]], -1
    while q:
        node = q.pop(0)
        blizzards = updateGrid(blizzards, bounds)
        current_state = getCurrentState(blizzards)
        nghbs = findOpenNeighbours(blizzards, node, points)
        minute += 1
        for nghb in nghbs:
            if (nghb, current_state) not in seen:
                q.append(nghb)
                seen.add((nghb, current_state))
                alt = minute
                if alt < dist[nghb]:
                    dist[nghb] = alt
                    prev[nghb] = node
    return dist, prev

# Get all possible visitable points
def getAllPoints(start, goal, bounds):
    points = [start]
    inner_points = [(i,j) for i in range(1, bounds[1]) for j in range(1,bounds[3])]
    points += inner_points + [goal]
    return points


start, goal, blizzards, bounds = populateGrid(lines)
points = getAllPoints(start, goal, bounds)
dist = defaultdict(lambda: float('inf'))
dist[start] = 0
prev = {}

dist, prev = djikstra(blizzards, points, dist, prev, bounds)

print(dist[goal])