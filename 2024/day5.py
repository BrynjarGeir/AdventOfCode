import numpy as np, re

input_path = './data/day5/input.txt'
test_path = './data/day5/test.txt'

with open(input_path, 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    
    index = lines.index('')
    rules = lines[:index]
    updates = lines[index+1:]

    rules = [rule.split('|') for rule in rules]
    updates = [update.split(',') for update in updates]

    rules = [(int(rule[0]), int(rule[1])) for rule in rules]
    updates = [[int(upd) for upd in update] for update in updates]

tmp = {}
for rule in rules:
    a, b = rule
    if a in tmp:
        tmp[a].add(b)
    else:
        tmp[a] = set([b])
rules = tmp

def validateUpdate(update, rules):
    seen = set()
    for pgn in update:
        if len(seen) == 0 or pgn not in rules or len(rules[pgn].intersection(seen)) == 0:
            seen.add(pgn)
        else:
            return False
    return True

counter = 0
for update in updates:
    if validateUpdate(update, rules):
        i = len(update)//2
        counter += update[i]

print(f'Part 1: {counter}')

def makeUpdate(update, rules, a, i):
    if a not in rules:
        return update
    for j in range(i-1, -1, -1):
        b = update[j]
        if b in rules[a]:
            update = update[:j] + update[j+1:i+1] + [b] + update[i+1:]
    return update

def part2(updates, rules):
    ans = 0
    for update in updates:
        if not validateUpdate(update, rules):
            while not validateUpdate(update, rules):
                for i, a in enumerate(update[::-1]):
                    update = makeUpdate(update, rules, a, len(update) - 1 - i)
            n = len(update)//2
            ans += update[n]
    return ans


print(f'Part 2: {part2(updates, rules)}')
                    