import ast

#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = []
    flines = f.readlines()
    
    for i in range(0, len(flines), 3):
        lines.append(ast.literal_eval(flines[i]))
        lines.append(ast.literal_eval(flines[i+1]))

lines.append([[2]])
lines.append([[6]])

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


change = True
while change:
    change = False

    for i in range(len(lines)-1):
        curr = compare_lists(lines[i], lines[i+1])
        if curr == -1:
            tmp = lines[i]
            lines[i] = lines[i+1]
            lines[i+1] = tmp
            change = True
            break

ans = []
for index, line in enumerate(lines):
    if line == [[2]] or line == [[6]]:
        ans.append(index+1)

print(ans[0] * ans[1])
