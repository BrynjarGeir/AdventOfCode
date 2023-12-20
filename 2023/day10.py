from utils.util import getLines

inpt = './data/day10/input.txt'
test_1 = './data/day10/test1.txt'
test_2 = './data/day10/test2.txt'
test_3 = './data/day10/test3.txt'
test_4 = './data/day10/test4.txt'

def findStart(grid: list[str]) -> (int, int):
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == "S":
                return (i, j)

def findStartType(grid: list[str], start: (int, int)) -> str:
    nghbs = findPossibleNeighbours(grid, start)
    nghbs = ''.join(nghbs)

def findPossibleNeighbours(grid: list[str], position: (int, int)) -> list[(int, int)]:
    x, y = position
    n, m = len(grid), len(grid[0])
    res, symbol = [], grid[x][y]

    if x > 0 and symbol in '|LJS' and grid[x-1][y] in '|F7':
        res.append((x-1, y))
    if x + 1 < n and symbol in '|F7S' and grid[x+1][y] in '|LJ':
        res.append((x+1, y))
    if y > 0 and symbol in '-LJS' and grid[x][y-1] in '-FL':
        res.append((x, y-1))
    if y + 1 < m and symbol in '-FLS' and grid[x][y+1] in '-J7':
        res.append((x, y+1))

    assert(len(res) == 2)
 
    return res

def findConnectedNeighbours(grid: list[str], position: (int, int), paths: dict) -> dict:
    x, y = position
    res, symbol = [], grid[x][y]
    n, m = len(grid), len(grid[0])

    if x > 0 and symbol in '|LJS' and grid[x-1][y] in '|F7':
        res.append((x-1, y))
    if x + 1 < n and symbol in '|F7S' and grid[x+1][y] in '|LJ':
        res.append((x+1, y))
    if y > 0 and symbol in '-LJS' and grid[x][y-1] in '-FL':
        res.append((x, y-1))
    if y + 1 < m and symbol in '-FLS' and grid[x][y+1] in '-J7':
        res.append((x, y+1))
    
    assert(len(res) == 2)

    paths[position] = res
    
    return paths 

def populatePaths(grid:list[str], position: (int, int), paths: dict, visited: set((int, int))) -> None:
    paths = findConnectedNeighbours(grid, position, paths)
    l, r = paths[position]
    if l not in visited:
        visited.update([l])
        populatePaths(grid, l, paths, visited)
    if r not in visited:
        visited.update([r])
        populatePaths(grid, r, paths, visited)

def walkPath(paths, position, seen) -> None:

    if position not in seen:
        seen.add(position)
        l, r = paths[position]

        walkPath(paths, l, seen)
        walkPath(paths, r, seen)

    return


def part1(filePath: str = inpt) -> int:
    grid = getLines(filePath)
    start = findStart(grid)

    print(f"The starting position is given as {start}")

    startingType = findStartType(grid, start)
    
    position = start

    res = findPossibleNeighbours(grid, start)

    paths = dict()
    visited = set([start])

    populatePaths(grid, position, paths, visited)

    res = set()

    walkPath(paths, start, res)

    res = len(res)

    res = res // 2 if not res % 2 else res // 2 + 1 

    print(f"The answer to part 1 is {res}")

    return res

part1()