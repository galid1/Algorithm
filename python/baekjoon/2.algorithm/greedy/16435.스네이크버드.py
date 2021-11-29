import sys


def solve():
    global n, l, ns

    ns.sort()

    i = 0
    while i < n:
        if ns[i] > l:
            break
        l += 1
        i += 1

    print(l)


n, l = map(int, sys.stdin.readline().strip().split(" "))
ns = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()