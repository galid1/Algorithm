import sys


def solution(s):
    result = []
    v = [0 for i in range(len(s))]

    dfs(result, v, s, [], 0)

    for res in result:
        print(res)
    print("")

def dfs(result, v, s, nums, start_idx):
    if len(nums) == 6:
        semi_res = ' '.join(nums)
        result.append(semi_res)
        return

    for i in range(start_idx, len(s)):
        if not v[i]:
            v[i] = 1
            nums.append(s[i])
            dfs(result, v, s, nums, i+1)
            nums.pop()
            v[i] = 0


while True:
    nums = list(sys.stdin.readline().strip().split(" "))
    if nums[0] == '0':
        break

    s = nums[1:]
    solution(s)