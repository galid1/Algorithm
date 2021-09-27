import sys


def solve():
    global n, m, stds, ans

    for pop_cnt in range(1, m+1):
        if ans < 11:
            return

        problems = set([i for i in range(1, n+1)])
        dfs(pop_cnt, 0, problems, 0)


def dfs(pop_cnt, cnt, problems, start_idx):
    global ans, stds

    if ans < 11:
        return

    if pop_cnt == cnt:
        if not problems:
            ans = cnt
        return

    for std_idx in range(start_idx, m):
        dfs(pop_cnt, cnt+1, problems.difference(stds[std_idx]), std_idx + 1)



n, m = map(int, sys.stdin.readline().strip().split(" "))
stds = []
for _ in range(m):
    stds.append(list(map(int, sys.stdin.readline().strip().split(" ")))[1:])

ans = 11
solve()

if ans == 11:
    print(-1)
else:
    print(ans)