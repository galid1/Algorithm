import sys


def solve():
    global n, gs

    gs = sorted(gs, key=lambda item: item[0])

    a, b = gs[0][0], gs[0][1]
    ans = 1

    for ca, cb in gs[1:]:
        if ca < a:
            ans += 1
            a = ca
        elif cb < b:
            ans += 1
            b = cb

    print(ans)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    gs = []
    for _ in range(n):
        gs.append(list(map(int, sys.stdin.readline().strip().split(" "))))

    solve()