#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = [[int(item) for item in line.rstrip()] for line in f.readlines()]

def scenicScoreLeft(i, j, grid):
    score = 0
    for l in range(j):
        if grid[i][j] > grid[i][j-l-1]:
            score += 1
        else:
            score += 1
            break
    return score

def scenicScoreRight(i, j, grid):
    score = 0
    n = len(grid[0])
    for l in range(n-j-1):
        if grid[i][j] > grid[i][j+l+1]:
            score += 1
        else:
            score += 1
            break
    return score

def scenicScoreUp(i, j, grid):
    score = 0
    for l in range(i):
        if grid[i][j] > grid[i-l-1][j]:
            score += 1
        else:
            score += 1
            break
    return score

def scenicScoreDown(i, j, grid):
    score = 0
    n = len(grid[0])
    for l in range(n-i-1):
        if grid[i][j] > grid[i+l+1][j]:
            score += 1
        else:
            score += 1
            break
    return score

def scenicScore(i, j, grid):
    d, l, r, u = scenicScoreDown(i, j, grid), scenicScoreLeft(i, j, grid), scenicScoreRight(i, j, grid), scenicScoreUp(i, j, grid)
    return d * l * r * u


def findTopScenicScore(grid):
    n, m, ans = len(grid), len(grid[0]), 0

    for i in range(n):
        for j in range(m):
            ans = max(ans, scenicScore(i, j, grid))
    return ans

print(findTopScenicScore(lines))
