import numpy as np

#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = [line.rstrip().split() for line in f.readlines()]

    lines = [[line[0], int(line[1])] for line in lines]

def distOk(a,b):
    if abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1:
        return True
    return False

def yDist(a,b):
    return a[0] - b[0]

def xDist(a,b):
    return a[1] - b[1]

def notRowCol(a, b):
    return a[0] != b[0] and a[1] != b[1]

visited, heads = set(), []
visited.add((0,0))
heads.append((0,0))
direction = {'R':(0,1), 'L':(0,-1), 'U':(1,0), 'D':(-1,0)}
posTail = np.array((0,0))
posHead = np.array((0,0))

for line in lines:
    angling = line[0]
    move = np.array(direction[angling])
    for i in range(line[1]):
        if distOk(posTail, posHead + move):
            posHead += move
        else:
            posHead += move
            posTail += move
            if notRowCol(posHead, posTail):
                if angling == 'L' or angling == 'R':
                    if yDist(posTail, posHead) == 1:
                        posTail += np.array(direction['D'])
                    else:
                        posTail += np.array(direction['U'])
                elif angling == 'D' or angling == 'U':
                    if xDist(posTail, posHead) == 1:
                        posTail +=  np.array(direction['L'])
                    else:
                        posTail += np.array(direction['R'])
        visited.add(tuple(posTail))
        heads.append(tuple(posHead))

print(len(visited))
#print(visited)