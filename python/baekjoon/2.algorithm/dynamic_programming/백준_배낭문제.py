# https://gsmesie692.tistory.com/113
import sys


def solution():
    global w, v, k
    dp = [[0 for _ in range(k + 1)] for _ in range(len(items))]
    for item_idx in range(0, len(items)):
        for weight_idx in range(0, k + 1):
            if weight_idx >= items[item_idx][0]:
                dp[item_idx][weight_idx] = max(dp[item_idx - 1][weight_idx], dp[item_idx - 1][weight_idx - items[item_idx][0]] + items[item_idx][1])
            else:
                dp[item_idx][weight_idx] = dp[item_idx - 1][weight_idx]

    print(dp[len(items) - 1][k])


n, k = map(int, sys.stdin.readline().strip().split(" "))
items = []
for i in range(n):
    w, v = map(int, sys.stdin.readline().strip().split(" "))
    items.append((w, v))
solution()
