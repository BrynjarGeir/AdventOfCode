from utils.util import getLines
from math import floor, ceil

inpt = "./data/day6/input.txt"
test = "./data/day6/test.txt"

def getTD(lines: list[str]) -> (list[int], list[int]):
    times, distances = lines
    times = [int(item) for item in times.split()[1:]]
    distances = [int(item) for item in distances.split()[1:]]
    return times, distances

def solveQuad(a: int, b:int, c: int) -> (float, float):
    root = (b**2-4*a*c)**0.5
    r1 = (-b+root)/(2*a)
    r2 = (-b-root)/(2*a)
    return r1, r2

def squishTD(lines: list[str]) -> (int, int):
    time, distance = lines
    time = time.split(":")[1]
    distance = distance.split(":")[1]
    time = time.replace(" ", "")
    distance = distance.replace(" ", "")

    return int(time), int(distance)

def part1(filePath: str = inpt) -> int:
    lines = getLines(filePath)
    times, distances = getTD(lines)
    n = len(times)

    res = 1

    for i in range(n):
        r1, r2 = solveQuad(1, times[i], distances[i])
        l, u = min(r1, r2), max(r1, r2)
        if l.is_integer():
            l += 1
        if u.is_integer():
            u -= 1
        l, u = ceil(l), floor(u)
        mult = u - l + 1
        res *= mult
        
    print(f"The answer to part 1 is {res}")

    return res

def part2(filePath: str = inpt) -> int:
    lines = getLines(filePath)
    time, distance = squishTD(lines)
    print(time, distance)
    r1, r2 = solveQuad(1, -time, distance)
    print(r1, r2)
    l, u = min(r1, r2), max(r1, r2)
    if l.is_integer():
        l += 1
    if u.is_integer():
        u -= 1
    l, u = ceil(l), floor(u)

    res = u - l + 1 # should not have the +1 I guess or that gives the right answer
    print(f"The answer to part 2 is {res}")

    return res

part1()
part2()