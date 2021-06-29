import sys

def solve():
    global n, nums

    cur_idx = 0
    cur_num = 1
    ans = []
    stack = []

    while cur_idx < n:
        if cur_num <= nums[cur_idx]:
            stack.append(cur_num)
            cur_num += 1
            ans.append('+')
            continue

        if stack[-1] > nums[cur_idx]:
            return print('NO')

        while stack and cur_idx < n and stack[-1] == nums[cur_idx]:
            stack.pop()
            cur_idx += 1
            ans.append('-')

    for a in ans:
        print(a)


n = int(sys.stdin.readline().strip())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline().strip()))

solve()