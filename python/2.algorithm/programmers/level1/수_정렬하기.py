import sys


def solution(nums):
    nums.sort()

    for n in nums:
        print(n, end=' ')


n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))

solution(nums)

