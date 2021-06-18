import sys


def solve():
    global n, nums

    decreasing = [1 for _ in range(n)]
    increasing = [1 for _ in range(n)]

    for i in range(1, n):
        # 증가하는 수열
        if nums[i] >= nums[i-1]:
            increasing[i] = increasing[i-1] + 1

        if nums[i] <= nums[i-1]:
            decreasing[i] = decreasing[i-1] + 1

    max_de = max(decreasing)
    max_in = max(increasing)

    print(max(max_de, max_in))



n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()