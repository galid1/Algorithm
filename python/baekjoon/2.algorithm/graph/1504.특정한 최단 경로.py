import sys, heapq
from collections import defaultdict


def solve():
    global n, e, es, v1, v2, INF

    # a -> v1 -> v2 -> n
    # a -> v2 -> v1 -> n
    one = dijkstra(1)
    v1_ = dijkstra(v1)
    v2_ = dijkstra(v2)
    path1 = one[v1] + v1_[v2] + v2_[n]
    path2 = one[v2] + v2_[v1] + v1_[n]
    ans = min(path1, path2)

    if ans >= INF:
        print(-1)
    else:
        print(ans)


def dijkstra(_from):
    global n, g, INF

    dis_arr = [INF for _ in range(n+1)]
    dis_arr[_from] = 0
    visited = [False for _ in range(n+1)]
    visited[_from] = True

    q = []
    for dest, w in g[_from].items():
        heapq.heappush(q, (w, dest))

    while q:
        w, dest = heapq.heappop(q)

        if visited[dest]:
            continue

        visited[dest] = True
        dis_arr[dest] = w

        for n_dest, n_w in g[dest].items():
            if visited[n_dest]:
                continue

            heapq.heappush(q, (w + n_w, n_dest))

    return dis_arr


INF = sys.maxsize
n, e = map(int, sys.stdin.readline().strip().split(" "))
g = defaultdict(dict)

for _ in range(e):
    f, t, c = map(int, sys.stdin.readline().strip().split(" "))
    if t in g[f].keys():
        g[f][t] = min(g[f][t], c)
        g[t][f] = min(g[t][f], c)
    else:
        g[f][t] = c
        g[t][f] = c

for i in range(1, n + 1):
    g[i][i] = 0

v1, v2 = map(int, sys.stdin.readline().strip().split(" "))

solve()