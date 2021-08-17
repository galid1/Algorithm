class Solution:
    def sortColors(self, nums):
        i, j, k = 0, 0, len(nums)-1
        mid = 1

        while j <= k:
            if nums[j] > mid:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1

            elif nums[j] < mid:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i+1, j+1

            else:
                j += 1

        return nums

s = Solution()
nums = [2,0,2,1,1,0,1,1,2,]
print(s.sortColors(nums))


