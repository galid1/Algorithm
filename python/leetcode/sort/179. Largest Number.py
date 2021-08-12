class Solution:
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        nums.sort(reverse=True)

        return str(int(''.join(self.custom_sort(nums))))

    def custom_sort(self, nums):
        for i in range(1, len(nums)):
            compared = nums[i]
            for j in range(i-1, -2, -1):
                if self.smallThanCompared(compared, nums[j]):
                    nums[j+1] = nums[j]
                else:
                    break
            nums[j+1] = compared

        return nums

    def smallThanCompared(self, compared, comparator):
        return int(compared+comparator) > int(comparator+compared)

s = Solution()
nums = [0, 0]
print(s.largestNumber(nums))