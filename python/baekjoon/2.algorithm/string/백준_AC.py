import sys
from collections import deque


def solve():
    global ps, n, nums

    # 0 == (정방향), 1 == (뒤집힌 뒤)
    di = 0

    for p in ps:
        if p == 'R':
            di = (di+1)%2
            continue

        if len(nums) == 0:
            return print("error")

        if di == 0:
            nums.popleft()
        else:
            nums.pop()

    res = '['
    # 정
    if di == 0:
        for i in range(len(nums)):
            res += nums[i]
            if i < len(nums) - 1:
                res += ','
        res += ']'
    # 뒤집
    else:
        for i in range(len(nums)-1, -1, -1):
            res += nums[i]
            if i > 0:
                res += ','
        res += ']'

    print(res)


t = int(sys.stdin.readline().strip())
for _ in range(t):
    ps = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    nums = sys.stdin.readline().strip()
    nums = nums[1:-1]
    nums = deque(list(nums.split(","))) if nums else deque()
    solve()


# 4
# RDD
# 4
# [1,2,3,4]
#
#
# 3
# DD
# 1
# [42]
# RRD
# 6
# [1,1,2,3,5,8]
# D
# 0
# []


# 1
# D
# 0
# []