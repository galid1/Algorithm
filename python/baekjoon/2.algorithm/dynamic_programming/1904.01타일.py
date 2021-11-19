import sys


def solve():
    global n

    dp = [0, 1, 2]

    for i in range(3, n+1):
        dp.append((dp[i-1] + dp[i-2]) % 15746)

    print(dp[n])


n = int(sys.stdin.readline().strip())
solve()