from utils.util import getLines

inpt = './data/day15/input.txt'
test = './data/day15/test.txt'

def runHASH(s: str) -> int:
    cv = 0

    for c in s:
        asc = ord(c)
        cv += asc
        cv *= 17
        cv %= 256
    return cv

def parseOperation(s: str) -> list[str]:
    if '-' in s:
        return [s[:-1]]

    else:
        a, b = s.split('=')
        res = [a, b]
    return res

def parseOperations(sequence: list[str]) -> list[list[str]]:
    ops = [parseOperation(s) for s in sequence]

    return ops

def doMinus(op: str, boxes: dict) -> dict:
    index = runHASH(op)
    if index in boxes:
        boxes[index] = [i for i in boxes[index] if i[0] != op]

    return boxes
    
def doUpdate(op: list[str], boxes: dict) -> dict:
    label, number = op
    number = int(number)
    index = runHASH(label)

    if index in boxes:
        labels = [i[0] for i in boxes[index]]
        if label in labels:
            ind = labels.index(label)
            boxes[index][ind] = [label, number]
        else:
            boxes[index].append([label, number])
    else:
        boxes[index] = [[label, number]]

    return boxes

def getFocusingPower(box: list[list[str]], boxIndex: int) -> int:
    res = 0
    for i,lens in enumerate(box):
        res += boxIndex * (i+1) * lens[1]
    return res

def getTotalFocusingPower(boxes: dict) -> int:
    res = sum([getFocusingPower(boxes[key], key+1) for key in boxes])
    return res
    
def part1(filePath: str = inpt) -> int:
    lines = getLines(filePath)

    sequence = lines[0].split(',')

    res = 0

    for s in sequence:
        c = runHASH(s)
        res += c

    print(f"The answer to part 1 is {res}")

    return res

def part2(filePath: str = inpt) -> int:
    lines = getLines(filePath)
    sequence = lines[0].split(',')

    boxes = {}
    ops = parseOperations(sequence)

    for op in ops:
        if len(op) == 1:
            boxes = doMinus(op[0], boxes)
        else:
            boxes = doUpdate(op, boxes)

    res = getTotalFocusingPower(boxes)

    print(f"The answer to part 2 is {res}")

    return res

part1()
part2()