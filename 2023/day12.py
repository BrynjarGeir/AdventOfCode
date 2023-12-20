from utils.util import getLines

inpt = './data/day12/input.txt'
test = './data/day12/test.txt'

memo = {}

def isValid(string: str, pattern: str) -> bool:
    pattern = pattern.split(",")
    pattern = [int(i) for i in pattern]
    groups = []

    current = ''

    for c in string:
        if c == '#':
            current += c
        elif c == '.' and current != '':
            groups.append(len(current))
            current = ''
        else:
            current = ''
    if current != '':
        groups.append(len(current))

    n, m = len(groups), len(pattern)
    
    return n == m and all([groups[i] == pattern[i] for i in range(n)])

def generatePermutations(s, index = 0):
    permutations = []

    if index == len(s):
        return [s]
    
    if s[index] == '?':
        s_list = list(s)
        s_list[index] = '.'
        permutations.extend(generatePermutations(''.join(s_list), index+1))

        s_list[index] = '#'
        permutations.extend(generatePermutations(''.join(s_list), index+1))
    else:
        permutations.extend(generatePermutations(s, index+1))

    return permutations

def score(s: str, pattern: list[int], i: int = 0, pi: int = 0, current: int = 0) -> int:
    key = (i, pi, current)

    if key in memo:
        return memo[key]
    
    if i == len(s):
        if pi == len(pattern) and current == 0:
            return 1
        elif pi == len(pattern) - 1 and pattern[pi] == current:
            return 1
        else:
            return 0
    res = 0

    for c in '.#':
        if s[i] == c or s[i] == '?':
            if c == '.' and current == 0:
                res += score(s, pattern, i+1, pi, 0)
            elif c == '.' and current > 0 and pi < len(pattern) and pattern[pi] == current:
                res += score(s, pattern, i+1, pi+1, 0)
            elif c == '#':
                res += score(s, pattern, i+1, pi, current + 1)

    memo[key] = res
    return res


def part1(filePath: str = inpt) -> int:
    lines = getLines(filePath)

    res = 0

    for line in lines:
        s, pattern = line.split()
        permutations = generatePermutations(s)

        for permutation in permutations:
            if isValid(permutation, pattern):
                res += 1

    print(f"The answer to part 1 is {res}")

    return res

# !Greatly helped by! [taken from] https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/12.py
def part2(filePath: str = inpt) -> int:
    lines = getLines(filePath)

    res = 0

    for line in lines:
        s, pattern = line.split()
        s = '?'.join([s, s, s, s, s])
        pattern = ','.join([pattern, pattern, pattern, pattern, pattern])
        pattern = [int(x) for x in pattern.split(',')]

        memo.clear()

        res += score(s, pattern)

    print(f"The answer to part 2 is {res}")

    return res

part2()