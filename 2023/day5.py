from utils.util import getLines
from time import time

inpt = "./data/day5/input.txt"
test = "./data/day5/test.txt"

def getSeeds(seedLine: str) -> list[int]:
    _, seeds = seedLine.split(":")
    seeds = [int(seed) for seed in seeds.split()]
    return seeds

def getSeedsRng(seedLine: str) -> list[tuple[int]]:
    _, rng = seedLine.split(":")
    seed_rngs = rng.split()
    n = len(seed_rngs)
    seeds = [(int(seed_rngs[i]), int(seed_rngs[i+1])) for i in range(0, n-1, 2)]
    return seeds

def inSeeds(seed: int, seeds: list[tuple[int]]) -> bool:
    for seedRng in seeds:
        start, length = seedRng
        if seed >= start and seed <= start + length:
            return True
    return False

def findSeed(location: int, maps: dict(), map_order: list[str]) -> bool:
    map_order = map_order[::-1]
    seed = getLocationSeed(location, maps, map_order)
    return seed

def getMap(startLine: int, lines: list[str]) -> (str, list[tuple[int]], int):
    name, _ = lines[startLine].split()
    i, cmap = startLine+1, []
    n = len(lines)

    while i < n and lines[i] != "":
        d, s, l = [int(num) for num in lines[i].split()]
        cmap.append((d,s,l))
        i += 1
    return name, cmap, i

def getSeedLocations(seeds: list[int], maps: dict, map_order: list[str]) -> list[int]:
    res = []
    for seed in seeds:
        seed_location = getSeedLocation(seed, maps, map_order)
        res.append(seed_location)
    return res

def getSeedLocation(seed: int, maps: dict, map_order: list[str]) -> int:
    c_val = seed
    for m in map_order:
        c_val = getNextValue(c_val, maps[m])
    return c_val

def getLocationSeed(location: int, maps: dict, map_order: list[str]) -> int:
    c_val = location
    for m in map_order:
        c_val = getPrevVal(c_val, maps[m])
    return c_val

def getNextValue(c_val: int, m: list[list[int]]) -> int:
    for rng in m:
        d, s, l = rng
        if c_val >= s and c_val <= s + l-1:
            return d + (c_val - s)
    return c_val

def getPrevVal(c_val: int, m: list[list[int]]) -> int:
    for rng in m:
        d, s, l = rng
        if c_val >= d and c_val <= d + l - 1:
            return s + (c_val - d)
    return c_val
        
def part1(filePath: str = inpt) -> int:
    lines = getLines(filePath)

    startLine, n = 2, len(lines)
    maps, map_order = {}, []

    seeds = getSeeds(lines[0])

    while startLine < n:
        name, cmap, i = getMap(startLine, lines)
        map_order.append(name)
        maps[name], startLine = cmap, i+1
    
    seed_locations = getSeedLocations(seeds, maps, map_order)

    res = min(seed_locations)

    print(f"The answer to part 1 is {res}")

    return res

def part2(filePath: str = inpt):
    start = time()
    lines = getLines(filePath)

    startLine, n = 2, len(lines)
    maps, map_order = {}, []

    seeds = getSeedsRng(lines[0])

    while startLine < n:
        name, cmap, i = getMap(startLine, lines)
        map_order.append(name)
        maps[name], startLine = cmap, i+1

    res = 0
    while True:
        seed = findSeed(res, maps, map_order)
        b = inSeeds(seed, seeds)
        if b:
            break
        res += 1


    print(f"The answer to part 2 is {res}")

    end = time()

    print(f"The total runtime of part 2 is {end - start}")

    return res

part1()

part2()