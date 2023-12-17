from utils.util import getLines

inpt = "./data/day2/input.txt"
test = "./data/day2/test.txt"

def legalGame(game: str) -> bool:
    mR, mG, mB = minimumLegalGame(game)
    
    return mR <= 12 and mG <= 13 and mB <= 14

def minimumLegalGame(game: str) -> list[int]:
    id, game = game.split(": ")
    parts = game.split(";")

    id = int(id.split()[1])
    mR, mG, mB = -1, -1, -1

    for part in parts:
        colors = part.split(",")
        for color in colors:
            v, c = color.split()
            v = int(v)
            if c == "red":
                mR = max(mR, v)
            elif c == "green":
                mG = max(mG, v)
            else:
                mB = max(mB, v)
    return mR, mG, mB

def powerOfCubes(mR, mG, mB):
    return mR * mG * mB

def part1(filepath: str = inpt) -> int:
    lines = getLines(filepath)

    possible = set()

    for i, game in enumerate(lines):
        c = legalGame(game)
        if c:
            possible.add(i+1)

    ans = sum(possible)
    
    print(f"The answer to part 1 is {ans}")

    return ans

def part2(filepath: str = inpt) -> int:
    lines = getLines(filepath)
    ans = 0

    for game in lines:
        mR, mG, mB = minimumLegalGame(game)
        c = powerOfCubes(mR, mG, mB)
        ans += c

    print(f"The answer to part 2 is {ans}")

    return ans


part1()
part2(test)
