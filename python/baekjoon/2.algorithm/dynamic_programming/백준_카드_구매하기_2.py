import sys


def solve():
    global n, ps

    d = [0 for i in range(n+1)]

    for i in range(n+1):
        res = ps[i]
        for j in range(1, i//2+1):
            res = min(res, d[i-j] + d[j])
        d[i] = res

    print(d[n])


n = int(sys.stdin.readline().strip())
ps = [0] + list(map(int, sys.stdin.readline().strip().split(" ")))
solve()