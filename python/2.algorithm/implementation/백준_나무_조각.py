import sys


def solve():
    global nums

    for i in range(4, -1, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                print(*nums)


nums = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()