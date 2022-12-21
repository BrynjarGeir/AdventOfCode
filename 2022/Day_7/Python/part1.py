from collections import defaultdict
import pickle

#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = [line.rstrip() for line in f.readlines()]

parent_directories = {}
child_directories = defaultdict(list)
directory = ''
root = sep = '/'
max_value = 100000

n = len(lines)

for i in range(n):
    line = lines[i].split()

    if line[0] == '$' and line[1] == 'cd' and line[2] != '..':
        if directory == '':
            directory += line[-1]
            parent_directories[directory] = root
        elif directory == root:
            tmp = directory + line[-1]
            parent_directories[tmp] = directory
            directory = tmp
        else:
            tmp = directory + sep + line[-1]
            parent_directories[tmp] = directory
            directory = tmp

    elif line[0] == '$' and line[1] == 'cd':
        if directory == root:
            continue
        else:
            directory = parent_directories[directory]

    elif line[0] == '$' and line[1] == 'ls':
        i += 1
        line = lines[i].split()
        while line[0] != '$' and i < n :
            if line[0] == 'dir' and directory != root:
                child_directories[directory].append(directory + sep + line[1])
            elif line[0] == 'dir':
                child_directories[directory].append(directory + line[1])
            else:
                size = int(line[0])
                child_directories[directory].append(size)

            i += 1
            if i < n:
                line = lines[i].split()

print(child_directories)

change = True

while change:
    change = False
    for directory in child_directories:
        if all(isinstance(item, int) for item in child_directories[directory]):
            child_directories[directory] = [sum(child_directories[directory])]
        else:
            for i, item in enumerate(child_directories[directory]):
                if type(item) == int:
                    continue
                if all(isinstance(it, int) for it in child_directories[item]):
                    child_directories[directory][i] = sum(child_directories[item])
                    change = True


print(parent_directories)

ans = 0

for directory in child_directories:
    if child_directories[directory][0] <= max_value:
        ans += child_directories[directory][0]

print(ans)

# Just to help with part 2
with open('../data/file_system.pkl', 'wb') as f:
    pickle.dump(child_directories, f)

with open('../data/end_nodes.pkl', 'wb') as f:
    pickle.dump(parent_directories, f)