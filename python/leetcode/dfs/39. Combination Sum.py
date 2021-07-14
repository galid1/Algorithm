def combinationSum(candidates, target: int):
    def dfs(cur_idx, nums:list, sums:int):
        if sums >= target:
            if sums == target:
                ans.append(nums.copy())
            return

        for i in range(cur_idx, length):
            cur_num = candidates[i]
            nums.append(cur_num)
            dfs(i, nums, sums+cur_num)
            nums.pop()

    ans = []
    length = len(candidates)
    dfs(0, [], 0)

    return ans


# candidates = [2, 3, 6, 7]
# target = 7
# candidates = [2, 3, 5]
# target = 8
candidates = [2]
target = 1
print(combinationSum(candidates, target))