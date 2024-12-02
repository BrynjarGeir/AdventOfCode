import heapq

def dijsktra_with_constraints(graph: dict, grid: list[str], start: tuple[int, int], end: tuple[int, int], max_moves: int) -> int:
    dist, prev = {}, {}
    dist[start] = 
    for v in graph:
   

    return float('inf')

def createGraph(grid: list[str]):
    graph = dict()
    n, m = len(grid), len(grid[0])

    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            nghbrs = getNeighbors(i, j, n, m)
            graph[(i, j)] = []
            for nghbr in nghbrs:
                r, c = nghbr
                cost = int(grid[r][c])
                graph[(i, j)].append(((r,c), cost))

    return graph

def getNeighbors(i: int, j: int, n: int, m: int):
    nghbrs = []
    if i > 0:
        nghbrs.append((i-1, j))
    if i < n-1:
        nghbrs.append((i+1, j))
    if j > 0:
        nghbrs.append((i, j-1))
    if j < m-1:
        nghbrs.append((i, j+1))

    return nghbrs
    
