from collections import deque

#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = [[c for c in line.rstrip()] for line in f.readlines()]

    for index, line in enumerate(lines):
        for i, c in enumerate(line):
            if not c.isupper():
                lines[index][i] = ord(c) - ord('a')
            elif c == 'S':
                start = (index, i)
                lines[index][i] = 0
            else:
                end = (index, i)
                lines[index][i] = ord('z') - ord('a')

#for line in lines:
#    print(line)

def neighbors(node, grid):
    n = []
    if node[0] > 0 and grid[node[0]][node[1]]-grid[node[0]-1][node[1]] >= -1:
        n.append((node[0]-1, node[1]))
    if node[0] + 1 < len(grid) and grid[node[0]][node[1]]-grid[node[0]+1][node[1]] >= -1:
        n.append((node[0]+1, node[1]))
    if node[1] > 0 and grid[node[0]][node[1]]-grid[node[0]][node[1]-1] >= -1:
        n.append((node[0], node[1]-1))
    if node[1] + 1 < len(grid[0]) and grid[node[0]][node[1]]-grid[node[0]][node[1]+1] >= -1:
        n.append((node[0], node[1]+1))

    return n

def backtrace(parent, start, goal):
    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path


def bfs(start, goal, grid):
    parent = {}
    q = deque()

    q.append(start)
    parent[start] = None

    while q:
        node = q.popleft()

        if node == end:
            return backtrace(parent, start, goal)

        for neighbor in neighbors(node, grid):
            if neighbor not in parent:
                parent[neighbor] = node
                q.append(neighbor)


ans = bfs(start, end, lines)

print(len(ans)-1)