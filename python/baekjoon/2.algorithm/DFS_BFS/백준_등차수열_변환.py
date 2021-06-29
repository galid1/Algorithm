# import sys
#
# # maximum recursive에 걸림
# def solve(diff, bef, idx, cnt):
#     global n, nums, ans
#
#     if idx == n:
#         ans = min(ans, cnt)
#         return
#
#     if diff == bef - (nums[idx] + 1):
#         solve(diff, nums[idx] + 1, idx+1, cnt+1)
#     if diff == bef - nums[idx]:
#         solve(diff, nums[idx], idx+1, cnt)
#     if diff == bef - (nums[idx] - 1):
#         solve(diff, nums[idx] - 1, idx+1, cnt+1)
#
#
# n = int(sys.stdin.readline().strip())
# nums = list(map(int, sys.stdin.readline().strip().split(" ")))
#
# if n <= 2:
#     print(0)
# else:
#     ans = sys.maxsize
#     solve((nums[0]+1) - (nums[1]+1), nums[1]+1, 2, 2)
#     solve((nums[0]+1) - nums[1], nums[1], 2, 1)
#     solve((nums[0]+1) - (nums[1]-1), nums[1]-1, 2, 2)
#
#     solve(nums[0] - (nums[1]+1), nums[1]+1, 2, 1)
#     solve(nums[0] - nums[1], nums[1], 2, 0)
#     solve(nums[0] - (nums[1]-1), nums[1]-1, 2, 1)
#
#     solve((nums[0]-1) - (nums[1]+1), nums[1]+1, 2, 2)
#     solve((nums[0]-1) - nums[1], nums[1], 2, 1)
#     solve((nums[0]-1) - (nums[1]-1), nums[1]-1, 2, 2)
#
#     if ans == sys.maxsize:
#         print(-1)
#     else:
#         print(ans)
#

import sys


def solve():
    global n, nums
    res = sys.maxsize

    if len(nums) <= 2:
        print(0)
        return

    # 차이 조합 선정(첫번째 수에 -1, 그대로, +1, 두번째 수에 -1, 그대로, +1)
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            ans = 0
            if i != 0:
                ans += 1
            if j != 0:
                ans += 1

            tmp_nums = nums.copy()
            tmp_nums[0] += i
            tmp_nums[1] += j
            diff = tmp_nums[0] - tmp_nums[1]

            success = True
            # 3번째 부터 시작해서 이전 차이와 계속 같도록 만들 수 있는지 확인
            for k in range(2, n):
                right = False
                # 3번째 부터 수에 -1, 그대로, +1을 해보면서 진행
                for l in (-1, 0, 1):
                    cur = tmp_nums[k] + l
                    cur_diff = tmp_nums[k-1] - cur
                    # 이전 차이와 현재 차이가 같은 경우 (즉, 등차)
                    if diff == cur_diff:
                        right = True
                        tmp_nums[k] = cur
                        if l != 0:
                           ans += 1

                if not right:
                    success = False
                    break

            if success:
                res = min(res, ans)

    if res == sys.maxsize:
        print(-1)
    else:
        print(res)


n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(' ')))
solve()
