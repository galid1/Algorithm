import sys


def dfs(start, res):
    global nums, visit

    if len(res) == 7:
        if sum(res) == 100:
            for r in res:
                print(r)

        return

    for i in range(start, len(nums)):
        if not visit[i]:
            visit[i] = 1
            res.append(nums[i])
            dfs(i+1, res)
            visit[i] = 0
            res.pop()


nums = []
for i in range(9):
    nums.append(int(sys.stdin.readline()))
visit = [0 for i in range(len(nums))]

dfs(0, [])