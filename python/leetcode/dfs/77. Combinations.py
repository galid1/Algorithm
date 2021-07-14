# def combine(n: int, k: int):
#     def dfs(nums, cur_num: list, cnt):
#         if cnt == k:
#             ans.append(nums.copy())
#             return
#
#         for i in range(cur_num+1, n+1):
#             nums.append(i)
#             dfs(nums, i, cnt+1)
#             nums.pop()
#
#     ans = []
#     for i in range(1, n+1):
#         dfs([i], i, 1)
#     return ans


def combine(n: int, k: int):
    def dfs(cur_num, nums:list, cnt):
        if cnt == k:
            ans.append(nums.copy())
            return

        for i in range(cur_num, n+1):
            nums.append(i)
            dfs(i+1, nums, cnt+1)
            nums.pop()

    ans = []
    dfs(1, [], 0)
    return ans

print(combine(4, 2))
