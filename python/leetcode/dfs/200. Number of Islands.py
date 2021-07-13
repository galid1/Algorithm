# stack dfs
# def numIslands(grid):
#     n, m = len(grid), len(grid[0])
#
#     ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
#     visited = [[False for _ in range(m)] for _ in range(n)]
#
#     island_num = 0
#     for i in range(n):
#         for j in range(m):
#             if visited[i][j]:
#                 continue
#
#             if grid[i][j] == "0":
#                 continue
#
#             island_num += 1
#
#             visited[i][j] = True
#             stack = [(i, j)]
#
#             while stack:
#                 cx, cy = stack.pop()
#                 visited[cx][cy] = True
#
#                 for dx, dy in ds:
#                     nx, ny = cx+dx, cy+dy
#                     if not is_valid(n, m, nx, ny):
#                         continue
#
#                     if visited[nx][ny]:
#                         continue
#
#                     if grid[nx][ny] == "1":
#                         stack.append((nx, ny))
#
#     return island_num

# recursive dfs
def numIslands(grid):
    def dfs(i, j):
        if not is_valid(n, m, i, j) or grid[i][j] == "0":
            return

        grid[i][j] = "0"
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)

    n, m = len(grid), len(grid[0])
    island_num = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                dfs(i, j)
                island_num += 1

    print(island_num)



def is_valid(n, m, x, y):
    return 0 <= x < n and 0 <= y < m

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "1"],
    ["0", "0", "1", "0", "0"]
]
numIslands(grid)