import numpy as np, re

input_path = './data/day3/input.txt'
test1_path = './data/day3/test1.txt'
test2_path = './data/day3/test2.txt'

with open(input_path, 'r') as f:
    lines = f.readlines()

string = ''.join(lines)
res = re.findall(r'mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)', string)
res = [item[4:-1].split(',') for item in res]
res = [(int(a[0]), int(a[1])) for a in res]
res = np.array(res)
res = np.prod(res, axis = 1)
res = sum(res)

print(f'Part 1: {res}')

#with open(test2_path, 'r') as f:
#    lines = f.readlines()

#string = ''.join(lines)
res = re.findall(r"mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)|don't\(\)|do\(\)", string)

res = [item[4:-1].split(',') if item.startswith('mul') else item for item in res]
ib, status = [], True
for item in res:
    if item == "don't()":
        status = False
    elif item == "do()":
        status = True
    elif status:
        ib.append(item)
res = ib
res = [(int(a[0]), int(a[1])) for a in res]
res = np.array(res)
res = np.prod(res, axis = 1)
res = sum(res)

print(f'Part 2: {res}')