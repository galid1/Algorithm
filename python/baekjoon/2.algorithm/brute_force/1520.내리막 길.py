import sys


def solve(x, y):
    global n, m, board, d, ds

    if x == m - 1 and y == n - 1:
        return 1

    if d[x][y] >= 0:
        return d[x][y]

    d[x][y] = 0
    for dx, dy in ds:
        nx, ny = dx+x, dy+y

        if not valid(nx, ny):
            continue

        if board[nx][ny] >= board[x][y]:
            continue

        d[x][y] += solve(nx, ny)

    return d[x][y]


def valid(x, y):
    global n, m

    return 0 <= x < n and 0 <= y < m


n, m = map(int, sys.stdin.readline().strip().split(' '))

board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split(" "))))

d = [[-1 for _ in range(m)] for _ in range(n)]
d[n-1][m-1] = 1
ds = [[-1, 0], [1, 0], [0, -1], [0, 1]]

print(solve(0, 0))