from utils.util import getLines
from pprint import pprint as pp

inpt = './data/day14/input.txt'
test = './data/day14/test.txt'

def findMovementNorth(grid: list[list[str]], o: list[int]) -> int:
    x, y = o
    for r in range(x-1, -1, -1):
        if '.' != grid[r][y]:
            return r+1
    return 0

def findMovementWest(grid: list[list[str]], o: list[int]) -> int:
    x, y = o
    n = len(grid[0])
    for r in range(y-1, -1, -1):
        if '.' != grid[x][r]:
            return r+1
    return 0

def findMovementSouth(grid: list[list[str]], o: list[int]) -> int:
    x, y = o
    n = len(grid)
    for r in range(x+1, n):
        if '.' != grid[r][y]:
            return r-1
    return n-1

def findMovementEast(grid: list[list[str]], o: list[int]) -> int:
    x, y = o
    n = len(grid[0])
    for r in range(y+1, n):
        if '.' != grid[x][r]:
            return r-1
    return n-1

def tiltNorth(grid: list[list[str]], os: list[tuple[int, int]]) -> (list[list[str]], list[tuple[int, int]]):
    for i, o in enumerate(os):
        x, y = o
        r = findMovementNorth(grid, o)
        grid[x][y], grid[r][y] = '.', 'O'
        os[i] = (r, y)
    return grid, os

def tiltWest(grid: list[list[str]], os: list[tuple[int, int]]) -> (list[list[str]], list[tuple[int, int]]):
    for i, o in enumerate(os):
        x, y = o
        r = findMovementWest(grid, o)
        grid[x][y], grid[x][r] = '.', 'O'
        os[i] = (x, r)
    return grid, os

def tiltSouth(grid: list[list[str]], os: list[tuple[int, int]]) -> (list[list[str]], list[tuple[int, int]]):
    for i, o in enumerate(os):
        x, y = o
        r = findMovementSouth(grid, o)
        grid[x][y], grid[r][y] = '.', 'O'
        os[i] = (r, y)
    return grid, os

def tiltEast(grid: list[list[str]], os: list[tuple[int, int]]) -> (list[list[str]], list[tuple[int, int]]):
    for i, o in enumerate(os):
        x, y = o
        r = findMovementEast(grid, o)
        grid[x][y], grid[x][r] = '.', 'O'
        os[i] = (x, r)
    return grid, os

def findOs(grid: list[list[str]]) -> list[tuple[int, int]]:
    res, n, m = [], len(grid), len(grid[0])

    for i in range(n):
        for j in range(m):
            if 'O' == grid[i][j]:
                res.append((i, j))

    return res

def scoreGrid(grid: list[list[str]]) -> int:
    res, n, m = 0, len(grid), len(grid[0])

    for i in range(n):
        for j in range(m):
            if 'O' == grid[i][j]:
                res += n - i
    return res

def doCycle(grid: list[list[str]], os: list[tuple[int, int]]) -> (list[list[str]], list[tuple[int, int]]):
    grid, os = tiltNorth(grid, os)
    os.sort(key = lambda x: x[1])
    grid, os = tiltWest(grid, os)
    os.sort(key = lambda x: x[0], reverse = True)
    grid, os = tiltSouth(grid, os)
    os.sort(key = lambda x: x[1], reverse=True)
    grid, os = tiltEast(grid, os)
    os.sort()


    return grid, os

def findCycle(grid: list[list[str]], os: list[tuple[int, int]], n_cycles: int = 1000000000) -> (list[list[str]], list[tuple[int, int]], int, int):
    visited = {}

    for i in range(n_cycles):
        grid, os = doCycle(grid, os)
        t_os = tuple(os)

        if t_os in visited:
            return grid, os, visited[t_os], i
        else:
            visited[t_os] = i

    return (grid, os, -1, -1)

def cycle(mat):
    mat = tiltV(mat, -1)
    print("after north tilt")
    pp(mat)
    mat = tiltH(mat, -1)
    print("after west tilt")
    pp(mat)
    mat = tiltV(mat, 1)
    print("after south tilt")
    pp(mat)
    mat = tiltH(mat, 1)
    print("after south tilt")
    pp(mat)
    return mat

def tiltV(mat, dx):
    if dx>0:
        mat.reverse()
    for i, l in enumerate(mat):
        for j, c in enumerate(l):
            if c == 'O':
                k = i-1 
                while k>=0:
                    w = mat[k][j]
                    if w == '#' or w =='O':
                        k = k +1
                        break
                    k = k-1
                k = max(k,0)
                mat[i][j]='.'
                mat[k][j]='O'
    
    if dx>0:
        mat.reverse()
    return mat

def tiltH(mat, dy):
    for i, l in enumerate(mat):
        if dy>0:
            l.reverse()
        for j, c in enumerate(l):
            if c == 'O':
                k = j-1 
                while k>=0:
                    w = mat[i][k]
                    if w == '#' or w =='O':
                        k = k +1
                        break
                    k = k-1
                k = max(k,0)
                mat[i][j]='.'
                mat[i][k]='O'
        if dy>0:
            l.reverse()
    return mat

def part1(filePath: str = inpt) -> int:
    lines = getLines(filePath)
    grid = [[a for a in line] for line in lines]
    os = findOs(grid)

    grid, os = tiltNorth(grid, os)

    res = scoreGrid(grid)

    print(f"The answer to part 1 is {res}")


    return res

def part2(filePath: str = inpt) -> int:
    lines = getLines(filePath)
    grid = [[a for a in line] for line in lines]
    os = findOs(grid)
    n_cycles = 1000000000

    grid, os, start_cycle, end_cycle = findCycle(grid, os)

    cycle_length = end_cycle - start_cycle

    spin_cycles_left = (n_cycles-start_cycle) % cycle_length

    for _ in range(spin_cycles_left-1):
        doCycle(grid, os)
    
    res = scoreGrid(grid)

    print(f"The answer to part 2 is {res}")

    return res

part1()

part2()