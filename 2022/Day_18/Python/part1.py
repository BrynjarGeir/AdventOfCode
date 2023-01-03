#file = '../data/small_test'
#file = '../data/test'
file = '../data/input'

with open(file) as f:
    cubes = [tuple([int(it) for it in item.rstrip().split(',')]) for item in f.readlines()]
    cubes = set(cubes)

def allNeighboursCubes(cubes, cube):
    return findNumNeighbours(cubes, cube) == 6

def findNumNeighbours(cubes, cube):
    num = 0
    neighbours = [[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0]]

    for neighbour in neighbours:
        if (cube[0]+neighbour[0], cube[1]+neighbour[1], cube[2]+neighbour[2]) in cubes:
            num += 1
    
    return num

def findAllUncoveredSides(cubes):
    uncovered_sides = 0
    for cube in cubes:
        uncovered_sides += 6 - findNumNeighbours(cubes, cube)

    return uncovered_sides

def findAllAirPockets(cubes):
    min_x, max_x, min_y, max_y, min_z, max_z = min([x[0] for x in cubes]), max([x[0] for x in cubes]), min([y[1] for y in cubes]), max([y[1] for y in cubes]), min([z[2] for z in cubes]), max([z[2] for z in cubes])
    pockets = 0
    for i in range(min_x, max_x+1):
        for j in range(min_y, max_y+1):
            for l in range(min_z, max_z+1):
                if (i, j, l) not in cubes and allNeighboursCubes(cubes, (i,j,l)):
                    pockets += 1

    return pockets

p1 = findAllUncoveredSides(cubes)

print(p1)
