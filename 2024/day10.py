from pprint import pp
import numpy as np

input_path = './data/day10/input.txt'
test_path = './data/day10/test.txt'

with open(input_path, 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [list(line) for line in lines]
    grid = [[int(c) for c in line] for line in lines]

def createGraph(grid):
    graph, starts, r, c = {}, [], len(grid), len(grid[0])
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            if v == 0:
                starts.append((i, j))
            if j+1 < c and grid[i][j+1] == v + 1:
                if (i, j) in graph:
                    graph[(i,j)].append((i, j+1))
                else:
                    graph[(i,j)] = [(i, j+1)]
            if j-1 >= 0 and grid[i][j-1] == v + 1:
                if (i, j) in graph:
                    graph[(i,j)].append((i, j-1))
                else:
                    graph[(i,j)] = [(i, j-1)]
            if i+1 < r and grid[i+1][j] == v + 1:
                if (i, j) in graph:
                    graph[(i,j)].append((i+1, j))
                else:
                    graph[(i,j)] = [(i+1, j)]
            if i-1 >= 0 and grid[i-1][j] == v + 1:
                if (i, j) in graph:
                    graph[(i,j)].append((i-1, j))
                else:
                    graph[(i,j)] = [(i-1, j)]
    return graph, starts

def dfs(graph, grid, pos, paths, path):
    if pos not in graph:
        if grid[pos[0]][pos[1]] == 9:
            paths.append(path + [pos])
    else:
        for p in graph[pos]:
            dfs(graph, grid, p, paths, path + [pos])

def part1(grid):
    graph, starts = createGraph(grid)
    paths = []
    for start in starts:
        dfs(graph, grid, start, paths, [])

    startEnds = {}
    for path in paths:
        start, end = path[0], path[-1]
        if start in startEnds:
            startEnds[start].add(end)
        else:
            startEnds[start] = set([end])
    res = 0
    for start in startEnds:
        res += len(startEnds[start])
    return res

def part2(grid):
    graph, starts = createGraph(grid)
    paths = []
    for start in starts:
        dfs(graph, grid, start, paths, [])
    return len(paths)


print(f"Part 1: {part1(grid)}")
print(f"Part 2: {part2(grid)}")
