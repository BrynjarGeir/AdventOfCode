import numpy as np, re
from itertools import product
from functools import reduce
from tqdm import tqdm, trange
input_path = './data/day7/input.txt'
test_path = './data/day7/test.txt'

with open(input_path, 'r') as f:
    lines = f.readlines()
    lines = [line.strip().split(':') for line in lines]
    results = [int(it[0]) for it in lines]
    numbers = [[int(it) for it in item[1].strip().split()] for item in lines]

def part1(results, numbers):
    n = len(results)
    ans = 0
    for i in trange(n):
        res, nums = results[i], numbers[i]
        operandsList = product(['+', '*'], repeat = len(nums)-1)
        for operands in operandsList:
            c = nums[0]
            for j in range(len(nums) - 1):
                c = eval(str(c) + operands[j] + str(nums[j+1]))
            if c == res:
                ans += res
                break
    return ans

def part2(results, numbers):
    n = len(results)
    ans = 0
    for i in trange(n):
        res, nums = results[i], numbers[i]
        operandsList = product(['+', '*', '||'], repeat = len(nums)-1)
        for operands in operandsList:
            c = nums[0]
            for j in range(len(nums) - 1):
                m = operands[j]
                if m == '*':
                    c *= nums[j+1]
                elif m == '+':
                    c += nums[j+1]
                else:
                    c = int(str(c) + str(nums[j+1]))
            if c == res:
                ans += res
                break
    return ans

print(f'Part 1: {part1(results, numbers)}')
print(f'Part 2: {part2(results, numbers)}')