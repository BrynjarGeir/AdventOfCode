#file = '../data/test'
file = '../data/input'

from sympy import Symbol
from sympy.solvers import solve

with open(file) as f:
    lines = [line.split(': ') for line in f.readlines()]
    lines = [[line[0], line[1].split()] if len(line[1].split()) > 1 else [line[0], int(line[1])] for line in lines]

operators = {'*': lambda x: x[0] * x[1], '/': lambda x: x[0] / x[1], '-': lambda x: x[0] - x[1], '+': lambda x: x[0] + x[1], '=': lambda x: x}
monkeys = {}

for line in lines:
    monkey = line[0]
    monkeys[monkey] = line[1]

x = Symbol('x')
monkeys['humn'] = x
monkeys['root'][1] = '='

def figure_out(monkeys):
    change = True
    while change:
        change = False
        for monkey in monkeys:
            if not isinstance(monkeys[monkey], list):
                continue
            elif not isinstance(monkeys[monkey][0], str) and not isinstance(monkeys[monkey][2], str):
                fun = operators[monkeys[monkey][1]]
                t = (monkeys[monkey][0], monkeys[monkey][2])
                updated = fun(t)
                monkeys[monkey] = updated
            else:
                if isinstance(monkeys[monkey][0], str) and not isinstance(monkeys[monkeys[monkey][0]], list):
                    monkeys[monkey][0] = monkeys[monkeys[monkey][0]]
                if isinstance(monkeys[monkey][2], str) and not isinstance(monkeys[monkeys[monkey][2]], list):
                    monkeys[monkey][2] = monkeys[monkeys[monkey][2]]
            
            change = True

figure_out(monkeys)

eq = monkeys['root']
ans = solve(eq[0] - eq[1], x)

print(eq)
print(ans[0])

#for monkey in monkeys:
#    print(monkey, ':', monkeys[monkey])