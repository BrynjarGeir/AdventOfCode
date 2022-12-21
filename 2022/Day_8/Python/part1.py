#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = [[int(item) for item in line.rstrip()] for line in f.readlines()]

def isVisibleLeft(i, j, grid):
    if grid[i][j] > max(grid[i][:j]):
        return True
    return False

def isVisibleRight(i, j, grid):
    if grid[i][j] > max(grid[i][j+1:]):
        return True
    return False

def isVisibleUp(i, j, grid):
    up = [grid[l][j] for l in range(i)]
    if grid[i][j] > max(up):
        return True
    return False

def isVisibleDown(i, j, grid):
    n = len(grid)
    down = [grid[l][j] for l in range(i+1,n)]
    if grid[i][j] > max(down):
        return True
    return False

def isVisible(i, j, grid):
    return isVisibleDown(i, j, grid) or isVisibleLeft(i, j, grid) or isVisibleRight(i, j, grid) or isVisibleUp(i, j, grid)

def isEdge(i, j, grid):
    n, m = len(grid), len(grid[0])
    return i == n - 1 or j == m - 1 or i == 0 or j == 0

def findVisibleTrees(grid):
    n, m, ans = len(grid), len(grid[0]), 0

    for i in range(n):
        for j in range(m):
            if isEdge(i, j, grid) or isVisible(i, j, grid):
                ans += 1

    return ans

print(findVisibleTrees(lines))
