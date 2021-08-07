import sys

def solve():
    global n, sbs

    for cnt in range(1, n+1):
        dfs(cnt, 0, 0, 1, 0)


def dfs(need_cnt, selected_cnt, start_idx, cur_s, cur_b):
    global ans, n, sbs

    if need_cnt == selected_cnt:
        ans = min(ans, abs(cur_s - cur_b))
        return

    for i in range(start_idx, n):
        dfs(need_cnt, selected_cnt+1, i+1, cur_s * sbs[i][0], cur_b + sbs[i][1])


n = int(sys.stdin.readline().strip())
sbs = []
for _ in range(n):
    sbs.append(list(map(int, sys.stdin.readline().strip().split(" "))))

ans = sys.maxsize
solve()
print(ans)