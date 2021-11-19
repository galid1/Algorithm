import sys


def solve(n):
    global dp
    print(dp[n][0], dp[n][1])


def init():
    dp = [[0, 0] for _ in range(41)]
    dp[0][0] = 1
    dp[1][1] = 1

    for i in range(2, 41):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

    return dp


t = int(sys.stdin.readline().strip())
dp = init()
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    solve(n)
