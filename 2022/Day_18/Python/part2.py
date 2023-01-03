#file = '../data/small_test'
file = '../data/test'
#file = '../data/input'

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

def isNotInPocket(cubes, air, visited, cubes_in_pockets, min_x, max_x, min_y, max_y, min_z, max_z):
    if air in cubes or air in visited: 
        cubes_in_pockets[0] += 1
        return False
    elif air[0] < min_x or air[0] > max_x or air[1] < min_y or air[1] > max_y or air[2] < min_z or air[2] > max_z: return True, visited
    else:
        neighbours = [[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0]]
        visited.add(air)
        for nghb in neighbours:
            passes = isNotInPocket((air[0]+nghb[0], air[1]+nghb[1], air[2]+nghb[2]))
            if passes:
                return passes
        return passes
        
def findAllUncoveredSides(cubes):
    uncovered_sides = 0
    for cube in cubes:
        uncovered_sides += 6 - findNumNeighbours(cubes, cube)

    return uncovered_sides

def findAllAirPockets(cubes):
    min_x, max_x, min_y, max_y, min_z, max_z = min([x[0] for x in cubes]), max([x[0] for x in cubes]), min([y[1] for y in cubes]), max([y[1] for y in cubes]), min([z[2] for z in cubes]), max([z[2] for z in cubes])
    pockets = []
    for i in range(min_x-1, max_x+1):
        for j in range(min_y-1, max_y+1):
            for l in range(min_z-1, max_z+1):
                cubes_in_pockets = [0]
                is_not_in = isNotInPocket(cubes, (i,j,l), visited, cubes_in_pockets, min_x, max_x, min_y, max_y, min_z, max_z)
                if not is_not_in:
                    

    return pockets

p1 = findAllUncoveredSides(cubes)
passes, visited = findAllAirPockets(cubes)

print()
