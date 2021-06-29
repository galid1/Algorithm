import sys

def solve():
    global n

    for i in range(n):
        for j in range(i):
            print(' ', end='')
        for j in range(n-i + n-i - 1):
            print('*', end='')

        print()


n = int(sys.stdin.readline().strip())
solve()