import re
from time import time

#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = [line.rstrip() for line in f.readlines()]

grid = lines[:-2]
instructions = lines[-1]

instructions = re.split('(R|L)', instructions)

instructions = [int(i) if i.isdigit() else i for i in instructions]

def populateWallsTiles(grid):
    walls, tiles = set(), set()
    position, rows,cols = None, -1, -1
    for i,m in enumerate(grid):
        for j,n in enumerate(m):
            if n == '.':
                if not position:
                    position = (i,j)
                tiles.add((i,j))
            elif n == '#':
                walls.add((i,j))
        rows, cols = max(rows, i+1), max(cols, j+1)
    return walls, tiles, rows, cols, position

def getRange(walls, tiles, rows, cols):
    min_cols, max_cols, min_rows, max_rows = [None for _ in range(cols)], [None for _ in range(cols)], [None for _ in range(rows)], [None for _ in range(rows)]

    for row in range(rows):
        min_rows[row] = min([it[1] for it in walls if it[0] == row] + [it[1] for it in tiles if it[0] == row])
        max_rows[row] = max([it[1] for it in walls if it[0] == row] + [it[1] for it in tiles if it[0] == row])

    for col in range(cols):
        min_cols[col] = min([it[0] for it in walls if it[1] == col] + [it[0] for it in tiles if it[1] == col])
        max_cols[col] = max([it[0] for it in walls if it[1] == col] + [it[0] for it in tiles if it[1] == col])

    rnge = ((min_rows, max_rows), (min_cols, max_cols))

    return rnge

def walk(position, distance, direction, walls, tiles, rnge):
    (min_cols, max_cols), (min_rows, max_rows) = rnge
    for _ in range(distance):
        if (position[0]+direction[0], position[1]+direction[1]) in tiles:
            position = (position[0]+direction[0], position[1]+direction[1])
        elif (position[0]+direction[0], position[1]+direction[1]) in walls:
            break
        elif direction[0] == -1 and (max_rows[position[1]], position[1]) in tiles:
            position = (max_rows[position[1]], position[1])
        elif direction[0] == 1 and (min_rows[position[1]], position[1]) in tiles:
            position = (min_rows[position[1]], position[1])
        elif direction[1] == -1 and (position[0], max_cols[position[0]]) in tiles:
            position = (position[0], max_cols[position[0]])
        elif direction[1] == 1 and (position[0], min_cols[position[0]]) in tiles:
            position = (position[0], min_cols[position[0]])
        else:
            break
    return position

def turn(facing, rotate):
    if rotate == 'R':
        facing += 1
    else:
        facing -= 1

    if facing >= 4:
        facing -= 4

    elif facing < 0:
        facing += 4
    
    return facing

def follow_instructions(instructions = instructions, facing = 0, move = [(0,1), (1,0), (0,-1), (-1,0)], walls = None, tiles = None, position = None, rnge = None):
    for instruction in instructions:
        if isinstance(instruction, int):
            position = walk(position, instruction, move[facing], walls, tiles, rnge)
        else:
            facing = turn(facing, instruction)
    return (position[0]+1, position[1]+1), facing

def getPassword(position, facing):
    password = position[0] * 1000 + position[1] * 4 + facing
    return password

start = time()
walls, tiles, rows, cols, position = populateWallsTiles(grid)
rnge = getRange(walls, tiles, rows, cols)

position, facing = follow_instructions(walls=walls, tiles=tiles, position=position, rnge=rnge)

password = getPassword(position, facing)
end = time()

print('Password is', password, '!')
print('It took us:',end - start,'seconds to arrive at that.')


