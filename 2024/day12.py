def read_and_map_regions(file_path):
    # Read the file and process it into a 2D array
    with open(file_path, 'r') as file:
        array = [list(line.strip()) for line in file]

    rows, cols = len(array), len(array[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    regions = {}
    region_id = 0

    def dfs(r, c, symbol):
        # Perform depth-first search to mark all connected cells
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or array[r][c] != symbol:
            return
        visited[r][c] = True
        if region_id not in regions:
            regions[region_id] = []
        regions[region_id].append((r, c))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Four primary directions
            dfs(r + dr, c + dc, symbol)

    # Iterate through the array to find regions
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                region_id += 1
                dfs(r, c, array[r][c])

    return len(array), len(array[0]), regions

def get_num_neighbors(cell, region):
    # Count the number of neighbors in the same region
    row, col = cell
    neighbors = 0
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Four primary directions
        new_row, new_col = row + dr, col + dc
        if (new_row, new_col) in region:
            neighbors += 1
    return neighbors

def lies_on_line(cell, visited, n, m):
    r, c = cell
    for dr in range(-n, n):
        if (r + dr, c) in visited:
            return True
    for dc in range(-m, m):
        if (r, c + dc) in visited:
            return True
    return False

def get_area(regions):
    area = {}
    for region_id, cells in regions.items():
        area[region_id] = len(cells)
    return area
def get_perimeter(regions):
    perimiter = {}
    for region_id in regions:
        cells = regions[region_id]
        c_perimeter = 0
        for cell in cells:
            gnn = get_num_neighbors(cell, regions[region_id])
            c_perimeter += 4 - gnn
        perimiter[region_id] = c_perimeter
    return perimiter

def get_corner_points(regions, n, m):
    corners = {}
    for region_id in regions:
        corners[region_id] = []
        cells = regions[region_id]
        for cell in cells:
            r, c = cell
            # Outer corners
            if not (r-1, c) in cells and not (r, c-1) in cells:
                corners[region_id].append(cell)
            if not (r+1, c) in cells and not (r, c+1) in cells:
                corners[region_id].append(cell)
            if not (r-1, c) in cells and not (r, c+1) in cells:
                corners[region_id].append(cell)
            if not (r+1, c) in cells and not (r, c-1) in cells:
                corners[region_id].append(cell)
            # Inner corners
            if (r-1, c) in cells and (r, c-1) in cells and not (r-1, c-1) in cells:
                corners[region_id].append(cell)
            if (r+1, c) in cells and (r, c+1) in cells and not (r+1, c+1) in cells:
                corners[region_id].append(cell)
            if (r-1, c) in cells and (r, c+1) in cells and not (r-1, c+1) in cells:
                corners[region_id].append(cell)
            if (r+1, c) in cells and (r, c-1) in cells and not (r+1, c-1) in cells:
                corners[region_id].append(cell)
            
    return corners

def solve_part1(regions):
    areas, perimiters = get_area(regions), get_perimeter(regions)
    ans = 0
    for region_id in regions:
        #print(f"Region {region_id}: {areas[region_id]} * {perimiters[region_id]} = {areas[region_id] * perimiters[region_id]}")
        ans += areas[region_id] * perimiters[region_id]
    return ans
def solve_part2(regions, n, m):
    areas, corners = get_area(regions), get_corner_points(regions, n, m)
    ans = 0
    for region_id in regions:
        #print(f"Region {region_id}: {areas[region_id]} * {corners[region_id]} = {areas[region_id] * corners[region_id]}")
        ans += areas[region_id] * len(corners[region_id])
    return ans

file_path = './2024/data/day12/input.txt'
n, m, regions = read_and_map_regions(file_path)
p1 = solve_part1(regions)
p2 = solve_part2(regions, n, m)
print(f"Part 1: {p1}")
# For part 2, thanks go to this comment: https://www.reddit.com/r/adventofcode/comments/1hdg24l/comment/m1vpmb0/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
print(f"Part 2: {p2}")