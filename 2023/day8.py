from utils.util import getLines
from math import lcm

inpt = './data/day8/input.txt'
test = './data/day8/test.txt'
test2 = './data/day8/test2.txt'


def findStartingPositions(mapping: dict()) -> list[str]:
    res = []
    for key in mapping:
        if key[-1] == 'A':
            res.append(key)
    return res

def findPath(mapping: dict(), position: str, directions: list[int]) -> int:
    res, n, i = 0, len(directions), 0

    while True:
        next = mapping[position][directions[i]]
        res += 1
        if next[-1] == 'Z':
            return res
        position = next
        i += 1
        
        i = 0 if i == n else i

def findAllPaths(mapping: dict, startingPositions: list[str], directions: list[int]) -> int:
    res = [findPath(mapping, position, directions) for position in startingPositions]
    return lcm(*res)

def populateMap(lines: list[str]) -> dict:
    mapping, instructions = dict(), ""

    seen_empty = False

    for line in lines:
        if line == "":
            seen_empty = True
            continue
        if seen_empty:
            station, LR = line.split("=")
            station = station.strip()
            LR = LR.strip()
            left, right = LR.split(", ")
            left, right = left[1:], right[:-1]

            mapping[station] = [left, right]
        else:
            instructions += line
    instructions = [1 if i == 'R' else 0 for i in instructions]
    return mapping, instructions

def part1(filePath: str = inpt) -> int:
    lines = getLines(filePath)

    mapping, instructions = populateMap(lines)
    position, target, instruction, end_of_instructions = 'AAA', 'ZZZ', 0, len(instructions)
    res = 0

    while True:
        if position == target:
            break
        instr = instructions[instruction]
        position = mapping[position][instr]
        res += 1
        instruction += 1

        if instruction == end_of_instructions:
            instruction = 0

    print(f"The answer to part 1 is {res}")

    return res

def part2(filePath: str = inpt) -> int:
    lines = getLines(filePath)
    mapping, directions = populateMap(lines)
    startingPositions = findStartingPositions(mapping)

    res = findAllPaths(mapping, startingPositions, directions)

    print(f"The answer to part 2 is {res}")

    return res

part1()

part2()