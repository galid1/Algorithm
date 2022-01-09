import sys


def solve():
    global arr, n

    dp = [0 for _ in range(n)]
    dp[-1] = 1

    max_len = 1
    for i in range(len(arr)-2, -1, -1):
        cur_max_len = 0
        for j in range(i, len(arr)):
            if arr[i] >= arr[j]:
                continue
            cur_max_len = max(cur_max_len, dp[j])

        dp[i] = cur_max_len + 1
        max_len = max(max_len, dp[i])

    print(max_len)


n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()