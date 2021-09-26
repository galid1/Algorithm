import sys

def solve():
    global n

    nums.sort()
    visited = [False for _ in range(len(nums))]
    dfs([], visited)


def dfs(cur, visited):
    global n, nums, ans

    if ans:
        return

    if len(cur) == len(nums):
        result = int(''.join(cur))
        if result > n:
            ans = result
        return

    for idx in range(len(nums)):
        if visited[idx]:
            continue

        visited[idx] = True
        cur.append(nums[idx])
        dfs(cur, visited)
        cur.pop()
        visited[idx] = False


n = int(sys.stdin.readline().strip())
nums = list(str(n))

ans = 0
solve()

print(ans)