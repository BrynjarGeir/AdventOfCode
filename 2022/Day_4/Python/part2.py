#file = '../data/test'
file = '../data/input'


with open(file) as f:
    lines = [line.rstrip().split(',') for line in f.readlines()]

covered = 0

for line in lines:

    e1 = line[0].split('-')
    e2 = line[1].split('-')

    e11 = int(e1[0])
    e12 = int(e1[1])
    e21 = int(e2[0])
    e22 = int(e2[1])

    if e11 <= e21 and e12 >= e21:
        covered += 1
    elif e11 >= e21 and e11 <= e22:
        covered += 1
   

print(covered)