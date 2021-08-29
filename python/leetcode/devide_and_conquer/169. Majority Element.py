from collections import Counter

class Solution:
    # 브루트 포스 풀이
    def majorityElement(self, nums):
        cnts = Counter(nums)
        total_cnt = len(nums)
        kind_cnt = len(cnts.keys())

        ans = nums[0]
        for k, v in cnts.items():
            if v/total_cnt > 1/kind_cnt:
                return k

        return ans


s = Solution()
# nums = [3,2,3,2,1,1,2]
nums = [1]
print(s.majorityElement(nums))