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
        idx = 0
        while idx < len(compared) and idx < len(comparator):
            if compared[idx] > comparator[idx]:
                return True
            elif comparator[idx] > compared[idx]:
                return False
            idx += 1

        # compared가 더 긴 경우
        if len(compared) > len(comparator):
            comparator = comparator[idx - 1]
            while idx < len(compared):
                if compared[idx] > comparator:
                    return True
                elif comparator > compared[idx]:
                    return False
                idx += 1

        else:
            compared = compared[idx - 1]
            while idx < len(comparator):
                if comparator[idx] > compared:
                    return False
                elif compared > comparator[idx]:
                    return True
                idx += 1

        return True

s = Solution()
nums = [3,30,34,5,9]
print(s.largestNumber(nums))