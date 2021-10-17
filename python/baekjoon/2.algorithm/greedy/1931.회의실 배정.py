import sys


def solve():
    global n, ms

    ms = sorted(ms, key = lambda item: (item[1], item[0]))

    ce = 0
    ans = 0
    for s, e in ms:
        if s >= ce:
           ans += 1
           ce = e

    print(ans)


n = int(sys.stdin.readline().strip())
ms = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().strip().split(" "))
    ms.append([s, e])

solve()