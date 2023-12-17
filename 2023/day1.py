from utils.util import getLines

inpt = "./data/day1/input.txt"
test = "./data/day1/test.txt"
test2 = "./data/day1/test2.txt"

digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
           'seven': 7, 'eight': 8, 'nine': 9}

def part1(filepath: str = inpt) -> int:
    lines = getLines(filepath)
    res = []

    for line in lines:
        start, end = None, None

        for c in line:
            if start == None and c.isdigit():
                start = int(c)
            elif c.isdigit():
                end = c
        if end == None:
            end = start
        else:
            end = int(end)
        curr = 10 * start + end
        res.append(curr)

    ans = sum(res)
    print(f"The answer for part 1 is {ans}")

    return ans

def part2(filepath: str = inpt) -> int:
    lines = getLines(filepath)
    res = []
    
    for line in lines:
        start, end, p = None, None, ''
        line = line.strip()
        n, i = len(line), 0
        j = 0
        while i < n:
            c = line[i]
            p += c                
            if start == None and p in digits.keys():
                start = digits[p]
                p = ''
            elif start == None and c.isdigit():
                start = int(c)
                p = ''
            elif start != None and p in digits.keys():
                end = digits[p]
                p = ''
            elif start != None and c.isdigit():
                end = int(c)
                p = ''

            if not any(s.startswith(p) for s in digits.keys()):
                i = j + 1
                j += 1
                p = ''
            else:
                i += 1


        if end == None:
            end = start
        curr = 10 * start + end
        res.append(curr)
   
    ans = sum(res)

    print(f"The answer for part 2 is {ans}")

    return ans

part1()
part2()