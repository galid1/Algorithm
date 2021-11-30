import sys


def solve():
    global n, nums

    nums.sort()

    ans = 0
    for idx, rank in enumerate(range(1, n+1)):
        ans += abs(rank - nums[idx])

    print(ans)


n = int(sys.stdin.readline().strip())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline().strip()))
solve()


# 5
# 1
# 1
# 2
# 3
# 5

