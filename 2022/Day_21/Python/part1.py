#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = [line.split(': ') for line in f.readlines()]
    lines = [[line[0], line[1].split()] if len(line[1].split()) > 1 else [line[0], int(line[1])] for line in lines]

operators = {'*': lambda x: x[0] * x[1], '/': lambda x: x[0] // x[1], '-': lambda x: x[0] - x[1], '+': lambda x: x[0] + x[1]}
monkeys = {}

for line in lines:
    monkey = line[0]
    monkeys[monkey] = line[1]

def figure_out(monkeys):
    change = True
    while change:
        change = False
        for monkey in monkeys:
            if isinstance(monkeys[monkey], int):
                continue
            elif isinstance(monkeys[monkey][0], int) and isinstance(monkeys[monkey][2], int):
                fun = operators[monkeys[monkey][1]]
                t = (monkeys[monkey][0], monkeys[monkey][2])
                updated = fun(t)
                monkeys[monkey] = updated
            else:
                if not isinstance(monkeys[monkey][0], int) and isinstance(monkeys[monkeys[monkey][0]], int):
                    monkeys[monkey][0] = monkeys[monkeys[monkey][0]]
                if not isinstance(monkeys[monkey][2], int) and isinstance(monkeys[monkeys[monkey][2]], int):
                    monkeys[monkey][2] = monkeys[monkeys[monkey][2]]
            
            change = True

figure_out(monkeys)

print(monkeys['root'])
