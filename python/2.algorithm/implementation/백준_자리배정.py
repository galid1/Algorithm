import sys


def solve():
    global r, c, target, ds

    di = -1
    num = 0
    ex, ey = r, c
    x, y = 0, 1

    if target > r*c:
        return print(0)

    while True:
        di = (di+1)%4

        if di == 0 or di == 2:
            for i in range(ex):
                if num == target:
                    return print(y, x)
                x += ds[di]
                num += 1
            ey -= 1
        else:
            for i in range(ey):
                if num == target:
                    return print(y, x)
                y += ds[di]
                num += 1
            ex -= 1



ds = [1, 1, -1, -1]
c, r = map(int, sys.stdin.readline().strip().split(" "))
target = int(sys.stdin.readline().strip())
solve()