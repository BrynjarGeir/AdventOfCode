from collections import deque
from functools import reduce

#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = [line.rstrip().split() for line in f.readlines()]

monkeys_items, monkeys_op, monkeys_test, monkeys_throw, monkeys_inspects = dict(), dict(), dict(), dict(), dict()

def lmbda_fun(op):
    if op[1] == '+' and op[2] == 'old':
        return lambda x: x * 2
    elif op[1] == '+':
        value = int(op[2])
        return lambda x: x + value
    elif op[1] == '*' and op[2] == 'old':
        return lambda x: x * x
    else:
        value = int(op[2])
        return lambda x: x * value

def mult(ans):
    sol = sorted(ans.values())[::-1][:2]
    return sol[0] * sol[1]

for i in range(0, len(lines), 7):

    monkey = int(lines[i][1].rstrip(':'))
    items = [int(value.rstrip(',')) for value in lines[i+1][2:]]
    op = lines[i+2][3:]
    test = int(lines[i+3][-1])
    throw = (int(lines[i+4][-1]), int(lines[i+5][-1]))

    monkeys_items[monkey] = deque(items)
    monkeys_op[monkey] = lmbda_fun(op)
    monkeys_test[monkey] = test
    monkeys_throw[monkey] = throw
    monkeys_inspects[monkey] = 0

rounds = 20

for i in range(rounds):
    for monkey in monkeys_items:
        if not monkeys_items[monkey]:
            continue
        while monkeys_items[monkey]:
            monkeys_inspects[monkey] += 1
            item = monkeys_items[monkey].popleft()
            value = monkeys_op[monkey](item)//3
            if not value % monkeys_test[monkey]:
                monkeys_items[monkeys_throw[monkey][0]].append(value)
            else:
                monkeys_items[monkeys_throw[monkey][1]].append(value)

print(monkeys_inspects)
print(mult(monkeys_inspects))