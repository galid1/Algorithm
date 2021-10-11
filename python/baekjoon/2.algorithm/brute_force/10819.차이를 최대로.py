import sys


def solve(selected):
    global n, nums, ans

    result = 0
    for i in range(n-1):
        result += abs(selected[i] - selected[i+1])

    ans = max(result, ans)


def select(cur, visited):
    global n, nums

    if len(cur) == n:
        solve(cur)
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        cur.append(nums[i])
        select(cur, visited)
        cur.pop()
        visited[i] = False


n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
visited = [False for _ in range(n)]
ans = 0
select([], visited)
print(ans)