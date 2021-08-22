class Solution:
    def search(self, nums, target):
        point = self.find_decrease_point(nums)
        sorted_arr = self.create_sorted_arr(nums, point)
        target_idx = self.get_target_idx(sorted_arr, target)

        if target_idx == -1:
            return -1
        return (target_idx + point)%len(nums)

    def find_decrease_point(self, nums):
        bef = nums[0]
        for i in range(1, len(nums)):
            if bef > nums[i]:
                return i
            bef = nums[i]

        return 0

    def create_sorted_arr(self, nums, point):
        if point == 0:
            return nums
        return nums[point:] + nums[0:point]

    def get_target_idx(self, sorted_arr, target):
        s, e = 0, len(sorted_arr)-1

        while s <= e:
            mid = (s+e)//2

            if sorted_arr[mid] == target:
                return mid

            if sorted_arr[mid] > target:
                e = mid-1
            else:
                s = mid+1

        return -1


s = Solution()
# nums = [4,5,6,7,0,1,2]
# nums = [5, 1, 2, 3, 4]

nums = [3, 1]
target = 3
print(s.search(nums, target))
