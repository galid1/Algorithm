class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num

        return result