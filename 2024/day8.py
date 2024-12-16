from itertools import combinations
from pprint import pp

input_path = './data/day8/input.txt'
test_path = './data/day8/test.txt'

with open(input_path, 'r') as f:
    lines = f.readlines()
    lines = [list(line.strip()) for line in lines]

def createMap(lines):
    map, nodes = {}, set()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != '.':
                if c not in map:
                    map[c] = [(i, j)]
                else:
                    map[c].append((i, j))
                nodes.add((i, j))
    return map, nodes, len(lines), len(lines[0])

def getDist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def createAntiNodesP1(p1, p2):
    rd, cd = abs(p1[0] - p2[0]), abs(p1[1] - p2[1])
    n11, n12 = p1
    n21, n22 = p2
    if n11 < n21:
        n11 -= rd
        n21 += rd
    else:
        n11 += rd
        n21 -= rd
    if n12 < n22:
        n12 -= cd
        n22 += cd
    else:
        n12 += cd
        n22 -= cd

    return (n11, n12), (n21, n22)

def createAntiNodesP2(p1, p2, r, c):
    rd, cd = p1[0] - p2[0], p1[1] - p2[1]
    n11, n12 = p1
    n21, n22 = p2
    res = set([p1, p2])

    cx, cy = n11, n12
    while 0 <= cx <= r and 0 <= cy <= c:
        cx -= rd
        cy -= cd
        res.add((cx, cy))
    cx, cy = n11, n12
    while 0 <= cx <= r and 0 <= cy <= c:
        cx += rd
        cy += cd
        res.add((cx, cy))
    
    return res    

def part1(lines):
    map, nodes, r, c =  createMap(lines)
    antinodes = set()

    for node in map:
        cnodes = map[node]
        combs = combinations(cnodes,2)
        for comb in combs:
            a1, a2 = createAntiNodesP1(*comb)
            antinodes.update([a1, a2])
    to_remove = set()
    for an in antinodes:
        anr, anc = an
        if 0 <= anr < r and 0 <= anc < c:
            continue
        to_remove.add(an)
    antinodes = antinodes.difference(to_remove)

    return len(antinodes)

def part2(lines):
    map, nodes, r, c =  createMap(lines)
    antinodes = set()

    for node in map:
        cnodes = map[node]
        combs = combinations(cnodes,2)
        for comb in combs:
            ants = createAntiNodesP2(*comb, r, c)
            antinodes.update(ants)
    to_remove = set()
    for an in antinodes:
        anr, anc = an
        if 0 <= anr < r and 0 <= anc < c:
            continue
        to_remove.add(an)
    antinodes = antinodes.difference(to_remove)
    return len(antinodes)

print(f'Part 1: {part1(lines)}')
print(f'Part 2: {part2(lines)}')