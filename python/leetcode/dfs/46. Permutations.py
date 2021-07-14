def permute(nums):
    def dfs(cur_nums: list, cnt):
        if cnt == length:
            ans.append(cur_nums.copy())
            return

        for i in range(length):
            if visited[i]:
                continue
            visited[i] = True
            cur_nums.append(nums[i])
            dfs(cur_nums, cnt+1)
            visited[i] = False
            cur_nums.pop()


    length = len(nums)
    visited = [False for _ in range(length)]
    ans = []
    dfs([], 0)
    return ans


nums = [1,2,3]
print(permute(nums))
