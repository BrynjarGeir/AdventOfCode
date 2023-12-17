from utils.util import getLines

inpt = "./data/day9/input.txt"
test = "./data/day9/test.txt"

def getSequences(lines: list[str]) -> list[list[int]]:
    return [[int(item) for item in line.split()] for line in lines]

def getDifferenceSequence(sequence: list[int]) -> list[str]:
    
    res, prev = [], None

    for item in sequence:
        if prev == None:
            prev = item
        else:
            diff = item - prev
            prev = item
            res.append(diff)
    
    return res

def getNextValue(sequence: list[int]) -> int:

    c, lvls = sequence, [sequence]

    while any(c):
        c = getDifferenceSequence(c)
        lvls.append(c)
    
    last = [lvls[i][-1] for i in range(len(lvls))]

    return sum(last)

def getNextValues(sequences: list[int]) -> list[int]:
    return [getNextValue(sequence) for sequence in sequences]

def getPrevValue(sequence: list[int]) -> int:

    c, lvls = sequence, [sequence]

    while any(c):
        c = getDifferenceSequence(c)
        lvls.append(c)
    res = 0
    for lvl in lvls[::-1][1:]:
        tmp = lvl[0] - res
        res = tmp

    return res

def getPrevValues(sequences: list[int]) -> int:
    return [getPrevValue(sequence) for sequence in sequences]

def part1(filePath: str = inpt) -> int:
    lines = getLines(filePath)
    sequences = getSequences(lines)
    nextValues = getNextValues(sequences)
    res = sum(nextValues)

    print(f"The answer to part 1 is {res}")

    return res

def part2(filePath: str = inpt) -> int:
    lines = getLines(filePath)
    sequences = getSequences(lines)
    prevValues = getPrevValues(sequences)
    res = sum(prevValues)

    print(f"The answer for part 2 is {res}")

    return res

part1()

part2()