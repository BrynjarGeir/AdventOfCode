import ast

#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = []
    flines = f.readlines()
    
    for i in range(0, len(flines), 3):
        curr = []
        curr.append(ast.literal_eval(flines[i]))
        curr.append(ast.literal_eval(flines[i+1]))
        lines.append(curr)

    
correct_order = []

def compare_lists(a, b):
    if type(a) == type(b) == int:
        if a > b:
            return -1
        elif a < b:
            return 1
        return 0
    elif type(a) == type(b) == list:
        n, m = len(a), len(b)
        res = 0
        for i in range(min(n,m)):
            res = compare_lists(a[i], b[i])
            if res:
                break
        if res == 0:
            if m < n:
                return -1
            elif m > n:
                return 1
            return 0
    elif type(a) == int:
        res = compare_lists([a], b)
    else:
        res = compare_lists(a, [b])
    
    return res

for index, line in enumerate(lines):
    if compare_lists(line[0], line[1]) == 1:
        correct_order.append(index+1)

print(sum(correct_order))