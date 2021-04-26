import sys

def solve():
    global n, nums

    stack = []

    for i in range(len(nums)):
        if not stack:
            stack.append(i)
            continue

        if nums[stack[-1]] >= nums[i]:
            if i < len(nums):
                stack.append(i)
                continue

            while stack:
                idx = stack.pop()
                nums[idx] = -1

        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            nums[idx] = nums[i]
        stack.append(i)

    while stack:
        idx = stack.pop()
        nums[idx] = -1

    # 정답
    for num in nums:
        print(num, end=' ')



n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
solve()


# 12
# 10 9 8 5 4 7 8 9 10 11 10 9