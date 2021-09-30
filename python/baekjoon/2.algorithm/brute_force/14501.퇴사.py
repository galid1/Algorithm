import sys


def solve(ct, cp):
    global n, schedules, ans

    if ct >= n:
        ans = max(ans, cp)
        return

    solve(ct+1, cp)

    t, p = schedules[ct]
    nt = ct + t
    if nt <= n:
        solve(ct+t, cp+p)


n = int(sys.stdin.readline().strip())
schedules = []
for _ in range(n):
    schedules.append(list(map(int, sys.stdin.readline().strip().split(" "))))

ans = 0
solve(0, 0)
print(ans)