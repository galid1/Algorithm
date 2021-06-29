import sys


def solve():
    global a, b, c, d, e, f

    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a*x + b*y == c and d*x + e*y == f:
                return print(x, y)


a, b, c, d, e, f = map(int, sys.stdin.readline().strip().split(" "))
solve()