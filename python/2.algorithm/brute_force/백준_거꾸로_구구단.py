import sys


def solve():
    global n, k

    mnum = 0
    for i in range(1, k+1):
        mnum = max(mnum, int(str(n*i)[-1::-1]))

    print(mnum)


n, k = map(int, sys.stdin.readline().strip().split(" "))
solve()
