def arrayPairSum(nums):
    nums.sort()

    ans = 0
    for i in range(0, len(nums)-1, 2):
        ans += min(nums[i], nums[i+1])

    print(ans)

# nums = [1, 4, 3, 2]
# nums = [6,2,6,5,1,2]
nums = [-5, -3, 1, 2]
arrayPairSum(nums)