def subsets(nums):
    def dfs(k, cur_nums:list, cur_idx, cnt):
        if cnt == k:
            ans.append(cur_nums.copy())
            return

        for i in range(cur_idx, length):
            cur_nums.append(nums[i])
            dfs(k, cur_nums, i+1, cnt+1)
            cur_nums.pop()

    ans = []
    length = len(nums)
    for k in range(0, length+1):
        dfs(k, [], 0, 0)

    return ans

nums = [1,2,3]
print(subsets(nums))
