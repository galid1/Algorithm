import sys

def solve():
    global n, m, target, ds

    if target > n*m:
        return print(0)

    ex, ey = n, m
    x, y = 0, 1
    di = -1
    num = 0
    while True:
        di = (di + 1)%4
        if di == 0 or di == 2:
            for i in range(ex):
                num += 1
                x += ds[di][0]
                if num == target:
                    return print(y, x)
            ey -= 1
        else:
            for i in range(ey):
                num += 1
                y += ds[di][1]
                if num == target:
                    return print(y, x)
            ex -= 1


ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
m, n = map(int, sys.stdin.readline().strip().split(" "))
target = int(sys.stdin.readline().strip())
solve()
