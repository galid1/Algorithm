import sys


def solve():
    global a, b

    nums = []

    for i in range(1, b+1):
        for j in range(i):
            nums.append(i)

    print(sum(nums[a-1:b]))


a, b = map(int, sys.stdin.readline().strip().split(" "))
solve()
