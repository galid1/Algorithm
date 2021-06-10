import sys

def solve():
    global n, nums

    d = [0 for _ in range(n+1)]
    d[1] = nums[1]

    for i in range(2, n+1):
        d[i] = max(nums[i], d[i-1] + nums[i])

    print(max(d[1:]))



t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    nums = [0] + list(map(int, sys.stdin.readline().strip().split(" ")))
    solve()


# 1
# 5
# -1 -2 -3 -4 -5