test_path = "./data/day2/test.txt"
input_path = "./data/day2/input.txt"

import numpy as np

with open(input_path, 'r') as f:
    lines = [line.split() for line in f.readlines()]
    lines = [[int(item) for item in line] for line in lines]

def isSafe(x):
    return np.logical_or(np.logical_and(np.all(np.diff(x) > 0), np.all(np.diff(x) <= 3)), 
                  np.logical_and(np.all(np.diff(x) < 0), np.all(np.diff(x) >= -3)))

a, b = 0, 0
for line in lines:
    x = np.array(line)
    c = isSafe(x)
    a = a + c

    if c:
        b = b + c
    else:
        perms = [np.delete(x, i) for i in range(len(x))]
        for p in perms:
            c = isSafe(p)
            if c:
                b = b + c
                break
        

print(f'Part 1: {a}')
print(f'Part 2: {b}')
