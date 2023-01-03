# Using hugseverycat for cycle part 2

from collections import defaultdict
from time import time

#file = '../data/test'
file = '../data/input'

with open(file) as f:
    inp = [1 if c == '>' else -1 for c in f.readline()]

height = 0
above = 4
rocks_to_drop = 1000000000000
num_rocks = 5
states = {}
occupied = defaultdict(lambda: False)
columns = {
    0: set(),
    1: set(),
    2: set(),
    3: set(),
    4: set(),
    5: set(),
    6: set()
}
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

def update_pos(columns, rock):
    for coord in rock:
        rx, ry = coord
        columns[rx].add(ry)
    return columns

def get_height(columns):
    h = 0
    for col in columns:
        if len(columns[col]):
            m = max(columns[col])
            h = max(m, h)
    return h+1

def find_cycle(occupied, columns, index, rock, rocks_to_drop, drop):
    max_cols = []
    for c in columns:
        if columns[c]:
            max_cols.append(max(columns[c]))
        else:
            max_cols.append(-1)
    min_col = min(max_cols)
    relative_cols = [mc - min_col for mc in max_cols]
    state = relative_cols.extend([rock, index])
    state = tuple(relative_cols)

    if state in states:
        height_gain_in_cycle = max(max_cols) - states[state]['height']
        rocks_in_cycle = drop - states[state]['rock']
        remaining_rocks = rocks_to_drop - drop
        cycles_remaining = remaining_rocks // rocks_in_cycle
        rock_remainder = remaining_rocks % rocks_in_cycle
        height_increase = height_gain_in_cycle * cycles_remaining
        return True, height_increase
    else:
        states[state] = {'rock': drop, 'height': height}
        return False, None


def runSimulation(rocks_to_drop, num_rocks, height, above, index, occupied, columns):
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

        columns = update_pos(columns, cr)
        height = get_height(columns)


        for point in cr:
            occupied[point] = True
            columns[point[0]].add(point[1])
        
        cycle_found, height_increase = find_cycle(occupied, columns, index, rock, rocks_to_drop, drop)

        if cycle_found:
            return height, height_increase  

    return height, None

start = time()
height, height_increase = runSimulation(rocks_to_drop, num_rocks, height, above, index, occupied, columns)
end = time()

print('The height we stopped at is ', height)
print('We had an increase after that of ', height_increase)
print('The final answer is thus ', height + height_increase)
print('It took ', end - start, ' to arrive at that')
