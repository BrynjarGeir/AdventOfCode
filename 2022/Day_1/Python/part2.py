#data = '../data/part1_test.txt'
data = '../data/part1_input.txt'
with open(data) as f:
    lines = [line.rstrip() for line in f]

current_calories = 0
calories = []

for index, line in enumerate(lines):
    if line == '':
        calories.append(current_calories)
        current_calories = 0
    else:
        current_calories += int(line)

calories.append(current_calories)

ans = sorted(calories)[::-1]
sol = sum(ans[:3])

print(sol)