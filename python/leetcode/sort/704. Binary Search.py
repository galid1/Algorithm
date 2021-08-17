class Solution:
    def search(self, nums, target):
        s, e = 0, len(nums)-1

        while s <= e:
            mid = (s+e)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid - 1
            else:
                s = mid + 1

        return -1



s = Solution()
# nums = [-1,0,3,5,9,12]
# target = 9
# target = -1

nums = [-1,0,3,5,9,12]
target = 2
print(s.search(nums, target))
