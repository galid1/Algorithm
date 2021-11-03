import sys


def solve():
    global n, nums

    nums.sort()

    sums = 0

    for i in range(n):
        if sums + 1 >= nums[i]:
            sums += nums[i]
        else:
            break

    print(sums+1)


n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()