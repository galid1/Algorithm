import sys
sys.setrecursionlimit(100000)

def solve():
    global n, cs

    visited = [0 for _ in range(n+1)]
    v_idx = 0
    ans = n
    for i in range(1, n + 1):
        v_idx += 1
        if visited[i] >= 1:
            continue

        visited[i] = v_idx

        g = {i:0}
        res = dfs(i, 0, g, visited, v_idx)
        ans -= res

    print(ans)


def dfs(v, depth, g, visited, v_idx):
    global n, cs

    nv = cs[v]

    # 현재 dfs말고 이전에 방문한 적이 있음
    if visited[nv] >= 1 and visited[nv] != v_idx:
        return 0

    if nv in g.keys():
        return (depth+1) - g[nv]

    visited[nv] = v_idx
    g[nv] = depth+1

    return dfs(nv, depth+1, g, visited, v_idx)



t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline())
    cs = [0] + list(map(int, sys.stdin.readline().strip().split(" ")))
    solve()
