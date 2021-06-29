import sys


def solve():
    global n, nums

    for i in range(1, len(nums)):
        if nums[i] != 0:
            for j in range(nums[i]):
                print(i)


n = int(sys.stdin.readline().strip())
nums = [0 for _ in range(10001)]
for _ in range(n):
    nums[int(sys.stdin.readline())] += 1
solve()

# 1 1 2 2 3 3 4 5 7
