from collections import defaultdict

#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = [[it for it in item.rstrip().split(' -> ')] for item in f.readlines()]

    lines = [[l.split(',') for l in line] for line in lines]

    lines = [[[int(l[0]), int(l[1])] for l in line] for line in lines]

grid = defaultdict(lambda: False)
start_pos = (500, 0)
grid[start_pos] = True
minX, maxX, maxY, units = 500, 500, 0, 0

for line in lines:
    for i in range(len(line)-1):
        curr, nxt = line[i], line[i+1]
        if curr[0] == nxt[0]:
            if nxt[1] > curr[1]:
                for i in range(curr[1], nxt[1]+1):
                    grid[(curr[0], i)] = True
                    minX = min(minX, curr[0])
                    maxX = max(maxX, curr[0])
                    maxY = max(maxY, i)
            else:
                for i in range(nxt[1], curr[1]+1):
                    grid[(curr[0], i)] = True
                    minX = min(minX, curr[0])
                    maxX = max(maxX, curr[0])
                    maxY = max(maxY, i)
        else:
            if nxt[0] > curr[0]:
                for i in range(curr[0], nxt[0]+1):
                    grid[(i, curr[1])] = True
                    minX = min(minX, i)
                    maxX = max(maxX, i)
                    maxY = max(maxY, curr[1])
            else:
                for i in range(nxt[0], curr[0]+1):
                    grid[(i, curr[1])] = True
                    minX = min(minX, i)
                    maxX = max(maxX, i)
                    maxY = max(maxY, curr[1])


while True:
    curr = start_pos
    out_of_bounds = False

    while True:
        if not grid[(curr[0], curr[1]+1)]:
            curr = (curr[0], curr[1]+1)
        elif not grid[(curr[0]-1, curr[1]+1)]:
            curr = (curr[0]-1, curr[1]+1)
        elif not grid[(curr[0]+1, curr[1]+1)]:
            curr = (curr[0]+1, curr[1]+1)
        else:
            units += 1
            grid[curr] = True
            break

        if curr[0] < minX or curr[0] > maxX or curr[1] > maxY:
            out_of_bounds = True
            break
    
    if out_of_bounds:
        break

print(units)