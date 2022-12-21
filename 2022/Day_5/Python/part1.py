#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = [line.rstrip() for line in f.readlines()]

for index, line in enumerate(lines):
    if line[1] == '1':
        num_stacks = int(line[-1])
        orders_index = index + 2
        stacks_index = index
        break

stacks = [[] for _ in range(num_stacks)]        
for index in range(stacks_index):
    for i in range(len(lines[index])):
        if lines[index][i].isalpha():
            stacks[int(lines[stacks_index][i])-1].append(lines[index][i])

orders = [[] for _ in range(len(lines[orders_index:]))]

for index in range(orders_index, len(lines)):

    current = lines[index].split()
    move, fr, to = int(current[1]), int(current[3]), int(current[5])
    
    tmp = stacks[fr-1][:move]
    stacks[fr-1] = stacks[fr-1][move:]
    stacks[to-1] = tmp[::-1] + stacks[to-1]

ans = [s[0] for s in stacks]

print(''.join(ans))