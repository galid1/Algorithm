import sys


def solve():
    global n, hs

    l = 1
    mh = hs[0]
    # 왼 -> 오
    for i in range(1, n):
        if hs[i] > mh:
            l += 1
            mh = hs[i]

    r = 1
    mh = hs[-1]
    # 오 -> 왼
    for j in range(n-2, -1, -1):
        if hs[j] > mh:
            r += 1
            mh = hs[j]

    print(l)
    print(r)


n = int(sys.stdin.readline().strip())
hs = []
for _ in range(n):
    hs.append(int(sys.stdin.readline().strip()))
solve()