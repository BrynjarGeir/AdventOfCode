from utils.util import getLines
from pprint import pprint as pp
import sys

sys.setrecursionlimit(10000)

inpt = './data/day16/input.txt'
test = './data/day16/test.txt'


def illegalState(state: tuple[int], n: int, m: int) -> bool:
    r, c, _, _ = state
    return not (r >= 0 and c >= 0 and r < n and c < m)

def nextState(state: tuple[int, int, int, int], grid: list[list[str]], visited: set) -> None:
    n, m = len(grid), len(grid[0])
    if state in visited or illegalState(state, n, m):
        return
    
    visited.add(state)
    
    r, c, dr, dc = state
    val = grid[r][c]


    if '|' == val and ((-1, 0) == (dr, dc) or (1, 0) == (dr, dc)):
        nextState((r + dr, c, dr, dc), grid, visited)
    elif '|' == val and ((0, 1) == (dr, dc) or (0, -1) == (dr, dc)):
        nextState((r - 1, c, -1, 0), grid, visited)
        nextState((r + 1, c, 1, 0), grid, visited)
    elif '-' == val and ((0, 1) == (dr, dc) or (0, -1) == (dr, dc)):
        nextState((r, c + dc, dr, dc), grid, visited)
    elif '-' == val and ((-1, 0) == (dr, dc) or (1, 0) == (dr, dc)):
        nextState((r, c + 1, 0, 1), grid, visited)
        nextState((r, c - 1, 0, -1), grid, visited)
    elif '\\' == val:
        nextState((r+dc, c+dr, dc, dr), grid, visited)
    elif '/' == val:
        nextState((r-dc, c-dr, -dc, -dr), grid, visited)
    else:
        nextState((r+dr, c+dc, dr, dc), grid, visited)

    

def part1(filePath: str = inpt) -> int:
    grid = getLines(filePath)
    grid = [list(row) for row in grid]
    visited = set()

    pos = (0, 0, 0, 1)
    nextState(pos, grid, visited)

    loc = set([(p[0], p[1]) for p in visited])

    res = len(loc)

    print(f"The answer to part 1 is {res}")

    return res

def part2(filePath: str = inpt) -> int:
    grid = getLines(filePath)
    grid = [list(row) for row in grid]
    visited = set()
    n, m = len(grid), len(grid[0])
    res = -1

    sides = [[(i, 0) for i in range(n)], [(0, j) for j in range(m)], [(i, m-1) for i in range(n)], [(n-1, j) for j in range(m)]]

    for i, startDir in enumerate([(0, 1), (1, 0), (-1, 0), (0, -1)]):
        for startPoint in sides[i]:
            r, c = startPoint
            dr, dc = startDir
            nextState((r, c, dr, dc), grid, visited)
            loc = set([(p[0], p[1]) for p in visited])
            c_res = len(loc)
            res = max(c_res, res)
            visited.clear()

    print(f"Answer to part 2 is {res}")

    return res

part1()
part2()