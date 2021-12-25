import sys


def solve():
    global cmds

    y, x = 0, 0
    d = 0

    for cmd, meta in cmds:
        if cmd == "TURN":
            # 왼쪽 회전
            if int(meta) == 0:
                d = (d - 1) % 4
            # 오른쪽 회전
            else:
                d = (d + 1) % 4

        else:
            move_cnt = int(meta)

            ny, nx = y + (ds[d][0] * move_cnt), x + (ds[d][1] * move_cnt)
            if not valid(ny, nx):
                return print(-1)

            y, x = ny, nx


    print(x, y)


def valid(x, y):
    global m

    return 0 <= x < m and 0 <= y < m


m, n = map(int, sys.stdin.readline().strip().split(" "))
ds = [[0, 1], [-1, 0], [0, -1], [1, 0]]
cmds = []

for _ in range(n):
    cmds.append(sys.stdin.readline().strip().split(" "))

solve()