from utils.util import getLines
from utils.algorithms import dijsktra_with_constraints, createGraph

inpt = './data/day17/input.txt'
test = './data/day17/test.txt'

def part1(filePath: str = inpt) -> int:
    grid = getLines(filePath)
    n, m = len(grid), len(grid[0])

    graph = createGraph(grid)

    res = dijsktra_with_constraints(graph, (0,0), (n-1, m-1), 3)

    print(f"The answer to part 1 is {res}")

    return res

part1(test)