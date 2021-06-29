import sys

def solution(nums):
    nums.sort()
    for num in nums:
        print(num)


n = int(sys.stdin.readline())
nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline()))
solution(nums)