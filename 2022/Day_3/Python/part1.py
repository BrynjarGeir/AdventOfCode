#file = '../data/test.txt'
file = '../data/input.txt'


with open(file) as f:
    lines = [line.rstrip() for line in f.readlines()]

sum_total = 0

for line in lines:

    middle = len(line) // 2

    first = line[:middle]
    second = line[middle:]

    first = set(first)
    second = set(second)

    ans = first.intersection(second).pop()

    if ans.isupper():
        sum_total += ord(ans) - ord('A') + 27
    else:
        sum_total += ord(ans) - ord('a') + 1

print(sum_total)