#file = '../data/test.txt'
file = '../data/input.txt'


with open(file) as f:
    lines = [line.rstrip() for line in f.readlines()]

sum_total = 0

for index in range(0, len(lines), 3):

    first = set(lines[index])
    second = set(lines[index+1])
    third = set(lines[index+2])

    ans = first.intersection(second)
    ans = ans.intersection(third).pop()

    if ans.isupper():
        sum_total += ord(ans) - ord('A') + 27
    else:
        sum_total += ord(ans) - ord('a') + 1

print(sum_total)