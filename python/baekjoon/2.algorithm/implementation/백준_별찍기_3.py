import sys


def solve():
    global n

    for i in range(n):
        for j in range(n-i):
            print("*", end='')
        print()



n = int(sys.stdin.readline().strip())
solve()