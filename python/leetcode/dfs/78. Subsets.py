def subsets(nums):
    def dfs(cur_nums:list, cur_idx, cnt):
        ans.append(cur_nums.copy())

        for i in range(cur_idx, length):
            cur_nums.append(nums[i])
            dfs(cur_nums, i+1, cnt+1)
            cur_nums.pop()

    ans = []
    length = len(nums)
    dfs([], 0, 0)

    return ans

nums = [1,2,3]
print(subsets(nums))
