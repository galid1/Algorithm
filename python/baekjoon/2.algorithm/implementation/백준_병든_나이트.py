import sys


def solve():
    global n, m

    if n == 1:
        return print(1)

    if n == 2:
        return print(min((m+1)//2, 4))

    if n >= 3:
        if m < 7:
            return print(min(4, m))

        if m >= 7:
            return print(m-2)

n, m = map(int, sys.stdin.readline().strip().split(" "))
solve()