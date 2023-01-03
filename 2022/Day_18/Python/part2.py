from time import time

#file = '../data/small_test'
#file = '../data/test'
file = '../data/input'

with open(file) as f:
    cubes = [tuple([int(it) for it in item.rstrip().split(',')]) for item in f.readlines()]
    cubes = set(cubes)

min_x, max_x = min([x[0] for x in cubes]), max([x[0] for x in cubes])
min_y, max_y = min([y[1] for y in cubes]), max([y[1] for y in cubes])
min_z, max_z = min([z[2] for z in cubes]), max([z[2] for z in cubes])
nghbs = [(0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0)]
seen, visited = set(), set()
visited.add((0,0,0))

def allNeighboursCubes(cubes, cube):
    return findNumNeighbours(cubes, cube) == 6

def findNumNeighbours(cubes, cube):
    num = 0
    neighbours = [[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0, 0]]

    for neighbour in neighbours:
        if (cube[0]+neighbour[0], cube[1]+neighbour[1], cube[2]+neighbour[2]) in cubes:
            num += 1
    
    return num

def reachEverySide():
    global visited, seen, nghbs
    for point in visited:
        x,y,z = point
        for nghb in nghbs:
            if (x+nghb[0], y+nghb[1], z+nghb[2]) in cubes:
                seen.add((point, (x+nghb[0], y+nghb[1], z+nghb[2])))
    return len(seen)


def findAllReachablePoints():
    global visited, nghbs
    while True:
        tmp = visited.copy()
        for point in visited:
            x,y,z = point
            for nghb in nghbs:
                if x+nghb[0] < min_x - 1 or x+nghb[0] > max_x+1 or y+nghb[1] < min_y - 1 or y+nghb[1] > max_y + 1 or z+nghb[2] < min_z - 1 or z+nghb[2] > max_z + 1:
                    continue
                elif (x+nghb[0], y+nghb[1], z+nghb[2]) in cubes:
                    continue
                else:
                    tmp.add((x+nghb[0], y+nghb[1], z+nghb[2]))
        if len(tmp) == len(visited):
            break
        visited = tmp



        
def findAllUncoveredSides(cubes):
    uncovered_sides = 0
    for cube in cubes:
        uncovered_sides += 6 - findNumNeighbours(cubes, cube)

    return uncovered_sides



#p1 = findAllUncoveredSides(cubes)
start = time()
findAllReachablePoints()
reachEverySide()
p2 = len(seen)
end = time()
print('Answer is: ',p2)
print('Took ' , end - start, 'seconds to arrive at that!')
