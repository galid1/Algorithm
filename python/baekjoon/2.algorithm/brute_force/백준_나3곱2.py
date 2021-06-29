import sys

def solve(cur, visited):
    global n, nums

    if len(cur) == n:
        for c in cur:
            print(c, end=' ')
        exit()
        return

    for i in range(n):
        if not visited[i]:
            if len(cur) == 0:
                visited[i] = True
                cur.append(nums[i])
                solve(cur, visited)
                visited[i] = False
                cur.pop()
                continue

            if (cur[-1] % 3 == 0 and cur[-1] // 3 == nums[i]) or cur[-1] * 2 == nums[i]:
                visited[i] = True
                cur.append(nums[i])
                solve(cur, visited)
                visited[i] = False
                cur.pop()


n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))
solve([], [False for _ in range(n)])