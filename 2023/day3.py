from utils.util import getLines

inpt = "./data/day3/input.txt"
test = "./data/day3/test.txt"

def findSymbols(grid: list[list[str]]) -> set[tuple[int]]:
    symbols = set()
    digits = '0123456789'

    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch not in digits and ch != '.':
                symbols.add((i,j))

    return symbols  

def findNumbers(grid: list[list[str]]) -> list[tuple[int]]:
    numbers = set()
    digits = '0123456789'
    r, c, l = -1, -1, 0
    for i, row in enumerate(grid):
        for j, ch in enumerate(row):
            if ch in digits and r == -1:
                r, c = i, j
                l += 1
            elif ch in digits:
                l += 1
            elif l != 0:
                numbers.add((r, c, l))
                l = 0
                r, c = -1, -1
        if l != 0:
            numbers.add((r, c, l))
            r, c, l = -1, -1, 0
    return numbers

def adjacent(number: tuple[int], symbol: tuple[int]) -> bool:
    r, c, l = number
    x, y = symbol

    for i in range(-1, l+1):
        if c + i == y and r - 1 == x:
            return True
        if c + i == y and r + 1 == x:
            return True
        if c + i == y and r == x:
            return True
    return False

def numbersTouchingSymbol(symbol: tuple[int], numbers: tuple[int]) -> list[tuple[int]]:
    res = []
    for number in numbers:
        if adjacent(number, symbol):
            res.append(number)
    return res

def numberTouchesSymbol(number: tuple[int], symbols: set(tuple[int])) -> bool:
    for symbol in symbols:
        if adjacent(number, symbol):
            return True
    return False
  
def getNumberValues(adjacentNumbers: list[tuple[int]], lines: list[list[str]]) -> (int, int):
    num1, num2 = adjacentNumbers
    r1, c1, l1 = num1
    r2, c2, l2 = num2
    a1 = int(lines[r1][c1:c1+l1])
    a2 = int(lines[r2][c2:c2+l2])
    return a1, a2


def part1(filePath: str = inpt) -> int:
    lines = getLines(filePath)

    symbols = findSymbols(lines)
    numbers = findNumbers(lines)

    res = 0

    for number in numbers:
        b  = numberTouchesSymbol(number, symbols)
        r, c, l = number
        if b:
            c = int(lines[r][c:c+l])
            res += c
    
    print(f" The answer to part 1 is {res}")

    return res

def part2(filePath: str = inpt) -> int:

    lines = getLines(filePath)

    symbols = findSymbols(lines)
    numbers = findNumbers(lines)

    res = 0

    for symbol in symbols:
        adjacentNumbers = numbersTouchingSymbol(symbol, numbers)
        if len(adjacentNumbers) != 2:
            continue
            
        a1, a2 = getNumberValues(adjacentNumbers, lines)

        res += a1*a2

    print(f"The answer to part 2 is {res}")

    return res

part1()
part2()