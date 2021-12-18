import sys


def solve(n, _from, _to):
    global cnt, res, dp

    if n > 20 and dp[n] > 0:
        return dp[n]

    if n == 1:
        res.append((_from, _to))
        return 1

    _transfer = 6 - _from - _to
    r1 = solve(n-1, _from, _transfer)
    dp[n-1] = r1

    r2 = solve(1, _from, _to)
    r3 = solve(n-1, _transfer, _to)

    return r1 + r2 + r3


n = int(sys.stdin.readline().strip())
cnt, res = 0, []
dp = [0 for _ in range(101)]
print(solve(n, 1, 3))

if n <= 20:
    for ft in res:
        print(*ft)