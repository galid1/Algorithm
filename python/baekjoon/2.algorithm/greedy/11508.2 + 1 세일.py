import sys


def solve():
    global gs

    gs.sort()
    ans = 0

    while gs:
        ans += gs.pop()

        if not gs:
            break
        ans += gs.pop()

        if not gs:
            break
        gs.pop()

    print(ans)



n = int(sys.stdin.readline().strip())
gs = []
for _ in range(n):
    gs.append(int(sys.stdin.readline().strip()))

solve()