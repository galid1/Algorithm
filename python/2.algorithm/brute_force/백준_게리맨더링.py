import sys


def solve(fir_cnt, selected_fir, idx):
    global n, ps, g, ans, zones

    if len(selected_fir) == fir_cnt:
        selected_sec = list(zones.difference(selected_fir))

        if is_valid(selected_fir) and is_valid(selected_sec):
            ans = min(ans, abs(get_ps(selected_fir) - get_ps(selected_sec)))
        return

    for i in range(idx, n):
        selected_fir.append(i)
        solve(fir_cnt, selected_fir, i+1)
        selected_fir.pop()


def is_valid(zones):
    global g, n

    visited = [True for _ in range(n+1)]
    for zone in zones:
        visited[zone] = False

    stack = [zones[0]]
    visited[zones[0]] = True

    while stack:
        ci = stack.pop()

        for i in range(1, n+1):
            # 연결 되어 있고 방문 x
            if g[ci][i] and not visited[i]:
                stack.append(i)
                visited[i] = True

    if False in visited:
        return False

    return True


def get_ps(zones):
    global ps

    res = 0
    for zone in zones:
        res += ps[zone]

    return res


n = int(sys.stdin.readline().strip())
ps = [0] + list(map(int, sys.stdin.readline().strip().split(" ")))
g = [[False for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for link in list(map(int, sys.stdin.readline().strip().split(" ")))[1:]:
        g[i][link] = True
        g[link][i] = True

ans = 1001
zones = {i for i in range(1, n+1)}
# 1번째 선거구의 구역 수
for i in range(1, n):
    solve(i, [], 1)

if ans == 1001:
    print(-1)
else:
    print(ans)