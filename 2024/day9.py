from itertools import combinations
from pprint import pp
import numpy as np

input_path = './data/day9/input.txt'
test_path = './data/day9/test.txt'

with open(input_path, 'r') as f:
    line = f.readline().strip()

def parseLine(line):
    diskMap, freeSpace = {}, {}
    id = 0
    for i,c in enumerate(line):
        if not i % 2:
            diskMap[id] = int(c)
        else:
            freeSpace[id] = int(c)
            id += 1
    return diskMap, freeSpace

def part1(line):
    diskMap, freeSpace = parseLine(line)
    res = []
    while diskMap and freeSpace:
        if len(diskMap.keys()) == 1:
            minDiskKey = min(diskMap.keys())
            res.extend([minDiskKey for _ in range(diskMap[minDiskKey])])
            break

        minDiskKey, minSpaceKey = min(diskMap.keys()), min(freeSpace.keys())
        cFree = freeSpace[minSpaceKey]
        res.extend([minDiskKey for _ in range(diskMap[minDiskKey])])
        while cFree > 0:
            maxDiskKey = max(diskMap.keys())
            fileSize = diskMap[maxDiskKey]
            if fileSize >= cFree:
                diskMap[maxDiskKey] -= cFree
                res.extend([maxDiskKey for _ in range(cFree)])
                cFree = 0
            else:
                cFree -= fileSize
                res.extend([maxDiskKey for _ in range(fileSize)])
                diskMap.pop(maxDiskKey)
        freeSpace.pop(minSpaceKey)
        diskMap.pop(minDiskKey)
    ans = sum([i * e for i, e in enumerate(res)])
    return ans

def part2(line):
    diskMap, freeSpace = parseLine(line)
    res = {id:[id for _ in range(diskMap[id])] for id in diskMap}
    for node in list(diskMap.keys())[::-1]:
        needed = diskMap[node]
        for id in freeSpace:
            if id >= node:
                break
            if freeSpace[id] >= needed:
                if id in res:
                    res[id].extend([node for _ in range(needed)])
                else:
                    res[id] = [node for _ in range(needed)]
                if all(res[node]) == node:
                    res.pop(node)
                else:
                    res[node] = [it if it != node else '.' for it in res[node] ]
                if needed == freeSpace[id]:
                    freeSpace.pop(id)
                else:
                    freeSpace[id] -= needed
                break
    diskMap, freeSpace = parseLine(line)
    ans = []
    for node in res:
        if node != max(diskMap.keys()):
            add = diskMap[node] + freeSpace[node] - len(res[node])
            ans.extend(res[node] + ['.' for _ in range(add)])
        else:
            ans.extend(res[node])
    return sum([i*e for i, e in enumerate(ans) if isinstance(e, int)])

print(f"Part 1: {part1(line)}")
print(f"Part 2: {part2(line)}")