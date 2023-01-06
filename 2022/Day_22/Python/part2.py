import re
from time import time
from collections import defaultdict

file = '../data/test'
#file = '../data/input'

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

def getSideLength(rnge):
    sidelength = min([rnge[0][1][i] - rnge[0][0][i] + 1 for i in range(len(rnge[0][0]))] + [rnge[1][1][i] - rnge[1][0][i] + 1 for i in range(len(rnge[1][0]))])
    return sidelength

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

def isCornerPoint(walls, tiles, sidelength, point):
    if point in walls or point not in tiles:
        return False
    elif ((point[0] % sidelength) == 0 and (point[1] % sidelength) == 0) or ((point[0]+1) % sidelength == 0 and (point[1]+1) % sidelength == 0):
        return True
    elif ((point[0]+1) % sidelength == 0 and point[1] % sidelength == 0) or ((point[0]+1) % sidelength == 0 and (point[1]+1) % sidelength == 0):
        return True
    return False

def isSidePoint(walls, tiles, sidelength, point):
    if point in walls or point not in tiles or isCornerPoint(walls, tiles, sidelength, point):
        return False
    elif ((point[0] % sidelength) == 0 and not (point[1] % sidelength) == 0) or (not (point[0] % sidelength) == 0 and (point[1] % sidelength) == 0):
        return True
    elif (((point[0]+1) % sidelength) == 0 and not ((point[1] + 1) % sidelength) == 0) or (not ((point[0]+1) % sidelength) == 0 and ((point[1] + 1) % sidelength) == 0):
        return True
    return False

def findCorrespondingPoint(walls, tiles, sidelength, point):
    return

def findCorrespondingPoints(walls, tiles, sidelength):
    correspondingPoints = {}

def getSide(face, direction, sidelength):
    if face == 1 and direction == 0:
        side = [(x,sidelength * 2) for x in range(sidelength)]
    elif face == 1 and direction == 1:
        side = [(0, y) for y in range(sidelength*2,sidelength*3)]
    elif face == 1 and direction == 2:
        side = [(x, sidelength*3-1) for x in range(sidelength)]
    elif face == 1 and direction == 3:
        side = [(sidelength-1, y) for y in range(sidelength*2,sidelength*3)]
    

# Just the cornerpoint if walking in certain direction off of certain face
def findProjection(point, direction, outer_points, face):
    next_face = getCorrespondingFace()[(face, direction)]

def getCornerPoints(sidelength):
    corners = {}
    corners[1] = (0, sidelength*2)
    corners[2] = (sidelength, 0)
    corners[3] = (sidelength, sidelength)
    corners[4] = (sidelength, sidelength*2)
    corners[5] = (sidelength*2, sidelength*2)
    corners[6] = (sidelength*2, sidelength*3)
    return corners

def getOpenOuterPoints(walls, starting_point, sidelength):
    outer_points = set()
    for i in range(sidelength):
        for j in range(sidelength):
            point = (starting_point[0]+i, starting_point[1]+j)
            if point in walls:
                continue
            elif isCornerPoint(walls, tiles, sidelength, point) or isSidePoint(walls, tiles, sidelength, point):
                outer_points.add(point)
    return outer_points

# Find the face that a certain point is on
def getFace(point, faces):
    i = 1
    for face in faces:
        if point in faces[face]:
            return i
        i += 1

def getCorrespondingFace():
    cubes = {}
    cubes[(1, 0)], cubes[(1,1)], cubes[(1,2)], cubes[(1,3)] = 6, 4, 3, 2
    cubes[(2, 0)], cubes[(2,1)], cubes[(2,2)], cubes[(2,3)] = 3, 5, 6, 1
    cubes[(3, 0)], cubes[(3,1)], cubes[(3,2)], cubes[(3,3)] = 4, 5, 2, 1
    cubes[(4, 0)], cubes[(4,1)], cubes[(4,2)], cubes[(4,3)] = 6, 5, 3, 1
    cubes[(5, 0)], cubes[(5,1)], cubes[(5,2)], cubes[(5,3)] = 6, 2, 3, 4
    cubes[(6, 0)], cubes[(6,1)], cubes[(6,2)], cubes[(6,3)] = 1, 2, 5, 4

    return cubes

def getCubesPoint():
    points = {}

start = time()
walls, tiles, rows, cols, position = populateWallsTiles(grid)
rnge = getRange(walls, tiles, rows, cols)

sidelength = getSideLength(rnge)

position, facing = follow_instructions(walls=walls, tiles=tiles, position=position, rnge=rnge)

password = getPassword(position, facing)
end = time()

cubes = {}
cornerPoints = getCornerPoints(sidelength)
for cornerPoint in cornerPoints:
    cubes[cornerPoint] = getOpenOuterPoints(walls, cornerPoints[cornerPoint], sidelength)

print(isSidePoint(walls, tiles, sidelength, (1,11)))

