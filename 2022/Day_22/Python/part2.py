import re
from time import time, sleep
from collections import defaultdict

#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = [line.rstrip() for line in f.readlines()]

grid = lines[:-2]
instructions = lines[-1]

instructions = re.split('(R|L)', instructions)

instructions = [int(i) if i.isdigit() else i for i in instructions]

# Loop over the input and note tiles and walls
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

# Just helping with figuring out the sidelength
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

# Walk a certain distance in a certain direction
def walk(position, distance, facing, corners, sidelength, move, walls, tiles):
    for _ in range(distance):
        direction = move[facing]
        if (position[0]+direction[0], position[1]+direction[1]) in tiles:
            position = (position[0]+direction[0], position[1]+direction[1])
        elif (position[0]+direction[0], position[1]+direction[1]) in walls:
            break
        else:           
            index = getOrderOnSide(position, sidelength)
            face = getFace(position, corners, sidelength)
            new_position = getSide(face, facing, sidelength)[index]

            if new_position in tiles:
                new_face = getFace(new_position, corners, sidelength)
                facing = getFacing(face, new_face)
                position = new_position
            else:
                break

    return position, facing

# Finding our sidelength of each face to simplify a lot of other stuff
def getSideLength(rnge):
    sidelength = min([rnge[0][1][i] - rnge[0][0][i] + 1 for i in range(len(rnge[0][0]))] + [rnge[1][1][i] - rnge[1][0][i] + 1 for i in range(len(rnge[1][0]))])
    return sidelength

# Turn and thus change the direction we are facing but not our position
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

# We follow every instruction from input, basically just calling walk, turn
def follow_instructions(corners, sidelength, instructions = instructions, facing = 0, move = [(0,1), (1,0), (0,-1), (-1,0)], walls = None, tiles = None, position = None):
    for instruction in instructions:
        if isinstance(instruction, int):
            position, facing = walk(position, instruction, facing, corners, sidelength, move, walls, tiles)
        else:
            facing = turn(facing, instruction)
    return (position[0]+1, position[1]+1), facing

# After having followed the instructions we can simply 
def getPassword(position, facing):
    password = position[0] * 1000 + position[1] * 4 + facing
    return password

# Check if point is in the corner of face
def isCornerPoint(walls, tiles, sidelength, point):
    if point in walls or point not in tiles:
        return False
    elif ((point[0] % sidelength) == 0 and (point[1] % sidelength) == 0) or ((point[0]+1) % sidelength == 0 and (point[1]+1) % sidelength == 0):
        return True
    elif ((point[0]+1) % sidelength == 0 and point[1] % sidelength == 0) or ((point[0]+1) % sidelength == 0 and (point[1]+1) % sidelength == 0):
        return True
    return False

# Check if point is on the side of face (outer point but not cornerpoint)
def isSidePoint(walls, tiles, sidelength, point):
    if point in walls or point not in tiles or isCornerPoint(walls, tiles, sidelength, point):
        return False
    elif ((point[0] % sidelength) == 0 and not (point[1] % sidelength) == 0) or (not (point[0] % sidelength) == 0 and (point[1] % sidelength) == 0):
        return True
    elif (((point[0]+1) % sidelength) == 0 and not ((point[1] + 1) % sidelength) == 0) or (not ((point[0]+1) % sidelength) == 0 and ((point[1] + 1) % sidelength) == 0):
        return True
    return False

# Get all possible points if going over side with direction <-- gotta change this for the input because of shape
def getSide(face, direction, sidelength):
    side = None
    if face == 1 and direction == 2:
        side = [(x, 0) for x in range(sidelength*3-1, sidelength * 2-1, -1)]
    elif face == 1 and direction == 3:
        side = [(0, y) for y in range(sidelength*2,sidelength*3)]
    elif face == 2 and direction == 0:
        side = [(x, sidelength*2-1) for x in range(sidelength*3-1,sidelength*2-1,-1)]
    elif face == 2 and direction == 1:
        side = [(x, sidelength*2-1) for x in range(sidelength, sidelength*2)]
    elif face == 2 and direction == 3:
        side = [(sidelength*4-1, y) for y in range(sidelength)]
    elif face == 3 and direction == 0:
        side = [(sidelength-1, y) for y in range(sidelength*2,sidelength*3)]
    elif face == 3 and direction == 2:
        side = [(sidelength*2, y) for y in range(sidelength)]
    elif face == 4 and direction == 0:
        side = [(x, sidelength*3-1) for x in range(sidelength-1, -1, -1)]
    elif face == 4 and direction == 1:
        side = [(x, sidelength-1) for x in range(sidelength*3, sidelength*4)]
    elif face == 5 and direction == 2:
        side = [(x, sidelength) for x in range(sidelength-1, -1, -1)]
    elif face == 5 and direction == 3:
        side = [(x, sidelength) for x in range(sidelength, sidelength*2)]
    elif face == 6 and direction == 0:
        side = [(sidelength*3-1, y) for y in range(sidelength, sidelength*2)]
    elif face == 6 and direction == 1:
        side = [(0, y) for y in range(sidelength*2, sidelength*3)]
    elif face == 6 and direction == 2:
        side = [(0, y) for y in range(sidelength, sidelength*2)]

    return side

# getSide just returns all sides on a specific edge and this function returns the index on the new edge for specific point
def getOrderOnSide(point, sidelength):
    x,y = point
    x %= sidelength
    y %= sidelength
    if x == 0 or x + 1 == sidelength:
        return y
    elif y == 0 or y + 1 == sidelength:
        return x

# Returns a dictionary that has the upper right corner points of every face (key 1-6 and points value)
def getCornerPoints(sidelength):
    corners = {}
    corners[1] = (0, sidelength)
    corners[2] = (0, sidelength*2)
    corners[3] = (sidelength, sidelength)
    corners[4] = (sidelength*2, sidelength)
    corners[5] = (sidelength*2, 0)
    corners[6] = (sidelength*3, 0)
    return corners

# Find the face that a certain point is on
def getFace(point, corners, sidelength):
    x, y = point
    for corner in corners:
        if x < corners[corner][0] + sidelength and y < corners[corner][1] + sidelength and x >= corners[corner][0] and y >= corners[corner][1]:
            return corner
    return None

# Update facing if we switch the face we are on       
def getFacing(pre_face, post_face):
    if pre_face == 1:
        return 0
    elif pre_face == 2:
        if post_face == 3 or post_face == 4:
            return 2
        else:
            return 3
    elif pre_face == 3:
        if post_face == 2:
            return 3
        else:
            return 1
    elif pre_face == 4:
        return 2
    elif pre_face == 5:
        return 0
    elif pre_face == 6:
        if post_face == 1 or post_face == 2:
            return 1
        else:
            return 3

start = time()
walls, tiles, rows, cols, position = populateWallsTiles(grid)
rnge = getRange(walls, tiles, rows, cols)
sidelength = getSideLength(rnge)
corners = getCornerPoints(sidelength)

position, facing = follow_instructions(corners, sidelength, walls=walls, tiles=tiles, position=position)

password = getPassword(position, facing)
end = time()

print('Our final password is', password)
print('Our final position is',position,'and we are facing',facing)
print('It took us', end - start,'seconds to arrive at that conclusion.')