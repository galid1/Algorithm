# import sys
#
#
# def solve():
#     global n, m, board, ds, dp
#
#     result = dfs(0, 0, 1, [(0, 0)])
#     print(result)
#
#
# def dfs(i, j, depth, paths):
#     global dp, board
#
#     max_depth = depth
#
#     for dx, dy in ds:
#         num = int(board[i][j])
#         nx, ny = i + (num * dx), j + (num * dy)
#
#         if not valid(nx, ny):
#             continue
#
#         if board[nx][ny] == "H":
#             continue
#
#         if (nx, ny) in paths:
#             return -1
#
#         history = dp[nx][ny]
#         if history > 0:
#             max_depth = max(max_depth, history)
#             continue
#
#         paths.append((nx, ny))
#         result = dfs(nx, ny, depth+1, paths)
#         paths.pop()
#
#         if result == -1:
#             return -1
#         else:
#             max_depth = max(max_depth, result)
#
#     dp[i][j] = max_depth - depth
#     return max_depth
#
#


import sys
sys.setrecursionlimit(100000)


def dfs(i, j):
    global board, dp, visited

    if not valid(i, j):
        return 0
    if board[i][j] == "H":
        return 0
    if visited[i][j]:
        return -1
    if dp[i][j] > 0:
        return dp[i][j]

    visited[i][j] = True
    jump = int(board[i][j])
    for dx, dy in ds:
        nx, ny = i + (dx * jump), j + (dy * jump)
        result = dfs(nx, ny)
        if result == -1:
            return -1

        dp[i][j] = max(dp[i][j], result + 1)
    visited[i][j] = False

    return dp[i][j]


def valid(x, y):
    global n, m
    return 0 <= x < n and 0 <= y < m


ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]
n, m = map(int, sys.stdin.readline().strip().split(" "))
board = []
dp = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))

visited = [[False for _ in range(m)] for _ in range(n)]
result = dfs(0, 0)

if result == -1:
    print(-1)
else:
    print(dp[0][0])