import sys


def solve():
    global n

    for i in range(n):
        for j in range(i+1):
            print("*", end='')
        print()


n = int(sys.stdin.readline())
solve()