from math import log10
from time import time

input_path = './data/day11/input.txt'
test_path = './data/day11/test.txt'

with open(input_path, 'r') as f:
    digits = f.readline().strip().split()
    digits = [int(digit) for digit in digits]

def NumDigits(n):
    if n == 0:
        return 1
    return int(log10(n)) + 1

def getBlink(digit):
    numD = NumDigits(digit)
    if digit == 0:
        return [1]
    elif not numD % 2:
        l, r = divmod(digit, 10 ** (numD//2))
        return [l, r]
    else:
        return [digit * 2024]

def blinkDigits(seen, digits):
    newDigits = {}
    for digit in digits.keys():
        if digit in seen:
            d = seen[digit]
        else:
            d = getBlink(digit)
            seen[digit] = d
        n = digits[digit]
        for num in d:
            if num not in newDigits:
                newDigits[num] = 0
            newDigits[num] += n
    return seen, newDigits

def solve(digits, num_blinks):
    seen, digits = {}, dict(zip(digits, [1 for _ in range(len(digits))]))
    for _ in range(num_blinks):
        seen, digits = blinkDigits(seen, digits)
    return sum(digits.values())

def part1(digits, num_blinks = 25):
    return solve(digits, num_blinks)

def part2(digits, num_blinks = 75):
    return solve(digits, num_blinks)

s = time()
print(f"Part 1: {part1(digits)}")
m = time()
print(f"Part 2: {part2(digits)}")
e = time()
print(f"First part took {(m-s)*1000:.0} ms")
print(f"Second part took {(e-m)*1000:.0} ms")