import sys
sys.setrecursionlimit(100000)


def solve(x, y):
    global n, m, board, dp, ds

    if not valid(x, y):
        return -1

    if dp[x][y] > -1:
        return dp[x][y]

    if x == n-1 and y == m-1:
        return board[x][y]

    max_cnt = 0
    for dx, dy in ds:
        nx, ny = x+dx, y+dy
        max_cnt = max(max_cnt, solve(nx, ny))

    dp[x][y] = max_cnt + board[x][y]
    return dp[x][y]


def valid(x, y):
    global n, m
    return 0 <= x < n and 0 <= y < m


ds = [[0, 1], [1, 0], [1, 1]]
n, m = map(int, sys.stdin.readline().strip().split(" "))
dp = [[-1 for _ in range(m)] for _ in range(n)]
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve(0, 0)
print(dp[0][0])
# 3 4
# 1 2 3 4
# 0 0 0 5
# 9 8 7 6