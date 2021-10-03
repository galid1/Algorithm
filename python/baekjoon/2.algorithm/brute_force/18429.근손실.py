import sys


def solve(cur_day, cur_muscle):
    global n, k, kits, visited, ans

    if cur_day == n:
        ans += 1
        return

    for i in range(n):
        if visited[i]:
            continue

        if cur_muscle + kits[i] - k < 500:
            continue

        visited[i] = True
        solve(cur_day + 1, cur_muscle + kits[i] - k)
        visited[i] = False


n, k = map(int, sys.stdin.readline().strip().split(" "))
kits = list(map(int, sys.stdin.readline().strip().split(" ")))
visited = [False for _ in range(n)]
ans = 0
solve(0, 500)
print(ans)