import sys


def solve():
    global n, board, dp

    ans = 0

    for i in range(n):
        for j in range(n):
            visited[i][j] = True
            res = dfs(i, j, 1)
            visited[i][j] = False
            dp[i][j] = res
            ans = max(ans, res)

    print(ans)


def dfs(x, y, depth):
    global ds, dp, board, visited

    max_depth = depth

    for dx, dy in ds:
        nx, ny = x+dx, y+dy

        if not valid(nx, ny):
            continue

        if visited[nx][ny]:
            continue

        if board[x][y] >= board[nx][ny]:
            continue

        if dp[nx][ny] > 0:
            max_depth = max(max_depth, depth + dp[nx][ny])
            continue

        visited[nx][ny] = True
        max_depth = max(max_depth, dfs(nx, ny, depth+1))
        visited[nx][ny] = False

    dp[x][y] = max_depth - depth + 1
    return max_depth


def valid(x, y):
    global n
    return 0 <= x < n and 0 <= y < n


ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]

n = int(sys.stdin.readline().strip())
dp = [[-1 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

solve()