import sys


# diffsum을 구하고, 더 작으면 갱신
# 더작으면 갱신하다가, 더 커지는 순간 이전 diff_sum 출력

def solve():
    global n, nums

    nums.sort()
    #
    # min_num, min_dsum = nums[0], 0
    # found = False
    # for i in range(1, len(nums)):
    #     min_dsum += abs(min_num - nums[i])
    #
    # for i in range(1, len(nums)):
    #     dsum = 0
    #     cur_num = nums[i]
    #     for j in range(len(nums)):
    #         if i == j:
    #             continue
    #
    #         dsum += abs(cur_num - nums[j])
    #     print("====")
    #     print("cur : ", cur_num, dsum)
    #     if dsum < min_dsum:
    #         found = True
    #         min_num, min_dsum = cur_num, dsum
    #     elif found and dsum >= min_dsum:
    #         continue

    if n%2 == 0:
        print(nums[n//2-1])
    else:
        print(nums[n//2])

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()