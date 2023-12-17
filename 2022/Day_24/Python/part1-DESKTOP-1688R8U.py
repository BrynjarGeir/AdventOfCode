from collections import defaultdict

prefix = '../data/'
file = prefix + 'test'
#file = prefix + 'complex'
#file = prefix + 'input'

with open(file) as f:
    lines = f.readlines()

def populateGrid(lines):
    blizzards = defaultdict(lambda: [])
    points = set()
    start,end, n, bounds = None, None, len(lines)-1, (0, len(lines)-1, 0, len(lines[0])-1)
    for index, line in enumerate(line):
        if index == 0:
            start = (0, line.index('.'))
        elif index == n-1:
            end = (n-1, line.index('.'))
        else:
            for i,c in enumerate(line):
                if c != '.' and c != '#':
                    blizzards[c].append((index, i))
                if c != '#':
                    points.append((index, i))

    return start, end, blizzards, bounds, points

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

def getAdj(blizzards, start, end, pos, bounds):
    adj = []
    nghbs = [(pos[0]+x, pos[1]+y) for (x,y) in [(-1,0), (1,0), (0, 0), (0,-1), (0,1)] if (pos[0]+x > 0 and pos[0]+x < bounds[1] and pos[1]+y > 0 and pos[y]+y < bounds[3]) or ((pos[0]+x, pos[1]+y) == start or (pos[0]+x, pos[1]+y) == end)]
    for nghb in nghbs:
        if nghb not in blizzards:
            adj.append(nghb)
    
    return adj

def bfsOfGraph(blizzards, start, end, pos, bounds, points):
    m, n = bounds[1], bounds[3]
    bfs_traversal = []
    vis = defaultdict(lambda: False)
    for point in points:
        if not vis[point]:
            q = []
            vis[point] = True
            q.append(point)

            while q:
                g_node = q.pop(0)
                bfs_traversal.append(g_node)
                new_blizzards = updateGrid(blizzards, bounds)
                adj = getAdj(new_blizzards, start, end, pos, bounds)
                blizzards = new_blizzards
                for it in adj:
                    if it not in vis:
                        vis[it] = True
                        q.append(it)
    return bfs_traversal
