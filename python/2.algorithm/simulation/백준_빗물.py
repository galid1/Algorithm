import sys


def solve():
    global n, m, hs

    ans = 0
    for i in range(1, m):
        l = find_left(i)
        r = find_right(i)

        ans += max(0, min(l, r) - hs[i])

    print(ans)


def find_left(si):
    global hs

    l = hs[si]
    for i in range(si - 1, -1, -1):
        if hs[i] > l:
            l = hs[i]
    return l


def find_right(si):
    global hs

    r = hs[si]
    for i in range(si+1, m):
        if hs[i] > r:
            r = hs[i]

    return r


n, m = map(int, sys.stdin.readline().strip().split(" "))
hs = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()

# 4 4
# 3 0 1 4