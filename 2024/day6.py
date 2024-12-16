import numpy as np, re
from tqdm import tqdm
input_path = './data/day6/input.txt'
test_path = './data/day6/test.txt'

with open(input_path, 'r') as f:
    lines = f.readlines()
    grid = [list(line.strip()) for line in lines]
    grid = np.array(grid)

rotMat = np.array([[0, -1], [1, 0]])

def outOfBounds(a, b, r, c):
    return a < 0 or b < 0 or a >= r or b >= c

def getPointsOfInterest(grid):
    blocks, startingGuard = set(), (-1, -1)
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "#":
                blocks.add((i, j))
            elif grid[i][j] == "^":
                startingGuard = (i, j)
    return startingGuard, blocks, (rows, cols)

def simulatePart1(guard, grid, bounds):
    r, c = bounds
    direction = np.array((-1, 0))
    x, y = guard
    steps = set([(x, y)])
    
    while 0 <= x < r and 0 <= y < c:

        steps.add((x, y))
        a, b = x + direction[0], y + direction[1]
        if (a, b) in grid:
            direction = np.matmul(direction, rotMat)
            a, b = x + direction[0], y + direction[1]
        x, y = a, b
    return len(steps)

def simulatePart2(guard, grid, bounds):
    r, c = bounds
    direction = np.array((-1, 0))
    x, y = guard
    minX, maxX, minY, maxY = np.inf, -np.inf, np.inf, -np.inf
    states = set([(x, y, direction[0], direction[1])])
    while 0 <= x < r and 0 <= y < c:
        states.add((x, y, direction[0], direction[1]))
        a, b = x + direction[0], y + direction[1]
        if (a, b) in grid:
            direction = np.matmul(direction, rotMat)
            a, b = x + direction[0], y + direction[1]
        x, y = a, b

    loops, tries = set([]), set([])
    for state in states:
        cx, cy = state[0], state[1]
        ps = [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1), (cx-1, cy-1), (cx-1, cy+1), (cx+1, cy-1), (cx+1, cy+1)]
        for p in ps:
            if not outOfBounds(*p, r, c):
                tries.add(p)

    tries = tries - set([guard]) - grid
   
    for p in tqdm(tries):
        rx, ry = p
        x, y = guard
        cgrid = grid.copy()
        cgrid.add(p)
        direction = np.array((-1, 0))
        seen = set([])
        while 0 <= x < r and 0 <= y < c:
            a, b = x + direction[0], y + direction[1]
            while (a, b) in cgrid:
                direction = np.matmul(direction, rotMat)
                a, b = x + direction[0], y + direction[1]
            x, y = a, b
            if (x, y, direction[0], direction[1]) in seen:
                loops.add((rx,ry))
                break
            seen.add((x, y, direction[0], direction[1]))
    return len(loops)

guard, grid, bounds = getPointsOfInterest(grid)
p1 = simulatePart1(guard, grid, bounds)
p2 = simulatePart2(guard, grid, bounds)

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')