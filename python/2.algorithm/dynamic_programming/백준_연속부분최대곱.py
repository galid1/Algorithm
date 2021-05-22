import sys


def solve():
    global n, nums

    d = [0 for _ in range(n)]
    d[0] = nums[0]

    for i in range(1, len(nums)):
        d[i] = max(d[i-1] * nums[i], nums[i])

    print("%.3f" %(max(d)))


n = int(sys.stdin.readline().strip())
nums = []

for _ in range(n):
    nums.append(float(sys.stdin.readline().strip()))

solve()
