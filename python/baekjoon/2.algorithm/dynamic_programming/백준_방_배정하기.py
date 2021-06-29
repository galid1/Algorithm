import sys


def solution():
    global a, b, c, n

    dp = [0 for i in range(301)]
    dp[a] = 1
    dp[b] = 1
    dp[c] = 1

    for i in range(1, n + 1):
        # 이미 만들 수 있는 수면 넘어감
        if dp[i]:
            continue

        if i - a > 0:
            if dp[i-a]:
                dp[i] = 1
                continue

        if i - b > 0:
            if dp[i-b]:
                dp[i] = 1
                continue

        if i - c > 0:
            if dp[i-c]:
                dp[i] = 1
                continue

    print(dp[n])


a, b, c, n = map(int, sys.stdin.readline().strip().split(" "))
solution()