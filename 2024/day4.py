import numpy as np, re

input_path = './data/day4/input.txt'
test_path = './data/day4/test.txt'

with open(input_path, 'r') as f:
    lines = f.readlines()

lines = [line.rstrip() for line in lines]
grid = np.array(lines)
xmas = 'XMAS'
rows, cols = len(grid), len(grid[0])

directions = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
    [1, 1],
    [-1, 1],
    [1, -1],
    [-1, -1]
]

def is_valid(x,  y):
    return 0 <= x < rows and 0 <= y < cols

def search(x,  y, dx, dy):
    for i in range(len(xmas)):
        cx, cy = x + i * dx, y + i * dy
        if not is_valid(cx, cy) or grid[cx][cy] != xmas[i]:
            return False
    return True

counter = 0

for x in range(rows):
    for y in range(cols):
        if grid[x][y] == xmas[0]:
            for (dx, dy) in directions:    
                if search(x, y, dx, dy):
                    counter += 1

print(f'Part 1: {counter}')

mas = 'MAS'

def validMas(x, y):
    return 0 < x < rows-1 and 0 < y < cols-1

def foundMas(x, y):
    a, b, c, d = grid[x-1][y-1], grid[x+1][y+1], grid[x-1][y+1], grid[x+1][y-1]

    e = (a == 'M' and b == 'S') or (a == 'S' and b == 'M')
    f = (c == 'M' and d == 'S') or (c == 'S' and d == 'M')

    return e and f
    

counter = 0

for x in range(rows):
    for y in range(cols):
        if grid[x][y] == mas[1] and validMas(x, y) and foundMas(x, y):
            counter += 1

print(f'Part 2: {counter}')
