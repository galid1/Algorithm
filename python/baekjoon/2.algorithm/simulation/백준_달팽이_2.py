import sys


def solve():
    global n, m, d

    ans = 0
    cur_direction = 0
    yc = m
    xc = n - 1

    num = n * m + 1
    turn = 'y'

    # 현재 좌표
    cx, cy = 0, -1
    while num > 1:
        end = yc if turn == 'y' else xc

        for i in range(end):
            cx += d[cur_direction][0]
            cy += d[cur_direction][1]
            num -= 1

        if turn == 'y':
            turn = 'x'
            yc -= 1
        else:
            turn = 'y'
            xc -= 1
        ans += 1

    print(ans - 1)


def switching_direction(cur_direction):
    return (cur_direction + 1) % 4


n, m = map(int, sys.stdin.readline().strip().split(" "))
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
solve()
