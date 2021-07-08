from collections import deque

def threeSum(nums):
    # 빈 리스트 또는 3개 이하
    if len(nums) < 3:
        return []

    nums.sort()
    ans = []

    for ti in range(len(nums)-2):
        if ti > 0 and nums[ti] == nums[ti-1]:
            continue

        L, R = ti+1, len(nums)-1

        while L < R:
            sums = nums[ti] + nums[L] + nums[R]

            if sums > 0:
                R -= 1
            elif sums < 0:
                L += 1
            else:
                ans.append([nums[ti], nums[L], nums[R]])

                L, R = L+1, R-1

                while L < R and nums[L] == nums[L-1]:
                    L += 1
                while L < R and nums[R] == nums[R+1]:
                    R -= 1

    return ans


# nums = [-1,0,1,2,-1,-4]
# nums = [-1, -2, -4, 0, 1, 5, 3, 2]

threeSum(nums)