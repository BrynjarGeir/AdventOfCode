from utils.util import getLines

inpt = './data/day13/input.txt'
test = './data/day13/test.txt'

def getPatterns(lines: list[str]) -> list[list[str]]:
    patterns, c = [], []
    for line in lines:
        if line == '':
            patterns.append(c)
            c.clear()
        else:
            c.append(line)

    if c != '':
        patterns.append(c)
    return patterns

def transpose(pattern: list[str]) -> list[str]:
    return [''.join(s) for s in zip(*pattern)]

def matches(pattern: list[str], i: int, j: int, n: int) -> bool:
    if i == -1 or j == n:
        return True
    return pattern[i] == pattern[j] and matches(pattern, i-1, j+1, n)    

def findHorizontalPattern(pattern: list[str]) -> int:
    n = len(pattern)

    for i in range(n-1):
        if matches(pattern, i, i+1, n):
                return i
    return -1

def findVerticalPattern(pattern: list[str]) -> int:
    pattern = transpose(pattern)
    return findHorizontalPattern(pattern)

def part1(filePath: str = inpt) -> int:
    lines = getLines(filePath)

    patterns = getPatterns(lines)

    res = 0

    for pattern in patterns:
        hor, vert = findHorizontalPattern(pattern), findVerticalPattern(pattern)

        if hor == -1:
            res += vert
        else:
            res += 100 * hor

    print(f"The answer to part 1 is {res}")

    return res


part1(test)