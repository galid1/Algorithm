import sys


def solve():
    global n

    for i in range(1, n+1):
        print(i)


n = int(sys.stdin.readline().strip())
solve()