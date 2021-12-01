import sys


def solve(ax, ay, bx, by):
    global k, board, ds, ans

    if ax == bx and ay == by:
        if not is_remain():
            ans += 1
        return

    for dax, day, dbx, dby in ds:
        nax, nay, nbx, nby = ax+dax, ay+day, bx+dbx, by+dby

        if not valid(nax, nay) or not valid(nbx, nby):
            continue
        if board[nax][nay] == 0 or board[nbx][nby] == 0:
            continue

        board[ax][ay] = 0
        board[bx][by] = 0

        solve(nax, nay, nbx, nby)

        board[ax][ay] = 1
        board[bx][by] = 1


def is_remain():
    global board

    remain = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                remain += 1

    return remain > 1


def valid(x, y):
    return 0 <= x < 5 and 0 <= y < 5


k = int(sys.stdin.readline().strip())
board = [[1 for _ in range(5)] for _ in range(5)]
for _ in range(k):
    x, y = map(lambda item: int(item) - 1, sys.stdin.readline().strip().split(" "))
    board[x][y] = 0

ds = (
    (-1, 0, -1, 0), (-1, 0, 1, 0), (-1, 0, 0, -1), (-1, 0, 0, 1),
    (1, 0, -1, 0), (1, 0, 1, 0), (1, 0, 0, -1), (1, 0, 0, 1),
    (0, -1, -1, 0), (0, -1, 1, 0), (0, -1, 0, -1), (0, -1, 0, 1),
    (0, 1, -1, 0), (0, 1, 1, 0), (0, 1, 0, -1), (0, 1, 0, 1)
)
ans = 0
remain = 5*5 - k - 2
solve(0, 0, 4, 4)
print(ans)