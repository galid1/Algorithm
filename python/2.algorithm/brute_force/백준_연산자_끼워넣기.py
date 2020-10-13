import sys


def solution(nums, operators, res, idx):
    global max_num, min_num

    if idx == len(nums) - 1:
        max_num = max(max_num, res)
        min_num = min(min_num, res)

    for j in range(4):
        if operators[j]:
            operators[j] -= 1
            solution(nums, operators, operate(j, res, nums[idx + 1]), idx + 1)
            operators[j] += 1


def operate(operator, num1, num2):
    if operator == 0:
        return num1 + num2
    elif operator == 1:
        return num1 - num2
    elif operator == 2:
        return num1 * num2
    else:
        return int(num1/num2)


max_num = -1e9
min_num = 1e9
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(" ")))
operators = list(map(int, sys.stdin.readline().split(" ")))
solution(nums, operators, nums[0], 0)

print(max_num)
print(min_num)

# N = int(input())
# nums = list(map(int, input().split()))
# add, sub, mul, div = map(int, input().split())
#
# min_, max_ = 1e9, -1e9
#
# def dfs(i, res, add, sub, mul, div):
#     global max_, min_
#     if i == N:
#         max_ = max(res, max_)
#         min_ = min(res, min_)
#         return
#
#     else:
#         if add:
#             dfs(i+1, res+nums[i], add-1, sub, mul, div)
#         if sub:
#             dfs(i+1, res-nums[i], add, sub-1, mul, div)
#         if mul:
#             dfs(i+1, res*nums[i], add, sub, mul-1, div)
#         if div:
#             dfs(i+1, int(res/nums[i]), add, sub, mul, div-1)
#
# dfs(1, nums[0], add, sub, mul, div)
# print(max_)
# print(min_)