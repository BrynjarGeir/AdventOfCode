def getLines(filePath: str) -> list[str]:
    with open(filePath) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines