from itertools import combinations
from pprint import pp
import numpy as np

input_path = './data/day10/input.txt'
test_path = './data/day10/test.txt'

with open(test_path, 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [list(line) for line in lines]
    grid = [[int(c) for c in line] for line in lines]

def creatGraph(grid):
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

def dfs(graph, grid, pos, paths):
    if pos not in graph:
        if grid[pos[0]][pos[1]] == 9:
            paths[0] += 1
    else:
        for p in graph[pos]:
            dfs(graph, grid, p, paths)

def part1(grid):
    graph, starts = creatGraph(grid)
    paths = [0]
    dfs(graph, grid, (0,2), paths)

    return paths[0]

print(f"Part 1: {part1(grid)}")           