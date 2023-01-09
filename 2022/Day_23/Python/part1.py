from time import time
from collections import defaultdict

#file = '../data/small_test'
file = '../data/test'
#file = '../data/input'


# Read each line to array to be processed more later
with open(file) as f:
    lines = f.readlines()

# The original ordering of directions to consider
ordering = ['N', 'S', 'W', 'E']
# The dictionary for directions, three for each of  main directions
directions = {'N':[[-1,0], [-1,-1], [-1,1]], 'S':[[1, 0], [1,-1], [1,1]], 'W':[[0,-1], [1,-1], [-1,-1]], 'E':[[0,1],[1,1], [-1,1]]}
main_directions = {'N':(-1,0), 'S':(1,0), 'W':(0,-1), 'E':(0,1)}

# Take original input and return a set with all positions of elves, as grid is infinite
def populateGrid(lines):
    elves = set()
    for index, line in enumerate(lines):
        for i,c in enumerate(line):
            if c == '#':
                elves.add((index, i))
    return elves

# consider all neighbours and return a set of the occupied spots
def considerNeighbours(elves, elf):
    nghbs = set([(1,0), (1,1), (0,1), (-1,0), (0, -1), (-1,-1), (1,-1), (-1,1)])
    occupied = set()
    for nghb in nghbs:
        if (elf[0]+nghb[0], elf[1]+nghb[1]) in elves:
            occupied.add((elf[0]+nghb[0], elf[1]+nghb[1]))
    return occupied

# consider and propose a move with a specific ordering of direcftions
def considerMoving(occupied, elf, ordering):
    if not occupied:
        return None, False
    for order in ordering:
        opn = 0
        for direction in directions[order]:
            if (elf[0]+direction[0], elf[1]+direction[1]) not in occupied:
                opn += 1
        if opn == 3:
            return order, True
    return None, False

# Take the proposed moves (along with staying put) and generate the new elves
def resolveClashes(proposed):
    new_elves = set()
    for prop in proposed:
        if len(proposed[prop]) > 1:
            for elf in proposed[prop]:
                new_elves.add(elf)
        else:
            new_elves.add(prop)

    return new_elves

# Update ordering by just slicing front to end
def updateOrdering(ordering):
    return ordering[1:] + [ordering[0]]

# Simulate one round of movement by the elves
def simulateRound(elves, ordering):
    proposed = defaultdict(lambda: [])
    for elf in elves:
        occupied = considerNeighbours(elves, elf)
        moveDirection, moving = considerMoving(occupied, elf, ordering)
        prop = (elf[0]+main_directions[moveDirection][0], elf[1]+main_directions[moveDirection][1]) if moving else elf
        proposed[prop].append(elf)

    elves = resolveClashes(proposed)

    return elves

# Simulate rounds
def simulate_rounds(elves, rounds, ordering):
    for _ in range(rounds):
        elves = simulateRound(elves, ordering)
        ordering = updateOrdering(ordering)
    return elves

def simulate_until(elves, ordering):
    i = 1
    while True:
        tmp = simulateRound(elves, ordering)
        if elves == tmp:
            return i
        elves = tmp
        ordering = updateOrdering(ordering)
        i += 1

# Find range values for box  
def findRectangleArea(elves):
    x,y = [x[0] for x in elves], [y[1] for y in elves]
    xrange, yrange = abs(max(x)-min(x))+1, abs(max(y) - min(y))+1
    return abs(xrange * yrange)

# Find empty tiles for final answer
def findEmptyTiles(elves, area):
    num_elves = len(elves)
    return area - num_elves
    
start = time()
elves = populateGrid(lines)
rounds = 10
elves = simulate_rounds(elves, rounds, ordering)
area = findRectangleArea(elves)
answer = findEmptyTiles(elves, area)
end = time()

print(f"The number of empty tiles after {rounds} rounds are: {answer}!")
print(f"The time it took to compute that is {end - start} seconds")
