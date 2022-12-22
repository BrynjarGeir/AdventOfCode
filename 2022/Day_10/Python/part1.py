#from collections import deque

#file = '../data/test'
#file = '../data/larger_test'
file = '../data/input'


with open(file) as f:
    lines = [line.rstrip().split() for line in f.readlines()]

for i in range(len(lines)):
    if len(lines[i]) == 2:
        lines[i][1] = int(lines[i][1])

x, cycle = 1, 1
ans = []

for line in lines:
    cycle += 1
    shown = False

    if not (cycle + 20) % 40:
        print('Cycle: ', cycle, ' with x: ', x)
        ans.append(cycle * x)
        shown = True

    if line[0] == 'addx':
        x += line[1]
        cycle += 1

    if not (cycle + 20) % 40 and not shown:
        print('Cycle: ', cycle, ' with x: ', x)
        ans.append(cycle * x)


print('Sum of signal strengths is: ', sum(ans))
        


