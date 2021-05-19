import sys


def solve():
    global n

    print(n*(n+1)//2)


n = int(sys.stdin.readline().strip())
solve()