import numpy as np

#file = '../data/test'
#file = '../data/large_test'
file = '../data/input'

with open(file) as f:
    lines = [line.rstrip().split() for line in f.readlines()]

    lines = [[line[0], int(line[1])] for line in lines]

def distOk(a,b):
    if abs(yDist(a,b)) <= 1 and abs(xDist(a,b)) <= 1:
        return True
    return False

def yDist(a,b):
    return a[0] - b[0]

def xDist(a,b):
    return a[1] - b[1]

def dist(a,b):
    return (yDist(a,b)**2 + xDist(a,b)**2)**0.5

def notRowCol(a, b):
    return a[0] != b[0] and a[1] != b[1]

visited = [set() for _ in range(10)]
for i in range(10):
    visited[i].add((0,0))
direction = {'R':(0,1), 'L':(0,-1), 'U':(1,0), 'D':(-1,0), 'dUR':(1,1), 'dUL':(1,-1), 'dDR':(-1,1), 'dDL':(-1,-1)}
positions = [np.array((0,0)) for _ in  range(10)]
ERROR = False

for line in lines:
    angling = line[0]
    move = np.array(direction[angling])
    for i in range(line[1]):
        if distOk(positions[1], positions[0] + move):
            positions[0] += move
        else:
            positions[0] += move
            for i in range(9):
                if not distOk(positions[i+1], positions[i]):
                    while notRowCol(positions[i+1], positions[i]) and not distOk(positions[i+1], positions[i]):
                        if yDist(positions[i+1], positions[i]) > 0 and xDist(positions[i+1], positions[i]) > 0:
                            positions[i+1] += np.array(direction['dDL'])
                        elif yDist(positions[i+1], positions[i]) < 0 and xDist(positions[i+1], positions[i]) > 0:
                            positions[i+1] += np.array(direction['dUL'])
                        elif yDist(positions[i+1], positions[i]) > 0 and xDist(positions[i+1], positions[i]) < 0:
                            positions[i+1] += np.array(direction['dDR'])
                        else:
                            positions[i+1] += np.array(direction['dUR'])
                    if yDist(positions[i+1], positions[i]) > 1:
                        positions[i+1][0] -= 1
                    elif yDist(positions[i+1], positions[i]) < -1:
                        positions[i+1][0] += 1
                    elif xDist(positions[i+1], positions[i]) > 1:
                        positions[i+1][1] -= 1
                    elif xDist(positions[i+1], positions[i]) < -1:
                        positions[i+1][1] += 1

                    if not distOk(positions[i+1], positions[i]):
                        ERROR = True          
        for i in range(10):
            visited[i].add(tuple(positions[i]))

print(len(visited[-1]))
print(ERROR)
#for i in range(10):
#    print(len(visited[i]))