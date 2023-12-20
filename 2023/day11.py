from utils.util import getLines
from pprint import pprint as pp
from itertools import combinations

inpt = "./data/day11/input.txt"
test = "./data/day11/test.txt"

def findEmpty(universe: list[str]) -> (list[int], list[int]):
    rows = []
    for index, row in enumerate(universe):
        if all(char == '.' for char in row):
            rows.append(index)
    
    n, cols = len(universe[0]), []

    for j in range(n):
        if all(s[j] == '.' for s in universe):
            cols.append(j)

    return rows, cols

def expandUniverse(universe: list[str]) -> list[str]:

    universe = [[pos for pos in row] for row in universe]

    rows, cols = findEmpty(universe)
    n = len(universe[0])
    addStrRow = ['.' for _ in range(n)]

    for row in rows[::-1]:
        universe = universe[:row] + [addStrRow] + universe[row:]

    m = len(universe)
    for col in cols[::-1]:
        for i in range(m):
            universe[i] = universe[i][:col] + ['.'] + universe[i][col:]

    for i in range(m):
        universe[i] = ''.join(universe[i])  

    return universe

def getGalaxies(universe: list[str]) -> list[(int, int)]:
    positions = []

    for i, row in enumerate(universe):
        for j, col in enumerate(row):
            if col == '#':
                positions.append((i, j))

    return positions

def getPairs(n: int) -> list[(int, int)]:
    return list(combinations(range(n), 2))

def getManhattan(a: (int, int), b: (int, int)) -> int:
    x1, y1 = a
    x2, y2 = b
    return abs(x1-x2) + abs(y1-y2)

def getXYDist(a: (int, int), b: (int, int)) -> int:
    x1, y1 = a
    x2, y2 = b
    return abs(x1-x2), abs(y1-y2)

def getRowColRange(a: (int, int), b: (int, int)) -> int:
    x1, y1 = a
    x2, y2 = b

    startRow, endRow, startCol, endCol = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)

    return startRow, endRow, startCol, endCol

def getNumberOfExpandedRowColsInRange(startRow: int, endRow: int, startCol: int, endCol: int, rows: list[int], cols: list[int]):
    xi, yi = 0, 0

    for row in rows:
        if row > startRow and row < endRow:
            xi += 1
    for col in cols:
        if col > startCol and col < endCol:
            yi += 1

    return xi, yi


def part1(filePath: str = inpt) -> int:
    universe = getLines(filePath)

    universe = expandUniverse(universe)

    galaxies = getGalaxies(universe)

    n = len(galaxies)
    
    pairs = getPairs(n)

    res = 0

    for pair in pairs:
        dist = getManhattan(galaxies[pair[0]], galaxies[pair[1]])
        res += dist

    print(f"The answer to part 1 is {res}")

    return res

def part2(filePath: str = inpt) -> int:
    universe = getLines(filePath)
    rows, cols = findEmpty(universe)

    galaxies = getGalaxies(universe)

    n, expansion = len(galaxies), 1e6

    pairs = getPairs(n)

    res = 0

    for pair in pairs:
        a, b = galaxies[pair[0]], galaxies[pair[1]]
        rowDiff, colDiff = getXYDist(a, b)
        startRow, endRow, startCol, endCol = getRowColRange(a, b)
        xi, yi = getNumberOfExpandedRowColsInRange(startRow, endRow, startCol, endCol, rows, cols)

        res += int(rowDiff + colDiff - (xi + yi) + (xi+yi) * expansion)

    print(f"The answer to part 2 is {res}")
    
    return res



    


part1()

part2()