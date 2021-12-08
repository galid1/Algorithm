import sys

def solve(x, y):
    global n, board, ds

    if x == n-1 and y == n-1:
        return 1

    cnt = 0
    mul = board[x][y]

    if mul == 0:
        return 0

    for dx, dy in ds:
        nx, ny = x + dx * mul, y + dy * mul

        if not valid(nx, ny):
            continue

        if dp[nx][ny] > 0:
            cnt += dp[nx][ny]
        else:
            cnt += solve(nx, ny)

    dp[x][y] = cnt
    return dp[x][y]


def valid(x, y):
    global n
    return 0 <= x < n and 0 <= y < n



n = int(sys.stdin.readline().strip())
ds = ((1, 0), (0, 1))
dp = [[0 for _ in range(n)] for _ in range(n)]
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))
solve(0, 0)

print(dp[0][0])
