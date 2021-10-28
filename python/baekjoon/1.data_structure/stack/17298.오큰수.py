import sys


def solve():
    global n, nums

    ans = [-1]
    stack = [nums[-1]]
    for i in range(len(nums) - 2, -1, -1):
        okn_exist = False
        while stack:
            if stack[-1] > nums[i]:
                ans.append(stack[-1])
                okn_exist = True
                break
            else:
                stack.pop()

        if not okn_exist:
            ans.append(-1)

        stack.append(nums[i])


    for i in range(len(ans) - 1, -1, -1):
        print(ans[i], end=' ')


n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()