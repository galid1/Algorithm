# sort 이용
# class Solution:
#     def findKthLargest(self, nums, k: int) -> int:
#         nums.sort(reverse=True)
#         return nums[k-1]


# heal이용
import heapq

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)

        while k > 1:
            k -= 1
            heapq.heappop(heap)

        return -heapq.heappop(heap)


nums =  [3,2,1,5,6,4]
k = 2
# nums = [3,2,3,1,2,4,5,5,6]
# k = 4
s = Solution()
print(s.findKthLargest(nums, k))