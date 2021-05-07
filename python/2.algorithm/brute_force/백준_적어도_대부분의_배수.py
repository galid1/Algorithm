import sys


def solve():
    global nums

    nums.sort()

    i = nums[0]
    while True:
        if is_ans(i):
            return print(i)

        i += 1


def is_ans(target):
    global nums

    cnt = 0
    for num in nums:
        if target % num == 0:
            cnt += 1

    if cnt >= 3:
        return True
    return False




nums = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()