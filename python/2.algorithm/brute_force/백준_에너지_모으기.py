import sys


def solution(nums, sums):
    global max_num

    if len(nums) == 2:
        max_num = max(max_num, sums)
        return

    t_nums = nums.copy()
    # 첫 원소, 마지막 원소 제외
    for i in range(1, len(t_nums) - 1):
        t_sums = sums + (t_nums[i-1] * t_nums[i+1])
        pop_num = t_nums.pop(i)
        solution(t_nums, t_sums)
        t_nums.insert(i, pop_num)


max_num = 0
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split(" ")))
solution(arr, 0)
print(max_num)