import sys, heapq
from collections import defaultdict


def solve():
    global n, e, es, v1, v2, INF

    # a -> v1 -> v2 -> n
    # a -> v2 -> v1 -> n
    path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
    path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)
    ans = min(path1, path2)

    if ans >= INF:
        print(-1)
    else:
        print(ans)


def dijkstra(_from, _to):
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

    return dis_arr[_to]


INF = sys.maxsize
n, e = map(int, sys.stdin.readline().strip().split(" "))
g = defaultdict(dict)

for _ in range(e):
    f, t, c = map(int, sys.stdin.readline().strip().split(" "))
    if t in g[f].keys():
        g[f][t] = min(g[f][t], c)
    else:
        g[f][t] = c

for i in range(1, n + 1):
    g[i][i] = 0

v1, v2 = map(int, sys.stdin.readline().strip().split(" "))

solve()





from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n, e = map(int, input().split())
s = [[] for i in range(n + 1)]
inf = sys.maxsize
for i in range(e):
    a, b, c = map(int, input().split())
    s[a].append([b, c])
    s[b].append([a, c])
v1, v2 = map(int, input().split())
def dijkstra(start):
    dp = [inf for i in range(n + 1)]
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        w, c = heappop(heap)
        for n_n, n_w in s[c]:
            wei = n_w + w
            if dp[n_n] > wei:
                dp[n_n] = wei
                heappush(heap, [wei, n_n])
    return dp
one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
cnt = min(one[v1] + v1_[v2] + v2_[n], one[v2] + v2_[v1] + v1_[n])
print(cnt if cnt < inf else -1)