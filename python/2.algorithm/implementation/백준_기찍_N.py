import sys


def solve():
    global n

    for i in range(n, 0, -1):
        print(i)


n = int(sys.stdin.readline().strip())
solve()