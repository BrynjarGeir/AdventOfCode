#from collections import deque

#file = '../data/test'
#file = '../data/larger_test'
file = '../data/input'


with open(file) as f:
    lines = [line.rstrip().split() for line in f.readlines()]

for i in range(len(lines)):
    if len(lines[i]) == 2:
        lines[i][1] = int(lines[i][1])

def distOK(a, b):
    return abs(a - b) <= 1

x = 1
crtY, crtX = 0, 0
ans = set()

for line in lines:
    if distOK(crtX, x):
        ans.add((crtY, crtX))
    
    crtX += 1
    if crtX == 40:
        crtX = 0
        crtY += 1

    if distOK(crtX, x):
        ans.add((crtY, crtX))

    if line[0] == 'noop':
        continue

    x += line[1]
    crtX += 1
    if crtX == 40:
        crtX = 0
        crtY += 1

    if distOK(crtX, x):
        ans.add((crtY, crtX))
    


grid = [['.' for _ in range(40)] for _ in range(6)]

for marked in ans:
    grid[marked[0]][marked[1]] = '#'

for line in grid:
    print(line)


