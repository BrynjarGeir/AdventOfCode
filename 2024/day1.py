test_path = "./data/day1/test.txt"
input_path = "./data/day1/input.txt"

import numpy as np

with open(input_path, 'r') as f:
    lines = [line.split() for line in f.readlines()]
    f1, f2 = [item[0] for item in lines], [item[1] for item in lines]
    f1, f2 = [int(i) for i in f1], [int(i) for i in f2]
    f1.sort(), f2.sort()

f1, f2 = np.array(f1), np.array(f2)

print(f'Part 1: {np.sum(np.absolute(f2 - f1))}')

unique, counts = np.unique(f2, return_counts = True)
counts = dict(zip(unique, counts))
x = np.vectorize(lambda a: a * counts.get(a, 0))

print(f'Part 2: {np.sum(x(f1))}')