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

    def recursive(self, nums, target):
        def binary(s, e):
            if s <= e:
                mid = (s+e)//2
                if nums[mid] == target:
                    return mid

                if nums[mid] > target:
                    return binary(s, mid-1)
                else:
                    return binary(mid+1, e)
            else:
                return -1

        return binary(0, len(nums)-1)




s = Solution()
# nums = [-1,0,3,5,9,12]
# target = 9
# target = -1

nums = [-1,0,3,5,9,12]
target = 2
print(s.recursive(nums, target))
