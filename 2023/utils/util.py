def getLines(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines