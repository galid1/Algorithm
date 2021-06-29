import sys

def solution(x, nums):
    res = []
    for num in nums:
        if num < x:
            res.append(num)

    for r in res:
        print(r, end=' ')


n, x = map(int, sys.stdin.readline().split(" "))
nums = list(map(int, sys.stdin.readline().split(" ")))
solution(x, nums)