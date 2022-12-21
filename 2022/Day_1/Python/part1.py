#data = '../data/part1_test.txt'
data = '../data/part1_input.txt'
with open(data) as f:
    lines = [line.rstrip() for line in f]

max_calories = -1
current_calories = 0

for line in lines:
    if line == '':
        max_calories = max(max_calories, current_calories)
        current_calories = 0
    else:
        current_calories += int(line)

print(max_calories)