from collections import defaultdict

#file = '../data/test'
file = '../data/input'

with open(file) as f:
    inp = [1 if c == '>' else -1 for c in f.readline()]

height = 0
above = 4
rocks_to_drop = 2022
num_rocks = 5
occupied = defaultdict(lambda: False)
for point in ((0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0)):
    occupied[point] = True
n = len(inp)
index = 0


rock1 = [(2,0), (3,0), (4,0), (5,0)]
rock2 = [(3,0), (2, 1), (3,1), (4,1), (3,2)]
rock3 = [(2,0), (3,0), (4,0), (4,1), (4,2)]
rock4 = [(2,0), (2,1), (2,2), (2,3)]
rock5 = [(2,0), (2,1), (3,0), (3,1)]

rocks = [rock1, rock2, rock3, rock4, rock5]

def pushRock(rock, direction, occupied):
    tmp = rock.copy()
    for i in range(len(rock)):
        if occupied[(rock[i][0]+direction, rock[i][1])]:
            return rock, False
        elif rock[i][0]+direction == -1 or rock[i][0]+direction == 7:
            return rock, True
        else:
            tmp[i] = (rock[i][0]+direction, rock[i][1])
    return tmp, True

def fallRock(rock, occupied):
    tmp = rock.copy()
    for i in range(len(rock)):
        if occupied[(rock[i][0], rock[i][1]-1)]:
            return rock, False
        else:
            tmp[i] = (rock[i][0], rock[i][1]-1)
    return tmp, True

for drop in range(rocks_to_drop):
    rock = drop % num_rocks
    cr = rocks[rock]
    cnt = True

    cr = [(r[0],r[1]+height+above) for r in cr]

    while cnt:
        index %= n
        cr, cnt = pushRock(cr, inp[index], occupied)

        cr, cnt = fallRock(cr, occupied)

        index += 1

    height = max(height, max([it[1] for it in cr]))

    for point in cr:
        occupied[point] = True

print(height)
