from utils.util import getLines
from pprint import pprint as pp

inpt = './data/day13/input.txt'
test = './data/day13/test.txt'
reddit_test = './data/day13/reddit_test.txt'

def getPatterns(lines: list[str]) -> list[list[str]]:
    patterns, c = [], []
    for line in lines:
        if line == '':
            patterns.append(c)
            c = []
        else:
            c.append(line)

    patterns.append(c)

    return patterns

def transpose(pattern: list[str]) -> list[str]:
    res = [''.join(s) for s in zip(*pattern)]
    return res

def matches(pattern: list[str], i: int, j: int, n: int) -> bool:
    if i == -1 or j == n:
        return True
    return pattern[i] == pattern[j] and matches(pattern, i-1, j+1, n)

def almostMatches(pattern: list[str], i: int, j: int, n: int, seen: int) -> bool:
    if -1 == i or n == j:
        return 1 == seen
    seen += hamming(pattern[i], pattern[j])
    if seen > 1:
        return False
    return almostMatches(pattern, i-1, j+1, n, seen)

def findHorizontalPattern(pattern: list[str]) -> int:
    n = len(pattern)

    for i in range(n-1):
        if matches(pattern, i, i+1, n):
            return i+1
    return -1

def findVerticalPattern(pattern: list[str]) -> int:
    pattern = transpose(pattern)
    return findHorizontalPattern(pattern)

def hamming(a: str, b: str) -> int:
    n, res = len(a), 0

    for i in range(n):
        if a[i] != b[i]:
            res += 1

    return res

def findHorizontalPatternAlmost(pattern: list[str]) -> int:
    n = len(pattern)
    seen = 0

    for i in range(n-1):
        if almostMatches(pattern, i, i+1, n, seen):
            return i+1
    return -1

def findVerticalPatternAlmost(pattern: list[str]) -> int:
    pattern = transpose(pattern)
    return findHorizontalPatternAlmost(pattern)

def getPart1HorVert(patterns:list[str]) -> list[list[int]]:
    res = []
    for pattern in patterns:
        hor, vert = findHorizontalPattern(pattern), findVerticalPattern(pattern)
        res.append([hor, vert])
    return res

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

def part2(filePath: str = inpt) -> int:
    lines = getLines(filePath)

    patterns = getPatterns(lines)

    res = 0

    for i, pattern in enumerate(patterns):           

        hor, vert = findHorizontalPatternAlmost(pattern), findVerticalPatternAlmost(pattern)

        if -1 == hor and -1 == vert:
            print(f"Both hor, vert no almost reflections. Res += 0 but some error")
            res += 0

        elif -1 == hor:
            res += vert
        elif -1 == vert:
            res += hor * 100
        elif hor > 0 and vert > 0:
            print("Both hor vert have reflections, some kind of error!")

        if hor > 0 and vert > 0:
            print(i, res, hor, vert)

    print(f"The answer to part 2 is {res}")    
    
    return res


part1()
part2()
