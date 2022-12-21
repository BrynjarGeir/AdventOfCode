# test has 5 different test lines while input only one complete
#file = '../data/test'
file = '../data/input'

with open(file) as f:
    lines = [line.rstrip() for line in f.readlines()]


for line in lines:
    for i in range(14, len(line)):
        if len(set(line[i-14:i])) == 14:
            print(i)
            break
