# Using hugseverycat for cycle part 2 (using his github)

from time import time

#file = '../data/test'
file = '../data/input'

with open(file) as f:
    jet_pattern = [1 if c == '>' else -1 for c in f.readline()]

height = 0
above = 3
rocks_to_drop = 1000000000000
num_rocks = 5
states = {}
columns = {
    0: set(),
    1: set(),
    2: set(),
    3: set(),
    4: set(),
    5: set(),
    6: set()
}
num_jets = len(jet_pattern)
jet = 0


rock1 = [(2,0), (3,0), (4,0), (5,0)]
rock2 = [(3,0), (2, 1), (3,1), (4,1), (3,2)]
rock3 = [(2,0), (3,0), (4,0), (4,1), (4,2)]
rock4 = [(2,0), (2,1), (2,2), (2,3)]
rock5 = [(2,0), (2,1), (3,0), (3,1)]

rocks = [rock1, rock2, rock3, rock4, rock5]

def pushRock(rock, direction, columns):
    tmp = [(tx+direction, ty) for tx,ty in rock]
    for tx, ty in tmp:
        if tx == -1 or tx== 7 or ty in columns[tx]:
            return rock, False
    return tmp, True

def fallRock(rock, columns):
    tmp = [(tx, ty-1) for tx,ty in rock]
    for tx,ty in tmp:
        if ty in columns[tx] or ty < 0:
            return rock, False
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
    return h + 1

def newRock(rock, rocks, height, above):
    nRock = [(tx,ty+height+above) for tx,ty in rocks[rock]]
    return nRock

def find_cycle(columns, jet, rock, rocks_to_drop, height, drop, states):
    max_cols = []
    for c in columns:
        if len(columns[c]):
            max_cols.append(max(columns[c]))
        else:
            max_cols.append(-1)
    min_col = min(max_cols)
    relative_cols = [mc - min_col for mc in max_cols]
    state = relative_cols.extend([rock, jet])
    state = tuple(relative_cols)

    if state in states:
        rocks_in_cycle = drop - states[state]['rock']
        height_gain_in_cycle = height - states[state]['height']
        remaining_rocks = rocks_to_drop - drop
        cycles_remaining = remaining_rocks // rocks_in_cycle
        rock_remainder = remaining_rocks % rocks_in_cycle
        height_increase = height_gain_in_cycle * cycles_remaining
        return True, height_increase, rocks_to_drop - rock_remainder, states
    else:
        states[state] = {'rock': drop, 'height': height}
        return False, None, None, states


def runSimulation(rocks_to_drop, num_rocks, height, above, jet, columns, cycle_found = False, drop = 0, states = {}):
    while drop < rocks_to_drop:

        rock = drop % num_rocks
        cr = newRock(rock, rocks, height, above)
        cnt = True
        tmp_drop = None

        while cnt:
            cr, cnt = pushRock(cr, jet_pattern[jet], columns)

            cr, cnt = fallRock(cr, columns)

            jet = (jet + 1) % num_jets

        columns = update_pos(columns, cr)
        height = get_height(columns)
        
        if not cycle_found:
            cycle_found, height_increase, tmp_drop, states = find_cycle(columns, jet, rock, rocks_to_drop, height, drop, states)
        
        if tmp_drop:
            drop = tmp_drop
        drop += 1


    if cycle_found:
        return height, height_increase
    return height, None

start = time()
height, height_increase = runSimulation(rocks_to_drop, num_rocks, height, above, jet, columns)
end = time()

print('The height we stopped at is ', height)
print('We had an increase after that of ', height_increase)
print('The final answer is thus ', height + height_increase)
print('It took ', end - start, ' to arrive at that')