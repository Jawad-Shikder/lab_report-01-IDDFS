from collections import deque

def is_valid(x, y, grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

def dfs_limited(x, y, tx, ty, grid, depth, path, visited, traversal):
    if depth < 0:
        return False
    
    traversal.append((x, y))
    
    if (x, y) == (tx, ty):
        path.append((x, y))
        return True

    visited.add((x, y))

    
    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if is_valid(nx, ny, grid) and (nx, ny) not in visited:
            if dfs_limited(nx, ny, tx, ty, grid, depth - 1, path, visited, traversal):
                path.append((x, y))
                return True

    return False

def iddfs(start, target, grid):
    sx, sy = start
    tx, ty = target

    max_depth = len(grid) * len(grid[0])

    for depth in range(max_depth + 1):
        path, traversal = [], []
        visited = set()

        if dfs_limited(sx, sy, tx, ty, grid, depth, path, visited, traversal):
            path.reverse()
            return depth, path, traversal

    return -1, [], []




2 
rows, cols = map(int, input().split())

grid = []
for _ in range(rows):
    grid.append(list(map(int, input().split())))

sx, sy = map(int, input().split())
tx, ty = map(int, input().split())


depth, path, traversal = iddfs((sx, sy), (tx, ty), grid)


if depth == -1:
    print(f"Path not found at max depth 6 using IDDFS")
else:
    print(f"Path found at depth {depth} using IDDFS")
    print("Traversal Order:", traversal)
