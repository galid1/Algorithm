import sys


def solve():
    global n, ps, ds, directions, visited, ans

    def dfs(cx, cy, n, cur_percent):
        global ans

        if n == 0:
            ans += cur_percent
            return

        for i in range(4):
            next_percent = cur_percent * ps[i]
            nx, ny = cx + ds[i][0], cy + ds[i][1]

            if not valid(nx, ny) or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            dfs(nx, ny, n-1, next_percent)
            visited[nx][ny] = False

    cx, cy = 14, 14
    visited[cx][cy] = True
    dfs(cx, cy, n, 1)

    print(ans)


def valid(x, y):
    return 0 <= x < 29 and 0 <= y < 29


# 입력
visited = [[False for _ in range(29)] for _ in range(29)]
ans = 0
n, ep, wp, sp, np = map(int, sys.stdin.readline().strip().split(" "))
ds = [[0, 1], [0, -1], [1, 0], [-1, 0]]
ps = [ep*0.01, wp*0.01, sp*0.01, np*0.01]

solve()

